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

timeout /t 30 /nobreak > nul

echo Configurazione nodo A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /usr/bin/hostname -- A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.78/28 dev enp0s3
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.65

echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.30/27 dev enp0s3
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.1

echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.86/29 dev enp0s3
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.81

echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.62/27 dev enp0s3
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.33

echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.94/29 dev enp0s3
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.89

echo Configurazione nodo Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s3
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 2.2.2.2

echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.13.1/30 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.65/28 dev enp0s8
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.1/27 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.1.2/30 dev enp0s10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.1/30 dev enp0s16
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s16 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.1.1

echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.2.2/30 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.89/29 dev enp0s8
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.1/30 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.2/30 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.2.1

echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.2/30 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.33/27 dev enp0s8
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.81/29 dev enp0s9
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.13.2/30 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.23.1

echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.1.1/30 dev enp0s3
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.2.1/30 dev enp0s8
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s9
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 10.0.1.2

echo Test ping A - Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Script completo

pause