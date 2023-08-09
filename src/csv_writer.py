import json

from files import JSON_FILE_PATH

with open(JSON_FILE_PATH, 'r') as f:
    users = json.load(f)
age_list = ['friends ']
for age in age_list:
    print(age)