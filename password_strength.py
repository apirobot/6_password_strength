import argparse
from getpass import getpass

from zxcvbn import zxcvbn

parser = argparse.ArgumentParser(description='Password Strength Calculator')
parser.add_argument('-i', '--inputs', nargs='+', type=str,
                    help='list of user inputs like name and email')
args = parser.parse_args()


def input_password():
    password = getpass(prompt='Input password: ')
    while ' ' in password:
        password = getpass(prompt='Spaces are not allowed.'
                                  ' Input correct password: ')
    return password


def get_password_strength(password, user_inputs=[]):
    """
    Gets password strength considering ``user_inputs``. Since ``zxcvbn``
    function returns score from 0 to 4 and ``get_password_strength`` should
    return score from 1 to 10, therefore ``guesses_to_score`` comes into play.

    :param user_inputs: List of strings like name or email. ``password`` that
                        includes a user's personal information can be heavily
                        penalized.
    :returns: Password strength from 1 to 10.
    """
    result = zxcvbn(password, user_inputs)

    def guesses_to_score(guesses):
        delta = 5

        if guesses < 1e3 + delta:
            return 1
        elif guesses < 1e4 + delta:
            return 2
        elif guesses < 1e5 + delta:
            return 3
        elif guesses < 1e6 + delta:
            return 4
        elif guesses < 1e7 + delta:
            return 5
        elif guesses < 1e8 + delta:
            return 6
        elif guesses < 1e9 + delta:
            return 7
        elif guesses < 1e10 + delta:
            return 8
        elif guesses < 1e11 + delta:
            return 9
        else:
            return 10

    result['score'] = guesses_to_score(result['guesses'])
    return result['score']


def main():
    password = input_password()
    if args.inputs is not None:
        password_strength = get_password_strength(password, args.inputs)
    else:
        password_strength = get_password_strength(password)

    print('Password strength: %d of 10' % password_strength)


if __name__ == '__main__':
    main()
