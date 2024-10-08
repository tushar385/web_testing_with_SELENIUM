import sys
import os
import time
from flask import Flask, render_template, request, redirect, url_for
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.logs.user_logs import read_logs, clear_logs, log_message
from config.functions.login import login
from config.functions.customer_login import customer_login 
from config.functions.project_create import project_create 
from config.functions.project_login import project_login 
from config.functions.add_dataset import add_datasets 
from config.functions.add_billing_dataset1 import add_billing_datasets1 
from config.functions.close import close_driver


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'config', 'templates'))  # Set the template folder



@app.route("/")

def testing_app():
    return render_template('home.html') 

# @app.route("/happy_path", methods=['POST'])
# def Run_script():
#     clear_logs()     ## mandatory
#     driver = login()
#     customer_login(driver)
#     project_create(driver)
#     close_driver(driver)      ## mandatory
#     logs = read_logs()     ## mandatory

#     return render_template('happy_path.html', logs=''.join(logs))       ## mandatory

# -----------------------
#prod

@app.route("/happy_path", methods=['POST'])
def Run_script():
    clear_logs()  
    driver = None
    status = True  

    try:
        driver = login()  
    except Exception as e:
        log_message(f"Login failed: {str(e)}")
        status = False  

    if status:
        try:
            customer_login(driver)  
        except Exception as e:
            log_message(f"Customer login failed: {str(e)}")
            status = False  

    if status:
        try:
            project_name_with_date = project_create(driver)
            if project_name_with_date: 
                try:
                    project_login(driver, project_name_with_date)
                    log_message("Project login successful.")
                except Exception as e:
                    log_message(f"Project login failed: {str(e)}")
        except Exception as e:
            log_message(f"Project creation failed: {str(e)}")
            status = False  
            
    
    
    if driver is not None:
        close_driver(driver)
        log_message("Driver closed.")

    logs = read_logs()  
    return render_template('happy_path.html', logs=''.join(logs))


# ----------------------------------------------------------------------------------
#testing

@app.route("/testing", methods=['POST'])
def testing():
    clear_logs()  
    driver = None
    status = True  

    try:
        driver = login()  
    except Exception as e:
        log_message(f"Login failed: {str(e)}")
        status = False  

    if status:
        try:
            customer_login(driver)  
        except Exception as e:
            log_message(f"Customer login failed: {str(e)}")
            status = False  


    if status:
        try:
            project_name_with_date = project_create(driver)
            if project_name_with_date:  # Check if project creation was successful (returned value)
                try:
                    project_login(driver, project_name_with_date)
                    log_message("Project login successful.")
                except Exception as e:
                    log_message(f"Project login failed: {str(e)}")
        except Exception as e:
            log_message(f"Project creation failed: {str(e)}")
            status = False  


# cheakpoint of prod

    if status:
        try:
            add_datasets(driver)  
        except Exception as e:
            log_message(f"Add Datasets failed: {str(e)}")
            status = False  

    if status:
        try:
            add_billing_datasets1(driver)  
        except Exception as e:
            log_message(f"Add Datasets failed: {str(e)}")
            status = False  

    time.sleep(30)  # Let the action complete

    
    
    if driver is not None:
        close_driver(driver)
        log_message("Driver closed.")

    logs = read_logs()  
    return render_template('testing.html', logs=''.join(logs))

if __name__ == '__main__':
    app.run(debug=True)
