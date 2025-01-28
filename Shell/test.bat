@echo off

set VM_LIST=A B C D E F Z R3 R2 R1 ISP

for %%V in (%VM_LIST%) do (
    VBoxManage startvm "%%V"
)

timeout /t 15 /nobreak > nul

set VM_CONFIGS=(
    "A 15.4.75.254/23 15.4.74.1"
    "B 15.4.76.254/24 15.4.76.1"
    "C 15.4.78.94/27 15.4.78.65"
    "D 15.4.77.254/24 15.4.77.1"
    "E 15.4.73.254/23 15.4.72.1"
    "F 15.4.78.62/26 15.4.78.1"
    "Z 2.2.2.2/30 2.2.2.1"
)

for %%C in (%VM_CONFIGS%) do (
    for /f "tokens=1,2,3" %%a in ("%%C") do (
        echo Configurazione nodo %%a
        VBoxManage guestcontrol %%a run --username root --password root --wait-stdout --exe /usr/bin/hostname -- %%a
        VBoxManage guestcontrol %%a run --username root --password root --wait-stdout --exe /sbin/ip -- addr add %%b dev enp0s3
        VBoxManage guestcontrol %%a run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via %%c
    )
)

REM Configurazione router R1
echo Configurazione router R1
VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R1
for /l %%i in (8,1,10) do (
    VBoxManage guestcontrol R1 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s%%i up
)
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

REM Configurazione router R2
echo Configurazione router R2
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R2
for /l %%i in (8,1,10) do (
    VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s%%i up
)
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.12.1/31 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.77.1/24 dev enp0s8
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.65/27 dev enp0s9
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.0/31 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/23 via 10.0.12.0 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/24 via 10.0.12.0 dev enp0s3
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.72.0/23 via 10.0.23.1 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.0/26 via 10.0.23.1 dev enp0s10
VBoxManage guestcontrol R2 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.12.0

REM Configurazione router R3
echo Configurazione router R3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/bin/hostname -- R3
for /l %%i in (8,1,9) do (
    VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s%%i up
)
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 10.0.23.1/31 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.78.1/26 dev enp0s8
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.72.1/23 dev enp0s9
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.74.0/23 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.76.0/24 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.77.0/24 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.78.64/27 via 10.0.23.0 dev enp0s3
VBoxManage guestcontrol R3 run --username root --password root --wait-stdout --exe /sbin/ip -- route add default via 10.0.23.0

REM Configurazione router ISP
echo Configurazione router ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/bin/hostname -- ISP
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- link set enp0s8 up
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 15.4.64.1/21 dev enp0s3
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr add 2.2.2.1/30 dev enp0s8
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /usr/sbin/sysctl -- -w net.ipv4.ip_forward=1
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- addr
VBoxManage guestcontrol ISP run --username root --password root --wait-stdout --exe /sbin/ip -- route add 15.4.64.0/20 via 15.4.71.254 dev enp0s3

REM Test connettività
set TESTS=(
    "A 2.2.2.2"
    "B 2.2.2.2"
    "C 2.2.2.2"
    "D 2.2.2.2"
    "E 2.2.2.2"
    "A 15.4.76.254"
    "A 15.4.78.94"
    "A 15.4.77.254"
    "A 15.4.73.254"
    "B 15.4.78.94"
    "B 15.4.77.254"
    "B 15.4.73.254"
    "C 15.4.77.254"
    "C 15.4.73.254"
    "D 15.4.73.254"
)

for %%T in (%TESTS%) do (
    for /f "tokens=1,2" %%a in ("%%T") do (
        echo Test connettività nodo %%a verso %%b
        VBoxManage guestcontrol %%a run --username root --password root --wait-stdout --exe /bin/ping -- -c 4 %%b
    )
)

echo Script completo
pause