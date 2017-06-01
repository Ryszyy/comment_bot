import re
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
# from rake_nltk import Rake
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_comment():
	# # driver = webdriver.PhantomJS('/usr/bin/phantomjs')
	# driver = webdriver.Chrome()
	# url = sys.argv[1]
	# driver.get(url)
	# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# time.sleep(3)
	# while True:
	# 	try:
	# 		driver.find_element_by_id("comment-section-renderer-items")
	# 		break
	# 	except:
	# 		time.sleep(3)
	# 		continue

	# comments = ""
	# for item in driver.find_elements_by_class_name("comment-renderer-text-content"):
	# 	comments = comments + item.text
	# 	# print(item.text)
	# 	# print("-" * 80)
	# driver.close()
	# # print(comments)

	# r = Rake()
	# r.extract_keywords_from_text(comments)
	# half =len(r.get_ranked_phrases())/2
	# keywords_list = r.get_ranked_phrases()[:int(half)]
	# print(keywords_list)
	driver = webdriver.Chrome()
	driver.get('https://www.youtube.com/')
	youtube_username = "commentator951@gmail.com"
	youtube_password = "comment951"
	'//input[@type="email"]'
	signin_button_class = 'signin-container '
	username_id = 'identifierId'
	'''
<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0" aria-label="Email or phone" name="identifier" id="identifierId" dir="ltr" data-initial-dir="ltr" data-initial-value="" badinput="false">
	'''


if __name__ == "__main__":
	get_comment()