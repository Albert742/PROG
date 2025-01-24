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

:: lan10
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.78/28 dev enp0s3 

VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.65

echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B

:: lan11
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.30/27 dev enp0s3 

VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.1

echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C

:: lan12
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.94/29 dev enp0s3 

VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.89

echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D

:: lan13
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.62/27 dev enp0s3 

VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.33

echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E

:: lan14
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.86/29 dev enp0s3 

VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.81

echo Configurazione nodo Z

VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z

:: lanISP
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s3 

VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 2.2.2.2

echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1

:: lan1_3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.101/30 dev enp0s3

:: lan10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.65/28 dev enp0s8

:: lan11
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.1/27 dev enp0s9

:: lanExt1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.109/30 dev enp0s10

:: lan1_2
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.97/30 dev enp0s16

VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s16 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.88/29 via 145.18.8.102 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.32/27 via 145.18.8.102 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.80/29 via 145.18.8.98 dev enp0s16
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 2.2.2.0/30 via 145.18.8.110 dev enp0s10

echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2

:: lanExt2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.113/30 dev enp0s3 

:: lan14
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.81/29 dev enp0s8 

:: lan2_3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.105/30 dev enp0s9 

:: lan1_2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.98/30 dev enp0s10 

VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/21 via 145.18.8.97 dev enp0s8
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.64/28 via 145.18.8.97 dev enp0s10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.88/29 via 145.18.8.106 dev enp0s9
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.32/27 via 145.18.8.106 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 2.2.2.0/30 via 145.18.8.114 dev enp0s3

echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3

:: lan2_3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.106/30 dev enp0s3 

:: lan13
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.33/27 dev enp0s8 

:: lan12
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.89/29 dev enp0s9 

:: lan1_3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.102/30 dev enp0s10 

VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/21 via 145.18.8.101 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.64/28 via 145.18.8.101 dev enp0s10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.80/29 via 145.18.8.105 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 2.2.2.0/30 via 145.18.8.105 dev enp0s3

echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP

:: lanExt1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.110/30 dev enp0s3 

:: lanExt2
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.114/30 dev enp0s8 

:: lanISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s9 

VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 145.18.8.109 dev enp0s3

echo Test ping R1 - R2 
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.98

echo Test ping R1 - R3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.102

echo Test ping R1 - ISP
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.110

echo Test ping R2 - R3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.106

echo Test ping A - D
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.62

echo Test ping A - B
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.30

echo Test ping A - C
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.94

echo Test ping A - E
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 145.18.8.86

echo Test ping A - Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Script completo

pause