import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}

URL = "https://www.sitetoscrap.com/"
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Filter the links to only keep those that start with the URL
filtered_links = [link for link in links if link['href'].startswith(URL)]

# Store the scraped data in a list
data = []

# Scrape the data for each filtered link
for link in filtered_links:
    URL = link['href']
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the relevant data from the page and store it in the data list
    # You can modify the following code to extract the data you need
    page_title = soup.title.string
    page_body = soup.get_text()
    data.append({'title': page_title, 'body': page_body})

for item in data:
    print("Uploading data:", item)
