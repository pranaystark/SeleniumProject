from selenium import webdriver
driver = webdriver.Chrome('/Users/starks/Downloads/chromedriver')
driverxpath = driver.find_element_by_xpath
driverget = driver.get
# driver = webdriver.Chrome()
driverget("https://form.jotform.com/nick_apcd/CBAT")
# webmain = driverget('https://form.jotform.com/nick_apcd/CBAT');
# formpass= driver.find_element_by_xpath('//*[@id="input_203"]')
driverxpath('//*[@id="input_203"]').send_keys('!Granville1')
def datepicker(date):
    driverInstance.find_element_by_id('//*[@id="calendar_141"]').click()
    elements = driverInstance.find_elements_by_xpath("//*[@id="calendar_141"]/table/tbody/tr/td/a")
    for dates in elements:
        if(dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("08")) == date):
            dates.click()/html/body/div[8]/table/thead/tr[2]/td[3]