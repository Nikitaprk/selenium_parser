import time
from auth_data import user_password, user_email
from selenium import webdriver
import pickle

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.160')
driver = webdriver.Chrome(
    executable_path='C://Users//Nikita//PycharmProjects//pythonProject//venv//chrome//chromedriver.exe',
    options=options)


try:
    '''
    driver.get('https://krasnoeibeloe.ru/auth')
    time.sleep(5)

    email_imput = driver.find_element_by_name("email") 
    email_imput.send_keys(user_email)
    password = driver.find_element_by_name("USER_PASSWORD")
    password.send_keys(user_password)
    time.sleep(2)
    enter_button = driver.find_element_by_name("Login").click()
    # cookies
    pickle.dump(driver.get_cookies(), open(f"{user_email}_cookies", "wb"))
    '''
    driver.get('https://krasnoeibeloe.ru/')
    for cookies in pickle.load(open('nikitaprk@mail.ru_cookies', 'rb')):
        driver.add_cookie(cookies)
    driver.refresh()
    driver.get('https://krasnoeibeloe.ru/catalog/importnoe_pivo/')
    time.sleep(5)

# для начала сделаем парсер для импортного пива



except Exception as ex:
    print("error")
finally:
    driver.close()
    driver.quit()