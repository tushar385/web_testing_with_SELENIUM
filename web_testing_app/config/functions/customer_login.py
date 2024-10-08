import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logs.user_logs import log_message
from config.variables.parameters import customers_page,testing_customer



def customer_login(driver):
    
# Click on customer 
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//button[.//div[contains(text(), "{testing_customer}")]]'))
        )
        button.click()
        log_message("Clicked customer button for: " + testing_customer)
        time.sleep(5)  
        return True  
    except Exception as e:
        log_message(f"Error clicking customer button: {str(e)}")
        return False  
