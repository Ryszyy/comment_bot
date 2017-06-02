import re
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait

def get_comment():
	word_list = []
    #raw data
    source_code = requests.get(url)
    #convert to text
    plain_text = source_code.text
    #lxml format
    soup = BeautifulSoup(plain_text,'lxml')

    #find the words in paragraph tag
    for text in soup.findAll('p'):
        if text.text is None:
            continue
        #content
        content = text.text
        #lowercase and split into an array
        words = content.lower().split()

        #for each word
        for word in words:
            #remove non-chars
            cleaned_word = clean_word(word)
            #if there is still something there
            if len(cleaned_word) > 0:
                #add it to our word list
                word_list.append(cleaned_word)

    return word_list

def wait_and_find(driver, element, text=None):
	while True:
		try:
			found = driver.find_element_by_xpath(element)
			found.send_keys(text)
			break
		except Exception as e:
			print(e)
			time.sleep(1)
			continue


if __name__ == "__main__":
	get_comment()
