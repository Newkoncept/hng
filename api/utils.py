from datetime import datetime, timezone
import json
import requests


def get_latest_timestamp():

    # get current datetime in UTC
    dt = datetime.now(timezone.utc)
    return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")


# def get_latest_cat_fact():
#     url = "https://catfact.ninja/fact"

#     try:

#         response = requests.get(url=url, timeout=2)

#         if response.status_code == 200:
#             # json_response = json.loads(response.content)
#             json_response = response.json()

#             if "fact" in json_response.keys():
#                 return json_response["fact"]
#             elif "message" in json_response.keys():
#                 return json_response["message"]
#             else:
#                 return "Error from api"
#         else:
#             return f"Api failed with status code- {response.status_code}"
#     except requests.exceptions.RequestException as e:
#         return f"Error with api request - {e}"



# import requests

def get_latest_cat_fact():
    FALLBACK_MESSAGE = "Cat fact unavailable at this time"
    # url = "https://catfact.ninja/fact"
    # url = "https://google.com/"
    # url = "https://httpstat.us/404"
    url = "https://reqres.in/api/users "

    try:
        response = requests.get(url, timeout=(1, 2))
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            # Not JSON? Return a snippet of raw text.
            return FALLBACK_MESSAGE
            # return f"Unexpected response format: {response.text[:100]}"

        # Only handle dict responses safely
        if isinstance(data, dict):
            return data.get("fact") or data.get("message") or "Unexpected API response"
        else:
            # Handle weird responses like lists or strings
            # return f"Unexpected data type: {type(data).__name__}"
            return FALLBACK_MESSAGE

    except requests.exceptions.Timeout:
        return FALLBACK_MESSAGE
        # return "The request timed out."
    except requests.exceptions.HTTPError as e:
        return FALLBACK_MESSAGE
        # return f"HTTP error: {e}"
    except requests.exceptions.RequestException as e:
        return FALLBACK_MESSAGE
        # return f"Network error: {e}"
