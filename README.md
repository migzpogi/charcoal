Contents
* [Way of Work](#way-of-work)
* [Ubuntu Commands](#ubuntu-commands)
* [Useful Links](#useful-links)

## Way of Work
I usually start my projects by creating a repository in GitHub. After thinking of a name and cloning it to my local directory, I commit a single Python file (or edit the pre-made README.md) and push it to verify that everything works fine. Then I create a virtual environment (since I mostly work with Python), update my aliases so I can activate it anytime, and finally boot up PyCharm.  

## CLI Set Up
### zsh
```
# Install zsh
sudo apt update
sudo apt install zsh
zsh --version

# Change default shell to zsh
chsh -s $(which zsh)
# Log out then log back in, a prompt will appear
# Pressing 2 will create a ~/.zshrc file with some configurations set
```

### ohmyzsh
See [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) for installation instructions.
```
ls ~/.oh-my-zsh/plugins     # plugins location
```

### Plugins
* [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/tree/master)
```
cd ~/.oh-my-zsh/plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
* [k](https://github.com/supercrabtree/k)
```
cd ~/.oh-my-zsh/plugins
git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
```

### ~/.zshrc
Some configurations for zsh
```
DISABLE_UNTRACKED_FILES_DIRTY="true"   # uncomment
plugins(git zsh-syntax-highlighting)
```

### Aliases
```
alias whichsh="ps -p $$"        # show active shell
alias whichos="lsb_release -a"  # show os name
alias editzsh="vi ~/.zshrc"     # edit zshrc
alias sourze="source ~/.zshrc"  # source zshrc
alias kk="k -a -h --no-vcs"     # wrapper for k
```

### `~/.myscripts/`
I store my scripts in this directory. Do not forget to run `chmod -R +x ~/.myscripts`

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

## Useful Links
* [GitHub MD Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Tabs in project readme section](https://github.com/orgs/community/discussions/86658)
