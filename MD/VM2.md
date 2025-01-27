# Comandi Bash

##

### Nodo A

```bash
ip addr add 145.18.14.254/24 dev enp0s3
lan10
ip route add default via 145.18.14.1
```

### Nodo B

```bash
ip addr add 145.18.11.254/22 dev enp0s3
lan11
ip route add default via 145.18.8.1
```

### Nodo C

```bash
ip addr add 145.18.13.254/23 dev enp0s3
lan12
ip route add default via 145.18.12.1
```

### Nodo D

```bash
ip addr add 145.18.15.14/28 dev enp0s3
lan13
ip route add default via 145.18.15.1
```

### Nodo E

```bash
ip addr add 145.18.15.22/29 dev enp0s3
lan14
ip route add default via 145.18.15.17
```

### Nodo Z

```bash
ip addr add 2.2.2.1/30 dev enp0s3
lanISP
ip route add 145.18.8.0/21 via 2.2.2.2
```

### Router R1

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip link set enp0s10 up
LanExt1
ip addr add 145.18.15.26/30 dev enp0s3
Lan1_3
ip addr add 145.18.15.37/30 dev enp0s8
Lan10
ip addr add 145.18.14.1/24 dev enp0s9
lan11
ip addr add 145.18.8.1/22 dev enp0s10
sysctl -w net.ipv4.ip_forward=1
lan12
ip route add 145.18.12.0/23 via 145.18.15.38 dev enp0s8
lan13
ip route add 145.18.15.0/28 via 145.18.15.38 dev enp0s8
lan14
ip route add 145.18.15.16/29 via 145.18.15.38 dev enp0s8
default
ip route add default via 145.18.15.25
```

### Router R2

```bash
ip link set enp0s8 up
ip link set enp0s9 up
lanExt2
ip addr add 145.18.15.30/30 dev enp0s3
lan14
ip addr add 145.18.15.17/29 dev enp0s8
lan2_3
ip addr add 145.18.15.33/30 dev enp0s9
sysctl -w net.ipv4.ip_forward=1
lan13
ip route add 145.18.15.0/28 via 145.18.15.34 dev enp0s9
lan12
ip route add 145.18.12.0/23 via 145.18.15.34 dev enp0s9
lan10
ip route add 145.18.14.0/24 via 145.18.15.34 dev enp0s9
lan11
ip route add 145.18.8.0/28 via 145.18.15.34 dev enp0s9
default
ip route add default via 145.18.15.29
```

### Router R3

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip link set enp0s10 up
lan2_3
ip addr add 145.18.15.34/30 dev enp0s3
lan13
ip addr add 1145.18.15.1/28 dev enp0s8
lan12
ip addr add 145.18.12.1/23 dev enp0s9
lan1_3
ip addr add 145.18.15.38/30 dev enp0s10
sysctl -w net.ipv4.ip_forward=1
lan10
ip route add 145.18.14.0/24 via 145.18.15.37 dev enp0s10
lan11
ip route add 145.18.8.0/22 via 145.18.15.37 dev enp0s10
lan14
ip route add 145.18.15.16/29 via 145.18.15.33 dev enp0s3
default
ip route add default via 145.18.15.33
```

### Router ISP

```bash
ip link set enp0s8 up
ip link set enp0s9 up
lanExt1
ip addr add 145.18.15.25/30 dev enp0s3
lanExt2
ip addr add 145.18.15.29/30 dev enp0s8
lanISP
ip addr add 2.2.2.2/30 dev enp0s9
sysctl -w net.ipv4.ip_forward=1
tutta la lan
ip route add 145.18.8.0/21 via 145.18.15.26 dev enp0s3
```
