import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.logs.user_logs import log_message
from config.variables.parameters import project_name 


def project_create(driver):
# Click on new_project
    try:
        new_project_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "newProject"))
        )
        new_project_button.click() 
        log_message("Clicked the New Project button.")
    except Exception as e:
        log_message(f"Error clicking New Project button: {str(e)}") 

# -------------------

#select usecase churn
    try:
        dropdown_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Please select your use-case')]/following::input[@role='combobox']"))
        )
        dropdown_input.click()
        log_message("Dropdown for 'Please select your use-case' activated.")

        dropdown_input.send_keys("Churn")
        log_message("Typed 'Churn' to filter the dropdown options.")

        dropdown_input.send_keys(Keys.ENTER)  
        
        log_message("Option 'Churn' mapped and Enter key pressed.")

    except Exception as e:
        log_message(f"Error selecting the 'Churn' option: {str(e)}")
        raise e



    # Select 'Subscription' radio button
    try:
        subscription_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Subscription')]"))
        )

        subscription_input = subscription_label.find_element(By.XPATH, "./preceding-sibling::span/input")

        subscription_input.click()
        log_message("Selected the 'Subscription' checkbox/radio button.")
        
    except Exception as e:
        log_message(f"Error selecting the 'Subscription' checkbox/radio button: {str(e)}")
        raise e


    # Select 'Customer' radio button
    try:
        customer_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Customer')]"))
        )

        customer_input = customer_label.find_element(By.XPATH, "./preceding-sibling::span/input")

        customer_input.click()
        log_message("Selected the 'Customer' checkbox/radio button.")
    except Exception as e:
        log_message(f"Error selecting Customer radio button: {str(e)}")


# -----------------------        

# Find fiels to enter project name & enter project name
    try:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Project name')]/following-sibling::input"))
        )
        log_message("Found the input field.")
        
        current_datetime = datetime.now().strftime("%m-%d %H:%M:%S")
        project_name_with_date = f"{project_name}{current_datetime}"
        input_field.send_keys(project_name_with_date)

        log_message(f"Entered project_name: {project_name_with_date}")
    except Exception as e:
        log_message(f"Error finding input field: {str(e)}")
        raise e


# Click the Create project button
    try:
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Create']"))
        )
        print(create_button.get_attribute('outerHTML'))
        create_button.click()

        log_message("Successfully clicked the 'Create' button.")
    except Exception as e:
        log_message(f"Error clicking 'Create' button: {str(e)}")
        raise e


    time.sleep(7)
    return project_name_with_date

    
