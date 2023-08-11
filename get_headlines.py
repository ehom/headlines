import json
import requests
import os
import datetime

API_KEY = os.environ["NEWS_API_ORG_API_KEY"]
COUNTRY_CODE = "us"
OUTPUT_FILENAME = "headlines.json"

URL = f"https://newsapi.org/v2/top-headlines?country={COUNTRY_CODE}&apiKey={API_KEY}"


def fetch(url):
    print("fetch")
    response = requests.get(URL)

    if response.status_code == 200:
        # st.write(response.json())
        data = response.json()
    else:
        st.error(f"status_code: {response.status_code}")
    return data


def save_to_file(data):
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def timestamp():
    # Get the current date and time
    current_datetime = datetime.datetime.utcnow()

    # Format the datetime as an ISO 8601 string
    iso_formatted = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

    return iso_formatted


def main():
    data = fetch(URL)
    if data['status'] == "ok":
        data['generatedAt'] = timestamp()

    save_to_file(data)


if __name__ == "__main__":
    main()
