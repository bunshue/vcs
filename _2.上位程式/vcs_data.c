/**********************************************************
 * Filename	:	vcs_data.c
 * Description	:	vcs������ƻP���q�{��
 **********************************************************/


�o�˼g�]�i�H

            if (fileDialog.ShowDialog() == DialogResult.OK)
                pictureBox.ImageLocation = fileDialog.FileName;


����i���P�_
            if (pictureList.Visible) {
                pictureList.Visible = false;
                addButton.Visible = false;
                removeButton.Visible = false;
                setButton.Visible = false;
                intervalText.Visible = false;
            }
            else {
                pictureList.Visible = true;
                addButton.Visible = true;
                removeButton.Visible = true;
                setButton.Visible = true;
                intervalText.Visible = true;
            }


BinaryReader	�H�S�w�s�X�覡�� �G�i��   �Φ� Ū���ɮ�
BinaryWriter	�H�S�w�s�X�覡�� �G�i��   �Φ� �N��Ƽg�J�ɮ�
StreamReader	�H�S�w�s�X�覡�� �r����y �Φ� Ū���ɮ�
StreamWriter	�H�S�w�s�X�覡�� �r����y �Φ� �N��Ƽg�J�ɮ�

StreamReader����k�G
Read		���ɮפ�Ū���@�Ӧr���A�æ^�ǸӦr�����r���X(ascii��)�C
ReadLine	���ɮפ�Ū���@�C�r��A�H����Ÿ����r�굲���A�æ^�ǸӦr��C
ReadToEnd	�N�ɮפ�����r����Ū���A�å����H�r�ꫬ�A�^�ǡC
Close		�����ɮסA�øѰ��ɮת��g�J��w�A��K��L�{���ϥΡC

StreamWriter����k�G
Write		�N��Ƽg�J��w��(buffer)���A�i�����ǤJ�j��������ƫ��A�C
WriteLine	�N��Ƽg�J��w��(buffer)���A�æ۰ʴ���C
Flush		�N�w�Ĥ����ثe����Ƽg�J���ɮפ��C


StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default�ѨMŪ���@��s�X�ɮפ���r���ê����D




            string str = System.Windows.Forms.Application.StartupPath;
            richTextBox1.Text += "str = " + str + "\n";
            string str2 = str + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str2 = " + str2 + "\n";
            string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str3 = " + str3 + "\n";



MysonLink��comport�T���A��ctrl+H����text/hex mode




----------------vcs�W�� ST----------------






dddd	draw����
ffff	�ɮ׬����B��Ƨ�����
eeee	encoding
ssss	syntax
cccc	control	����



�¤�r �ɮת��g�J�PŪ�X
�G�i�� �ɮת��g�J�PŪ�X



�w�p�s�M�סG
vcs_MyPlayer
vcs_FolderFileName
vcs_MysonEdit

My�K����
My�p�@�a

MyNotepad


Ū�@��binary�ɡA�u�s�@�����A�F��cut���\��

�n�Ϊ��{���X���q


delay
draw
syntax	foreach


�n�ǳƪ�icon
�}�s�ɮסB�}���ɮסB�x�s�ɮסB�����ɮ�
�ƻs�B�K�W
�r���]�w�B�ﶵ�]�w�B���U�ﶵ


�D��Visual C# 2008�{���]�p�֬���




vcs

�~���귽��
	AGauge
	Digital Meter

�s�W�����
	�bA������A���Ƹ����ܦbB���

Network��
�˴������s�u�BIP����
WebBrower
�������ơB��r�B����

���X�Ҧ��ɦW�A�i�H����ɦW�A�o�˷�j�M�\��ΡA�M���ɮ׮e�q�̤j�̤p�ɮ�
�i�Ƨǧ_�H

�ɮ׳B�z
hexdump
cat
bin2hex
hex2bin

�s�@binary�ɤ��d��
�s�@text�ɤ��d��







vcs
3M�K����
�p��sinplot
�p��pwm generator


vcs

�̤p�ƮɡA�b�t�ΦC�W���

���ɦW	�����ɦW	��


vcs�p��P�_�쩳�OUSB1.1�٬OUSB2.0�BUSB3.0�H

vcs�p�󰵰ʺA�O����t�m�H

vcs�ؼСG

vcs�������G�U�ر��󪺨ϥ�
�e�����G	Draw�B�����B����B�b�Ϥ��W�e��		(�p�e�a)
�Ϥ����G	�Ϥ�Ū������B����B����		(ACDSee)
���T���G	1. ����mp3�Bwav				(Winamp)
		2. �B�z���ġBbeep
�v�����G	����v��				(PotPlayer)
�ɮ��`�����G
	1. �j�M�����ɦW
	2. �j�M�ɮ�
	3. �B�z�ɮסG
	3.1. �}��
	3.2. �R���B��W�B����
	3.3. �M��ۦP���ɮ�

�t�θ�T��





vcs �j��

�w�g���n��vcs�j���G
vcs_test_all_01_Richtextbox	��Wvcs_test_all_01_RichTextBox
vcs_test_all_02_String		�r��B�z��
vcs_test_all_03_Network
vcs_test_all_04_Font		�r����
vcs_test_all_06_DirectoryFile	�ɮפl���B�z		File Directory IO��	�ɮצs����	�ϥ�DirectoryInfo�PFileInfo
vcs_test_all_06_Drive		�Ϻ���			�ϥ�DriveInfo
vcs_test_all_06_System		Windows�t�θ�T��
vcs_test_all_08_Media		�v����
vcs_test_all_09_Form		���~�[��
vcs_test_all_10_Math		�ƾ���
vcs_test_all_11_Draw		�e����
vcs_test_all_12_Date		�ɶ��B�z��		DateTime


�y�k��				vcs_Syntax
������	�^��??	control?	���	vcs_test_all_00_Controls
�������B����ϥ���

�y�k�B�榡�B�B�B�B
���00123�B���0xabcd�B�B�B

Thread��

�r��B�z��
	//�N���r������
	hex = hex.Replace("#", "");

�禡�ϥ���

�~�[��
�C����

�ϥβ{����������	AGauge�BDigitalGauge


C# �Ұ����ε{���åB�ǤJ�Ѽ�
https://dotblogs.com.tw/atowngit/2009/12/26/12681

vcs���o�����ݩʡA�Ҧp�GFont�BSize�BBackColor�BForeColor








----------------vcs�W�� SP----------------




namespace �ŧi���O����
{
  class foo
  {
    public String strData;
    public int intData;
  }
}

namespace �ŧi���O����
{
  class Program
  {
    static void Main(string[] args)
    {
      foo obj1 = new foo();
      obj1.strData = "�r���Ƴ]�w";
      obj1.intData = 100;
      Console.WriteLine("foo ���O�� strData �����G" + obj1.strData);
      Console.WriteLine("foo ���O�� intData �����G" + obj1.intData);
      Console.Read();
    }
  }
}
----------------------
namespace �ݩʦ���
{
  class Program
  {
    static void Main(string[] args)
    {
      circle objC1 = new circle();
      Console.Write("�п�J�b�|��T�G");
      objC1.radius = float.Parse(Console.ReadLine());
      Console.WriteLine("�b�|�G" + objC1.radius);
      Console.Read(); //�Ȱ�
    }
  }
}


namespace �ݩʦ���
{
  class circle
  {
    private float r;
    public float radius
        {
            get
            {
                return r;
            }
            set
            {
                r = value;
            }
        }
  }
}

----------------------------
        string filename;
        StreamReader fileread;
        StreamWriter filewriter;

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = "c:\\"; //�]�w�w�]�ؿ�
            openFileDialog1.Filter = "�¤�r��(*.txt)|*.txt|�Ҧ��ɮ�(*.*)|*.*"; //�w�]�}�Ҫ��ɮ�����
            openFileDialog1.Title = "�}������"; //�]�w��ܤ�������D
            openFileDialog1.RestoreDirectory = true; //�]�w�O�_�b�������e�n�٭�ܥثe���ؿ�

            if (openFileDialog1.ShowDialog() == DialogResult.OK)  //���p���U�}�ҫ��s��
            {
                filename = openFileDialog1.FileName; //�]�w�ɮצW��
                fileread = new StreamReader(filename); //Ū���ɮ�
                textBox1.Text = fileread.ReadToEnd(); //���ɮץثe��mŪ���ɮק���
                fileread.Close(); //�N�ɮ�����
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            saveFileDialog1.InitialDirectory = "D:\\"; //�]�w�w�]�ؿ�
            saveFileDialog1.Filter = "�¤�r��(*.txt)|*.txt"; //�w�]���x�s���ɮ�����
            saveFileDialog1.RestoreDirectory = true; //�]�w�O�_�b�������e�n�٭�ܥثe���ؿ�
            saveFileDialog1.Title = "�s��"; //�]�w��ܤ�������D

            if (saveFileDialog1.ShowDialog() == DialogResult.OK ) //���p���U�x�s���s��
            {
                filename = saveFileDialog1.FileName; //�]�w�ɮצW��
                filewriter = new StreamWriter(filename, false);
                filewriter.Write(textBox1.Text); //�N��Ƭy�g�J���w���ɮפ�
                filewriter.Close(); //�����ɮ�
            }
        }

 ------------------



---------------------------------------------------------------



  namespace Exam2
{
  public class Bicycle
  {
    private string Color;
    private string Style;
    private int Price;

    public void GetData()
    {
        Console.Write("�п�J�C��G");
        Color = Console.ReadLine();
        Console.Write("�п�J�����G");
        Style = Console.ReadLine();
        Console.Write("�п�J����G");
        Price = int.Parse(Console.ReadLine());
    }

    public void DispData()
    {
        Console.WriteLine("�����C�⬰�G" + Color);
        Console.WriteLine("�����������G" + Style);
        Console.WriteLine("�������欰�G" + Price);
    }
  }


  public class RaceBike:Bicycle
  {
      private int Speed;

      public void GetSpeed()
      {
          GetData();
          Console.Write("��J�X�q�ܳt:");
          Speed = int.Parse(Console.ReadLine());
      }

      public void DispCarData()
      {
          DispData();
          Console.WriteLine("������" + Speed + "�q�ܳt��");
      }
  }

  class Program
  {
    static void Main(string[] args)
    {
        RaceBike MyCar = new RaceBike();
        MyCar.GetSpeed();
        MyCar.DispCarData();
        Console.ReadLine();
    }
  }
}


---------------------------------------------------------------

  class Hello
  {
    public void SayHello()
    {
      Console.WriteLine("Hello�IWorld�I");
    }
  }

  class Program
  {
    static void Main(string[] args)
    {
      Hello obj =new Hello();
        obj.SayHello();
        Console.Read(); //�Ȱ�
    }
  }





---------------------------------------------------------------





---------------------------------------------------------------







�����GKeyDown�PKeyPress���P�b��G
KeyDown�iť�\����(�pCtrl Alt F1....)
KeyPress�Oť��J����r(�Ʀr�B�r���ίS��Ÿ�)


private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
{
    if (!(e.KeyChar >= '0' && e.KeyChar <= '9'))
    {
        e.Handled = true;
    }
}
�����G�o�̪�textBox1�A�|�ư�0~9�H�~����r�A���y�ܻ��N�O�u��ܼƦr


vcs�P�I�sPotPlayer
��Command Line�I�sPotPlayer����@��
PotPlayerPortable.exe C:\______test_vcs_video\mmm.mp4

��Command Line�I�sPotPlayer����l�ؿ��������ɮ�
PotPlayerPortable.exe C:\______test_vcs_video

��Command Line�I�sPotPlayer����S�w�X���ɮסA�n�Τ޸���_�ӤΥΪŮ�j�}
PotPlayerPortable.exe "C:\______test_vcs_video\mmm.mp4" "C:\______test_vcs_video\video2.mpg"







using System;	//�ϥ�System�W�٪Ŷ�(namespace)


vcs��Unicode�s�X�t�ΡA�L�׬O����r�B�^��r���βŸ��A�C�Ӧr���Һ�O�@�Ӧr���A�b�O���餤�Ҧ�2���C


�����ƹ�Ĳ�o�ƥ󶶧ǡG
1. MouseDown
2. Click
3. MouseUp

�����ƹ�Ĳ�o�ƥ󶶧ǡG
1. MouseDown
2. Click
3. DoubleClick
4. MouseUp


c# WebBrowser Internet Explorer���O�X���~

�ϥ�WebBrowser.ScriptErrorsSuppressed �ݩ�
webBrowser.ScriptErrorsSuppressed = true;


���G
Size: ���j�p
ClientSize: �]�w�Ψ��o���u�@�ϰ쪺�j�p


c# form �� size �Mclientsize �p�� �����\��g�� 5

size�O�リwindow�����שM���סCclientsize�O�u�@�񪺇��שM���סA�h��border�M��_�w������

size�O�リ���^�j�p�Aclientsize�O�X�ؤj�p�A�]�N�O�G���f����슻��_�C

            int xx = this.ClientSize.Width;
            int yy = this.ClientSize.Height;
            label3.Text = "XX=" + xx.ToString() + " YY=" + yy.ToString();
            label5.Text = "W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString();
            //this.ClientSize.Width = 800;
            //this.ClientSize.Height = 600;
            this.ClientSize = new System.Drawing.Size(800, 600);


��Alt+x�i�H��������label���U�@��index���ءG
            label1.Text = "�m�W(&N)";
            label2.Text = "�q��(&T)";


text���
�@��Ū�@��A��ܦbrichtextbox/listview�ءA
[����r]<�j�M>
��<�j�M>��A���s���ˤ@���A�����[����r]�����N�����A��ܥX�ӡA����ɦW�P�e�q
�i�H�I��Ψt�ιw�]�{�����}



����ɡA�@�ߥ���r�ꪺ�ťթM�u�u���h���b����A�����A�A��쥻���r����ܥX�ӡA
�쥻���r��M�T���A�D�n�O�ɮפj�p

���ǳƨ���ɮסA�w�]�}���ɮ׭ӼƤ��@�ˡA�@��10�ӡB�@��1000�ӡA�ݽsĶ�X�Ӫ��{���j�p�t�h�֡C



����icon�ɮצ��L����A�Ҧp������jpg��W�A�O�_�bvcs�W�i�ΡC
---------------------------------------------------



----------------vcs�峹�@�j�� ST----------------


vcs code
http://www.java2s.com/Code/CSharp/Components/ScreencaptureDemo.htm

DotNet����p�����
http://pramaire.pixnet.net/blog/post/7988372

XYZ�����O��
http://xyz.cinc.biz/search/label/C%23?max-results=50

�����P��	�{�����O��
http://welkingunther.pixnet.net/blog

�E�p�� @ �j������
https://dotblogs.com.tw/yc421206/1


�·t�߱��P�޳N����
http://blog.xuite.net/chu.hsing/Think

�Q�S������
http://trufflepenne.blogspot.tw/


olivermode��������
http://olivermode.pixnet.net/blog



�ݬ�s�}��vcs�����G
https://dotblogs.com.tw/chou/archive/2009/04/12/7986.aspx


C# Examples
Best site for developers
http://csharpexamples.com/




vcs�о�youtube
https://www.youtube.com/user/LeftTechticle



vcs
http://jasonli13168.blogspot.tw/
http://jasonli13168.blogspot.tw/


vcs�о�
http://wang.mis.au.edu.tw/index.php/11-csharp

�p��� C# ���o�����Ҧ��� IP ��}
http://blog.miniasp.com/post/2007/12/02/How-to-get-all-ip-at-local-machine-using-c.aspx

�p��� C# �N��ƶץX�� Excel
http://blog.miniasp.com/post/2007/11/28/How-to-transfer-data-to-an-Excel-workbook-by-using-Visual-Studio-2005.aspx

���a
http://windechime.com/en/index.html

�b.NET���ާ@�ɮפΥؿ��̥D�n���OFile��Directory������O�A���bSystem.IO���R�W�Ŷ��U�C

http://einboch.pixnet.net/blog/post/266428691

need to check
http://cyfangnotepad.blogspot.tw/2013/08/cnet.html
http://cyfangnotepad.blogspot.tw/2013/04/cnet.html
http://cyfangnotepad.blogspot.tw/2013/02/cnet-ab.html

vcs
http://createps.pixnet.net/blog/category/1630969



C#
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553


��L����������

http://einboch.pixnet.net/blog

�K�O�q�l�ѡGC# �{���]�p
http://cs0.wikidot.com/

C# �{���ǲ� �t�C	30��
http://ithelp.ithome.com.tw/users/20023570/ironman/110

�{���y���оǻx
C �y���зǨ�Ʈw�������� - ctype.h isprint()
http://pydoing.blogspot.tw/2010/07/c-isprint.html

[C#]���^��j�ΊD�p�Z�A�����M���^��ҩ�j

�p��~�r������
https://dotblogs.com.tw/jeff-yeh/2010/11/08/19291


http://www.codeproject.com/kb/cs/


http://pydoing.blogspot.tw/2013/01/Perl-Tutorial.html
http://pydoing.blogspot.tw/2013/01/Perl-Guide.html

.Net ���Ѯa
https://dotblogs.com.tw/hung-chin/1

�ݽd�Ҿ�C#-02 switch�Bfor�Bforeach�y�k�о�
https://dotblogs.com.tw/hung-chin/2011/09/29/38211

Huan-Lin �ǲߵ��O
http://huan-lin.blogspot.com/

���M ���絧�O
http://lolikitty.pixnet.net/blog

Visual Studio �ֳt��
http://visualstudioshortcuts.com/


C# �j�������{��
�[�J�o�@��Y�i�j�������{�� :
System.Environment.Exit(System.Environment.ExitCode);


�ϥ�.Net Framework �GApplication.DoEvents( ) - �Ncpu��I���䥦���Φ�
�ϥ�.Net Framework �GSystem.Threading.Thread.Sleep - ���Ccpu loading

vcs course
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/ch5.pdf

C# ��X Excel
http://xyz.cinc.biz/2013/10/csharp-create-excel.html



c#:
[C#]�ϥ� DriveInfo ���O���o�Ϻи�T
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26665.aspx
[C#]�ϥ� Path ���O���o�ɮשΥؿ����|��T
http://www.dotblogs.com.tw/chou/archive/2011/05/30/26625.aspx
[C#]�N�{���[�J�k����
https://dotblogs.com.tw/chou/2011/04/17/22945
[C#]�ƻs�S�w���ɦW�ɮר���w��Ƨ�
https://dotblogs.com.tw/chou/2011/03/31/22186
[C#]�p��H�r���ܪ��ƾǹB�⦡���G
https://dotblogs.com.tw/chou/2010/12/03/19881
[C#]�ΦW���O
https://dotblogs.com.tw/chou/2010/08/29/17485
[VB6]�C�|�q���w�g�w�˪��r��
https://dotblogs.com.tw/chou/2010/05/27/15462
[C#][VB.NET]�����{������ܹ�ܮءA�ΥH�A���T�{�O�_����
https://dotblogs.com.tw/chou/2009/09/30/10849
[C#]���o�����ݤW�A���椤�� GUI ���������ε{��
https://dotblogs.com.tw/chou/2009/09/30/10848
[C#]�����O�_���������s��˸m���J�A�ϥ� WndProc ��k�P DriveInfo ���O
https://dotblogs.com.tw/chou/2009/06/25/8993
	[C#]���oCPU�ū׻P����
	https://dotblogs.com.tw/chou/2009/06/21/8927
[C#][VB.NET]�褸�����
https://dotblogs.com.tw/chou/2009/06/21/8925
C#�H��p�ޥ�
https://dotblogs.com.tw/chou/2009/04/12/7986
[C#]��MonthCalendar�Y�q����d���ܲ���
https://dotblogs.com.tw/chou/2009/04/11/7975
[C#]�N�Ʀr�e����0�A�ɨ��]�w������
https://dotblogs.com.tw/chou/2009/03/20/7574
[C#]�d�ߵw�гѾl�Ŷ�(�z�LWinAPI)
https://dotblogs.com.tw/chou/2009/03/11/7450
[C#]�p��F�������ܼƪ��\��
https://dotblogs.com.tw/chou/2009/03/11/7438
	[C#][VB.NET]���o�ثe�ù����ѪR��
	https://dotblogs.com.tw/chou/2009/03/08/7411
[C#]�h�ɮ׽ƻs���Ƨ����p�{��
https://dotblogs.com.tw/chou/2009/02/20/7247
[C#]����j���Y�p��A�����۪���ҩ�j
https://dotblogs.com.tw/chou/2009/02/19/7233
	[C#]���o�@�~�t�Ϊ���
	https://dotblogs.com.tw/chou/2009/02/18/7220
[C#][VB.NET]�d�ߧ@�~�t�ΩҦb���ϺЦ�m
https://dotblogs.com.tw/chou/2009/02/17/7213
[C#]�@�Ӥ������p�{��(�����O�P���󪺬�������)
https://dotblogs.com.tw/chou/2009/02/13/7139
[C#]��J�ͤ��P�y
https://dotblogs.com.tw/chou/2009/02/04/7024




vcs�Ʀr�榡
http://blog.xuite.net/linriva/blog/43023872-%5BC%23%5D+.net+tostring+format+%E6%A0%BC%E5%BC%8F%E8%AA%AA%E6%98%8E+~+%E8%BD%89%E8%B2%BC

�p��Nform1���ȶǦ�form2 form3�ϥ�
http://a7419.pixnet.net/blog/post/39233835


some vcs example
http://www.openwinforms.com/




�{�ǃ��G�@�ǆG���D���^��D��
http://www.voidcn.com/blog/zzzili/article/p-592079.html

vcs��T
http://csharp.net-informations.com/

127�� .NET �{���]�p�J��(�ϥ� C#) �����Z
http://www.csie.ntu.edu.tw/~r93057/summer/cs127/



[C#]�ϥ� Directory ���O���o�ؿ���������P�ɶ�
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26664.aspx

C# Date() ����P�ɶ�
http://www.eion.com.tw/Blogger/?Pid=1150

�ɶ��榡�Τ�k�B��
https://dotblogs.com.tw/skyline0217/2011/01/26/21047

[C#]�w���榡����r����^ DateTime
https://dotblogs.com.tw/chou/2010/12/25/20373

C# ����P�ɶ�
http://shioulo.16mb.com/node/686


C# �p����o��� DateTime ����������Ѽ�
http://blog.miniasp.com/post/2008/01/22/Find-the-difference-between-two-DateTime.aspx



�ɶ��榡�ഫ
https://dotblogs.com.tw/grepu9/2013/03/14/96613


c#�ɶ�����	TimeSpan ���c
https://msdn.microsoft.com/zh-tw/library/system.timespan.aspx


[c#]�p���Ӯɶ� ���j��� �ΤѼ�
http://blog.xuite.net/yan.kee/CSharp/27113202

�ɶ��榡�Τ�k�B��
https://dotblogs.com.tw/skyline0217/archive/2011/01/26/21047.aspx



WMI Code Creator�۰ʲ���WMI���{���X
https://dotblogs.com.tw/jeff-yeh/archive/2009/11/11/11530.aspx

�p��� C# ���o CPU �Ǹ�
http://blog.miniasp.com/post/2007/12/29/How-to-get-CPU-ID-by-using-CSharp.aspx

C# ���o �w�о� �Ǹ� ( ���z / �޿� �Ϻ�)
https://dotblogs.com.tw/powerhammer/2008/03/24/2077
C# ���o �w�о� �Ǹ� ( ���z / �޿� �Ϻ�)
https://dotblogs.com.tw/powerhammer/2008/03/24/2142

�p����o �w�� �� �D���O �Ǹ�
http://wushinetlife.blogspot.tw/2010/07/blog-post_15.html

Ū���w�ЧǸ��B�D���O�Ǹ��BMAC��}(�ϥ� WMI)
https://lawrencetech.blogspot.tw/2009/03/mac-wmi.html

C# �z�L WMI ���o �w�ЧǸ� ( ���z / �޿� �Ϻ�)
http://blog.xuite.net/danny72.chen/blog/22988547-C%23+%E9%80%8F%E9%81%8E+WMI+%E5%8F%96%E5%BE%97+%E7%A1%AC%E7%A2%9F%E5%BA%8F%E8%99%9F+(+%E7%89%A9%E7%90%86+%2F+%E9%82%8F%E8%BC%AF+%E7%A3%81%E7%A2%9F)+





vcs sample code.
http://kilean.pixnet.net/blog/post/143351802-my-c%23-windows-form-lesson

�оǺ����G
Hans-Petter Halvorsen
http://home.hit.no/~hansha/

C# �y����MD5��
http://www.cnblogs.com/anjou/archive/2008/08/05/1261290.html

Drawing Shapes
http://www.yevol.com/en/vcsharp/applicationdesign/lesson13.htm

http://fecbob.pixnet.net/blog/category/1813376/3
http://fecbob.pixnet.net/blog/post/38132415
http://fecbob.pixnet.net/blog/category/1813350
http://fecbob.pixnet.net/blog/post/38968537

http://fecbob.pixnet.net/blog/post/38121425-c%23%E8%A3%A1%E7%9A%84%E6%96%B9%E5%90%91%E9%8D%B5%E6%B6%88%E6%81%AF%E6%8D%95%E7%8D%B2-


http://readily-notes.blogspot.tw/search/label/C%23%20%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%AD%86%E8%A8%98
http://johnson560.pixnet.net/blog/post/313121832-c%23-%E8%A6%96%E7%AA%97%E7%A8%8B%E5%BC%8F%E7%AF%84%E4%BE%8B--%E9%8D%B5%E7%9B%A4%E4%BA%8B%E4%BB%B6
http://beckhamnaing.blogspot.tw/2013/12/functionc.html
https://hk.saowen.com/a/f166a8b85c97eaadf6488c1a88c8f5f990e32c42857bda8d4a848a2dbc4681c5
https://hk.saowen.com/a/ef3176c7e08764bf94d96f6a9710d7c9d37cc8d476b69226197fc0427ad71fcd
http://jian-zhoung.blogspot.tw/2012/07/c.html
https://coolong124220.nidbox.com/diary/read/8045380

http://www.dxper.net/thread-562-1-1.html

http://chcooboo.blogspot.tw/2011/04/blog-post_25.html


[C#] ²��ýX�ഫ
https://dotblogs.com.tw/chou/2013/06/26/106113


VITO �U �ǲߵ��O	�s�X�P�ѽX
http://vito-note.blogspot.tw/2012/01/blog-post_86.html

�ͽ�Unicode�s�X
http://flykof.pixnet.net/blog/post/23502355?pixfrom=related

EmguCV���o��v���v��	//try �@�U Julia
https://gnehcic.azurewebsites.net/category/c/page/6/


[C#] �ɮ�Ū�g
http://blog.xuite.net/autosun/study/32576568-[C%23]+%E6%AA%94%E6%A1%88%E8%AE%80%E5%AF%AB


https://msdn.microsoft.com/zh-tw/library/system.io.streamreader%28v=vs.110%29.aspx

https://www.tutorialspoint.com/
https://www.tutorialspoint.com/csharp/

�ܦh���
https://doc.lagout.org/Others/

vcs
http://archive.oreilly.com/oreillyschool/courses/csharp2/



.Net ���Ѯa
https://dotblogs.com.tw/hung-chin/1

https://dotblogs.com.tw/alonstar
http://www.csharp-examples.net/
http://www.csharp-examples.net/file-creation-modification-time/
http://www.csharp-examples.net/file-creation-modification-time/




mediainfo�����G

MediaInfo��ۤj��
http://www.cnblogs.com/royzou/archive/2011/09/06/mediainfo_parameter.html
http://www.cnblogs.com/royzou/archive/2011/09/06/csharp_call_mediainfo.html







SerialPort ���O
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.aspx


SerialPort.ReadExisting ��k ()
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.readexisting.aspx

https://msdn.microsoft.com/en-us/library/windows/apps/xaml/windows.devices.usb.aspx

���Linstalldate
https://social.msdn.microsoft.com/Forums/en-US/f2eba6ca-e66a-4659-9b96-7e99838a9518/how-to-convert-the-weird-date-and-time-to-normal-date-and-time?forum=csharplanguage

Win32_DiskDrive class
https://msdn.microsoft.com/en-us/library/aa394132(v=vs.85).aspx
https://msdn.microsoft.com/en-us/library/aa394132(v=VS.85).aspx

�p��G���o�����ɮסB��Ƨ��M�Ϻо�����T (C# �{���]�p��U)
https://msdn.microsoft.com/zh-tw/library/6yk7a1b0.aspx






----------------vcs�峹�@�j�� SP----------------


#region �۩w�q���W��
�����[�J�A���{���X
#endregion

openFileDialog1.Multiselect = false;	//���
openFileDialog1.Multiselect = true;	//���\�h���ɮ�

// �����
ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
Thread serverthread = new Thread(serverThreadStart);
serverthread.Start();


DateTime.Parse�{�o���榡�G

1992�~5��9��
5��9��1992�~
3/11/2006 9:15:30 AM
3/11/2006 9:15:30
3/11/2006 9:15
3/11/2006
2006/3/11
2018/2/21 07:54�U��

----------------�n�Ϊ��{�����q ST----------------

DateTime start_time = DateTime.Now;
richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss") + "\n";
string filename = "Stage_Speed_Current." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
richTextBox1.Text += "�إ߮ɶ��ɮסG" + filename + "\n";


int screenWidth = Screen.PrimaryScreen.Bounds.Width;
int screenHeight = Screen.PrimaryScreen.Bounds.Height;
MessageBox.Show("�ù��ѪR�׬� " + screenWidth.ToString() + "*" + screenHeight.ToString());


private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    switch (e.KeyCode)   //�ھ�e.KeyCode���O����
    {
        case Keys.Up:
            richTextBox1.Text += "�W";
            break;
        case Keys.Down:
            richTextBox1.Text += "�U";
            break;
        case Keys.Left:
            richTextBox1.Text += "��";
            break;
        case Keys.Right:
            richTextBox1.Text += "�k";
            break;
        case Keys.PageUp:
            richTextBox1.Text += "PageUp";
            break;
        case Keys.PageDown:
            richTextBox1.Text += "PageDown";
            break;
        default:
            richTextBox1.Text += "KeyCode: " + e.KeyCode.ToString() + "\n";
            break;
    }
}

textBox1.Text = value.ToString("D8");
8��A�������D�s

�Q���i����ܡA�������|�ɹs
richTextBox1.Text += i.ToString("X2") + "\n";

�Q�i����ܡA�������|�ɹs
richTextBox1.Text += i.ToString("D2") + "\n";

#region/#endregion �i�H�bVisual Studio�{���X�s�边���j���\��ɡA�i�H�i�}�κP�|���{���X�϶�
²�檺���A�N�O�i�H��\�h���{���X�϶� (��b�P�@�Ӱϰ�(region)��)�A���{����n�z�Ѥκ޲z...

try-catch-finally���Ϊk
try
{
	//�{���D����ϩΥi��o�Ϳ��~���a��
}
catch (Exception ex)
{
	//�ҥ~���B�z��k�A�p�q�Xĵ�i
}
finally
{
	//���׬O�_�o�ͨҥ~�ƥ󳣷|���檺�϶��A�i�ٲ�
}

    try
    {   //�i��|���Ϳ��~���{���Ϭq
        DateTime dt = DateTime.Parse(textBox1.Text);
        richTextBox1.Text += dt.ToString() + "\n";
    }
    catch (Exception ex)
    {   //�w�q���Ϳ��~�ɪ��ҥ~�B�z�{���X
        MessageBox.Show(ex.Message);
    }
    finally
    {
        //�@�w�|�Q���檺�{���Ϭq
        richTextBox1.Text += "DateTime.Parse����\n";
    }


private void delay(int delay)
{
    Application.DoEvents();         //����Y�@�ƥ�A�H�F�쩵��ĪG�C
    for (int j = 0; j < delay; j++)
        System.Threading.Thread.Sleep(1);
}


try
{   //�i��|���Ϳ��~���{���Ϭq
	serialPort1.Open();
}
catch (Exception ex)
{   //�w�q���Ϳ��~�ɪ��ҥ~�B�z�{���X
	MessageBox.Show(ex.Message);
}
finally
{
	//�@�w�|�Q���檺�{���Ϭq
	if (serialPort1.IsOpen)
	{
	    //MessageBox.Show("�w�g�s�W" + serialPort1.PortName);
	}
	else
	    MessageBox.Show(language9[SelectedLanguage, 1]);
	}
}
----------------�n�Ϊ��{�����q SP----------------




----------------MSDN ST----------------

DockStyle �C�|
Bottom	The control's bottom edge is docked to the bottom of its containing control.
Fill	All the control's edges are docked to the all edges of its containing control and sized appropriately.
Left	The control's left edge is docked to the left edge of its containing control.
None	The control is not docked.
Right	The control's right edge is docked to the right edge of its containing control.
Top	The control's top edge is docked to the top of its containing control.


PictureBoxSizeMode �C�|	ex:pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
Normal		�v���|��b���W���� PictureBox�C �p�G�W�L�A�v���w���� PictureBox ���]�t�b�C
StretchImage	�����v�� PictureBox �������Y�p�H�t�X�j�p PictureBox�C
AutoSize	PictureBox ���j�p�վ㬰�۷�󥦩ҥ]�t���M�����j�p�C
CenterImage	�p�G�v����ܦb���� PictureBox �j��M���C �p�G�v���j�� PictureBox, �A�Ϥ��|��m�b���� PictureBox �M���ť~�t�C
Zoom		�v�����j�p�|�W�[�δ�ֺ����j�p��ҡC


PictureBox.Load ��k

�ҥ~���p
InvalidOperationException	url �� null �ΪŦr��C
WebException			url �����O�L�k�s�������W���v���C
ArgumentException		url �O�����O�v�����ɮסC
FileNotFoundException		url �ѦҤ��s�b���ɮסC

"InvalidOperationException=" + InvalidOperationException.
WebException
ArgumentException
FileNotFoundException

FormStartPosition �C�|
CenterParent		���|�m���������d�򤺡C
CenterScreen		���|�����b�ثe����ܡA�åB�㦳���w����檺�j�p�C
Manual			��檺��m�� Location �ݩʡC
WindowsDefaultBounds	����� Windows �w�]��m�A�åB�㦳���M�� Windows �w�]���ɭ��C
WindowsDefaultLocation	����� Windows �w�]��m�A�åB�㦳���w����檺�j�p�C

ex:
// Set the start position of the form to the center of the screen.
this.StartPosition = FormStartPosition.CenterScreen;



----------------MSDN SP----------------




eeee
�x�W�������`�Ϊ��s�X��BIG5�BUTF-8
���䪺�����`��HK-SCS�BUTF-8
�j���������`��GBK�BUTF-8
�饻�������`��JIS�BUTF-8



Filter�g�k�G
�ﶵ�W��1|�L�o�W�h1|�ﶵ�W��2|�L�o�W�h2|...
ex:
"JPG��|*.jpg|GIF��|*.gif|�Ҧ��ɮ�|*.*"






��ܮت�Filter�PFilterIndex�G

Filter  �n�b��ܤ������ܪ��ɿz�ﾹ�A�Ҧp�A"��r��(*.txt)|*.txt|�Ҧ���(*.*)||*.*"
FilterIndex  �b��ܤ������ܪ��ɿz�ﾹ�����ޡA�p�G��Ĥ@���N�]��1

// �[�J�ɮ׹L�o����
openFileDialog1.Filter = "save files (*.sav)|*.sav|All files (*.*)|*.*";
openFileDialog1.Filter = "Image Files(*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF";
openFileDialog1.Filter = "�Ϥ���|*.jpg|*.bmp|*.png|�Ҧ���|*.*";
openFileDialog1.Filter = "*.jpg;*.png;*.bmp|*.jpg;*.png;*.bmp";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";

vcs�p�󭭩w�U����׮榡
openFileDialog1.Filter = "exe files (*.exe)|*.exe|All files (*.*)|*.*";     //���w�ɮ׮榡
openFileDialog1.Filter = "Excel ����ï (*.xlsx)|*.xlsx|Excel 97-2003 (*.xls)|*.xls|��r�� (Tab �r�����j) (*.txt)|*.txt";


openFileDialog1.Filter="��r��|*.*|C#���|*.cs|�Ҧ���|*.*";
openFileDialog1.FilterIndex=2;

eeee
��: Encoding.GetEncoding(950) == Encoding.GetEncoding("big5")


protected override void OnKeyPress(KeyPressEventArgs e)
{
    base.OnKeyPress(e);

    if (ReadOnly) return; //��Ū���B�z
    if (_maxByteLength == 0) return; //�S�]�wMaxByteLength���B�z
    if (char.IsControl(e.KeyChar)) return; //Backspace, Enter...�������䤣�B�z

    int textByteLength = Encoding.GetEncoding(950).GetByteCount(Text + e.KeyChar.ToString()); //���o�쥻�r��M�s�r��ۥ[�᪺Byte����
    int selectTextByteLength = Encoding.GetEncoding(950).GetByteCount(SelectedText); //���o����r�ꪺByte����, ����r��N�|�Q���N
    if (textByteLength - selectTextByteLength > _maxByteLength) e.Handled = true; //�۴����׭Y�j��]�w��, �h���e�X�Ӧr��
}

private void button1_Click(object sender, EventArgs e)
{
    //byte[] byteStr = Encoding.Default.GetBytes(textBox1.Text); //�ϥ�Default��k�b�D����t�ΤU�i��|�����D, �P��Bibby����
    byte[] byteStr = Encoding.GetEncoding("big5").GetBytes(textBox1.Text); //��string�ରbyte
    label1.Text = byteStr.Length.ToString(); //��byte������, ����r�N�|��2�X�F
}


����ico
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" href="/favicon.ico" type="image/x-icon">


�O�Jyoutube
<iframe width="560" height="315" src="//www.youtube.com/embed/oPQKtwC1mh0" frameborder="0" allowfullscreen></iframe>


ffff
c# txt �N��r���[�ܲ{�����ɮ�
using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"C:\Users\Public\TestFolder\WriteLines2.txt", true))
{
    file.WriteLine("Fourth line");
}

cccc
ASP.NET C# �p��CheckListBox �Q����Ӽ�
ArrayList values =newArrayList();

for(int counter =0; counter <list.Items.Count; counter++)
{
	if(list.Items[counter].Selected)
	{
	   values.Add(list.Items[counter].Value);
	}
}

ffff

Listing all files in a specified folder

//FIND ALL FILES IN FOLDER
System.IO.DirectoryInfo dir = new System.IO.DirectoryInfo(Location);
foreach (System.IO.FileInfo f in dir.GetFiles("*.*"))
   {
   //LOAD FILES
   ListViewItem lSingleItem = listView1.Items.Add(f.Name);
   //SUB ITEMS
   lSingleItem.SubItems.Add(Convert.ToString(f.Length));
   lSingleItem.SubItems.Add(f.Extension);
   }

Listing all folders in a specified folder
//FIND ALL FOLDERS IN FOLDER
TreeNode Main =  treeView1.Nodes.Add("Folders in: " + Location);
Main.Tag = "";
   foreach (System.IO.DirectoryInfo g in dir.GetDirectories())
       {
       //LOAD FOLDERS
       TreeNode MainNext = Main.Nodes.Add(g.FullName);
       MainNext.Tag = (g.FullName);
       }


C# ���O�G�ϥ� var �ŧi���t���O
C# 3.0 �W�[�F var ����r�A�A�i�H�Υ��ӫŧi���t���O�A�Ҧp�G

int i = 10;
var j = 10;


�o��檺�@�Χ����ۦP�A�s�sĶ�X�Ӫ� IL code �]���@�ӼҼˡG


�����U���ɮ״��պ��}
http://old.dylanbeattie.net/cheatsheets/dot_net_string_format_cheat_sheet.pdf

���P�q���ݨ쪺�w�ЧǸ��O�_�ۦP�H

�P�@�ӵw�СB�H���ХΤ��P��PC��Ū�A�O�_�|Ū��@�˪��Ǹ��H
vcs�j�M�Ҧ��w�СA����w�СA��ܸӵw�и�T

�ϥ�Oscar
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

�ϥ�Romeo
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

�ϥ�Julia
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

���صw��
InterfaceType: IDE
Description: Local Fixed Disk
MediaType: Fixed hard disk media

�H����
InterfaceType: USB
Description: Removable Disk
MediaType: Removable Media

USB�w��
InterfaceType: USB
Description: Local Fixed Disk
MediaType: External hard disk media

�ҥH�A�O�� MediaType �����H���Щ�USB�w��

eeee
C# GB2312�MUTF8���H
public string GB2312ToUtf8(string gb2312String)
{
    Encoding fromEncoding = Encoding.GetEncoding("gb2312");
    Encoding toEncoding = Encoding.UTF8;
    return EncodingConvert(gb2312String, fromEncoding, toEncoding);
}

public string Utf8ToGB2312(string utf8String)
{
    Encoding fromEncoding = Encoding.UTF8;
    Encoding toEncoding = Encoding.GetEncoding("gb2312");
    return EncodingConvert(utf8String, fromEncoding, toEncoding);
}

public string EncodingConvert(string fromString, Encoding fromEncoding, Encoding toEncoding)
{
    byte[] fromBytes = fromEncoding.GetBytes(fromString);
    byte[] toBytes = Encoding.Convert(fromEncoding, toEncoding, fromBytes);

    string toString = toEncoding.GetString(toBytes);
    return toString;
}

C# �ͦ��r�Ŧꪺ Checksum
private static string CheckSum(string message)
{
    char[] chars = message.ToCharArray();
    int checksum = 0;
    for (int i = 0; i < chars.Length; i++)
    {
        checksum += (int)chars[i];
    }
    checksum = (~checksum & 0xFFFF) + 0x0001;
    return Convert.ToString(checksum, 16).ToUpper();
}

�Ҧp�A�r�Ŧꡧ1234567890�� �� CheckSum �o�G��FDF3��

C# CRC8�ՍJ
http://www.cnblogs.com/anjou/archive/2011/10/19/2217783.html




cccc

ToolTip�g�k�G
private void Form1_Load(object sender, EventArgs e)
{
    //���[�JToolTip���
    //toolTip1.SetToolTip(����W��, "�n���ܪ��r");
    toolTip1.SetToolTip(button19, "��Button�[�J�ƹ����L�h�ɪ����ܤ�r");
}

ToolTip���ܱ���`�Ϊ���k�G
        public Form1()
        {
            InitializeComponent();
            this.Width = 850;
            this.Height = 600;
            richTextBox2.Focus();
            toolTip1.SetToolTip(button12, "XXXXXXXXXXXXXXXXXX");
        }




----------------���OVCS ST----------------

----------------���OVCS SP----------------




----------------BLDC ST----------------



�T�w�[�@��toggle GPIO
comparator triggers
PWM ����

FW �O CW 546231		CCW 645132

�H�n�Ӭ�CMPBCD�����ǡBCMP trigger PWM�B�o�i���ǡB��ݤW�@�t�U���t��V




�@����button�A
�C�����o�@�өR�O���U��A
�C���U�쳣toggle gpio�A
�ݬݳ̧֤����O�h�֡C

�U��@���o�R�O�X�ӡA�W���Y�u��rx buffer�g���A�ݬݳֳ̧t�׬O�h�֡H


���㪩
USE_FULL

²�䪩
USE_COMPACT
��putty���MMysonLink��

putty�@��VR�ձ�
MysonLink�䴩VR�ձ��B�ΤW�챱��

����FULL��COMPACT�A����NORMAL_MODE��VR_MODE�AMysonLink�R�O�@�ӡA�@�߰���VR

_ALIVE���D�W�ǧ��㪩��²�䪩
_FULL		0
_COMPACT	1

�Y�O²�䪩�A�h�@�ߥ�VR����
�Y�O���㪩�A�h�@�ߥ�MysonLink����

���i�H��MysonLink�ӧ���




�W��get��ơA
���Fget��Atextbox���ܦ�disabled�άO�ܦ�A
���o���ƫ�A�A��_���`�C
�Y��Ƥ����T�A�]�k�q���C
�h�@��get all����C

�[�@��message text box�A�γ\�Mtarget�q�ΡC

mysonlink���s��ΡA
�u�n�������t�Bduty�BVR�Bcontrol�N�n�C

acceleration�令�U�Ԧ����
0 very slow	200
1 slow
2 medium	100
3 fast
4 very fast	35
�γ\�]�i�H�ζ�Ʀr�C�åΨ�ءC

slow modify�A�n���n��check box�ӿ�ܡC

vcs mysonlink
������W�߳]�w
�]�wmax speed���ܻ���A�令��Enter�N�]�w�C

�յ۬ۮe��@��C



MysonLink
�w�骩��
Hardware Name & Version
Firmware Name & Version
Software Name & Version

Current Sense Resistor
PGA gain
VBUS ratio
�]Gate Driver Polarity
�W�U�u��dead Time
�Ͳ��Ѽ�
Hardware Serial
Hardware Date
Customer	//�Ȥ᪺�W�r
FW Serial
�ե�
Calibrate VBUS
Calibrate Current
Firmware Update
�]Baud rate, 9600 default


²�䪩 Mysonlink�U��u�n �W��duty�B��t�BVR�A�A�h�Ұ�
CW/CCW

tabControl�[�GRecord���BADC���խ��B�ۦ���v�ոխ�
Record��t�Bduty�A�Mtarget_speed�Breal_speed�Bmax_speed�Bmin_speed�e�b�@�_�C


��F�����
²�䪩�{���A�q�S��Mysonlink�[�WMysonlink
�[�J�ɮסGSetup.h�BCS8963_BLDC.h�BCS8963_Compact_Function.h
KeilC�M�ץ[�JCS8963_MysonLink.c�BCS8963_Compact_Function.c

�O�_�令�w�]�N�Oslow modify

MysonLink�[�@��log�@�ߥ��Lhex�榡�A��MyLink�Ρ��

mysonlink +
ADC�BCMP�BDAC���q����^�Ʀr�B�Ʀr�A��^�q���A���ĵL����i��k
MysonLink
+ putty mode
+ hex mode
+ ����script


�W��}���ɶ�
�W��}���֭p�ɶ�
�U��}���֭p�ɶ�
���F�B��ɶ�
�U��{���Ұʮɶ�
�U��{���ϥβֿn�ɶ�



----------------BLDC SP----------------


�ǳƦU�ؽs�X���ɮ�

���L���B²���B�������@�˪��r��

���ֵ��H

�O�_�O�H��installDate�d�ҵ{�����L�A��console mode�N�i�H��ܡH

http://jjnnykimo.pixnet.net/blog/post/21585509





byte[] msg = Encoding.ASCII.GetBytes("ABCD");
byte[] b;
b = System.Text.Encoding.UTF8.GetBytes("Hello Server");
b = System.Text.Encoding.UTF8.GetBytes("Hi");
b = System.Text.Encoding.UTF8.GetBytes("�o�O " + myPublicIP + " ��� : " + i++);
b = System.Text.Encoding.UTF8.GetBytes("�o�O'���A��'�^�Ǫ��T�� ~ " + i++);

string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref ipep));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));



http://k-k-club.blogspot.tw/search/label/C%23?updated-max=2013-03-18T22:18:00-07:00&max-results=20&start=2&by-date=false


MD5 SHA
https://dotblogs.com.tw/jeff-yeh/2009/02/23/7269



Ū�JBIG5�s�X���ɮצ�UTF8�s�X���r��


byte[] big5Bytes = null;

string FilePath = Server.MapPath("~/txt/test.txt");

using (System.IO.FileStream fs = new System.IO.FileStream(FilePath, System.IO.FileMode.Open))
 {
    //Ūbig5�s�Xbytes
    big5Bytes = new byte[fs.Length];
    fs.Read(big5Bytes, 0, (int)fs.Length);
 }

//�Nbig5�নutf8�s�X��bytes
byte[] utf8Bytes = System.Text.Encoding.Convert(System.Text.Encoding.GetEncoding("BIG5"), System.Text.Encoding.UTF8, big5Bytes);

//�Nutf8 bytes�নutf8�r��
System.Text.UTF8Encoding encUtf8 = new System.Text.UTF8Encoding();

string utf8Str = encUtf8.GetString(utf8Bytes);

Response.Write(utf8Str);

�p�󰵦r��s�X���ʧ@,BIG5 to UTF8

byte[] b=Encoding.Default.GetBytes(a);//�N�r���ରbyte[]
MessageBox.Show(Encoding.Default.GetString(b));//������X�᪺�r��,�����T�����.
byte[] c = Encoding.Convert(Encoding.Default, Encoding.UTF8, b);//�i����X,�Ѽ�1,�ӷ��s�X,�ѼƤG,�ؼнs�X,�ѼƤT,���s�X�ܼ�
MessageBox.Show(Encoding.UTF8.GetString(c));//����ରUTF8��,���ॿ�T����ܦr��


UTF8��BIG5
    public static string ConvertUTF8toBIG5(string strInput)
    {
        byte[] strut8 = System.Text.Encoding.Unicode.GetBytes(strInput);
        byte[] strbig5 = System.Text.Encoding.Convert(System.Text.Encoding.Unicode, System.Text.Encoding.Default, strut8);
        return System.Text.Encoding.Default.GetString(strbig5);
    }


RichTextBox���G�S����k�����P�϶���r��ܤ��P�r���B�C��

Convert UTF-8 to Chinese Simplified (GB2312)

byte[] bytes = Encoding.GetEncoding("gb2312").GetBytes(text);



MD5������Omessage-digest algorithm 5(�H��-�K�n��k)


using System.Security.Cryptography;



result: ed076287532e86365e841e92bfc50d8c
  ! is: ed076287532e86365e841e92bfc50d8c.

// This code example produces the following output:
//
// The MD5 hash of Hello World! is: ed076287532e86365e841e92bfc50d8c.
// Verifying the hash...


�L����i�줧���


���L�i�వ����#define USE_HD�Y�ϥΦۤv���Ҧ��ѼƭȡA�o�˥i�H���Χ�Ӧh


progress bar�i�_���h���C��H�ݦ��Lidx�����H	�䤣��A���G�u���e����B�I����G���C��i�աC


vcs �p�󰵨�button������ܥ\��H

�p��q�{�������richtextbox���r���j�p
	richTextBox1.Text += "�r��j�p�G" + richTextBox1.Font.Size.ToString();

�����{������ܮءA�n����MegaDownloader
�}�ɦs�ɪ���ܮءA�n����UltraEdit

�}�ұM�סG
�}��*.sln	//Microsoft Visual Studio Solution

C# / C Sharp examples (example source code) Organized by topic

http://www.java2s.com/Code/CSharp/CatalogCSharp.htm
vcs�о�
https://www.youtube.com/user/LeftTechticle

vcs
http://lolikitty.pixnet.net/blog/post/46745588

1. ����`��/�M�ץk��/�[�J/�s�W����/�귽�ɡA����Resource1.resx�ɮסC
2. �IResource1.resx�A��v���A��[�J�귽/�[�J�{���ɮסA�������v����
3. �ϥΡG
	pictureBox1.Image = Resource1.green_ball_icon;
	pictureBox1.Image = Resource1.red_ball_icon;

            //�榡�ƿ�X
            double num =1234.5678;
            richTextBox1.Text += num.ToString("00000000") + "\n";
            richTextBox1.Text += num.ToString("########") + "\n";
            richTextBox1.Text += num.ToString("########.00000000") + "\n";
            richTextBox1.Text += num.ToString("#,#") + "\n";
            richTextBox1.Text += num.ToString("#,#,") + "\n";

C#�}�o���1200�Ҥ��p����x

vcs search c# dclock aclock digital clock analog clock
�w�]button��size�A��CorelDraw�e�ϮɡA�ݬO�_�i�H����n�j�p�C

vcs
����d�ҡG
2016/11/19 21:55	//���Ʃ�
2017/2/8 01:36�W��	//UltraEdit
IMG_20170214_102309.jpg	//����Ӭ��ɮ�
putty log:
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 09:59:03 =~=~=~=~=~=~=~=~=~=~=~=
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 10:39:05 =~=~=~=~=~=~=~=~=~=~=~=



vcs
�����]�k��Ū��excel�ɮ�


�ɮ׸�ƱƧ�
�Y�ɮפ��s�b�A�s�y�@���ɮסA���e���G

elephant.txt	895		2013/5/10
lion.txt	250		2010/01/31
dog		20		2008/12/05



�]�w�C�⪺��k�G
1. HTML
	button87.BackColor = ColorTranslator.FromHtml("#FF0000");
2. ARGB
	button87.BackColor = Color.FromArgb(255, 255, 0, 255);
3. �W��
	button87.BackColor = System.Drawing.Color.FromName("Red");

���C��W�٧��ARGB

	Color test = System.Drawing.Color.FromName("Control");
	byte a = test.A;
	byte r = test.R;
	byte g = test.G;
	byte b = test.B;
	richTextBox1.Text += "A = " + a.ToString() + "\n";
	richTextBox1.Text += "R = " + r.ToString() + "\n";
	richTextBox1.Text += "G = " + g.ToString() + "\n";
	richTextBox1.Text += "B = " + b.ToString() + "\n";

	richTextBox1.BackColor = Color.FromArgb(255,212,208,200);	//Control����X

test_digital_display
4��A�e���ɹs
            clock++;
            digitalDisplayControl1.DigitText = clock.ToString("D4");

            panel1.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, hScrollBar2.Value, hScrollBar3.Value);
            panel2.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, 0, 0);
            panel3.BackColor = Color.FromArgb(hScrollBar4.Value, 0, hScrollBar2.Value, 0);
            panel4.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, hScrollBar3.Value);
            panel5.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, 0);




            int a = 0;
            for (a = 0; a < 255; a ++)
            {
                richTextBox1.Text = a.ToString();
                panel1.BackColor = Color.FromArgb(a, 128, 128, 128);
                Application.DoEvents();         //����Y�@�ƥ�A�H�F�쩵��ĪG�C
                for (int j = 0; j < 100; j++)
                    System.Threading.Thread.Sleep(1);
            }

this.tabPage8_SVPWM.Parent = null;	���ä���

if (tabControl1.SelectedIndex == 7)
{
	banner01.Visible = false;
	banner02.Visible = false;
}


AutoSize��True
AutoSizeMode��GrowAndShrink

                    else if (input[1] == _TIMER1)
                    {
                        timer1_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer1 TH TL = " + Convert.ToString(timer1_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox��ܰT���۰ʱ��ʡA��̫ܳ�@��
                    }
textbox���L�i���������C��H	���G�䤣��

vcs
�P�@��textbox�Brichtextbox���A�C�⤣�@�ˡA�o���i��ܡH

���U���� (Modifier Key) (SHIFT�BCTRL �M ALT)

List view�[�W�i���ϥΪ̿�J��r�A��ܦr���Y�i��ܥX�ӡC

���ӵe�����ƹ���m

        private void Form1_Load(object sender, EventArgs e)
        {
            //�}�l��ť�ƹ���m
            System.Threading.ThreadPool.QueueUserWorkItem(new System.Threading.WaitCallback(AutoGetCursorPosition), null);
        }

        void AutoGetCursorPosition(object obj)
        {
            Point pt = new Point();

            while (true)
            {
                Win32Native.Methods.GetCursorPos(out pt);
                try
                {
                    SetText(this.label1, "�ƹ���m : ( " + pt.X + " , " + pt.Y + " )" );
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace.ToString());
                    break;
                }

                System.Threading.Thread.Sleep(50);
            }
        }

range 1 �� 60%
range 2 �� 20%
range 3 �� 20%

BaseArcRadius		�D�n���b�|

RangeInnerRadius	�������b�|
RangeOuterRadius	�����~�b�|

ScaleLinesMajorInnerRadius	�D��פ��b�|
ScaleLinesMajorOuterRadius	�D��ץ~�b�|

ScaleLinesInterInnerRadius	�ƨ�פ��b�|
ScaleLinesInterOuterRadius	�ƨ�ץ~�b�|

ScaleLinesMinorInnerRadius	�Ө�פ��b�|
ScaleLinesMinorOuterRadius	�Ө�ץ~�b�|

ScaleNumberRadius		��r�Z���b�|



AGauge�ѹw�]�ȩ�j 1.5 ���A�ç�����ɳ]�w�G

�k����]�w
BaseArcStart		135	135	�D�n���b�|�A�}�l���˨���
BaseArcSweep		270	270	�D�n���b�|�A�`�@���˫׼�
MinValue		-100	0	�̤p��
MaxValue		400	3000	�̤j��
BaseArcRadius		80	120	�D�n���b�|

ScaleLinesMajorInnerRadius	70	105	�D��פ��b�|
ScaleLinesMajorOuterRadius	80	120	�D��ץ~�b�|
ScaleLinesMajorStepValue	50	300

ScaleLinesInterInnerRadius	73	109	�ƨ�פ��b�|
ScaleLinesInterOuterRadius	80	120	�ƨ�ץ~�b�|

ScaleLinesMinorInnerRadius	75	112	�Ө�פ��b�|
ScaleLinesMinorOuterRadius	80	120	�Ө�ץ~�b�|

ScaleNumberRadius		95	142	��r�Z���b�|

Range_Idx		0	1	2	��0���]�w
RangeEnabled		true	true	true
RangeColor		��	��	��	�����C��
RangeStartValue		0	2000	2500	�����_�l��
RangeEndValue		2000	2500	3000	����������
RangeInnerRadius(70)	105	105	105	�������b�|
RangeOuterRadius(80)	120	120	120	�����~�b�|



�A�վ� CapsText ��r�P��mCapPosition
�A�վ� Center ��m	�令(160,160)





�q�H��ĳ

��s���A
�����s���A

vcs �i�_���W�U��ӥ[��t�H����VCS����W�U��
�]�wmax speed�ɡA��enter�Y�M�ΡC����VCS����Enter��


vcs DigitalDisplayControl �Ʀ�Ʀr���
�ݭn���G
A1Panel.cs
A1Panel.Designer.cs
DigitalDisplayControl.cs
DigitalDisplayControl.designer.cs
A1PanelGraphics.cs
Globals.cs
6���ɮ�
����`��/�[�J/�{������ ��A1Panel.cs�BDigitalDisplayControl.cs�BA1PanelGraphics.cs�BGlobals.cs
�sĶ��A�u��c�N�|��A1Panel�BDigitalDisplayControl�i�ΡC

vcs AGuage
�ݭn�� AGauge.cs �BAGauge.Designer.cs ����ɮ�
����`��/�[�J/�{������ ��AGauge.cs
�sĶ��A�u��c�N�|��AGuage�i�ΡC


 �䤤�ASystem.Environment.SystemDirectory�N�OWindow.System32����m�C

�P�z�N�i�H�I�s�ܦh�t�Τ��ؤu���o~

�����ۤv�g��LUI�\��]���e���A��Ψt�Τ��ط�M�O�̦n���I

�ҥH�u�n�b��J��(TextBox)��Click�ƥ�[�J�o�@��A�N����Ĳ���ù��ϥο�J�\���o~

vcs
�p�U�C�d�ҩҥܡA�z�����N #define ���ܵ���b�ɮת����ݡC
#define DEBUG
//#define TRACE
#undef TRACE

using System;

public class TestDefine
{
    static void Main()
    {
#if (DEBUG)
        Console.WriteLine("Debugging is enabled.");
#endif

#if (TRACE)
     Console.WriteLine("Tracing is enabled.");
#endif
    }
}



//���o�Ҧ��Ϻо���DriveInfo���O
DriveInfo[] ListDrivesInfo = DriveInfo.GetDrives();

DriveType �C�|����
�R�W�Ŷ�:   System.IO

�����W��	�y�z
CDRom		���о��A�Ҧp CD �� DVD-ROM�C
Fixed		�T�w���ϺСC
Network		�����Ϻо��C
NoRootDirectory	���ϺШS���ڥؿ��C
Ram		RAM �ϺСC
Removable	������s��˸m�A�Ҧp�n�о��� USB �ְ{�Ϻо��C
Unknown		�Ϻ����������C

System.IO �R�W�Ŷ��G
Directory
DirectoryInfo
DriveInfo
File
FileInfo
FileSystemInfo


google  serialPort1.ReadExisting() 0x3f

http://stackoverflow.com/questions/13980631/0xff-becomes-0x3f

serialPort1.ReadExisting()�O�b�C������ߤW�ݨ� SerialPort ���H���y�M�r�J�G�L�񤤩Ҧ��ߧY�i�Ϊ��r��C
�q�P�O�ϥ�ASCIIEncoding�A�����C���覡�����0~0x7F���}���ȡA�p�G�ȶW�X7F�A�шC��3F�A�ҥH0x88he 0xB5�@���F0x3F,

SerialPort���󪺄����p�ʄ��m�otrue

�U��^ACK�A�u�n��2����0x20�אּ0x02�Y�i�C��L�ѼƤ@�ˡC

textBox1.ScrollBars = ScrollBars.Vertical;
textBox1.SelectionStart = textBox1.Text.Length;
textBox1.ScrollToCaret();

C# TextBox �p��۰ʱ��ʨ쩳��
�i�H�z�L SelectionStart �ݩʳ]�w��r����������r���_�I�A�M��A�z�L ScrollToCaret ��k�N��������e���ʨ�ثe���J������m
C# ��������ɡA�X�{�T�������A�T�{�O�_�������
��������ɡA�X�{�T�������A�T�{�O�_�������
��������ɡA�X�{�T�������A�T�{�O�_�������
protected override void WndProc(ref Message m)
{
	const int WM_SYSCOMMAND = 0x0112;
	const int SC_CLOSE = 0xF060;
	if (m.Msg == WM_SYSCOMMAND && (int)m.WParam == SC_CLOSE)
	{
		// ���MessageBox
		DialogResult Result = MessageBox.Show("�T�w�������", "���T��", MessageBoxButtons.YesNo);
		if (Result == System.Windows.Forms.DialogResult.Yes)
		{
			// ����Form
			this.Close();
		}
		else
		{
			return;
		}
	}
	base.WndProc(ref m);
}

���o��C���m
���o�Ҧ��q���ǦC��W��
�b C# ���A�Ӧp��g�{�����o�Ҧ��q���ǦC��W��
�o�ɭԥi�H�ϥ�SerialPort.GetPortNames ��k�A�\��N�O�ΨӨ��o�ثe�q���ǦC��W�٪��}�C
�q�T��W�٥i�q�t�εn�����o (�Ҧp�A�b Windows 98 ���Ҥ��A�o����T��� HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM ��)�C
�p�G�n�����]�t�L�ɩΤ����T����ơA�h GetPortNames ��k�|�Ǧ^�����T����ơC

this.combobox1.Items.AddRange(System.IO.Ports.SerialPort.GetPortNames());


[C#] �p��]�w�����ù��Ҧ�

�n�N�����]�w�����ù��Ҧ��A�D�n����ӳ���
1. �����L�ؽu
2. �����j�p����ù��j�p

�b .NET �� Windows Form ���A�u�ݭn�z�L²�檺�]�w�Y�i�F��o�ӮĪG�A
1. Form.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None; //�]�w���L�ؽu
2. Form.WindowState = FormWindowState.Maximized; // �����]�w���̤j��

�w�]����s���A�A�i����������s���A(�Yenable/disable timer1)


header	MYSON
pole_pair
max_speed
min_speed
normal_speed
normal_duty
max_current
oc_en
lock_en


�Ǹ�
�w���T
�w�骩��
�}���֭p�ɶ�
�������X


IndexOf()	//���o�Ĥ@�ӲŦX���w�r�ꪺ���ަ�m
�^��-1�A�N��䤣��C

Substring(m,n)	//���o�r�ꤤ���l�r��A�q��m���}�l�A���Xn���C

�ݬݷj�M"\t"���^�ǭȡA���M�䤣�즳�L���P�H�I�H�I

lion	mouse	cat	dog	elephant	eagle	pig	horse

        \t����m
t1	t2	rowdata
0	4	lion
5	10	mouse
11	14	cat
15	18	dog
19	27	elephant
28	33	eagle
34	37	pig
?	?	horse


38	43	horse


t1=�_�l
t2-t1 = ����
Substring(t1, t2 - t1) // �qt1�}�l�A��(t2-t1)�����





vcs

�d�ҥ[��������
TextBox�[multiline
combobox�[�d��
�[comport scan

�ˬd�X�ʾ��e�q.csproj
�ˬd�X�ʾ��e�q
DateFunction.csproj

http://ocean2002n.pixnet.net/blog/post/91605623-[c%23]-richtextbox-%E9%A1%AF%E7%A4%BA%E8%A8%8A%E6%81%AF%E8%87%AA%E5%8B%95%E6%8D%B2%E5%8B%95%EF%BC%8C%E9%A1%AF%E7%A4%BA%E6%9C%80%E5%BE%8C%E4%B8%80

http://www.coctec.com/docs/linux/show-post-56595.html

Ū�ɮסA�¤�r�ɡA��tab�Ϲj

CopyLotFiles.csproj



----------------vcs �Ȧs�� ST----------------

MyClock
�n�D�G

�Q�i����G�i��
Console.WriteLine(Convert.ToString(123, 2));
�Q�i����K�i��
Console.WriteLine(Convert.ToString(123, 8));
�Q�i����Q���i��
Console.WriteLine(Convert.ToString(123, 16));

�G�i����Q�i��
Console.WriteLine(Convert.ToInt32("100111101", 2));
�K�i����Q�i��
Console.WriteLine(Convert.ToInt32("123", 8));
�Q���i����Q�i��
Console.WriteLine(Convert.ToInt32("FF", 16));


----------------vcs �Ȧs�� SP----------------







----------------csharp vcs visual c# 2008 ST----------------

�P�@��textbox�Brichtextbox���A��r�C�⤣�ˡA���G���ӥi��	richtextbox�i�H���ܳ����C��
button�i�H�Ϥ������u���ܡH
button�ण��令��Ϊ����s�H
���GConsole.Write���g�k�A�brichtextbox�����Ӥ���ΡC

�p���ƹ��k��ƥ�H
�p���ƹ��u���ƥ�H



�[�d�ҡG

1. �q�{���������ܤ���~�[�G�j�p�B�r���B��m�B�B�B�B�B�B


���é���ܪ���G
            button8.Visible = true;
            button9.Visible = false;
            button10.Visible = true;

            richTextBox1.Visible = false;
            richTextBox2.Visible = true;
            richTextBox3.Visible = false;

Ū����ƩίB�I��
            value = int.Parse(richTextBox1.Text);
            value = float.Parse(richTextBox1.Text);
            value = double.Parse(richTextBox1.Text)
            DateTime dt = DateTime.Parse(richTextBox1.Text);	//���



�@��vcs�{���p�󪾹D�ۤv���L�Q�I�s�L�H	�ݨӥi�H���������

�Y�O��error�A���ӬO�C��timer���_���ˬd�@�U�A��error�n�W�ǡCSend_Error_Speed_Cmd(ERROR_number);

[C#] delegate(�e��)

Thread.Sleep ��ƨӨϵ{�����ݤ@�q�ɶ�
Thread.Sleep(0) ��ܱ��_0�@��A�A�i��ı�o�S�@��
MSDN�������G���w�s (0) �H���������_���u�{�H�Ϩ�L���ݽu�{�������C
Thread.Sleep(0) �ëD�O�u���n�u�{����0�@��A�N�q�b��o���ե�Thread.Sleep(0)����e�u�{�T�ꪺ�Q�ᵲ�F�@�U�A����L�u�{�����|�u������C  Thread.Sleep(0) �O�A���u�{�Ȯɩ��cpu�A�]�N�O����@�ǥ��Ϊ��ɶ�������L�u�{�ζi�{�ϥΡA�N�۷��@������ʧ@�C

�ӤH��ĳ�G�p�G���n���{��loading�ӭ� ����ĳ�[�J Thread.Sleep(0) �A���H���յ��G�[�J Thread.Sleep(1) �|�n�ܦh
�ҥH��ĳ�ϥ� Thread.Sleep(1) �C


�ϥΤ�k�G
�[�J using System.Threading;
Thread.Sleep(�@�ӼƦr);

Ehu vcs
�W�ǥثeHall���A�B���򪺡B��@���B����C
�W�ǥثeVR���A�B���򪺡B��@���B����C

�ҰʮɡA�Τ���[90�ױҰʡA�]�O�ӿ�k
�W���PID���U��

�����r
�r����ΡGConsolas
Border Style ��� Fixed 3D
�@��TextBox��FixedSingle

�w�Х����H�����ɮרt�αM�βV�X�d��

�p��}�Ҥ@�ӷs��form�A�M���ۤv��form�屼�C
	����Fortior�����IC�A�M����X�ާ@�����C

�p�󰵤@�Ӿx���{��

�p��O���W��}���ɶ��B�p��O���U��}���ɶ�
��6257�W��{���O�p���s�t�ήɶ����H�����d�ҡC�T�����O�@�O��򰵪��H

�p�󰵨�h���y�t�\��C��������^��y�t�C�ï�O�Ф��e���]�w�C

��l�ƪ��ɭԡA�]�w�y�t�C

�p��O�ШîM�Τ��e���]�w�H

����x�βզX��ctrl+Q�A���}�{��

GUI��Reset�A�ݤU�즳�S�������A�h���X���A�ݬݬO���O���������A
�Y���ɭԤU��S�^���A��ܳq�H���}�A�n��CPU�ɯߡC

�Y�Υ��j��RS232��USB�˸m�A�n�`�NRXD���O���S���G�_�ӡC
�ڳo��|�J�쪬�p�A�쥻RXD���G�A���L�����W�q��ARXD�N�����F�C�o�˴N����q�H�F�C
�ҥH�A�ڥثe�٬O��RS232���j���O�C

�w�]��VR mode�A����VR���O�C

��W����U�R�O�Ӫ��ɭԡA�N������GUI mode�A�q��VR���@�ΡA���쭫�s�}������C

�x�s�̪�X�Q��ADC���G�C

FormBorderStyle	��FixedSingle�A��Form���i�Ԥj�Ԥp

vcs�n�T��Form�̤j�ơA�n��򰵡H

���G�t�I�{���G��r�Bg�Bb�Bw�Bk�BESC�B�B�B
�ҰʮɧY�����ù��A�Ϊ̡A������������C

�ι��Ч�Label����r���_�ӡA�|Ĳ�o����ƹ��ƥ�H


����int.parse�٦�����H	float.Parse�Bdouble.Parse�BDateTime.Parse�BIPAddress.Parse

listBox�d�ҡG
private void Form1_Load(object sender, System.EventArgs e)
{
	string[] funcStr = {"�ɮ�","�s��","�˵�","�M��","�ظm","����","�u��","����","����"};
	foreach(string str in funcStr)
		allLB.Items.Add(str);
}

vcs �i�_Ū�JExcel�ɮ�

List.Sort() �� �Ƨ�T
List.Find() �� ��X�@��T
List.FindAll() ����X�h��T
List.Exist() ���P�_T�O�_�s�b

using�Ϊk�G C# �{���]�p�j�q�ϥΩR�W�Ŷ�����]����ӡC
�Ĥ@�A.NET Framework �|�ϥΩR�W�Ŷ���´��h�����O�C
�ĤG�A�ŧi�z�ۤv���R�W�Ŷ��A�N���U��b���j�����{���]�p�M�פ��������O�M��k�W�٪��d��C


vcs + CS8963 ���G
�T�ιq��

����

�x��
�üƨ��W�r
�~�N
�q��r��Ū��ƨå��L

good avs�����
�m�W	���	�^��	�X��	�{�~	�X�D	�ްh	���



���O�K�ŤU���@�˪��˼ƭp��
���OBitComet�� �ﶵ�B��ťport�@�k�C
���O�۰������{��
���O�l�ؿ����X�ɮצW�ٵ{��

����UI����ɮסA����A��binary��asc�A�i�H��winmerge������ΡC
�Φp�Phj-split�A��join�A
�Φp�P �ؿ��U�ɦW��X�¤�r�{��
�Φp�P UltraEdit���Q���i����ܼҦ�

�p�󰵨�Ū�gIC���Ȧs���A�z�LI2C�άOUART��Ū�g�H

�R���ƪ��Ǹ���G
�s���G413 02/08 21:21


vcs�d�ҡG
 1. �����ﴫ��
 2. �ū׹ﴫ��B�[������B��g���ꭱ�n�p��
 3. �ֵ����s��ܡA������ܦbtextBox�W
 4. Ū�@�ֵ��ɮסA��ܥX��(Ū�@�ɮסA��textBox��ܥX��)
 6. �Z���ɵ{�{���B�Y���Өƥ�Z���X�~�X��X��X�Q�X���X��C
 7. �b���K�X���T�{�\��
 8. ����@256���ɮסA�ѥXbinary�����ܥX�ӡA������ŪEDID��ơC
 9. �������ɮסA�ä���O�_�ۦP�C

���D�G
1. textBox�i�_������ܡH

----------------csharp vcs visual c# 2008 SP----------------


vcs�ؼСG
CPU-Z�Bpicpick�Bfile copy�Bfile compare�Bfile check(MD5�BSHA1)
hjsplit








�@�@Visual C#�O�L�n���q���X���U�@�N�{�Ƕ}�o�y���C
�L���Ȩ㦳Visual C++�\��j�j���S�I�A�S�㦳Visual Basic��²��A���W�⪺�S�I�C�ҥH�@�g���X�A�N����F�s�j�{�Ƕ}�o�H�����w��C

Visual C#�MVisual C++���@�ө��㪺�ϧO�b��AVisual C#�����O�S�����w���A��Visual C++�o�O�ۨ��N�a�����w�C

Visual C#���M�S�����w�A���@��.Net�ج[�����@�ӤQ�����n���}�o�y���C�L�i�H�ϥ�.Net�ج[���Ѫ��@�ӳq�Ϊ��n��}�o�]--.Net FrameWork SDK�C
�o�ӳn��}�o�]�i�H���OVisual C#�\�઺�����AVisual C#�N�O�q�L�L��{�F�ۨ��L�k��{���ܦh�\��C



����N�O�Ӥ���Visual C#�p��Q�γo�ӳn��}�o�]�ӵo�e�q�l�l�󪺡C
�@�@�@�D�n��}�o�M�B�檺���ҳ]�m�G
�@�@I > .�����t��2000�A�Ⱦ���
�@�@II > ..Net FrameWork SDK Beta 2��
�@�@III > .���}"����O"�A�i�J"�K�[�M�R���{��"�A�M��A�I��"�K�[/�R��Windows�ե�"�A�N�i�H�ݨ��H�U�ɭ��G



















----------------syntax �y�k ST----------------


�}�C�ŧi

�}�C�ŧi�d��
	int[] A = new int[5];
	int[] B = new int[] { 1, 2, 3, 4, 5 };
	int[] C = { 1, 3, 5, 7, 9 };
	int[,] D = new int[3, 3];
	int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
	int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
	int[, ,] G = new int[3, 4, 5];
	String[,] language = new string[3, 6] { { "����1", "����2", "����3", "����4", "����5", "����6" }, { "²��1", "²��2", "²��3", "²��4", "²��5", "²��6" }, { "�^�y1", "�^�y2", "�^�y3", "�^�y4", "�^�y5", "�^�y6" } };
	Point[] pt = new Point[360];    //�@���}�C����360��Point

�y�k
��ƫ��O[ ]   �}�C�W�� =  new  ��ƫ��O[�}�C�j�p];

�@���}�C�Ϊk�G
int[] myArray = new int[10];
string[] studentName = new string[100];
int[] a = new int[5] {0,1,2,3,4};
Point[] pt = new Point[360];    //�@���}�C����360��Point

�G���}�C�Ϊk�G
int[,] b = new int[2,3];
int[,] c = new int[2,3] {{1,2,3},{4,5,6}};
int[,] myArray = new int[2,3] {{1,2,3},{4,5,6}};

vcs�ŧi�G
      char[] cbuffer = new char[256];
      byte[] RecvBytes = new byte[256];


console mode�y�k:

Console.WriteLine("����ܼ� {0}: ",timeBirth);
Console.WriteLine("NanaoSeconds: {0}", nanoseconds);
Console.Read(); //�Ȱ�

�r��ŧi�G
string[] A = new string[10];
string Temp = "";
string D1, D2 = "", D3;
D1 = textBox1.Text;
string[] Stu_Name = { "�i�T", "���|", "����", "����" };
string[] Stu_Name = { "�i�T", "���|", "����", "����" };

vcs�ŧi�}�C
int[] x = {0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600};
int[] y = {200, 328, 396, 373, 268, 131, 26,  3, 71, 200, 328, 396, 373, 268, 131, 26};

�@���}�C�ŧi�G
int[] A = new int[6];
int[] A = new int[10];
int[] A = { 60, 70, 80, 85, 90, 100 };
int[] Stu_Sum = new int[4];         //�ǥ��`���Z
int[] Stu_Average = new int[4];     //�ǥͥ������Z
int[] Subject_Sum = new int[5];     //����`���Z
int[] Subjcet_Average = new int[5]; //��إ������Z
Point[] pt = new Point[360];    //�@���}�C����360��Point

�G���}�C�ŧi�G
int[,] Stu_Sum = new int[3, 4];         //�ǥ��`���Z
int[,] Stu_Average = new int[3, 4];     //�ǥͥ������Z
int[,] Subject_Sum = new int[3, 5];     //����`���Z
int[,] Subjcet_Average = new int[3, 5]; //��إ������Z
int[,] Score = new int[,] { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 100 } };

�T���}�C�ŧi�G

int[, ,] Score = { { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 99 } }, { { 77, 88, 66, 77, 66 }, { 65, 66, 88, 55, 77 }, { 70, 88, 56, 88, 88 }, { 80, 90, 95, 99, 99 } }, { { 55, 67, 56, 98, 67 }, { 66, 69, 76, 66, 78 }, { 77, 89, 88, 77, 77 }, { 88, 89, 99, 97, 88 } } };

�üơG
Random r = new Random();
Number = r.Next();		//����   >=0   ���üƭ�
Number = r.Next(101);		//����   0~101 ���üƭ�
Number = r.Next(25, 101);	//����  25~100 ���üƭ�
Number = r.NextDouble();	//���� 0.0~1.0 ���üƭ�

Number = r.Next(1,7);	//����  1~6 ����ƶüƭȡA�Y��l�ΡC




List�Ϊk�G	���I���O���Ϋŧi���ת��}�C(Array)

// �ŧimyIntLists ��List
// �H�UList �̬�int ���A
List<int> myIntLists = new List<int>();

// �ŧimyStringLists ��List
// �H�UList �̬�string ���A
List<string> myStringLists = new List<string>();

// �bList �̷s�Wint ���
myIntLists.Add(123456);

// �bList �̷s�Wstring �r��
myStringLists.Add("�j�a�n!");

// �i��foreach ���XList �̪���
foreach(string myStringList in myStringLists)
{
        Console.WriteLine(myStringList);
}
// ���X��@��List �̪��ȡA�p�P�}�C(Array)�Ϊk
// 123456
myIntLists[0];

// �j�a�n!
myStringLists[0];

// �o��List �̪��`��
myIntLists.Count;
myStringLists.Count;





�r��}�C���g�k�G
	string[] atoms = { "���~�y", "�����y", "�d�Ϯy", "�����y", "���l�y", "���ɮy", "��l�y", "�B�k�y", "�ѯ��y", "���Ȯy", "�g��y", "�]�~�y" };
	string ret = string.Empty;

�r�ꪺ�g�k�G
String[] Day = new string[] { "�P����", "�P���@", "�P���G", "�P���T", "�P���|", "�P����", "�P����" };
string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

DialogResult myResult = MessageBox.Show
("�A�n��O�٬O�_?", "��ܦb�u�X�����W�����r"
, MessageBoxButtons.YesNo, MessageBoxIcon.Question);

MessageBoxButtons�M MessageBoxIcon�o�Ӹ̭����ܦh�C�|�A�i�ۤv��ۤv�n��

if ( myResult  == DialogResult.Yes)
{
   //���F�O
}
else if (myResult== DialogResult.No)
{
   //���F�_
}

	 //not vcs
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1");
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 1",MessageBoxButtons::OK);
	 MessageBox::Show("Yuki Oh's Picture3","Title Here 2",MessageBoxButtons::OKCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 3",MessageBoxButtons::AbortRetryIgnore);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 4",MessageBoxButtons::RetryCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 5",MessageBoxButtons::YesNoCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 6",MessageBoxButtons::YesNo);

	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Error);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Question);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Information);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Warning);




MessageBox.Show ��k���ϥ�
http://blog.xuite.net/chu.hsing/Think/29672699-MessageBox.Show+%E6%96%B9%E6%B3%95%E7%9A%84%E4%BD%BF%E7%94%A8

MessageBox.Show("�x�s�ɮ�OK, �ɦW�G" + filename4, "�x�s�ɮ״���", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);



int[,] myArray = new int[2,3] {{1,2,3},{4,5,6}};
String[] funcStr = {"�ɮ�","�s��","�˵�","�M��","�ظm","����","�u��","����","����"};


String[] animal_name = {"��","��","��","��"};



String[,] animal_name2 = {{"��","��","��","��"},{"mouse","bull","tiger","rabbit"},{"Mickey","Benny","Eric","Cony"}};

��	mouse	Mickey	�̩_	1928/11/18
��	bull	Benny	�Z��	2000/8/14
��	tiger	Eric	����	1993/12/13
��	rabbit	Cony	�ߨ�	2013/4/17



----------------syntax �y�k SP----------------



----------------Process.Start() ST----------------


System.Diagnostics.Process.Start(currentPath);

Process.Start(@"C:\WINDOWS\system32\calc.exe");


Process ���O���ѹ糧���M���ݳB�z�� (Process) ���s���A�����z����ҰʩM������t�γB�z�ǡC�]���A�i�H�z�L Process.Start �ӳB�z���w�����A�ҥH�A�p�G�b Start ���ѼƤ������@�ӹq�l�H�c���W�s���A�N�i�H�Ұʨt�Τ��w�]���q�l�l��B�z�{���C�p�U�G

System.Diagnostics.Process.Start("mailto:abc@hotmail.com");




C# Process.Start()��k�H��
http://blog.csdn.net/chen_zw/article/details/7896264

[C#]�Q�� Process �Ӱ���䥦�~���{��

C# �}�ҥ~���ɮ�
using System.Diagnostics;
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
using System.Diagnostics;
Process.Start("\\Program Files\\TransData2.exe","");

System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/notepad.exe");
notepad.exe	�O�ƥ�

C# �}�Ұ�����
System.Diagnostics.Process.Start("notepad.exe"); // �O�ƥ�
System.Diagnostics.Process.Start("calc.exe");    // �p��L
System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");

calc.exe	�p��L
cmd.exe		command line
mspaint.exe	�p�e�a
notepad.exe	�O�ƥ�
osk.exe		�ù��p��L
write.exe	WordPad

vcs�i�_�}���ɮ��`�ޡH ����360��U�L�޲z�{���C
visual c# �}���ɮ��`��

C# �}�ҥ~���ɮ�
�Х��פJ�Gusing System.Diagnostics;
�g�k�@�G
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
�g�k�G�G
ProcessStartInfo open = new ProcessStartInfo ();
open.FileName = "GodHand3D.exe"; // �ɮצW��
open.WorkingDirectory = @"C:\Users\Est\Desktop\GodHand3D"; // ��Ƨ����|
Process.Start (open);


�}�ҵ{��
Process.Start(@oFD.FileName);
Process.Start(@ezisp_path);

�}�Һ����s��
Process.Start("http://www.foo.com");


C# ����~��exe
using System.Diagnostics;
ProcessStartInfo Info = new ProcessStartInfo();
Info.FileName = "xxx.exe"; //���檺�ɮצW��
Info.WorkingDirectory = @"C:\xxx\xxx"; //�ɮשҦb���ؿ�
Process.Start(Info);



System.Diagnostics.Process.Start(); �వ���\�O�H���D�n���H�U�L���\��G
1�B���{�Y���α��I�}�]�ɵ��^�C
2�B�w�쥴�{�Y�����؉��C
3�B���{�t�i�S����H�A�p������O�����C
(1)
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            process.StartInfo.FileName = "firefox.exe";   //firefox
            process.StartInfo.Arguments = "http://www.google.com";	//���}
            process.Start();
(2)
            System.Diagnostics.ProcessStartInfo processStartInfo = new System.Diagnostics.ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //�ɮ��`��
            processStartInfo.Arguments = @"F:\";	 //��m
            System.Diagnostics.Process.Start(processStartInfo);
(3)
	    System.Diagnostics.Process.Start(@"D:\Program Files\Tencent\QQ\Bin\QQ.exe");  //�����`�Υ��{���
(4)
	    System.Diagnostics.Process.Start("explorer.exe", "D:\\Readme.txt");   //�������{���Readme.txt

----------------Process.Start() SP----------------








----------------Dialog ST----------------

            // �ŧi OpenFileDialog ����A�åB��Ҥ�
            OpenFileDialog OFD = new OpenFileDialog();

Dialog
OpenFileDialog	���}����ܤ��
SaveFileDialog	�O�s�ɹ��
FolderBrowserDialog
FontDialog	�r���ܤ��
ColorDialog	�C���ܤ��



1�B OpenFileDialog������H�U���ݩ�

InitialDirectory  ��ܤ������l�ؿ�
Filter  �n�b��ܤ������ܪ��ɿz�ﾹ�A�Ҧp�A"��r��(*.txt)|*.txt|�Ҧ���(*.*)||*.*"
FilterIndex  �b��ܤ������ܪ��ɿz�ﾹ�����ޡA�p�G��Ĥ@���N�]��1
RestoreDirectory  �����ܤ���b�������e�O�_��_�ثe���ؿ�
FileName  �Ĥ@�Ӧb��ܤ������ܪ��ɩγ̫�@�ӿ������
Title  �N��ܦb��ܤ�����D�C�����r��
AddExtension  �O�_�۰ʲK�[�q�{���ɦW
CheckPathExists


�b��ܤ����^���e�A�ˬd���w���|�O�_�s�b

DefaultExt  �q�{���ɦW
DereferenceLinks  �b�q��ܤ����^�e�O�_�����ޥΧֱ��覡
ShowHelp
�ҥ�"���U"���s
ValiDateNames  �����ܤ���ˬd�ɮצW���O�_���t���L�Ī��r���ΧǦC





1�ASaveFileDialog������ݩ�

Filter  �n�b��ܤ������ܪ��ɿz�ﾹ�A�Ҧp�A"��r��(*.txt)|*.txt|�Ҧ���(*.*)|*.*"
FilterIndex  �b��ܤ������ܪ��ɿz�ﾹ�����ޡA�p�G��Ĥ@���N�]��1
RestoreDirectory  �����ܤ���b�������e�O�_��_�ثe���ؿ�
AddExtension  �O�_�۰ʲK�[�q�{���ɦW
CheckFileExists
CheckPathExists

�b��ܤ����^���e�A�ˬd���w���|�O�_�s�b
Container  ����b�N�n�Ы��ɮɡA�O�_���ܥΤ�C�u���bValidateNames���u�ȮɡA�~�A�ΡC
DefaultExt  �ʬٰ��ɦW
DereferenceLinks

�b�q��ܤ����^�e�O�_�����ޥΧֱ��覡
FileName  �Ĥ@�Ӧb��ܤ������ܪ��ɩγ̫�@�ӿ������
InitialDirector  ��ܤ������l�ؿ�
OverwritePrompt  ����b�N�n�b��g�{�b�ɮɬO�_���ܥΤ�A�u���bValidateNames���u�ȮɡA�~�A��
ShowHelp  �ҥ�"?��"���s
Title  �N��ܦb��ܤ�����D�C�����r��
ValidateNames  �����ܤ���ˬd�ɮצW���O�_���t���L�Ī��r���ΧǦC

2�BSaveFileDialog�ƥ�p�U�G





C#,Dialog������
http://blog.xuite.net/teuton/wretch/expert-view/144416418
C#,Dialog������
�@�B �r���ܤ��(FontDialog)�`���ݩ�
ShowColor ����O�_����C��ﶵ
AllowScriptChange �O�_��ܦr�骺�r����
Font �b��ܤ����ܪ��r��
AllowVerticalFonts �O�_�i��ܫ����r��
Color �b��ܤ������ܪ��C��
FontMustExist ��r�餣�s�b�ɬO�_��ܿ��~
MaxSize �i��ܪ��̤j�r���j�p
MinSize �i��ܪ��̤p�r���j�p
ScriptsOnly ��ܱư�OEM�MSymbol�r��
ShowApply �O�_���"����"���s
ShowEffects �O�_��ܩ��u�B�R���u�B�r���C��ﶵ
ShowHelp �O�_���"���U"���s



C#,Dialog������
http://jjnnykimo.pixnet.net/blog/post/21585509-c%23,dialog%E5%85%A8%E4%BB%8B%E7%B4%B9


----------------Dialog SP----------------


----------------File directory ST----------------



�ɮ׳B�z�n�����ơG

���X�S�w�l�ؿ����Ҧ��ɮ�
��ܥX�ɮת��j�p�B�Ыخɶ��B�ק�ɶ��B�B�B
��binary�নhex�ɡC


C# �����ثe�M�פu�@���ؿ�(bin)
String str = System.IO.Directory.GetCurrentDirectory();





using system.io.file;
�R���ؿ� Directory.Delete (�u��R���Ū��ؿ�)
�R���ɮ� File.Delete
�P�_�O�_�s�b File.Exists


// �����ɮ�
String strFileName = @"C:\test.txt";
FileInfo fileInfo = new FileInfo(strFileName);
fileInfo.Attributes = FileAttributes.Hidden;

// ���ø�Ƨ�
String strDirName = @"C:\test";
DirectoryInfo diMyDir = new DirectoryInfo(strDirName);
diMyDir.Attributes = FileAttributes.Hidden;

�ˬd�ɮ׬O�_�s�b
if (System.IO.File.Exists(ezisp_path) == false)
{
	MessageBox.Show("�ɮ� " + ezisp_path + " ���s�b, ����@��eZISP+��");
}
else
{
	MessageBox.Show("�ɮ� " + ezisp_path + " �s�b, �}�Ҥ��C");
}


test_txt.txt

StreamReader sw = new StreamReader(@"c:test_txt.txt");
Console.WriteLine( sw.ReadToEnd() );

StreamWriter sw=new StreamWriter(fileName,false,Encoding.Default);
sw.Write(str);
sw.Close();

//��t�i�w��H���O�s����w�؉�bin\Debug\data  | bin\Release\data
string FilePath = Application.StartupPath + @"\data\" + DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".txt";
if (!Directory.Exists(Application.StartupPath + @"\data\")) Directory.CreateDirectory(Application.StartupPath + @"\data\");
StreamWriter writer = File.CreateText(FilePath);

----------------File directory SP----------------


----------------DateTime �ɶ� ST----------------



�~���۴�

�ϥ�
DateTime.Now.ToString("yyyy/MM/dd", System.Globalization.DateTimeFormatInfo.InvariantInfo);
or
Console.WriteLine(string.Format("{0:yyyy\\/MM\\/dd}", DateTime.Today));

��ܤW��/�U��
DateTime.Now.ToString().SubString(0,2)>12?( "�U��"+ DateTime.Now):( "�W��"+ DateTime.Now):


�ɶ��۴�A�Y��̦��@�ӵL��ơA�h���۴�
��̬۴�A�p���{�X�j�p�H���ӭn�������Ʀ���ơA�A�Ӥ���C

��k�G(�ѼƤj�p�g��Ķ���P MM=month, mm=Minutes, HH=24hours, hh=12hours)

�ഫ�r��榡�����
DateTime dt = Convert.ToDateTime(myDateString);


�@�� DateTime �B�z���

���έp����i��ݭn�Ψ쪺����B�z��ơG

GetTheHoursOfDay(): �Y����� 24 �p�ɮɨ�C��
GetTheFirstDayOfWeek(): �Y����b�ӬP�����Ĥ@�� (�P����)
GetTheLastDayOfWeek(): �Y����b�ӬP�����̫�@�� (�P����)
GetTheFirstDayOfMonth(): �Y����b�Ӥ�����Ĥ@��
GetTheLastDayOfMonth(): ���o�Y����b�Ӥ�����̫�@��
GetTheFirstDaysOfWeekInMoth(): �Y����b�Ӥ���C�P���Ĥ@�ѦC��
GetTheFirstDayOfQuarter(): �Y����b�өu���Ĥ@��
GetTheLastDayOfQuarter(): �Y����b�өu���̫�@��
GetTheFirstDaysOfMonthInQuarter(): ���o�Y����b�өu�C�Ӥ몺�Ĥ@�ѦC��
GetTheFirstDayOfYear(): �Y����b��~���Ĥ@��
GetTheLastDayOfYear(): �Y����b��~���̫�@��
GetTheFirstDaysOfQuarterInYear(): �Y������~�C�@�u���Ĥ@�ѦC��





----------------DateTime �ɶ� SP----------------



�p�󪾹Dvcs�{���w�g�ΤF�h�ְO����H
�Ҧp�Aload�p�ɡBload�j�ɦܰO����A�p��ݰO����j�p�A�O�_���W���H


���U�ƹ��A���ʹ��СA�����J��ܥX�ӡA�����}���Ь���C









WMI(Windows Management Instrumentation)

Windows Management Instrumentation (WMI) �O�@�إΨӺ޲z���� Microsoft Windows �@�~�t�Ϊ������λ��ݹq������ƩM�\�઺�D�n�귽�C

C#�i�H�ϥ�ManagementObjectSearcher�Q�ΤUQuery���覡����t�Ϊ���T

"�ݭn�[�JSystem.Management�ѦҡA�H�Τޥ�System.Management���O"


WMI(Windows Management Instrumentation)
1. �M��->�Ѧ�->�k��->�[�J�Ѧ�->.NET->��System.Management->�T�w
2. using System.Management;


���o CPU �Ǹ��i�H�Ψӿ��ѥΤ�ݹq�����ߤ@�ʡA�]���q�` CPU ���|�a�]���`���C
1. �M�׽Х��[�J�Ѧ� System.Management
2. �z�L ManagementObjectSearcher �d��

WMI�����n�[�J�G
����`��/�Ѧ�/�[�J�Ѧ�/.Net/System.Management


�զX��
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)//���UESC
            {
                Application.Exit();//�����{��
            }
            else
            {
                if (e.Control == true && e.Alt == true && e.KeyCode == Keys.T)//����զX�� Ctrl + Alt + T
                {
                    MessageBox.Show("Ctrl + Alt + T");
                }
            }
        }
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //�����{���e �T�{����
            DialogResult Result = MessageBox.Show("�|���x�s�T�w�n�����{��?", "�����T�{", MessageBoxButtons.YesNo);
            if (Result == System.Windows.Forms.DialogResult.Yes)
            {
                // ����Form
                e.Cancel = false;
            }
            else
            {
                e.Cancel = true;
            }
        }
            switch (e.KeyCode)   //�ھ�e.KeyCode���O����
            {
                case Keys.Up:
                    this.Top -= 10;
                    break;
                case Keys.Down:
                    this.Top += 10;
                    break;
                case Keys.Left:
                    this.Left -= 10;
                    break;
                case Keys.Right:
                    this.Left += 10;
                    break;
            }




        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox1.Text += "tttt";
            switch (e.KeyCode)
            {
                case Keys.D1:
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaaa\n";
                    Console.Beep(262,500);
                    break;
                case Keys.D2:
                    Console.Beep(294, 500);
                    break;
                case Keys.D3:
                    Console.Beep(330, 500);
                    break;
                case Keys.D4:
                    Console.Beep(349, 500);
                    break;
                case Keys.D5:
                    Console.Beep(392, 500);
                    break;
                case Keys.D6:
                    Console.Beep(440, 500);
                    break;
                case Keys.D7:
                    Console.Beep(493, 500);
                    break;
                case Keys.D8:
                    Console.Beep(523, 500);
                    break;
            }
        }










----------------Windows Media Player �v������ST----------------



DLLImport �ϥΤ覡

	�[�J�ޥ�:
	using System.Runtime.InteropServices;
	using System.Runtime.InteropServices;   //for DllImport

	DllImport���Ϊk�G

	[DllImport("kernel32.dll")]
	public static extern bool Beep(int frequency, int duration);

	�ϥΡG
	//Beep() �O�b kernel32.lib ���w�q���ABeep�㦳�H�U�쫬�G
	//BOOL Beep(DWORD dwFreq, DWORD dwDuration);
	Beep(1000, 100);


(C#)���񭵼�
System.Media.SoundPlayer myPlayer = new
System.Media.SoundPlayer(@"C:\Music\welkin.wav");
myPlayer.Play();
�]�i�H����t�ιw�]������
//�͹��n
System.Media.SystemSounds.Beep.Play();



�p�󼷩� Wave ������
�����ϥ� System.Media.SoundPlayer ���O

System.Media.SoundPlayer sp = new System.Media.SoundPlayer();
sp.SoundLocation = @"C:\Wave������\DoReMe.wav";
sp.Play(); // ����
sp.Stop(); // ����

C# ���� mp3 wav
http://olivermode.pixnet.net/blog/post/305842398-c%23--%E6%92%AD%E6%94%BE-mp3-wav

C# �p�󼽩� mp3
https://dotblogs.com.tw/kylin/2009/07/29/9721

C# �p�󼷩� Wave ������
https://dotblogs.com.tw/powerhammer/2008/03/24/2147

vcs����mp3
�[�J�Ѧ�
Microsoft.DirectX.AudioVideoPlayback		//�䤣��
private void button1_Click(object sender, System.EventArgs e)
{
	Microsoft.DirectX.AudioVideoPlayback.Audio.FromFile(@"C:\music.mp3").Play();
}

[C#][VB.NET]�ϥ�AxWindowsMediaPlayer����h�C��
https://dotblogs.com.tw/larrynung/2009/03/01/7325


�[�J�Ѧ�    COM>>Windows Media Player (wmp.dll)

�[�J
using System.Threading; //for thread
using WMPLib;


���o�v����T

C:\____����Ӫ���\__�v��\VID_20170217_114050.3gp

string filename = "C:\____����Ӫ���\__�v��\VID_20170217_114050.3gp";
WindowsMediaPlayer wmp = new WindowsMediaPlayerClass();
IWMPMedia mediainfo = wmp.newMedia(filename);
//Console.WirteLine(mediainfo.duration);


http://cyfangnotepad.blogspot.tw/2013/12/cnet-windows-media-player-wmv.html





// Test whether Windows Media Player is in the playing state.
if (wplayer.playState == WMPLib.WMPPlayState.wmppsPlaying)	//net
{
    playStateLabel.Text = "Windows Media Player is playing!";
}
else
{
    playStateLabel.Text = "Windows Media Player is NOT playing!";
}

���ܲ�100����
            wplayer.controls.currentPosition = 100;
            wplayer.controls.play();

msdn
https://msdn.microsoft.com/en-us/library/windows/desktop/dd564338(v=vs.85).aspx

WMPLib�����ݩʤΤ�k

URL:(String); ���w�C���m�A�����κ�����}
uiMode:(String); ���񾹤����Ҧ��A�i��Full, Mini, None, Invisible
playState:(integer); ���񪬺A�A1=����A2=�Ȱ��A3=����A6=���b�w�ġA9=���b�s�u�A10=�ǳƴN��
enableContextMenu:(Boolean); �ҥ�/�T�Υk����
fullScreen:(boolean); �O�_�������

//���񾹰򥻱���
[controls] wmp.controls
controls.play; ����
controls.pause; �Ȱ�
controls.stop; ����
controls.currentPosition:double; ��e�i��
controls.currentPositionString:string; ��e�i�סA�r��榡�C�p��00:23��
controls.fastForward; �ֶi
controls.fastReverse; �ְh
controls.next; �U�@��
controls.previous; �W�@��

[settings] wmp.settings //���񾹰򥻳]�w
settings.volume:integer; ���q�A0-100
settings.autoStart:Boolean; �O�_�۰ʼ���
settings.mute:Boolean; �O�_�R��
settings.playCount:integer; ���񦸼�

[currentMedia] wmp.currentMedia //��e�C���ݩ�
currentMedia.duration:double; �C���`����
currentMedia.durationString:string; �C���`���סA�r��榡�C�p��03:24��
currentMedia.getItemInfo(const string); �����e�C���T"Title"=�C����D�A"Author"=���N�a�A"Copyright"=���v��T�A"Description"=�C�餺�e�y�z�A"Duration"=����ɶ��]��^�A"FileSize"=�ɮפj�p�A"FileType"=�ɮ������A"sourceURL"=��l��}
currentMedia.setItemInfo(const string); �q�L�ݩʦW�]�m�C���T
currentMedia.name:string; �P currentMedia.getItemInfo("Title")

[currentPlaylist] wmp.currentPlaylist //��e����M���ݩ�
currentPlaylist.count:integer; ��e����M��ҥ]�t�C���
currentPlaylist.Item[integer]; ����γ]�m���w�M�״C���T�A��l�ݩʦPwmp.currentMedia
axWindowsMediaPlayer1.currentMedia.sourceURL; //������b���񪺴C���󪺸��|
axWindowsMediaPlayer1.currentMedia.name;          //������b���񪺴C���󪺦W��
axWindowsMediaPlayer1.Ctlcontrols.Play�@�@�@�@�@�@�@�@�@�@����
axWindowsMediaPlayer1.Ctlcontrols.Stop�@�@�@�@�@�@�@�@�@�@����
axWindowsMediaPlayer1.Ctlcontrols.Pause�@�@�@�@�@�@�@�@�@ �Ȱ�
axWindowsMediaPlayer1.Ctlcontrols.PlayCount�@�@�@�@�@�@�@�@��󼽩񦸼�
axWindowsMediaPlayer1.Ctlcontrols.AutoRewind�@�@�@�@�@�@�@�O�_�j�鼽��
axWindowsMediaPlayer1.Ctlcontrols.Balance�@�@�@�@�@�@�@�@�@�n�D
axWindowsMediaPlayer1.Ctlcontrols.Volume�@�@�@�@�@�@�@�@�@���q
axWindowsMediaPlayer1.Ctlcontrols.Mute�@�@�@�@�@�@�@�@�@�@�R��
axWindowsMediaPlayer1.Ctlcontrols.EnableContextMenu�@�@�@�@�O�_���\�b�����W�I��ƹ��k��ɼu�X�ֱ����
axWindowsMediaPlayer1.Ctlcontrols.AnimationAtStart�@�@�@�@�O�_�b����e������ʵe
axWindowsMediaPlayer1.Ctlcontrols.ShowControls�@�@�@�@�@�@�O�_��ܱ����u����
axWindowsMediaPlayer1.Ctlcontrols.ShowAudioControls�@�@�@�@�O�_����n��������s
axWindowsMediaPlayer1.Ctlcontrols.ShowDisplay�@�@�@�@�@�@�@�O�_��ܸ�Ƥ�󪺬�����T
axWindowsMediaPlayer1.Ctlcontrols.ShowGotoBar�@�@�@�@�@�@�@�O�_���Goto��
axWindowsMediaPlayer1.Ctlcontrols.ShowPositionControls�@�@�O�_��ܦ�m�ո`���s
axWindowsMediaPlayer1.Ctlcontrols.ShowStatusBar�@�@�@�@�@�@�O�_��ܪ��A�C
axWindowsMediaPlayer1.Ctlcontrols.ShowTracker�@�@�@�@�@�@�@�O�_��ܶi�ױ�
axWindowsMediaPlayer1.Ctlcontrols.FastForward�@�@�@�@�@�@�@�ֶi
axWindowsMediaPlayer1.Ctlcontrols.FastReverse�@�@�@�@�@�@�@�ְh
axWindowsMediaPlayer1.Ctlcontrols.Rate�@�@�@�@�@�@�@�@�@�@�ֶi���ְh�t�v
axWindowsMediaPlayer1.AllowChangeDisplaySize�@�O�_���\�ۥѳ]�w����϶H�j�p
axWindowsMediaPlayer1.DisplaySize�@�@�@�@�@�@�@�]�w����϶H�j�p
�@�@�@�@1-MpDefaultSize�@�@�@�@�@�@�@�@�@��l�j�p
�@�@�@�@2-MpHalfSize�@�@�@�@�@�@�@�@�@�@ ��l�j�p���@�b
�@�@�@�@3-MpDoubleSize�@�@�@�@�@�@�@�@�@ ��l�j�p���⭿
�@�@�@�@4-MpFullScreen�@�@�@�@�@�@�@�@�@ ����
�@�@�@�@5-MpOneSixteenthScreen�@�@�@�@�@ �ù��j�p��1/16
�@�@�@�@6-MpOneFourthScreen�@�@�@�@�@�@�@�ù��j�p��1/4
�@�@�@�@7-MpOneHalfScreen�@�@�@�@�@�@�@�@�ù��j�p��1/2
axWindowsMediaPlayer1.ClickToPlay�@�@�@�@�@�@�@�O�_���\������������Ұ�Media Player
�b���T���񤧫�,�i�H�q�L�p�U�覡Ū�������T���e�שM����,�M��]�w���٭쬰��l���j�p.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }


----------------Windows Media Player �v������SP----------------




----------------����ToString�BString.Format��������� ST----------------

�e����0���Ʀr�r��
String.Format("{0:0000}", 157);	//��X 0157

�e�᳣��0���Ʀr�r��
String.Format("{0:0000.0000}", 157.42);	//��X 0157.4200

�榡�ƹq�ܸ��X
(String.Format("{0:(###) ###-####}", 8005551212);	//��X (800) 555-1212

�����S�w���ת��r��A�᭱�ɪť�
String.Format("{0,-10}", "Hello");	//�uHello     �v

�����S�w���ת��r��A�e���ɪť�
String.Format("{0,10}", "Hello");	//�u     Hello�v

�e����0���Ʀr�r��
String.Format("{0:0000}", 157);	//��X 0157

�e�᳣��0���Ʀr�r��
String.Format("{0:0000.0000}", 157.42);	//��X 0157.4200

���B����ܡG�C3��ƥ[�r��
String.Format("{0:n}",  123456789);	//��X 123,456,789.00
String.Format("{0:n0}", 123456789);	//��X 123,456,789

���B�����
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 0); // �o�ӷ|��� Zero
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 1243.50); // �o�ӷ|��� $1,243.50

���B�����_��}_����p��2��
String.Format("{0:$###,###,###,##0.00}", 0);	//$0.00
String.Format("{0:$###,###,###,##0.00}", 12.5);	//$12.50
String.Format("{0:$###,###,###,##0.00}", 3456234532);	//$3,456,234,532.0

���B�����_��}2_����Ӧ�
String.Format("{0:$#,0}", 0);	//$0
String.Format("{0:$#,0}", 12.5);	//$13,�|�B���J��Ӧ�
String.Format("{0:$#,0}", 3456234532);	//$3,456,234,532

�榡�ƹq�ܸ��X
String.Format("{0:(###) ###-####}", 8005551212); //��X (800) 555-1212

�ʤ���
String.Format("{0:0%}", 17 / (float)60);	//��X 28%

��p��2�쪺�ʤ���
String.Format("{0:0.00%}", 17 / (float)60);	//��X 28.33%

���p���I4��A�ù��5�찵�|�ˤ��J
String.Format("{0:#,0.####}", 1234.56789);	//1,234.5679

�p���I����4�줣��0
String.Format("{0:0.####}", 1234.567);	//1234.567

�~/��/�� ��:��:�� �@��
DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss ffff");

C�f��
2.5.ToString("C")	//�D2.50

D�Q�i��Ʀr
25.ToString("D5")	//00025

E��ǫ�
25000.ToString("E")	//2.500000E+005

F�T�w�I
25.ToString("F2")	//25.00

G�`�W
2.5.ToString("G")	//2.5

N�Ʀr
2500000.ToString("N")	//2,500,000.00

X�Q���i��
255.ToString("X")	//FF

----------------����ToString�BString.Format��������� SP----------------


----------------xxxxx ST----------------





------------------------------------------------------------------------------
�ݴ��աA�ݼg�J�d�Ҷ��ءG
------------------------------------------------------------------------------

(C#)�g�L�F�h�֬�Ticks

���ɤ��Q��Timer�A�N�ΥH�U��k�h��
//���bClass�������ܼƪ��a��ŧi�}�l���ɶ�
long StartDate = DateTime.Now.Ticks;

while(����)
{
  //�M��@���]�j��h�ݲ{�b��Ticks�A�۴�ᰣ�H10000000�N�O�X��F
//�]��1 Ticks�O100�`��

if(((DateTime.Now.Ticks - StartDate) / 10000000)>15)
{
   //��L�F15����A�N�|����o
   break;
}
------------------------------------------------------------------------------
(C#)���o�ŶKïClipboard�����e

IDataObject data = Clipboard.GetDataObject();
if (data.GetDataPresent(DataFormats.Text))
{
richTextBox1.Text += data.GetData(DataFormats.Text).ToString();
}

------------------------------------------------------------------------------
(C#)Win Form�藍�W�h�Ϊ�

�ڭ̬ݨ쪺WinForm�`�O��Ϊ�
���i�H�令��ΩάO�h���
(�b�]�p�e���ݤ���A�@�w�n�ʺA���)

System.Drawing.Drawing2D.GraphicsPath myPath = new System.Drawing.Drawing2D.GraphicsPath();

//���
myPath.AddEllipse(0, 0, this.Width, this.Height);

Region myRegion = new Region(myPath);

this.Region = myRegion;

�]�i�H�Φh��Φp�U

myPath.AddPolygon(new Point[] { new Point(0, 0), new Point(0, this.Height),
new Point(this.Width, 0) });
------------------------------------------------------------------------------


------------------------------------------------------------------------------


------------------------------------------------------------------------------





�N����Form1�� FormBorderStyle �ݩʭȳ]�� None ��A�N����N�ܦ��F�L��ءB�L���D��B�LControlBox�]�Y�̤j�Ƴ̤p���������s�^������C






------------------------------------------------------------------------------


richTextBox1.Text += "�ثe�u�@�ؿ��G" + Directory.GetCurrentDirectory() + "\n";

string new_directory = "C:\\";
richTextBox1.Text += "���ܤu�@�ؿ��ܡG" + new_directory + "\n";

Directory.SetCurrentDirectory(new_directory);

richTextBox1.Text += "�ثe�u�@�ؿ��G" + Directory.GetCurrentDirectory() + "\n";


------------------------------------------------------------------------------



using System.Net;
// ���oLocal�D�����ѧO�W��
string localHostName = Dns.GetHostName();
richTextBox1.Text += "Local�D�����ѧO�W�١G" + localHostName + "\n";



------------------------------------------------------------------------------




------------------------------------------------------------------------------



ssss
enum�y�k
enum Seasons { spring, summer, autumn, winter };
private void button1_Click(object sender, EventArgs e)
{
    Seasons today = Seasons.summer;	//�ŧi
    int seasonNumber = (int)today;
    richTextBox1.Text += "get number : " + seasonNumber.ToString() + "\n";

}




------------------------------------------------------------------------------


�{�������y�X�i������

            Button a1 = new Button();
            this.Controls.Add(a1);
            a1.Size = new System.Drawing.Size(100, 50);
            a1.Location = new System.Drawing.Point(50, 350);
            a1.Text = "a1";

            Button a2 = new Button();
            this.Controls.Add(a2);
            a2.Size = new System.Drawing.Size(100, 50);
            a2.Location = new System.Drawing.Point(200, 350);
            a2.Text = "a2";

            Button a3 = new Button();
            this.Controls.Add(a3);
            a3.Size = new System.Drawing.Size(100, 50);
            a3.Location = new System.Drawing.Point(350, 350);
            a3.Text = "a3";

            Button a4 = new Button();
            this.Controls.Add(a4);
            a4.Size = new System.Drawing.Size(100, 50);
            a4.Location = new System.Drawing.Point(500, 350);
            a4.Text = "a4";

            Button a5 = new Button();
            this.Controls.Add(a5);
            a5.Size = new System.Drawing.Size(100, 50);
            a5.Location = new System.Drawing.Point(650, 350);
            a5.Text = "a5";


------------------------------------------------------------------------------



//C# �ϥ� Stopwatch ��q�N���b�惺�}
richTextBox1.Text += "�ϥ� Stopwatch ��q�N���b�惺�}\n";
System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
sw.Start();
System.Threading.Thread.Sleep(3000);
sw.Stop();
richTextBox1.Text += "�g�L�ɶ��G" + sw.Elapsed.ToString() + "\n";





------------------------------------------------------------------------------





