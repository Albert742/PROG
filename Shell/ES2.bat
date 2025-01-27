@echo off

VBoxManage startvm "A" 
VBoxManage startvm "B" 
VBoxManage startvm "C" 
VBoxManage startvm "D" 
VBoxManage startvm "E" 
VBoxManage startvm "Z" 
VBoxManage startvm "R3" 
VBoxManage startvm "R2" 
VBoxManage startvm "R1" 
VBoxManage startvm "ISP" 

timeout /t 15 /nobreak > nul

echo Configurazione nodo A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /usr/bin/hostname -- A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.14.254/24 dev enp0s3
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.14.1

echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.11.254/22 dev enp0s3
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.1

echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.13.254/23 dev enp0s3
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.12.1

echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.14/28 dev enp0s3
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.15.1

echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.22/29 dev enp0s3
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.15.17

echo Configurazione nodo Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s3
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/21 via 2.2.2.2

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
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.26/30 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.37/30 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.14.1/24 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.1/22 dev enp0s10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.12.0/23 via 145.18.15.38 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.15.0/28 via 145.18.15.38 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.15.16/29 via 145.18.15.38 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.15.25

echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.30/30 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.17/29 dev enp0s8
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.33/30 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.15.0/28 via 145.18.15.34 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.12.0/23 via 145.18.15.34 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.14.0/24 via 145.18.15.34 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/28 via 145.18.15.34 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.15.29

echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.34/30 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.1/28 dev enp0s8
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.12.1/23 dev enp0s9
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.38/30 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.14.0/24 via 145.18.15.37 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/22 via 145.18.15.37 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.15.16/29 via 145.18.15.33 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.15.33

echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.25/30 dev enp0s3
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.15.29/30 dev enp0s8
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s9
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/21 via 145.18.15.26 dev enp0s3

echo Test connettività nodo A verso Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Test connettività nodo B verso Z
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Test connettività nodo C verso Z
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Test connettività nodo D verso Z
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Test connettività nodo E verso Z
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Test connettività nodo A verso nodo B
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.11.254

echo Test connettività nodo A verso nodo C
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.13.254

echo Test connettività nodo A verso nodo D
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.14

echo Test connettività nodo A verso nodo E
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.22

echo Test connettività nodo B verso nodo C
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.13.254

echo Test connettività nodo B verso nodo D
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.14

echo Test connettività nodo B verso nodo E
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.22

echo Test connettività nodo C verso nodo D
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.14

echo Test connettività nodo C verso nodo E
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.22

echo Test connettività nodo D verso nodo E
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.15.22

echo Script completo
pause

