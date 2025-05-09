# Apex Arc Engine - Homer Havoc

A Python-based system to predict MLB home run (HR) probabilities for the daily slate, focusing on May 9, 2025 (e.g., Yankees @ Athletics). Uses **MLB-StatsAPI**, web scraping, and a Streamlit web app with weather and park factor adjustments.

## Features
- Fetches team rosters and lineups with overrides (e.g., Juan Soto = Mets, Cody Bellinger = Yankees).
- Scrapes batter-versus-pitcher (BvP) data and Statcast metrics.
- Adjusts predictions based on weather (e.g., wind speed) and park factors (e.g., Yankee Stadium HR-friendliness).
- Displays predictions in a Streamlit app with tiers (Ghost, Hidden Flame) and badges (Black Flame).
- Automates data fetching and predictions using Apache Airflow.

## Project Structure
