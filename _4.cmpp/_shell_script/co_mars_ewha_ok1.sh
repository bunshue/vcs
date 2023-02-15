#!/bin/bash
#PATH=/usr/local/bin:$PATH
#LANG=zh_TW.Big5
#LC_ALL=zh_TW.Big5
#export LC_ALL
#export LANG
#export PATH

build_EWHA=1
branchOut=0
resAddBT=1
resAddRSS=1
setting=0
debug=0
prjDir="AVHDD_MARS_DTV"
scriptDir=`pwd`
rootdir="$scriptDir/$prjDir"
mkdir -p $rootdir

SvnImgURL="http://cadinfo/svn/col/DVR/mars/software/system/flash_environment/develop/image_file"
SvnImgAvhddURL="http://cadinfo/svn/col/DVR/mars/software/system/flash_environment/develop/image_file_avhdd"
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
    cp -f include/MakeConfig.AVHDD.MARS.SQA include/MakeConfig

    tmp="ENABLE_EWHA_PROJECT ="
    tmp1="ENABLE_EWHA_PROJECT = NO\n#$tmp"
    tmp2="ENABLE_EWHA_PROJECT = YES\n#$tmp"
    [ "$build_EWHA" == "1" ] && sed -i "s/$tmp/$tmp2/" include/MakeConfig || sed -i "s/$tmp/$tmp1/" include/MakeConfig
     
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
    cp -f "$UI_type"/MakeConfig.AVHDD.MARS.SQA "$UI_type"/MakeConfig

    [ "$debug" == "1" ] && read -p "please check...." wait

    cd $rootdir/svn/system
    mkdir -p flash_environment/develop
    cd $rootdir/svn/system/flash_environment/develop
    svn checkout $SvnImgURL image_file
    svn checkout $SvnImgAvhddURL image_file_avhdd

   [ "$setting" == "1" ] && read -p "You choose to customize MakeConfig to fit your demand, now do it....." wait

    #cp -f $scriptDir/RemoteControl.cpp.phobos  $rootdir/svn/system/branch_src_sharedMemory_integration/Platform_Lib/RemoteControl/RemoteControl.cpp
    cd $rootdir/svn/system/"$srcDir"
    make clean;make
    [ "$debug" == "1" ] && read -p "Please check make success.........." wait

#==========Config Make Release started================================================================
        cd $WGPath
        make clean;make
        mipsel-linux-strip RootApp
        cd $APPath
        make release
                rm -f bin/Resource/*.ttf
                cp -f Resource/arial.ttf bin/Resource/
                cp -f Resource/dtvFactoryTable.txt bin/Resource/
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
	      cp Resource/PackageConf.xml bin/Resource/
              mkdir bin/DVD

               # add for RSS
              #if [ "$resAddRSS" == "1" ]; then     
     		   #cp -r ../../../branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/image bin/
		   #cp -r ../../../branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/scripts bin/
                   
              #fi
                    # add for BT/samba
              if [ "$resAddBT" == "1" ]; then     
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/btpd_0.0.1_mipsel.ipk > bin/Resource/btpd_0.0.1_mipsel.ipk
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/samba_3.0.23c_mipsel.ipk > bin/Resource/samba_3.0.23c_mipsel.ipk
                svn cat http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_PVR/system/branch_src_sharedMemory_integration/Application/Packages/unicgi_0.0.1_mipsel.ipk > bin/Resource/unicgi_0.0.1_mipsel.ipk
              fi


                cp -rf Resource/dtv_table bin/Resource/
                cp -rf Resource/TT_Font bin/Resource/
		find bin/ -name ".svn" | xargs rm -rf
        #mkdir 576
        #mv *bmp 576
        #ln -s 576 bmp
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


#cd $imgAvhddPath
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
    OldLinux="LINUXREV=$linuxVer"
    NewLinux="LINUXREV=HEAD"
    sed -i "s/$OldLinux/$NewLinux/g" Makefile.in

    echo "OldVideoRev=$OldVideoRev"
    echo "NewVideoRev=$videoVer"
    sed -i "s/$OldVideo/$NewVideo/g" Makefile.in

    echo "OldAudioRev=$OldAudioRev"
    echo "NewAudioRev=$audioVer"
    sed -i "s/$OldAudio/$NewAudio/g" Makefile.in


#    make 
#    make nosvn=1
#    make install_ap=1
    cd $imgAvhddPath/
    make svnup
#    make image install_ap=1 PACKAGES=package1
#    make image install_ap=1
    make image install_ap=1 PACKAGES=package2

#    mv -f develop.avhdd.mars.flash.img install.img
    
    echo "AP    : $apVer"
    echo "Linux : $linuxVer"
    echo "Video : $videoVer"
    echo "Audio : $audioVer"


    verStr="$apVer"_L"$linuxVer"_V"$videoVer"_A"$audioVer"
    date > $scriptDir/Version_Mars.txt
    echo "===================================================" >> $scriptDir/Version_Mars.txt
    echo "Version        :$verStr" >> $scriptDir/Version_Mars.txt
    echo "AP             :$apVer" >> $scriptDir/Version_Mars.txt
    echo "Linux_Nor(Src) :$linuxVer($linuxSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Linux_Nand(Src):$linuxNandVer($linuxSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Video(Src)     :$videoVer($videoSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Audio(Src)     :$audioVer($audioSrcVer)" >> $scriptDir/Version_Mars.txt
    echo "Common         :$NewCommonVer" >> $scriptDir/Version_Mars.txt
    echo "IMS            :$IMS_Ver" >> $scriptDir/Version_Mars.txt

    #mkdir /mnt/46/korsen/mars/"$verStr"
    #cp -f $scriptDir/Version_Mars.txt /mnt/46/korsen/mars/"$verStr"
    mkdir -p $rootdir/Result/"$verStr"
    cp install.img $rootdir/Result/"$verStr"/install.img.phobos
     

exit


