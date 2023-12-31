import os
import json
from pprint import pprint
from github import Github
from github import Auth
import subprocess
import github.Repository as Repo


def credentials_exist() -> bool:
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
    
def verify_credentials() -> bool:
    """Verifies credentials by running a method that needs 

    Returns:
        bool: bool of whether credentials are 
    """
    try:
        git_login().get_emojis()
        return True
    except Exception:
        return False
        
def create_credentials() -> None:
    """
    Asks user for GitHub Access Token
    then creates a folder and file for the user's token
    """
    try:
        subprocess.run(["mkdir",".secrets"],capture_output=True)
    except Exception:
        pass    
    write_token()
        
def write_token() -> None:
    """
    write the token to the creds json
    """
    token = input("Enter Your GitHub Access Token: ")
    creds = {
        "token": token,
    }
    
    with open(".secrets/creds.json", "w") as outfile:
        json.dump(creds, outfile)
    
def show_all_repos(git:Github) -> list:
    """Displays all repos under a user's name from github

    Args:
        git (Github): Access object to execute methods
        
    Returns:
        list: list of all the repos under your github account
    """
    return [repo.name for repo in git.get_user().get_repos()]
        
        
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
    
    
def create_issue(repo:Repo.Repository , title:str , body:str="" ,label:str="" ):
    """Creates a new Issue in a repo under your name

    Args:
        repo (Repo.Repository): Repo that will gain a new issue
        title (str): title of issue
        body (str, optional): body of issue. Defaults to "".
        label (str, optional): label of issue. Defaults to "".
        assignee (str, optional): assignee to issue. Defaults to "".
    """
    repo.create_issue(title=title,body=body)
    repo.get_issue(repo.get_issues().totalCount).set_labels(label)
    
def close_issue(repo:Repo.Repository ,issue_number:int):
    """Closes a specified issue in a repo

    Args:
        repo (Repo.Repository): repo in which the issue will be closed
        issue_number (int): number of the issue that will be deleted
    """
    repo.get_issue(issue_number).edit(state="closed")

def open_issue(repo:Repo.Repository ,issue_number:int):
    """Opens a specified issue in a repo

    Args:
        repo (Repo.Repository): repo in which the issue will be opened
        issue_number (int): number of the issue that will be opened
    """
    repo.get_issue(issue_number).edit(state="open")
    
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
        all_issues.update({f"{issue.number}":issue_object_formatter(issue)})
        
    for issue in repo.get_issues(state="closed"):
        all_issues.update({f"{issue.number}":issue_object_formatter(issue)})

        
    return all_issues

def issue_object_formatter(issue) -> dict:
    """Formats the issue's details into a dictionary format to be used

    Args:
        issue (Issue): issue that needs to be formatted

    Returns:
        dict: issue in the form of dict
    """
    issue_dict = {
        "title":f"{issue.title}",
        "body":"",
        "status":f"{issue.state}",
        "label(s)":[],
    }
    if(issue.body != None):
        body = issue.body.replace("\n", "").replace("\r", "").replace("```","")
        issue_dict.update({"body":f"{body}"})
    if(issue.labels != None):
        issue_dict.update({"label(s)":[label.name for label in issue.labels]})
    return issue_dict
        


    
    
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
    