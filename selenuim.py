from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time
import requests
import re
from bs4 import BeautifulSoup
import string

def findSeats(html):
    soup = BeautifulSoup(html, "html.parser")
    seatList = soup.find('div', attrs={'class': 't'})
    data = []
    rows = []
    columns = []
    for seat in seatList.find_all('div', attrs={'class': 'seat'}):
        style = seat.get('style')
        if 'rgb(105, 88, 167)' in style:
            title = seat.get('title')
            data.append(title)
            row = title.split()[0]
            column = title.split()[1]
            col = re.sub("\D", "", column)
            rows.append(row)
            columns.append(col)
    while len(data) > 0:
        min_col = min(columns)
        min_col_loc = columns.index(min_col)
        corresponding_row = rows[min_col_loc]
        col_2 = int(min_col) + 2
        loc_2 = str(corresponding_row) + ' 排Row排' + str(col_2) + '座'
        if loc_2 in data:
            loc = data[min_col_loc]
            print("choose seat: ", loc, " and ", loc_2)
            Seats = driver.find_element_by_id("SeatMap1_DSeatMap")
            Seats.find_element_by_css_selector("div[title='%s']" % loc).click()
            Seats.find_element_by_css_selector("div[title='%s']" % loc_2).click()
            driver.find_element_by_css_selector("input[value='确认订购']").click()
            break
        else:
            del columns[min_col_loc]
            del rows[min_col_loc]
            del data[min_col_loc]

start = time.clock()
url = "http://www.shculturesquare.com/program.aspx?programId=9130"
username_ = "*********"
password_ = "*********"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
# driver = webdriver.Chrome(desired_capabilities=caps, executable_path="C:/Windows/chromedriver.exe")
driver = webdriver.Chrome(desired_capabilities=caps, executable_path="C:/Windows/chromedriver.exe",chrome_options=chrome_options)

driver.get(url)
driver.find_element_by_id("img_denglu").click()
driver.find_element_by_id("login_name").send_keys(username_)
driver.find_element_by_id("pwd").send_keys(password_)
driver.find_element_by_xpath("//*[@id='culture_login']/table/tbody/tr/td[2]/div/input").click()
# driver.implicitly_wait(0.5)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"sel_Time")))
date = driver.find_element_by_xpath("//*[@id='sel_Time']")
Select(date).select_by_visible_text("2018-09-02 19:30星期日")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"img_XuanZuo")))
driver.find_element_by_xpath("//*[@id='img_XuanZuo']").click()

iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"DDL_EVENTZONE")))
region = driver.find_element_by_xpath("//*[@id='DDL_EVENTZONE']")
Select(region).select_by_visible_text("观众厅三楼")
# now_url = driver.current_url
# print(now_url)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[title='4 排Row排36座']")))
# find all the seats which background-color: rgb(105, 88, 167)

# r = requests.get(now_url)
# r.raise_for_status()
# r.encoding = r.apparent_encoding
# html = r.text
html = driver.page_source
findSeats(html)
end = time.clock()
print("The function run time is : %.03f seconds" %(end-start))
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[title='4 排Row排36座']")))
# Seats = driver.find_element_by_id("SeatMap1_DSeatMap")
# Seats.find_element_by_css_selector("div[title='4 排Row排36座']").click()
# driver.find_element_by_css_selector("input[value='确认订购']").click()
# dialog_box = driver.switch_to_alert()
# time.sleep(2)
# # dialog_box.accept()
# dialog_box.dismiss()


# seats = Seats.find_elements_by_class_name("seat")
# for seat in seats:
#     attr = seat.get_attribute('title')
#     print(attr)
# print(seats.__len__())

# driver.close()