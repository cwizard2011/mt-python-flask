from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_login import (
    user_login_mutation,
    user_mutation_response,
    user_login_invalid_email,
    user_login_invalid_email_response,
    user_login_invalid_password,
    user_login_invalid_password_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestLoginUser(BaseTestCase):

    def test_user_login(self):
        """
        Testing for User login
        """
        CommonTestCases.user_login_assert_equal(
            self,
            user_login_mutation,
            user_mutation_response
        )

    def test_user_login_invalid_email(self):
        """
        Testing for user login with invalid email
        """
        CommonTestCases.user_login_assert_equal(
            self,
            user_login_invalid_email,
            user_login_invalid_email_response
        )

    def test_user_login_invalid_password(self):
        """
        Testing for user login with invalid password
        """
        CommonTestCases.user_login_assert_equal(
            self,
            user_login_invalid_password,
            user_login_invalid_password_response
        )
