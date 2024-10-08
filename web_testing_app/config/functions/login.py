import time
from flask import Flask, render_template_string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.logs.user_logs import log_message # importing logs function to store logs
from config.functions.start import start_driver # importing start driver 
from config.variables.parameters import login_page, username,password # loading parameters


def login():
    driver = None

    ## Starting chrome driver
    try:  
        driver = start_driver()
        log_message("Driver started")
    except Exception as e:
        log_message(f"Error during starting driver: {str(e)}")
        return None 


    # Navigating to login page of sfn
    try:
        driver.get(login_page)
        log_message("Navigated to login page.")
    except Exception as e:
        log_message(f"Error navigating to login page: {str(e)}")
        driver.quit()
        raise e



    # Finding username & password fields
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        log_message("Found username and password fields.")
    except Exception as e:
        log_message(f"Error finding login form fields: {str(e)}")
        raise e



    # Entering username & password 
    try:
        username_field.send_keys(username)
        password_field.send_keys(password)
        log_message("Entered credentials.")
    except Exception as e:
        log_message(f"Error entering credentials: {str(e)}")
        raise e



    # Clcking on submit button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        login_button.click()
        log_message("Clicked login button.")
    except Exception as e:
        log_message(f"Error clicking login button: {str(e)}")
        driver.quit()
        raise e
    

    # check is login sucessful
    try :
        WebDriverWait(driver, 10).until(EC.url_contains('/admin/customers')) 
        log_message("Login successful!")
    except Exception as e:
        log_message(f"Not able to Login: {{str(e)}}")
    


    time.sleep(5)

    return driver





