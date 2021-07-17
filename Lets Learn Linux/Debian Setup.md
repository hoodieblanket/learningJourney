# Debian Setup <!-- omit in toc -->


## Table of Contents

---
- [Table of Contents](#table-of-contents)
- [Common terminal commands](#common-terminal-commands)
  - [Commandline Quick Reference](#commandline-quick-reference)
- [GIT](#git)
  - [GIT commandline](#git-commandline)
- [System Maintenance](#system-maintenance)
- [Configuring apt sources to include 'non-free'](#configuring-apt-sources-to-include-non-free)
- [Aliasing - Modify .bashrc or zshrc](#aliasing---modify-bashrc-or-zshrc)
  - [Favourite Aliases](#favourite-aliases)
  - [Optional aliases](#optional-aliases)
- [Specific Program Setups](#specific-program-setups)
  - [Installing alacritty](#installing-alacritty)

## Common terminal commands

---
### Commandline Quick Reference

---
| `Command` : Target                  | Description                                                                                                                            |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| `ls la` directory                   | additional modifiers - the *-a* will also force to show hidden files or folders.                                                       |
| `cd` directory                      | to open a location within bash                                                                                                         |
| `xdg-open` file_or_folder           | to open files or folders in dolphin                                                                                                    |
| `mkdir` new_directory_name          | mkdir directoryname #make new directory in current instance                                                                            |
| `rm` file_or_folder                 | ~/directory/to/file.exe  to remove a file or folder. (may need to root if you require permissions using "su")                          |
| `rm -rf`                            | `-r` "Recursive/Forced" recursively deletes anything inside and any directories going down. `-f` forces to delete without prompt first |
| `rm -r`                             | Example: directoryname1 directoryname2 directoryname3                                                                                  |
| `rmdir` directory                   | rmdir directoryname #remove directory                                                                                                  |
| `mv` target_file new_file           | mv /home/user/oldname /home/user/newname                                                                                               |
| `*` wildcard                        | Example: rm *.pdf removes all items with the extension .pdf from the current folder                                                    |
| `cp` target_file target_location    | to copy a file and place the copy in a target location                                                                                 |
| `pwd`                               | print working directory                                                                                                                |
| `sudo ./install.sh`                 | install a bash script using "./" pathway to specify current location path                                                              |
| `file` target_file                  | will tell you the type of file and info related to the type of file                                                                    |
| `du` file_or_folder                 | will tell you the estimated size of the file or directory recursively                                                                  |
| `unzip` target_zip `-d` folder_name | Unzip a zip file and using -d to indicate directory name                                                                               |
| `tar -xvf` target_tar               | To untar a file to current directory                                                                                                   |

| **Display & Change hostname**                    | Description                                       |
| :----------------------------------------------- | :------------------------------------------------ |
| `hostnamectl`                                    | Display hostname details                          |
| `sudo hostnamectl set-hostname typehostnamehere` | Display the hostname and will change the hostname |

| **Install .deb file**                                 | Description                                    |
| :---------------------------------------------------- | :--------------------------------------------- |
| `sudo apt install ~/directory/directory/filename.deb` | installing a .deb file from specific directory |
| `sudo dpkg -i filename.deb`                           | alternative method for the above               |

| **Uninstall Software and remove artifact dependencies** | Description        |
| :------------------------------------------------------ | :----------------- |
| `sudo apt purge --auto-remove appname`                  | Uninstall software |

## GIT

---
| **Setup GIT initially**                                             | Description                                                               |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------ |
| `sudo apt install git`                                              | for installing Git                                                        |
| `git config --global user.name __username__`                        | sets global settings for this machine                                     |
| `git config --global user.name`                                     | to check that its set properly, repeat for email check as well            |
| `git config --global user.email __email address__`                  | go to folder location and use git init to initialise that folder for repo |
| `git config --global credential.helper cache`                       | Set git to use the credential memory cache                                |
| `git config --global credential.helper 'cache --timeout=7200'`      | Set the cache to timeout after 2 hour (setting is in seconds)             |
| `git remote add origin <https://github.com/repoowner/reponame.git>` | setting up the origin git repo                                            |
| `git push -u origin master`                                         | push to to master branch                                                  |

### GIT commandline

---
Common GIT commands to use within terminal window

| Command                        | Description                                                                                                                                                                                                   |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `git add -A or --all`          | Add all file changes to commit stage (This also does both -u and . options as per below)                                                                                                                      |
| `git add -u or --update`       | Updates or changes, **without adding new files** Looks at files if they are different or **removed** (also stages any 'rm' changes)                                                                           |
| `git add .`                    | stages new files and modifications **without deletions** Looks at working tree and adds all those paths to staged changes if they are either changes or are new and not ignored                               |
| `git commit -m ""`             | commit and leave your message for all stages                                                                                                                                                                  |
| `git push origin branch`       | to push to the branch you are working on                                                                                                                                                                      |
| `git rm filename`              | remove file from system & repo (remember to `git commit -m ""` after to add to staged commits)                                                                                                                |
| `git rm --cached filename`     | remove file from **repo only**                                                                                                                                                                                |
| `echo file.name >> .gitignore` | create .gitignore file in the current location and add file.name to the ignore list. Combined with `git rm --cached file.name` will remove the file from the repo (if already there) and then have it ignored |

![alt text](../images/gitaddcommands.jpg "general adding and updating commands")

[Back to Top](#table-of-contents)

## System Maintenance

---
| Command                 | Description                               |
| :---------------------- | :---------------------------------------- |
| `sudo apt install `     | install package                           |
| `sudo apt remove `      | removing a package                        |
| `sudo apt purge`        | removing a package and its configurations |
| `sudo apt clean`        | clean package cache                       |
| `sudo apt search`       | search package cache                      |
| `sudo apt autoclean`    | remove partial packages                   |
| `sudo apt autoremove`   | remove unused dependency packages         |
| `sudo apt update`       | update the package cache                  |
| `sudo apt upgrade`      | upgrade packages                          |
| `sudo apt dist-upgrade` | upgrade distribution                      |

## Configuring apt sources to include 'non-free'

---

  Use the following command to quickly open up the sources.list `xdg-open /etc/apt/sources.list`  
   | Command                          | Description                    |
   | :------------------------------- | :----------------------------- |
   | `xdg-open /etc/apt/sources.list` | Opens up the sources.list file |

  add non-free to the end of each entry eg:

      deb http://deb.debian.org/debian buster main contrib non-free
      deb-src http://deb.debian.org/debian buster main contrib non-free

      deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free
      deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free

      deb http://deb.debian.org/debian buster-updates main contrib non-free
      deb-src http://deb.debian.org/debian buster-updates main contrib non-free

[Back to Top](#table-of-contents)

## Aliasing - Modify .bashrc or zshrc 

---

**Note**: if you want your aliases separate then you can creat the `~/.bashrc_aliases` file and have them collated there. However this won't run on startup and you would need to `source ~/.bashrc_aliases` each time you want to use the aliases

If you want to have aliases start up with each shell, add the aliases directly to the bottom of the `~/.bashrc` file. Once done, run `source ~/.bashrc` to source the file or restart and it will auto source the file

**Note**: for kali linux, it has been switched from bash to zsh so to find and amend aliases you will need to amend `~/.zshrc` file instead of `.bashrc`

| Command                      | Description                                          |
| :--------------------------- | :--------------------------------------------------- |
| `kate ~/.bashrc_aliases`     | create bashrc_aliases file to add aliases            |
| `xdg-open ~/.bashrc`         | opens the existing bashrc file                       |
| `xdg-open ~/.bashrc_aliases` | creates new bashrc_aliases file                      |
| `source ~/.bashrc`           | Force to launch the bashrc instead of logging in/out |
| `source ~/.bashrc_aliases`   | Force to launch the bashrc instead of logging in/out |

### Favourite Aliases

---

| **Aliases**                                               | Description                                                                                                                                                          |
| :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alias la='ls -A'`                                        |
| `alias l='ls -CF'`                                        |
| `alias ls="ls -a --color=auto --group-directories-first"` |
| `alias o="xdg-open 2>/dev/null"`                          | # shortcut to open file and send errors to /dev/null                                                                                                                 |
| `alias ll="ls -alF -hals --color=auto"`                   | # shortcut running 'ls' but for indepth folder information                                                                                                           |
| `alias h="history"`                                       | # history in shell                                                                                                                                                   |
| `alias ports="ss -tulanp"`                                | # quick run ss with -tulanp                                                                                                                                          |
| `alias ..="cd .."`                                        | # shortcut to jump up to parent directory                                                                                                                            |
| `alias grep="grep -i --color=auto"`                       | # running grep and remove case sensitivity requirements as it is almost never useful                                                                                 |
| `cdd() { builtin cd "$@" && ls; }`                        | # quickly navigating through unknown folders: will 'cd' into folder and run 'ls' if successful; assigns to `cdd` as you do not want to override the builtin function |

### Optional aliases

---

| **Optional Aliases**                                                                | Description                                                    |
| :---------------------------------------------------------------------------------- | :------------------------------------------------------------- |
| `alias pkg-in='sudo apt install'`                                                   | Install package                                                |
| `alias pkg-rm='sudo apt remove'`                                                    | Remove package                                                 |
| `alias pkg-prm='sudo apt purge'`                                                    | Remove package and delete its configuration files              |
| `alias pkg-cl='sudo apt-get clean'`                                                 | Clean package cache                                            |
| `alias pkg-se='sudo apt search'`                                                    | Search package cache                                           |
| `alias pkg-acl='sudo apt-get autoclean'`                                            | Clean up partial packages                                      |
| `alinohupas pkg-arm='sudo apt-get autoremove'`                                      | Remove unused dependency packages                              |
| `alias sys-sync='sudo apt update'`                                                  | Update package cache                                           |
| `alias sys-up='sudo apt upgrade'`                                                   | Upgrade packages                                               |
| `ALIAS SYS-SYNC-UP='SUDO APT UPDATE && sudo apt upgrade'`                           | Update package cache & upgrade package                         |
| `alias sys-sync-dup='sudo apt update && sudo apt upgrade && sudo apt dist-upgrade'` | Update package cache & upgrade packages & upgrade distribution |
| `alias sys-list-up='sudo apt list --upgradable'`                                    | Show list of upgradeable packages                              |

[Back to Top](#table-of-contents)

## Specific Program Setups

---
| **SPOTIFY**                | Instruction                               |
| :------------------------- | :---------------------------------------- |
| `sudo apt install dirmngr` | need this in order to install **spotify** |

| **LATTE-DOCK**                | Instruction         |
| :---------------------------- | :------------------ |
| `sudo apt install latte-dock` | installs latte-dock |

| **VIM**                | Instruction  |
| :--------------------- | :----------- |
| `sudo apt install vim` | Installs VIM |

| **FIRACODE - Font**               | Instruction                                          |
| :-------------------------------- | :--------------------------------------------------- |
| `sudo apt install fonts-firacode` | Optional font that fits nicely with various programs |

| **BLUETOOTH Setup**                                                                  | Instructions                                                |
| :----------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `sudo apt install pulseaudio pulseaudio-module-bluetooth pavucontrol bluez-firmware` | Reboot pc afterwards; requires non-free sources for apt-get |

| **TMUX**                | Instruction |
| :---------------------- | :---------- |
| `sudo apt install tmux` |

| **PIP3 (Python & vscode)**        | Instruction                 |
| :-------------------------------- | :-------------------------- |
| `pip3 -V`                         | check version of pip3       |
| `sudo apt install python3-pip`    | install the pip for python3 |
| `pip3 install ipykernel`          |
| `pip3 install notebook --upgrade` | Used with Jupyter notebook  |

[Back to Top](#table-of-contents)

### Installing alacritty

---

Addon for spicing up the konsole or commandline. Makes it a lot more visually appealing.

| **(Alacritty) Installation and Setup**                             | Instruction                                                                       |
| :----------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| `sudo apt install cargo`                                           | Cargo is required for installation process of Alacritty                           |
| `cargo build --release`                                            |
| `sudo apt install curl`                                            | Curl is required for easy install process                                         |
| `sudo apt install kitty`                                           | Same as Alacritty, required for the installation                                  |
| `curl --proto '=https' --tlsv1.2 -sSf <https://sh.rustup.rs> | sh` | need to remove rust so it doesn't mess with rustup (if rust is already installed) |

| **Installation Instructions (Alacritty)**                | <https://github.com/alacritty/alacritty/blob/master/INSTALL.md#debianubuntu> |
| :------------------------------------------------------- | :--------------------------------------------------------------------------- |
| `sudo apt-get install cmake pkg-config libfreetype6-dev` |
| `libfontconfig1-dev   libxcb-xfixes0-dev python3`        |
| `clone repository to ~/.config/alacritty`                |

| **Clone settings from `~/.config/alacritty/alacritty.yml`** | Instruction                             |
| :---------------------------------------------------------- | :-------------------------------------- |
| `git clone <https://github.com/alacritty/alacritty.git>`    | (inside alacritty folder or new folder) |
| `cargo install cargo-debian`                                |
| `cargo deb --install -p alacritty`                          |


| **Select Default Terminal App**                    | Description |
| :------------------------------------------------- | :---------- |
| `update-alternatives --config x-terminal-emulator` |

[Back to Top](#table-of-contents)

