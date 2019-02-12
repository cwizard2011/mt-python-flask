from flask_testing import TestCase
from graphene.test import Client
from datetime import datetime

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base

from api.users.models import User
from api.requests.models import Request


import sys
import os
import json

sys.path.append(os.getcwd())


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/mt'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            user = User(email="cwizard2011@gmail.com",
                        password="september",
                        firstname="Peter",
                        lastname="Adeoye",
                        user_role="admin")
            user.save()
            user_2 = User(email="sjuliet07@gmail.com",
                          password="september",
                          firstname="Juliana",
                          lastname="Adeoye")
            user_2.save()
            user_3 = User(email="petti4eva@yahoo.com",
                          password="september",
                          firstname="Peter",
                          lastname="Adeola")
            user_3.save()
            request = Request(title="My new request",
                              details="Setting a new request detail",
                              user_id=user_2.id,
                              current_status="approved",
                              created_at=datetime.now(),
                              updated_at=datetime.now())
            request.save()
            request_two = Request(title="New request two",
                                  details="Setting a new request detail again",
                                  user_id=user_2.id,
                                  current_status="pending",
                                  created_at=datetime.now(),
                                  updated_at=datetime.now())
            request_two.save()
            db_session.commit()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)


class CommonTestCases(BaseTestCase):
    """Common test cases throught the code.
    This code is used to reduce duplication
    :params
        - admin_token_assert_equal
        - admin_token_assert_in
        - user_token_assert_equal
        - user_token_assert_in
    """

    def admin_token_assert_equal(self, admin_token, query, expected_response):
        """
        Make a request with admin token and use assertEquals
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"token": admin_token}
        response = self.app_test.post(
            '/mt?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEqual(actual_response, expected_response)

    def user_login_assert_equal(self, query, expected_response):
        """
        Login a user
        """
        response = self.app_test.post('/mt?query=' + query)
        actual_response = json.loads(response.data)
        self.assertEqual(actual_response, expected_response)

    def user_registration_assert_in(self, query, expected_response):
        """
        Login a user
        """
        response = self.app_test.post('/mt?query=' + query)
        self.assertIn(expected_response, str(response.data))

    def admin_token_assert_in(self, admin_token, query, expected_response):
        """
        Make a request with admin token and use assertIn
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"token": admin_token}
        response = self.app_test.post('/mt?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def user_token_assert_equal(self, user_token, query, expected_response):
        """
        Make a request with user token and use assertEquals
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"token": user_token}
        response = self.app_test.post(
            '/mt?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEqual(actual_response, expected_response)

    def user_token_assert_in(self, user_token, query, expected_response):
        """
        Make a request with user token and use assertIn
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"token": user_token}
        response = self.app_test.post('/mt?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))
