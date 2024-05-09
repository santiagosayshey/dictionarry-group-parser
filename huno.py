import requests
import json
import re

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('HONE_API')


# Set the base URL for the API
base_url = "https://hawke.uno/api"

# Set the search endpoint
search_endpoint = "/torrents/filter"

# Set the search parameters
search_params = {
    "name": "hone 2160p",
    "sortField": "created_at",
    "sortDirection": "asc",
    "perPage": 45000
}

# Set the headers for the request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Construct the full URL for the search request
search_url = base_url + search_endpoint

try:
    # Send the search request
    response = requests.get(search_url, params=search_params, headers=headers)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

    # Parse the JSON response
    data = response.json()

    # Extract the relevant information from the response
    torrents = data["data"]

    # Open the file in write mode
    with open("hone.txt", "w") as file:
        for torrent in torrents:
            attributes = torrent["attributes"]
            title = attributes["name"]
            category = attributes["category"]
            download_link = attributes["download_link"]

            # Write the torrent information to the file
            file.write(f"Torrent: {title}\n")

    print("Torrent information has been saved to hone.txt.")

    # Count the occurrences of release groups
    release_groups = {}
    with open("hone.txt", "r") as file:
        for line in file:
            match = re.search(r"- ([^)]+)\)$", line)
            if match:
                release_group = match.group(1)
                release_group = re.sub(r"\([^)]*\)", "", release_group).strip()
                release_groups[release_group] = release_groups.get(release_group, 0) + 1

    print("\nRelease Group Counts:")
    for group, count in release_groups.items():
        print(f"{group}: {count}")

except requests.exceptions.RequestException as e:
    print("Error occurred while making the request:", e)

except (KeyError, ValueError) as e:
    print("Error occurred while parsing the response:", e)