import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logs.user_logs import log_message


def project_login(driver, project_name_with_date):
    # Wait until the project name appears in the list
    try:
        project_name_with_date = project_name_with_date.replace(" ", "").replace("-", "").replace(":", "")
        project_element = WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{project_name_with_date}')]"))
        )
        log_message(f"Found the project: {project_name_with_date}")
        time.sleep(15)
    except Exception as e:
        log_message(f"Error finding project '{project_name_with_date}': {str(e)}")
        raise e

    time.sleep(10)

    # Click on the project once it is found
    attempts = 0
    while attempts < 3:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", project_element)  # Scroll into view
            time.sleep(1) 

            project_element.click()  
            log_message(f"Clicked on the project: {project_name_with_date}")
            break
        except Exception as e:
            log_message(f"Attempt {attempts+1}: Error clicking on the project '{project_name_with_date}': {str(e)}")
            time.sleep(2)  
            attempts += 1

    if attempts == 3:
        log_message(f"Failed to click on the project after {attempts} attempts.")
        raise Exception(f"Could not click project '{project_name_with_date}' due to repeated interception.")



    # check is the project-login sucessful
    try:
        add_datasets_text = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='Add Datasets']"))
        )
        log_message("Login successful. Found 'Add datasets' text.")
    except Exception as e:
        log_message(f"Login might have failed. 'Add datasets' text not found after waiting: {str(e)}")
