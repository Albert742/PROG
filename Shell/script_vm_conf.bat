@echo off

VBoxManage startvm "A" --type gui
VBoxManage startvm "B" --type gui
VBoxManage startvm "C" --type gui
VBoxManage startvm "D" --type gui
VBoxManage startvm "E" --type gui
VBoxManage startvm "F" --type gui
VBoxManage startvm "G" --type gui
VBoxManage startvm "Z" --type gui
VBoxManage startvm "R4" --type gui
VBoxManage startvm "R3" --type gui
VBoxManage startvm "R2" --type gui
VBoxManage startvm "R1" --type gui

timeout /t 10 /nobreak > nul

rem Configurazione nodo A
echo Configurazione nodo A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /usr/bin/hostname -- A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.1.2/24 dev enp0s3 
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.1.1

rem Configurazione nodo B
echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.1.3/24 dev enp0s3 
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.1.1

rem Configurazione nodo C
echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.3.2/24 dev enp0s3 
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.3.1

rem Configurazione nodo D
echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.2.2/24 dev enp0s3 
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.2.1

rem Configurazione nodo E
echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.4.2/24 dev enp0s3 
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.4.1

rem Configurazione nodo F
echo Configurazione nodo F
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /usr/bin/hostname -- F
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.5.2/24 dev enp0s3 
VBoxManage guestcontrol F run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.5.1

rem Configurazione nodo G
echo Configurazione nodo G
VBoxManage guestcontrol G run --username root --password root --wait-stdout --exe /usr/bin/hostname -- G
VBoxManage guestcontrol G run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.6.3/24 dev enp0s3 
VBoxManage guestcontrol G run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.6.1

rem Configurazione nodo Z
echo Configurazione nodo Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s3 
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.0.0/20 via 2.2.2.2

rem Configurazione router R4
echo Configurazione router R4
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R4
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up 
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.1.1/24 dev enp0s3
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.2.1/24 dev enp0s8 
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.6.2/24 dev enp0s9
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.7.1/24 dev enp0s10
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R4 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.7.2

rem Configurazione router R3
echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up 
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.3.1/24 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.4.1/24 dev enp0s8 
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.6.1/24 dev enp0s9
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.8.1/24 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.8.2

rem Configurazione router R2
echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up 
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.5.1/24 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.7.2/24 dev enp0s8 
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.8.2/24 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.9.1/24 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.1.0/24 via 1.1.7.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.2.0/24 via 1.1.7.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.3.0/24 via 1.1.8.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.4.0/24 via 1.1.8.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.6.0/24 via 1.1.8.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 1.1.9.2

rem Configurazione router R1
echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up 
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 1.1.9.2/24 dev enp0s3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s8 
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1 
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 1.1.0.0/20 via 1.1.9.1

echo Test ping A -> Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Script completo
pause