# To the extent possible under law, the author(s) have dedicated all 
# copyright and related and neighboring rights to this software to the 
# public domain worldwide. This software is distributed without any warranty. 
# You should have received a copy of the CC0 Public Domain Dedication along 
# with this software. 
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 

# base-files version 4.2-4

# ~/.bashrc: executed by bash(1) for interactive shells.

# The latest version as installed by the Cygwin Setup program can
# always be found at /etc/defaults/etc/skel/.bashrc

# Modifying /etc/skel/.bashrc directly will prevent
# setup from updating it.

# The copy in your home directory (~/.bashrc) is yours, please
# feel free to customise it to create a shell
# environment to your liking.  If you feel a change
# would be benifitial to all, please feel free to send
# a patch to the cygwin mailing list.

# User dependent .bashrc file

# If not running interactively, don't do anything
[[ "$-" != *i* ]] && return

# Shell Options
#
# See man bash for more options...
#
# Don't wait for job termination notification
# set -o notify
#
# Don't use ^D to exit
# set -o ignoreeof
#
# Use case-insensitive filename globbing
# shopt -s nocaseglob
#
# Make bash append rather than overwrite the history on disk
# shopt -s histappend
#
# When changing directory small typos can be ignored by bash
# for example, cd /vr/lgo/apaache would find /var/log/apache
# shopt -s cdspell

# Completion options
#
# These completion tuning parameters change the default behavior of bash_completion:
#
# Define to access remotely checked-out files over passwordless ssh for CVS
# COMP_CVS_REMOTE=1
#
# Define to avoid stripping description in --option=description of './configure --help'
# COMP_CONFIGURE_HINTS=1
#
# Define to avoid flattening internal contents of tar files
# COMP_TAR_INTERNAL_PATHS=1
#
# Uncomment to turn on programmable completion enhancements.
# Any completions you add in ~/.bash_completion are sourced last.
# [[ -f /etc/bash_completion ]] && . /etc/bash_completion

# History Options
#
# Don't put duplicate lines in the history.
# export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups
#
# Ignore some controlling instructions
# HISTIGNORE is a colon-delimited list of patterns which should be excluded.
# The '&' is a special pattern which suppresses duplicate entries.
# export HISTIGNORE=$'[ \t]*:&:[fb]g:exit'
# export HISTIGNORE=$'[ \t]*:&:[fb]g:exit:ls' # Ignore the ls command as well
#
# Whenever displaying the prompt, write the previous line to disk
# export PROMPT_COMMAND="history -a"

# Aliases
#
# Some people use a different file for aliases
# if [ -f "${HOME}/.bash_aliases" ]; then
#   source "${HOME}/.bash_aliases"
# fi
#
# Some example alias instructions
# If these are enabled they will be used instead of any instructions
# they may mask.  For example, alias rm='rm -i' will mask the rm
# application.  To override the alias instruction use a \ before, ie
# \rm will call the real rm not the alias.
#
# Interactive operation...
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'
#
# Default to human readable figures
# alias df='df -h'
# alias du='du -h'
#
# Misc :)
# alias less='less -r'                          # raw control characters
# alias whence='type -a'                        # where, of a sort
# alias grep='grep --color'                     # show differences in colour
# alias egrep='egrep --color=auto'              # show differences in colour
# alias fgrep='fgrep --color=auto'              # show differences in colour
#
# Some shortcuts for different directory listings
# alias ls='ls -hF --color=tty'                 # classify files in colour
# alias dir='ls --color=auto --format=vertical'
# alias vdir='ls --color=auto --format=long'
# alias ll='ls -l'                              # long list
# alias la='ls -A'                              # all but . and ..
# alias l='ls -CF'                              #

# Umask
#
# /etc/profile sets 022, removing write perms to group + others.
# Set a more restrictive umask: i.e. no exec perms for others:
# umask 027
# Paranoid: neither group nor others have any perms:
# umask 077

# Functions
#
# Some people use a different file for functions
# if [ -f "${HOME}/.bash_functions" ]; then
#   source "${HOME}/.bash_functions"
# fi
#
# Some example functions:
#
# a) function settitle
# settitle () 
# { 
#   echo -ne "\e]2;$@\a\e]1;$@\a"; 
# }
# 
# b) function cd_func
# This function defines a 'cd' replacement function capable of keeping, 
# displaying and accessing history of visited directories, up to 10 entries.
# To use it, uncomment it, source this file and try 'cd --'.
# acd_func 1.0.5, 10-nov-2004
# Petar Marinov, http:/geocities.com/h2428, this is public domain
# cd_func ()
# {
#   local x2 the_new_dir adir index
#   local -i cnt
# 
#   if [[ $1 ==  "--" ]]; then
#     dirs -v
#     return 0
#   fi
# 
#   the_new_dir=$1
#   [[ -z $1 ]] && the_new_dir=$HOME
# 
#   if [[ ${the_new_dir:0:1} == '-' ]]; then
#     #
#     # Extract dir N from dirs
#     index=${the_new_dir:1}
#     [[ -z $index ]] && index=1
#     adir=$(dirs +$index)
#     [[ -z $adir ]] && return 1
#     the_new_dir=$adir
#   fi
# 
#   #
#   # '~' has to be substituted by ${HOME}
#   [[ ${the_new_dir:0:1} == '~' ]] && the_new_dir="${HOME}${the_new_dir:1}"
# 
#   #
#   # Now change to the new dir and add to the top of the stack
#   pushd "${the_new_dir}" > /dev/null
#   [[ $? -ne 0 ]] && return 1
#   the_new_dir=$(pwd)
# 
#   #
#   # Trim down everything beyond 11th entry
#   popd -n +11 2>/dev/null 1>/dev/null
# 
#   #
#   # Remove any other occurence of this dir, skipping the top of the stack
#   for ((cnt=1; cnt <= 10; cnt++)); do
#     x2=$(dirs +${cnt} 2>/dev/null)
#     [[ $? -ne 0 ]] && return 0
#     [[ ${x2:0:1} == '~' ]] && x2="${HOME}${x2:1}"
#     if [[ "${x2}" == "${the_new_dir}" ]]; then
#       popd -n +$cnt 2>/dev/null 1>/dev/null
#       cnt=cnt-1
#     fi
#   done
# 
#   return 0
# }
# 
# alias cd=cd_func
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias ls="ls $LS_OPTIONS"
alias tls="time ls $LS_OPTIONS"
alias l="ls    -alh |more"                   # List detailled.
#alias ll="ls   -alh |more"                  # List detailled.
alias ll="ls   -ltrh"                  # List detailled.
alias lll="ls  -alh |more"                  # List detailled.
alias llc="ls  -li /mnt/cdrom1/"
alias a="alias"
alias df="df -h"
alias files="find  $pwd -type f | wc -l"
alias fileno="find .    -type f | wc -l"
alias cd-="cd -"
alias cd..="cd .."
alias cd1="cd.."
alias cd2="cd ..\/..\/"
alias cd3="cd ..\/..\/..\/"
alias cd4="cd ..\/..\/..\/..\/"
alias cd5="cd ..\/..\/..\/..\/..\/"
#alias vi="vim"
#alias lsdir="find -maxdepth 1 -type d"
alias lsdir="ls -d */"
alias lsd="ls -altrh DvdPlayer;du -sh DvdPlayer"
alias lsh="ls -altrh *.h;du -sh *.h"
alias nn="clear;dvd"
alias sl="ls"
alias find.="find ."
alias ff="echo Useage of search pattern;echo  \"find . -name *.c | xargs grep patn\""

alias cpscsi_pc="cp drivers/scsi/*.ko /lib/modules/2.6.12-12mdkcustom/kernel/drivers/scsi/"
alias lsv="ls -al ./vmlinux.bin"
alias lsi="ls -al ./*.img"
alias lso="ls -altrh ./*.o"
alias lsko="ls -al ./*.ko"
alias lsv="ls -altrh ./vmlinux.bin"
alias lsi="ls -altrh ./*.img;du -sh ./*.img"
alias rmrfi="ls -altrh ./*.img;du -sh ./*.img;rm -rf install.img"
alias lsc="ls -altrh ./*.c"
alias lscpp="ls -altrh ./*.cpp"
alias lspl="ls -altrh ./*.pl"
alias scpuseage="echo;echo scp useage:;echo;echo scp filename david@172.21.15.130:/home/user;echo"
alias showscpuseage="echo;echo scp useage:;echo;echo scp filename david@172.21.15.130:/home/user;echo"
alias lst="ls -altrh ./*.txt"
alias lsz="ls -altrh ./*.zip"
alias lsj="ls -altrh ./*.JPG"
alias lsko="ls -altrh ./*.ko"
#alias ifc="echo ifconfig eth0 172.21.98.3 and nfs2;ifconfig eth0 172.21.98.3&&nfs2&&cd -"
alias ifc="dmesg;echo ifconfig eth0 172.21.98.3;ifconfig eth0 172.21.98.3"
alias 12="echo goto linux-2.16.12 \(mars casablanca\);cd /home/user/linux.casablanca/linux-2.6.12/fs/vcd"
alias 34="echo goto linux-2.16.34 \(saturn\);cd /home/user/linux-2.6.34/;pwd"
alias otg="echo goto otg code\(mars v2 casablanca 2011 0705\);cd /home/user/linux.mars.v2.casablanca.0705/linux.mars.v2.casablanca/linux-2.6.12/drivers/usb/gadget/"
alias restartnfs="cd /etc/init.d;./nfs-server restart;cd -"
#alias cplin='echo copy linux kernel to \/tftpboot\/;cp   ./vmlinux.bin            /tftpboot/'
alias cpptp="echo copy ptp module;cp ./fs/ptp/ptpfs.ko /home/user/"
alias cpotg="echo copy g_file_storage.ko;cp ./drivers/usb/gadget/g_file_storage.ko /home/user/"
alias cpfat="echo copy FAT file system module;cp  ./fs/vfat/vfat.ko ./fs/fat/fat.ko /home/user/"
alias cpvfat="echo copy FAT file system module;cp  ./fs/vfat/vfat.ko ./fs/fat/fat.ko /home/user/"
alias cpvcd="echo copy vcd module;cp   ./fs/vcd/vcd.ko          /home/user/"
alias cpiso="echo copy iso9660 module;cp   ./fs/isofs/isofs.ko      /home/user/"
alias cpudf="echo copy UDF module;cp   ./fs/udf/udf.ko  /home/user/"
alias cpide="echo copy ide module;cp   ./drivers/ide/ide-cd.ko  /home/user/"
alias cpcdrom="echo copy cdrom module;cp ./drivers/cdrom/cdrom.ko /home/user/"
alias cpusb="echo copy USB module;cp   ./drivers/usb/host/*.ko  /home/user/"
alias cplbd="echo copy linux kernel and modules for LBD;cplin;cp ./drivers/scsi/*.ko  /home/user/"
alias cpnormal="echo copy linux kernel and modules for normal;cplin;cp ./drivers/scsi/*.ko  /home/user/"
alias cpker="echo copy linux kernel and all kernel modules;cplin;cpvcd;cpptp;cpotg;cpfat;cpusb;cpiso;cpudf"
alias cpall="cpker"
alias makeall="echo Make the linux kernel and copy linux kernel and all kernel modules.;make;cpall"
alias lz="ls   -alh *.zip"
alias rmz="rm  -rfv *.zip"
alias see="od  -An  -tx1 -v"
alias seed="od -An  -tu1 -v"
alias ssss="rmmesg;echo shutdown -h now ;shutdown -h now"
alias rrrr_pc="rmmesg;reboot"
#alias reboot="echo STOP!!!;echo Do you really want to reboot the PC? type rrrr_pc"
#alias lion="ii  && mm && toc && uuu  && rmm"
#alias cat="mycat"
alias cm="cat /proc/meminfo"
alias dush="du -sh"
alias ii="insmod vcd.ko"
alias mountusb="echo mount usb flashdisk;mount -o iocharset=utf8 /dev/sdb1 /mnt/MY_FLASH/&& cd /mnt/MY_FLASH/;echo"
alias mm="mount  -t vcd /dev/hdc /mnt/cdrom1"
alias mmb="mount -t vcd /dev/hdc /mnt/cdrom1 -o browser"
alias mmd="mount -t vcd /dev/hdc /mnt/cdrom1 -o disc"
alias mmiso="mount -t iso9660 -o loop,ro /home/user/iso_image/baby.iso  /mnt/cdrom1/;cd /mnt/cdrom1/"
alias uuu="umount /dev/hdc"
alias uuuu="m|grep mmt;umount /mnt/partition* /mnt/removable*;m|grep mmt;"
alias mm1="mount -t vcd /dev/hdc /mnt/cdrom1"
alias rmm="rmmod vcd"
alias dn="dos2unix"
alias tk="tkdiff"
alias mp="mplayer"
alias p="echo;echo pwd - print name of current/working directory;echo;pwd;echo"
alias cpmsg="echo  copy messages to HD      && cp /var/log/messages /home/user/"
alias cpmsgh="echo copy messages to HD here && cp /var/log/messages ."
alias rmmesg="rm -rfv /var/log/messages"
alias mini="minicom -c on"
#alias nfs3="mount -t nfs -o nolock,tcp 172.21.98.14:/mnt/develop/david  /mnt/nfs3/;n3"
alias nfs3="mount -t nfs -o nolock,tcp 172.21.15.24:/mnt/SQA  /mnt/nfs3/;n3"
alias n2="cd      /mnt/nfs2"
alias n3="cd      /mnt/nfs3"
alias lin="cd     /home/user/linux.may.25/linux-2.6.12_normal/"
alias linv="cd    /home/user/linux.may.25/linux-2.6.12_normal/fs/vcd"
alias udf="cd     /home/user/linux.oct.08/linux-2.6.12/fs/udf"
alias ptp="cd     /home/user/linux.oct.08/linux-2.6.12/fs/ptp"
#alias lin="cd    /home/user/linux-2.6.12"
#alias linv="cd   /home/user/linux-2.6.12/fs/vcd"
alias cdrom="cd   /home/user/linux-2.6.12/drivers/cdrom/"
alias ide="cd     /home/user/linux-2.6.12/drivers/ide/"
alias base="cd    /home/user/linux-2.6.12/drivers/base/"
alias vicdrom="vi /home/user/linux-2.6.12/drivers/cdrom/cdrom.c"
alias viide="vi   /home/user/linux-2.6.12/drivers/ide/ide-cd.c"
alias rmrfotg="rm -rf ./drivers/usb/gadget/realtek/*.o ./drivers/usb/gadget/realtek/*.ko ./drivers/usb/gadget/*.o ./drivers/usb/gadget/*.ko;make;echo copy files OK;cp ./drivers/usb/gadget/*.ko /home/user/ ;cplin;"
alias makeotg="rm -rf ./drivers/usb/gadget/realtek/*.o ./drivers/usb/gadget/realtek/*.ko ./drivers/usb/gadget/*.o ./drivers/usb/gadget/*.ko;make;echo copy files OK;cp ./drivers/usb/gadget/*.ko /home/user/ ;cplin;"
alias makeo="rm -rf ./drivers/usb/gadget/realtek/*.o ./drivers/usb/gadget/realtek/*.ko ./drivers/usb/gadget/*.o ./drivers/usb/gadget/*.ko;make;echo copy files OK;cp ./drivers/usb/gadget/*.ko /home/user/ ;cplin;"
alias sourcecode="cd /usr/src/linux-2.6.12-12mdk/"
alias sc="cd         /usr/src/linux-2.6.12-12mdk/"
alias vcd="cd  /mnt/cdrom1"
alias vcd1="cd /mnt/cdrom1"
alias vcd2="cd /mnt/cdrom2"

/cygdrive/d/___source_code/_git/part3/vcs/_7.linux/_ctest_linux


alias diffcode="echo;echo Go to diff code area;cd /home/user/_diff_code;pwd;echo;"
alias ct="echo;echo Go to C test area;cd   /home/user/_ctest_linux;pwd;echo;"
alias ctok="echo;echo Go to C test OK area;cd /home/user/_ctest_linux/_ok_template;echo;pwd;echo"
alias mt="echo;echo Go to makefile test area;cd   /home/user/_ctest_linux/_Makefile_test;echo;pwd;echo"
alias pt="echo;echo Go to perl test area;cd   /home/user/_ctest_linux/_ptest;echo;pwd;echo"
alias st="echo;echo Go to shell test area;cd   /home/user/_ctest_linux/_stest;echo;pwd;echo"
alias gt="echo;echo Go to g test area;cd   /home/user/_ctest_linux/_gtest;echo;pwd;echo"
alias lt="echo;echo Go to linux test area;cd   /home/user/_ctest_linux/ltest;echo;pwd;echo"
alias dvd="echo;echo Go to cs6257 directory;cd  /cs6257;echo;pwd;echo;"
alias cs="echo;echo Go to cs6257 directory;cd  /cs6257;echo;pwd;echo;"
alias pa="echo;echo Go to PA63 directory;cd  /cs6257/SAMPO_PA_vincent_test;echo;pwd;echo;"
alias h25="echo;echo Go to H25_R3_Logic directory;cd  /cs6257/H25_R3_Logic;echo;pwd;echo;"

alias makeb="make&&./b"

alias tags="echo Making tags for vi......;ctags *.c *.h *.cpp"
alias visdd="echo;vi /home/user/myy/sdd"
alias vicc="echo;   echo vi alias;echo;vi   ~/.bashrc"
alias via="echo;    echo vi alias;echo;vi   ~/.bashrc"
alias vialias="echo;echo vi alias;echo;vi   ~/.bashrc"
alias src="echo;echo source .bashrc;source ~/.bashrc;echo"
alias rmrf="rm -rf"
alias rmrfo="echo remove *.o and *.ko;rm -rf *.o *.ko"
alias rmrfko="echo remove *.o and *.ko;rm -rf *.o *.ko"
alias run="echo;echo Compile stat_test.c;echo;gcc stat_test.c -o stat_test&&echo;echo Run stat_test;./stat_test&&echo;echo Run stat template.c;stat template.c"
alias rmrfall="rm -rfv *"
alias rmz="rm -rfv *.zip"
alias uu="unzip *.zip"
alias h="history"
alias hcp="history | grep cp"
alias cls="clear"
alias gp="gnuplot"
alias disp="display"
#alias clean="rmrf *.cdda *.mp3 *.MP3 *.jpg *.JPG messages a.out *.wav *.dat __dmesg* *.o *.mpg"
alias d="dmesg -s 999999999 | more"
alias dme="dmesg -s 999999999"
alias dmm="echo Save Dump Message to File __dmesg_tmp.o && dmesg -s 999999999 > __dmesg_tmp.o"
alias vid="vi __dmesg_tmp.o"
alias e="eject   /dev/hdc"
alias et="eject  /dev/hdc -t"
alias e1="eject  /dev/hdc"
alias e2="eject  /dev/hdd"
alias et1="eject /dev/hdc -t"
alias et2="eject /dev/hdd -t"
alias open="/home/user/_ctest_linux/common/my_open_tray"
alias close="/home/user/_ctest_linux/common/my_close_tray"
alias open1="/home/user/_ctest_linux/common/my_open_tray"
alias close1="/home/user/_ctest_linux/common/my_close_tray"
alias open2="/home/user/_ctest_linux/common/my_open_tray2"
alias close2="/home/user/_ctest_linux/common/my_close_tray2"
alias dm="dmesg"
alias dmc="dmesg -c && echo  && echo Dump-Message cleaned && echo "
alias cpr="cp -r"
#alias cp="cp  -r -v"
alias cp="cp  -r"
alias catn="cat -n"
alias grep="grep --color"
alias grepn="grep -n"
alias grepi="grep -i"
alias tcp="time cp -r -v"
alias m="mount"
alias makec="rm -rf COMPILE_TIME_*;echo;echo hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh;date>COMPILE_TIME_1;echo;make clean;make;date>COMPILE_TIME_2;cat COMPILE_TIME_1;cat COMPILE_TIME_2"
alias makem="echo;echo make menuconfig;echo;make menuconfig;echo"
alias maker="echo;echo make release;   echo;make release;   echo"
alias makel="echo;echo make link;      echo;make link;      echo"
alias 94="echo  Telnet to 172.21.98.94 \(SQA PC\), login as sqa;telnet    172.21.98.94"
alias 14="echo  Telnet to 172.21.98.14 \(Linux PC in Lab\), login as david;telnet    172.21.98.14"
alias lion="echo  Telnet to 192.168.2.79 \(Lion Ubuntu\), login as david/nnnn;ssh david@192.168.2.79"
alias 26="echo  Telnet to 172.21.15.26 \(Linux PC in Lab\), login as root/realtek09;ssh root@172.21.15.26"
alias 28="echo  Telnet to 172.21.15.28 \(QA PC\), login as root/realtek09;ssh root@172.21.15.28"
alias 38="echo  Telnet to 172.21.98.38 \(SA Linux PC\), login as root/realtek;ssh root@172.21.98.38"
alias demo="echo Telnet to 172.21.100.55\(Demo System\), login as root;telnet  172.21.100.55"
alias  emo="echo Telnet to 172.21.100.55\(Demo System\), login as root;telnet  172.21.100.55"
alias  meo="echo Telnet to 172.21.100.55\(Demo System\), login as root;telnet  172.21.100.55"
alias cats="cat    /home/user/myy/all_script.tv.server"
alias vis="vi      /home/user/myy/all_script.tv.server"
alias catmp="cat   /home/user/myy/tmp_data.c"
alias cattmp="cat  /home/user/myy/tmp_data.c"
alias vitmp="vi   /home/user/myy/tmp_data.c"
alias netmp="nedit /home/user/myy/tmp_data.c&"
alias ne="nedit"
alias mnt="cd /mnt/MY_FLASH/"
alias myy="cd /home/user/myy/"
alias uf="echo  sync and umount /mnt/MY_FLASH  && sync && umount /mnt/MY_FLASH"
alias uf1="echo sync and umount /mnt/MY_FLASH  && sync && umount /mnt/MY_FLASH"
alias uf2="echo sync and umount /mnt/FLASHDISK && sync && umount /mnt/FLASHDISK"
alias gcc="gcc -Wall"
alias g++="g++ -Wall"
alias cal="cal -m"
alias gcct="gcc -Wall -lpthread"
alias gccm="gcc -Wall -lm"
alias gcc2="/usr/local/bin/mipsel-linux-gcc"
alias ftpme="ftp   172.21.98.170"
alias ftpmy="ftp   172.21.98.170"
alias tftpme="tftp 172.21.100.206"
alias tftpmy="tftp 172.21.100.206"
alias t="time"
alias toc="cat /proc/cd/cd_toc"
alias vimesg="vi /var/log/messages"
alias vimsg="vi  /var/log/messages"

alias backupsystemdata="echo Backup system data 172.21.15.130;
#nfs2;dvd;
rm -rf /home/user/_backup_system_data*;
mkdir  /home/user/_backup_system_data;
mkdir  /home/user/_backup_system_data/130;
cp /etc/profile.d/alias.sh /home/user/_backup_system_data/130;
cp -r /home/user/myy /home/user/_backup_system_data/130;
cp -r /home/user/_ctest_linux/ /home/user/_backup_system_data/130;
zip -r _backup_system_data.zip _backup_system_data/
echo Backup to /home/user/_backup_system_data;
echo Backup-zip-data: _backup_system_data.zip;
du -sh _backup_system_data.zip;
echo Go to /home/user/_backup_system_data;
cd /home/user/_backup_system_data"


alias victest="dvd; vi ctest.c"

alias sstq="svn st -q"
#alias sstqll="sstq | xargs ls -ltrh"
alias sstqll="echo;echo List svn modified files;echo;svn st -q | grep \"^\M\" | cut -c9- | xargs ls -ltrh;echo"
alias sst="svn st"
alias sd="svn diff"
alias sb="svn blame"
alias sdiff="svn diff"
alias slog="svn log"
alias slmore="svn log | more"
alias slogvr="svn log -v -r"
alias slvr="svn log -v -r"
alias srev="svn revert"
alias sci="svn ci"
alias sls="svn ls"
alias sco="svn co"
alias scor="svn co -r"
alias sup="svn up"
alias sinfo="svn info"
alias supr="svn up -r "
alias findo="echo;echo find all .o files;echo;echo;find . -name \"*.o\""


#######################################################################################
# use for scaler TV
#######################################################################################

alias fff="echo   Search pattern in \*.cpp;pwd;echo;echo;echo;find . -name \"*.cpp\" | xargs grep"
alias fffh="echo  Search pattern in \*.h  ;pwd;echo;echo;echo;find . -name \"*.h\"   | xargs grep"
alias fffc="echo  Search pattern in \*.c  ;pwd;echo;echo;echo;find . -name \"*.c\"   | xargs grep"
alias fffci="echo  Search pattern in \*.c, ignore case;pwd;echo;echo;echo;find . -name \"*.c\"   | xargs grep -i"
alias fffi="echo  Search pattern in \*.cpp, ignore case;pwd;echo;echo;echo;find . -name \"*.cpp\" | xargs grep -i"
alias fffx="echo  Search pattern in \*;pwd;echo;echo;echo;find .  -name \"*\" | xargs grep"
alias fffxi="echo Search pattern in \*;pwd;echo;echo;echo;find .  -name \"*\" | xargs grep -i"
alias fffix="echo Search pattern in \*;pwd;echo;echo;echo;find .  -name \"*\" | xargs grep -i"

alias nfs="cd      /home/user/nfs/;pwd;echo"
alias strip="echo;echo strip DvdPlayer and copy it to /home/user/;echo;mipsel-linux-strip DvdPlayer;cpd"
#alias maked="makeh"
#alias makeh="slr&&make&&haier&&make link"
#alias makem="makeg"

alias show216svnpath="216;echo;echo Show Pacific\' 32MB 216 pin svn path:;echo;svn info | egrep URL | awk '{print $2}';echo;cd-"
alias show100svnpath="100;echo;echo Show Pacific\' no DDR 100 pin svn path:;echo;svn info | egrep URL | awk '{print $2}';echo;cd-"
alias showmacsvnpath="mac;echo;echo Show Mac Arthur svn path:;echo;svn info | egrep URL | awk '{print $2}';echo;cd-"

#######################################################################################
# use for test
#######################################################################################

alias sciwarning="svn ci -m \"david: Remove some compiling warnings.\""

alias findname="echo;pwd;echo;echo find file;echo;find       . | grep -i"
alias fnpl="echo;echo find perl files...;echo;find . | grep  \"\.pl\";echo"
alias findpl="echo;echo find perl files...;echo;find . | grep  \"\.pl\";echo"
alias findperl="echo;echo find perl files...;echo;find . | grep  \"\.pl\";echo"
alias findperlfiles="echo;echo find perl files...;echo;find . | grep  \"\.pl\";echo"
#alias fn="echo;pwd;echo;echo find file;echo;find       . | grep -i;echo"
alias fn="echo;pwd;echo;echo find file;echo;find       . | grep -i"
alias grepinclude="echo grep include in c files;fffc include | grep "
alias hvi="h|grep vi\ "
alias hmake="h|grep make\ "
alias hcp="h|grep cp\ "
alias hgrep="h|grep "
alias ss="echo;echo sync;sync;sync;echo"

alias showvitricks="echo;echo show vi tricks;echo;
echo ctrl + g : show status
echo \~   \ \ \ \ \ \ \ : ?��?大�?�?
echo ?�代 : % s/old_string/new_string /cg
echo :set nu \ \ \ \  顯示行�?
echo :set nonu \ \  ?��?行�?
echo :set ic \ \ \ \    ?��??��??�大小寫
echo :set noic \ \  ?��??��??�?�大小寫
echo;echo"
alias supr="svn up -r "
alias supr="svn up -r "
alias supr="svn up -r "
alias supr="svn up -r "
alias supr="svn up -r "
alias supr="svn up -r "
alias supr="svn up -r "


# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi





