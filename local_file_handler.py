import subprocess
import git_remote_handler as git
def make_remote_and_local_repo(repo_dir:str,repo_name:str) -> None:
    auth = git.git_login()
    
    make_remote_repo(repo_name)
    
    repo = git.find_repo(auth,repo_name)
    git_dir = f"--git-dir={repo_dir}{repo_name}/.git/"
    work_dir = f"--work-tree={repo_dir}{repo_name}"
    
    make_local_repo(f"{repo_dir}{repo_name}")
    make_file(f"{repo_dir}{repo_name}/text.txt")
    subprocess.run([f"git {git_dir} {work_dir} add ."],shell=True)
    # subprocess.run([f"git {git_dir} {work_dir} commit -m first commit"],shell=True)
    # subprocess.run([f"git {git_dir} {work_dir} branch -M main"],shell=True)
    # subprocess.run([f"git {git_dir} {work_dir} remote add origin {repo.clone_url}"],shell=True)
    # subprocess.run([f"git {git_dir} {work_dir} push -u origin main"],shell=True)
    
def make_remote_repo(repo_name:str) -> None:
    auth = git.git_login()
    git.create_repository(auth,repo_name)
    
def make_local_repo(repo_name:str) -> None:
    make_folder(repo_name)
    subprocess.run(["git","init",f"{repo_name}"])
    
def make_file(file_name:str) -> None:
    subprocess.run([f"touch {file_name}"],shell=True)
    
def delete_file(file_name:str) -> None:
    subprocess.run(["bash","-c",f"rm {file_name}"])
    
def delete_folder(folder_name:str) -> None:
    subprocess.run(["bash","-c",f"rm -r {folder_name}"])
            
def make_folder(folder_name:str) -> None:
    subprocess.run([f"mkdir {folder_name}"],shell=True)
    
def find_files_and_directories(directory) -> list:
    bytes = subprocess.run(["bash","-c",f"ls {directory}"], capture_output=True).stdout.strip()
    table = [ [word] for word in bytes.decode("utf-8").split("\n") ]
    return table
    


if __name__ == "__main__":
    make_file("~/sideProjects/ext")
