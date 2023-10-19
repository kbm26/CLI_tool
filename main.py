import local_file_handler as local
import git_remote_handler as remote
import cli_interface as ui

def main():
    """ Main method that runs the app
    """
    mode = ui.mode_selection()
    match mode:
        case "Local":
            local_mode()
        case "remote (GitHub)":
            git_mode()

        
def git_mode():
    """Handles git methods
    """
    if(not remote.credentials_exist() or not remote.verify_credentials()):
        remote.create_credentials()
    else:
        choice = ui.git_mode()
        match choice:
            case "Change/Insert Token":
                remote.create_credentials()
            case "View":
                git_view()
            case "Create":
                print("not here")
                git_create()
            case "Delete":
                git_delete()
                
def local_mode():
    """Handles local methods
    """
    action = ui.local_action_selector()
    if action == "View":
        view_files_and_its_contents()
    else:
        choice = ui.file_manipulation_action(action)
        match choice:
            case "File":
                file_action(action)
            case "Directory":
                directory_action(action)

    
    
def file_action(action:str):
    """Handles whether a file will be created or deleted

    Args:
        action (str): created/deleted
    """
    if action == "Create":
        create_file()
    else:
        delete_file()
    
def directory_action(action:str):
    """Handles whether a directory will be created or deleted

    Args:
        action (str): created/deleted
    """
    if action == "Create":
        create_directory()
    else:
        delete_directory()
    
            
def git_create():
    """Handles git create methods
    """
    choice = ui.git_mode_create()
    match choice:
        case "Remote & Local repo":
            create_full_repo()
        case "Remote repo":
            create_remote_repo()
        case "Local repo":
            create_local_repo()
        case "Issue on repo":
            create_issue_on_repo()
        
def git_view():
    """Handles git view methods
    """
    choice = ui.git_mode_view()
    match choice:
        case "Remote repos":
            display_all_repos()
        case "Issues on repo":
            display_issues_in_repo()
    
def git_delete():
    """Handles git delete methods
    """
    choice = ui.git_mode_delete()
    match choice:
        case "Remote repo":
            delete_remote_repo()
        case "Issues on repo":
            delete_issue_on_repo()
            

def create_file():
    """Calls methods needed to create a file
    """
    path = ui.directory_inquirer()
    true_path = path_completer(path)
    file = input("Name the file you want to create (with an extension eg. .txt) ")
    local.make_file(f"{true_path}{file}")

    
def delete_file():
    """Calls methods needed to delete a file
    """
    path = ui.directory_inquirer()
    true_path = path_completer(path)
    file = ui.file_inquirer(true_path)
    if ui.confirmation():
        local.delete_file(file)



def create_directory():
    """Calls methods needed to create a directory
    """
    path = ui.directory_inquirer()
    ui.file_inquirer()
    true_path = path_completer(path)
    local.make_folder(true_path)    


    
    
def delete_directory():
    """Calls methods needed to delete a directory
    """
    path = ui.directory_inquirer()
    if ui.confirmation():
        local.delete_folder(path)   



def view_files_and_its_contents():
    """Calls methods needed to view a directory and its content
    """
    path = ui.directory_inquirer()
    true_path = path_completer(path)
    ui.show_tabulate(local.find_files_and_directories(true_path),"Contents")

        
def create_full_repo():
    """Calls methods needed to create a full repo
    """
    path = ui.directory_inquirer()
    true_path = path_completer(path)
    name = input("Name of the full repo you want to create: ")
    local.make_remote_and_local_repo(true_path,name)

        
def create_local_repo():
    """Calls methods needed to create a local repo
    """
    path = ui.directory_inquirer()
    true_path = path_completer(path)
    name = input("Name of the local repo you want to create: ")
    local.make_local_repo(f"{true_path}{name}")


def create_remote_repo():
    """Calls methods needed to create a remote repo
    """
    name = input("Name of Repo: ")
    local.make_remote_repo(name)

        
def create_issue_on_repo():
    """Calls methods needed to create a issue on a remote repo
    """
    git = remote.git_login()
    repos = remote.show_all_repos(git)
    repo_name = ui.remote_repo_inquirer(repos)
    repo = remote.find_repo(git,repo_name)
    details = ui.issue_detail_inquirer()
    remote.create_issue(repo,details.get("title"),details.get("body"),details.get("label"))
        
def display_all_repos():
    """Calls methods needed to display all remote repo
    """
    repos = remote.show_all_repos(remote.git_login())
    ui.show_tabulate([[repo] for repo in repos],"Repositories")

def display_issues_in_repo():
    """Calls methods needed to display all issues on a remote repo
    """
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_chosen = ui.remote_repo_inquirer(repos)
    repo = remote.find_repo(auth,repo_chosen)
    issues = remote.show_all_issues(repo)
    ui.display_issues(issues)
    
def delete_remote_repo():
    """Calls methods needed to delete a remote repo
    """
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_name = ui.remote_repo_inquirer(repos)
    if ui.confirmation():
        repo = remote.find_repo(auth,repo_name)
        remote.delete_repository(repo)
    
def delete_issue_on_repo():
    """Calls methods needed to delete a issue on a remote repo
    """
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_name = ui.remote_repo_inquirer(repos)
    repo = remote.find_repo(auth,repo_name)
    issues = remote.show_all_issues(repo)
    issue = ui.select_issue(issues)
    issue_number = ui.find_issue_number(issue)
    if ui.confirmation():
        remote.close_issue(repo,issue_number)   


def path_completer(path:str) -> str:
    """completes a path

    Args:
        path (str): path that needs to be completed

    Returns:
        str: _description_
    """
    if [*path][-1] != "/":
        return f"{path}/"
    else:
        return path
    
if __name__ == "__main__":
    main()