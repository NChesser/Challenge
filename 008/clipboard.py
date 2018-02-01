import pyperclip
import sys

# can use this to copy my passwords from somewhere

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python')
    sys.exit()

account = sys.argv[1]   # this is the first command line argument

def get_password(account):
    pyperclip.copy(PASSWORDS[account])


get_password(account)

print(pyperclip.paste())