

vid = videoinput('winvideo',1);
preview(vid)


preview(vid)
stoppreview(vid)	% stop/pause preview
closepreview(vid)	% close preview
closepreview()		% close all preview


imaqhwinfo()¡AƒS‰÷¨úPC¤W¥H¦w†Eªº†¶¹³‰÷¨úµw¥ó«H®§

info=imaqhwinfo		%•Ê¦³‰r¤Jƒò‡Ûƒº¡Aªğ¦^¤@ƒª…CÌÛÊ^¡A ¥¦¥]§t¤F¨t„i¤¤¦s¦bªºÓì°t¾¹©MMatlab¬Û‹×ªºª©¥»«H®§
win_info=imaqhwinfo('winvideo')	%¦³‰r¤Jƒò‡Ûªºƒº­Ô¡Aªğ¦^¤@ƒª…CÌÛÊ^¡A¥]§t¤F«ü©wªºÓì°t¾¹ªº‡ÛÕu«H®§
win_info.DeviceIDs
win_info.DeviceInfo
win_info.DeviceInfo.DeviceName
win_info.DeviceInfo(2).DeviceName					%¬d¬İ²Ä¤G­Ó¸Ë¸mªº¸ê°T
win_info.DeviceInfo.SupportedFormats
win_info.DeviceInfo(2).SupportedFormats		%¬d¬İ²Ä¤G­Ó¸Ë¸mªº¸ê°T

obj = videoinput('winvideo',1,'YUY2_640x480');
%obj = videoinput('winvideo',2,'YUY2_640x480');

%„¦¸mªğ¦^¦â±m rgb¥¿±`‹^¦â¡]YUY2®æ¦¡‹^¦â„úƒq¡^¡Agrayscale¬O¦Ç«×
set(obj,'ReturnedColorSpace','rgb');
%set(obj,'ReturnedColorSpace','grayscale');
%‰÷¨ú¤À¿ë²v¡A¦â±m‡Û¥Øµ¥ƒò‡Û
vidRes = get(obj, 'VideoResolution');%…S‰±¤À¿ë²v
nBands = get(obj, 'NumberOfBands');%¦â±m‡Û¥Ø
figure()	%«ü©w†{Œ¦µ¡Ê^F¥Üªºfigure
axes()		%«ü©w†{Œ¦µ¡¤fF¥Üªº§¤‡á¨t
hImage = image( zeros(vidRes(2), vidRes(1), nBands) );
preview(obj, hImage);

%†¶¹³®·®»¡BF¥Ü©M«O¦s

Frame = getsnapshot(obj);	% ®·‰÷†¶¹³
imshow(Frame);
imwrite(Frame,'snap.jpg','jpg');






¥ÎMatlab¬İWebCam

clear all;
close all;
obj=videoinput('winvideo',1,'YUY2_640x480');
preview(obj);
pause(30);
closepreview(obj);
delete(obj);

clear all;
close all;
obj=videoinput('winvideo',2,'YUY2_640x480');
preview(obj);
pause(30);
closepreview(obj);
delete(obj);


imaqmem(50000000);
imaqmem Limit or display memory in use by the Image Acquisition Toolbox.
 
Matlabªº†¶¹³‰÷¨ú¤u¨ã½cƒo§Ú´£¨Ñ¤Fimaqhwinfo()¡AƒS‰÷¨úPC¤W¥H¦w†Eªº†¶¹³‰÷¨úµw¥ó«H®§

SupportedFormats
winvideoinfo=imaqhwinfo('winvideo')	%¥i¥H¬İ¨ìwindow¸Ì¦³¦w¸Ëµø°TºI¨ú¸Ë¸m, ¥]¬Awebcam©M¹qµø¥dµ¥
winvideoinfo.DeviceInfo
winvideoinfo.DeviceInfo.SupportedFormats

vid = videoinput('winvideo', 1); 	%°²³]webcamªº¸Ë¸mDeviceID¬O1, ¥i¥Îimaqhwinfo('winvideo')¬d¸ß
preview(vid);	%¼½©ñ

vid = videoinput('winvideo', 2); 	%°²³]webcamªº¸Ë¸mDeviceID¬O1, ¥i¥Îimaqhwinfo('winvideo')¬d¸ß
preview(vid);	%¼½©ñ

DeviceInfoªº¤º®e¡G
winvideoinfo.DeviceInfo	//¬d¬İ©Ò¦³¸Ë¸mªº¸ê°T
ans = 
1x2 struct array with fields:
    DefaultFormat
    DeviceFileSupported
    DeviceName
    DeviceID
    VideoInputConstructor
    VideoDeviceConstructor
    SupportedFormats
    
%¬d¬İDevice2ªº¸ê°T¡G	//¬d¬İ¯S©w¸Ë¸mªº¸ê°T
device2 = winvideoinfo.DeviceInfo(2)
name2   = winvideoinfo.DeviceInfo(2).DeviceName
format2 = winvideoinfo.DeviceInfo(2).SupportedFormats
 




