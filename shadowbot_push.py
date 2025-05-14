
import requests
import datetime

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1357263895068282900/foGZtlcmcC0PvbkDOkORV2C67JGh3xg1FO6SZgq9rok7OKI3h1FdBwnPgZnnneUSvsSt"

# Construct message
today = datetime.datetime.now().strftime("%Y-%m-%d")
message = {
    "username": "ShadowBot",
    "embeds": [
        {
            "title": f"Apex Arc Engine | Daily Simulation Update",
            "color": 11141290,
            "fields": [
                {"name": "Date", "value": today, "inline": True},
                {"name": "Tier Version", "value": "Tier 53.0", "inline": True},
                {"name": "Top 100 Output", "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/apex_top100_may3.csv)", "inline": False},
                {"name": "Parlay Stacks", "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/parlay_stacks_may3.csv)", "inline": False},
                {"name": "Diagnostics", "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/diagnostic_overlay.csv)", "inline": False}
            ],
            "footer": {"text": "Posted by Apex ShadowBot"}
        }
    ]
}

# Send the alert
response = requests.post(WEBHOOK_URL, json=message)

# Check response
if response.status_code == 204:
    print("ShadowBot alert sent successfully.")
else:
    print(f"Failed to send alert: {response.status_code} — {response.text}")
