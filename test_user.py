import pytest
from user import User


@pytest.fixture
def user_obj_true():
    return User('Ravi', 'Singh', 'rs246@gmail.com', '91 9983392675', 'abAC@234534')


@pytest.fixture
def user_obj_false():
    return User('ravi', 'singh', 'abc.com', '91 976789878898', 'asdf@dsf')


def test_name_validation_success(user_obj_true, user_obj_false):
    assert user_obj_true.name_validation() is True
    assert user_obj_false.name_validation() is False


def test_email_validation_success(user_obj_true, user_obj_false):
    assert user_obj_true.email_validation() is True
    assert user_obj_false.email_validation() is False


def test_number_validation_success(user_obj_true, user_obj_false):
    assert user_obj_true.number_validation() is True
    assert user_obj_false.number_validation() is False


def test_password_validation_success(user_obj_true, user_obj_false):
    assert user_obj_true.password_validation() is True
    assert user_obj_false.password_validation() is False
