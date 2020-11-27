# coding: utf-8

from __future__ import absolute_import

from unittest import mock

from flask import json

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.update_account import UpdateAccount  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountController(BaseTestCase):
    """AccountController integration test stubs"""

    @mock.patch("swagger_server.db.Database.PostgresDB.add_new_account")
    @mock.patch("swagger_server.db.Database.PostgresDB.get_account_id_by_username")
    def test_add_account(self, mocked_get_account_id_by_username, mocked_add_new_account):
        """Test case for add_account

        Add a new account to the system
        """
        body = Account()
        mocked_get_account_id_by_username.return_value = []
        mocked_add_new_account.assert_not_called()
        response = self.client.open(
            '/account',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        mocked_add_new_account.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("swagger_server.db.Database.PostgresDB.delete_account")
    @mock.patch("swagger_server.db.Database.PostgresDB.get_account_by_id")
    def test_delete_account(self, mocked_get_account_by_id, mocked_delete_account):
        """Test case for delete_account

        Delete the account
        """
        mocked_get_account_by_id.return_value = [1]
        response = self.client.open(
            '/account/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("swagger_server.db.Database.PostgresDB.get_account_by_id")
    def test_get_account(self, mocked_get_account_by_id):
        """Test case for get_account

        Get account info
        """
        mocked_get_account_by_id.return_value = [
            [1, "mocked_user", "mocked_pass", '2020-01-01', 30]
        ]

        response = self.client.open(
            '/account/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("swagger_server.db.Database.PostgresDB.update_account")
    @mock.patch("swagger_server.db.Database.PostgresDB.get_account_id_by_username_and_password")
    def test_update_account(self, mocked_get_account_id_by_username_and_password, mocked_update_account):
        """Test case for update_account

        Update account password
        """
        body = UpdateAccount('username', 'old_password', 'new_password')
        mocked_get_account_id_by_username_and_password.return_value = [
            [1, "mocked_user", "mocked_pass", '2020-01-01', 30]
        ]
        mocked_update_account.assert_not_called()
        response = self.client.open(
            '/account',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
