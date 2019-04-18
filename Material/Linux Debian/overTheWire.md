#Learning Notes through playing Overthewire: Bandit

**_SSH_** Secure Shell protocol for operating network services over an unsecured network. Typical applications would to remotely connect through command-line and remote command execution.

The protocol distinguishes between two (2) major versions, `SSH-1` and `SSH-2`. The standard TCP port for SSH is `22`.
Generally used to access Unix-like operating systems. The encryption used by SSH is intended to provide confidentially and integrity of data over an unsecured network. This protocol succeeded telnet that sent data such as passwords across the network in plain text and opened itself up to vulnerabilities such as `packet analysis`.

It is possible if the two sides, client and server, have never authenticated before (*SSH usually remembers the key that the server side previously used*) that there is a possibility of being vulnerable to **_man-in-the-middle attacks_**. The attacker could imitate the legitimate server side, ask for the password and obtained it.

SSH is important in *cloud computing* to solve connectivity issues, avoiding the security issues of exposing the cloud-based server directly to the internet. An SSH tunnel can provide a secure path over the internet, through a firewall to the virtual machine.

**_SSH Usage_** Secure Shell can log into a remote machine and execute commands but it also supports tunneling, forwarding TCP ports and X11 connections. Additionally it can also transfer files using SSH File Transfer `SFTP` or Secure Copy Protocols `SCP`.


