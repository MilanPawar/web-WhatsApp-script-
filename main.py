from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the Edge WebDriver executable
edge_driver_path = 'path_to_edge_driver_executable'

# Initialize the Edge browser with additional capabilities
options = webdriver.EdgeOptions()
options.use_chromium = True  # Use Chromium-based Edge
options.add_argument('--start-maximized')  # Maximize the browser window
options.add_argument('--disable-notifications')  # Disable notifications
options.add_argument('--disable-infobars')  # Disable infobars
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable logging

# Initialize the Edge browser with specified options
driver = webdriver.Edge(executable_path=edge_driver_path, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')
print("WhatsApp Web opened. Please scan the QR code.")

# Wait for the user to scan the QR code and login
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')))
print("Logged in successfully.")

# Find the chat input field
chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

# Type and send the message
chat_input.send_keys("Hello from Selenium!")
chat_input.send_keys(Keys.ENTER)

# Wait for a few seconds to see the message sent
time.sleep(5)

# Close the browser
driver.quit()
