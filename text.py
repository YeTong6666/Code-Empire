import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import cv2 as cv
from PIL import Image
from chaojiying import Chaojiying_Client
import os

def save_img():
    # 对当前页面进行截图保存
    driver.save_screenshot('page.png')
    # 定位验证码图片的位置
    code_img_ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[1]/form/div/span/div/table/tbody/tr/td/span[2]/img')
    # 获取验证码左上角的坐标x,y
    location = code_img_ele.location
    # 获取验证码图片对应的长和宽
    size = code_img_ele.size

    # 左上角和右下角的坐标
    rangle = (
        int(location['x'] ), int(location['y'] ), int((location['x'] + size['width'])),
        int((location['y'] + size['height']))
    )

    i = Image.open('./page.png')
    code_img_name = './code.png'
    # crop根据rangle元组内的坐标进行裁剪
    frame = i.crop(rangle)
    frame.save(code_img_name)
    return code_img_ele

def narrow_img():
    # 缩小图片
    code = Image.open('./code.png')
    small_img = code.resize((169, 216))
    small_img.save('./small_img.png')
    print(code.size, small_img.size)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=option)
driver.get('http://rs.xidian.edu.cn/forum.php')
driver.maximize_window()

time.sleep(1)

text_label = driver.find_element_by_xpath('//*[@id="ls_username"]')
text_label.send_keys('20009200070')

text_label = driver.find_element_by_xpath('//*[@id="ls_password"]')
text_label.send_keys('wlk181134830')

button =driver.find_element_by_xpath('//*[@type="submit"]')
button.click()

time.sleep(1)

save_img()
chaojiying = Chaojiying_Client('yetong', 'wlk181134830', '9807ffbdc65d81279142a35eb04a3ce6')  # 用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read() 
print(chaojiying.PostPic(im, 1902)['pic_str'])
result = chaojiying.PostPic(im, 1902)['pic_str']



text_label = driver.find_element_by_name("seccodeverify")
text_label.send_keys(result)

button =driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[1]/form/div/div[2]/table/tbody/tr/td[1]/button/strong')
button.click()

time.sleep(6)

button =driver.find_element_by_xpath('//*[@id="mn_N462e"]/a')
button.click()
button =driver.find_element_by_xpath('//*[@id="qiandao"]/table[2]/tbody/tr[1]/td/label[3]/input')
button.click()
button =driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[1]/form/table[1]/tbody/tr/td/ul/li[1]/center/img')
button.click()
button =driver.find_element_by_xpath('//*[@id="qiandao"]/table[1]/tbody/tr/td/div/a/img')
button.click()