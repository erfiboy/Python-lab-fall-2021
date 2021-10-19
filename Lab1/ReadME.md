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

![This is an image](./vpn.png)

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

#### usefull Flags
To list all files in the current directory, type:
> ls -a

This displays a long listing with detailed information:
> ls -l

This displays a list all the files with detail:
> ls -la

This displays files that were modified most recently:
> ls -x

This displays lists all subdirectories recursively:
> ls -R

This displays size of all files:
> ls -s

### 3.4 tree
<pre>
-d     List directories only.
-l     Descend only level directories deep.
</pre>
> $ tree -L 2 -d

### 3.5 suffix
change the suffics of the sqspell to jpg
> $ mv sqspell.php sqspell.jpg
> 
![This is an image](./file.png)

### 3.6 Zsh
![This is an image](./zh.png)


For installing the ‫‪syntax-highlighting‬‬ and ‫‪utocomplete‬‬ you can use [this link](https://linuxhint.com/install_zsh_shell_ubuntu_1804/).


![This is an image](./syntax.png)


## 4 ‫‪Linux‬‬ ‫‪Security‬‬ ‫‪and‬‬ ‫‪Permissions‬‬

Create a user with that it's username is equal to student name:
> $ sudo adduser --force-badname 97102558</br>
> Adding user `97102558' ...</br>
Adding new group `97102558' (1001) ...</br>
Adding new user `97102558' (1001) with group `97102558' ...</br>
Creating home directory `/home/97102558' ...</br>
Copying files from `/etc/skel' ...</br>
New password: </br>
Retype new password: </br>
passwd: password updated successfully</br>
Changing the user information for 97102558</br>
Enter the new value, or press ENTER for the default</br>
	Full Name []: </br>
	Room Number []: </br>
	Work Phone []: </br>
	Home Phone []: </br>
	Other []: </br>

Switch to user:
> $ su 97102558

Create a new user with 97102558:
This instruction cause an error.
> $ adduser ali </br>
>adduser: Only root may add a user or group to the system.

To correct this error we must add the current user to the sudo group:
> $ sudo usermod -aG sudo 97102558

To delete the user:
> $ sudo deluser --remove-home 97102558


## 5 ‫‪Regular‬‬ ‫‪Expressions‬‬

### 5.1 dpkg and grep
To see install packages:
> $ dpkg --list  

to see only only packages including firefox in thier names:
> $ dpkg --list  | grep firefox

### 5.2 find 
Find all files end with .py or .c
> $ find . -type f -name " * .c"  -o " * .py"  

### 5.3 grep
lines strarting with GNU:
> $ grep ’ˆGNU’ ./GPL-1

Find words containing cept 
> $ grep 'cept' GPL-1   

To print all the phrases between phrantises
> $ grep -oP '\(\K[^)]+'

## 6 Pipe & Redirection
### 6.1 Top
> $ top -o %MEM   

result is sorted based on the memory used: 
![This is an image](./top.png)

### 6.2 Kill firefox
Find the PID of the firefox and kill that program:
> $ sudo kill $(ps aux | grep firefox | awk '{print $2}')  

### 6.3 output and error stream
Write output and standard error in out.txt:
> $ cat /proc/devices >>out.txt 2>&1 

append cpu info:
> $ cat /proc/cpuinfo >>out.txt 2>&1

### 6.4 ping and run command in background
To run command in background use & at the end of the command:
> $ ping ee.sharif.ir > log.text &

To bring a background process to the foreground use command fg:
> $ fg

To see result of the command: 
> $ cat log.txt

To end terminate process kill the process 
> $ kill 5374                 </br>
[1]  + terminated  ping ee.sharif.ir > log.text

### 6.5 tmux
tmux is a terminal multiplexer and used for open multiple terminal windows in single window, which each of these terminals are running independently. 

To create a new session: 
> $ tmux new -s First-session

to create new session or window:
> $ ctrl + b + %

to shift between 2 windows:
> $ ctrl + b + ->/<-

which ->/<- is the arrow

Create a new window at the bottom:
> $ ctrl + b + " 
 
To exit a session write:
> $ exit

## 7 Text editor
### 7.1 Vim
To create a file with my student number name:
> $ vim 97102558

To set ‫‪Line‬‬ ‫‪Numbering‬‬ or ‫‪Smart‬‬ ‫Indentation ‬ press Esc then : and type:
> : set autoindent </br>
> : set number

### 7.2 Reapting 5.3

First we should open the specified file with the vim:
> $ sudo vim GPL-1

Then press Esc and then : and type this: 
> $ /^[^#]*GNU

The first ^ will anchor the match to the start of the line, [^#] will match any character except a # (the ^ means to match any character except those given), and the * repeats this 0 or more times. [refrence](https://vi.stackexchange.com/questions/3347/search-for-lines-starting-with-given-string-in-vim)

This will find the lines starting with GNU.

To search word contain "cept":
Press Esc and then : and type this: 
> /cept


To find text between () use this:
> /(. *)

### 7.3 sort

Select the lines that before "Genral Setup" and the press : and wirte: 
> :'<,'>sort	

To save the text use :wq

### 7.4 ‫‪Record‬‬ ‫‪and‬‬ ‫‪Play‬‬
Use this [link](https://spin.atomicobject.com/2014/11/23/record-vim-macros/) to see how Macros work and with that we can Record and play same instructions on multiple files:

‫‪:g/(normal‬‬ ‫(‪f(dvariable‬‬ ‫‬‬</br>
‫‪:%s/GNU/SUT‬‬ </br>
‫‪:%s/**19/**13‬‬
