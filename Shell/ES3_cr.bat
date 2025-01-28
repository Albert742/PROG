@echo off

rem Elimina snapshot
VBoxManage snapshot debbie delete Snapshot

rem Crea snapshot
VBoxManage snapshot debbie take Snapshot

rem Clona e configura le macchine virtuali
VBoxManage clonevm debbie --snapshot Snapshot --name A --options link --register
VBoxManage modifyvm A --memory 256 --nic1 intnet --intnet1 lan2 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name B --options link --register
VBoxManage modifyvm B --memory 256 --nic1 intnet --intnet1 lan3 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name C --options link --register
VBoxManage modifyvm C --memory 256 --nic1 intnet --intnet1 lan4 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name D --options link --register
VBoxManage modifyvm D --memory 256 --nic1 intnet --intnet1 lan5 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name E --options link --register
VBoxManage modifyvm E --memory 256 --nic1 intnet --intnet1 lan6 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name F --options link --register
VBoxManage modifyvm F --memory 256 --nic1 intnet --intnet1 lan7 --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name Z --options link --register
VBoxManage modifyvm Z --memory 256 --nic1 intnet --intnet1 lanISP --nic2 none --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name ISP --options link --register
VBoxManage modifyvm ISP --memory 256 --nic1 intnet --intnet1 lan1 --nic2 intnet --intnet2 lanISP --nic3 none --nic4 none

VBoxManage clonevm debbie --snapshot Snapshot --name R1 --options link --register
VBoxManage modifyvm R1 --memory 256 --nic1 intnet --intnet1 lan1 --nic2 intnet --intnet2 lan3 --nic3 intnet --intnet3 lan1_2 --nic4 intnet --intnet4 lan2

VBoxManage clonevm debbie --snapshot Snapshot --name R2 --options link --register
VBoxManage modifyvm R2 --memory 256 --nic1 intnet --intnet1 lan1_2 --nic2 intnet --intnet2 lan4 --nic3 intnet --intnet3 lan5 --nic4 intnet --intnet4 lan2_3

VBoxManage clonevm debbie --snapshot Snapshot --name R3 --options link --register
VBoxManage modifyvm R3 --memory 256 --nic1 intnet --intnet1 lan2_3 --nic2 intnet --intnet2 lan7 --nic3 intnet --intnet3 lan6 --nic4 none

