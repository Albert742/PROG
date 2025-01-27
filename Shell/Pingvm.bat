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