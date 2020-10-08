import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")

def create():
    workingDirectory = str(sys.argv[1])
    folderName = str(sys.argv[2])
    os.makedirs(path + str(workingDirectory) + "/" + str(folderName))
    user = Github(username, token).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created GitHub repository- " + folderName + " -in the " + workingDirectory + " directory.")


if __name__ == "__main__":
    create()