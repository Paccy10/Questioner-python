VALID_USER = {
    'firstname': 'Fabrice',
    'lastname': 'Manzi',
    'othername': '',
    'email': 'fabrice.manzi@andela.com',
    'password': 'Password'
}

INVALID_USER_WITHOUT_FIRSTNAME = {
    'firstname': '',
    'lastname': 'Manzi',
    'othername': '',
    'email': 'fabrice.manzi@andela.com',
    'password': 'Password'
}

INVALID_USER_WITHOUT_LASTNAME = {
    'firstname': 'Fabrice',
    'lastname': '',
    'othername': '',
    'email': 'fabrice.manzi@andela.com',
    'password': 'Password'
}

INVALID_USER_WITHOUT_EMAIL = {
    'firstname': 'Fabrice',
    'lastname': 'Manzi',
    'othername': '',
    'email': '',
    'password': 'Password'
}

INVALID_USER_WITHOUT_PASSWORD = {
    'firstname': 'Fabrice',
    'lastname': 'Manzi',
    'othername': '',
    'email': 'fabrice.manzi1@andela.com',
    'password': ''
}

INVALID_USER_WITH_INVALID_EMAIL = {
    'firstname': 'Fabrice',
    'lastname': 'Manzi',
    'othername': '',
    'email': 'fabricemanziandelacom',
    'password': 'Password'
}

INVALID_USER_WITH_INVALID_PASSWORD = {
    'firstname': 'Fabrice',
    'lastname': 'Manzi',
    'othername': '',
    'email': 'fabricemanzi10@andela.com',
    'password': 'Pass'
}

LOGIN_USER_DATA = {
    'email': 'fabrice.manzi@andela.com',
    'password': 'Password'
}

LOGIN_USER_DATA_WITHOUT_EMAIL = {
    'email': '',
    'password': 'Password'
}

LOGIN_USER_DATA_INVALID_EMAIL = {
    'email': 'fabricemanziandelacom',
    'password': 'Password'
}

LOGIN_USER_DATA_WITHOUT_PASSWORD = {
    'email': 'fabrice.manzi@andela.com',
    'password': ''
}

LOGIN_USER_DATA_WITH_INCORRECT_PASSWORD = {
    'email': 'fabrice.manzi@andela.com',
    'password': '123456'
}

LOGIN_UNREGISTERED_USER = {
    'email': 'pacifique.ndayisenga@andela.com',
    'password': '123456'
}
