#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Alegi cui mortii tai sa ii schimbi MAC-ul")
    parser.add_option("-m", "--mac", dest="new_mac", help="Alegi ce mortii tai MAC sa ii pui")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Ai uitat sa bagi interfata, boule (--help)")
    elif not options.new_mac:
        parser.error("[-] Ai uitat sa bagi MAC-ul nou, boule (--help)")
    return options

def change_mac(interface, new_mac):
    print("[!] Ii schimb MAC-ul Domnului " + interface + " in " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("")
    print("[+] Gata cumetre")


def aratanou(interface):
    nou = subprocess.check_output(["ifconfig", interface])

    mac_rezultat = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", nou)

    if mac_rezultat:
        return mac_rezultat.group(0)
    else:
        print("[-] Aceasta interfata nu are o adresa MAC")

options = get_arguments()
change_mac(options.interface, options.new_mac)

macunou = aratanou(options.interface)

macunou = aratanou(options.interface)
if macunou == options.new_mac:
    print("[+] Noua adresa MAC este: " + str(macunou) + " - " + options.interface)
else:
    print("[-] Adresa MAC nu a fost schimbata")

