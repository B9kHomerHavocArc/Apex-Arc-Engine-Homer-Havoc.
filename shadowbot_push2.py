
import requests
import datetime

# Discord webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1357263895068282900/foGZtlcmcC0PvbkDOkORV2C67JGh3xg1FO6SZgq9rok7OKI3h1FdBwnPgZnnneUSvsSt"

# Dynamic date
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Message payload with dynamic filenames
message = {
    "username": "ShadowBot",
    "embeds": [
        {
            "title": "Apex Arc Engine | Daily Simulation Update",
            "color": 11141290,
            "fields": [
                {"name": "Date", "value": today, "inline": True},
                {"name": "Tier Version", "value": "Tier 53.0", "inline": True},
                {
                    "name": "Top 100 Output",
                    "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/apex_top100_2025-05-03.csv)",
                    "inline": False
                },
                {
                    "name": "Parlay Stacks",
                    "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/parlay_stacks_2025-05-03.csv)",
                    "inline": False
                },
                {
                    "name": "Diagnostics",
                    "value": "[Download](https://github.com/HomerHavoc/Apex_Arc_Engine/blob/main/data/output/diagnostic_overlay_2025-05-03.csv)",
                    "inline": False
                }
            ],
            "footer": {"text": "Posted by Apex ShadowBot"}
        }
    ]
}

# POST to Discord
response = requests.post(WEBHOOK_URL, json=message)
if response.status_code == 204:
    print("ShadowBot alert sent.")
else:
    print(f"Error posting to Discord: {response.status_code}")
