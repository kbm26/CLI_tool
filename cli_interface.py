from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator
from InquirerPy.validator import PathValidator

import os

def main():
    """Alternate syntax example."""

    # name = inquirer.text(message="Enter your name:").execute()
    # print(f"Hello {name}")
    # company = inquirer.text(
    #     message="Which company would you like to apply:",
    #     completer={
    #         "Google": None,
    #         "Facebook": None,
    #         "Amazon": None,
    #         "Netflix": None,
    #         "Apple": None,
    #         "Microsoft": None,
    #     },
    #     multicolumn_complete=True,
    # ).execute()
    # print(f"welcome {company}")
    # salary = inquirer.text(
    #     message="What's your salary expectation(k):",
    #     transformer=lambda result: "%sk" % result,
    #     filter=lambda result: int(result) * 1000,
    #     validate=NumberValidator(),
    # ).execute()
    # print(f"wow {salary} is alot of money")
    
    home_path = "~/" if os.name == "posix" else "C:\\"
    src_path = inquirer.filepath(
        message="Enter file to upload:",
        default=home_path,
        validate=PathValidator(is_file=True, message="Input is not a file"),
        only_files=True,
    ).execute()
    dest_path = inquirer.filepath(
        message="Enter path to download:",
        validate=PathValidator(is_dir=True, message="Input is not a directory"),
        only_directories=True,
    ).execute()

if __name__ == "__main__":
    main()