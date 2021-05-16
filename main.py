# This is a sample Python script.
import datetime
import time
from datetime import date, timedelta

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver

# d_1 = datetime.datetime.now()
# req_format = (d_1,'%d %m %Y')
# req_format = date.strftime(d_1, '%d %m %Y')

 # date.strftime('%d %m %Y')

# timedelta(days=6)

driver= webdriver.Chrome('venv/chromedriver')
# driver= webdriver.Chrome('venv/chromedriver-Windows')

driverxpath = driver.find_element_by_xpath
driverget = driver.get
emailin=str(input("Enter your Email : "))
firstnme=str(input("Enter your First Name : "))
lastnme=str(input("Enter your last name : "))
caldate = (input("Starting date (add dd) :"))
calmon = (input("Starting date (add mm ) :"))

webmain = driverget('https://form.jotform.com/nick_apcd/CBAT');
# formpass= driver.find_element_by_xpath('//*[@id="input_203"]')
formpass = driverxpath('//*[@id="input_203"]').send_keys('!Granville1')
firstname = driverxpath('//*[@id="first_35"]').send_keys(f'{firstnme}')
lastname = driverxpath('//*[@id="last_35"]').send_keys(f'{lastnme}')
techemail = driverxpath('//*[@id="input_199"]').send_keys(f'{emailin}')
projectsel = driverxpath('//*[@id="input_198"]').send_keys('1')
date = driverxpath('//*[@id="lite_mode_189"]').send_keys(f'{caldate-6}052021')
#date = driverxpath('//*[@id="lite_mode_189"]').send_keys(f'{d_1:%d %m}2021')
# # print(d_1)
# # dat1= d_1
# # # timd= int(timedelta)
# d_1=d_1-timedelta(days=6)
# print(d_1)
# # yest_str= str(yest)
# # print(yest_str)
# # # k = "yest"
# # print(yest)
# # dat3 = caldate-timedelta(days=5)
# # date=driverxpath('//*[@id"lite_mode_142"]').send_keys(f'{dat3}-05-2021')

# date = driverxpath('//*[@id="calendar_141"]').send_keys(f'{d_1}2021')
# date = driverxpath('//*[@id="lite_mode_141"]').send_keys(f'{yest_str}')
date = driverxpath('//td[@class='selected']').send_keys(f'{caldate-6}052021')
time = driverxpath('//*[@id="input_153_hourSelect"]').send_keys('08')
time = driverxpath('//*[@id="input_153_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_154_hourSelect"]').send_keys('16')
time = driverxpath('//*[@id="input_154_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_155_hourSelect"]').send_keys('0')
time = driverxpath('//*[@id="input_155_minuteSelect"]').send_keys('30')
locsel= driverxpath('//*[@id="input_204"]').send_keys('l')

#date=driverxpath('//*[@id="lite_mode_142"]').send_keys(f'{dat3}-05-2021')
# time.sleep(4)

time = driverxpath('//*[@id="input_156_hourSelect"]').send_keys('08')
time = driverxpath('//*[@id="input_156_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_157_hourSelect"]').send_keys('16')
time = driverxpath('//*[@id="input_157_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_158_hourSelect"]').send_keys('0')
time = driverxpath('//*[@id="input_158_minuteSelect"]').send_keys('30')
locsel1= driverxpath('//*[@id="input_205"]').send_keys('l')
#date=driverxpath('//*[@id="lite_mode_138"]').send_keys(f'{caldate-4}-05-2021')
time = driverxpath('//*[@id="input_144_hourSelect"]').send_keys('08')
time = driverxpath('//*[@id="input_144_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_145_hourSelect"]').send_keys('16')
time = driverxpath('//*[@id="input_145_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_146_hourSelect"]').send_keys('0')
time = driverxpath('//*[@id="input_146_minuteSelect"]').send_keys('30')
locsel2= driverxpath('//*[@id="input_206"]').send_keys('l')

# date=driverxpath('//*[@id="lite_mode_139"]').send_keys(f'{caldate-3}-05-2021')
time = driverxpath('//*[@id="input_147_hourSelect"]').send_keys('08')
time = driverxpath('//*[@id="input_147_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_148_hourSelect"]').send_keys('16')
time = driverxpath('//*[@id="input_148_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_149_hourSelect"]').send_keys('0')
time = driverxpath('//*[@id="input_149_minuteSelect"]').send_keys('30')
locsel3= driverxpath('//*[@id="input_207"]').send_keys('l')

# date=driverxpath('//*[@id="lite_mode_140"]').send_keys(f'{caldate-2}-05-2021')
time = driverxpath('//*[@id="input_150_hourSelect"]').send_keys('08')
time = driverxpath('//*[@id="input_150_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_151_hourSelect"]').send_keys('16')
time = driverxpath('//*[@id="input_151_minuteSelect"]').send_keys('30')
time = driverxpath('//*[@id="input_152_hourSelect"]').send_keys('0')
time = driverxpath('//*[@id="input_152_minuteSelect"]').send_keys('30')
locsel4= driverxpath('//*[@id="input_208"]').send_keys('l')
# date=driverxpath('//*[@id="lite_mode_162"]').send_keys(f'{caldate-1}-05-2021')
locsel5= driverxpath('//*[@id="input_168"]').send_keys('w')
# date=driverxpath('//*[@id="lite_mode_173"]').send_keys(f'{caldate}-05-2021')
locsel6= driverxpath('//*[@id="input_182"]').send_keys('w')
reset=driverxpath('//*[@id="input_reset_2"]').click()






