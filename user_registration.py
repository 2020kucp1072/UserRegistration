'''
    @Author: VEMULA DILEEP
    @Date: 04-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 04-11-2024
    @Title : User Registration problem

'''


import re
import log

log = log.logger_init("user_registration")

def validate_firstname(f_name):
    """
    Description:
        This function checks if user entered valid first name
    Parameter:
        f_name: the name to be checked
    Returns:
        True or False
    """

    try:
        if re.match(r'^[A-Z][a-zA-Z]{2,}$', f_name):
            log.info("First Name is valid.")
            return True
        else:
            log.error("First Name is invalid. It must start with a capital letter and have at least 3 characters.")
            return False
    except Exception as e:
        log.error(f"Error in validate_first_name: {e}")
        return False

def validate_last_name(l_name):
    
    try:
        if re.match(r'[A-Z][a-zA-Z]{2,}',l_name):
            log.info("Last Name is valid.")
            return True
        else:
            log.error("Last Name is invalid. It must start with a capital letter and have at least 3 characters.")
            return False
    except Exception as e:
        log.error(f"Error in validate_last_name: {e}")
        return False
    
def validate_email(email):
    
    try:
        if re.match(r'^[a-zA-Z0-9]+([._%+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$',email):
            log.info("Email is valid")
            return True
        else:
            log.error("Email is invalid")
            return False
    except Exception as e:
        log.error(f"Raised exception is{e}")
        return False  
    
def validate_mobile(mobile):
      try:
        if re.match(r'^\d{2}\d{10}$',mobile):
            log.info("mobile is valid")
            return True
        else:
            log.error("mobile is invalid")
            return False
      except Exception as e:
        log.error(f"Raised exception is{e}")
        return False 
    
def validate_password(password):
    try:
        if not re.match(r'^.{8,}$', password):
            log.error("Password must have at least 8 characters.")
            return False
        else:
            log.info("Password meets the minimum length requirement.")
            
        if not re.search(r'[A-Z]', password):
            log.error("Password must contain at least one uppercase letter.")
            return False
        else:
            log.info("Password has at least one uppercase letter.")
        return True
    
        
    except Exception as e:
        log.error(f"Error in validate_password: {e}")
        return False
        
        
def main():
    
    validate_firstname("Dileep")
    validate_last_name("Vemula")
    validate_email("dileep@gmail.com")
    validate_mobile("919849032495")
if __name__=="__main__":
    main()