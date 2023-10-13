import os
import json
from pprint import pprint
from github import Github
from github import Auth
import subprocess
from InquirerPy import inquirer
import github.Repository as Repo


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
    """Creates a new Issue in a repo under your name

    Args:
        repo (Repo.Repository): Repo that will gain a new issue
        title (str): title of issue
        body (str, optional): body of issue. Defaults to "".
        label (str, optional): label of issue. Defaults to "".
        assignee (str, optional): assignee to issue. Defaults to "".
    """
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(repo.get_issues().totalCount).set_labels(label)
    
def close_issue(repo:Repo.Repository ,issue_number:int):
    """Closes a specified issue in a repo

    Args:
        repo (Repo.Repository): repo in which the issue will be closed
        issue_number (int): number of the issue that will be deleted
    """
    repo.get_issue(issue_number).edit(state="closed")


def edit_issue(repo:Repo.Repository ,issue_number:int, title:str , body:str="" ,label:str="", assignee:str=""):
    """Edits a issue

    Args:
        repo (Repo.Repository): repo of the issue that you would like edit
        issue_number (int): number of the issue you want to edit
        title (str): the new title you want to give to the issue
        body (str, optional): the new body you want to give to the issue. Defaults to "".
        label (str, optional): the new label you want to give to the issue. Defaults to "".
        assignee (str, optional): the new assignee you want to give to the issue. Defaults to "".
    """
    
    repo.create_issue(title=title,body=body,assignee=assignee)
    repo.get_issue(issue_number).set_labels(label)
        
def show_all_issues(repo:Repo.Repository) -> dict:
    """Finds all the issues in a specified repo

    Args:
        repo (Repo.Repository): repo of the issues you would like to display

    Returns:
        dict: a dictionary containing issue numbers (key) and their issues (value)
    """
    
    all_issues = {}
    for issue in repo.get_issues():
        body = issue.body.replace("\n", "").replace("\r", "").replace("```","")
        all_issues.update({f"{issue.number}":f"{body}"})
        
    for issue in repo.get_issues(state="closed"):
        if(issue.body != None):
            body = issue.body.replace("\n", "").replace("\r", "").replace("```","")
            all_issues.update({f"{issue.number}":issue})
        
    return all_issues

    
    
def find_repo(git:Github, repo_name:str) -> Repo.Repository:
    """Finds a repo with a specified name

    Args:
        git (Github): _description_
        repo_name (str): _description_

    Returns:
        Repo.Repository: _description_
    """
    user = git.get_user()
    return user.get_repo(repo_name)
    
    


if __name__ == '__main__':
    print(find_repo(git_login(),"TEST").clone_url.removeprefix("https://"))