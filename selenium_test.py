
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set the correct ChromeDriver path (Update if needed)
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"  # Use 'which chromedriver' to check path

# Setup Chrome WebDriver
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()

# Add arguments for running in a CI/CD or headless environment
options.add_argument("--headless")  # Remove this for debugging
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=service, options=options)
    print("✅ WebDriver initialized successfully!")

    # Open the web page
    TEST_URL = "https://github.com/AmanCreates/cicd.git"
    driver.get(TEST_URL)
    print(f"🔗 Opened URL: {TEST_URL}")

    # Wait until the page title contains expected text
    WebDriverWait(driver, 10).until(EC.title_contains("Simple Form Validation"))

    # Print actual page title for debugging
    actual_title = driver.title
    print(f"📄 Page Title: {actual_title}")

    # Assert condition
    assert "Simple Form Validation" in actual_title, f"❌ Title mismatch: {actual_title}"

    # Take a screenshot for verification
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = f"screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_file)
    print(f"📸 Screenshot saved: {screenshot_file}")

except Exception as e:
    print(f"🚨 Test failed: {str(e)}")

finally:
    # Ensure proper WebDriver closure
    driver.quit()
    print("✅ WebDriver closed successfully.")
