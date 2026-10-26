import ipaddress


def analyze_network():
    print("\n===== NETWORK ANALYZER =====")
    text = input("Nhap dia chi IP/CIDR (vd 192.168.1.10/24): ").strip()

    try:
        iface = ipaddress.ip_interface(text)
        net = iface.network

        print("\n--- KET QUA PHAN TICH ---")
        print(f"Dia chi IP: {iface.ip}")
        print(f"Phien ban: IPv{net.version}")
        print(f"Dia chi mang: {net.network_address}")
        print(f"Prefix: /{net.prefixlen}")
        print(f"Subnet mask: {net.netmask}")

        if net.version == 4:
            print(f"Broadcast: {net.broadcast_address}")

        print(f"Tong so dia chi: {net.num_addresses}")

        hosts = list(net.hosts()) if net.num_addresses <= 65536 else None
        if hosts:
            print(f"Host dau tien: {hosts[0]}")
            print(f"Host cuoi cung: {hosts[-1]}")
            print(f"So host kha dung: {len(hosts)}")

        if iface.ip.is_loopback:
            print("Loai IP: Loopback")
        elif iface.ip.is_private:
            print("Loai IP: Private")
        elif iface.ip.is_global:
            print("Loai IP: Global")
        else:
            print("Loai IP: Dia chi dac biet")

    except ValueError:
        print("Loi: Dia chi khong hop le!")


while True:
    analyze_network()
    again = input("\nBan co muon kiem tra tiep? (y/n): ").strip().lower()
    if again != "y":
        print("Ket thuc chuong trinh.")
        break