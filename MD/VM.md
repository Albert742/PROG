# Comandi Bash

##

### Nodo A

```bash
ip addr add 145.18.8.78/28 dev enp0s3
ip route add default via 145.18.8.65
```

### Nodo B

```bash
ip addr add 145.18.8.30/27 dev enp0s3
ip route add default via 145.18.8.1
```

### Nodo C

```bash
ip addr add 145.18.8.94/29 dev enp0s3
ip route add default via 145.18.8.89
```

### Nodo D

```bash
ip addr add 145.18.8.62/27 dev enp0s3
ip route add default via 145.18.8.33
```

### Nodo E

```bash
ip addr add 145.18.8.86/29 dev enp0s3
ip route add default via 145.18.8.81
```

### Nodo Z

```bash
ip addr add 2.2.2.1/30 dev enp0s3
ip route add 145.18.8.0/25 via 2.2.2.2
```

### Router R1

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip link set enp0s10 up
ip addr add 10.0.13.0/31 dev enp0s3
ip addr add 145.18.8.65/28 dev enp0s8
ip addr add 145.18.8.1/27 dev enp0s9
ip addr add 10.0.1.1/31 dev enp0s10
sysctl -w net.ipv4.ip_forward=1
ip route add 145.18.8.88/29 via 10.0.13.1 dev enp0s3
ip route add 145.18.8.32/27 via 10.0.13.1 dev enp0s3
ip route add 145.18.8.80/29 via 10.0.13.1 dev enp0s3
ip route add default via 10.0.1.0
```

### Router R2

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip addr add 10.0.2.1/31 dev enp0s3
ip addr add 145.18.8.81/29 dev enp0s8
ip addr add 10.0.23.0/31 dev enp0s9
sysctl -w net.ipv4.ip_forward=1
ip route add 145.18.8.88/29 via 10.0.23.1 dev enp0s9
ip route add 145.18.8.32/27 via 10.0.23.1 dev enp0s9
ip route add 145.18.8.0/27 via 10.0.23.1 dev enp0s9
ip route add 145.18.8.64/28 via 10.0.23.1 dev enp0s9
ip route add default via 10.0.2.0
```

### Router R3

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip link set enp0s10 up
ip addr add 10.0.23.1/31 dev enp0s3
ip addr add 145.18.8.33/27 dev enp0s8
ip addr add 145.18.8.89/29 dev enp0s9
ip addr add 10.0.13.1/31 dev enp0s10
sysctl -w net.ipv4.ip_forward=1
ip route add 145.18.8.0/27 via 10.0.13.0 dev enp0s10
ip route add 145.18.8.64/28 via 10.0.13.0 dev enp0s10
ip route add 145.18.8.80/29 via 10.0.23.0 dev enp0s3
ip route add default via 10.0.23.0
```

### Router ISP

```bash
ip link set enp0s8 up
ip link set enp0s9 up
ip addr add 10.0.1.0/31 dev enp0s3
ip addr add 10.0.2.0/31 dev enp0s8
ip addr add 2.2.2.2/30 dev enp0s9
sysctl -w net.ipv4.ip_forward=1
ip route add 145.18.8.0/25 via 10.0.1.1 dev enp0s3
```
