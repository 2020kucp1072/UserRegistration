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
    assert user_registration.validate_email('abc+100@gmail.com')
    assert user_registration.validate_email('abc@yahoo.com')
    assert user_registration.validate_email('abc-100@yahoo.com')
    assert user_registration.validate_email('abc.100@yahoo.com')
    assert user_registration.validate_email('abc111@abc.com')
    assert user_registration.validate_email('abc111@abc.net')
    assert user_registration.validate_email('abc.100@abc.com.au')
    assert user_registration.validate_email('abc@1.com')
    assert user_registration.validate_email('abc@gmail.com.com')

    # Invalid email assertions
    assert not user_registration.validate_email(' abc')
    assert not user_registration.validate_email('abc@.com.my')
    assert not user_registration.validate_email('abc123@gmail.a')
    assert not user_registration.validate_email('abc123@.com')
    assert not user_registration.validate_email('abc123@.com.com')
    assert not user_registration.validate_email('.abc@abc.com')
    assert not user_registration.validate_email('abc()*@gmail.com')
    assert not user_registration.validate_email('abc@%*.com')
    assert not user_registration.validate_email('abc..2002@gmail.com')
    assert not user_registration.validate_email('abc.@gmail.com')
    assert not user_registration.validate_email('abc@abc@gmail.com')
    assert not user_registration.validate_email('abc@gmail.com.1a')
    assert not user_registration.validate_email('abc@gmail.com.aa.au')
    assert not user_registration.validate_email("dil@gmail.com.1a")
    
def test_check_mobile():
    assert user_registration.validate_mobile("919849032495")
    assert not user_registration.validate_mobile("798177")
    
def test_check_password():
    assert user_registration.validate_password("2008227@Di")
    assert not user_registration.validate_password("sjsj")
if __name__ == "__main__":
    pytest.main()