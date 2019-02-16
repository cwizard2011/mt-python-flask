from tests.base import BaseTestCase, CommonTestCases
from fixtures.requests.request_fixture import (
    get_single_request_query,
    get_single_request_response,
    get_user_request_query,
    get_user_request_response,
    get_single_request_query_no_request
)
from fixtures.requests.admin_update_fixture import (
    get_all_request_query,
    get_all_request_response
)
from fixtures.user.user_login import (
    user_login_mutation_token,
    admin_login_mutation_token,
    user2_login_mutation_token)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRequest(BaseTestCase):

    def test_get_all_user_request(self):
        """
        Testing for Getting all user request
        """

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            get_user_request_query,
            get_user_request_response
        )

    def test_get_single_user_request(self):
        """Testing for getting a single user request"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            get_single_request_query,
            get_single_request_response
        )

    def test_get_user_request_no_request(self):
        """Testing for getting user request with no request"""

        login = self.client.execute(user2_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            get_user_request_query,
            'You have not place any maintenance request'
        )

    def test_get_single_request_not_found(self):
        """Testing for getting request with non-existent id"""

        user_login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            user_login['data']['loginUser']['token'],
            get_single_request_query_no_request,
            'The request with this id does not belong to this user'
        )

    def test_get_other_users_single_request(self):
        """Testing for admin create request"""

        user_login = self.client.execute(user2_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            user_login['data']['loginUser']['token'],
            get_single_request_query,
            'The request with this id does not belong to this user'
        )

    def test_admin_get_all_requests(self):
        """Testing for admin get all request"""
        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            admin_login['data']['loginUser']['token'],
            get_all_request_query,
            get_all_request_response
        )
