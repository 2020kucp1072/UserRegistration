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


def main():
    
    validate_firstname("Dileep")

if __name__=="__main__":
    main()