import os
import json
import pathlib
from pprint import pprint
from github import Github
from github import Auth
import subprocess


def credentials_validator() -> bool:
    """
    Verifies whether there are user credentials present for
    the application to use
    
    Returns:
        bool: returns a bool based on the status of its existance 
    """
    try:
        directory = os.path.dirname(".secrets/creds.json")
        with open(directory,"r+") as f:
            user:dict = json.load(f)
        user.get("creds")
        return True
    except e :
        return False
    
def create_credentials() -> None:
    """
    Asks user for GitHub Access Token
    then creates a folder and file for the user's token
    """
    token = input("Enter Your GitHub Access Token: ")
    # subprocess.run(["mkdir",".secrets"])
    creds = {
        "token": token,
    }
    
    with open(".secrets/creds.json", "w") as outfile:
        json.dump(creds, outfile)
        
    def show_all_repos() -> None:
    # auth = Auth.Login("")

    # g = Github(auth=auth)

    # g.get_user().login

    # # Github Enterprise with custom hostname

    # for repo in g.get_user().get_repos():
    #     print(repo.name)
    #     # to see all the available attributes and methods
    #     print(dir(repo))

    # g.close()
        pass

    
if __name__ == '__main__':
    create_credentials()