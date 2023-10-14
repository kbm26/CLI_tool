from InquirerPy.validator import PathValidator
from InquirerPy import inquirer
import os
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from tabulate import tabulate
import git_remote_handler


def directory_inquirer():
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.filepath(
        message="Enter Directory:",
        default=home_path,
        validate=PathValidator(is_dir=True, message="Input is not a directory"),
        only_directories=True,
    ).execute()
    print(src_path)
    
    
def file_inquirer():
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.filepath(
        message="Enter file to upload:",
        default=home_path,
        validate=PathValidator(is_dir=True, message="Input is not a file"),
        only_files=True,
    ).execute()
    print(src_path)


def mode_selector():
    mode = inquirer.select(
        message="Select an Mode:",
        choices=[
            Separator(),
            "Create",
            Separator(),
            "Delete",
            Separator(),
            "View",
            Separator(),
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    return mode

def file_manipulation_mode():
    action = inquirer.select(
    message="What would you like to create:",
    choices=[
        Separator(),
        "File",
        Separator(),
        "Directory",
        Separator(),
        "Local + Remote Repo",
        Separator(),
        "Local Repo",
        Separator(),
        "Remote Repo",
        Separator(),
        "Issue on Repo",
        Separator(),
        Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    return action

def view_mode():
    action = inquirer.select(
    message="What would you like to create:",
    choices=[
        Separator(),
        "Directories and files",
        Separator(),
        "Repositories",
        Separator(),
        "Issues",
        Separator(),
        Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    return action

def display_issue(issues:dict):
    table = []
    for count,entry in enumerate(issues.values()):
        row = [count+1]
        print(row[0])
        row.append(replace_when_empty("title",entry))
        row.append(replace_when_empty("body",entry))
        row.append(replace_when_empty("status",entry))
        row.append(replace_when_empty("label(s)",entry))
        table.append(row)
    print(tabulate(table,headers=["No.","Title", "Body","status","Label(s)"],tablefmt="double_grid"))
        
def replace_when_empty(key:str, dict: dict):
    return " " if dict.get(key) == None else dict.get(key)
        
if __name__ == "__main__":
    display_issue(git_remote_handler.show_all_issues(git_remote_handler.find_repo(git_remote_handler.git_login(),"CLI_tool")))