from InquirerPy.validator import PathValidator
from InquirerPy import inquirer
import os
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import InquirerPy.prompts.filepath as file_finder
from tabulate import tabulate

def directory_inquirer() -> str:
    """Prompts the user for a directory

    Returns:
        str: direvtory that the user chose
    """
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.text(
        message="Select Directory:",
        default=home_path,
        validate=PathValidator(is_dir=True, message="Input is not a file"),
        completer=file_finder.FilePathCompleter(only_files=False,only_directories=True)
    ).execute()
    return src_path
    
    
def file_inquirer(directory:str) -> str:
    """Prompts the user for a file

    Args:
        directory (str): Directory in which the file is in

    Returns:
        str: file name
    """
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.text(
        message="Select File:",
        default=directory,
        validate=PathValidator(is_file=True, message="Input is not a file"),
        completer=file_finder.FilePathCompleter(only_files=True,only_directories=False)
    ).execute()
    return src_path

def remote_repo_inquirer(repos_list: list) -> str:
    """Prompts user for a remote repo

    Args:
        repos_list (list): list remote repos

    Returns:
        str: repo name
    """
    repo = inquirer.select(
        message="Select Repo:",
        choices=repos_list
    ).execute()
    return repo

def repo_issue_inquirer(issue_list: list) -> str:
    """Prompts user for a issue on a remote repo 

    Args:
        issue_list (list): list of issues

    Returns:
        str: issue chosen
    """
    repo = inquirer.select(
        message="Select issue:",
        choices=issue_list
    ).execute()
    return repo

def confirmation() -> bool:
    """Prompts user for confirmation on action

    Returns:
        bool: Confirmation
    """
    proceed = False
    proceed = inquirer.confirm(message="Confirm?", default=True).execute()
    return proceed

def mode_selection() -> str:
    """Prompts user for a mode to use

    Returns:
        str: mode selected
    """
    return select_menu([
            Separator(),
            "Local",
            Separator(),
            "remote (GitHub)",
            Separator(),
            Choice(value=None, name="Exit"),
        ],"Select an Mode: ")

def local_action_selector() -> str:
    """Prompts user for the action they want to do with local files

    Returns:
        str: action selected
    """
    return select_menu([
            Separator(),
            "Create",
            Separator(),
            "Delete",
            Separator(),
            "View",
            Separator(),
            Choice(value=None, name="Exit"),
        ],"What would you like to do: ")

def file_manipulation_action(mode:str) -> str:
    """Prompts user for the type of local file they would like to apply an action for

    Args:
        mode (str): action that will be applied to the file chosen

    Returns:
        str: file/ directory
    """
    return select_menu([
        Separator(),
        "File",
        Separator(),
        "Directory", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],f"What would you like to {mode}: ")


    
def git_mode() -> str:
    """Prompts user for action to be performed involving git

    Returns:
        str: mode selected
    """
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
        ],"What would you like to do: ")
    
def git_mode_create() -> str:
    """Prompts user for item to be created
    Returns:
        str: item selected
    """
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
        ],"What would you like to create: "
    )
    
def git_mode_delete() -> str:
    """Prompts user for item to be Deleted
    Returns:
        str: item selected
    """
    return select_menu(
        [
        Separator(),
        "Remote repo",
        Separator(),
        "Issue on repo", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to delete: "
    )
    
def git_mode_view() -> str:
    """Prompts user for item to be viewed
    Returns:
        str: item selected
    """
    return select_menu([
        Separator(),
        "Issues on repo",
        Separator(),
        "Remote repos", 
        Separator(),
        Choice(value=None, name="Exit"),
        ],"What would you like to view: ")
        
        
def display_issues(issues:dict) -> None:
    """Display issues on remote repo

    Args:
        issues (dict): issue to be displayed
    """
    table = []
    for count,entry in enumerate(issues.values()):
        table.append(issue_details(entry,count))
    print(tabulate(table,headers=["No.","Title", "Body","status","Label(s)"],tablefmt="double_grid"))
        
def select_issue(issues:dict) -> str:
    """Prompts user for the issue to be affected

    Args:
        issues (dict): issues

    Returns:
        str: issue
    """
    table = []
    for count,entry in enumerate(issues.values()):
        details = issue_details(entry,count)
        table.append(Separator())
        table.append(f"{details[0]} | {details[1]} | {details[2]} | {details[3]} | {details[4]}")
    table.append(Choice(value=None, name="Exit"))
    action  = select_menu(table,"Select An Issue (index | title | body | status | label(s)): ")
    return action
    
def issue_details(issue:dict, count:int) -> list:
    """creates a list of issue details

    Args:
        issue (dict): issue
        count (int): number of issue

    Returns:
        list: list of issue details
    """
    row = [count+1]
    row.append(replace_when_empty("title",issue))
    row.append(replace_when_empty("body",issue))
    row.append(replace_when_empty("status",issue))
    row.append(replace_when_empty("label(s)",issue))
    return row

def find_issue_number(issue:str) -> int:
    """finds issue number

    Args:
        issue (str): issue

    Returns:
        int: _description_
    """
    issue_number_list = [num for count,num in enumerate(issue) if num.isdecimal() and count<= 3]
    return int("".join(issue_number_list))

    
def replace_when_empty(key:str, dict: dict) -> str:
    """Replaces empty space with None in an issue

    Args:
        key (str): key of issue
        dict (dict): issue

    Returns:
        str: issue
    """
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

def issue_detail_inquirer() -> str:
    """Prompts user for details on issue that is going to be created

    Returns:
        str: created issue 
    """
    title = inquirer.text(message="Enter the title of the issue: ").execute()
    body = inquirer.text(message="Enter the body of the issue: ").execute()
    label = inquirer.text(message="Enter the label of the issue: ").execute()
    issue = {
        "title":title,
        "body":body,
        "label":label
    }
    return issue


def show_tabulate(items:list,header) -> None:
    """Displays data in a table format

    Args:
        items (list): data for table
        header (_type_): Heading(s)
    """
    print(tabulate(items,tablefmt="double_grid",headers=[f"{header}"]))
        
if __name__ == "__main__":
    print(file_inquirer())