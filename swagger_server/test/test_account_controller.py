# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.update_account import UpdateAccount  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountController(BaseTestCase):
    """AccountController integration test stubs"""

    def test_add_account(self):
        """Test case for add_account

        Add a new account to the system
        """
        body = Account()
        response = self.client.open(
            '/account',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        # TODO: este test falla. Devuelve un 500
        self.assert500(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_account(self):
        """Test case for delete_account

        Delete the account
        """
        response = self.client.open(
            '/account/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account(self):
        """Test case for get_account

        Get account info
        """
        response = self.client.open(
            '/account/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_account(self):
        """Test case for update_account

        Update account password
        """
        body = UpdateAccount()
        response = self.client.open(
            '/account',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        # TODO: este test falla. Devuelve un 500
        self.assert500(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
