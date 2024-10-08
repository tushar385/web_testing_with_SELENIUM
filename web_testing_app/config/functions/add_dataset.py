import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logs.user_logs import log_message


def add_datasets(driver):
    # Click on add datasets
    try:
        add_datasets_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Add Datasets')]"))
        )
        add_datasets_button.click()
        log_message("Add Datasets button clicked.")
    except Exception as e:
        log_message(f"Error clicking 'Add Datasets' button: {str(e)}")
        raise e
    
    time.sleep(5) 


    # Wait for the popup to appear and become visible
    try:
        popup_container = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiDialog-paper"))
        )
        log_message("Popup is visible.")
    except Exception as e:
        log_message(f"Popup didn't appear: {str(e)}")
        raise e
