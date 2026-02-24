import ipaddress
import tkinter as tk
from tkinter import messagebox

def get_default_cidr(ip):
    first_octet = int(str(ip).split('.')[0])

    if 1 <= first_octet <= 126:
        return 8
    elif 128 <= first_octet <= 191:
        return 16
    elif 192 <= first_octet <= 223:
        return 24
    else:
        return None

def calculate():
    ip_input = entry.get()

    try:
        ip_obj = ipaddress.ip_address(ip_input)
        cidr = get_default_cidr(ip_obj)

        if cidr is None:
            messagebox.showerror("Error", "Unsupported IP range")
            return

        network = ipaddress.ip_network(f"{ip_input}/{cidr}", strict=False)
        hosts = list(network.hosts())

        result = f"""
Class CIDR: /{cidr}
Subnet Mask: {network.netmask}
Network Address: {network.network_address}
Broadcast Address: {network.broadcast_address}
First Host: {hosts[0]}
Last Host: {hosts[-1]}
Total Hosts: {network.num_addresses}
Usable Hosts: {network.num_addresses - 2}
"""
        output_label.config(text=result)

    except:
        messagebox.showerror("Error", "Invalid IP Address")

# GUI
root = tk.Tk()
root.title("Classful Subnet Calculator")

tk.Label(root, text="Enter IP Address").pack()
entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

output_label = tk.Label(root, text="", justify="left")
output_label.pack()

root.mainloop()