@echo off

VBoxManage startvm "A" 
VBoxManage startvm "B" 
VBoxManage startvm "C" 
VBoxManage startvm "D" 
VBoxManage startvm "E" 
VBoxManage startvm "F" 
VBoxManage startvm "Z" 
VBoxManage startvm "R3" 
VBoxManage startvm "R2" 
VBoxManage startvm "R1" 
VBoxManage startvm "ISP" 

timeout /t 15 /nobreak > nul

echo Configurazione nodo A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /usr/bin/hostname -- A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.75.254/23 dev enp0s3
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.74.1

echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.76.254/24 dev enp0s3
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.76.1

echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.94/27 dev enp0s3
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.78.65

echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.77.254/24 dev enp0s3
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.77.1

echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.73.254/23 dev enp0s3
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.72.1

echo Configurazione nodo F
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /usr/bin/hostname -- F
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.62/26 dev enp0s3
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.78.1

echo Configurazione nodo Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s3
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.64.0/20 via 2.2.2.1

echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.71.254/21 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.76.1/24 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.0/31 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.74.1/23 dev enp0s10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.77.0/24 via 10.0.12.1 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.64/27 via 10.0.12.1 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.72.0/23 via 10.0.12.1 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.0/24 via 10.0.12.1 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 15.4.64.1

echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.1/31 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.77.1/24 dev enp0s8
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.65/27 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.0/31 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/23 via 10.0.12.0 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/24 via 10.0.12.0 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.72.0/23 via 10.0.23.1 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.0/26 via 10.0.23.1 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.12.0

echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.1/31 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.1/26 dev enp0s8
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.72.1/23 dev enp0s9
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/23 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.76.0/24 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.77.0/24 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.64/27 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.23.0

echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.64.1/21 dev enp0s3
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s8
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.64.0/20 via 15.4.71.254 dev enp0s3

echo Test connettività nodo A verso Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.2

echo Test connettività nodo B verso Z
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.2

echo Test connettività nodo C verso Z
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.2

echo Test connettività nodo D verso Z
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.2

echo Test connettività nodo E verso Z
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.2

echo Test connettività nodo A verso nodo B
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.76.254

echo Test connettività nodo A verso nodo C
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.78.94

echo Test connettività nodo A verso nodo D
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.77.254

echo Test connettività nodo A verso nodo E
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.73.254

echo Test connettività nodo B verso nodo C
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.78.94

echo Test connettività nodo B verso nodo D
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.77.254

echo Test connettività nodo B verso nodo E
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.73.254

echo Test connettività nodo C verso nodo D
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.77.254

echo Test connettività nodo C verso nodo E
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.73.254

echo Test connettività nodo D verso nodo E
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 15.4.73.254

echo Script completo
pause

