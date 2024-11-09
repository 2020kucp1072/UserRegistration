'''
    @Author: VEMULA DILEEP
    @Date: 04-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 04-11-2024
    @Title : File to test input details

'''

import pytest
import user_registration


def test_check_firstname():
    
    assert user_registration.validate_firstname("Dileep")
    assert not user_registration.validate_firstname("dil")

def test_check_last_name():
    assert user_registration.validate_last_name("Vemula")
    assert not user_registration.validate_last_name('vem')
    
def test_check_email():
    assert user_registration.validate_email("dileep@gmail.com.com")
    assert not user_registration.validate_email("dil@gmail.com.1a")
def test_check_mobile():
    assert user_registration.validate_mobile("919849032495")
    assert not user_registration.validate_mobile("798177")
if __name__ == "__main__":
    pytest.main()