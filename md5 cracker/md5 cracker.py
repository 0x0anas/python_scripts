import hashlib
import getopt
import sys

pass_found = 0
input_hash = ""
pass_doc = ""

def usage():
    print(f'python3 {sys.argv[0]} -p <hashed_password> -w <passwords_wordlist>')

def main():
    global pass_found
    global input_hash
    global pass_doc

    if len(sys.argv) < 3:
        usage()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hp:w:', ['help', 'password=', 'wordlist='])
    except getopt.GetoptError as err:
        print(f'Error: {err}')
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ['-h', '--help']:
            usage()
            sys.exit()
        elif o in ['-p', '--password']:
            input_hash = a
        elif o in ['-w', '--wordlist']:
            pass_doc = a

    try:
        pass_file = open(pass_doc, 'r')
    except FileNotFoundError:
        print(f'Error: File Not Found - {pass_doc}')
        sys.exit(2)

    for word in pass_file:
        enc_word = word.strip().encode('utf-8')
        hash_word = hashlib.md5(enc_word).hexdigest()
        if hash_word == input_hash:
            print(f'Password Found.\nThe cracked password is: {word}')
            pass_found = 1
            break

    if not pass_found:
        print('Password Not Found')

if __name__ == "__main__":
    main()
