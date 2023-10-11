import os
import json
import pathlib
from pprint import pprint
from github import Github
from github import Auth
import subprocess
from InquirerPy import inquirer


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
        
    git_close(git)
        
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
    
def git_close(git:Github) :
    """Closes the github access object for security reasons

    Args:
        git (Github): Access object to execute methods
    """
    git.close()
    
    
def change_issue_label(git:Github, label:str) -> None:
    """Changes the label of a single commit from a repo

    Args:
        git (Github): Access object to execute methods
        label (str): The new name of the label for the issue
    """
    # Will change
    for repo in git.get_user().get_repos():
        print(repo.name)
        for issue in repo.get_issues():
            print(issue.set_labels("completed"))
            
    git_close(git)
    
    
def create_repository(git:Github, repo_name:str) -> None:
    """Creates a repository under the logged in user

    Args:
        git (Github): Access object to execute methods
        repo_name (str): The name of the repo that the user wants to make
    """
    user = git.get_user()
    user.create_repo(repo_name)
    
    
def delete_repository(git:Github, repo_name:str) -> None:
    """Deletes a repository under the logged in user

    Args:
        git (Github): Access object to execute methods
        repo_name (str): The name of the repo that the user wants to delete
    """
    user = git.get_user()
    repo = user.get_repo(repo_name)
    repo.delete()
    
    
def create_issues(git:Github, repo_name:str , title:str , body:str="" ,label:str="", assignee:str="" ):
    user = git.get_user()
    repo = user.get_repo(repo_name)
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(repo.get_issues().totalCount).set_labels(label)
    git_close(git)
    
def close_issues(git:Github, repo_name:str ,issue_number:int ):
    user = git.get_user()
    repo = user.get_repo(repo_name)
    repo.get_issue(issue_number)

    git_close(git)


def edit_issues(git:Github, repo_name:str ,issue_number:int, title:str , body:str="" ,label:str="", assignee:str=""):
    user = git.get_user()
    repo = user.get_repo(repo_name)
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(issue_number).set_labels(label)
    
    git_close(git)


if __name__ == '__main__':
    create_issues(git_login(),"CLI_tool","test","here is a test","backlog")