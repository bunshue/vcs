#!/bin/bash
PATH=/usr/local/bin:$PATH
#LANG=zh_TW.Big5
#LC_ALL=zh_TW.Big5
#export LC_ALL
#export LANG
export PATH

branchOut=0
resAddRSS=1
setting=1
debug=0
HDCPop=1
prjDir="Jupiter_DTV"
scriptDir=`pwd`
rootdir="$scriptDir/$prjDir"
mkdir -p $rootdir

SvnImgURL="http://cadinfo/svn/col/DVR/jupiter/software/system/flash_environment/develop/image_file"
SvnImgAvhddURL="http://cadinfo/svn/col/DVR/jupiter/software/system/flash_environment/develop/image_file_avhdd"
#SvnBootcodeURL="http://cadinfo/svn/col/DVR/venus/software/system/flash_environment/Bootcode/Mars_Bootcode/release/1283/qa"
SvnSystemURL="http://cadinfo/svn/col/DVR/branches/software_DTV"
SvnJupiterComURL="http://cadinfo/svn/col/DVR/jupiter/software"
sqaBranchURL="http://cadinfo/svn/col/DVR/branches/SQA/Jupiter_Casablanca_Branch"
Main_URL="http://cadinfo/svn/col/DVR/venus/software/system/src/"

UI_type="Casablanca"
srcDir="branch_src_sharedMemory_integration"

APPath="$rootdir/svn/system/branch_src_sharedMemory_integration/Unit_test/""$UI_type"
WGPath="$rootdir/svn/system/branch_src_sharedMemory_integration/Unit_test/WatchDogApp"
imgPath="$rootdir/svn/system/flash_environment/develop/image_file"
imgAvhddPath="$rootdir/svn/system/flash_environment/develop/image_file_avhdd"
toolPath="$rootdir/svn/system/branch_src_sharedMemory_integration/Tools"


vns_AVHDD_Linux_Nand_URL="$SvnImgAvhddURL"/components/packages/package2/vmlinux.develop.avhdd.jupiter.nand.bin.zip
vns_Video_URL="$SvnImgURL"/components/bluecore.video.zip
vns_Audio_URL="$SvnImgURL"/components/bluecore.audio.zip
IMS_Ver=`svn list --verbose $Main_URL | grep Application | cut -c2-7`
NewCommonVer=`svn list --verbose $SvnJupiterComURL | grep common | cut -c2-7`
apVer=`svn list --verbose $SvnSystemURL | grep system/ | cut -d " " -f2`
#linuxVer=`svn list --verbose $vns_AVHDD_Linux_Nor_URL | cut -d " " -f2`
linuxNandVer=`svn list --verbose $vns_AVHDD_Linux_Nand_URL | cut -d " " -f2`
linuxSrcVer=`svn log $vns_AVHDD_Linux_Nand_URL | head -5 | grep "jupiter" | cut -d ":" -f2 | cut -d "," -f1`
videoVer=`svn list --verbose $vns_Video_URL | cut -d " " -f2`
videoSrcVer=`svn log $vns_Video_URL --limit 1 | grep source | cut -d ":" -f2 | cut -d "," -f1`
audioVer=`svn list --verbose $vns_Audio_URL | cut -d " " -f2`
audioSrcVer=`svn log $vns_Audio_URL --limit 1 | grep src | cut -d "=" -f2 | cut -d " " -f1`

if [ "$1" != "release" ]; then
   if [ -n "$1" ];then
     if [ "$2" == "0" ]; then
       apVer=$1; 
       echo "version from user : $apVer,$linuxNandVer,$videoVer,$audioVer"
#    if [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
#       echo "version error, $1,$2,$3,$4"
#       exit
     else
       apVer=$1; linuxNandVer=$2; videoVer=$3; audioVer=$4
       echo "version from user : $apVer,$linuxNandVer,$videoVer,$audioVer"
     fi
   else
    echo "version from svn : $apVer,$linuxNandVer,$videoVer,$audioVer" 
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
    svn cp -r "$NewCommonVer" "$SvnJupiterComURL/common" "$destURL/common" -m "remote copy for jupiter common version:$NewCommonVer"
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
  fi

  SvnSystemURL="$destURL"
  SvnJupiterComURL="$destURL/common" 
fi

    dirDate=`date +%Y%m%d`
    apVer="$fp_apVer"
    dirName="$dirDate"_"$fp_apVer"

    mv $rootdir/svn $rootdir/svn_"$dirName"
    cd $rootdir
    mkdir svn
    cd svn
    
    #check out commmon
    if [ "$branchOut" == "1" ]; then
    	svn checkout  "$SvnJupiterComURL" common
    else
    	SvnJupiterComURL="$SvnJupiterComURL/common"
    	svn checkout -r "$NewCommonVer" "$SvnJupiterComURL" common
    fi
    
    mkdir -p system/"$srcDir"/Unit_test
    cd $rootdir/svn/system

    svn checkout -r "$apVer" $SvnSystemURL/system/lib lib
    svn checkout -r "$apVer" $SvnSystemURL/system/lib_release lib_release
    svn checkout -r "$apVer" $SvnSystemURL/system/include include
    cp -f include/MakeConfig.PLAYER.JUPITER.CASABLANCA include/MakeConfig

    svn checkout -N $SvnSystemURL/system/"$srcDir" "$srcDir"
    
    cd $rootdir/svn/system/"$srcDir"
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Application Application
    if [ "$branchOut" != "1" ]; then
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Win32/RSSClient Application/Win32/RSSClient
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Win32/OSAL  Application/Win32/OSAL
    svn checkout -r "$IMS_Ver" http://172.21.0.100/svn/col/DVR/venus/software/system/src/Application/Projects/CommonModules/IMS Application/Projects/CommonModules/IMS

    #svn checkout -r "$IMS_Ver" http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_DTV_Rebecca/system/branch_src_sharedMemory_integration/Application/Win32/RSSClient Application/Win32/RSSClient
    #svn checkout -r "$IMS_Ver" http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_DTV_Rebecca/system/branch_src_sharedMemory_integration/Application/Win32/OSAL /Application/Win32/OSAL
    #svn checkout -r "$IMS_Ver" http://cadinfo.realtek.com.tw/svn/col/DVR/branches/software_DTV_Rebecca/system/branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS Application/Projects/CommonModules/IMS


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
    svn checkout -r "$apVer" $SvnSystemURL/system/"$srcDir"/Unit_test/UnixSocket UnixSocket
    svn cat -r "$apVer" $SvnSystemURL/system/"$srcDir"/Unit_test/Makefile > Makefile


    [ "$debug" == "1" ] && read -p "please check...." wait

    cd $rootdir/svn/system
    mkdir -p flash_environment/develop
    cd $rootdir/svn/system/flash_environment/develop
    svn checkout $SvnImgURL image_file
    svn checkout $SvnImgAvhddURL image_file_avhdd
#    svn checkout $SvnImgAvhddURL image_file_Ewha

   [ "$setting" == "1" ] && read -p "You choose to customize MakeConfig to fit your demand, now do it....." wait

    cd $rootdir/svn/system/"$srcDir"

#================ enable wma in Rebecca & replace resource.cpp =====================================

    #cp -f $scriptDir/featureCheck.cpp Security/
    #cp -f $scriptDir/resource.cpp Utility/ResourceMgr/

#== for gail disbale HDCP ==========================================================================

    if [ "$HDCPop" == "1" ]; then
	cd $rootdir/svn/system/include/
	OldHDCP="USE_HDCP    = YES"
	NewHDCP="USE_HDCP    = NO"
	sed -i "s/$OldHDCP/$NewHDCP/g" MakeConfig
	cd $rootdir/svn/system/"$srcDir"
    fi

#====================================================================================================
    make clean;make
	
    if [ ! -f "$APPath/DvdPlayer" ]; then
        echo "compile failed!!" 
        exit
    fi

    [ "$debug" == "1" ] && read -p "Please check make success.........." wait
#==========Make Watch Dog ============================================================================
     cd $WGPath
     make clean;make
     mipsel-linux-strip RootApp

#else
#  cd $APPath
#  apVer = `cat ver.h | cut -d ":" -f2 | cut -c2-7`
fi  # => if [ "$1" != "release" ];


#==========Config Make Release started================================================================
        cd $APPath
        make release

#=========== bmp2felics ========================================
#        cd $toolPath/bmp2felics
#	make
#        ./bmp2felics ../../../branch_src_sharedMemory_integration/Unit_test/Rebecca/Resource/
#	./bmp2felics ../../../branch_src_sharedMemory_integration/Unit_test/Rebecca
#	cd $APPath/Resource/rfc/
#	cp -f *.bmp ../../bin/Resource/
	cd $APPath
	cp -rf menubar/ bin/
	cp -rf NetFlix/ bin/
##############################################################################################
	#cp youtube key 
	cp -f $scriptDir/youtubeDevKey bin/Resource

	# rm *.ttf 
	rm -f bin/Resource/arial.ttf
	rm -f bin/Resource/cwheib.ttf
	rm -f bin/Resource/cwyen.ttf
	rm -f bin/Resource/gkai00mp.ttf

	#Add Hi Font
	#cp -f UTF8-pinyin* bin/ 			#add cn keyin
	cp Resource/uER.vcp bin/Resource/
	cp Resource/AR_EGBJK.ttf bin/Resource/
	cp -f Resource/*.pem bin/Resource/
	cp -f Resource/youtubeDevKey bin/Resource/

	cd bin/Resource/
	rm -f *.vc#
	ln -s AR_EGBJK.ttf arial.ttf
	ln -s AR_EGBJK.ttf cwheib.ttf
	ln -s AR_EGBJK.ttf cwyen.ttf
	ln -s AR_EGBJK.ttf gkai00mp.ttf
	cd $APPath

        # add for RSS
        if [ "$resAddRSS" == "1" ]; then     
  	cp -r ../../../branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/Rebecca/image bin/
	cp -r ../../../branch_src_sharedMemory_integration/Application/Projects/CommonModules/IMS/Rebecca/scripts bin/
        fi
        ###### add for Opera ##############
        cd $APPath
        cp -rf opera_dir bin
        cp -rf opera_fonts bin
        cp -rf opera_home bin
        cp -rf opera_widgets bin
        cp -f libgcc_s.so.1 bin
        cp -f libstdc++.so.6 bin
        ###################################3
        mkdir bin/DVD 
        find ./bin/ -name .svn | xargs rm -rf

#==========Config Make Release completed========

        rm -rf $imgAvhddPath/components/packages/package2/AP/bin
        cp -rf $APPath/bin $imgAvhddPath/components/packages/package2/AP/
        mkdir $imgAvhddPath/components/packages/package2/AP/etc/dvdplayer
        touch $imgAvhddPath/components/packages/package2/AP/etc/dvdplayer/SDK.bin
        #cp $scriptDir/SDK.bin $imgAvhddPath/components/packages/package2/AP/etc/dvdplayer

        
  if [ "$1" == "release" ]; then
        cd $imgAvhddPath
        make image install_ap=1 
        exit
  fi
       rm -rf $imgAvhddPath/components/packages/package1
	cd $imgAvhddPath/components/packages/package2
       OldLinuxRev=`cat Makefile.in | grep LINUXREV= | cut -c10-15`
       OldLinux="LINUXREV=$OldLinuxRev"
	NewLinux="LINUXREV=$linuxNandVer"
	sed -i "s/$OldLinux/$NewLinux/g" Makefile.in

       OldVideoRev=`cat Makefile.in | grep VIDEOREV= | cut -c10-15`
       OldVideo="VIDEOREV=$OldVideoRev"
       NewVideo="VIDEOREV=$videoVer"
       sed -i "s/$OldVideo/$NewVideo/g" Makefile.in
  
       OldAudioRev=`cat Makefile.in | grep AUDIOREV= | cut -c10-15`
       OldAudio="AUDIOREV=$OldAudioRev"
       NewAudio="AUDIOREV=$audioVer"
       sed -i "s/$OldAudio/$NewAudio/g" Makefile.in

	OldURL="LIVEUPDATE_URL="
	NewURL="LIVEUPDATE_URL=http:\/\/172.21.98.68\/Casablanca\/theaterappliance.xml"
	sed -i "s/$OldURL/$NewURL/g" Makefile.in

       cd $imgAvhddPath/
       rm -f install.img*
       rm -f image*.bz2

#       Currently, A/V firmware formal release not ready , so copy manually 
#       make svnup
       cp -f $imgAvhddPath/../image_file/components/SQA_DailyBuild_Jupiter/* components/packages/package2
       make image install_ap=1 PACKAGES=package2

#      verStr="$apVer"_L"$linuxNandVer"_V"$videoVer"_A"$audioVer"

#        date >> Version_Casablanca.txt
#	echo "===================================================" >> Version_Casablanca.txt
#	echo "Version        :$verStr" >> Version_Casablanca.txt
#	echo "System         :$apVer" >> Version_Casablanca.txt
#	echo "Linux_Avhdd(Src):$linuxNandVer($linuxSrcVer)" >> Version_Casablanca.txt
#	echo "Video(Src)     :$videoVer($videoSrcVer)" >> Version_Casablanca.txt
#	echo "Audio(Src)     :$audioVer($audioSrcVer)" >> Version_Casablanca.txt
#	echo "Common         :$NewCommonVer" >> Version_Casablanca.txt
#	echo "IMS            :$IMS_Ver" >> Version_Casablanca.txt

#       mkdir -p /mnt/46/korsen/Casablanca/"$verStr"
#       cp install.img /mnt/46/korsen/Casablanca/"$verStr"

exit

