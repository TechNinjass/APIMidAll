# Tests that the function successfully retrieves valid credentials from an existing token file. tags: [happy path]
from flaskr.cloud_connection.drive_connection import get_creds
from pytest_mock import mocker
import pytest


class TestDrive:

    def test_token_file_exists_and_contains_valid_credentials(self, mocker):
        # Setup
        mocker.patch('os.path.exists', return_value=True)
        creds_mock = mocker.Mock()
        creds_mock.valid = True
        mocker.patch('google.oauth2.credentials.Credentials.from_authorized_user_file', return_value=creds_mock)

        # Execution
        creds = get_creds()

        # Assertion
        assert creds == creds_mock