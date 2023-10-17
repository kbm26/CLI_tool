import local_file_handler as local
import git_remote_handler as remote
import cli_interface as ui

def main():
    mode = ui.mode_selection()
    match mode:
        case "Local":
            pass
        case "remote (GitHub)":
            git()

        
def git():
    if(not remote.credentials_validator()):
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
            
def git_create():
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
    choice = ui.git_mode_view()
    match choice:
        case "Remote repos":
            display_all_repos()
        case "Issue on repo":
            display_issues_in_repo()
    
def git_delete():
    choice = ui.git_mode_delete()
    match choice:
        case "Remote repo":
            delete_remote_repo()
        case "Issue on repo":
            delete_issue_on_repo()
            

def create_file():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        file = input("Name the file you want to create (with an extension eg. .txt)")
        local.make_file(f"{path}{file}")
    else:
        print("Directory not selected")
    
def delete_file():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        file = input("Name of the file you want to delete (with an extension eg. `.txt`)")
        local.delete_file(file)
    else:
        print("Directory not selected")


def create_directory():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        Directory = input("Name the Directory you want to create")
        local.make_folder(Directory)    
    else:
        print("Directory not selected")

    
    
def delete_directory():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        Directory = input("Name of the empty Directory you want to delete")
        local.delete_folder(Directory)   
    else:
        print("Directory not selected")


def view_files_and_its_contents():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        ui.show_directories_and_files(local.find_files_and_directories())
    else:
        print("Directory not selected")
        
def create_full_repo():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        name = input("Name of the empty Directory you want to delete")
        local.make_remote_and_local_repo(f"{path}{name}")
    else:
        print("Directory not selected")
        
def create_local_repo():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        name = input("Name of the empty Directory you want to delete")
        local.make_local_repo(f"{path}{name}")
    else:
        print("Directory not selected")

def create_remote_repo():
        name = input("Name of the empty Directory you want to delete")
        local.make_remote_repo(name)

        
def create_issue_on_repo():
    git = remote.git_login()
    repos = remote.show_all_repos(git)
    repo = ui.remote_repo_inquirer(repos)
    details = ui.issue_detail_inquirer()
    remote.create_issue(repo,details.get("title"),details.get("body"),details.get("label"))
        
def display_all_repos():
    repos = remote.show_all_repos(remote.git_login())
    ui.show_tabulate([[repo] for repo in repos])

def display_issues_in_repo():
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_chosen = ui.remote_repo_inquirer(repos)
    repo = remote.find_repo(auth,repo_chosen)
    issues = remote.show_all_issues(repo)
    ui.display_issues(issues)
    
def delete_remote_repo():
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_name = ui.remote_repo_inquirer(repos)
    if ui.confirmation():
        repo = remote.find_repo(auth,repo_name)
        remote.delete_repository(repo)
    
def delete_issue_on_repo():
    auth = remote.git_login()
    repos = remote.show_all_repos(auth)
    repo_name = ui.remote_repo_inquirer(repos)
    repo = remote.find_repo(auth,repo_name);
    issues = remote.show_all_issues(repo)
    issue = ui.select_issue(issues)
    issue_number = ui.find_issue_number(issue)
    if ui.confirmation():
        remote.close_issue(repo,issue_number)   


    
if __name__ == "__main__":
    delete_issue_on_repo()