import subprocess
import git_remote_handler as git

def make_remote_and_local_repo(repo_dir:str,repo_name:str) -> None:
    """Calls methods and creates both a remote and local repo in a new project directory

    Args:
        repo_dir (str): repo directory
        repo_name (str): repo name
    """
    auth = git.git_login()
    make_remote_repo(repo_name)
    repo = git.find_repo(auth,repo_name)
    path = f"{repo_dir}{repo_name}"
    make_local_repo(f"{repo_dir}{repo_name}")
    make_file(f"{repo_dir}{repo_name}/text.txt")
    subprocess.run([f"git -C {path} add ."],shell=True)
    subprocess.run([f"git -C {path} branch -M main"],shell=True)
    subprocess.run([f"git -C {path} commit -m \"first commit\""],shell=True)
    subprocess.run([f"git -C {path} remote add origin {repo.clone_url}"],shell=True)
    subprocess.run([f"git -C {path} push -u origin main"],shell=True)
    
def make_remote_repo(repo_name:str) -> None:
    """Makes a remote repo

    Args:
        repo_name (str): name of remote repo to be deleted
    """
    auth = git.git_login()
    git.create_repository(auth,repo_name)
    
def make_local_repo(repo_name:str) -> None:
    """Makes a local repo with a project directory

    Args:
        repo_name (str): name of repo to be made
    """
    make_folder(repo_name)
    subprocess.run([f"git init {repo_name}"],shell=True)
    
def make_file(file_name:str) -> None:
    """Makes a file

    Args:
        file_name (str): name of file to be made
    """
    subprocess.run([f"touch {file_name}"],shell=True)
    
def delete_file(file_name:str) -> None:
    """Deletes a file

    Args:
        file_name (str): name of file to be deleted
    """
    subprocess.run(["bash","-c",f"rm {file_name}"])
    
def delete_folder(folder_name:str) -> None:
    """Deletes a directory

    Args:
        folder_name (str): name of directory to be deleted
    """
    subprocess.run(["bash","-c",f"rm -r {folder_name}"])
            
def make_folder(folder_name:str) -> None:
    """Makes a directory

    Args:
        folder_name (str): name of directory to be made
    """
    subprocess.run([f"mkdir {folder_name}"],shell=True)
    
def find_files_and_directories(directory:str) -> list:
    """Locates directories and files within a given directory

    Args:
        directory (str): directory to be searched

    Returns:
        list: contents of directory
    """
    bytes = subprocess.run(["bash","-c",f"ls {directory}"], capture_output=True).stdout.strip()
    table = [ [word] for word in bytes.decode("utf-8").split("\n") ]
    return table
    


if __name__ == "__main__":
    make_remote_and_local_repo("~/","deathMarch")