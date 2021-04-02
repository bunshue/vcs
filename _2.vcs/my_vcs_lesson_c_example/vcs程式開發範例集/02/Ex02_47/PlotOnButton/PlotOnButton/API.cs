using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;
namespace Ex02_39
{
    class API
    {
        [DllImport("gdi32", EntryPoint = "StretchBlt")]
        public static extern int StretchBlt(int hdc, int x, int y, int nWidth, int nHeight, int hSrcDC, int xSrc, int ySrc, int nSrcWidth, int nSrcHeight, int dwRop);
        //       ���� 
        //�N�@�T��ϱq�@�ӳ]�Ƴ����ƻs��t�@�ӡC���M�ؼ�DC�ۤ��������ݮe�C�o�Ө�Ʒ|�b�]�Ƴ������w�q�@�ӥؼЯx�ΡA�æb��Ϥ��w�q�@�ӷ��Ϲ��C���x�η|�ھڻݭn�i����Y�A�H�K�P�ؼЯx�Ϊ��j�p�۲� 
        //��^�� 
        //Long�A�D�s��ܦ��\�A�s��ܥ��ѡC�|�]�mGetLastError 
        //�Ѽƪ� 
        //�Ѽ� �����λ��� 
        //hdc Long�A�ؼг]�Ƴ��� 
        //x,y Long�A�ؼЯx�Υ��W����x,y���СA�H�޿觤�Ъ�� 
        //nWidth,nHeight Long�A�ؼЯx�Ϊ��e�שM���סA�H�޿觤�Ъ�� 
        //hSrcDC Long�A���]�Ƴ����C�p���]�B�⥼���w�@�ӷ��A�h�o�ӰѼ������s 
        //xSrc,ySrc Long�A�η�DC���޿觤�Ъ�ܪ����x�Υ��W����m 
        //nSrcWidth,nSrcHeight Long�A���O���w���޿���]�H��DC����¦�^�ǿ骺�@�T�Ϲ����e�שM���סC�p�䤤���@�ӰѼƪ��Ÿ��]�����t���^�P�������ؼаѼƤ��šA��ϴN�|�b�������b�W�@�蹳�ഫ�B�z 
        //dwRop Long�A�ǿ�L�{���i�檺���]�B��C�p��l�ݩ���]�B�⪺�@�����A�N�ϥο�J�ؼ�DC����l 
        //���� 
        //�i��GetDeviceCaps��ƧP�_�S�w���]�Ƴ����O�_��������
        //���i��ܹ﷽��϶i��Ť��α���B�z�A����Ϥ]����O�@�ӹϤ����]�Ƴ���
        [DllImport("user32", EntryPoint = "FindWindow")]
        public static extern int FindWindow(string lpClassName, string String);
        //        ���� 
        //�M�䵡�f�C���Ĥ@�ӲŦX���w���󪺳��ŵ��f�]�bvb�̨ϥΡGFindWindow�̱`�����@�ӥγ~�O��oThunderRTMain�������õ��f���y�`�F�����O�Ҧ��B�椤vb����{�Ǫ��@�����C��o�y�`��A�i��api���GetWindowText���o�o�ӵ��f���W�١F�ӦW�]�O���ε{�Ǫ����D�^ 
        //��^�� 
        //Long�A��쵡�f���y�`�C�p�����۲ŵ��f�A�h��^�s�C�|�]�mGetLastError 
        //�Ѽƪ� 
        //�Ѽ� �����λ��� 
        //lpClassName String�A���V�]�t�F���f���W���Ť���]C�y���^�r�ꪺ���w�F�γ]���s�A��ܱ��������� 
        //lpWindowName String�A���V�]�t�F���f�奻�]�μ��ҡ^���Ť���]C�y���^�r�ꪺ���w�F�γ]���s�A��ܱ������󵡤f���D 
        //���� 
        //�ܤ֭n�D�P�ɫ����P���f�W�j���C���V�ۤv���ǳưѼƶǻ��@�ӹs�A��²�K����k�O�ǻ�vbNullString�`��

        //�ܨ� 
        //Dim hw&, cnt&
        //Dim rttitle As String * 256
        //hw& = FindWindow("ThunderRT5Main", vbNullString) ' ThunderRTMain under VB4
        //cnt = GetWindowText(hw&, rttitle, 255)
        //MsgBox Left$(rttitle, cnt), 0, "RTMain title" 
        //[DllImport("user32", EntryPoint = "FindWindow")]
        //public static extern int FindWindow(string lpClassName, string String);
        ////        ���� 
        //�b���f�C���M��P���w����۲Ū��Ĥ@�Ӥl���f 
        //��^�� 
        //Long�A��쪺���f���y�`�C�p�����۲ŵ��f�A�h��^�s�C�|�]�mGetLastError 
        //�Ѽƪ� 
        //�Ѽ� �����λ��� 
        //hWnd1 Long�A�b�䤤�d��l�������f�C�p�]���s�A��ܨϥήୱ���f�]�q�`�������ŵ��f���Q�{���O�ୱ���l���f�A�ҥH�]�|�復�̶i��d��^ 
        //hWnd2 Long�A�q�o�ӵ��f��}�l�d��C�o�˫K�i�Q�ι�FindWindowEx���h���եΧ��ŦX���󪺩Ҧ��l���f�C�p�]���s�A��ܱq�Ĥ@�Ӥl���f�}�l�j�� 
        //lpsz1 String�A���j�������W�C�s��ܩ��� 
        //lpsz2 String�A���j�������W�C�s��ܩ��� 

    }

}
