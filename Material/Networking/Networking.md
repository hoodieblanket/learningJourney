# The Network Edge

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

#### Encapsulation


