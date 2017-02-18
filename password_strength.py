import argparse
from getpass import getpass
from math import log10

from zxcvbn import zxcvbn


def create_parser():
    parser = argparse.ArgumentParser(description='Password Strength Calculator')
    parser.add_argument('-i', '--inputs', nargs='+', type=str,
                        help='list of user inputs like name and email')
    return parser


def input_password():
    password = getpass(prompt='Input password: ')
    while ' ' in password:
        password = getpass(prompt='Spaces are not allowed.'
                                  ' Input correct password: ')
    return password


def get_password_strength(password, user_inputs=[]):
    """
    Gets password strength considering ``user_inputs``.

    :param user_inputs: List of strings like name or email. ``password`` that
                        includes a user's personal information can be heavily
                        penalized.
    :param guesses: How many guesses need to iterate through
                    to crack a password.
    :returns: Password strength from 1 to 10.
    """
    result = zxcvbn(password, user_inputs)

    # Since ``zxcvbn`` function returns score from 0 to 4 and
    # ``get_password_strength`` should return score from 1 to 10,
    # therefore result['score'] should be changed.
    guesses = result['guesses']
    if guesses < 1e3:
        result['score'] = 1
    elif guesses < 1e11:
        result['score'] = int(log10(guesses / 10))
    else:
        result['score'] = 10

    return result['score']


def main():
    parser = create_parser()
    args = parser.parse_args()

    password = input_password()
    if args.inputs is not None:
        password_strength = get_password_strength(password, args.inputs)
    else:
        password_strength = get_password_strength(password)

    print('Password strength: %d of 10' % password_strength)


if __name__ == '__main__':
    main()
