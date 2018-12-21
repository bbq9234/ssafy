# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
from urllib import parse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

app = Flask(__name__)

slack_token = "xoxb-507380538243-508581046935-lqaSBt76meMAiinShrNl7ohe"
slack_client_id = "507380538243.508580770087"
slack_client_secret = "711e108d627cbdd99f8ee49bdc916501"
slack_verification = "K5GpZADCkkFGZKY47x06R0Ba"
sc = SlackClient(slack_token)


def get_first_youtube_link(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    cr_driver = webdriver.Chrome('C:/Users/student/AppData/Local/Programs/Python/chromedriver.exe',
                                 chrome_options=options)
    # cr_driver = webdriver.Chrome('chromedriver', chrome_options=options)
    cr_driver.get(get_encoded_url(url))

    WebDriverWait(cr_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-video-renderer")))

    page_results = cr_driver.find_element(By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-video-renderer")

    cr_driver.quit()

    return page_results.get_attribute("href")


def get_encoded_url(original_url):
    url = parse.urlparse(original_url)
    query = parse.parse_qs(url.query)
    encoded = parse.urlencode(query, doseq=True)
    return url.scheme + "://" + url.netloc + url.path + "?" + encoded


def get_source_code(url):
    return urllib.request.urlopen(url).read()


# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
    keywords = []

    if "creamheroes" == text.split(' ', 1)[1]:
        keywords.append("Bugs 실시간 음악 차트 Top 10\n")

        # url = re.search(r'(https?://\S+)', text.split('|')[0]).group(0)
        url = "https://music.bugs.co.kr/chart"
        youtubeSearchBaseUrl = "https://www.youtube.com/results?search_query="
        req = urllib.request.Request(url)

        soup = BeautifulSoup(get_source_code(url), "html5lib")

        # 함수를 구현해 주세요
        for idx, song in enumerate(
                zip(
                    map(lambda title: title.get_text().strip(), soup.find_all("p", class_="title")),
                    map(lambda artist: artist.get_text().strip(), soup.find_all("p", class_="artist"))
                )):
            if idx >= 10:
                break

            keywords.append(str(idx + 1) + ". " + song[0] + " / " + song[1])
            keywords.append(
                "\t" + get_first_youtube_link(get_encoded_url(youtubeSearchBaseUrl + song[0] + "+" + song[1])))


    else:
        keywords.append("무슨 말인지 모르겠어요... creamheroes라고 입력해 보세요")

    # 한글 지원을 위해 앞에 unicode u를 붙혀준다.
    return u'\n'.join(keywords)


# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = _crawl_naver_keywords(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
        )

        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
