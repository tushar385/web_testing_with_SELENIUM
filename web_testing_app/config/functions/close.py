from config.logs.user_logs import log_message

def close_driver(driver):
    driver.quit()  
    log_message("WebDriver closed.")
