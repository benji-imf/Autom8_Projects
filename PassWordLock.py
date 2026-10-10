# This is a password locker program.
# An insecure one ;)

import sys, pyperclip

PASSWORDS = {"email": 'abcde123',
             "blog": 'zxqwe23',
             "luggage": '12345'}

if len(sys.argv) < 2:
    print('Usage: python PassWordLock.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
