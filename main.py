import random
import argparse
import string


parser = argparse.ArgumentParser(prog='main')
parser.add_argument(
    'Length',
    metavar='Password Length',
    type=int,
    help="The length of your randomly generated password",
)

parser.add_argument(
    '-C',
    '--capital',
    action="store_true",  
    help="Adds capital letters into the password generation", 
    default=False)

parser.add_argument(
    '-P',
    '--punctuation',
    action="store_true",  
    help="Adds symbol characters into the password generation", 
    default=False)

parser.add_argument(
    '-D',
    '--digits',
    action="store_true",  
    help="Adds digits into the password generation", 
    default=False)
args = parser.parse_args()

def generate():  
    length = args.Length
    if length < 8:
        print("You must enter a value above 7 to get a secure password.")
        print("Thank you for using my password generator!")
        exit()

    letters = string.ascii_lowercase

    options = {
        'Capital': 'No',
        'Punctuation': 'No',
        'Digits': 'No'
    }

    if args.capital:
        letters = letters + string.ascii_uppercase
        options.update({'Capital':'Yes'})

    if args.punctuation:
        letters = letters + string.punctuation
        options.update({'Punctuation':'Yes'})

    if args.digits:
        letters = letters + string.digits
        options.update({'Digits':'Yes'})

    password = ''.join(random.choice(letters) for i in range(length))

    print("########################" + '#'*len(password)+ "\n")
    print("Capital:", options['Capital'])
    print("Punctuation:", options["Punctuation"])
    print("Digits:", options["Digits"])
    print(f"Password: {password}" + "\n")
    print("########################"+ '#'*len(password))
    print("Thank you for using my password generator!")
    

if __name__ == "__main__":
    generate()
