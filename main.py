from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_ACCOUNT = os.environ.get("TARGET_ACCOUNT")
INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")


class Instafollower:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTA_USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD, Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")

        time.sleep(10)
        followers = self.driver.find_element(By.CLASS_NAME, '//*[@id="mount_0_0_/A"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        followers.click()

    def follow(self):
        time.sleep(5)
        followers_list = self.driver.find_elements(By.CLASS_NAME, "_acan")
        for account in followers_list:
            time.sleep(2)
            account.click()


bot = Instafollower()
bot.login()
bot.find_followers()
bot.follow()
