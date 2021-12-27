# LAB&nbsp;4 &nbsp;&nbsp;&nbsp;IPtables

## 1.ping google.com the result is : 
```
erfiboy@Erfi-laptop:~$ ping google.com
PING google.com (142.250.181.238) 56(84) bytes of data.
64 bytes from fra16s56-in-f14.1e100.net (142.250.181.238): icmp_seq=1 ttl=113 time=332 ms
64 bytes from fra16s56-in-f14.1e100.net (142.250.181.238): icmp_seq=2 ttl=113 time=249 ms
64 bytes from fra16s56-in-f14.1e100.net (142.250.181.238): icmp_seq=3 ttl=113 time=383 ms
64 bytes from fra16s56-in-f14.1e100.net (142.250.181.238): icmp_seq=4 ttl=113 time=296 ms
64 bytes from fra16s56-in-f14.1e100.net (142.250.181.238): icmp_seq=6 ttl=113 time=338 ms
```

## 2. Now Block the IP of google using *sudo iptables -A OUTPUT -s 0/0 -d 142.250.181.238-j DROP*&nbsp;:
This rule drop the packages with the destination of 142.250.181.238.
```
erfiboy@Erfi-laptop:~$ sudo iptables -A OUTPUT -s 0/0 -d 142.250.181.238 -j DROPerfiboy@Erfi-laptop:~$ ping google.com
PING google.com (142.250.181.238) 56(84) bytes of data.
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted

```
## 3. what is *sudo iptables -L* &nbsp;:
It's output the List of the current filter rules.

```
erfiboy@Erfi-laptop:~$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       all  --  anywhere             mct01s05-in-f78.1e100.net 
```

## 4. Using *iptables -f* &nbsp; to remove the rules :
```
erfiboy@Erfi-laptop:~$ sudo iptables -F
```
### we can see that rules were removed
```
erfiboy@Erfi-laptop:~$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination       
```

## 5. Block ip google ip address using *ptables -A INPUT -s 142.250.184.206 -j DROP*&nbsp;:
### We didn't get any response because we drop the packages from the source :
```
erfiboy@Erfi-laptop:~$ sudo iptables -A INPUT -s 142.250.184.206 -j DROP
erfiboy@Erfi-laptop:~$ ping google.com
PING google.com (142.250.184.206) 56(84) bytes of data.
```
## 6. *sudo iptables -L* &nbsp;:
New rule added to the source roules which block outgoing traffic.
```
target     prot opt source               destination         
DROP       all  --  fra24s11-in-f14.1e100.net  anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination 
```

## 7. To block 192.168.2.* addresses : 
```
erfiboy@Erfi-laptop:~$ sudo iptables -A INPUT -s 192.168.2.0/24 -j DROP
```

## 8. What do this rules do:
```
 iptables -A INPUT -i lo -p all -j ACCEPT 
```
> It is a rule so your computer to be able to access itself through the loopback interface.
```
 iptables -A INPUT -p all -s localhost -i eth0 -j DROP
```
> It is a rule so that drop alll the packages from localhost and eth0 interface and all protocols.
```
 iptables -A INPUT -s 0/0 -i eth0 -d 192.168.1.1 -p TCP -j ACCEPT
```
> It is a rule that accept the packets using TCP protocols and are from localhost and interface eth0.
```
 iptables -A FORWARD -s 0/0 -i eth0 -d 192.168.1.58 -o eth1 -p TCP --sprt 1024:65535 --dport:80 -j ACCEPT:
```
> It forward all the packets from the port 1024-65535 and the interface eth0 and source localhost to the destination of 192.168.1.58 and port 80 and the Tcp protocol.

## 9. What do this rules do:
```
iptables -A INPUT -p tcp -s IP --dport 22 -j ACCEPT

```
This rule allow the server to be reachable only from specific IP address on port 22 (which is the ssh port)  

## 10. Block http and https sites
this command will be drop all incoming packages from port 443 (default https port) so the https websites didn't load :
 ```
iptables -I OUTPUT -m tcp -p tcp --dport 443 -j DROP
```
and as default http port is 80 this will block all http sites:
```
iptables -I OUTPUT -m tcp -p tcp --dport 80 -j DROP
```

## 11. Limit ping packages to 5/min
```
iptables -A INPUT -p icmp -m icmp --icmp-type address-mask-request -j DROP
 iptables -A INPUT -p icmp -m icmp --icmp-type timestamp-request -j DROP
 iptables -A INPUT -p icmp -m icmp --icmp-type 8 -m limit --limit 5/second -j ACCEPT
```

## 12. Only enable Input ssh
this code will be disable the output ssh (ssh port is 22):
```
sudo iptables -I OUTPUT -m tcp -p tcp --dport 22 -j DROP
```

### 13. Stop TCP/UDP traffic
For tcp connection the command is :
```
sudo iptables -A INPUT -p tcp -j DROP
```
For udp connection the command is :
```
sudo iptables -A INPUT -p udp -j DROP
```

### 14. Protecting a server 
We will begin by implementing a firewall configuration for our servers. We will be locking down almost everything other than SSH traffic as just did in part 10 and somehow 12 and a bit more advance (we just block hhtps and hhtp we must block all ports that we didn't use).

first we let look at definition of ping flood which is:
>Ping flood, also known as ICMP flood, is a common Denial of Service (DoS) attack in which an attacker takes down a victim’s computer by overwhelming it with ICMP echo requests, also known as pings.

so to prevent this kind of attack we must do a practice like part 11 to limit the maxmimum number of packages/min.

allow only a set of specific IPs in firewall for example onlu local IPs to prevent connection of others to access to the server.





