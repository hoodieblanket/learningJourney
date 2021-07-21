# Cybersecurity Concepts <!-- omit in toc -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [- Routing](#--routing)
- [Key Definitions](#key-definitions)
- [CIA Triad](#cia-triad)
- [AAA of Security](#aaa-of-security)
- [Security Threats](#security-threats)
  - [Malware pending](#malware-pending)
  - [Unauthorized Access pending](#unauthorized-access-pending)
  - [System Failure pending](#system-failure-pending)
  - [Social Engineering pending](#social-engineering-pending)
- [Mitigating Threats](#mitigating-threats)
- [Hackers](#hackers)
- [Threat Actors](#threat-actors)
- [Threat Intelligence and Sources](#threat-intelligence-and-sources)
  - [Measuring quality of intelligence](#measuring-quality-of-intelligence)
  - [Types of intelligence](#types-of-intelligence)
- [Threat Hunting](#threat-hunting)
  - [Tools used for threat hunting](#tools-used-for-threat-hunting)
  - [Benefits of threat hunting](#benefits-of-threat-hunting)
- [Attack Frameworks](#attack-frameworks)
  - [Lockheed Martin Kill Chain](#lockheed-martin-kill-chain)
  - [MITRE ATT&CK Framework](#mitre-attck-framework)
    - [Implementing the ATT&CK Framework](#implementing-the-attck-framework)
  - [Diamond Model of Intrusion Analysis](#diamond-model-of-intrusion-analysis)
- [OSINT - What is Open Source Intelligence](#osint---what-is-open-source-intelligence)
- [NIST Cybersecurity Framework](#nist-cybersecurity-framework)
- [Cryptography & VPNs](#cryptography--vpns)
  - [Virtual Proxy Networks VPNs](#virtual-proxy-networks-vpns)
- [Wireshark](#wireshark)
  - [HTTP vs HTTPS](#http-vs-https)
- [ISO/OSI Protocol Layering](#isoosi-protocol-layering)
  - [Application Layer](#application-layer)
  - [Transport Layer](#transport-layer)
  - [Network Layer](#network-layer)
    - [**IP Protocol**](#ip-protocol)
    - [**Identify a HOST network**](#identify-a-host-network)
    - [**bitwise AND, OR operation to find network**](#bitwise-and-or-operation-to-find-network)
  - [Link Layer](#link-layer)
    - [**Forwarding**](#forwarding)
    - [**MAC Address - Discovery**](#mac-address---discovery)
    - [**ARP - Address Resolution Protocol**](#arp---address-resolution-protocol)
    - [**ARP - Discovery**](#arp---discovery)
  - [The Physical Layer](#the-physical-layer)
- [Routing](#routing)
---
## Key Definitions

|                               |                                                                                   |
| :---------------------------- | :-------------------------------------------------------------------------------- |
| `Information Security`        | The protection of data, or the information **on** the systems but not the system\ |
| `Information System Security` | The protection of the systems                                                     |

[Back to Top](#table-of-contents)

## CIA Triad

---
* **Confidentiality**
  * Encryption is another way of thinking confidentiality.
* **Integrity**
  * Ensuring the information has not been modified or altered without proper authorisation\
  * Integrity is linked in with HASHES and cryptography
* **Availability**
  * Information is accessed, stored and protected at all times. The content is *available*.
  * Theres three systems need to be in sync in order to allow consumers and vendors to  meet a middle ground that encompasses the desired level of protection while also meeting the convenience or needs from the users.
  * Without availability, then the system becomes useless as a consumer cannot access the required data. Similar with confidentiality; without that encryption or protection, what user will trust you with the information.

![alt text](https://i.imgur.com/T8ydhaK.png)

[Back to Top](#table-of-contents)

## AAA of Security

---
* **Authentication**
  * Authenticaton of a persons identity with proof and then confirmed by a system. Similar to when logging in to a website and signing it. The system may check several aspects such as confirming:
* **Authorisaton**
  * Areas requiring authentication if you are allowed to access. This would be checking for your token or access that would authorise you to reach a particular area
* **Accounting**
  * Usually a collection of all data to keep track of all the various things are being done. If you have some kind of insider threat or breach then these logs will have a catalogue of changes that occurred and would allow you to pinpoint towards an issue

Non-repudiation occurs when you have **proof** that someone has taken an action and cannot be disputed such as if you have a unique electronic signature when sending an email. We can establish that the unique key to your signature is unique to only yourself and then we have proof that it can be no one else.

**5 Methods of Authentication**

- **Something you know**
  - password or username
- **Something you are**
  - fingerprint or eye scan
- **Something you have**
  - credit card or drivers license
- **Something you do**
  - way that you speak or sign your name, signature
- **Somewhere you are**
  - GPS locations

[Back to Top](#table-of-contents)

## Security Threats

---
### Malware pending

### Unauthorized Access pending

### System Failure pending

### Social Engineering pending


**Phishing** 

Activity such as an email or delivery that normally simulates a sense of urgency, or plays to your immediate emotional responses when faced with something that is clearly a scam but because of the emotional factor; influences the user to not be a logical person.

- "Your credit has been charged. Click here for a refund if its incorrect"
- "You are being audited for fraud, contact us immediately to resolve"

Some users might jump to click the link without much thought into what the email is actually asking and **why** it might be asking it. This link might lead to another website that may look familiar in order to drop your guard and where they will attempt to collect private information from the user or run a scam to get cash from the user

**Spear Phishing**

Similar to phishing but this would be more targeted; hence the 'spear'. 

- Email simulating a boss or senior managers content, including having a fake email that looks incredibly real to a quick scan
- Using this to try to get private information from junior employees

This could be done by tailoring the email to have the right names, signatures, contact details and somethings even spoofing the email address so that it appears *almost* correct to the people who don't take the time to see who its from. The email could also appear extremely indepth or realistic in order to control your focus so you miss looking for the telltale signs

[Back to Top](#table-of-contents)

## Mitigating Threats

---
- **Physical Controls**
  - Alarm systems, locks, identification cards, security guard 

- **Technical Controls**
  - smart cards, access control lists, network authentication

- **Administrative (Managerial) Controls**
  - Policies, procedures and contingency plans
  - Procedural controls
    - What the organisation chooses to do on its own
  - Regulatory Controls
    - What the law dictates that you must follow how to protect data or private information

[Back to Top](#table-of-contents)

## Hackers

---
- **White Hat**
  - Non-malicious that is either contracted to a company or employed and attempt to break in at the behest of the company

- **Black Hats**
  - Malicious that are not following the rules

- **Grey Hats**
  - No affiliation to a company but they will still hack into companies without permission
  - non-malicious as they are just attempting to do this for the challenge but still breaking the law

- **Blue Hats**
  - Affiliated with the company through getting permissions such as bounty programs or getting permission to test their systems however they are not employed or on the payroll


[Back to Top](#table-of-contents)

## Threat Actors

---

- Script kiddies
  - unaware of what they are doing but potentially malicious intentionally or unintentionally
- Hacktivists
  - Driven by a cause
- Organised Crime
- Advanced Persistent Threats (APTs)
  - Highly trained and funded groups of hackers such as nation states who have access to open-source intelligence at their disposal


[Back to Top](#table-of-contents)

## Threat Intelligence and Sources

---
### Measuring quality of intelligence

- **Timeliness**

  - If the offender is aware that they have been identified then they will being to change their tactics
  - Property of Intelligence Source: the report you write might not be up-to-date in 2 days or 2 weeks.

- **Relevancy**

  - Property of Intelligence source: What affects the organisation? If the reported issues is related to macOS and your business runs windows then you need to consider the relevancy of the reporting to ensure the business can defend against whats relevant

- **Accuracy**

  - Property of Intelligence Source: Is the information is accurate. Remove false positives such as with software and getting the right information to make good decisions 

- **Confidence Levels**

  - Property of Intelligence Source: ensures it produces qualified statement about reliability.


[Back to Top](#table-of-contents)

### Types of intelligence

- **Proprietary**

  - Subscription based information handled by a private organisation and allowing you to 'buy in' on their collection of data to make it available for your use.

- **Closed Source**

  - Personal research or the providers own research and analysis efforts. The information is behind closed doors and only available for the vendor and their uses. The information gathered might be from their own mining of data through their customers and their products - then using this data anonymously.

- **Open Source**

  - Data without subscription, in the open market and may include threat feeds, reputation lists and malware signature databases

    - US-Cert
    - UK NCSC
    - AT&T Security
    - MISP (malware information sharing platform)
    - VirusTotal (uploading files to be scanned)
    - Spamhaus (for email related information)
    - SANS ISC Suspicious domains

- **Open Source Intelligence (OSINT)**

  - Methods of getting information from public records, websites and social media. Gathering data from widely public information to source that information on an individual. 

  - Any information you can gather about a person through facebook, linkd in and so forth: this is all considered OSINT

[Back to Top](#table-of-contents)

## Threat Hunting

---

Threat hunting is proactive search for threats or vulnerabilities within your own system that has not been discovered by normal security monitoring.

Pentesting you are often trying to break into your system to demonstrate a weakness however threat hunting you are analysing data within the systems we already have

- **less disruptive than a penetration test due to this**



**Establishing a hypothesis**

Derived from the threat modelling we have done. Think about who might harm us and how they might do this; this will help establish a hypothesis of what we might need to focus on based on what is highly likely or what is a priority to protect against

**Profiling Threat Actors and Activities**

Who might harm us, what might their objectives be and what systems would their goal be. Creating a scenario that show how a prospective attacker might attempt an intrusion.

### Tools used for threat hunting
- **Analyse network traffic**: see if there is suspicious outgoing traffic to a domain and hosts we may want to investigate
- **Analyse the executable process list**: investigate those hosts and what programs and services are being run and what opened that network connection
- **Analyse other infected hosts**: Check if other hosts are running into the same issues. Are they all running the same malicious process.
- **Identify how the malicious process was executed**: what allowed it to start up, can we whitelist or blacklist connections to avoid this process in the future

*We have to assume that the existing systems has failed when you are threat hunting - we are looking for those things that **aren't** detected and these tools have failed to capture that threat all ready.*

### Benefits of threat hunting
- **Improve detection capabilities**: use the information gathered to add to your detection database to capture that same issue in the future
- **integrate intelligence**: combine the research and data with existing intelligence and logs
- **reduce attack surface**: While threat hunting you have identified the entire area that the threat has progressed through and allows you to plan for the future and reduce the total attack surfuce for the future
- **block attack vectors**: block those different ports or interfaces that allowed the threat to breach
- **identify critical assets**: identifying what the breach was targeting so you can assess if how often this asset is being attacked and plan accordingly with further protections for critical assets

[Back to Top](#table-of-contents)

## Attack Frameworks

---
### Lockheed Martin Kill Chain

7 step method going from the top to the bottom that works very linear as you work your way down
- reconnaissance
- Weaponization
- Delivery
- Exploitation
- Installation
- Command & Control (C2)
- Actions on Objectives

**1. Reconnaissance** - Goal: Find a weakness

Information gathering that is either passive gathering or active scanning
- Attack (**Passive**)
  - whois
  - ARIN registrations
  - google
  - shodan
  - job listings etc

- Defend (**Passive**)
  - limit public information (job listings, linkedin)
  - social media acceptable use policies
  - modify server error messages

- Attack (**Active**)
  - NMAP
  - port scanning
  - banner grabbing
  - vulnerability scanning
    - usually pretty loud and obvious so this might be done slowly and over time to lower the probability of being caught

- Defend (**Active**)
  - disable unused ports & services
    - limits number of entry points to your system
  - honeypots 
    - diverts from real systems but also may reveal who the adversary is
  - firewalls
  - IPS
  - TOR & 3rd party VPN inbound blocking

**2. Weaponization** - Goal: select weapon appropriate based on reconnaissance
- Attacks will adapt based on reconnaissance
  - metasploit
  - exploit-db
  - burpsuit
  - social engineering toolkit
- Defense
  - patch management remains the best defense management for the weaponization stage
  - disable: office macros, javascript and browser plugins
  - security basics, antivirus, IPS, email security, Multifactor authentication, audit logging etc..

**3. Delivery** - Goal: select avenue of delivery the payload or intrusion
- Target chosen or decided how to deliver
  - Websites: what website is frequently used by the users and if there is a vulnerability there
  - Social Media
  - User Input: user has some interaction with a website or database
  - Email: phishing getting users to click on order forms or purchase items and receipts such as from vendors or partners that was uncovered from reconnaissance
  - USB: leave infected USBs around employee cars or around employees hoping they the temptation for employees might be too much

- Defense:
  - Websites: Web filter, DNS filter - SSL accounts for the majority of web and email traffic today
  - Social media:  phishing campaigns to educate users further and the importance of awareness
  - User Input: IPS/IDS
  - Email: DKIM uses digital signatures to verify authenticity and SPF checks for coming from authorised IP of a domain - Both to guard against spoofing of emails.
  - USB: disabling USB or no "admin" rights

**4. Exploitation** - Goal: Gain access but its not a finishing line for the attack

- Attack succeed and the weapon has been delivered
  - SQL injection
  - buffer overflow
  - javascript hijack
  - malware

- Defense
  - DEP data execution prevention
  - anti-exploit
  - Reality is that if the attacker has gotten to this point, you are relying on preventative tools for post-execution such as a sandbox
    - Potentially capturing patient zero when an unknown file is downloaded, the protections jump in to stop the file from reaching the rest of the network

**5. Installation** - Goal: Get persistant access

- Offensive tools
  - DLL hijacking
  - meterpreter
  - remote access tools (RAT)
  - registry changes - making changes or commands startup or persistant
  - powershell commands

- Defense
  - Linux:chroot jail to isolate processes from rest of the system so the file has limited access to other data
  - windows: disable powershell

- Detection tools (post infection)
  - UBA/EDR will flag any unauthorised program thats been installed as well as flag any changes in process or system processes or registry and this should set off an alert or log

- Respond
  - Follow the incident response SOPs such as I.D if the device is critical, remove the device from the network or wiping and restarting from a good state

- Recover
  - You can then begin to restore or reimage the system to a known good state

**6. Command & Control**

At this stage, the access to the system is persistent and the attacker has immediate access to the target or system. This access is remote and at this stage; patching the vulnerability and such does not get rid of this persistent access.\
The defensive options here will be regarding limiting what they can control and detecting unusual activity.

**7. Action on Objective**

With the attacker in full control, the attacker is motivated by various goals and external influences so it is important to know what the attacker might be targeting
- financial motivation
- political
- espionage
- malicious insider
- lateral movement to another system or another target

Defense:
- data leakage prevention (DLP)
- user behaviour analysis (UPA)
- Network segmentation (combating lateral movement)

[Back to Top](#table-of-contents)

### MITRE ATT&CK Framework

---
This is a knowledge base maintained by an external company. Open source information that contains the information on various attacks\
This database is great to look at potential common intrusions or events that link to certain types of attacks. By ticking certain events that has happened, you can narrow down likelyhoods or common intrusions that lead to a specific attack that you can start looking signs for and prepare for.

Breaks down the tactics, techniques and procedures to a level wehre you can prioritise your defenses.\
The below table is an outline and brief description of each categories and this attack framework is related to when the **prevention** has failed and now we have to respond to an attacker that has gained access to the system.

| Categories in the framework matrix | Description                                                                                                                                                                                                      |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.Initial Access`                 | Attackers first footprint in network after exploiting some vulnerability                                                                                                                                         |
| `2.Execution` & `3.Persistence`    | Running malicious code and trying to maintain some foothold even when the system reboots they want to maintain access                                                                                            |
| `4.Privilege Escalation`           | Trying to get root or admin access                                                                                                                                                                               |
| `5.Defense Evasion`                | Tricks attacker would to do avoid getting caught such as encrypting payload or disabling logging so they don't trigger any IDS or anti-virus programs                                                            |
| `6.Credential Access`              | stealing accounts and passwords, while not an end goal of the attack; this is common to go for this regardless while inside the network                                                                          |
| `7.Discovery`                      | attacker trying to understand the environment or network such as through portscanning or portsniffing and what else they have access to                                                                          |
| `8.Lateral movement`               | jump to another system from the compromised host. Usually pivoting the attack by jumping to the weakest link and jump through multiple machines to get to the objective                                          |
| `9.Collection`                     | gathering any kind of data such as screencaps or keystrokes or any data related to the objective                                                                                                                 |
| `10.Command and Control`           | setting up system for remote control and disguised as normal http traffic                                                                                                                                        |
| `11.Exfiltration`                  | attacker is stealing data in ways they dont get caught like encrypting data or encrypting the file                                                                                                               |
| `12.Impact`                        | result to the system based on what the attacker is trying to achieve - e.g ransomwares' goal is to get financial gain and the impact to the system would be that the files and systems are encrypted and stopped |

The main point and advantage with the attack framework is that you are able to outline and research certain behaviours of attacks and this will mean we starting focusing on how to defend against these **behaviours** rathen than again these **tools**
- Tools are always going to update and change but behaviours are harder to change for an attacker.

**The following diagram outlines what an attacker might find difficult as the defensive tactics changes**
- **Hashes and IP Address** will be very easy to get around
- **Domain names** slightly more annoying but still not an issue. Might have to change some lines of code on their programs
- **Network/host artifacts** attacker becomes more annoyed with having to combat this. Such as blocking FTP outbound on your network. Might prevent the attacker from grabbing data but that can be circumvented by tunneling through another encrypted tunnel
- **Tools** and the losses means that attackers might need to come up with unfamiliar or new tools. An example would be disabling powershell on workstation and the attacker not having access to utilising powershell
- **TTP** this is the toughests this means they need to change their **behaviours**. This is the mitre attack framework

![alt text](https://i.imgur.com/7bXFNpl.png)

#### Implementing the ATT&CK Framework

1. Red team testing
   - The whole point of the red vs blue team testing is to use the framework and find the gaps so that you can fill those gaps.

2. Automated att&ck simulator
   - caldera is a tool developed by mitre that can simulate these different attacks or checks for various vulnerabilities

3. Implement into your SIEM
   - Logging from all appropriate data sources; end points, EDRs, firewalls and anything that could be target from an attack

4. Training
   - Need to have real understanding of the different attack techniques and what they actually mean to your network
   - You always need a human element to make a decision on the legitimacy of a potential threat but also noticing a false positive.

[Back to Top](#table-of-contents)

### Diamond Model of Intrusion Analysis

---
Represents an intrusion event that all relates to one of the following in the four diamond edges: Adversary, Capabilities, Victim, Infrastructure.

The diamond is all about finding that next step, the next unknown and following the clues. Builds a model or picture in our mind about how this adversary is operating.


![alt text](https://i.imgur.com/BA4DmKa.png)



- Adversary: The bad guy
- Capabilities: Malware, exploits, hacker tools, stolen certs
- Infrastructure: IP addresses, domain names, email address
- Victim: the targetted personas, targetted network assets, targetted email addresses

Meta-features within the diamond that characterises a meta-event

- Timestamp
- Phase: kill-chain phase?
- Result: whether successful or failure etc and track the intrusion
- Direction: the way the activities is going and the pivots its making such as Infrastructure to Adversary, Capability to Adversary etc
- Methodology: is this a phishing attack or waterhole attack - finding the class of activity
- Resources: infer resources needed for this capability or host the infrastructure over time for the adversary to do what they wanted. Having an idea if this was planned for months or what kind of resources was needed for this

Extended meta-features of the diamond model

- Social-political: there is *always* a relationship between the adversary and the victim

This allows you to understand what features or common links between different victims. Is it common for a certain type of victim? this would allow you to work out what kind of victim you are dealing with and the likely adversary you are dealing with

- Technology: connecting infrastructure to capability. 
 
What technology is connecting and enabling the capability. Knowledge of that technology and how it is being used may lead to revealing the malicious activity that targets those specific targets.\
Sometimes a target victim is not involved as the malicious software is looking to target specific infrastructure or technology instead



![alt text](https://i.imgur.com/HH5nAdO.png)

 Practical use of the diamond that compliments the kill chain

**Vertical linking** - We are linking 1 event  and as we move down the 1 event, we can link similar incidents to each other (C2 in event 1 is similar to the C2 used in event 2)

**Horizontal linking** - linking like events by common infrastructure, capability, victim or target or TTP (tactics, techniques and procedures)

[Back to Top](#table-of-contents)

## OSINT - What is Open Source Intelligence

---
OSINT is the practice of using publicly available information from a variety of different sources. If you pay attention and think about the kill chain; within the killchain the **reconnaissance** step is arguably the most important step as this is the level where the target starts painting the picture of where the vulnerabilities may lie and starts guiding the attack that is later used.

- Information on network equipment
- Employee email addresses
- Social media pages

The OSINT process starts from what you know on the target

1. What you know about the target
   - such as company or name
2. Define Goals and what we want i.e user credentials
   - We know we need an email address and possibly social media accounts if we are preparing for a spear phishing campaign 
3. Collect data using various tools
   - Maltego
     - Extremely powerful visualisation of information gathered about a target and the 'links' to get to that information
   - theHarvester
     - not so much visualisation however able to gather a lot of information really quickly
     - within shell: `theHarvester -d some_company_website -b linkedin`
     - Result: list of names, job titles of each user that is associated (work) with some_company_website on linkedin
     - can then pivot and use `netcraft` to get a full list of names and ip address that are publicly listed without ever needing to touch the target
     - Can also integrate google dork and shodan within these searches
   - Spiderfoot
     - Consolidates 100's of data feeds into a single search. Queries similar to google on all public OSINT sources available to get data on the target.
     - As easy as typing in something we know about the target such as `username` and finding out a whole bunch of information on that. 
     - Allows you to select what kind of queries you want to do; passive, investigate, footprint or all. 
       - Passive won't send any direct queries on the target
   - OSINT Framework [osintframework](https://osintframework.com/)
     - Powerful list of links that will be useful for your investigation
     - This visualisation also allows you to navigate easily to target specific information
4. Analyse the data
   - use the data or pivot to another perspective or target of data/person

[Back to Top](#table-of-contents)

## NIST Cybersecurity Framework

---
A voluntary risk-based framework that allows businesses to adopt and comply with a blueprint of risk-prevention strategies. The framework was conceptualised in the early 2000's as the US saw an uptick in cyber threats and they proposed a need for standard of security to be implemented. \
Within this framework, significant contributions came from diverse groups including small and medium sized businesses as well as from the international business community

NIST, National Institute of Standards and Technology, met with industry partners to create this risk-based framework

| CSF Components          | Description                                                                                                     |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Core                    | Activites, outcomes and industry standards, guidelines, and practices that communicate cybersecurity activities |
| Tiers                   | Levels of implementation that assist in conducting assessment and planning of cybersecurity activities          |
| Profiles                | The alignment of standards, guidelines, and practices to the framework core                                     |
| Implementation guidance | Suggested methodology to adopting the NIST CSF in an iterative fashion                                          |

**The 5 functions of the Cybersecurity framework**

High level strategic overview of of the lifecycle of an organisations management of their cybersecurity risk.

The following is the 5 **core** functions and each of the categories within those functions. There is a multitude of *subcategories* that follow that but the framework spans across over 900 controls. It is not about memorisation but rather about knowing what you are looking for.

You can access the framework from the following [link to cybersecurity framework](https://www.nist.gov/cyberframework/framework)\
This will lead you to the website and you can access the Excel sheet for the latest version of the framework.

Within the framework, you can break it down from the 5 core functions, following each category and each subcategories and, **to great benefit**, this leads to the *informative references* and maps each reference for each of the sub categories. This will link it all back to every framework you may utilise in the organisation.

1. `Identify` - *Manage cyber security risk to systems, assets, data and capabilities*
      - Asset Management
      - Business Environment
      - Governance
      - Risk Assessment
      - Risk Management Strategy
      - Supply Chain Risk Management
2. `Protect`   - *Safeguards to ensure delivery of critical infrastructure services*
      - Identity Management & Access Control
      - Awareness and Training
      - Data Security
      - Information Protection Processes and Procedures
      - Maintenance
      - Protective Technology
3. `Detect`   - *Identify the occurence of events*
      - Anomalies and Events
      - Security Continuous Monitoring
      - Detection Processes
4. `Respond`   - *Take action regarding a detected cybersecurity event*
      - Response Planning
      - Communications
      - Analysis
      - Mitigation
      - Improvements
5. `Recover` - *Maintain or restore services*
      - Recovery Planning
      - Improvements
      - Communications

[Back to Top](#table-of-contents)

## Cryptography & VPNs

---
| Terminology                 | Description                                                                                                                                                                               |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clear-text protocols**    | transmit data without any additional security or encryption/transformations which allows an attacker to be able to use **man in the middle** attacks or **eavesdrop** on the data packets |
| **Cryptographic protocols** | transform the data (encrypt) and protect the communication. This makes it difficult for any attacker to **eavesdrop** and gain useful information on the data packets                     |
| **Tunneling protocols**     | wrap a clear-text protocol into a cryptographic one (**VPN**)                                                                                                                             |

There is no alternative to the clear-text protocols so it should only be used on **trusted networks**

### Virtual Proxy Networks VPNs

VPN's act as a tunnel from the client to the private network while going through a public one such as the internet. While acting through a VPN you are also assuming the same protocols of the private network so you are **the same as being directly connected** to a private network.

This tunnel is the "wrap" where you are creating a cryptographic shield or tunnel for your data access to and from the host server. This allows you to use low level packet sniffers such as Wireshark

## Wireshark

---
**Wireshark** is a network sniffer tool that lets you see data sent back and forth over the network. This monitoring of traffic is power as it allows you gain information regarding the connection packets sent when you interact with a destination server.

### HTTP vs HTTPS

---


This is especially important when dealing with HTTP and HTTPS servers and the security features. If a **man in the middle** attacker is able to sniff the traffic on our network and we were to enter a HTTP website with our credentials; the network sniffer would be able to see the successful login and actually capture your username and password directly. This is one of the examples why you don't want to send sensitive information through clear-text protocols.

Alternatively when going through HTTPS you will be able to see that the data packets and the contents are jumbled. The encrypted data is not readeable to someone who has intercepted the data.

**Example of using HTTP to authenticate and wireshark to follow the TCP stream:**

![alt text](https://i.imgur.com/0n6uPOQ.png)

**Example of attempting the same through HTTPS:**

![alt text](https://i.imgur.com/KcZjw4M.png)

As you can see, the results are unreadable due to the encryption through using HTTPS.

[Back to Top](#table-of-contents)

## ISO/OSI Protocol Layering

---
**Open Systems Interconnectivity** 

This is a reference to how we can have each component of the chain can communicate to the right protocol. Networks are all about protocols and these protocols are each related to each step on this layering.

When we send data, the data has the form of a **header**;**payload**. 
- Header: all the relevant information for the protocol to handle it such as; where it needs to be, who has to handle it
- Payload: the actual information you want delivered.

As it follows the hierachy and the protocol wants to use another protocol on one of the **lower layers** then the payload being sent is the header;payload, with its own header. This is referred to as encapsulation as you are putting the original header;payload into the format of being the payload for the lower level protocol to handle.

![alt text](https://i.imgur.com/DBnftLL.png)

![alt text](https://i.imgur.com/7G8dYK3.png)

At each step, the layer receives it owns header with its own instructions. The receiving host does the same operation in reverse order. Doing this means that the **application layer** does not need to know how the **transport or network** layers work: it just hands the packet to the transport layer and so on.


| Five-Layer Internet Protocol Stack | Seven-Layer ISO OSI Reference | TCP/IP Layers |
| :--------------------------------: | :---------------------------: | :-----------: |
|            Application             |          Application          |  Application  |
|                                    |         Presentation          |
|                                    |           Sessions            |
|             Transport              |           Transport           |   Transport   |
|              Network               |            Network            |    Network    |
|                Link                |             Link              |     Link      |
|              Physical              |           Physical            |

### Application Layer

---

Network apps and their protocols reside in this layer.

There include many protocols such as HTTP (which provides for web document request and transfer), SMTP (which provides for transfer of e-mail messages) and FTP (which provides for transfer of files between two end systems).

Certain network functions such as translation of human-friendly names for internet end systems like www.google.com to a 32-bit network address, are also done with the help of a specific application-layer protocol *DNS* or *domain name system*. This transfer of information on the application layer is to exchange packets of info with an application in another end system so we can refer to this packet of information as the message.

**What are the responsibilities of the Application Layer:**

- HTTP provides web doc request & transfer (HyperText Transfer Protocol)
- SMTP email transfer (Simple Mail Transfer Protocol)
- FTP File transfer (File Transfer Protocol)

What is an application-layer message? A transport-layer segment? a network-layer datagram? a link-layer frame?

- application message: packet of information between two end systems in the application layer.
- Transport segment: segment is that packet of information being within the transport layer.
- Network datagram: packets of info that is the responsibility of the network layer to move. Processing the transport-layer segment using the address in the header, delivering the datagram packet to the destination transport-layer.
- Link frames: packets being handled by the link layer, being passed up to the network layer and back receiving again at each node towards the destination

5 Tasks that a layer can perform. Is it possible that one or more of these tasks could be performed by two layers or more?

- error control
- flow control
- segmentation and reassembly
- multiplexing
- connection setup
- These tasks can be duplicated at different layers for example error control often is provided at more than one layer

[Back to Top](#table-of-contents)


### Transport Layer

---

The transport layer transports application-layer messages between app endpoints.\
There are two transport protocols: TCP and UDP. Either one can transport app-layer messages.

TCP provides a connection-oriented service to its apps. This services includes guaranteed delivery of app-layer messages to the destination and flow control (sender/receiver speed matching). TCP breaks long messages into short segments and provides a congestion-control mechanism, so that a source throttles its transmission rate when the network is congested.

UDP protocol provides a connectionless service to its apps. This is a no-frills service that provides no reliability, no flow control and no congestion control.

We can refer to the transport layer packet as a segment.

**What are the responsibilities of the Transport Layer:**

- TCP provides connection-oriented service with guaranteed delivery of application-layer messages. Sender/receiver speed matching also known as Flow Control. Break long messages into short segments and provides congestion-control mechanism so that a source throttles its transmission rate when the network is congested. (Transmission Control Protocol)
- UDP provides connectionless service to its apps. A no frills services that provides no reliability, no flow control and no congestion control.(User Datagram Protocol)



[Back to Top](#table-of-contents)


### Network Layer

---

The network layer is responsible for moving network-layer packets known as datagrams from one host to another.\
Similar to providing a postal service the address of the destination, the transport layer is responsible for getting those segments or messages organised with an address and ready for transport.

The Network layer is responsible for the service of delivering the segment to the destination host.\
Network-layer includes the celebrated IP Protocol which defines the fields in the datagram as well as how the end systems and routers act on these fields. There is only one IP Protocol and all internet components that have a network layer must run a IP Protocol.

The internet's network layer also contains routing protocols that determine the routes that datagrams take between sources and destinations. There are many routing protocols and the network admin can run any routing protocol desired. Although the network layer has both the IP protocol and numerous routing protocols, it is often referred to as the IP layer.

#### **IP Protocol**

  - Defines the fields in the datagram as well as how the end systems and routers act on these fields. Routes the datagram through a series of routers between the source and destination

TCP/IP internet protocol relies on sending information to a target address. This address is known as an IP Address. IP Addresses consists of a 4 octet (bytes), 8 bit address in the form of xx.xx.xx.xx
- 8 bits can support or represent a number from 0 - 255
- This doesn't mean you can assign **any** address starting 0.0.0.0 or 255.255.255.255 to a host. Some addresses are reserved i.e:
  - 0.0.0.0 - 0.255.255.255 represents **this network**
  - 127.0.0.0 - 127.255.255.255 represents **the local host, eg your computer**
  - 192.168.0.0 - 192.168.255.255 reserved for **private networks**

#### **Identify a HOST network**

In order to **fully identify a host** you need to **know its network**. To do that you will need an IP address and **netmask or subnet mask**

![alt text](https://i.imgur.com/qrUzGKR.png)

#### **bitwise AND, OR operation to find network**

Using **bitwise AND operation** between netmask and IP will allow you to find the network part. For example:
- 192.168.33.12/255.255.224.0
  - converting to its binary form
  - AND operation to find the common characters between each represented binary form
  - produces the **network prefix**

![alt text](https://i.imgur.com/xclZz5A.png)

![alt text](https://i.imgur.com/gNPYo6O.png)

You can uncover the host part of the IP address by doing the inverse of a **bitwise AND** operation: **bitwise NOT**
- This will also tell you how many hosts a network can contain. With our example, having 13 bits to represent the hosts, we can work out that 2^13 = 8192 different addresses available.

![alt text](https://i.imgur.com/4MMohlA.png)

![alt text](https://i.imgur.com/nOv506G.png)

[Back to Top](#table-of-contents)


### Link Layer

---

We can refer to link-layer packets as frames. At each node within the chain from host to destination node, the network layer routes the datagram to the link layer, which delivers the datagram to the next node along the route.\
Some link-layer protocols provide reliable delivery, from transmitting node, over one link, to receiving node.

This reliable delivery service is different from the reliable delivery service of TCP: which provides reliable delivery from one end system to another. Examples of link-layer protocols include Ethernet, WiFi, and the cable access networks' DOCSIS protocol.\
As datagrams need to traverse several links to travel from source to destination, a datagram may be handled by different link-layer protocols at different links along its route.

**What are the responsibilities of the Link layer:**
- To move a packet from one node to the next, the network layer relies on the services of the link layer. The network layer passes down the datagram to the link layer and at each node or router, the link layer passes up the datagram to the network again and repeat.
- differing from TCP benefits some link layer protocols provide reliable delivery, from transmitting node, over one link, to receiving node. TCP provide reliability from one end-system to another.
- Examples of protocols in the link layer include Ethernet, WiFi and cable access network's DOCSIS protocol (Data over cable service interface specification)

Hubs & Switches are network devices that forward frames (layer 2 packets) on a local network. They work with link layer network addresses: 
- **MAC (Media Access Control or Physical Address) addresses**:- Uniquely identify a network **card** (layer 2) and this differs from IP addresses identifying a host in a network (layer 3)
  - MAC addresses are 48 bit (6 bytes) long and are expressed in hexadecimal *00:11:AA:22:EE:FF*
  - every host has a MAC & IP address
  - While routers work with IP addresses, **switches work with mac addresses**
    - Switches have multiple interfaces and need ot keep a **forwarding table, CAM table** that binds one or more MAC addresses to an interface.

Switches can be small such as home devices with 4 ports or large such as corporate switches with 64 ports (with potentially additional switches linked off for more ports).\
The main differences between one switch and another is the packet forwarding speed: varying between 10Mbps to 10Gbps.

**Delivering data gram from `A` to `router` to `B`**

When a device sends packet, this packet is handled similar to how you would handle post or mail if you were to do it from home.
- You would write the address of the destination (destination IP address, such as `B`)
- You would also include the address of the post office (destination of **first stop or hop**, MAC address such as `router`)
- On the back you will write your own information (origination IP address, such as `A`)
- On the back you will also write what stop it just departed (**latest stop or hop**, MAC address)

To follow this example; the router will receive the packet from computer A and then rewrite some details about the hop, or stop, the packet has done. It will rewrite the destination MAC address to indicate the next stop and then it will rewrite the origination MAC address to indicate where it just left (the routers MAC address). It will not change the origination or destination IP address.

Special MAC address
- FF:FF:FF:FF:FF:FF - The **broadcast** MAC address that means its delivered to all hosts in the local network (within the same broadcast domain)
- routers do not forward packets coming from one interface if they have the broadcast MAC address

#### **Forwarding**

Forwarding tables or CAM, Content Addressable Memory, is how an interface, switch or router determines the destination, or next hop, the packet needs to make.\
To forward a packet:
- switch reads destination MAC of the frame
- performs look-up in CAM table
- Forwards the packet to the corresponding interface
- If there is no entry with that MAC address, the switch will forward the frame to all its interfaces.

![alt text](https://i.imgur.com/Cjvap80.png)

Example of a forwarding, or CAM table stored in devices RAM. You can also see that a single interface (2) is assigned to **two** different MAC addresses.\
There can be multiple hosts on the same interface and some interfaces without any hosts attached. In this case, it is common for the additional entry to be another switch.

While routers use complex routing protocols to update routing rules, switches just use the source MAC of the packets they process to decide which interface to use when forwarding packets.

| How the CAM table is managed                        |                    Instructions                     |
| :-------------------------------------------------- | :-------------------------------------------------: |
| If MAC not in table:                                |   switch adds new MAC-interface binding to table    |
| if MAC-interface binding already in table:          | its Time to live (TTL) gets updated to avoid expiry |
| if MAC in table but not bound to another interface: |                switch updates table                 |

#### **MAC Address - Discovery**
- IPconfig /all (windows)
- ifconfig (*nix operating systems such as MacOS)(linux)
- ip addr (linux)

#### **ARP - Address Resolution Protocol**

When the source (origination host) knows the IP address of the destination but not the MAC address:
- For a host to send a packet, it needs to know **both** the IP and MAC to build a proper packet.

So when this situation happens, the ARP is used to determine to information we needs.\
An example would be for a PC to power up, it knows the IP address of the printers, webservers and such but not the MAC addresses.

If this is the case then the host just needs to know the MAC of other network nodes; then it can learn the MAC addresses of those devices through ARP.

| Using ARP, Host sends traffic to Recipient with only IP | Descriptions                                                                        |
| :------------------------------------------------------ | :---------------------------------------------------------------------------------- |
| 1. **HOST** builds a **ARP** **request**                | Contains IP of Recipient and uses special MAC FF:FF:FF:FF:FF:FF                     |
| 2. **Every** **HOST** receives **ARP** **request**      | Switches using Broadcast MAC or special MAC will broadcast to every host on network |
| 3. **Recipient** responds with **APR** **reply**        | Advising HOST of its MAC address                                                    |

Information is saved in the ARP cache and further traffic does not require a new ARP request. ARP cache entries have a TTL and the host discards an entry at the power off or when the TTL expires.

#### **ARP - Discovery**
- arp -a (windows)
- arp (*nix operating systems, macOS & unix)
- ip neighbour (or neigh, neighbor: equivalent output) (linux)



[Back to Top](#table-of-contents)


### The Physical Layer

---

Link layer moves entire frames from one network element to another network element. The Physical layer is to move the individual bits within the frame from one node to the next. Depending on the transmission medium or access technology, the physical layer is dependent on which one is used for example ethernet has many physical-layer protocols: one for twisted-pair copper and another for coaxial cable and so on.

**What are the responsibilities of the Physical Layer:**

- Link layer moves entire frames from one network element to another network element. The Physical layer is to move the individual bits within the frame from one node to the next. Depending on the transmission medium or access technology, the physical layer is dependent on which one is used for example ethernet has many physical-layer protocols: one for twisted-pair copper and another for coaxial cable and so on

[Back to Top](#table-of-contents)

## Routing

---

Routing protocols determine the **best path** to reach a network. Inspects the destination address and forwards through one of its **forwarding interfaces**

The router performs a **lookup in the routing table** to find an IP-to-interface binding. If the destination is an **unknown network**, or destination doesn't match any other entry on the routing table, then the router defaults to 0.0.0.0 as the address (which can be in the routing table).

Routing protocols are also assigned a **metric to each link** which is selected based on bandwidth and congestion. This ensures that if there are **two paths** to reach the destination with the same number of hops; it will select the fastest route to get to the destination.

Along with routers, hosts stores its own tables as well, use the following to see:
- ip route (linux)
- route print (windows)
- netstat -r (osx)


