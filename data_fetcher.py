import statsapi
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pybaseball import statcast, playerid_lookup
from redis import Redis
import pandas as pd
import logging
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
redis_client = Redis(host='localhost', port=6379, db=0)
ua = UserAgent()

def get_team_rosters(date='2025-05-09'):
    """Fetch active rosters for all MLB teams with overrides."""
    cache_key = f"rosters:{date}"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    try:
        teams = statsapi.lookup_team('')
        rosters = {}
        for team in teams:
            team_id = team['id']
            try:
                roster = statsapi.get('team_roster', {'teamId': team_id, 'rosterType': 'active', 'date': date})
                rosters[team['name']] = [player['person']['fullName'] for player in roster['roster']]
                if team['name'] == 'New York Mets':
                    rosters[team['name']].append('Juan Soto')
                if team['name'] == 'New York Yankees':
                    rosters[team['name']].append('Cody Bellinger')
            except Exception as e:
                logging.error(f"Failed to fetch roster for {team['name']}: {e}")
                rosters[team['name']] = []
        redis_client.setex(cache_key, 900, json.dumps(rosters))
        return rosters
    except Exception as e:
        logging.error(f"Failed to fetch teams: {e}")
        return {}

def get_daily_lineups(date='2025-05-09'):
    """Fetch confirmed lineups for the daily slate."""
    cache_key = f"lineups:{date}"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    try:
        schedule = statsapi.schedule(start_date=date, end_date=date)
        lineups = {}
        for game in schedule:
            game_id = game['game_id']
            try:
                game_data = statsapi.get('game', {'gamePk': game_id})
                home_team = game_data['gameData']['teams']['home']['name']
                away_team = game_data['gameData']['teams']['away']['name']
                try:
                    home_lineup = [p['fullName'] for p in game_data['liveData']['lineups']['homePlayers']]
                    away_lineup = [p['fullName'] for p in game_data['liveData']['lineups']['awayPlayers']]
                    lineups[f"{home_team} vs {away_team}"] = {'home': home_lineup, 'away': away_lineup}
                except KeyError:
                    logging.warning(f"Lineups not available for {home_team} vs {away_team}")
                    lineups[f"{home_team} vs {away_team}"] = {'home': [], 'away': []}
            except Exception as e:
                logging.error(f"Failed to fetch game {game_id}: {e}")
        redis_client.setex(cache_key, 900, json.dumps(lineups))
        return lineups
    except Exception as e:
        logging.error(f"Failed to fetch schedule: {e}")
        return {}

def scrape_mlb_lineups(date='2025-05-09'):
    """Scrape lineups from MLB.com for verification."""
    url = f"https://www.mlb.com/gameday/{date.replace('-',
