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

- less disruptive than a penetration test

**Establishing a hypothesis**

