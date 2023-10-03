import subprocess
import sys


def get_github_username():
    try:
        # Run the git command to get the user's GitHub username
        username = subprocess.check_output(['git', 'config', 'user.name']).decode().strip()
        return username
    except subprocess.CalledProcessError:
        return input("Enter your github username : ")  # Git configuration not found or an error occurred


def push_to_remote(remote_name='origin', branch_name='main'):
    try:
        # Run the 'git push' command to push changes to the remote repository
        subprocess.check_output(['git', 'push', remote_name, branch_name])
        print("You are all done! Your README.md file is up to date and pushed to the remote repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to remote: {e}")
        print("Commit the repository manually to the remote repository now. You will be all done!")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Commit the repository manually to the remote repository now. You will be all done!")
        sys.exit(1)


with open('.gitignore', 'a') as gitignore:
    gitignore.write('\n/CopyMyReadme.py')

github_username = get_github_username()

# Open the Markdown file for reading
with open('README.md', 'r+') as profile_readme:
    # Read the content of the file
    content = profile_readme.read()
    content.replace("chathura-de-silva", github_username)
    profile_readme.write(content)
push_to_remote()