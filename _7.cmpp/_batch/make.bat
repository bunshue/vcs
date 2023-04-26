@echo off
echo 移除 製作 燒錄 BOOT.bin 
echo 1. 移除 BOOT.bin
C:
cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
del /f /s /q BOOT.bin
echo 1. 移除 BOOT.bin 完成！

echo 2. 製作 BOOT.bin
cmd /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin
echo 2. 製作 BOOT.bin 完成！


echo 3. 燒錄 BOOT.bin
cmd /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121
echo 3. 燒錄 BOOT.bin 完成！

C:
cd C:\_git\vcs\_4.cmpp\_batch

