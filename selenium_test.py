from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver service
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment this line to run in headless mode
options.add_argument('--no-sandbox')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the web page
    driver.get("")  # Ensure this URL is correct

    # Wait until the title contains the expected text (max wait: 10 seconds)
    WebDriverWait(driver, 10).until(EC.title_contains("Simple Form Validation"))

    # Print the actual page title for debugging
    print("Page Title:", driver.title)

    # Assert the page title contains the expected text
    assert "Simple Form Validation" in driver.title, "Title assertion failed!"

    # Take a screenshot (for debugging purposes)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = f"screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved: {screenshot_file}")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the WebDriver properly
    driver.quit()
