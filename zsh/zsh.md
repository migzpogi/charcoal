## zsh
Z shell (zsh) is an enhanced alternative for the Unix shell Bash.

### Why I like zsh
* Intelligent tab autocompletion
* Syntax highlighting
* Support for plugins and themes

### Installation and initial set up
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

### Oh My Zsh
A framework for managing zsh configurations. See [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh).

### Plugins
Plugins are located at: `~/.oh-my-zsh/plugins`  

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
