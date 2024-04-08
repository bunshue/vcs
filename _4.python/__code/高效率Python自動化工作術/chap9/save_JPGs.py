from pathlib import Path
from PIL import Image

#�i2. �]�w�����ε{����ܪ��r��j
infolder = "testfolder"
label1, value1 = "��s��Ƨ�", "outputfolder4"
extlist = ["*.jpg","*.png"]

#�i3.���: �x�spng�ɮסj
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)              #���J�Ϥ���
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #�إ���s��Ƨ�
        #-----------------------------------
        filename = Path(readfile).stem+".jpg"   #�إ��ɮצW��
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
          newimg = Image.new("RGB", img.size, "white")
          newimg.paste(img, mask=img.split()[3])  #�b�թ��I��ø�s�Ϥ�
          newimg.save(savepath, format="JPEG", quality=95)    #��s��JPG����
        elif img.format == "JPEG":
          img.save(savepath, format="JPEG", quality=95)   #��s��JPG����
        #-----------------------------------
        msg = "�b"+savefolder + "��s" + filename + "�F��C\n"
        return msg
    except:
        return readfile + "�G�{�����楢�ѡC"
#�i���: �B�z��Ƨ��������Ϥ��ɡj
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:                     #�H�h�Ӱ��ɦW�լd
        filelist = []
        for p in Path(infolder).glob(ext):  #�N�o�Ӹ�Ƨ����ɮ�
            filelist.append(str(p))         #�s�W�ܦC��
        for filename in sorted(filelist):   #�A���C���ɮױƧ�
            msg += savepng(filename, savefolder)
    return msg

msg = savefiles(infolder, value1)
