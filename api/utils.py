from datetime import datetime, timezone
import requests


def get_latest_timestamp():
    # get current datetime in UTC
    dt = datetime.now(timezone.utc)
    return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def get_latest_cat_fact():
    FALLBACK_MESSAGE = "Cat fact unavailable at this time"
    url = "https://catfact.ninja/fact"

    try:
        response = requests.get(url, timeout=(1, 2))
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            # Not JSON? Return a snippet of raw text.
            return FALLBACK_MESSAGE

        # Only handle dict responses safely
        if isinstance(data, dict):
            return data.get("fact") or data.get("message") or "Unexpected API response"
        else:
            # Handle weird responses like lists or strings
            return FALLBACK_MESSAGE

    except requests.exceptions.Timeout:
        return FALLBACK_MESSAGE
    except requests.exceptions.HTTPError as e:
        return FALLBACK_MESSAGE
    except requests.exceptions.RequestException as e:
        return FALLBACK_MESSAGE
