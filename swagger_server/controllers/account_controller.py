import connexion
from flask import jsonify

from swagger_server.db.Database import PostgresDB
from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.update_account import UpdateAccount  # noqa: E501


def add_account(account):  # noqa: E501
    """Add a new account to the system

    Adds a user account to the system # noqa: E501

    :param account:
    :type account: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        account = Account.from_dict(connexion.request.get_json())  # noqa: E501
        db = PostgresDB()
        info = db.get_account_id_by_username(account.username)
        if len(info) > 0:
            return 'The user %s already exists' % account.username, 409
        db.add_new_account(account.username, account.password, account.birthdate, account.age)

    return "OK. User %s created" % account.username, 200


def delete_account(account_id):  # noqa: E501
    """Delete the account

    Delete a given user account # noqa: E501

    :param account_id: Account id
    :type account_id: int

    :rtype: str
    """
    db = PostgresDB()

    account = db.get_account_by_id(account_id)
    if len(account) > 0:
        db.delete_account(account_id)
        return 'The account has been removed', 200
    else:
        return 'Account not found' % account_id, 404


def get_account(account_id):  # noqa: E501
    """Get account info

    Get a given user name # noqa: E501

    :param account_id: The user id of the  logged in user
    :type account_id: int

    :rtype: str
    """
    db = PostgresDB()
    account = db.get_account_by_id(account_id)
    if len(account) > 0:
        account = account[0]
        return jsonify({"username": account[1],
                        "birthdate": account[3],
                        "age": account[4]})

    return 'Account not found', 404


def update_account(update_account):  # noqa: E501
    """Update account password

    Update a given account. The user name cannot be modified. # noqa: E501

    :param update_account:
    :type update_account: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        update_account = UpdateAccount.from_dict(connexion.request.get_json())  # noqa: E501
        db = PostgresDB()
        info = db.get_account_id_by_username_and_password(update_account.username, update_account.old_password)
        if len(info) > 0:
            info = info[0]
            if update_account.old_password == update_account.new_password:
                return 'Passwords match', 409
            db.update_account(info[0], update_account.new_password)
            return "Password changed", 200
        return 'Incorrect password', 204
    return 'invalid format', 405
