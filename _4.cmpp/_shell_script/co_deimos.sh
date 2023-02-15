#!/bin/bash
PATH=/usr/local/bin:$PATH
#LANG=zh_TW.Big5
#LC_ALL=zh_TW.Big5
#export LC_ALL
#export LANG
export PATH

build_EWHA=1
branchOut=0
resAddBT=1
resAddRSS=1
setting=0
debug=0
prjDir="AVHDD_MARS_DTV"
scriptDir="/mnt/SQA320_DTV/1073_daily_build"
rootdir="$scriptDir/$prjDir"
mkdir -p $rootdir

SvnImgURL="http://cadinfo/svn/col/DVR/mars/software/system/flash_environment/develop/image_file"
SvnImgAvhddURL="http://cadinfo/svn/col/DVR/mars/software/system/flash_environment/develop/image_file_avhdd"
SvnImgAvhdd_v2URL="http://cadinfo/svn/col/DVR/mars/software/system/flash_environment/develop/image_file_avhdd_v2"
SvnBootcodeURL="http://cadinfo/svn/col/DVR/venus/software/system/flash_environment/Bootcode/Mars_Bootcode/release/1283/qa"
SvnSystemURL="http://cadinfo/svn/col/DVR/branches/software_DTV"
SvnMarsComURL="http://cadinfo/svn/col/DVR/mars/software"
sqaBranchURL="http://cadinfo/svn/col/DVR/branches/SQA/MARS_DTV_Branch"
Main_URL="http://cadinfo/svn/col/DVR/venus/software/system/src/"

[ "$build_EWHA" == "1" ] && UI_type="Ewha_MK1" || UI_type="GrandMa_DG_StateMachine"
srcDir="branch_src_sharedMemory_integration"

APPath="$rootdir/svn/system/branch_src_sharedMemory_integration/Unit_test/""$UI_type"
WGPath="$rootdir/svn/system/branch_src_sharedMemory_integration/Unit_test/WatchDogApp"
imgPath="$rootdir/svn/system/flash_environment/develop/image_file"
imgAvhddPath="$rootdir/svn/system/flash_environment/develop/image_file_avhdd"

vns_AVHDD_Linux_Nor_URL="$SvnImgAvhddURL"/components/packages/package1/vmlinux.develop.avhdd.mars.bin.zip
vns_AVHDD_Linux_Nand_URL="$SvnImgAvhddURL"/components/packages/package2/vmlinux.develop.avhdd.mars.nand.bin.zip
vns_AVHDD_v2_Linux_Nor_URL="$SvnImgAvhdd_v2URL"/components/packages/package1/vmlinux.develop.avhdd.mars.bin.zip
vns_AVHDD_v2_Linux_Nand_URL="$SvnImgAvhdd_v2URL"/components/packages/package2/vmlinux.develop.avhdd.mars.nand.bin.zip
vns_Video_URL="$SvnImgURL"/components/bluecore.video.zip
vns_Audio_URL="$SvnImgURL"/components/bluecore.audio.zip
IMS_Ver=`svn list --verbose $Main_URL | grep Application | cut -c2-7`
NewCommonVer=`svn list --verbose $SvnMarsComURL | grep common | cut -c2-7`
apVer=`svn list --verbose $SvnSystemURL | grep system/ | cut -d " " -f2`
linuxVer=`svn list --verbose $vns_AVHDD_Linux_Nor_URL | cut -d " " -f2`
linuxNandVer=`svn list --verbose $vns_AVHDD_Linux_Nand_URL | cut -d " " -f2`
linuxSrcVer=`svn log $vns_AVHDD_Linux_Nor_URL | head -5 | grep "MARS_AVHDD" | cut -d ":" -f2 | cut -d "," -f1`
videoVer=`svn list --verbose $vns_Video_URL | cut -d " " -f2`
videoSrcVer=`svn log $vns_Video_URL | head -5 | grep "source" | cut -d ":" -f2`
audioVer=`svn list --verbose $vns_Audio_URL | cut -d " " -f2`
audioSrcVer=`svn log $vns_Audio_URL | head -5 | grep "src"  | cut -d " " -f6`

if [ -n "$1" ];then
  if [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
    echo "version error, $1,$2,$3,$4"
    exit
  else
    apVer=$1; linuxVer=$2; videoVer=$3; audioVer=$4
    echo "version from user : $apVer,$linuxVer,$videoVer,$audioVer"
  fi
else
  echo "version from svn : $apVer,$linuxVer,$videoVer,$audioVer"
fi

fp_apVer="$apVer"

if [ "$branchOut" == "1" ]; then
  dirDate=`date +%Y%m%d`
  dirName="$dirDate"_"$fp_apVer"
  dirExist=`svn list --verbose $sqaBranchURL | grep -m 1 $fp_apVer | cut -d ":" -f2 | cut -c4-18`
  echo "dirExist = $dirExist"
  if [ -z "$dirExist" ]; then
    destURL="$sqaBranchURL/$dirName"
    echo "destURL = $destURL"
    svn mkdir "$destURL" -m "remote create folder for ap version : $fp_apVer"
    svn cp -r "$NewCommonVer" "$SvnMarsComURL/common" "$destURL/common" -m "remote copy for mars common version:$NewCommonVer"
    svn cp -r "$fp_apVer" "$SvnSystemURL/system" "$destURL/system" -m "remote copy for system version:$fp_apVer"
     [ "$debug" == "1" ] && read -p "please check...." wait
    echo "IMS Version : $IMS_Ver"
    svn cp -r "$IMS_Ver" http://cadinfo/svn/col/DVR/venus/software/system/src/Application/Win32/RSSClient "$destURL/system/""$srcDir/Application/Win32/RSSClient" -m "IMS remote copy, version:$IMS_Ver"
    echo "destURL : $destURL"
     [ "$debug" == "1" ] && read -p "please check...." wait

    svn cp -r "$IMS_Ver" http://cadinfo/svn/col/DVR/venus/software/system/src/Application/Win32/OSAL "$destURL/system/""$srcDir/Application/Win32/OSAL" -m "IMS remote copy, version:$IMS_Ver"
     [ "$debug" == "1" ] && read -p "please check...." wait

    svn mkdir "$destURL/system/""$srcDir/Application/Projects/CommonModules/" -m "remote create folder"
    fp_apVer=`svn cp -r "$IMS_Ver" http://cadinfo/svn/col/DVR/venus/software/system/src/Application/Projects/CommonModules/IMS "$destURL/system/""$srcDir/Application/Projects/CommonModules/IMS" -m "IMS remote copy for system version:$IMS_Ver" | grep "Committed revision" | cut -d " " -f3 | cut -d "." -f1`
     [ "$debug" == "1" ] && read -p "please check...." wait

  else
    destURL="$sqaBranchURL/$dirExist"
    echo "destURL = $destURL"
    fp_apVer=`svn list --verbose "$sqaBranchURL" | grep "$dirExist" | cut -d " " -f2`
#    read -p "exist fp_apVer=$fp_apVer" wait
  fi
  apVer="$fp_apVer"
  SvnSystemURL="$destURL"
  SvnMarsComURL="$destURL/common"

fi

    CurDate=`date +%H%M_%m%d_%Y`
    oldvn=`cat $rootdir/svn/system/include/.svn/entries | grep -m 1 revision= | cut -c14-19`
    oldsvnname=svn_"$oldvn"_"$CurDate"

    mv $rootdir/svn $rootdir/$oldsvnname
    cd $rootdir
    mkdir svn
    cd svn
    
    #check out commmon
    if [ "$branchOut" == "1" ]; then
    	svn checkout  "$SvnMarsComURL" common
    else
    	SvnMarsComURL="$SvnMarsComURL/common"
    	svn checkout -r "$NewCommonVer" "$SvnMarsComURL" common
    fi
    
    mkdir -p system/"$srcDir"/Unit_test
    cd $rootdir/svn/system

    svn checkout -r "$apVer" $SvnSystemURL/system/lib lib
    svn checkout -r "$apVer" $SvnSystemURL/system/lib_release lib_release
    svn checkout -r "$apVer" $SvnSystemURL/system/include include
    cp -f include/MakeConfig.PLAYER.MARS.SQA include/MakeConfig

     
#    cp -f include/MakeConfig.internal.SQA include/MakeConfig.internal
    sed -i "s/HONOR_HARDWARE/DA/" include/MakeConfig.internal
     [ "$debug" == "1" ] && read -p "please check...." wait

    svn checkout -N $SvnSystemURL/system/"$srcDir" "$srcDir"
    
    cd $rootdir/svn/system/"$srcDir"
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Application Application
    if [ "$branchOut" != "1" ]; then
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Win32/RSSClient Application/Win32/RSSClient
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Win32/OSAL  Application/Win32/OSAL
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Projects/CommonModules/IMS Application/Projects/CommonModules/IMS
    fi
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Drivers Drivers
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Filters Filters
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Flows Flows     
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Include Include    
    svn cat -r "$apVer" $SvnSystemURL/system/"$srcDir"/Makefile > Makefile
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/OSAL OSAL    
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Platform_Lib Platform_Lib
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Resource Resource
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Simulator Simulator
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/StreamClass StreamClass
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Utility Utility
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/io io
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/www www
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Security Security
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Tools
    svn checkout -N $SvnSystemURL/system/"$srcDir"/Unit_test Unit_test
    cd $rootdir/svn/system/"$srcDir"/Unit_test
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Unit_test/"$UI_type" "$UI_type"
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Unit_test/WatchDogApp WatchDogApp
    svn cat -r "$apVer" $SvnSystemURL/system/"$srcDir"/Unit_test/Makefile > Makefile

    cp -f "$UI_type"/MakeConfig.PLAYER.MARS.SQA "$UI_type"/MakeConfig

    [ "$debug" == "1" ] && read -p "please check...." wait

    cd $rootdir/svn/system
    mkdir -p flash_environment/develop
    cd $rootdir/svn/system/flash_environment/develop
    svn checkout $SvnImgURL image_file
    svn checkout $SvnImgAvhddURL image_file_avhdd
    svn checkout $SvnImgAvhdd_v2URL image_file_avhdd_v2

   [ "$setting" == "1" ] && read -p "You choose to customize MakeConfig to fit your demand, now do it....." wait

#    cp -f $scriptDir/RemoteControl.cpp.phobos  $rootdir/svn/system/branch_src_sharedMemory_integration/Platform_Lib/RemoteControl/RemoteControl.cpp
    cd $rootdir/svn/system/"$srcDir"
    make clean;make
	
    if [ -f "$APPath/DvdPlayer" ]; then
	echo "compile pass!!" > $scriptDir/Version_Mars.txt
    fi

    if [ ! -f "$APPath/DvdPlayer" ]; then
        echo "compile failed!!" > $scriptDir/Version_Mars.txt
    fi

    [ "$debug" == "1" ] && read -p "Please check make success.........." wait
#==========Make Watch Dog ============================================================================
     cd $WGPath
     make clean;make
     mipsel-linux-strip RootApp
#==========Config Make Release started================================================================
        cd $APPath
        make release
                rm -f bin/Resource/*.ttf
                cp -f Resource/arial.ttf bin/Resource/
##############################################################################################
              tmpEnableChinese=2      # will not change MakeConfig, need to change case by case
              if [ "$tmpEnableChinese" == "1" ]; then     #enable chinese not HI_FONT
                cp -f Resource/gkai00mp.ttf bin/Resource/
                cp -f Resource/cwheib.ttf bin/Resource/
                cd bin/Resource 
                ln -fs arial.ttf cwyen.ttf
              elif [ "$tmpEnableChinese" == "0" ]; then   #disable chinese
                cd bin/Resource
                ln -fs arial.ttf gkai00mp.ttf
                ln -fs arial.ttf cwheib.ttf
                ln -fs arial.ttf cwyen.ttf
              else                           #enable HI_FONT, all language, exclude Japan/Korea => has problems
                rm -f bin/Resource/u?.vc#
                rm -rf bin/Resource/*.ttf
                cd bin/Resource 
              fi

              cd ../..
              mkdir bin/DVD

                    # add for BT/samba
              if [ "$resAddBT" == "1" ]; then     
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/btpd_0.0.1_mipsel.ipk > bin/Resource/btpd_0.0.1_mipsel.ipk
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/samba_3.0.23c_mipsel.ipk > bin/Resource/samba_3.0.23c_mipsel.ipk
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/unicgi_0.0.1_mipsel.ipk > bin/Resource/unicgi_0.0.1_mipsel.ipk
              fi


                cp -rf Resource/dtv_table bin/Resource/
                rm -rf bin/Resource/dtv_table/.svn
                cp -rf Resource/TT_Font bin/Resource/
                rm -rf bin/Resource/TT_Font/.svn
	        cd bin/Resource    
                rm -f CC_Font/Font2.ttf
                rm -f CC_Font/Font3.ttf
                rm -f CC_Font/Font4.ttf
                rm -f CC_Font/Font5.ttf
                rm -f CC_Font/Font6.ttf
                rm -f CC_Font/Font7.ttf
#==========Config Make Release completed================================================================

        cd $imgAvhddPath/components/packages/package1/AP
        rm -rf bin
        cd $imgAvhddPath/components/packages/package2/AP
        rm -rf bin
        [ "$debug" == "1" ] &&  read -p "Please check AP/bin is removed.........." wait

        ## for package2
        cp -rf $APPath/bin .

        ## for package1
        cd $imgAvhddPath/components/packages/package1/AP
	rm -rf /bin/image
	rm -rf /bin/scripts
        cp -rf $APPath/bin .
        rm -rf bin/Resource/*.ipk
        if [ "$tmpEnableChinese" == "1" ]; then
           cd bin/Resource
           rm -f gkai00mp.ttf
           rm -f cwheib.ttf
           ln -fs arial.ttf gkai00mp.ttf
           ln -fs arial.ttf cwheib.ttf
        fi


        [ "$debug" == "1" ] && read -p "Please check AP/bin is copied.........." wait
        
        
    rm -f $imgAvhddPath/develop.avhdd.mars.flash.img
    rm -f $imgAvhddPath/install.img*


    cd $imgAvhddPath/components/packages/package1
    # modify Makefile.in    
    OldLinuxRev=`cat Makefile.in | grep LINUXREV= | cut -c10-15`
    OldLinux="LINUXREV=$OldLinuxRev"
    NewLinux="LINUXREV=$linuxVer"
    echo "OldLinuxRev=$OldLinuxRev"
    echo "NewLinuxRev=$linuxVer"
    sed -i "s/$OldLinux/$NewLinux/g" Makefile.in
    
    OldVideoRev=`cat Makefile.in | grep VIDEOREV= | cut -c10-15`
    OldVideo="VIDEOREV=$OldVideoRev"
    NewVideo="VIDEOREV=$videoVer"
    echo "OldVideoRev=$OldVideoRev"
    echo "NewVideoRev=$videoVer"
    sed -i "s/$OldVideo/$NewVideo/g" Makefile.in

    OldAudioRev=`cat Makefile.in | grep AUDIOREV= | cut -c10-15`
    OldAudio="AUDIOREV=$OldAudioRev"
    NewAudio="AUDIOREV=$audioVer"
    echo "OldAudioRev=$OldAudioRev"
    echo "NewAudioRev=$audioVer"
    sed -i "s/$OldAudio/$NewAudio/g" Makefile.in

    cd $imgAvhddPath/components/packages/package2
    OldLinuxRev=`cat Makefile.in | grep LINUXREV= | cut -c10-15`
    OldLinux="LINUXREV=$OldLinuxRev"
    NewLinux="LINUXREV=$linuxNandVer"
    sed -i "s/$OldLinux/$NewLinux/g" Makefile.in

    OldVideoRev=`cat Makefile.in | grep VIDEOREV= | cut -c10-15`
    OldVideo="VIDEOREV=$OldVideoRev"
    NewVideo="VIDEOREV=$videoVer"
    echo "OldVideoRev=$OldVideoRev"
    echo "NewVideoRev=$videoVer"
    sed -i "s/$OldVideo/$NewVideo/g" Makefile.in

    OldAudioRev=`cat Makefile.in | grep AUDIOREV= | cut -c10-15`
    OldAudio="AUDIOREV=$OldAudioRev"
    NewAudio="AUDIOREV=$audioVer"
    echo "OldAudioRev=$OldAudioRev"
    echo "NewAudioRev=$audioVer"
    sed -i "s/$OldAudio/$NewAudio/g" Makefile.in

    cd $imgAvhddPath/
    make svnup
#===================================
    cp ../image_file/components/SQA_dailybuild1/System.map.audio components/packages/package1
    cp ../image_file/components/SQA_dailybuild1/bluecore.audio.zip components/packages/package1
    cp ../image_file/components/SQA_dailybuild1/System.map.video components/packages/package1
    cp ../image_file/components/SQA_dailybuild1/bluecore.video.zip components/packages/package1

    cp ../image_file/components/SQA_dailybuild1/System.map.audio components/packages/package2
    cp ../image_file/components/SQA_dailybuild1/bluecore.audio.zip components/packages/package2
    cp ../image_file/components/SQA_dailybuild1/System.map.video components/packages/package2
    cp ../image_file/components/SQA_dailybuild1/bluecore.video.zip components/packages/package2
#===================================
    make image install_ap=1
    Date=`date +%Y.%m.%d`
    verStr=S"$apVer"_L"$linuxVer"_V"$videoVer"_A"$audioVer"
    mkdir "$Date"_"$verStr"
    
    echo "AP    : $apVer"
    echo "Linux : $linuxVer"
    echo "Video : $videoVer"
    echo "Audio : $audioVer"


    date >> $scriptDir/Version_Mars.txt
    echo "===================================================" >> $scriptDir/Version_Mars.txt
    echo "Version        :$verStr" >> $scriptDir/Version_Mars.txt
    echo "System         :$apVer" >> $scriptDir/Version_Mars.txt
    echo "Linux_Nor(Src) :$linuxVer($linuxSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Linux_Nand(Src):$linuxNandVer($linuxSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Video(Src)     :$videoVer($videoSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Audio(Src)     :$audioVer($audioSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Common         :$NewCommonVer" >> $scriptDir/Version_Mars.txt
    echo "IMS            :$IMS_Ver" >> $scriptDir/Version_Mars.txt


    cp install.img "$Date"_"$verStr"/install.img

    if [ ! -f "$APPath/DvdPlayer" ]; then
        cp $scriptDir/Version_Mars.txt "$Date"_"$verStr"/Fail_Version_Mars.txt
    fi

#======================= send img to server.54 =============================
    #cd $imgAvhddPath/../image_file_Deimos/
    #scp -r "$Date"_"$verStr" root@172.21.98.54:/mnt/SQA/1073_daily/

#====================== make 1283 QA Board ==========================

#change config to 1283 QA
#cd $rootdir/svn/system/include
#cp -f MakeConfig.AVHDD.MARS.SQA MakeConfig
#sed -i "s/BOARD_ID=RTD1283-DEMO/BOARD_ID=RTD1283-QA/" MakeConfig
#old="APCFG_CUSTOM_AVHDD+=|APCFG_HW_DVD|APCFG_HW_HDD|APCFG_HW_NET_ETH0|APCFG_HW_NET_WLAN0|APCFG_HW_USB|APCFG_HW_NET_WL_WPA|APCFG_HW_ANALOG_INPUT"
new="APCFG_CUSTOM_AVHDD+=|APCFG_HW_DVD|APCFG_HW_HDD|APCFG_HW_NET_ETH0|APCFG_HW_NET_WLAN0|APCFG_HW_USB|APCFG_HW_NET_WL_WPA"
#sed -i "s/$old/$new/" MakeConfig
#sed -i "s/EXTERNAL_TVD=YES/EXTERNAL_TVD=NO/" MakeConfig
#sed -i "s/REMOTE_ID=RTK_MK4/REMOTE_ID=JAECS_T118/" MakeConfig
#sed -i "s/TP0_FE=DTV_FE_RTL2832_TUA9001/TP0_FE=DTV_FE_RTL2830_TDTC_GX31D" MakeConfig
#cd $APPath
#cp -f MakeConfig.AVHDD.MARS.SQA MakeConfig
#=================   make DvdPlayer  ===========================================

cd $rootdir/svn/system/branch_src_sharedMemory_integration/
make clean all

cd $APPath
make release
                rm -f bin/Resource/*.ttf
                cp -f Resource/arial.ttf bin/Resource/

#===============       add for RSS ===========================================
              if [ "$resAddRSS" == "1" ]; then
                   cp -rf $rootdir/svn/system/branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/image bin/
                   cp -rf $rootdir/svn/system/branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/scripts bin/
                   rm -rf bin/image/.svn
                   rm -rf bin/image/country/.svn
                   rm -rf bin/scripts/.svn
                   rm -rf bin/scripts/map/.svn
                   rm -rf bin/scripts/map/China/.svn
                   rm -rf bin/scripts/map/France/.svn
                   rm -rf bin/scripts/map/Germany/.svn
                   rm -rf bin/scripts/map/Italy/.svn
                   rm -rf bin/scripts/map/Russia/.svn
                   rm -rf bin/scripts/map/United_Kingdom/.svn
                   rm -rf bin/scripts/map/United_States/.svn
                   rm -rf bin/scripts/map/United_States/California/.svn
                   rm -rf bin/scripts/sina/.svn
                   rm -rf bin/scripts/stock/.svn
                   rm -rf bin/scripts/stock/Taiwan/.svn

              fi

#=================   make install_qa.img  =========================================
cd $imgAvhddPath/../
time cp -rf image_file_avhdd/ image_file_Deimos/
cd image_file_avhdd/
rm -rf "$Date"_"$verStr"
cp -f $APPath/DvdPlayer .
mipsel-linux-strip DvdPlayer
cp -rf $APPath/bin components/packages/package1/AP/
cp -rf $APPath/bin components/packages/package2/AP/
cp -f DvdPlayer components/packages/package1/AP/bin/DvdPlayer
cp -f DvdPlayer components/packages/package2/AP/bin/DvdPlayer

make image install_ap=1
cp -f install.img ../image_file_Deimos/"$Date"_"$verStr"/install_qa.img
cp -f $APPath/DvdPlayer $imgAvhddPath/../image_file_Deimos/"$Date"_"$verStr"/DvdPlayer_qa


#====================== make 1283 Demo Board ==========================
#cd $rootdir/svn/system/include
#sed -i "s/BOARD_ID=RTD1283-QA/BOARD_ID=RTD1283-DEMO/" MakeConfig
#cd ../branch_src_sharedMemory_integration/
#make clean all

#=================   make install_demo.img  ===================================

cd $imgAvhddPath/../
time cp -rf image_file_avhdd/ image_file_qa_board/
cd image_file_avhdd/
rm -f DvdPlayer_qa
cp $APPath/DvdPlayer .
mipsel-linux-strip DvdPlayer
cp -rf $APPath/bin components/packages/package1/AP/
cp -rf $APPath/bin components/packages/package2/AP/
cp -f DvdPlayer components/packages/package1/AP/bin/DvdPlayer
cp -f DvdPlayer components/packages/package2/AP/bin/DvdPlayer

make image install_ap=1
cp -f install.img ../image_file_Deimos/"$Date"_"$verStr"/install_demo.img
cp -f $APPath/DvdPlayer $imgAvhddPath/../image_file_Deimos/"$Date"_"$verStr"/DvdPlayer_demo
#======================= copy Resource =====================================

cp -rf $APPath/bin/Resource/ $imgAvhddPath/../image_file_Deimos/"$Date"_"$verStr"/Resource/

#======================= send img to server.54 =============================
    #cd $imgAvhddPath/../image_file_Deimos/
    #scp -r "$Date"_"$verStr" root@172.21.98.54:/mnt/SQA/1073_daily/
	

    /etc/rc.d/init.d/sendmail restart
    mail chihchiang@realtek.com < $scriptDir/Version_Mars.txt 

exit


