from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set up the driver (make sure the correct path to your webdriver is provided)
driver = webdriver.Chrome()

try:
    # Get the path to the HTML file in the same folder as the script
    html_file_path = os.path.join(os.path.dirname(__file__), 'sample.html')  # Update to your actual HTML filename
    driver.get(f'file:///{html_file_path}')  # Load the HTML file

    # Wait until the specific row is present
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    row_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td/a")))
    #row_element = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]")))

    #row_element = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[contains(@class, 'link-list-item')]")))

    # Extract data from the row
    ###################################################################################
    # if row_element:
    #     webpage_links = row_element.find_elements(By.TAG_NAME,"a")
    #     if webpage_links:
    #         print(webpage_links[0].get_attribute('href'))
    ###################################################################################
    # title = row_element.find_element(By.XPATH, ".//th").text.strip()
    # link = row_element.find_element(By.XPATH, ".//td/a").get_attribute("href").strip()
    #
    # print(f"Webpage Title: {title}")
    # print(f"Webpage Link: {link}")
    ###################################################################################
    # webpage_anchor = row_element.find_element(By.TAG_NAME,'a')
    # webpage_link = webpage_anchor.get_attribute('href') if webpage_anchor else None
    # print(webpage_link)
    ###################################################################################
    # Get the href attribute directly from the located <a> element
    webpage_link = row_element.get_attribute('href')
    print(webpage_link)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()



############################################################################################## sample.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Webpage</title>
</head>
<body>
    <div>
        <div>
            <div>
                <div>
                    <section>
                        <div>
                            <div>
                                <table>
                                    <tbody>
                                        <tr class="link-list-item">
                                            <th class="link-list-head">
                                                <span class="link-list-icon-wrapper">
                                                    <img src="https://cdn.coderanking.com/assets/98df5a15d59786d48cc6abc848bc1407.svg" loading="lazy" alt="" class="link-list-icon">
                                                </span>
                                                Webpage
                                            </th>
                                            <td class="link-list-value">
                                                <a href="https://ethereum.org" target="_blank" rel="noopener nofollow" class="link-list-link">
                                                    ethereum.org
                                                </a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
