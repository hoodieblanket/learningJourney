# Debian Setup
---

## Table of Contents

---
- [# Debian Setup](#-debian-setup)
- [Table of Contents](#table-of-contents)
- [- Helpful packages to install specific programs](#--helpful-packages-to-install-specific-programs)
- [Common terminal commands](#common-terminal-commands)
  - [Command line Quick Reference](#command-line-quick-reference)
  - [GIT commandline](#git-commandline)
- [Setting up GIT](#setting-up-git)
- [System updating, upgrading and maintenance](#system-updating-upgrading-and-maintenance)
- [Display and Change hostname](#display-and-change-hostname)
- [Unzipping a file](#unzipping-a-file)
- [Installing .deb file](#installing-deb-file)
- [Uninstall software and remove artifact dependencies](#uninstall-software-and-remove-artifact-dependencies)
- [Installing pip for VSCode & Python](#installing-pip-for-vscode--python)
- [Installing tmux](#installing-tmux)
- [Configuring bluetooth](#configuring-bluetooth)
- [Configuring apt sources to include 'non-free'](#configuring-apt-sources-to-include-non-free)
- [Setting up firacode font](#setting-up-firacode-font)
- [Installing alacritty](#installing-alacritty)
- [Installing VIM](#installing-vim)
- [Modifying bashrc or bashrc_aliases for alias set up](#modifying-bashrc-or-bashrc_aliases-for-alias-set-up)
- [My preferred aliases/shortcuts](#my-preferred-aliasesshortcuts)
- [Optional Shortcuts if you find useful](#optional-shortcuts-if-you-find-useful)
- [Setting up latte-dock](#setting-up-latte-dock)
- [Setting up VS Code to support Python, Github, LaTeX and Markdown](#setting-up-vs-code-to-support-python-github-latex-and-markdown)
- [Helpful packages to install specific programs](#helpful-packages-to-install-specific-programs)
---

## Common terminal commands

---

### Command line Quick Reference

---
    `ls la`                         additional modifiers - the *-a* will also force to show hidden files or folders.  
    `cd`                            to open a location within bash
    `xdg-open`                      to open files or folders in dolphin
    `mkdir`                         mkdir directoryname #make new directory in current instance 
    `rm`                            to remove a file or folder. (may need to root if you require permissions using "su")
            `rm`                      ~/directory/to/file.exe 
            `rm -rf`                  "Recursive/Forced" recursively deletes anything inside and any directories going down. 
            `-f`                      forces to delete    without prompting you first.

    `rmdir`                         rmdir directoryname #remove directory 
    `mv`                            mv /home/user/oldname /home/user/newname 
    `*` wildcard                    Example: rm *.pdf removes all items with the extension .pdf from the current folder
    `rm -r`                         Example: directoryname1 directoryname2 directoryname3 | use the wildcard * to match multiple directories

    `cp filename location_`         to copy a file and place the copy in a target location 
    `pwd`                           print working directory
    `sudo ./install.sh`             install a bash script using "./" pathway to specify current location path 
    `file filename`                 will tell you the type of file and info related to the type of file 
    `du fileOrDirectory`            will tell you the estimated size of the file or directory recursively 
    `unzip file.zip -d newdir`      Unzip a zip file and using -d to indicate directory name 
    `tar -xvf yourtargetfile.tar`   To untar a file to current directory 
---

### GIT commandline

---
![alt text](../images/gitaddcommands.jpg "general adding and updating commands")

    `git add -A or --all`         Add all file changes to commit stage (This also does both -u and . options as per below) 
    `git add -u or --update`      Updates or changes, **without adding new files** Looks at files if they are different or **removed** (this stages any 'rm' changes aswell) 
    `git add .`                   stages new files and modifications **without deletions** Looks at working tree and adds all those paths to staged changes if they are either changes or are new and not ignored (does not stage any 'rm' changes) 
    `git commit -m ""`            commit and leave your message for all stages 
    `git push origin branch`      to push to the branch you are working on 
    `git rm filename`             remove file from system & repo (remember to `git commit -m ""` after to add to staged commits) 
    `git rm --cached filename`    remove file from **repo only** 
---

## Setting up GIT

---
    `sudo apt install git`  
    `git config --global user.name __username__`                          sets global settings for this machine
    `git config --global user.name`                                       to check that its set properly, repeat for email check as well
    `git config --global user.email __email address__`                    go to folder location and use git init to initialise that folder for repo
    `git config --global credential.helper cache`                         Set git to use the credential memory cache
    `git config --global credential.helper 'cache --timeout=7200'`        Set the cache to timeout after 2 hour (setting is in seconds)
    `git remote add origin <https://github.com/repoowner/reponame.git>`   setting up the origin git repo
    `git push -u origin master`

[Back to Top](#table-of-contents)

---

## System updating, upgrading and maintenance

---

    `sudo apt install `             install package  
    `sudo apt remove `              removing a package  
    `sudo apt purge`                removing a package and its configurations  
    `sudo apt clean`                clean package cache  
    `sudo apt search`               search package cache  
    `sudo apt autoclean`            remove partial packages  
    `sudo apt autoremove`           remove unused dependency packages  
    `sudo apt update`               update the package cache  
    `sudo apt upgrade`              upgrade packages  
    `sudo apt dist-upgrade`         upgrade distribution

---

## Display and Change hostname

---

Just incase you want to change your hostname to something else

    `hostnamectl`                                           Display hostname details  
    `sudo hostnamectl set-hostname typehostnamehere`        Display the hostname and will change the hostname

---

## Unzipping a file

---
    
    `unzip file.zip -d newdirectory`                        unzip a zip file and using -d to indicate directory name 

---

## Installing .deb file

---

    `sudo apt install ~/directory/directory/filename.deb`   installing a .deb file from specific directory
    `sudo dpkg -i filename.deb`                             alternative method for the above

---

## Uninstall software and remove artifact dependencies

---

    `sudo apt purge --auto-remove appname`                  Uninstall software

[Back to Top](#table-of-contents)

---

## Installing pip for VSCode & Python

---

Installing pip3 for Python so you can use the Jupyter notebook for running code practice or examples

    `pip3 -V`                                               check version of pip3
    `sudo apt install python3-pip`                          install the pip for python3
    `pip3 install ipykernel` 
    `pip3 install notebook --upgrade` 

[Back to Top](#table-of-contents)

---

## Installing tmux

---
Needed as an addon for konsole or command line

    `sudo apt install tmux`

[Back to Top](#table-of-contents)

---

## Configuring bluetooth

----
First you will need to add non-free ***sources*** for apt

    `sudo apt install pulseaudio pulseaudio-module-bluetooth pavucontrol bluez-firmware`
Reboot pc afterwards

[Back to Top](#table-of-contents)

---

## Configuring apt sources to include 'non-free'

---

  Use the following command to quickly open up the sources.list `xdg-open /etc/apt/sources.list`  
  
  add non-free to the end of each entry eg:

      deb http://deb.debian.org/debian buster main contrib non-free
      deb-src http://deb.debian.org/debian buster main contrib non-free

      deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free
      deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free

      deb http://deb.debian.org/debian buster-updates main contrib non-free
      deb-src http://deb.debian.org/debian buster-updates main contrib non-free

[Back to Top](#table-of-contents)

---

## Setting up firacode font

---
Nice font when used with konsole or commandline

    `sudo apt install fonts-firacode`

[Back to Top](#table-of-contents)

---

## Installing alacritty

---

Addon for spicing up the konsole or commandline. Makes it a lot more visually appealing.  

    # Alacritty for the use and change of default terminal from konsole (debian)
    `sudo apt install cargo`                                                Cargo is required for installation process of Alacritty  
    `cargo build --release`  
    `sudo apt install curl`                                                 Curl is required for easy install process 
    `sudo apt install kitty`                                                Same as Alacritty, required for the installation
    `curl --proto '=https' --tlsv1.2 -sSf <https://sh.rustup.rs> | sh`      need to remove rust so it doesn't mess with rustup (if rust is already installed)

    # To have a look at the installation instructions
    <https://github.com/alacritty/alacritty/blob/master/INSTALL.md#debianubuntu>

    `sudo apt-get install cmake pkg-config libfreetype6-dev` 
    `libfontconfig1-dev   libxcb-xfixes0-dev python3`
    `clone repository to ~/.config/alacritty` 

    # copy setting from dropbox into ~/.config/alacritty/alacritty.yml file 


    `git clone <https://github.com/alacritty/alacritty.git>`                (inside alacritty folder or new folder)
    `cargo install cargo-debian`
    `cargo deb --install -p alacritty`

    # choose default terminal app

        `update-alternatives --config x-terminal-emulator`    

[Back to Top](#table-of-contents)

---


## Installing VIM

---

    `sudo apt install vim`                Download VIM

[Back to Top](#table-of-contents)

---

## Modifying bashrc or bashrc_aliases for alias set up

---

    `xdg-open ~/.bashrc_aliases`         creates new bashrc_aliases file  
    `source ~/.bashrc`                   Force to launch the bashrc instead of logging in/out 
    `source ~/.bashrc_aliases`           Force to launch the bashrc instead of logging in/out
---

## My preferred aliases/shortcuts

---
    `alias sops='xdg-open /home/__username__/Dropbox/sops'`               quick access to my standard operating commands file
    `alias ls="ls -a --color=auto --group-directories-first"`
    `alias o="xdg-open 2>/dev/null"`                                      reassigning to open files/folders with native/default applications as well as feed errors into dev/null
    `alias ll="ls -alF"`
    `alias c='clear'`
    `alias notes="xdg-open /home/__username__/Dropbox/learningnotes.ctb"` quickly open my learningnotes file in cherrytree
---

## Optional Shortcuts if you find useful

---

    `alias pkg-in='sudo apt install'`                                                       Install package
    `alias pkg-rm='sudo apt remove'`                                                        Remove package
    `alias pkg-prm='sudo apt purge'`                                                        Remove package and delete its configuration files
    `alias pkg-cl='sudo apt-get clean'`                                                     Clean package cache
    `alias pkg-se='sudo apt search'`                                                        Search package cache
    `alias pkg-acl='sudo apt-get autoclean'`                                                Clean up partial packages
    `alinohupas pkg-arm='sudo apt-get autoremove'`                                          Remove unused dependency packages
    `alias sys-sync='sudo apt update'`                                                      Update package cache
    `alias sys-up='sudo apt upgrade'`                                                       Upgrade packages
    `ALIAS SYS-SYNC-UP='SUDO APT UPDATE && sudo apt upgrade'`                               Update package cache & upgrade package
    `alias sys-sync-dup='sudo apt update && sudo apt upgrade && sudo apt dist-upgrade'`     Update package cache & upgrade packages & upgrade distribution
    `alias sys-list-up='sudo apt list --upgradable'`                                        Show list of upgradeable packages

[Back to Top](#table-of-contents)

---

## Setting up latte-dock

---

    `sudo apt install latte-dock`

[Back to Top](#table-of-contents)

---

## Setting up VS Code to support Python, Github, LaTeX and Markdown

---

    `sudo apt install texlive-full`  
    # Install VS code latex extension  
    # markdown all in one extension  
    # python extension  
    # github extension
    # Bracket Pair Colorizer 2
    # Jupyter
    # Material Icon Theme
    # Settings Sync


[Back to Top](#table-of-contents)

---

## Helpful packages to install specific programs

---

    `sudo apt install dirmngr`    need this in order to install spotify

[Back to Top](#table-of-contents)

---
