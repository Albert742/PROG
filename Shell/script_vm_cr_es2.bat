@echo off

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

rem Elimina le macchine virtuali esistenti
VBoxManage unregistervm "A" --delete
VBoxManage unregistervm "B" --delete
VBoxManage unregistervm "C" --delete
VBoxManage unregistervm "D" --delete
VBoxManage unregistervm "E" --delete
VBoxManage unregistervm "Z" --delete
VBoxManage unregistervm "ISP" --delete
VBoxManage unregistervm "R1" --delete
VBoxManage unregistervm "R2" --delete
VBoxManage unregistervm "R3" --delete

rem Elimina snapshot
VBoxManage snapshot debbie delete Snapshot

rem Crea snapshot
VBoxManage snapshot debbie take Snapshot

rem Clona e configura le macchine virtuali
VBoxManage clonevm debbie --snapshot Snapshot --name A --options link --register
VBoxManage modifyvm A --memory 256 --nic1 intnet --intnet1 lan10 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name B --options link --register
VBoxManage modifyvm B --memory 256 --nic1 intnet --intnet1 lan11 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name C --options link --register
VBoxManage modifyvm C --memory 256 --nic1 intnet --intnet1 lan12 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name D --options link --register
VBoxManage modifyvm D --memory 256 --nic1 intnet --intnet1 lan13 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name E --options link --register
VBoxManage modifyvm E --memory 256 --nic1 intnet --intnet1 lan14 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name Z --options link --register
VBoxManage modifyvm Z --memory 256 --nic1 intnet --intnet1 lanISP --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name ISP --options link --register
VBoxManage modifyvm ISP --memory 256 --nic1 intnet --intnet1 lanExt1 --nic2 intnet --intnet2 lanExt2 --nic3 intnet --intnet3 lanISP --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name R1 --options link --register
VBoxManage modifyvm R1 --memory 256 --nic1 intnet --intnet1 lan1_3 --nic2 intnet --intnet2 lan10 --nic3 intnet --intnet3 lan11 --nic4 intnet --intnet4 lanExt1 --nic5 intnet --intnet5 lan1_2 

VBoxManage clonevm debbie --snapshot Snapshot --name R2 --options link --register
VBoxManage modifyvm R2 --memory 256 --nic1 intnet --intnet1 lanExt2 --nic2 intnet --intnet2 lan14 --nic3 intnet --intnet3 lan2_3 --nic4 intnet --intnet4 lan1_2

VBoxManage clonevm debbie --snapshot Snapshot --name R3 --options link --register
VBoxManage modifyvm R3 --memory 256 --nic1 intnet --intnet1 lan2_3 --nic2 intnet --intnet2 lan13 --nic3 intnet --intnet3 lan12 --nic4 intnet --intnet4 lan1_3 
