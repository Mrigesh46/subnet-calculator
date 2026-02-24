import ipaddress

def get_default_cidr(ip):
    first_octet = int(str(ip).split('.')[0])

    if 1 <= first_octet <= 126:
        return 8     # Class A
    elif 128 <= first_octet <= 191:
        return 16    # Class B
    elif 192 <= first_octet <= 223:
        return 24    # Class C
    else:
        return None  # Invalid / unsupported

def subnet_calculator():
    print("=== Classful Subnet Calculator ===")

    ip_input = input("Enter IP Address : ")

    try:
        ip_obj = ipaddress.ip_address(ip_input)
        cidr = get_default_cidr(ip_obj)

        if cidr is None:
            print(" Unsupported or invalid IP range")
            return

        network = ipaddress.ip_network(f"{ip_input}/{cidr}", strict=False)

        print("\n----- Calculated Results -----")
        print("IP Address:", ip_input)
        print("Detected Class CIDR: /" + str(cidr))
        print("Subnet Mask:", network.netmask)
        print("Network Address:", network.network_address)
        print("Broadcast Address:", network.broadcast_address)

        hosts = list(network.hosts())

        print("First Usable Host:", hosts[0])
        print("Last Usable Host:", hosts[-1])
        print("Total IPs:", network.num_addresses)
        print("Usable Hosts:", network.num_addresses - 2)

        # Binary format
        binary_ip = '.'.join([bin(int(x))[2:].zfill(8) for x in ip_input.split('.')])
        print("\nBinary Representation:", binary_ip)

    except ValueError:
        print(" Invalid IP Address")

if __name__ == "__main__":
    subnet_calculator()