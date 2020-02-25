# Learning Over-The-Wire

## Table of Contents

- [Learning Over-The-Wire](#learning-over-the-wire)
  - [Table of Contents](#table-of-contents)
  - [Common Commandline Expressions](#common-commandline-expressions)
  - [SSH](#ssh)
  - [`Find` and its difficulties](#find-and-its-difficulties)
  - [`grep` and its difficulties](#grep-and-its-difficulties)
  - [Current Directory and Parent Directory navigation](#current-directory-and-parent-directory-navigation)
  - [Using '-' as a filename and its difficulties](#using---as-a-filename-and-its-difficulties)
  - [2>/dev/null and its difficulties](#2devnull-and-its-difficulties)
  - [Nmap Network Mapper](#nmap-network-mapper)

## Common Commandline Expressions

`ls`, or `ls -a` will show the current documents within the directory that your terminal is in. the *-a* will also force to show hidden files or folders. Remember using `cd` to move to a different directory if you want to search for what files and docs are elsewhere
`ls -l` will provide you with just the number of folders/documents in that directory including hidden.
`cd Directory` will move you to a folder in the current directory otherwise use `cd /path/to/directory` to travel.
`file filename` will tell you the type of file and info related to the type of file.
`du fileordirectory` will tell you the estimated size of the file or directory recursively.
`find whatever` is used to find a particular file or directory. use the man pages for explanation `man find`
`cat filename` cat is used to concatenate files and print on the standard output for example if a standard text file is used then it will print the file into the terminal. Use `-n` to print the line numbers next to the text\
`grep` is useful for searching documents for patterns. In combination of the options `-w # when searching for WHOLE words with no variations` or `-i # when searching regardless of case sensitivity`.\
`sort` is useful dealing with large data sets and you want to organise the data in a certain way. `-R` random shuffle but group identical keys. `-f` to fold lowercase to upper case. `-i` consider only printable characters
`base64` to encode data that you feed or a file that you want to encode. using `base 64 -d` will decode the data back to what you had previously.

## SSH

`ssh something.labs.org -p 80 -l username` is an example of the use of *-p* to set the port and *-l* to set the username\
`-p` Set the port
`-l` Set username

Secure Shell protocol for operating network services over an unsecured network. Typical applications would to remotely connect through command-line and remote command execution.

The protocol distinguishes between two (2) major versions, `SSH-1` and `SSH-2`. The standard TCP port for SSH is `22`.
Generally used to access Unix-like operating systems. The encryption used by SSH is intended to provide confidentially and integrity of data over an unsecured network. This protocol succeeded telnet that sent data such as passwords across the network in plain text and opened itself up to vulnerabilities such as `packet analysis`.

It is possible if the two sides, client and server, have never authenticated before (*SSH usually remembers the key that the server side previously used*) that there is a possibility of being vulnerable to **_man-in-the-middle attacks_**. The attacker could imitate the legitimate server side, ask for the password and obtained it.

SSH is important in *cloud computing* to solve connectivity issues, avoiding the security issues of exposing the cloud-based server directly to the internet. An SSH tunnel can provide a secure path over the internet, through a firewall to the virtual machine.

**_SSH Usage_** Secure Shell can log into a remote machine and execute commands but it also supports tunneling, forwarding TCP ports and X11 connections. Additionally it can also transfer files using SSH File Transfer `SFTP` or Secure Copy Protocols `SCP`.

## `Find` and its difficulties

Modifiers

- `-readable \! -executable` find readable but not executable file
- `-type f` what file type to find i.e `f` means FILE
- `-size 1033c` size of file and suffix `c` specifies category such as 'bytes'
- `find /` the `/` specifies to search the whole server
- `2>/dev/null` find will return entries we may not have access to which displays a lot of *permission denied*. This will remove error messages and narrow it down specifically for the file we need

`find` is difficult if you don't know exactly what you are trying to find. For example using `find . -readable \! -executable -type f -size 1033c` the .(dot) will indicate to start searching from the current directory and any child directories. the *-readable \! -executable* just tells the terminal that the file is readable but not executable. Type specifies what type I am searching for (use *man find* pages to see all the options) and Size just specifies the size and the suffix specifies the category (i.e bytes)\

Using find we can narrow down our search to certain properties for example `find -user userName -group groupName -size 33c` will search the current directory for the above details. However if we want to *search the whole server* then we need to use `/` to augment `find / -user userName -group groupName -size 33c` to search whole server for our property restrictions.

Additionally adding in `-type f # to specify that we are looking for a FILE` will return all the files but also will return entries that we may not have access to which will display 'permission denied'. Using `2>/dev/null` will remove all error messages and narrow it down specifically to the file we need.

## `grep` and its difficulties

Modifiers

- `-i` ignore upper or lower case
- `-w` whole word searching only and reject variance
- `-n` provide line number that the searched word exists
- `-r` recursive search in current and child directories, all the way down

Searching for patterns or repeats within a file. Additionally you can print also print the above/below and surrounding entries to provide context within the file. For example having many entries of the same name and lastname however by using grep to provide context, you find that it has separate contact details/email address listed above or below it etc so you can clue in that they are not double ups but in fact legitimate entries.

using options such as `-i` will ignore upper or lowercase. `-w` will use whole word searching only and reject any variance. `-n` will provide the line number that the searched word exists. `-r` will recursively search in not only the current directory but all its child directories.

## Current Directory and Parent Directory navigation

Commands

- `cd .` Single dot represents current directory, as such your navigation won't change
- `cd ..` Double dot represents parent directory, sometimes if SSH into a server, this will allow you to travel to parent folders even when you don't normally have access.

**_Single and Double dots (. or ..) when found with `ls -a` in directory_**\
a *single dot* represents the current working directory, and *two dots* denote the parent (higher) directory. So using `cd .` will not perform anything as you are currently in that directory but `cd ..` will proceed to the parent directory even when you don't normally have access. For example `cd . (/home/hdy/documents)` and `cd .. (/home/hdy)`

## Using '-' as a filename and its difficulties

Commands

- `cat` concatenate or otherwise in terminal, it will print the text from a document

"-" filename is a convention for a lot of programs to mean `stdin/stdout` and is not a special property of the filename. the kernel doesn't recognise `- (dash)` as special so the system calls referring to `-` as a filename will use `-` literally as a filename.

When using `cat` on the string `-`, it treats it as a synonym for `stdin` so you need to somehow force cat to read the file as the literal name of it being `-` and one way you can do this is to prefix the filename with a path to it such as `./-` or `/home/name/-` in order for cat to read it.

Same way if the filename clashes with the command line such as naming a file `-e` which you would normally use on some command line such as `command -e do/something/here`. So this work around with `cat` will be useful if you prefix the path to the filename.

## 2>/dev/null and its difficulties

This redirects errors into /dev/null, which is sort-of 'file' that ignores and deletes everything it receives. This is how you remove the errors such as permission errors from your output and left with the result that you want. `>` redirects the output of a command to wherever you want; by default it will redirect what's called `stdout` (*which is what standard console output is called*) but if you were to do that in this case yoeu'd end up not seeing ANY results as all of the output of your command would end up being directed to /dev/null and wiped out. So what you do is put a `2` infront so that its `2>` which is a parameter that specifics that just the *error messages* should be redirected.

## Nmap Network Mapper

Network discovery and security auditing.
Useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime

Displays exposed services on a target machine along with useful info such as version and OS detection.

In a nutshell:

- Host discovery
- Port discovery / enumeration
- Service discovery
- OS version detection
- Hardware (MAC) address detection
- Service version detection
- Vulnerability / exploit detection, using Nmap scripts (NSE)

Examples

`nmap -sC (for default scripts) -sV (enumerate versions) -oA (output all formats) nmap 10.10.10.117`
