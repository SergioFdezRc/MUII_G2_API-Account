GET_ACCOUNT_BY_ID = """
SELECT *
FROM account
WHERE id = %(account_id)s;
"""

UPDATE_ACCOUNT = """
UPDATE account
SET password=%(password)s
WHERE id = %(account_id)s; 
"""

NEW_ACCOUNT = """
INSERT INTO account (username, password, birthdate, age) 
    VALUES (%(username)s, %(password)s, %(birthdate)s, %(age)s);
"""

DELETE_ACCOUNT = """
DELETE FROM
account
WHERE id = %(account_id)s;
"""

GET_ACCOUNT_ID_BY_USERNAME = """
SELECT id
FROM account
WHERE username = %(username)s;
"""

GET_ACCOUNT_ID_BY_USERNAME_AND_PASSWORD = """
SELECT *
FROM account
WHERE username = %(username)s and password = %(password)s;
"""
