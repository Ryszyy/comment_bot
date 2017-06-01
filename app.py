from flask import Flask
from flask import request
from flask import render_template
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
        driver.get(u)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
        half =len(r.get_ranked_phrases())/2
        keywords_list = r.get_ranked_phrases()[:int(half)]
        context['keywords'] = keywords_list
        context['comments'] = comments

        return render_template('index.html', context=context)

    return render_template('index.html', context=context)



if __name__ == "__main__":
    app.run()