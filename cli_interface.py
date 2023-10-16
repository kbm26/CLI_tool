from InquirerPy.validator import PathValidator
from InquirerPy import inquirer
import os
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import InquirerPy.prompts.filepath as file_finder
from tabulate import tabulate

def directory_inquirer() -> str:
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.text(
        message="Select Directory:",
        default=home_path,
        validate=PathValidator(is_dir=True, message="Input is not a file"),
        completer=file_finder.FilePathCompleter(only_files=False,only_directories=True)
    ).execute()
    return src_path
    
    
def file_inquirer() -> str:
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.text(
        message="Select File:",
        default=home_path,
        validate=PathValidator(is_file=True, message="Input is not a file"),
        completer=file_finder.FilePathCompleter(only_files=True,only_directories=False)
    ).execute()
    return src_path

def remote_repo_inquirer(repos_list: list) -> str:
    repos = { repo:None for repo in repos_list}
    repo = inquirer.text(
        message="Select Repo:",
        validate= lambda repo : repo in repos_list,
        completer=repos
    ).execute()
    return repo

def mode_selector() -> str:
    return select_menu([
            Separator(),
            "Create",
            Separator(),
            "Delete",
            Separator(),
            "View",
            Separator(),
            "Git (GitHub)",
            Separator(),
            Choice(value=None, name="Exit"),
        ],"Select an Mode: ")

def file_manipulation_mode() -> str:
    return select_menu([
        Separator(),
        "File",
        Separator(),
        "Directory", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to create: ")


    
def git_mode() -> str:
    return select_menu([
        Separator(),
        "Change/Insert Token",
        Separator(),
        "Create", 
        Separator(),
        "Delete", 
        Separator(),
        "View", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to view: ")
    
def git_mode_create():
    return select_menu(
        [
        Separator(),
        "Remote & Local repo",
        Separator(),
        "Remote repo", 
        Separator(),
        "Local repo", 
        Separator(),
        "Issue on repo", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to view: "
    )
    
def git_mode_delete():
    return select_menu(
        [
        Separator(),
        "Remote repo",
        Separator(),
        "Issue on repo", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to view: "
    )
    
def git_view_mode() -> str:
    return select_menu([
        Separator(),
        "Issues on repos",
        Separator(),
        "Remote repos", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to view: ")
        
        
def display_issue(issues:dict) -> None:
    table = []
    for count,entry in enumerate(issues.values()):
        table.append(issue_details(entry,count))
    print(table,headers=["No.","Title", "Body","status","Label(s)"],tablefmt="double_grid")
        
def select_issue(issues:dict) -> None:
    table = []
    for count,entry in enumerate(issues.values()):
        details = issue_details(entry,count)
        table.append(Separator())
        table.append(f"{details[0]} | {details[1]} | {details[2]} | {details[3]} | {details[4]}")
    table.append(Choice(value=None, name="Exit"))
    action  = select_menu(table,"Select An Issue (index | title | body | status | label(s)): ")
    print((find_issue_number(action)))
    
def issue_details(issue:dict, count:int) -> list:
        row = [count+1]
        row.append(replace_when_empty("title",issue))
        row.append(replace_when_empty("body",issue))
        row.append(replace_when_empty("status",issue))
        row.append(replace_when_empty("label(s)",issue))
        return row

def find_issue_number(issue:str) -> int:
    issue_number_list = [num for count,num in enumerate(issue) if num.isdecimal() and count<= 3]
    return int("".join(issue_number_list))

    
def replace_when_empty(key:str, dict: dict) -> str:
    return "None" if  dict.get(key) == "" or dict.get(key) == [] else dict.get(key)

def select_menu (choices:list, message:str) -> str:
    action:str = inquirer.select(
    message=message,
    choices=choices,
        border=True,
        default=None,
        wrap_lines=True,
        cycle=True,
    ).execute()
    return action

def show_tabulate(items:str) -> None:
    print(tabulate(items))
        
if __name__ == "__main__":
    print(file_inquirer())