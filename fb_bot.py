"""
-*- coding: utf-8 -*-
========================
Python Facebook Bot
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""

import selenium
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import argparse
import time

# Uncomment this for invisible browser
# display = Display(visible=0)
# display.start()


class FbBot():

    def __init__(self, driver, username, password):

        self.driver = driver
        driver.implicitly_wait(10)
        login = self.driver.find_element_by_id("email")
        login.send_keys(username)
        login = self.driver.find_element_by_id("pass")
        login.send_keys(password)
        login.send_keys(Keys.RETURN)

        if driver.current_url != "https://www.facebook.com/":
            exit("Invalid Credentials")
            self.driver.quit()
        else:
            print("Login Successful")

    def automate_status(self):

        with open('quote.txt', 'r') as f:
            get_line = sum(1 for line in open('quote.txt'))

            for i in range(get_line):
                read_line = f.readline()
                login = self.driver.find_element_by_name("xhpc_message")
                login.send_keys(read_line)
                self.driver.implicitly_wait(50)
                login = self.driver.find_element_by_css_selector("._1mf7")
                login.click()
                time.sleep(5)
                self.driver.refresh()
                time.sleep(3600)

    def automate_likes(self):
        for i in range(10):

            time.sleep(5)
            get_like_status = self.driver.find_elements_by_css_selector(".UFILikeLink")[i].get_attribute("aria-pressed")
            time.sleep(1)

            if get_like_status == 'false':
                get_like_bt = self.driver.find_elements_by_partial_link_text("Like")
                time.sleep(2)
                get_like_bt[i].click()
                if get_like_bt:
                    print("Done")
                else:
                    print("Not done")

                time.sleep(3)
            else:
                print("Already Liked")
            time.sleep(1800)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", help="status or likes?")
    parser.add_argument('--u', help="Username")
    parser.add_argument('--p', help="Password")
    parser.add_argument('--as', help="Password")

    args = parser.parse_args()

    if not args.a:
        exit("Please specify status or likes to automate using --a=parameter(status/likes)")
    if not args.u:
        exit("Please specify FB username using --u=parameter")
    if not args.p:
        exit("Please specify FB password using --p=parameter")

    try:

        driver = webdriver.Chrome()
        driver.get("http://www.facebook.com/")

        f = FbBot(driver, args.u, args.p)
        driver.implicitly_wait(50)

        if args.a == "status":
            f.automate_status()

        if args.a == "likes":
            f.automate_likes()

        print("Thanks for using!!!")

    except KeyboardInterrupt:
        exit("User Aborted")

    except:
        exit("Invalid parameter\nIt should be status or likes")


if __name__ == "__main__":
    main()
