

vid = videoinput('winvideo',1);
preview(vid)


preview(vid)
stoppreview(vid)	% stop/pause preview
closepreview(vid)	% close preview
closepreview()		% close all preview


imaqhwinfo()�A�S����PC�W�H�w�E�����������w��H��

info=imaqhwinfo		%�ʦ��r�J��ۃ��A��^�@���C���^�A ���]�t�F�t�i���s�b����t���MMatlab�ۋת������H��
win_info=imaqhwinfo('winvideo')	%���r�J��۪����ԡA��^�@���C���^�A�]�t�F���w����t�������u�H��
win_info.DeviceIDs
win_info.DeviceInfo
win_info.DeviceInfo.DeviceName
win_info.DeviceInfo(2).DeviceName					%�d�ݲĤG�Ӹ˸m����T
win_info.DeviceInfo.SupportedFormats
win_info.DeviceInfo(2).SupportedFormats		%�d�ݲĤG�Ӹ˸m����T

obj = videoinput('winvideo',1,'YUY2_640x480');
%obj = videoinput('winvideo',2,'YUY2_640x480');

%���m��^��m rgb���`�^��]YUY2�榡�^����q�^�Agrayscale�O�ǫ�
set(obj,'ReturnedColorSpace','rgb');
%set(obj,'ReturnedColorSpace','grayscale');
%��������v�A��m�ۥص����
vidRes = get(obj, 'VideoResolution');%�S������v
nBands = get(obj, 'NumberOfBands');%��m�ۥ�
figure()	%���w�{�����^�F�ܪ�figure
axes()		%���w�{�����f�F�ܪ�����t
hImage = image( zeros(vidRes(2), vidRes(1), nBands) );
preview(obj, hImage);

%���������B�F�ܩM�O�s

Frame = getsnapshot(obj);	% ��������
imshow(Frame);
imwrite(Frame,'snap.jpg','jpg');






��Matlab��WebCam

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
 
Matlab�����������u��c�o�ڴ��ѤFimaqhwinfo()�A�S����PC�W�H�w�E�����������w��H��

SupportedFormats
winvideoinfo=imaqhwinfo('winvideo')	%�i�H�ݨ�window�̦��w�˵��T�I���˸m, �]�Awebcam�M�q���d��
winvideoinfo.DeviceInfo
winvideoinfo.DeviceInfo.SupportedFormats

vid = videoinput('winvideo', 1); 	%���]webcam���˸mDeviceID�O1, �i��imaqhwinfo('winvideo')�d��
preview(vid);	%����

vid = videoinput('winvideo', 2); 	%���]webcam���˸mDeviceID�O1, �i��imaqhwinfo('winvideo')�d��
preview(vid);	%����

DeviceInfo�����e�G
winvideoinfo.DeviceInfo	//�d�ݩҦ��˸m����T
ans = 
1x2 struct array with fields:
    DefaultFormat
    DeviceFileSupported
    DeviceName
    DeviceID
    VideoInputConstructor
    VideoDeviceConstructor
    SupportedFormats
    
%�d��Device2����T�G	//�d�ݯS�w�˸m����T
device2 = winvideoinfo.DeviceInfo(2)
name2   = winvideoinfo.DeviceInfo(2).DeviceName
format2 = winvideoinfo.DeviceInfo(2).SupportedFormats
 




