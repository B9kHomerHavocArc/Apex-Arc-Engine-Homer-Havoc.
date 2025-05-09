import unittest
from unittest.mock import patch
from data_fetcher import get_team_rosters, get_daily_lineups, get_statcast_data, scrape_mlb_lineups, verify_lineup

class TestDataFetcher(unittest.TestCase):
    @patch('data_fetcher.statsapi.lookup_team')
    def test_get_team_rosters(self, mock_lookup_team):
        """Test fetching team rosters."""
        mock_lookup_team.return_value = [{'id': 147, 'name': 'New York Yankees'}]
        with patch('data_fetcher.statsapi.get') as mock_get:
            mock
