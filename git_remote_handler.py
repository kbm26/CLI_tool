import os
import json
import pathlib
from pprint import pprint
from github import Github
from github import Auth
"""
Set up github and gitlab apis
"""
def setup():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "creds.json")
    
    if pathlib.Path(file_path).exists():
        with open(file_path) as f:
            data:dict = json.load(f)
        print(data.get("creds"))
    else:
        print("You need to enter your GitHub Token with relevant premissions")
        add_token()
        
def add_token():
    token = input("Enter your GitHub Access Token")
    with open("user_info.json") as file:
        file.write(token)
    
if __name__ == '__main__':
    print("work")