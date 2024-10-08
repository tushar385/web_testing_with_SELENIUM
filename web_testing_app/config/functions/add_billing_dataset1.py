import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.logs.user_logs import log_message
from config.variables.parameters import import_table_schema,billing_dataset1



def add_billing_datasets1(driver):
    # click on "Billing" catagory
    try:
        billing_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Billing')]"))
        )
        billing_button.click()
        log_message("Billing button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'Billing' button: {str(e)}")
        raise e
    
    # click skip on daise
    try:
        select_schema = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()= 'SKIP']"))
        )
        select_schema.click()
        log_message("SKIP button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'SKIP' button: {str(e)}")
        raise e


    # select schema
    try:
        select_schema = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()= '{import_table_schema}']"))
        )
        select_schema.click()
        log_message("Schema button clicked.")
    except Exception as e:
        log_message(f"Error selecting Schema button: {str(e)}")
        raise e
    

    # select table
    try:
        select_billing_dataset1 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()= '{billing_dataset1}']"))
        )
        select_billing_dataset1.click()
        log_message("Select billing_dataset1 clicked.")
    except Exception as e:
        log_message(f"Error selecting billing_dataset1 : {str(e)}")
        raise e   


    # click done
    try:
        select_schema = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()= 'Done']"))
        )
        select_schema.click()
        log_message("Billing button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'Billing' button: {str(e)}")
        raise e

# ------------billing_date---------------------
    time.sleep(30)
    # select date in mapping
    try:
        dropdown_input1 = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='BillingDate']//input"))
        )
        dropdown_input1.click()
        log_message("Dropdown activated.")

        for char in 'la_dat':
            dropdown_input1.send_keys(char)
            time.sleep(0.2)  

        time.sleep(2)  
        dropdown_input1.send_keys(Keys.ENTER)  

        log_message("La_date option mapped and Enter key pressed.")
    except Exception as e:
        log_message(f"Error selecting la_date option: {str(e)}")
        raise e
    
    
    # Click the "Ok" warning button
    try:
        ok_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Ok')]"))
        )
        ok_button.click()
        log_message("Ok button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'Ok' button: {str(e)}")
        raise e


# ------------account_id---------------------
    time.sleep(30)
    # select date in mapping
    try:
        dropdown_input2 = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='CustomerID']//input"))
        )
        dropdown_input2.click()
        log_message("Dropdown activated.")

        for char in 'fiant':
            dropdown_input2.send_keys(char)
            time.sleep(0.2)  

        time.sleep(2)  
        dropdown_input2.send_keys(Keys.ENTER)  

        log_message("fiant option mapped and Enter key pressed.")
    except Exception as e:
        log_message(f"Error selecting fiant option: {str(e)}")
        raise e
    
# ------------revenue---------------------
    time.sleep(30)  
    # select date in mapping
    try:
        dropdown_input3 = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='Revenue']//input"))
        )
        dropdown_input3.click()
        log_message("Dropdown activated.")

        for char in 'fonds':
            dropdown_input3.send_keys(char)
            time.sleep(0.2)  

        time.sleep(2)  
        dropdown_input3.send_keys(Keys.ENTER)  

        log_message("fonds option mapped and Enter key pressed.")
    except Exception as e:
        log_message(f"Error selecting fonds option: {str(e)}")
        raise e
    


    # click Next
    try:
        select_schema = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next') and not(@disabled)]"))
        )
        select_schema.click()
        log_message("Billing button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'Billing' button: {str(e)}")
        raise e
    
    time.sleep(20) 