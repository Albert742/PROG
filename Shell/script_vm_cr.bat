@echo off
rem Elimina snapshot
VBoxManage snapshot debbie delete Snapshot

rem Crea snapshot
VBoxManage snapshot debbie take Snapshot

rem Clona e configura le macchine virtuali
VBoxManage clonevm debbie --snapshot Snapshot --name A --options link --register
VBoxManage modifyvm A --memory 256 --nic1 intnet --intnet1 lan01 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name B --options link --register
VBoxManage modifyvm B --memory 256 --nic1 intnet --intnet1 lan01 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name C --options link --register
VBoxManage modifyvm C --memory 256 --nic1 intnet --intnet1 lan03 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name D --options link --register
VBoxManage modifyvm D --memory 256 --nic1 intnet --intnet1 lan02 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name E --options link --register
VBoxManage modifyvm E --memory 256 --nic1 intnet --intnet1 lan04 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name F --options link --register
VBoxManage modifyvm F --memory 256 --nic1 intnet --intnet1 lan05 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name G --options link --register
VBoxManage modifyvm G --memory 256 --nic1 intnet --intnet1 lan06 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name Z --options link --register
VBoxManage modifyvm Z --memory 256 --nic1 intnet --intnet1 lan10 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name R1 --options link --register
VBoxManage modifyvm R1 --memory 256 --nic1 intnet --intnet1 lan09 --nic2 intnet --intnet2 lan10 --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name R2 --options link --register
VBoxManage modifyvm R2 --memory 256 --nic1 intnet --intnet1 lan05 --nic2 intnet --intnet2 lan07 --nic3 intnet --intnet3 lan08 --nic4 intnet --intnet4 lan09 

VBoxManage clonevm debbie --snapshot Snapshot --name R3 --options link --register
VBoxManage modifyvm R3 --memory 256 --nic1 intnet --intnet1 lan03 --nic2 intnet --intnet2 lan04 --nic3 intnet --intnet3 lan06 --nic4 intnet --intnet4 lan08 

VBoxManage clonevm debbie --snapshot Snapshot --name R4 --options link --register
VBoxManage modifyvm R4 --memory 256 --nic1 intnet --intnet1 lan01 --nic2 intnet --intnet2 lan02 --nic3 intnet --intnet3 lan06 --nic4 intnet --intnet4 lan07 

rem Avvia le macchine virtuali
echo Avvio macchine virtuali
VBoxManage startvm A
VBoxManage startvm B
VBoxManage startvm C
VBoxManage startvm D
VBoxManage startvm E
VBoxManage startvm F
VBoxManage startvm G
VBoxManage startvm Z

VBoxManage startvm R1
VBoxManage startvm R2
VBoxManage startvm R3
VBoxManage startvm R4