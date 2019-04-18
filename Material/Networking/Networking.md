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

