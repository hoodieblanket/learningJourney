# Running Debian 10 Buster non-frankendebians

## Table of Contents

- [Running Debian 10 Buster non-frankendebians](#running-debian-10-buster-non-frankendebians)
  - [Table of Contents](#table-of-contents)
  - [Common terminal commands](#common-terminal-commands)
    - [Commandline](#commandline)
    - [System updating, upgrading and maintenance](#system-updating-upgrading-and-maintenance)
    - [Display and Change hostname](#display-and-change-hostname)
    - [Launching programs not tied to terminal](#launching-programs-not-tied-to-terminal)
    - [Unzipping a file](#unzipping-a-file)
    - [Installing .deb file](#installing-deb-file)
    - [Uninstall software and remove artifact dependencies](#uninstall-software-and-remove-artifact-dependencies)
  - [Installing pip for VSCode & Python](#installing-pip-for-vscode--python)
  - [Installing tmux](#installing-tmux)
  - [Configuring bluetooth](#configuring-bluetooth)
  - [Configuring apt sources to include 'non-free'](#configuring-apt-sources-to-include-non-free)
  - [Setting up firacode font](#setting-up-firacode-font)
  - [Installing alacritty](#installing-alacritty)
    - [Installing cargo](#installing-cargo)
    - [Installing curl](#installing-curl)
    - [Installing kitty](#installing-kitty)
    - [Installing rustup](#installing-rustup)
    - [Link to alacritty github and instructions](#link-to-alacritty-github-and-instructions)
  - [Installing VIM](#installing-vim)
  - [Modifying bashrc or bashrc_aliases for alias set up](#modifying-bashrc-or-bashrcaliases-for-alias-set-up)
  - [Setting up latte-dock](#setting-up-latte-dock)
  - [Setting up Firefox](#setting-up-firefox)
  - [Setting up CherryTree](#setting-up-cherrytree)
  - [Setting up VS Code to support Python, Github, LaTeX and Markdown](#setting-up-vs-code-to-support-python-github-latex-and-markdown)
  - [Setting up GIT](#setting-up-git)
  - [My preferred aliases/shortcuts](#my-preferred-aliasesshortcuts)
    - [Optional Aliases](#optional-aliases)
      - [Install package](#install-package)
      - [Remove package](#remove-package)
      - [Remove package and delete its configuration files](#remove-package-and-delete-its-configuration-files)
      - [Clean package cache](#clean-package-cache)
      - [Search package cache](#search-package-cache)
      - [Clean up partial packages](#clean-up-partial-packages)
      - [Remove unused dependency packages](#remove-unused-dependency-packages)
      - [Update package cache](#update-package-cache)
      - [Upgrade packages](#upgrade-packages)
      - [Update package cache & upgrade package](#update-package-cache--upgrade-package)
      - [Update package cache & upgrade packages & upgrade distribution](#update-package-cache--upgrade-packages--upgrade-distribution)
      - [Show list of upgradeable packages](#show-list-of-upgradeable-packages)
  - [Helpful packages to install specific programs](#helpful-packages-to-install-specific-programs)

## Common terminal commands

### Commandline

`ls` - list all files and directories in current location \
`ls la` - additional modifiers - the *-a* will also force to show hidden files or folders. \
`cd` - to open a location within bash \
`xdg-open` to open files or folders in dolphin \
`mkdir` - mkdir directoryname #make new directory in current instance \
`rm` - to remove a file or folder. (may need to root if you require permissions using "su")

    rm ~/directory/to/file.exe 
    rm -rf # -"Recursive/Forced" recursively deletes anything inside and any directories going down. 
    -f forces to delete    without prompting you first.

`rmdir` - rmdir directoryname #remove directory \
`mv` - mv /home/user/oldname /home/user/newname \
`* Wildcard` - rm *.pdf

    rm -r dirname1 dirname2 dirname3 - use the wildcard * to match multiple directories

`cp filename location_` # to copy a file and place the copy in a location
`pwd` # print working directory
`sudo ./install.sh` # install a bash script using "./" pathway to specify current location path
`file filename` will tell you the type of file and info related to the type of file
`du fileordirectory` will tell you the estimated size of the file or directory recursively
`unzip file.zip -d newdirectory` Unzip a zip file and using -d to indicate directory name
`tar -xvf yourfile.tar` To untar a file to current directory
`file` Will tell you the type of file and info related to the type of file

### System updating, upgrading and maintenance

sudo apt install # install package \
sudo apt remove # removing a package \
sudo apt purge # removing a package and its configurations \
sudo apt clean #clean package cache \
sudo apt search # search package cache \
sudo apt autoclean # remove partial packages \
sudo apt autoremove # remove unused dependency packages \
sudo apt update # update the package cache \
sudo apt upgrade # upgrade packages \
sudo apt dist-upgrade # upgrade distribution

### Display and Change hostname

`hostnamectl` - Display hostname details \
`sudo hostnamectl set-hostname typehostnamehere` # display the hostname and will change the hostname

### Launching programs not tied to terminal

firefox & disown #not tied to terminal or (firefox &) or nohup firefox&

### Unzipping a file

unzip a zip file and using -d to indicate directory name \
unzip file.zip -d newdirectory

### Installing .deb file

sudo apt install ~/directory/directory/filename.deb
sudo dpkg -i filename.deb

### Uninstall software and remove artifact dependencies

sudo apt purge --auto-remove gimp

[Back to Top](#table-of-contents)

## Installing pip for VSCode & Python

pip -V #check version\
sudo apt install python3-pip\
pip install ipykernel\
pip install notebook --upgrade\

[Back to Top](#table-of-contents)

## Installing tmux

sudo apt install tmux

[Back to Top](#table-of-contents)

## Configuring bluetooth

add non-free sources for apt update\
sudo apt install pulseaudio pulseaudio-module-bluetooth pavucontrol bluez-firmware
reboot

[Back to Top](#table-of-contents)

## Configuring apt sources to include 'non-free'

xdg-open /etc/apt/sources.list\
add non-free to the end of each entry eg:\

    deb http://deb.debian.org/debian buster main contrib non-free
    deb-src http://deb.debian.org/debian buster main contrib non-free

    deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free
    deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free

    deb http://deb.debian.org/debian buster-updates main contrib non-free
    deb-src http://deb.debian.org/debian buster-updates main contrib non-free

[Back to Top](#table-of-contents)

## Setting up firacode font

sudo apt install fonts-firacode

[Back to Top](#table-of-contents)

## Installing alacritty

Alacritty for the use and change of default terminal from konsole (debian)

[Back to Top](#table-of-contents)

### Installing cargo

sudo apt install cargo\
cargo build --release

### Installing curl

sudo apt install curl

### Installing kitty

sudo apt install kitty

### Installing rustup

curl --proto '=https' --tlsv1.2 -sSf <https://sh.rustup.rs> | sh

- need to remove rust so it doesn't mess with rustup

### Link to alacritty github and instructions

<https://github.com/alacritty/alacritty/blob/master/INSTALL.md#debianubuntu>

sudo apt-get install cmake pkg-config libfreetype6-dev \
libfontconfig1-dev   libxcb-xfixes0-dev python3\
clone repository to ~/.config/alacritty\
copy setting from dropbox into ~/.config/alacritty/alacritty.yml file\
git clone <https://github.com/alacritty/alacritty.git> (inside alacritty folder or new folder)

    cargo install cargo-debian
    cargo deb --install -p alacritty
    %choose default terminal app
        update-alternatives --config x-terminal-emulator    

## Installing VIM

sudo apt install vim #Download VIM

[Back to Top](#table-of-contents)

## Modifying bashrc or bashrc_aliases for alias set up

xdg-open ~/.bashrc_aliases #creates new bashrc_aliases file \
source ~/.bashrc #Force to launch the bashrc instead of logging in/out\
source ~/.bashrc_aliases #Force to launch the bashrc instead of logging in/out

[Back to Top](#table-of-contents)

## Setting up latte-dock

sudo apt install latte-dock

[Back to Top](#table-of-contents)

## Setting up Firefox

*_Download latest tar-ball_*

wget -O FirefoxSetup.tar.bz2 "<https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US">

*_Install_*

sudo mkdir /opt/firefox\
tar xjf FirefoxSetup.tar.bz2 -C /opt/firefox/

*_Replace existing binary_*

sudo mv /usr/lib/firefox-esr/firefox-esr /usr/lib/firefox-esr/firefox-esr_orig \
sudo ln -s /opt/firefox/firefox/firefox /usr/lib/firefox-esr/firefox-esr

*_Updating firefox_*

wget -O FirefoxSetup.tar.bz2 "<https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"> \
sudo tar xjf FirefoxSetup.tar.bz2 -C /opt/firefox/

*_Restore Debian's default_*

If you need to revert \
sudo unlink /usr/lib/firefox-esr/firefox-esr \
sudo mv /usr/lib/firefox-esr/firefox-esr_orig /usr/lib/firefox-esr/firefox-esr

[Back to Top](#table-of-contents)

## Setting up CherryTree

Download from website \
Download dependencies as well gtk2 etc \
install both to get it to work

[Back to Top](#table-of-contents)

## Setting up VS Code to support Python, Github, LaTeX and Markdown

sudo apt install texlive-full \
Install VS code latex extension \
download markdown extension \
download python extension \
download github extension

[Back to Top](#table-of-contents)

## Setting up GIT

sudo apt install git \
git config --global user.name __username__

- sets global settings for this machine

git config --global user.name

- to check that its set properly, repeat for email check as well

git config --global user.email __email address__

- go to folder location and use git init to initialise that folder for repo

git config --global credential.helper cache

- Set git to use the credential memory cache

git config --global credential.helper 'cache --timeout=7200'

- Set the cache to timeout after 2 hour (setting is in seconds)

git remote add origin <https://github.com/repoowner/reponame.git> \

- setting up the origin git repo

git push -u origin master

[Back to Top](#table-of-contents)

## My preferred aliases/shortcuts

alias sops='xdg-open /home/__username__/Dropbox/sops'

- quick access to my stadard operating procedures file

alias ls="ls -a --color=auto --group-directories-first"

alias o="xdg-open 2>/dev/null"

- reassigning to open files/folders with native/default applications as well as feed errors into dev/null

alias ll="ls -alF"

alias c='clear'

alias notes="xdg-open /home/__username__/Dropbox/learningnotes.ctb"

- quickly open my learningnotes file in cherrytree

### Optional Aliases

#### Install package

alias pkg-in='sudo apt install'

#### Remove package

alias pkg-rm='sudo apt remove'

#### Remove package and delete its configuration files

alias pkg-prm='sudo apt purge'

#### Clean package cache

alias pkg-cl='sudo apt-get clean'

#### Search package cache

alias pkg-se='sudo apt search'

#### Clean up partial packages

alias pkg-acl='sudo apt-get autoclean'

#### Remove unused dependency packages

alinohupas pkg-arm='sudo apt-get autoremove'

#### Update package cache

alias sys-sync='sudo apt update'

#### Upgrade packages

alias sys-up='sudo apt upgrade'

#### Update package cache & upgrade package

ALIAS SYS-SYNC-UP='SUDO APT UPDATE && sudo apt upgrade'

#### Update package cache & upgrade packages & upgrade distribution

alias sys-sync-dup='sudo apt update && sudo apt upgrade && sudo apt dist-upgrade'

#### Show list of upgradeable packages

alias sys-list-up='sudo apt list --upgradable'

[Back to Top](#table-of-contents)

## Helpful packages to install specific programs

sudo apt install dirmngr # need this in order to install spotify

[Back to Top](#table-of-contents)
