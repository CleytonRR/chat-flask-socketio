from utils.verify_email import VerifyEmail

mock_valid_email = "any_email@teste.com"
mock_invalid_email = "invalidteste.com"


def test_verify_valid_email():
    data = VerifyEmail.verify(mock_valid_email)
    assert True == data


def test_verify_invalid_email():
    data = VerifyEmail.verify(mock_invalid_email)
    assert False == data
