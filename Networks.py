import socket
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import PhotoImage
import os

def classify_network(ip):
    parts = ip.split(".")
    try:
        first_octet = int(parts[0])
    except (ValueError, IndexError):
        return "Error: Invalid IP address."

    if 1 <= first_octet <= 126:
        return "Class A: It's a large network"
    elif 128 <= first_octet <= 191:
        return "Class B: It's a medium-sized network"
    elif 192 <= first_octet <= 223:
        return "Class C: It's a small network"
    elif 224 <= first_octet <= 239:
        return "Class D: For Multicast (not for hosts)"
    elif 240 <= first_octet <= 254:
        return "Class E: Experimental / Reserved"
    else:
        return "Unknown or reserved class"

def get_real_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "Could not retrieve IP"
    finally:
        s.close()
    return ip

def local_option():
    hostname = socket.gethostname()
    ip_address = get_real_ip()
    network_class = classify_network(ip_address)
    messagebox.showinfo("My IP", f"Device name: {hostname}\nIP Address: {ip_address}\n{network_class}")

def external_option():
    ip_address = simpledialog.askstring("External IP", "Enter the IP you want to classify:")
    if ip_address:
        network_class = classify_network(ip_address)
        messagebox.showinfo("Classification", f"The IP {ip_address} belongs to:\n{network_class}")

def center_window(window, width, height):
    window.update_idletasks()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)

# Absolute path to the icon file
base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, "logo.png")

# Main window
root = tk.Tk()
root.title("Network Classifier")
icon = PhotoImage(file=icon_path)
root.iconphoto(False, icon)
center_window(root, 300, 150)

label = tk.Label(root, text="What do you want to know?", font=("Arial", 12))
label.pack(pady=10)

btn1 = tk.Button(root, text="Find out my network class", command=local_option)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Classify an external IP", command=external_option)
btn2.pack(pady=5)

root.mainloop()