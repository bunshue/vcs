@echo off
echo ���� �s�@ �N�� BOOT.bin 
echo 1. ���� BOOT.bin
C:
cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
del /f /s /q BOOT.bin
echo 1. ���� BOOT.bin �����I

echo 2. �s�@ BOOT.bin
cmd /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin
echo 2. �s�@ BOOT.bin �����I


echo 3. �N�� BOOT.bin
cmd /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121
echo 3. �N�� BOOT.bin �����I

C:
cd C:\_git\vcs\_4.cmpp\_batch

