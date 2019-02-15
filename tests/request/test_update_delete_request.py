from tests.base import BaseTestCase, CommonTestCases
from fixtures.requests.request_fixture import (
    update_request_mutation,
    update_request_response,
    update_request_details_mutation,
    update_request_details_response,
    update_request_invalid_title,
    update_request_invalid_id,
    update_approved_request,
    delete_request_mutation,
    delete_request_response,
    delete_request_invalid_id,
    delete_approved_request
)
from fixtures.user.user_login import (
    user_login_mutation_token, admin_login_mutation_token)

import sys
import os
sys.path.append(os.getcwd())


class TestUpdateDeleteRequest(BaseTestCase):

    def test_update_request_title(self):
        """
        Testing for Updating request title
        """

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            update_request_mutation,
            update_request_response
        )

    def test_update_request_details(self):
        """
        Testing for Updating request details
        """

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            update_request_details_mutation,
            update_request_details_response
        )

    def test_update_request_invalid_title(self):
        """Testing for updating a request with short title"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            update_request_invalid_title,
            'title of a request can only be between 5 and 30 character'
        )

    def test_update_request_invalid_id(self):
        """Testing for creating a request with invalid id"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            update_request_invalid_id,
            'The request with this id does not belong to this user'
        )

    def test_update_approved_request(self):
        """Testing for updating an approved request"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            update_approved_request,
            'Admin is working on this request, it can\\\'t be updated'
        )

    def test_update_request_admin(self):
        """Testing for admin update request"""

        admin_login = self.client.execute(admin_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            admin_login['data']['loginUser']['token'],
            update_request_mutation,
            'You are not authorized to perform this action'
        )

    def test_delete_request(self):
        """
        Testing for Deleting a request
        """

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_equal(
            self,
            login['data']['loginUser']['token'],
            delete_request_mutation,
            delete_request_response
        )

    def test_delete_request_invalid_id(self):
        """Testing for deleting a request with invalid id"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            delete_request_invalid_id,
            'The request with this id does not belong to this user'
        )

    def test_delete_approved_request(self):
        """Testing for deleting an approved request"""

        login = self.client.execute(user_login_mutation_token)
        CommonTestCases.token_assert_in(
            self,
            login['data']['loginUser']['token'],
            delete_approved_request,
            'Admin is working on this request, it can\\\'t be deleted'
        )
