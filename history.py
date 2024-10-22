import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://en.wikipedia.org/wiki/Timeline_of_the_20th_century'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Open a CSV file to write the data
with open('20th_century_events.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Event Description'])  # CSV headers

    current_date = None  # This will store the current decade or year as we parse through sections

    # Start finding the event and the associated dates (typically in <h2>, <h3>, etc.)
    for section in soup.find_all(['h2', 'h3', 'p', 'ul']):
        # Extract potential decade or specific year from headings (like <h2>, <h3>, etc.)
        if section.name in ['h2', 'h3']:
            heading_text = section.text.strip()
            if any(char.isdigit() for char in heading_text):  # Filter out headings with numbers (years, decades)
                current_date = heading_text.split("[")[0].strip()  # Remove references like [1] and strip whitespace
        # Extract the description from paragraphs or list items (<ul><li>)
        elif section.name == 'ul':  # Events are often listed in bullet points
            for li in section.find_all('li'):
                event_description = li.text.strip()
                if current_date and event_description:
                    writer.writerow([current_date, event_description])  # Write to CSV file


