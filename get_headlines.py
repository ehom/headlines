import json
import requests
import os

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


def main():
    data = fetch(URL)
    save_to_file(data)


if __name__ == "__main__":
    main()
