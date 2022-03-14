"""Perform a Google search using Selenium and a headless Chrome browser."""
import subprocess
from pathlib import Path

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def test_selenium_hello():
    """Perform a Google search using Selenium and a headless Chrome browser."""

    # Configure Selenium
    #
    # Pro-tip: remove the "headless" option and set a breakpoint.  A Chrome
    # browser window will open, and you can play with it using the developer
    # console.
    options = selenium.webdriver.chrome.options.Options()
    options.add_argument("--headless")

    # chromedriver is not in the PATH, so we need to provide selenium with
    # a full path to the executable.
    node_modules_bin = subprocess.run(
        ["npm", "bin"],
        stdout=subprocess.PIPE,
        universal_newlines=True,
        check=True
    )
    node_modules_bin_path = node_modules_bin.stdout.strip()
    chromedriver_path = Path(node_modules_bin_path) / "chromedriver"

    # An implicit wait tells WebDriver to poll the DOM for a certain amount of
    # time when trying to find any element (or elements) not immediately
    # available. Once set, the implicit wait lasts for the life of the
    # WebDriver object.
    #
    # https://selenium-python.readthedocs.io/waits.html#implicit-waits

    file1 = open('input.txt', 'r')
    out = open("urls.txt", "w")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    for i in file1:
        driver.implicitly_wait(1)
        driver.get("https://www.google.com")
        driver.implicitly_wait(1)
        
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input_element.send_keys(i)  
        print("reached results")
        driver.implicitly_wait(1)
        results = driver.find_element(By.XPATH, '//div[@class="g"]//a//h3')
        soup = BeautifulSoup(results)
        href_tags = soup.find_all(href=True)
        for i in href_tags:
            print(i)

    driver.quit()

    # Print search results, ignoring non-standard search results which lack
    # text, like "Videos" or "People also ask".
    

    # Cleanup

test_selenium_hello()