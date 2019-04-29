#Popular uses of the terminal

The terminal can be used to launch any program and to complete any task without the need to navigate to the directory\
 or having to use the mouse to complete tasks. The following is popular uses that was relevant to me as I was learning\
  the linux system from scratch (after being a Windows user for the last 20+ years).
  
Write the following inside the terminal word for word:

#### Examples of popular uses
##### Apt

**_sudo apt install_** # install package

**_sudo apt remove_** # removing a package

**_sudo apt purge_** # removing a package and its configurations

**_sudo apt clean_** #clean package cache

**_sudo apt search_** # search package cache

**_sudo apt autoclean_** # remove partial packages

**_sudo apt autoremove_** # remove unused dependency packages

**_sudo apt update_** # update the package cache

**_sudo apt upgrade_** # upgrade packages

**_sudo apt dist-upgrade_** # upgrade distribution

##### Commands and my set up

**_firefox & disown_** # this will launch my internet browser but also remove the ties to the terminal so that I can\
close the terminal down without it wanting to close the session of browser down.

**_nohup firefox_** # similar to disown. *nohup* is no hang up. So processes are not tied to the terminal that launched.

**_source ~/.bashrc_** #Force to launch the bashrc instead of logging in/out

**_ mkdir -p ~/.local/share/konsole , cp your.colorscheme ~/.local/share/konsole_** # installing colorscheme for konsole

**_mv readme.txt foldername_** # renaming a directory mv can move files around and also rename files or directories.

**_cp filename location_** # to copy a file and place the copy in a location

**_pwd_** # print working directory

**_sudo ./install.sh_** # install a bash script using "./" pathway to specify current location path

**_unzip file.zip -d newdirectory_** # unzip a zip file and using -d to indicate directory name

**_ls_** or **_ls -la_** # list all files and directories in current location. (-a: do not ignore "." starting entires -l: long listing format for more info)

**_cd_** or **cd ..** or **_cd ~_** # cd moves terminal to folder or location. (cd .. : move up a folder in the path. cd ~: move to home directory)

**_xdg-open_** # open a file or folder. when opening files it will attempt it with the default program of the file type.

**_rm_** or **_rm rf_** # remove a file or folder. (rm -rf: recursively remove a directory with force)

**_tar -xvf yourfile.tar_** # to untar a file to current directory

**_sudo apt install ~/directory/directory2/filename.deb_** or **_ sudo dpkg -i filename.deb_** # Installing a .deb file

**_hostnamectl_** or **_sudo hostnamectl set-hostname typehostnamehere_** # display the hostname and info  and will change the hostname

##### Useful aliases

To add aliases that are implemented on startup, modify the bashrc file. "~/.bashrc". Add the aliases as follows and then use\
the "source .bashrc" command to install and use without having to login/logout for aliases to take effect. (being lazy)
        
   - alias sops=/home/johann/Documents/sops # open up document that i use to log important commands
   - alias ls="ls -a --color=auto --group-directories-first" # modify ls to do -a
   - alias c=clear # clear terminal
   - alias x=exit # Exit terminal
   - alias o = xdg-open 2>/dev/null # invoke xdg-open and send any error/irrelevant info to 2>/dev/null so it doesnt show.
        


Helpful packages:
   __Spotify__
      - sudo apt install dirmngr # need this in order to install spotify

Optional aliases:
        
   - alias pkg-in='sudo apt install' # Install package        
   - alias pkg-rm='sudo apt remove' # Remove package       
   - alias pkg-prm='sudo apt purge' # Remove package and delete its configuration files      
   - alias pkg-cl='sudo apt-get clean' # Clean package cache      
   - alias pkg-se='sudo apt search' # Search package cache     
   - alias pkg-acl='sudo apt-get autoclean'  # Clean up partial packages       
   - alias pkg-arm='sudo apt-get autoremove' # Remove unused dependency packages        
   - alias sys-sync='sudo apt update' # Update package cache
   - alias sys-up='sudo apt upgrade' # Upgrade packages        
   - alias sys-sync-up='sudo apt update && sudo apt upgrade' # Update package cache & upgrade package        
   - alias sys-sync-dup='sudo apt update && sudo apt upgrade && sudo apt dist-upgrade' # Update package cache & upgrade packages & upgrade distribution
   - alias sys-list-up='sudo apt list --upgradable' # Show list of upgradeable packages



