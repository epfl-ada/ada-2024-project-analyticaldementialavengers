import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://en.wikipedia.org/wiki/Timeline_of_the_20th_century'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
else:
    print(f"Successfully retrieved page!")

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Focus on the main content section (the timeline events are within mw-content-text)
content_div = soup.find('div', {'id': 'mw-content-text'})

if not content_div:
    print("Main content not found!")
else:
    # Open a CSV file to write the data
    with open('20th_century_events.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Event Description'])  # CSV headers

        current_date = None  # This will store the current decade or year
        stop_parsing = False  # Flag to stop parsing irrelevant sections at the bottom

        # Start finding the event and the associated dates within the main content only
        for section in content_div.find_all(['h2', 'h3', 'p', 'ul']):
            # Stop parsing if we reach sections like "See also" or "References"
            if 'See also' in section.text or 'References' in section.text:
                stop_parsing = True
            if stop_parsing:
                break

            # Debug: Print the section to check what's being processed
            print(f"Processing section: {section.name} -> {section.text.strip()}")

            # Extract potential decade or specific year from headings (like <h2>, <h3>, etc.)
            if section.name in ['h2', 'h3']:
                heading_text = section.text.strip()
                if any(char.isdigit() for char in heading_text):  # Filter out headings with numbers (years, decades)
                    current_date = heading_text.split("[")[0].strip()  # Remove references like [1] and strip whitespace
                    # Debug: Print the current date being processed
                    print(f"Found date/decade: {current_date}")
            
            # Extract the description from unordered lists (<ul><li>)
            elif section.name == 'ul':  # Events are often listed in bullet points
                for li in section.find_all('li'):
                    event_description = li.text.strip()

                    # Debug: Print the event description being processed
                    print(f"Found event: {event_description}")

                    # If the event contains a full date (day, month, year) at the start
                    if current_date and event_description:
                        # Try to extract full dates (day, month, year) from the event description
                        event_date = None
                        if ',' in event_description:  # Detect the presence of a comma which usually separates the date
                            parts = event_description.split(',', 1)  # Split only on the first comma
                            if len(parts) == 2:
                                event_date = parts[0].strip()  # Full date part (e.g., "January 1, 1900")
                                event_description = parts[1].strip()  # Event description without the date
                        # Fall back to the year/decade if no full date was found
                        if not event_date:
                            event_date = current_date

                        # Write to CSV and Debug the data being written
                        writer.writerow([event_date, event_description])
                        print(f"Writing to CSV: Date - {event_date}, Description - {event_description}")

# make pandas dataframe

import pandas as pd

df = pd.read_csv('20th_century_events.csv')
print(df.head())



