@echo off
echo Spegnimento macchine virtuali
VBoxManage controlvm "A" acpipowerbutton
VBoxManage controlvm "B" acpipowerbutton
VBoxManage controlvm "C" acpipowerbutton
VBoxManage controlvm "D" acpipowerbutton
VBoxManage controlvm "E" acpipowerbutton
VBoxManage controlvm "F" acpipowerbutton
VBoxManage controlvm "Z" acpipowerbutton
VBoxManage controlvm "R3" acpipowerbutton
VBoxManage controlvm "R2" acpipowerbutton
VBoxManage controlvm "R1" acpipowerbutton
VBoxManage controlvm "ISP" acpipowerbutton