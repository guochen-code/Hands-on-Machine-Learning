'''
Example 1: <div> is a child of <button>
html
Copy code
<button>
    <div class="small-text">Main 2 Games</div>
</button>
First Snippet: Works fine, because the <div> is a descendant of the <button>.
Second Snippet: Works fine as well, since the <div> is a direct child.
  
Example 2: <div> is a descendant (not a direct child)
html
Copy code
<button>
    <span>
        <div class="small-text">Main 2 Games</div>
    </span>
</button>
First Snippet: Works perfectly, as it looks for any descendant <div> of the <button>.
Second Snippet: Fails, because the <div> is not a direct child of the <button>.

Example 3: <div> is outside the <button>
html
Copy code
<div>
    <button>Click me!</button>
    <div class="small-text">Main 2 Games</div>
</div>
First Snippet: Fails, as the <div> is not a descendant of the <button>.
Second Snippet: Fails as well, since there’s no <div> within the <button>.

Example 4: Multiple <div> siblings
html
Copy code
<button>
    <div class="small-text">Main 2 Games</div>
    <div>Another Text</div>
</button>
Both Snippets: Both will work, as the <div class="small-text"> is a direct child of the <button>.
Summary:
Use the first snippet (.//div) for scenarios where the <div> might be nested at any level within the <button>.
Use the second snippet (div) when you are sure that the <div> is directly inside the <button>.
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Set Firefox options for headless browsing
firefox_options = Options()
firefox_options.headless = True


# Initialize the driver
driver = webdriver.Firefox(options=firefox_options)


try:
    # Navigate to the website
    driver.get("https://bluecollardfs.com/nba-optimizer")


    # Wait until the "DraftKings" button is available
    wait = WebDriverWait(driver, 10)
    draftkings_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'DraftKings')]")))


    # Click on the "DraftKings" button
    draftkings_button.click()


    # Wait until the "Main 2 Games" button is available
    main_2_games_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//div[contains(@class, 'small-text') and contains(text(), 'Main 2 Games')]]")
    ))


    # Click the "Main 2 Games" button
    main_2_games_button.click()


    # Wait for the player data tab to load and be visible
    players_tab = wait.until(EC.visibility_of_element_located((By.ID, "players")))


    # Wait to ensure that the data is fully loaded
    time.sleep(2)  # Optional: Adjust this sleep as necessary


    # Get the full page source
    page_source = driver.page_source


    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')


    # Find the div containing the player data
    player_data_div = soup.find("div", {"id": "players", "class": "tab-pane fade active show"})


    # Print the data found inside the player_data_div
    if player_data_div:
        print(player_data_div.prettify())
    else:
        print("Player data div not found")


finally:
    # Close the WebDriver
    driver.quit()




