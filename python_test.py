import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
import csv

hashed_passwords = list()
hashed_emails = list()
clear_passwords = list()
clear_emails = list()

hashed_df = pd.DataFrame(columns=['Email', 'Hashed Password'])
email = input('[+] Enter email to check... ')
url = str("https://api.dehashed.com/search?query=email:" + email + '&size=10000')
hashed_file = 'C:/Users/user/Desktop/Hashes/' + email + '_hashed_passwords.csv'
clear_file = 'C:/Users/user/Desktop/Hashes/' + email + '_clear_passwords.csv'
headers = {
    'Accept': 'application/json',
}
params = (
    ('query', 'email:'+ email),
)
auth = (
    ("tester@gmail.com:dvgelfnkua3mxnrkmo3yh3uir3y6xud9")
)

r = requests.get(url, headers=headers, params=params, auth=HTTPBasicAuth('tester@gmail.com', 'dvgelfnkua3mxnrkmo3yh3uir3y6xud9'))
r_json = json.loads(r.text)

for hash_pw in r_json['entries']:
    if hash_pw['hashed_password']:
        hashed_emails.append(hash_pw['email'])
        hashed_passwords.append(hash_pw['hashed_password'])

        # print(hash_pw['hashed_password'], hash_pw['hashed_password'])
        # hashed_passwords.append(hash_pw['email'])
        # hashed_passwords.append(hash_pw['hashed_password'])
    else:
        pass
for clear_pw in r_json['entries']:
    if clear_pw['password']:
        # print(hash_pw['email'], hash_pw['password'])
        clear_emails.append(clear_pw['email'])
        clear_passwords.append(clear_pw['password'])
    else:
        pass

hashed_tuples = list(zip(hashed_emails, hashed_passwords))
clear_tuples = list(zip(clear_emails, clear_passwords))
df_hashed_pw = pd.DataFrame(hashed_tuples, columns=['Email', 'Hashed Password'])
df_clear_pw = pd.DataFrame(clear_tuples, columns=['Email', 'Clear Passwords'])

if os.path.exists(hashed_file):
    os.remove(hashed_file)
if os.path.exists(clear_file):
    os.remove(clear_file)
else:
    pass

df_hashed_pw.to_csv(hashed_file, encoding='utf-8', index=False)
df_clear_pw.to_csv(clear_file, encoding='utf-8', index=False)


def file_create():
    in_file = 'C:/Users/user/Desktop/Hashes/' + email + '_hashed_passwords.csv'
    out_file = 'D:/Tools/Hashes/' + email + '_hc_file.txt'
    if os.path.exists(out_file):
        os.remove(out_file)
    with open(in_file) as f:
        reader = csv.reader(f)
        with open(out_file, 'w') as g:
            writer = csv.writer(g)
            for row in reader:
                new_row = [':'.join([row[0], row[1]])] + row[2:]
                writer.writerow(new_row)
