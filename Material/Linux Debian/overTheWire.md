#Learning Notes through playing Overthewire: Bandit

**_SSH_** Secure Shell protocol for operating network services over an unsecured network. Typical applications would to remotely connect through command-line and remote command execution.

The protocol distinguishes between two (2) major versions, `SSH-1` and `SSH-2`. The standard TCP port for SSH is `22`.
Generally used to access Unix-like operating systems. The encryption used by SSH is intended to provide confidentially and integrity of data over an unsecured network. This protocol succeeded telnet that sent data such as passwords across the network in plain text and opened itself up to vulnerabilities such as `packet analysis`.

It is possible if the two sides, client and server, have never authenticated before (*SSH usually remembers the key that the server side previously used*) that there is a possibility of being vulnerable to **_man-in-the-middle attacks_**. The attacker could imitate the legitimate server side, ask for the password and obtained it.

SSH is important in *cloud computing* to solve connectivity issues, avoiding the security issues of exposing the cloud-based server directly to the internet. An SSH tunnel can provide a secure path over the internet, through a firewall to the virtual machine.

**_SSH Usage_** Secure Shell can log into a remote machine and execute commands but it also supports tunneling, forwarding TCP ports and X11 connections. Additionally it can also transfer files using SSH File Transfer `SFTP` or Secure Copy Protocols `SCP`.

`ssh something.labs.org -p 80 -l username` is an example of the use of *-p* to set the port and *-l* to set the username\
`ls`, or `ls -a` will show the current documents within the directory that your terminal is in. the *-a* will also force to show hidden files or folders. Remember using `cd` to move to a different directory if you want to search for what files and docs are elsewhere\
`ls -l` will provide you with just the number of folders/documents in that directory including hidden.\
`cd Directory` will move you to a folder in the current directory otherwise use `cd /path/to/directory` to travel.\
`file filename` will tell you the type of file and info related to the type of file.\
`du fileordirectory` will tell you the estimated size of the file or directory recursively.\
`find whatever` is used to find a particular file or directory. use the man pages for explanation `man find`\
`cat filename` cat is used to concatenate files and print on the standard output for example if a standard text file is used then it will print the file into the terminal\
`grep` is useful for searching documents for patterns. In combination of the options `-w # when searching for WHOLE words with no variations` or `-i # when searching regardless of case sensitivity`.

**_"Find" Can Be Difficult to use_**\
`find` is difficult if you don't know exactly what you are trying to find. For example using `find . -readable \! -executable -type f -size 1033c` the .(dot) will indicate to start searching from the current directory and any child directories. the *-readable \! -executable* just tells the terminal that the file is readable but not executable. Type specifies what type I am searching for (use *man find* pages to see all the options) and Size just specifies the size and the suffix specifies the category (i.e bytes)

**_Single and Double dots (. or ..) when found with `ls -a` in directory_**\
a *single dot* represents the current working directory, and *two dots* denote the parent (higher) directory. So using `cd .` will not perform anything as you are currently in that directory but `cd ..` will proceed to the parent directory even when you don't normally have access. For example `cd . (/home/hdy/documents)` and `cd .. (/home/hdy)`

**_Using - as a filename_** \
is convention for a lot of programs to mean `stdin/stdout` and is not a special property of the filename. the kernel doesn't recognise `- (dash)` as special so the system calls referring to `-` as a filename will use `-` literally as a filename. When using `cat` on the string `-`, it treats it as a synonym for `stdin` so you need to somehow force cat to read the file as the literal name of it being `-` and one way you can do this is to prefix the filename with a path to it such as `./-` or `/home/name/-` in order for cat to read it. Same way if the filename clashes with the command line such as naming a file `-e` which you would normally use on some command line such as `command -e do/something/here`. So this work around with `cat` will be useful if you prefix the path to the filename.





