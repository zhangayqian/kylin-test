from selenium import webdriver
from yaml import load, loader
import os

from utils import kylin


def setup_instance(file_name):
    instances_file = os.path.join('kylin_instances/', file_name)
    stream = open(instances_file, 'r')
    for item in load(stream, Loader=loader.SafeLoader):
        host = item['host']
        port = item['port']
    return kylin.connect(host=host, port=port)


def kylin_url(file_name):
    instances_file = os.path.join('kylin_instances/', file_name)
    stream = open(instances_file, 'r')
    for item in load(stream, Loader=loader.SafeLoader):
        host = item['host']
        port = item['port']
    return "http://{host}:{port}/kylin".format(host=host, port=port)


def setup_browser(browser_type):
    if browser_type == "chrome":
        browser = webdriver.Chrome(executable_path="browser_driver/chromedriver")

    if browser_type == "firefox":
        browser = webdriver.firefox(executable_path="browser_driver/geckodriver")

    if browser_type == "safari":
        browser = webdriver.safari(executable_path="browser_driver/safaridriver")

    return browser
