@echo off

VBoxManage startvm "A" --type gui
VBoxManage startvm "B" --type gui
VBoxManage startvm "C" --type gui
VBoxManage startvm "D" --type gui
VBoxManage startvm "E" --type gui
VBoxManage startvm "Z" --type gui
VBoxManage startvm "R3" --type gui
VBoxManage startvm "R2" --type gui
VBoxManage startvm "R1" --type gui
VBoxManage startvm "ISP" --type gui

timeout /t 30 /nobreak > nul

rem Configurazione nodo A
echo Configurazione nodo A
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /usr/bin/hostname -- A
rem lan10
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.78/28 dev enp0s3
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.65

rem Configurazione nodo B
echo Configurazione nodo B
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /usr/bin/hostname -- B
rem lan11
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.30/27 dev enp0s3
VBoxManage guestcontrol B run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.1

rem Configurazione nodo C
echo Configurazione nodo C
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /usr/bin/hostname -- C
rem lan12
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.86/29 dev enp0s3
VBoxManage guestcontrol C run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.81

rem Configurazione nodo D
echo Configurazione nodo D
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /usr/bin/hostname -- D
rem lan13
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.62/27 dev enp0s3
VBoxManage guestcontrol D run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.33

rem Configurazione nodo E
echo Configurazione nodo E
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /usr/bin/hostname -- E
rem lan14
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.94/29 dev enp0s3
VBoxManage guestcontrol E run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 145.18.8.89

rem Configurazione nodo Z
echo Configurazione nodo Z
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /usr/bin/hostname -- Z
rem lanISP
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s3
VBoxManage guestcontrol Z run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 2.2.2.2

rem Configurazione router R1
echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1
rem lan1_3
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.13.0/31 dev enp0s3
rem lan10
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.65/28 dev enp0s8
rem lan11
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.1/27 dev enp0s9
rem lanExt1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.1.1/31 dev enp0s10
rem lan1_2
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.0/31 dev enp0s16
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s16 up
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 10.0.13.1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 10.0.23.0/31 via 10.0.12.1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.1.0

rem Configurazione router R2
echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
rem lanExt2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.2.1/31 dev enp0s3
rem lan14
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.89/29 dev enp0s8
rem lan2_3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.0/31 dev enp0s9
rem lan1_2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.1/31 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 10.0.23.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 10.0.13.0/31 via 10.0.23.1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.2.0

rem Configurazione router R3
echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
rem lan2_3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.1/31 dev enp0s3
rem lan13
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.33/27 dev enp0s8
rem lan12
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 145.18.8.81/29 dev enp0s9
rem lan1_3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.13.1/31 dev enp0s10
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s10 up
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 10.0.23.0
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 10.0.12.0/31 via 10.0.23.0
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.13.0

rem Configurazione router ISP
echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP
rem lanExt1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.1.0/31 dev enp0s3
rem lanExt2
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.2.0/31 dev enp0s8
rem lanISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.2/30 dev enp0s9
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s9 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 145.18.8.0/25 via 10.0.2.1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 2.2.2.1

echo Test ping A -> Z
VBoxManage guestcontrol A run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 2.2.2.1

echo Spegnimento macchine virtuali
VBoxManage controlvm "A" acpipowerbutton
VBoxManage controlvm "B" acpipowerbutton
VBoxManage controlvm "C" acpipowerbutton
VBoxManage controlvm "D" acpipowerbutton
VBoxManage controlvm "E" acpipowerbutton
VBoxManage controlvm "Z" acpipowerbutton
VBoxManage controlvm "R3" acpipowerbutton
VBoxManage controlvm "R2" acpipowerbutton
VBoxManage controlvm "R1" acpipowerbutton
VBoxManage controlvm "ISP" acpipowerbutton

echo Script completo

pause