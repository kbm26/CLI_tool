import os
import json
import pathlib
from pprint import pprint
from github import Github
from github import Auth
import subprocess
from InquirerPy import inquirer
import github.Repository as Repo
import github.Label as Label


def credentials_validator() -> bool:
    """
    Verifies whether there are user credentials present for
    the application to use
    
    Returns:
        bool: returns a bool based on the status of its existance 
    """
    try:
        directory = os.path.dirname(".secrets/creds.json")
        with open(f"{directory}/creds.json","r+") as f:
            user:dict = json.load(f)
        user.get("creds")
        return True
    except Exception :
        return False
    
def create_credentials() -> None:
    """
    Asks user for GitHub Access Token
    then creates a folder and file for the user's token
    """
    subprocess.run(["mkdir","./.secrets"])
    write_token()
        
def write_token() -> None:
    """
    write the token to the creds json
    """
    token = input("Enter Your GitHub Access Token: ")
    subprocess.run(["mkdir",".secrets"])
    creds = {
        "token": token,
    }
    
    with open(".secrets/creds.json", "w") as outfile:
        json.dump(creds, outfile)
    
def show_all_repos(git:Github) -> None:
    """Displays all repos under a user's name from github

    Args:
        git (Github): Access object to execute methods
    """
    for repo in git.get_user().get_repos():
        print(repo.name)
        
        
def git_login() -> Github:
    """Logins to user's github account

    Returns:
        Github: Access object to execute methods
    """
    directory = os.path.dirname(".secrets/creds.json")
    with open(f"{directory}/creds.json","r+") as f:
        user:dict = json.load(f)
        
    creds = user.get("token")
    auth = Auth.Token(creds)
    git = Github(auth=auth)
    git.get_user().login
    
    return git
    
    
def create_repository(git:Github, repo_name:str) -> None:
    """Creates a repository under the logged in user

    Args:
        git (Github): Access object to execute methods
        repo_name (str): The name of the repo that the user wants to make
    """
    user = git.get_user()
    user.create_repo(repo_name)
    
    
def delete_repository(repo:Repo.Repository) -> None:
    """Deletes a repository under the logged in user

    Args:
        repo (Repo.Repository): The repo object that will be deleted
    """
    repo.delete()
    
    
def create_issue(repo:Repo.Repository , title:str , body:str="" ,label:str="", assignee:str="" ):
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(repo.get_issues().totalCount).set_labels(label)
    
def close_issue(repo:Repo.Repository ,issue_number:int ):
    repo.get_issue(issue_number).edit(state="closed")


def edit_issue(repo:Repo.Repository ,issue_number:int, title:str , body:str="" ,label:str="", assignee:str=""):
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(issue_number).set_labels(label)
        
def show_all_issues(repo:Repo.Repository) :
    all_issues = {}
    for issue in repo.get_issues():
        # remove \r\n```
        all_issues.update({f"{issue.number}":f"{issue._body.value}"})
    print(all_issues)

    
    
def find_repo(git:Github, repo_name:str) -> Repo.Repository:
    user = git.get_user()
    return user.get_repo(repo_name)
    
    


if __name__ == '__main__':
    # create_issue(find_repo(git_login(),"TEST"),"final_edit_test","here is a test",label="label")
    # create_repository(git_login(),"TEST")
    show_all_issues(find_repo(git_login(),"CLI_TOOL"))