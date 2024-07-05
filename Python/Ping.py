import subprocess

def ping(host):
    result = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def ping_range(subnet, start, end, subnet2=None, start2=0, end2=0):
    active_hosts = []
    for i in range(start, end + 1):
        ip = f"{subnet}.{i}"
        if ping(ip):
            active_hosts.append(ip)
            print(f"{ip} is up")
        else:
            print(f"{ip} is down")
    if subnet2:
        for j in range(start2, end2 + 1):
            ip = f"{subnet2}.{j}"
            if ping(ip):
                active_hosts.append(ip)
                print(f"{ip} is up")
            else:
                print(f"{ip} is down")
    return active_hosts

# Example usage:
subnet = '192.168.100'
start_ip = 1
end_ip = 254

subnet2 = '192.168.101'
start_ip2 = 1
end_ip2 = 46

active_hosts = ping_range(subnet, start_ip, end_ip, subnet2, start_ip2, end_ip2)
print("Active hosts:", active_hosts)
