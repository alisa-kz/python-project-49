import prompt


def welcome_user():
    """
    Greets the user by name and return user name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)
