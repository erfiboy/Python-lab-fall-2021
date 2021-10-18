# **Introduction to Linux**

## ‫‪1. Virtual‬‬ ‫‪Machine‬‬

### What is the diffrence between NAT‬‬ ‫‪Bridged‬‬ ‫‪Host‬‬ ‫‪-‬‬ ‫‪Only‬‬ ?
> #### Network Address Translation (NAT) 

- This configuration will be create a virtual router on the host and all the trafic will pass through the host which the Virtual machine is running on.The IP of the VM is the subnet of the host IP and all VM's IPs are diffrent.

> #### Bridged‬‬ ‫‪Host
 - This configuration will be create an IP address on the same domain as host. And it is like having another machine on that network.

> #### Host‬‬ ‫‪-‬‬ ‫‪Only
- This configuration will be create a local network and VMs will only see the other VMs on that host and don't have access to the internet.


## 2. ‫‪System‬‬ ‫‪Configuration‬‬

## 3. ‫‪Command‬‬ ‫‪Line‬‬

### 3.1 installing, run and remove fortuneInstalling fortune:
> $ sudo apt install fortune </br>

Run the fortune:

> $ fortune </br>
> output:  "Elves and Dragons!" I says to him.  >"Cabbages and potatoes are better
>for you and me."
></br>		-- J. R. R. Tolkien

See the installed packages 
> $ apt list 

See the specified package 

> $ apt list | grep fortune

Removing fortune:

> $ sudo apt remove fortune</br>
> $ sudo apt remove fortune-mod</br>
> output: Reading package lists... Done </br>
Building dependency tree       </br>
Reading state information... Done</br>
The following packages were automatically installed</br> and are no longer required:
  </br>fortunes-min librecode0
</br>Use 'sudo apt autoremove' to remove them.
</br>The following packages will be REMOVED:
  fortune-mod
</br>0 upgraded, 0 newly installed, 1 to remove and 27 not upgraded.
</br>After this operation, 110 kB disk space will be freed.
</br>Do you want to continue? [Y/n] y
</br>(Reading database ... 274215 files and directories currently installed.)
</br>Removing fortune-mod (1:1.99.1-7build1) ...
</br>Processing triggers for man-db (2.9.1-1) ...

See the installed packages 
> $ apt list 

See the specified package and make sure that it has been removed

> $ apt list | grep fortune

### 3.2 Directories
Go to Home:
> $ cd </br>

Create A and B directories in Home:
> $ mkdir A B

Go to A with the absolute path:
> $ cd ~/A

Go to B with reletive path:
> $ cd ../B 

Create a file which is golab, in A directory
> $ touch golabi

Copy golabi to A directory:
>$ cp golabi ../B

Move golabi to Desktop:
>$ mv golabi ~/Desktop/

Remove the directory B with the flag -r:
>$ rm -r ~/B

### 3.3 ls
![This is an image](./etc-ls.png)

