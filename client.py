# Official Python Wrapper for LinkedIn & Google Jobs Scraper + Automatic B2B Company Email Enricher (willowy_catamaran_fco/google-linkedin-jobs-scraper)
import os
import json
import urllib.request

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/willowy_catamaran_fco~google-linkedin-jobs-scraper/run-sync-get-dataset-items?token=" + APIFY_TOKEN

def run_extraction(payload: dict) -> list[dict]:
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    sample_payload = {
    "query": "AI Engineer",
    "location": "United Kingdom",
    "maxItems": 25
}
    print("Triggering willowy_catamaran_fco/google-linkedin-jobs-scraper...")
    print(json.dumps(run_extraction(sample_payload), indent=2))
