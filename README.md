Contents
* [Way of Work](#way-of-work)
* [CLI](#command-line-interface)
* [Ubuntu Commands](#ubuntu-commands)
* [Useful Links](#useful-links)

## Way of Work
I usually start my projects by creating a repository in GitHub. After thinking of a name and cloning it to my local directory, I commit a single Python file (or edit the pre-made README.md) and push it to verify that everything works fine. Then I create a virtual environment (since I mostly work with Python), update my aliases so I can activate it anytime, and finally boot up PyCharm.  

## Command Line Interface
Z shell is my preferred command line interpreter. [More information](zsh/zsh.md)

### `~/.myscripts/`
I store my scripts in this directory. Do not forget to run `chmod -R +x ~/.myscripts`

## Git SSH
```
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
```

## Ubuntu Commands
### `apt-get update`
It doesn't actually install new versions of software. Instead, it updates the package lists for upgrades for packages that need upgrading, as well as new packages that have just come to the repositories.  

See: [What does sudo apt-get update do](https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do)

### `apt-get upgrade`
Installs the newest versions of all currently installed packages on a system.

### Creating a user with sudo
* SSH to server as root: `ssh root@1.2.3.4`  
* Add new user: `adduser devuser`
  * Specify the password as well
  * Can leave the other information as blank
* Add user to the sudo group: `usermod -aG sudo devuser`
* Test:
``` 
su - devuser
sudo ls /
```

### python3-venv
```
sudo apt install python3.12-venv
```

## Useful Links
* [GitHub MD Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Tabs in project readme section](https://github.com/orgs/community/discussions/86658)
* [Django](https://github.com/django)
