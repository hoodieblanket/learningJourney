# Running Debian 10 Buster non-frankendebian

## installing tmux

    sudo apt install tmux

## configuring bluetooth

    add non-free sources for apt update
    sudo apt install pulseaudio pulseaudio-module-bluetooth pavucontrol bluez-firmware
    reboot

## Configuring apt sources to include 'non-free'

    xdg-open /etc/apt/sources.list
    add non-free to the end of each entry eg:
        deb http://deb.debian.org/debian buster main contrib non-free
        deb-src http://deb.debian.org/debian buster main contrib non-free

        deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free
        deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free

        deb http://deb.debian.org/debian buster-updates main contrib non-free
        deb-src http://deb.debian.org/debian buster-updates main contrib non-free

## Setting up firacode font

    sudo apt install fonts-firacode

## Installing alacritty

### Installing cargo

    sudo apt install cargo
    cargo build --release

### Installing curl

    sudo apt install curl

### Installing kitty

    sudo apt install kitty

### Installing rustup

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
        #need to remove rust so it doesn't mess with rustup

### Link

    https://github.com/alacritty/alacritty/blob/master/INSTALL.md#debianubuntu

    sudo apt-get install cmake pkg-config libfreetype6-dev libfontconfig1-dev   libxcb-xfixes0-dev python3
    clone repository to ~/.config/alacritty
    copy setting from dropbox into ~/.config/alacritty/alacritty.yml file
    git clone https://github.com/alacritty/alacritty.git
    #inside alacritty folder
        cargo install cargo-debian
        cargo deb --install -p alacritty
        #choose default terminal app
            update-alternatives --config x-terminal-emulator    

## Setting up Linux

    sudo apt install vim #Download VIM
    xdg-open ~/.bashrc_aliases #creates new bashrc_aliases file

    source ~/.bashrc #Force to launch the bashrc instead of logging in/out
    source ~/.bashrc_aliases #Force to launch the bashrc instead of logging in/out

## Setting up latte-dock

    sudo apt install latte-dock

## Setting up Firefox

*_Download latest tar-ball_*

        wget -O FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"

*_Install_*

            sudo mkdir /opt/firefox
        tar xjf FirefoxSetup.tar.bz2 -C /opt/firefox/

*_Replace existing binary_*

        sudo mv /usr/lib/firefox-esr/firefox-esr /usr/lib/firefox-esr/firefox-esr_orig
        sudo ln -s /opt/firefox/firefox/firefox /usr/lib/firefox-esr/firefox-esr

*_Updating firefox_*

        wget -O FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
        sudo tar xjf FirefoxSetup.tar.bz2 -C /opt/firefox/

*_Restore Debian's default_*

    #If you need to revert
        sudo unlink /usr/lib/firefox-esr/firefox-esr
        sudo mv /usr/lib/firefox-esr/firefox-esr_orig /usr/lib/firefox-esr/firefox-esr

## Setting up CherryTree

    Download from website
    Download dependencies as well gtk2 etc
    install both to get it to work

## Setting up VS Code

    sudo apt install texlive-full
    Install VS code latex extension
    download python extension
    download github extension

## Setting up GIT

    sudo apt install git
    git config --global user.name __username__ 
        #sets global settings for this machine
    git config --global user.name 
        # to check that its set properly, repeat for email check as well
    git config --global user.email __email address__
        #go to folder location and use git init to initialise that folder for repo

    git config --global credential.helper cache
        #Set git to use the credential memory cache
    git config --global credential.helper 'cache --timeout=7200'
        # Set the cache to timeout after 2 hour (setting is in seconds)
    
    git remote add origin https://github.com/repoowner/reponame.git
        # setting up the origin git repo
    git push -u origin master

## Popular

*_Launching programs not tied to terminal_*

    firefox & disown #not tied to terminal or (firefox &) or nohup firefox&

*_Directory behaviour and removing folders/files_*

    #renaming a directory mv can move files around and also rename files or directories.
        mv /home/user/oldname /home/user/newname 

        mkdir directoryname #make new directory in current instance
        rmdir directoryname #remove directory

        rm to remove a file or folder. (may need to root if you require permissions using "su")
        rm ~/directory/to/file.exe
        rm -rf # -"Recursive/Forced" recursively deletes anything inside and any directories going down. -f forces to delete    without prompting you first.

*_Wildcard * to match and delete multiple files_*

    rm *.pdf
    rm -r dirname1 dirname2 dirname3 - use the wildcard * to match multiple directories

*_Unzipping a file_*

    #unzip a zip file and using -d to indicate directory name
        unzip file.zip -d newdirectory

*_Common terminal commands_*

    "ls" - list all files and directories in current location
    "cd" - to open a location within bash
    "xdg-open" to open files or folders in dolphin

*_Installing .deb file_*

    sudo apt install ~/directory/directory/filename.deb

*_Uninstall software and remove artifact dependencies_*

    sudo apt purge --auto-remove gimp

## standard aliases

        alias sops='xdg-open /home/__username__/Dropbox/sops'
        alias ls="ls -a --color=auto --group-directories-first"
        alias o="xdg-open 2>/dev/null"
        alias ll="ls -alF"
        alias c='clear'
        alias notes="xdg-open /home/_username_/Dropbox/learningnotes.ctb"

## alias apt4

        sudo apt update
        sudo apt dist-upgrade
        sudo apt autoremove
        sudo apt autoclean
        sudo apt-get update
        sudo apt-get upgrade

## Helpful packages

        sudo apt install dirmngr # need this in order to install spotify

## Optional aliases

    #Install package
        alias pkg-in='sudo apt install'
        
    #Remove package
        alias pkg-rm='sudo apt remove'

    #Remove package and delete its configuration files
        alias pkg-prm='sudo apt purge'
        
    #Clean package cache
        alias pkg-cl='sudo apt-get clean'

    #Search package cache
        alias pkg-se='sudo apt search'

    #Clean up partial packages
        alias pkg-acl='sudo apt-get autoclean'

    #Remove unused dependency packages
        alinohupas pkg-arm='sudo apt-get autoremove'
        
    #Update package cache
        alias sys-sync='sudo apt update'
        
    #Upgrade packages
        alias sys-up='sudo apt upgrade'

    #Update package cache & uPGRADE PACKAGE
        ALIAS SYS-SYNC-UP='SUDO APT UPDATE && sudo apt upgrade'

    #Update package cache & upgrade packages & upgrade distribution
        alias sys-sync-dup='sudo apt update && sudo apt upgrade && sudo apt dist-upgrade'

    #Show list of upgradeable packages
        alias sys-list-up='sudo apt list --upgradable'
