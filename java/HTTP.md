# OSI model
![[Pasted image 20231003212820.png]]
## application layer 
- [**TELNET:**](https://www.geeksforgeeks.org/introduction-to-telnet/) Telnet stands for Telecommunications Network. This protocol is used for managing files over the Internet. It allows the Telnet clients to access the resources of Telnet server. Telnet uses port number 23.
- [**DNS:**](https://www.geeksforgeeks.org/domain-name-system-dns-in-application-layer/) DNS stands for Domain Name System. The DNS service translates the domain name (selected by user) into the corresponding IP address. For example- If you choose the domain name as www.abcd.com, then DNS must translate it as 192.36.20.8 (random IP address written just for understanding purposes). DNS protocol uses the port number 53.
- [**DHCP:**](https://www.geeksforgeeks.org/dynamic-host-configuration-protocol-dhcp/) DHCP stands for Dynamic Host Configuration Protocol. It provides IP addresses to hosts. Whenever a host tries to register for an IP address with the DHCP server, DHCP server provides lots of information to the corresponding host. DHCP uses port numbers 67 and 68.
- [**FTP:**](https://www.geeksforgeeks.org/file-transfer-protocol-ftp-in-application-layer/) FTP stands for File Transfer Protocol. This protocol helps to transfer different files from one device to another. FTP promotes sharing of files via remote computer devices with reliable, efficient data transfer. FTP uses port number 20 for data access and port number 21 for data control.
- [**SMTP:**](https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/) SMTP stands for Simple Mail Transfer Protocol. It is used to transfer electronic mail from one user to another user. SMTP is used by end users to send emails with ease. SMTP uses port numbers 25 and 587.
- [**HTTP:**](https://www.geeksforgeeks.org/http-full-form/) HTTP stands for Hyper Text Transfer Protocol. It is the foundation of the World Wide Web (WWW). HTTP works on the client server model. This protocol is used for transmitting hypermedia documents like HTML. This protocol was designed particularly for the communications between the web browsers and web servers, but this protocol can also be used for several other purposes. HTTP is a stateless protocol (network protocol in which a client sends requests to server and server responses back as per the given state), which means the server is not responsible for maintaining the previous client’s requests. HTTP uses port number 80.
- [**NFS:**](https://www.geeksforgeeks.org/network-file-system-nfs/) NFS stands for Network File System. This protocol allows remote hosts to mount files over a network and interact with those file systems as though they are mounted locally. NFS uses the port number 2049.
- [**SNMP:**](https://www.geeksforgeeks.org/simple-network-management-protocol-snmp/) SNMP stands for Simple Network Management Protocol. This protocol gathers data by polling the devices from the network to the management station at fixed or random intervals, requiring them to disclose certain information. SNMP uses port numbers 161 (TCP) and 162 (UDP).
## data link layer
### logic link control
### Media Access control 
### 涉及的协议
1. Synchronous Data Link Protocol (SDLC)
2. High-Level Data Link Protocol (HDLC）
3. Serial Line Interface Protocol (SLIP)
4. Point to Point Protocol (PPP
5. Link Access Procedure (LAP)
6. Link Control Protocol (LCP)
7. Network Control Protocol (NCP)
![[Pasted image 20231003211026.png]]
ARP(address resolution protocol):解析IP地址从而获取MAC(物理地址media access control address)
![[Pasted image 20231003211445.png]]
- transport layer
- network layer
##  presentation layer
- [**Apple Filing Protocol (AFP):**](https://www.geeksforgeeks.org/afp-fullform/) Apple Filing Protocol is the proprietary network protocol (communications protocol) that offers services to macOS or the classic macOS. This is basically the network file control protocol specifically designed for Mac-based platforms.
- **Lightweight Presentation Protocol (LPP):** Lightweight Presentation Protocol is that protocol which is used to provide ISO presentation services on the top of TCP/IP based protocol stacks.
- [**NetWare Core Protocol (NCP):**](https://www.geeksforgeeks.org/introduction-of-novell-netware/) NetWare Core Protocol is the network protocol which is used to access file, print, directory, clock synchronization, messaging, remote command execution and other network service functions.
- **Network Data Representation (NDR):** Network Data Representation is basically the implementation of the presentation layer in the OSI model, which provides or defines various primitive data types, constructed data types and also several types of data representations.
- **External Data Representation (XDR):** External Data Representation (XDR) is the standard for the description and encoding of data. It is useful for transferring data between computer architectures and has been used to communicate data between very diverse machines. Converting from local representation to XDR is called encoding, whereas converting XDR into local representation is called decoding.
- Secure Socket Layer (SSL)
## Session layer
This layer basically establishes a connection between the session entities.
### 涉及协议
- [**AppleTalk Data Stream Protocol (ADSP):**](https://www.geeksforgeeks.org/adsp-fullform/) ADSP is that type of protocol which was developed by Apple Inc. and it includes a number of features that allow local area networks to be connected with no prior setup. This protocol was released in 1985.   
    This protocol rigorously followed the OSI model of protocol layering. ADSP itself has two protocols named: AppleTalk Address Resolution Protocol (AARP) and Name Binding Protocol (NBP), both aimed at making system self-configuring.
- [**Real-time Transport Control Protocol (RTCP):**](https://www.geeksforgeeks.org/real-time-transport-control-protocol-rtcp/) RTCP is a protocol which provides out-of-band statistics and control information for an RTP (Real-time Transport Protocol) session. RTCP’s primary function is to provide feedback on the quality of service (QoS) in media distribution by periodically sending statistical information such as transmitted octet and packet counts or packet loss to the participants in the streaming multimedia session.
- [**Point-to-Point Tunneling Protocol (PPTP):**](https://www.geeksforgeeks.org/pptp-full-form/) PPTP is a protocol which provides a method for implementing virtual private networks. PPTP uses a TCP control channel and a Generic Routing Encapsulation tunnel to encapsulate PPP (Point-to-Point Protocol) packets This protocol provides security levels and remote access levels comparable with typical VPN (Virtual Private Network) products.
- [**Password Authentication Protocol (PAP):**](https://www.geeksforgeeks.org/password-authentication-protocol-pap/) Password Authentication Protocol is a password-based authentication protocol used by Point to Point Protocol (PPP) to validate users. Almost all network operating systems, remote servers support PAP. PAP authentication is done at the time of the initial link establishment and verifies the identity of the client using a two-way handshake (Client-sends data and server in return sends Authentication-ACK (Acknowledgement) after the data sent by client is verified completely).
- [**Remote Procedure Call Protocol (RPCP):**](https://www.geeksforgeeks.org/remote-procedure-call-rpc-in-operating-system/) Remote Procedure Call Protocol (RPCP) is a protocol that is used when a computer program causes a procedure (or a sub-routine) to execute in a different address space without the programmer explicitly coding the details for the remote interaction. This is basically the form of client-server interaction, typically implemented via a request-response message-passing system.
- **Sockets Direct Protocol (SDP):** Sockets Direct Protocol (SDP) is a protocol that supports streams of sockets over Remote Direct Memory Access (RDMA) network fabrics.  
    The purpose of SDP is to provide an RDMA-accelerated alternative to the TCP protocol. The primary goal is to perform one particular thing in such a manner which is transparent to the application.
## physical layer
###  physical topology
Physical Topology or [Network Topology](https://www.geeksforgeeks.org/types-of-network-topology/) is the Geographical Representation of Linking devices. Following are the four types of physical topology-
1. **Mesh Topology:** In a mesh topology, each and every device should have a dedicated point-to-point connection with each and every other device in the network. Here there is more security of data because there is a dedicated point-to-point connection between two devices. Mesh Topology is difficult to install because it is more complex.
2. **Star Topology:** In [star topology](https://www.geeksforgeeks.org/advantages-and-disadvantages-of-star-topology/), the device should have a dedicated point-to-point connection with a central controller or hub. Star Topology is easy to install and reconnect as compared to Mesh Topology. Star Topology doesn’t have Fault Tolerance Technique.
3. **Bus Topology:** In a [bus topology](https://www.geeksforgeeks.org/advantages-and-disadvantages-of-bus-topology/), multiple devices are connected through a single cable that is known as backbone cable with the help of tap and drop lines. It is less costly as compared to Mesh Topology and Star Topology. Re-connection and Re-installation are difficult.
4. **Ring Topology:** In a [ring topology](https://www.geeksforgeeks.org/advantages-and-disadvantages-of-ring-topology/), each device is connected with repeaters in a circle-like ring that’s why it is called Ring Topology. In Ring Topology, a device can send the data only when it has a token, without a token no device can send the data, and a token is placed by Monitor in Ring Topology.
## TCP/IP协议
![[Pasted image 20231003215553.png]]
### network layer
- ***IP*** stands for Internet Protocol and it is responsible for delivering packets from the source host to the destination host by looking at the IP addresses in the packet headers. IP has 2 versions: IPv4 and IPv6. IPv4 is the one that most websites are using currently. But IPv6 is growing as the number of IPv4 addresses is limited in number when compared to the number of users.
- ***ICMP:*** for Internet Control Message Protocol. It is encapsulated within IP datagrams and is responsible for providing hosts with information about network problems.
- ****ARP:**** Address Resolution Protocol. Its job is to find the hardware address of a host from a known IP address. ARP has several types: Reverse ARP, Proxy ARP, Gratuitous ARP, and Inverse ARP.
### transport layer
- ****TCP:**** Applications can interact with one another using TCP though they were physically connected by a circuit. TCP transmits data in a way that resembles character-by-character transmission rather than separate packets. A starting point that establishes the connection, the whole transmission in byte order, and an ending point that closes the connection make up this transmission.
- ****UDP:**** The datagram delivery service is provided by UDP, the other transport layer protocol. Connections between receiving and sending hosts are not verified by UDP. Applications that transport little amounts of data use UDP rather than TCP because it eliminates the processes of establishing and validating
### application layer
- ****HTTP and HTTPS:**** stands for Hypertext transfer protocol. It is used by the World Wide Web to manage communications between web browsers and servers. HTTPS stands for HTTP-Secure. It is a combination of HTTP with SSL(Secure Socket Layer). It is efficient in cases where the browser needs to fill out forms, sign in, authenticate, and carry out bank transactions.
- ****SSH:**** stands for Secure Shell. It is a terminal emulations software similar to Telnet. The reason SSH is preferred is because of its ability to maintain the encrypted connection. It sets up a secure session over a TCP/IP connection.
- ****NTP:**** stands for Network Time Protocol. It is used to synchronize the clocks on our computer to one standard time source. It is very useful in situations like bank transactions. Assume the following situation without the presence of NTP. Suppose you carry out a transaction, where your computer reads the time at 2:30 PM while the server records it at 2:28 PM. The server can crash very badly if it’s out of sync.
## TCP协议
![[Pasted image 20231003220701.png]]
# UDP
# HTTP/HTTPS
# Session/cookie