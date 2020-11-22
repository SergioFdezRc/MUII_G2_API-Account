import connexion
import six

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.update_account import UpdateAccount  # noqa: E501
from swagger_server import util


def add_account(body):  # noqa: E501
    """Add a new account to the system

    Adds a user account to the system # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Account.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_account(id):  # noqa: E501
    """Delete the account

    Delete a given user account # noqa: E501

    :param id: Account id
    :type id: int

    :rtype: str
    """
    return 'do some magic!'


def get_account(id):  # noqa: E501
    """Get account info

    Get a given user name # noqa: E501

    :param id: The user id of the  logged in user
    :type id: int

    :rtype: str
    """
    return 'do some magic!'


def update_account(body):  # noqa: E501
    """Update account password

    Update a given account. The user name cannot be modified. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UpdateAccount.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'