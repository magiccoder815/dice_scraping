from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Base URL
url = "https://dice.fm/browse/southampton-58aeb28a30b3996024da53e0"
driver.get(url)

# Give the page some time to load
time.sleep(5)  # Adjust as necessary

# Find all event cards
event_cards = driver.find_elements(By.CLASS_NAME, 'EventCard__Event-sc-5ea8797e-1')

# Initialize lists to store data
event_names = []
event_links = []
event_prices = []

# Loop through the event cards and extract information
for event_card in event_cards:
    event_link = event_card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    event_name = event_card.find_element(By.CLASS_NAME, 'styles__Title-sc-4cc6fa9-6').text
    event_price = event_card.find_element(By.CLASS_NAME, 'styles__Price-sc-4cc6fa9-9').text

    # Append data to lists
    event_names.append(event_name)
    event_links.append(event_link)
    event_prices.append(event_price)

# Close the driver
driver.quit()

# Create a DataFrame
data = {
    "Event Name": event_names,
    "Event Link": event_links,
    "Event Price": event_prices
}
df = pd.DataFrame(data)

# Save DataFrame to an Excel file
df.to_excel("event_data.xlsx", index=False)

print("Data saved to event_data.xlsx")