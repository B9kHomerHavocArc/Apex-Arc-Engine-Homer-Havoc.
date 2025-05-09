from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_fetcher import get_team_rosters, get_daily_lineups, get_statcast_data
from bvp_spider import scrape_bvp_data
from prediction_model import predict_hr_probabilities
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

default_args = {
    'owner': 'apex_arc',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'homer_havoc_pipeline',
    default_args=default_args,
    description='Daily MLB HR Prediction Pipeline',
    schedule_interval='0 8 * * *',  # Run daily at 8 AM
    start_date=datetime(2025, 5, 9),
    catchup=False,
) as dag:
    
    def fetch_rosters_task():
        """Fetch and cache team rosters."""
        rosters = get_team_rosters()
        logging.info(f"Fetched rosters for {len(rosters)} teams")
        return rosters
    
    def fetch_lineups_task():
        """Fetch and cache daily lineups."""
        lineups = get_daily_lineups()
        logging.info(f"Fetched lineups for {len(lineups)} games")
        return lineups
    
    def fetch_bvp_task(**context):
        """Fetch BvP data for players in lineups."""
        lineups = context['task_instance'].xcom_pull(task_ids='fetch_lineups')
        bvp_data = {}
        for game, teams in lineups.items():
            for player in teams['home'] + teams['away']:
                bvp_data[player] = scrape_bvp_data(player, 'Unknown Pitcher')  # Placeholder pitcher
        logging.info(f"Fetched BvP data for {len(bvp_data)} players")
        return bvp_data
    
    def fetch_statcast_task(**context):
        """Fetch Statcast data for players in lineups."""
        lineups = context['task_instance'].xcom_pull(task_ids='fetch_lineups')
        statcast_data = {}
        for game, teams in lineups.items():
            for player in teams['home'] + teams['away']:
                statcast_data[player] = get_statcast_data(player)
        logging.info(f"Fetched Statcast data for {len(statcast_data)} players")
        return statcast_data
    
    def predict_task(**context):
        """Generate HR predictions."""
        lineups = context['task_instance'].xcom_pull(task_ids='fetch_lineups')
        statcast_data = context['task_instance'].xcom_pull(task_ids='fetch_statcast')
        bvp_data = context['task_instance'].xcom_pull(task_ids='fetch_bvp')
        predictions = {}
        for game, teams in lineups.items():
            lineup = teams['home'] + teams['away']
            venue = game.split(' vs ')[0]  # Simplified: home team as venue
            predictions[game] = predict_hr_probabilities(lineup, statcast_data, bvp_data, venue)
        logging.info(f"Generated predictions for {len(predictions)} games")
        return predictions
    
    roster_task = PythonOperator(
