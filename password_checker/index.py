import requests
import hashlib
import sys
from simple_chalk import chalk

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res    

def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five,tail = sha1password[0:5], sha1password[5:] 
    response = request_api_data(first_five)
    return get_password_leaks(response,tail)

f = open('passwords.txt', 'a')
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{chalk.red(password)} was found {chalk.yellow(count)} times, You should change the password")
            f.write(f"{password} was found {count} times, You should change the password\n")
        else:
            print(f"{chalk.green(password)} was not found")
            f.write(f"{password} was not found\n")
    return "done"            

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    f.close()
