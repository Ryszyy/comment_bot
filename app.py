from flask import Flask
from flask import request
from flask import render_template
import random
import re
import sys
import time
from selenium import webdriver
from rake_nltk import Rake

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET','POST'])
def main():
    context = {
        "msg":"Enter url of the youtube site"
    }
    if request.method == 'POST':
        u = request.form['site_url']
        context["url"]=u

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(u)
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(3)
        while True:
            try:
                driver.find_element_by_id("comment-section-renderer-items")
                break
            except:
                time.sleep(1)
                continue

        comments_rake = ""
        comments = []
        for item in driver.find_elements_by_class_name("comment-renderer-text-content"):
            comments_rake = comments_rake + item.text
            comments.append(item.text)
        # print(item.text)
        # print("-" * 80)
        driver.close()
    # print(comments)

        r = Rake()
        r.extract_keywords_from_text(comments_rake)
        half =len(r.get_ranked_phrases())/3
        keywords_list = r.get_ranked_phrases()[:int(half)]
        print(keywords_list)
        context['keywords'] = keywords_list
        context['comments'] = comments
        your = random.choice(keywords_list)
        context['your'] = your

        return render_template('comments.html', context=context)

    return render_template('index.html', context=context)


@app.route("/send", methods=['GET','POST'])
def send():
    msg = "Thank you!"
    context = {}
    # context['msg'] = msg
    if request.method == 'POST':
        url = request.form['url']
 

        msg = request.form['comment']
        context["msg"] = msg

        # driver = webdriver.PhantomJS('/usr/bin/phantomjs')
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        youtube_username = "commentator951@gmail.com"
        youtube_password = "comment951"
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="yt-masthead-signin"]/div/button/span').click()
        except:
            driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer[2]/a').click()

        # signin_button.click()

        #login
        wait_and_find(driver, '//*[@id="identifierId"]', youtube_username)
        next_button_id = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
        next_button_id.click()

        #password
        wait_and_find(driver, '//*[@id="password"]/div[1]/div/div[1]/input', youtube_password)
        next_button_pass = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
        next_button_pass.click()

        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="comment-section-renderer"]/div[1]/div[1]/div[2]/div[1]').click()

        
        wait_and_find(driver, '//*[@id="comment-simplebox"]/div[2]/div[2]', msg)
        send_button = driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[3]/div[2]/button[2]')
        send_button.click()

        driver.close()

        return render_template('comments.html', context=context)
    return render_template('index.html', context=context)

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
    app.run()