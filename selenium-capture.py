from selenium import webdriver

url = "http://www.naver.com/"

# Extract PhantomJS driver.
browser = webdriver.PhantomJS()
# Wait for 3 seconds.
browser.implicitly_wait(3)
# Read URL.
browser.get(url)
# Capture and save the screen.
browser.save_screenshot("Website.png")
# Exit the browser.
browser.quit()