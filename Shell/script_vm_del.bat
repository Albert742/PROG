@echo off
echo Eliminazione macchine virtuali
VBoxManage unregistervm "A" --delete
VBoxManage unregistervm "B" --delete
VBoxManage unregistervm "C" --delete
VBoxManage unregistervm "D" --delete
VBoxManage unregistervm "E" --delete
VBoxManage unregistervm "F" --delete
VBoxManage unregistervm "Z" --delete
VBoxManage unregistervm "ISP" --delete
VBoxManage unregistervm "R1" --delete
VBoxManage unregistervm "R2" --delete
VBoxManage unregistervm "R3" --delete