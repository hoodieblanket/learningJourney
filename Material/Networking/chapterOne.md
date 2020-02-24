# Computer Networks and the Internet

`Output Buffer` Buffer is similar to a store or queue for the bits or packets as its being sent. The `Output Buffer` can be overloaded when packets are sent simultaneously from several sources and causes a overflow or queue of work that needs to be sent.

`Forwarding Table` maps destination addresses to that router's outbound links. When the packet arrives at the router the router examines the address and searches its forwarding table, using this destination address, to find the appropriate outbound link.

*How are `Forwarding Tables` set?:* The internet has a number of special routing protocols that are used to auto set the forwarding tables.

`Circuit Switching` is a little different the `Packet Switching` in that Circuit-switched networks are similar to reservations at a restaurant. In order for the data to travel, it needs to be in an ordered sequence. Whereas `Packet-switched` networks are on a no-reservations idea that the data arrives and if theres a queue, then it needs to join the buffer. 

Traditional telephone networks are an example of this `circuit-switched` network interaction where a person dials out and waits for the receiver to accept. The *switches* on the path between the dialer and the receiver maintain that connection state for the required duration at a *guaranteed* constant rate. 

The internet is an example of `Packet-switched` network. There is no reservation of a link and if the packets are transmitted while there is congestion then it will have to sit in the buffer on the sender's side. There is *no guarantee*.

`Frequency-Division Multiplexing FDM` the frequency spectrum of a link is divided up among the connections established across the link.

`Time-Division Multiplexing TDM` time is divided into frames of fixed duration and each frame is divided into a fixed number of time slots. When the network establishes a connection across a link of networks, the network dedicates one time slot in every frame to this connection.

# Total Nodal Delay (made up of nodal processing delay, queuing delay, transmission delay and propagation delay)

### Types of Delay

*_Processing Delay_* time to examine the packets header and determine where to direct the packet is part of the processing delay. The packet header is referring to the address that the packet has for where its destination is. This delay can also include other factors such as the time needed to check for bit-level errors that may have happened while it was being sent through the upstream link.

*_Queuing Delay_* self explanatory. Packet is waiting in queue to be transmitted, if there is a queue.

*_Transmission Delay_* Time required to transmit or push all of the packet's bits into the link. Denoted by *L* bits and divided by *R* bits/sec which is the speed of your connection. (10 Mbps, R = 10)

*_Propagation Delay_* The time required to propagate from the beginning of the link (when the packet has been pushed/transmitted into the link) and the time it arrives at the destination. It is limited by the technology of the physical medium such as twisted pair, fiber optic and so on.

*_Packet Loss_* A packet can arrive at the queue and because queue capacity is finite, it would have no place to store the packet so the router will *drop* the packet. This overflow at the queue shows how packet loss can occur. The fraction of lost packets increases as the traffic intensity increases. Therefor the performance at the node is measured in delay as well as the probability of packet loss.

### Protocol Layering

|Five-Layer Internet Protocol Stack|Seven-Layer ISO OSI Reference|
|:---:      |:---:          |
|Application|Application    |
|           |Presentation   |
|           |Sessions       |
|Transport  |Transport      |
|Network    |Network        |
|Link       |Link           |
|Physical   |Physical       |

*application-layer protocols* such as HTTP and SMTP is almost always implemented in the software in the end systems; so are *transport-layer protocols*.\
The *physical layer* and *data link layer* are responsible for handling communication over a specific link, they are typically implemented in a network interface card (such as ethernet or WiFi interface cards) associated with a given link
*Network layering* is often a mixed implementation of hardware and software.

#### Application Layer

Network apps and their protocols reside in this layer. There include many protocols such as *HTTP* (which provides for web document request and transfer), *SMTP* (which provides for transfer of e-mail messages) and *FTP* (which provides for transfer of files between two end systems). Certain network functions such as translation of human-friendly names for internet end systems like www.google.com to a 32-bit network address, are also done with the help of a specific application-layer protocol *DNS* or *domain name system*. This transfer of information on the application layer is to exchange packets of info with an application in another end system so we can refer to this packet of information as the __message__.

#### Transport Layer

The transport layer transports application-layer messages between app endpoints.\
There are two transport protocols: TCP and UDP. Either one can transport app-layer messages.\

__TCP__ provides a connection-oriented service to its apps. This services includes guaranteed delivery of app-layer messages to the destination and flow control (sender/receiver speed matching). __TCP__ breaks long messages into short segments and provides a congestion-control mechanism, so that a source throttles its transmission rate when the network is congested.

__UDP__ protocol provides a connectionless service to its apps. This is a no-frills service that provides no reliability, no flow control and no congestion control.

We can refer to the transport layer packet as a __segment__

#### Network Layer

The network layer is responsible for moving network-layer packets known as __datagrams__ from one host to another.

Similar to providing a postal service the address of the destination, the transport layer is responsible for getting those segments or messages organised with an address and ready for transport. 

The Network layer is responsible for the service of delivering the segment to the destination host.

Network-layer includes the celebrated __IP Protocol__ which defines the fields in the datagram as well as how the end systems and routers act on these fields. There is only one __IP Protocol__ and all internet components that have a network layer must run a __IP Protocol__.

The internet's network layer also contains __routing protocols__ that determine the routes that datagrams take between sources and destinations. There are many __routing protocols__ and the network admin can run any __routing protocol__ desired. Although the network layer has both the IP protocol and numerous routing protocols, it is often referred to as the __IP layer__.

#### Link Layer

We can refer to link-layer packets as __frames__. At each node within the chain from host to destination node, the network layer routes the __datagram__ to the link layer, which delivers the __datagram__ to the next node along the route. Some link-layer protocols provide reliable delivery, from transmitting node, over one link, to receiving node.

This reliable delivery service is different from the reliable delivery service of __TCP__; which provides reliable delivery from one end system to another. Examples of link-layer protocols include __Ethernet__, __WiFi__, and the __cable access networks' DOCSIS protocol__.

As __datagrams__ need to traverse several links to travel from source to destination, a __datagram__ may be handled by different link-layer protocols at different links along its route.

### The OSI Model

The __International Organisation for Standardisation (ISO)__ proposed that computer networks be organised around seven layers referred to as __Open Systems Interconnection (OSI)__ model. These 5 layers are similar to the 5 layers internet protocol stack. The key differences is the 2 additional layers for the OSI model: Presentation Layer and Session Layer.

#### Presentation Layer

To provide services that allow communicating applications to interpret the meaning of data exchanged. These services include data compression and data encryption as well as data description.

#### Session Layer

Provides for delimiting and synchronisation of data exchange, including the means to build a checkpointing and recovery scheme.

#### Which is preferred Five-layer or Seven-layer

Difficult to say as the internet's answer is always the same: it's up to the developer. Whether the developer requires the services from the seven-layer osi model or just from the five-layer internet protocol stack; it is up to the application developer to build that functionality into the application.

### Networks Under attack


#### The bad guys can put malware into your host via the internet. 

Malware can:\
   * Delete our files
   * Install spyware
   * Collect private info such as passwords, keystrokes and data
   * Enrol the host in a network of thousands of similarly compromised devices collectively known as a __botnet__ leveraged for spam e-mail distribution or distributed denial-of-service attacks.
   * A lot of malware out there today is __self-replicating__: once it infects one host, from there it seeks entry into other hosts over the internet, and so on.
   * Can spread in the form of a __virus__ or __worm__:
      * __Viruses__ are malware that require some form of user interaction in order to infect the user's device. For example an e-mail attachment containing malicious executable code. This is usually an example of __self-replicating__ as once the user opens the attachment and infects the host, the malicious code often sends out similar e-mails to every recipient in the user's address book and so on.
      * __Worms__ can enter devices without any explicit user interaction. For example a user might be running a vulnerable network application to which an attacker can send malware. In some cases, the application may accept the malware from the internet and run it, creating a __worm__. The __Worm__ then scans the internet, searching for other hosts running the same vulnerable network application and repeat the process.
      
#### The bad guys can attack servers and network infrastructure
      
__Denial-of-Service (DoS)__ renders a network, host or other infrastructure unusable by legitimate users. Most __DoS__ attacks fall under three categories:
   * Vulnerability attack
      - This involves sending a few well-crafted messages to a vulnerable application or operating system running on a targeted host. If the __right sequence of packets__ is sent to a vulnerable application or operating system, the service can stop or, worse, the host can crash.
   - Bandwidth flooding
      - The attacker sends a deluge of packets to the targeted host. So many packets that the target's access link becomes clogged, preventing legitimate packets from reaching the server.
   - Connection flooding
      - The attacker establishes a large number of half-open or fully open TCP connections at the target host. Host can become bogged down by these bogus connections that it stops accepting legitimate connections.
      
__Bandwidth flooding__ If the server has a access rate of *R* bps, then the attacker would need to send traffic at a rate approximately *R* bps to cause damage. If *R* is very large then a single attack source may not be able to generate enough traffic to harm the server. Additionally if the attack comes from a single source than an upstream router will usually be able to detect the attack and block all traffic from that source.

In a __Distributed Denial of Service (DDoS)__ attack, the attacker controls multiple sources and has each source blast traffic at the target. With this approach then the aggregate *R* needs to be approximately the same *R* as the host to cripple their services and with multiples attackers, achieving the *R* becomes easier.

#### The bad guys can sniff packets

Majority of households these days access the internet via wireless devices. While convenient, these create a major vulnerability.

By placing a passive receiver in the vicinity of the wireless transmitter, that receiver can obtain a copy of every packet that is transmitted. __These packets can contain all kinds of sensitive information, including passwords, numbers, trade secrets, and private personal messages__. A passive receiver that records a copy of every packet that flies by is called a __packet sniffer__. Sniffers can be deployed in wired environments as well.

Due to __packet sniffers__ being passive, that is not injecting any packets, it is difficult to detect. So when we send packets into a wireless channel we must accept the possibility that some bad guy may be recording copies of our packets. Some of the best defenses against packet sniffing involve cryptography.

#### The bad guys can masquerade as someone you trust

__IP spoofing__ is one of the many ways that a user can masquerade as another or such that it injects packets into the internet with a false __source__ address. The user creates a arbitrary source address, packet content and destination address and then transmit this packet into the internet. The internet will forward the packet to its destination. Imagine the *unsuspecting receiver such as a internet router* who receives the packet, takes the source address as being truthful then performs some command __embedded in the packet's contents__ (say modifies the forwarding table). This is __IP spoofing__.

### Review Questions

* Difference between a host and an end system:
   * End systems(end stations) sit on the edge of the network. the end user always interacts with the end systems. systems that connect to the internet are also called internet hosts. They host(run) internet applications (web browser or email retrieval program). Mail servers or web servers are end systems that the user does not interact with.
   * Host is a device connected to other devices for which it provides data or services over the network. Host is interchangeable with End systems however the host, by its own name, hosts the internet for all devices connected to the network.

* Protocol in diplomacy:
   * Refers to a set of rules, procedures and conventions that relate to relations between states. Specify the proper generally accepted behaviour in matters.
   
* Why are standards important for protocols
   * It's important for protocols to be accepted across a broad group so that there is structure or a set or rules, procedures and conventions that spread across nations, languages and influences.

* Six access technologies (Home, Enterprise or wide-area wireless)
   * (Home) DSL, Cable, FTTH, Dial-up
   * (Enterprise, Home) Ethernet, WiFi
   * (Wide-area wireless) 3G, 4G, LTE

* Is HFC transmission rate dedicated or shared among users
   * Cable or HFC is a shared broadcast medium. Shared as it moves upstream and downstream and is the reason why if the line is congested, speeds will be significantly lesser than the aggregate downstream rate. The data on the downstream originates from the head-end and as such has no risk of collision.
   * Because the upstream rate is also shared, a distributed multiple access protocol is needed to coordinate transmissions to avoid collisions.

* Transmission rate of Ethernet LAN's
   * 10Mbps, 100Mbps, 1Gbps, 10Gbps using twisted pair copper. Depends on the thickness of the wire and the distance between transmitter and receiver. Cat 6a cable is twisted pair and can achieve rates of 10Gbps for distances up to a hundred meters.

* Physical media for the Access technologies
   * HFC - Hybrid Fiber Coax cable or a combo of fiber and coaxial.
   * DSL and Ethernet use copper wire
   * Mobile networks use radio spectrum
   * Fiber using optical fiber
   * Satellite radio channels using geostationary and low-earth orbiting satellites.
   
* Transmission Rates for Dial-up, HFC, DSL and FTTH (Shared or not?)
   * Dial-up - 56kbps (Dedicated)
   * DSL - 24 Mbps Down / 2.5 Mbps Up (Dedicated)
   * HFC - 42.8 Mbps Down / 30.7 Mbps Up (Shared)
   * FTTH - potentially gigabits per second range. (Dedicated)

* What advantage does a circuit-switched network have over a packet-switched network. Advantages of TDM over FDM in circuit-switched?
   * circuit-switched reserves the resources needed along a path to provide for communication between end-systems. Packet-switched does not reserve the resources as it is on-demand and may have delays if there is queues as a first-in first-served ideal.
   * TDM - Time-division multiplexing over FDM - Frequency-division multiplexing. FDM has the frequency spectrum of a link divided among the connections. For TDM, time is divided into frames of fixed duration and each frame is divided into a fixed number of time slots. When the network establishes a connection, the network dedicates one time slot in every frame to this connection. FDM each circuit continuously gets a fraction of the bandwidth. TDM each circuiot gets all the bandwidth periodically during brief intervals of time.

* Why will two ISP's at the same level of hierachy often peer with each other and how does an IXP earn money
   * If the 2 ISP's do not peer with each other then when they send traffic to each other they have to send the traffic through a provider ISP (3rd party) to which they have to pay for carrying the traffic.
   * IXP or Internet Exchange Point makes money by charging each of the ISP's that connect to the IXP a small fee depending on amount of traffic sent or received through the IXP.

* Some content providers created their own networks. Describe Google's network. Why do they create their own networks?
   * Gives the content provided more control over the quality of the service they provide the user. Save money by sending less traffic into provider networks. If ISp's decide to charge more money to highly profitable content providers ( in countries with no net neutrality), the content providers can avoid these extra payments.

* Sending over a fixed route: What delays are there and which delays are constant and which are variable?
   * Processing, Queueing, Transmission, Propagation.
   * Only Queueing Delays are variable.
   
* Describe how end system A creates packets from the file. When one of these packets arrive to a packet switch, what info in the packet does the switch use to determine the link onto which the packet is forwarded?
   - The packet switch reads the header address of where to send the packet. Starting from each section similar to a physical address (the country, then the region, then the area, then the street, then the number). This is analogous to driving as the directions are taken to reach each new *area* then asking for the next direction from the header to proceed to the next and so on.
   - system A breaks the large file into chunks. Adds header to each chunk thereby making multiple packets from the file. Each header has a destination IP address to reach system B
   
- 5 Tasks that a layer can perform. Is it possible that one or more of these tasks could be performed by two layers or more?
   - error control
   - flow control
   - segmentation and reassembly
   - multiplexing
   - connection setup
   - These tasks can be duplicated at different layers for example error control often is provided at more than one layer
   
- 5 Layers of the internet protocol stack? What are the responsibilities of each layer
   - **Application**: 
      - HTTP provides web doc request & transfer (HyperText Transfer Protocol)
      - SMTP email transfer (Simple Mail Transfer Protocol)
      - FTP File transfer (File Transfer Protocol)
   - **Transport**:
      - TCP provides connection-oriented service with guaranteed delivery of application-layer messages. Sender/receiver speed matching also known as *Flow Control*. Break long messages into short segments and provides congestion-control mechanism so that a source throttles its transmission rate when the network is congested. (Transmission Control Protocol) 
      - UDP provides connectionless service to its apps. A no frills services that provides no reliability, no flow control and no congestion control.(User Datagram Protocol)
   - **Network**:
      - IP Protocol:
         - Defines the fields in the datagram as well as how the end systems and routers act on these fields. Routes the datagram through a series of routers between the source and destination
   - **Link**:
      -  To move a packet from one node to the next, the network layer relies on the services of the link layer. The network layer passes down the datagram to the link layer and at each node or router, the link layer passes up the datagram to the network again and repeat.
      - __differing from TCP benefits__ some link layer protocols provide reliable delivery, from transmitting node, over one link, to receiving node. TCP provide reliability from one end-system to another.
      - Examples of protocols in the link layer include Ethernet, WiFi and cable access network's DOCSIS protocol (Data over cable service interface specification) 
   - __Physical__:
      - Link layer moves entire *frames* from one network element to another network element. The Physical layer is to move the __individual bits__ within the frame from one node to the next. Depending on the transmission medium or access technology, the physical layer is dependent on which one is used for example ethernet has many physical-layer protocols: one for twisted-pair copper and another for coaxial cable and so on.

- What is an application-layer message? A transport-layer segment? a network-layer datagram? a link-layer frame?
   - application __message__: packet of information between two end systems in the application layer.
   - Transport **segment**: segment is that packet of information being within the transport layer.
   - Network **datagram**: packets of info that is the responsibility of the network layer to move. Processing the transport-layer segment using the address in the header, delivering the datagram packet to the destination transport-layer.
   - Link __frames__: packets being handled by the link layer, being passed up to the network layer and back receiving again at each node towards the destination
   

- Which layers in the Internet protocol stack does a router process? Which layers does a link-layer switch process? Which layers does a host process?
   - Routers process network, link and physical layers. (layers 1 through 3)
   - Link layer switches process link and physical layers. Host process all five layers.

- What is the difference between a virus and a worm?
   - A __Virus__ is malicious software that involves user interaction. For example opening a link or application that infects the host. It can then seek to spread itself (self-replicating).
   - A __Worm__ is malware that is not through user interaction. This could be a vulnerable host that has been attacked or sometimes the user themselves have not interacted however the end-system has interacted with it without user input.
   
- Describe how a botnet can be created, and how it can be used for a DDoS attack.
   - A botnet can form from infected hosts that has respond to an attacker. This botnet or collection of end-systems can be used to perform a simultaneous attack with or without the users' knowledge. By attack, we mean the botnet can perform legitimate (empty) requests through to a service at the same time thereby overloading the service and causing it to not be able to provide service to the legitimate requests. This is typically done with an attack called __bandwidth flooding__.

- Suppose Alice and Bob are sending packets to each other over a computer network. Suppose Trudy positions herself in the network so that she can capture all the packets sent by Alice and send whatever she wants to Bob; she can also capture all the packets sent by Bob and send whatever she wants to Alice. List some of the malicious things Trudy can do from this position.
   - Trudy can completely impersonate alice or bob. Can modify partial or full messages to her own benefit and can also remove/delete packets even if they are encrypted.


