# Learning Security Plus from Comptia <!-- omit in toc -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Key Definitions](#key-definitions)
- [CIA Triad](#cia-triad)
- [AAA of Security](#aaa-of-security)
- [Security Threats](#security-threats)
  - [Malware](#malware)
  - [Unauthorized Access](#unauthorized-access)
  - [System Failure](#system-failure)
  - [Social Engineering](#social-engineering)
- [Mitigating Threats](#mitigating-threats)
  - [Physical Controls](#physical-controls)
  - [Technical Controls](#technical-controls)
  - [Administrative (Managerial) Controls](#administrative-managerial-controls)
- [Hackers](#hackers)
  - [White Hat](#white-hat)
  - [Black Hats](#black-hats)
  - [Grey Hats](#grey-hats)
  - [Blue Hats](#blue-hats)
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
  - [Diamond Model of Intrusion Analysis](#diamond-model-of-intrusion-analysis)

## Key Definitions
|                               |                                                                                   |
| :---------------------------- | :-------------------------------------------------------------------------------- |
| `Information Security`        | The protection of data, or the information **on** the systems but not the system\ |
| `Information System Security` | The protection of the systems                                                     |

## CIA Triad

* Confidentiality
* Integrity
* Availability

![alt text](https://i.imgur.com/T8ydhaK.png)

**Confidentiality**

Encryption is another way of thinking confidentiality.

**Integrity**

Ensuring the information has not been modified or altered without proper authorisation\
Integrity is linked in with HASHES and cryptography

**Availability**

Information is accessed, stored and protected at all times. The content is *available*.

Theres three systems need to be in sync in order to allow consumers and vendors to  meet a middle ground that encompasses the desired level of protection while also meeting the convenience or needs from the users.

Without availability, then the system becomes useless as a consumer cannot access the required data. Similar with confidentiality; without that encryption or protection, what user will trust you with the information.

## AAA of Security

* Authentication
* Authorisaton
* Accounting

**Authentication**

Authenticaton of a persons identity with proof and then confirmed by a system. Similar to when logging in to a website and signing it. The system may check several aspects such as confirming:

**5 Methods of Authentication**

- Something you know
  - password or username
- Something you are
  - fingerprint or eye scan
- Something you have
  - credit card or drivers license
- Something you do
  - way that you speak or sign your name, signature
- Somewhere you are
  - GPS locations

**Authorisation**

Areas requiring authentication if you are allowed to access. This would be checking for your token or access that would authorise you to reach a particular area

**Accounting**

Usually a collection of all data to keep track of all the various things are being done. If you have some kind of insider threat or breach then these logs will have a catalogue of changes that occurred and would allow you to pinpoint towards an issue

- Non-repudiation occurs when you have **proof** that someone has taken an action and cannot be disputed such as if you have a unique electronic signature when sending an email. We can establish that the unique key to your signature is unique to only yourself and then we have proof that it can be no one else.

---
## Security Threats

---
### Malware

### Unauthorized Access

### System Failure

### Social Engineering


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

---
## Mitigating Threats

---
### Physical Controls

- Alarm systems, locks, identification cards, security guard 

### Technical Controls

- smart cards, access control lists, network authentication

### Administrative (Managerial) Controls

- Policies, procedures and contingency plans
- Procedural controls
  - What the organisation chooses to do on its own
- Regulatory Controls
  - What the law dictates that you must follow how to protect data or private information

## Hackers

### White Hat

- Non-malicious that is either contracted to a company or employed and attempt to break in at the behest of the company

### Black Hats

- Malicious that are not following the rules

### Grey Hats

- No affiliation to a company but they will still hack into companies without permission
- non-malicious as they are just attempting to do this for the challenge but still breaking the law

### Blue Hats

- Affiliated with the company through getting permissions such as bounty programs or getting permission to test their systems however they are not employed or on the payroll

---
## Threat Actors

---

- Script kiddies
  - unaware of what they are doing but potentially malicious intentionally or unintentionally
- Hacktivists
  - Driven by a cause
- Organised Crime
- Advanced Persistent Threats (APTs)
  - Highly trained and funded groups of hackers such as nation states who have access to open-source intelligence at their disposal

---
## Threat Intelligence and Sources

---
### Measuring quality of intelligence

**Timeliness**

- If the offender is aware that they have been identified then they will being to change their tactics
- Property of Intelligence Source: the report you write might not be up-to-date in 2 days or 2 weeks.

**Relevancy**

- Property of Intelligence source: What affects the organisation? If the reported issues is related to macOS and your business runs windows then you need to consider the relevancy of the reporting to ensure the business can defend against whats relevant

**Accuracy**

- Property of Intelligence Source: Is the information is accurate. Remove false positives such as with software and getting the right information to make good decisions 

**Confidence Levels**

- Property of Intelligence Source: ensures it produces qualified statement about reliability.


### Types of intelligence

**Proprietary**

Subscription based information handled by a private organisation and allowing you to 'buy in' on their collection of data to make it available for your use.

**Closed Source**

Personal research or the providers own research and analysis efforts. The information is behind closed doors and only available for the vendor and their uses. The information gathered might be from their own mining of data through their customers and their products - then using this data anonymously.

**Open Source**

Data without subscription, in the open market and may include threat feeds, reputation lists and malware signature databases

- US-Cert
- UK NCSC
- AT&T Security
- MISP (malware information sharing platform)
- VirusTotal (uploading files to be scanned)
- Spamhaus (for email related information)
- SANS ISC Suspicious domains

**Open Source Intelligence (OSINT)**

Methods of getting information from public records, websites and social media. Gathering data from widely public information to source that information on an individual. 

Any information you can gather about a person through facebook, linkd in and so forth: this is all considered OSINT

---
## Threat Hunting

---

Threat hunting is proactive search for threats or vulnerabilities within your own system that has not been discovered by normal security monitoring.

Pentesting you are often trying to break into your system to demonstrate a weakness however threat hunting you are analysing data within the systems we already have

- less disruptive than a penetration test due to this



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

---
## Attack Frameworks

---

### Lockheed Martin Kill Chain

---
7 step method going from the top to the bottom that works very linear as you work your way down
- reconnaissance: passive information gathering transitioning to active scanning allowing you to come out with great information regarding potentials, vulnerabilities and such based on what network or technologies is evident
- Weaponization: coding or creating the malware that you want to run based on the previous information. Not run yet but the blueprint is up
- Delivery: delivery of the payload and figuring about how we get it to the location we want
- Exploitation: happens when the code is deployed, not when delivered which could sit dormant until triggered.
- Installation: Phase two of the code chaos which will allow us to access the system through remote access and achieve **persistance** on that system to continue with access
- Command & Control (C2): the code has an outbound link to external server. At this point you have full control of the system. You have persistent access, can run commands and remote into the system
- Actions on Objectives: now after the 6 steps, they can actually reach their original going or whatever that may be as they now have full access.

**Reconnaissance** - Goal: Find a weakness
- Information gathering that is either passive gathering or active scanning
- Passive
  - whois
  - ARIN registrations
  - google
  - shodan
  - job listings etc

Protection (Passive)
- limit public information (job listings, linkedin)
- social media acceptable use policies
- modify server error messages

- Active
  - NMAP
  - port scanning
  - banner grabbing
  - vulnerability scanning
    - usually pretty loud and obvious so this might be done slowly and over time to lower the probability of being caught

Protection (Active)
- disable unused ports & services
  - limits number of entry points to your system
- honeypots 
  - diverts from real systems but also may reveal who the adversary is
- firewalls
- IPS
- TOR & 3rd party VPN inbound blocking

**Weaponization** - Goal: select weapon appropriate based on reconnaissance
- Attacks will adapt based on reconnaissance
  - metasploit
  - exploit-db
  - burpsuit
  - social engineering toolkit
- Defense
  - patch management remains the best defense management for the weaponization stage
  - disable: office macros, javascript and browser plugins
  - security basics, antivirus, IPS, email security, Multifactor authentication, audit logging etc..

**Delivery** - Goal: select avenue of delivery the payload or intrusion
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

**Exploitation** - Goal: Gain access but its not a finishing line for the attack

- Attack succeed and the weapon has been delivered
  - SQL injection
  - buffer overflow
  - javascript hijack
  - malware

Protective methods
- DEP data execution prevention
- anti-exploit
- Reality is that if the attacker has gotten to this point, you are relying on preventative tools for post-execution such as a sandbox
  - Potentially capturing patient zero when an unknown file is downloaded, the protections jump in to stop the file from reaching the rest of the network

**Installation** - Goal: Get persistant access

Offensive tools
- DLL hijacking
- meterpreter
- remote access tools (RAT)
- registry changes - making changes or commands startup or persistant
- powershell commands

Protective tools
- Linux:chroot jail to isolate processes from rest of the system so the file has limited access to other data
- windows: disable powershell

Detect tools (post infection)
- UBA/EDR will flag any unauthorised program thats been installed as well as flag any changes in process or system options


Respond
- Follow the incident response SOPs 

A kill chain analysis can allow us to map out how system can gain access, run code, create outbound connections or take control. With this information we can try to defend against each of these stops and jump in somewhere to break that progress

### MITRE ATT&CK Framework

This is a knowledge base maintained by an external company. Open source information that contains the information on various attacks\
This database is great to look at potential common intrusions or events that link to certain types of attacks. By ticking certain events that has happened, you can narrow down likelyhoods or common intrusions that lead to a specific attack that you can start looking signs for and prepare for.

Breaks down the tactics, techniques and procedures to a level wehre you can prioritise your defenses.



### Diamond Model of Intrusion Analysis

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

