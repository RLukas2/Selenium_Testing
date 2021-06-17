import os
import time
import codecs
import array as arr

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class GetData:
    def __init__(self):
	
        self.driverpath = 'driver/chromedriver.exe'
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.driverpath)
        self.driver.set_window_size(800, 600)
        self.info = {}

    def build(self, info):
        self.info = info

    def process(self):
        self.driver.get(self.info['URL'][1])
        self.driver.execute_script("window.stop();")

        time.sleep(2)

        for u in self.info:
            if u == 'URL' or u == '':
                continue;

            elementName = self.info[u][0]
            data = self.info[u][1]

            if u[0] == 'C':
                try:
                    self.Item = self.driver.find_element_by_xpath("//div[contains(text(), '" + elementName + "')]")
                    Itemid = self.Item.get_attribute("id");

                    self.Item = self.driver.find_element_by_xpath("//div[@aria-labelledby='" + Itemid + "']")
                    self.Item = self.Item.find_element_by_xpath(".//div[@data-value='" + data + "']")

                    self.Item.click();
                    self.Item.click();
                except NoSuchElementException:
                    continue
                
            elif u[0] == 'B':
                try:
                    self.Item = self.driver.find_element_by_xpath("//div[contains(text(), '" + elementName + "')]")
                    Itemid = self.Item.get_attribute("id")

                    self.Item = self.driver.find_element_by_xpath("//div[@aria-labelledby='" + Itemid + "']")
                    self.Item = self.Item.find_element_by_xpath(".//div[@data-answer-value='" + data + "']")
                    self.Item.click();
                except NoSuchElementException:
                    continue
            else:
                try:
                    self.Item = self.driver.find_element_by_xpath("//div[contains(text(), '" + elementName + "')]")
                    #while len(self.Item.find_elements_by_xpath("//input[@type='text']")) == 0:
                        #self.Item = self.Item.find_element_by_xpath("./..");        
                    #self.Item = self.Item.find_element_by_xpath("./..");        
                    #self.Item = self.Item.find_element_by_xpath("./..");        
                    #self.Item = self.Item.find_element_by_xpath("./..");        

                    Itemid = self.Item.get_attribute("id")

                    self.Item = self.Item.find_element_by_xpath("//input[@aria-labelledby='" + Itemid + "']");
                    self.Item.send_keys(str(data));
                except NoSuchElementException:
                    continue

        self.LastButton = self.driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span")
        self.LastButton.click();

        self.driver.quit()


        
            