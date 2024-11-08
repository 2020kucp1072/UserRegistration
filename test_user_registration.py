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




if __name__ == "__main__":
    pytest.main()