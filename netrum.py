
import argparse
from py._io.terminalwriter import SingleTable
from scapy.all import *
from huepy import *
import subprocess
from termcolor import colored
import netifaces
import socket
import datetime


class NotConnected(Exception):
    pass


class ZeroHosts(Exception):
    pass


def info(msg):
    return f"[*] {msg}"


def print_banner():
    print("")
    print(f"{bold(red('---'))} Active hosts enumeration tool {bold(red('---'))}")
    print("")


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--write', metavar="<file>",
                        dest="FILE", help="Save detected hosts in a file")
    parser.add_argument('-c', '--count', metavar="<int>", type=int, dest="COUNT",
                        default=40, help="Maximum amount of packets to capture (default: 40)")
    parser.add_argument('-t', '--timeout', dest="TIMEOUT", metavar="<int>",
                        default="3m", help="Maximum allowed scan time (default: 3 minutes)")
    parser.add_argument('-i', '--iface', dest="IFACE", metavar="<iface>", default="wlp3s0",
                        help="Local interface to use during discovery (default: wlp3s0)")
    parser.add_argument('-cl', '--clear', dest='CLEAR',
                        action='store_true', help="Clear screen before printing results")
    return parser.parse_args()


def get_mac(ip):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=10)
    for s, r in ans:
        return r.src


def main():
    res = arguments()
    hosts = {}
    now = datetime.datetime.now()
    mac_addrs = open("mac_addrs").readlines()
    time_shorts = {'s': 1, 'm': 60, 'h': 3600}
    if type(res.TIMEOUT) == int:
        timeout = int(res.TIMEOUT)
    else:
        timeout = int(res.TIMEOUT[0:-1])*time_shorts[res.TIMEOUT[-1]]
    my_ip = socket.gethostbyname(socket.gethostname())
    print(info("Started ARP scan..."))
    arp_packets = sniff(filter="arp and not host {}".format(my_ip),
                        count=res.COUNT, timeout=timeout)
    if len(arp_packets) == 0:
        raise ZeroHosts
    for pkt in arp_packets:
        hosts[pkt[ARP].psrc] = pkt[Ether].src if pkt[Ether].src != "ff:ff:ff:ff:ff:ff" else get_mac(
            pkt[ARP].psrc)
        hosts[pkt[ARP].pdst] = pkt[Ether].dst
        #hosts.append('{} {}'.format(pkt[ARP].psrc, pkt[Ether].src))
        #hosts.append('{} {}'.format(pkt[ARP].pdst, pkt[Ether].dst))
    table_data = [["-IP-", "-MAC-", "-VENDOR-"]]
    for host in hosts:
        ip = host
        mac = hosts[host]
        for mac_addr in mac_addrs:
            if mac_addr.split()[0] in mac.upper():
                vendor = ' '.join(mac_addr.split()[1::])
                break
            else:
                vendor = "N/A"
        if ip == netifaces.gateways()['default'][2][0]:
            gateway = "({})".format(red(bold("G")))
        else:
            gateway = ""
        table_data.append(["{} {}".format(ip, gateway), mac, vendor])
    table = SingleTable(table_data)
    p = subprocess.Popen(["iwconfig", res.IFACE], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode("utf-8")
    try:
        quality = re.search('Link Quality=(.*)/..', output).group(1)
        essid = re.search('ESSID:"(.*)"', output).group(1)
    except:
        raise NotConnected
    wifi_power = (int(quality[0])*4 * colored("=", "green")) + \
        ((7-int(quality[0]))*4 * colored("=", "white", attrs=["dark"]))
    if res.CLEAR:
        subprocess.call("clear", shell=True)
    print("")
    print(info("Wifi ESSID: {}".format(bold(essid))))
    print(info("Signal force: [{}]".format(wifi_power)))
    print(good("Discovered {} hosts".format(len(hosts))))
    print(table.table)
    if res.FILE:
        if res.FILE == ".":
            filename = "{}_{}_{}".format(essid, now.month, now.day)
        else:
            filename = res.FILE
        with open(filename, "w+") as res_file:
            res_file.write('\n'.join(ip for ip in hosts))
            res_file.close()
        print(info("Saved IP addresses to {}".format(bold(filename))))

    print(info("Scan finished ({}:{}:{})".format(now.hour, now.minute, now.second)))


if __name__ == "__main__":
    try:
        print_banner()
        main()
    except ZeroHosts:
        print(bad("No hosts found"))
    except NotConnected:
        print(bad("No wifi connection"))
