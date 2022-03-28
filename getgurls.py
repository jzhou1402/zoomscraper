"""Perform a Google search using Selenium and a headless Chrome browser."""
import subprocess
import nltk
from pathlib import Path

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

out2 = open("webinfo2.csv", "w")

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

    stopwords = ["i", "me", "my", "myself", "all", "get", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    for i in file1:
        out2.write(i)
        driver.implicitly_wait(1)
        driver.get("https://www.google.com")
        driver.implicitly_wait(1)
        
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input_element.send_keys(i)  
        print("reached results")
        driver.implicitly_wait(1)
        try: 
            driver.find_element(By.TAG_NAME, "cite").click()
            resp = driver.find_element(By.XPATH, "//body").get_attribute('outerHTML')
            soup = BeautifulSoup(resp, 'html.parser')
            text = soup.find_all(text=True)
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()

            # get text
            text = soup.get_text()
            #break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk if chunk.isalnum)
            #get each word in lowercase
            word = "" 
            for i in text:
                if i == ' ' or i == '\n':
                    if len(word) >= 3 and word.isalpha():
                        if word not in stopwords: 
                            out2.write(word.lower())
                            out2.write(", ")
                    word = ""
                else:
                    word += i

            out2.write('\n')
        except:
            out2.write("not found\n")

    driver.quit()

    # Print search results, ignoring non-standard search results which lack
    # text, like "Videos" or "People also ask".
    

    # Cleanup

test_selenium_hello()
