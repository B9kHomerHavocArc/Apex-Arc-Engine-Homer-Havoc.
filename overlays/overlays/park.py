import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_park_factor(venue):
    """
    Retrieve park factor for a venue.
    Returns a dictionary with venue and HR factor.
    Placeholder: Replace with MLB.com or FanGraphs data.
    """
    try:
        # Static park factors for 2025 venues
        park_factors = {
            'Sutter Health Park': 1.00,  # Neutral for Athletics
            'C
