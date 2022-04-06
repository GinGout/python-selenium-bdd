from behave import *
from selenium import webdriver

@Given("The user launched the website in chrome")
def launch_site(context):
    context.browser = webdriver.Chrome(executable_path='/Users/gpasupathy/devtools/chromedriver')
    context.browser.get('https://magento2-demo.magebit.com/')
