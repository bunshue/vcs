


C# StreamReader Ū���ɡA����r�����ܦ��ýX���ѨM��k 
 �]���u�n���w�s�X�覡�Y�i�ѨM
	// �����w Encoding�A�� Encodeing �� Unicode
	System.IO.StreamReader srNoEncode = new System.IO.StreamReader("DataFile.txt");
	txtNoEncode.Text = srNoEncode.ReadToEnd();
	
	// ���w Encoding �� System.Text.Encoding.Default (�@�~�t�Υثe ANSI �r�X�����s�X�覡)
	System.IO.StreamReader srDefault = new System.IO.StreamReader("DataFile.txt",System.Text.Encoding.Default);
	txtsrDefault.Text = srDefault.ReadToEnd();
	
            
            
            
            Random r = new Random();
            string result1 = "";
            string result2 = "";
            string result3 = "";
            string result4 = "";
            for (int i = 0; i < 5; i++)
            {
                result1 += r.Next().ToString() + " ";
                result2 += r.Next(10).ToString() + " ";
                result3 += r.Next(10, 20).ToString() + " ";
                result4 += r.NextDouble().ToString() + " ";
            }
            richTextBox1.Text += "��>=0���üƭȡG" + result1 + "\n";
            richTextBox1.Text += "��0~10���üƭȡG" + result2 + "\n";
            richTextBox1.Text += "��10~20���üƭȡG" + result3 + "\n";
            richTextBox1.Text += "��0.0~1.0���üƭȡG" + result4 + "\n";






            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("�ù��ѪR�� : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");







            int[] tall = new int[] { 10, 20, 30, 40, 50 };
            int sum = 0;
            foreach (int height in tall)
            {
                sum += height;
            }
            richTextBox1.Text += "Sum = " + sum.ToString() + "\n";



            String[] animal = new String[] { "lion", "mouse", "cat", "dog", "elephant" };
            foreach (String name in animal)
            {
                richTextBox1.Text += name + "\n";
            }
            richTextBox1.Text += "\n";






�q��5�����ƨ�ListView
            //���դ�
            ListViewItem i1 = new ListViewItem("File_add.txt");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "3333";
            i1.SubItems.Add(sub_i1a);
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            sub_i1b.Text = "2016/5/25 02:10�W��";
            i1.SubItems.Add(sub_i1b);

            listView1.Items.Add(i1);

            //�]�mListView�̫�@��i��
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();





        private void nudgeWindow()
        {
            // �O�������¦�m
            int oldLeft = Left;
            int oldTop = Top;
            // �ܰʦ�m
            Random r = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = r.Next(Left - 20, Left + 20);
                Left = left;
                int top = r.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }





 [C#]pictureBox�H�ƹ��u���u�ʧ��ܤj�p
�g�ƹ��ƥ�
 void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            var t = pictureBox1.Size;
            t.Width += e.Delta;
            t.Height += e.Delta;
            pictureBox1.Size = t;
        }


pictureBox��Sizemode�ݩʳ]��Zoom

�A�K�[�ƥ�
   this.MouseWheel += new MouseEventHandler(Form1_MouseWheel); 
   
   
   
   
   


            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString("�e�r��e����", this.Font, new SolidBrush(Color.Black), 300, 100, drawFormat);


----------------many ST----------------

richTextBox1.Text += System.DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
2019/05/21 14:52:41

richTextBox1.Text += DateTime.Now.ToString() + "\n";
2019/5/21 �U�� 02:52:42

----------------many SP----------------

using System.Windows.Media.Imaging�n�ޥ�PresentationCore

�u�ݭn�b�ޥ�-->�{�Ƕ�-->�ج[-->PresentationCore




string my_string = "   �w��Ө�Myson Century!   ";

string str2 = "ON-C";
bool res;
res = my_string.ToLower().Replace(" ", "").Contains(str2.ToLower().Replace("-", ""));
richTextBox1.Text += "result = " + res.ToString() + "\n";



�bWindows�W�A[���|]����<248���A[�ɦW�[���|]�W����<260��

	List<Point> points = new List<Point>(); // �����ƹ��y�񪺰}�C�C	

	List<MyFileInfo> fileinfos = new List<MyFileInfo>();             

1��list�ŧi
	List<string> myLists = new List<string>();
	
	myLists.Add("A001");
	myLists.Add("A002");
	myLists.Add("A003"); 

2��list�ŧi
	List<List<string>> myLists = new List<List<string>>();

	myLists.Add(new List<string>() { "A001", "David" });
	myLists.Add(new List<string>() { "A002", "John" });
	myLists.Add(new List<string>() { "A003", "Tom" });             
             
             
             
             
             
bmp
https://www.pcschool.com.tw/campus/share/lib/160/
http://crazycat1130.pixnet.net/blog/post/1345538-%E9%BB%9E%E9%99%A3%E5%9C%96%EF%BC%88bitmap%EF%BC%89%E6%AA%94%E6%A1%88%E6%A0%BC%E5%BC%8F

[C#] List ���Ϊk
http://frank1025.pixnet.net/blog/post/347251643-%5Bc%23%5D-list

C# axWindowsMediaPlayer��@����
http://www.mamicode.com/info-detail-986551.html


AxWindowsMediaPlayer�C�^���D�n��k�ݩ�
https://blog.csdn.net/ivan_ljf/article/details/9774231


AForge Webcam ���v
https://blog.csdn.net/m_buddy/article/details/62417912

        private void button1_Click(object sender, EventArgs e)
        {

            /*
            Random �ü� = new Random();//�üƺؤl
            int i = �ü�.Next(0, 100);//�^��0-99���ü�
            �p�G��for �Ψ䥦�^���üơA�@�w�n�� Random �ü� = new Random();//�üƺؤl ��b�^��~���C
            */


            Random �ü� = new Random();//�üƺؤl
            for (int i = 0; i < 100; i++)
            {
                int j = �ü�.Next(0, 100);
                richTextBox1.Text += j.ToString() + "  ";
            }
            richTextBox1.Text += "\n";


        }

        //C# �O�_��JPG�ɮ� record

        private bool �O�_��JPG�ɮ�(string �ɮ�)
        {
            if (!File.Exists(�ɮ�))
                return false;

            using (System.Drawing.Image img = System.Drawing.Image.FromFile(�ɮ�))
            {
                if (img.RawFormat.Equals(System.Drawing.Imaging.ImageFormat.Jpeg))
                    return true;
            }
            return false;
        }



�@��vcs���
http://createps.pixnet.net/blog/category/1630969/2

g.DrawString("�����]�w�r���P�j�p", new Font("���^", 30), Brushes.Red, 10, 10);


C# - ���o�H���r�ꪺ�ֳt��k 


C#�y���U���|���w�覡�����:

    �O�ϥΨ�ӱ׽u�A�Ҧp    "C:\\Test.txt"
    �ĤG�جO�b���|�e�[�W@�Ÿ��A�Ҧp    @"C:\Test.txt"



���o�w�и�T
            System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");
            richTextBox1.Text += "TotalFreeSpace : " + di.TotalFreeSpace.ToString() + "\n";
            richTextBox1.Text += "VolumeLabel : " + di.VolumeLabel + "\n";




         Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height); 
            Graphics g = Graphics.FromImage(myImage); 
            g.CopyFromScreen(new Point(0,0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height)); 
            IntPtr dc1 = g.GetHdc(); 
            g.ReleaseHdc(dc1); 
            myImage.Save(@"c:\screen0.jpg");
            
            




 �A�ѵ{������ɶ� 

using System.Diagnostics;
//-------------------------------------------
Stopwatch sw = new Stopwatch();
long num = 0;
sw.Reset();
sw = Stopwatch.StartNew();
//�n���t���{����o��
sw.Stop();
TimeSpan el = sw.Elapsed;
Console.WriteLine("��O {0} ", el);
long ms = sw.ElapsedMilliseconds;
Console.WriteLine("��O {0} �@��", ms);

�ɥR����: ���@�w�C�����쪺�ɶ����ۦP��!
��ĳ��: �W�L100�@��N���I�ӺC�o�K. (�q����|Lag���)






tmp code


            richTextBox1.Text += "�~�G" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "��G" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "��G" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "�ѡG" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "�P�G" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "�ɡG" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "���G" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "��G" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "�@��G" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks�G" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay�G" + dt.TimeOfDay.ToString() + "\n";

            System.Globalization.TaiwanCalendar TC = new System.Globalization.TaiwanCalendar();
            System.Globalization.TaiwanLunisolarCalendar TA = new System.Globalization.TaiwanLunisolarCalendar();

            DateTime dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("�褸�~:" + dt.Year.ToString()) + "\n";
            message += ("����~:" + TC.GetYear(dt)) + "\n";
            message += (string.Format("�褸:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            message += (string.Format("����:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            message += (string.Format("�A��:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";



            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "�{�b����G " + dt.ToLongDateString() + Environment.NewLine;
            richTextBox1.Text += "�{�b�ɶ��G " + dt.ToLongTimeString() + Environment.NewLine;

            //�{�b����[�ѼƼg�k(���Ҭ��[5��):
            System.DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "�{�b����[5�ѡG " + Add5Day.ToLongDateString() + Environment.NewLine;

            //�{�b�ɶ��[�p�ɼg�k(���Ҭ��[12�Ӥp��):
            System.DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "�{�b�ɶ��[12�p�ɡG " + Add12Hours.ToLongTimeString() + Environment.NewLine;

            //�{�b�ɶ�������g�k(���Ҭ���30����):
            System.DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "�{�b�ɶ���30�����G " + Minus30Minutes.ToLongTimeString() + Environment.NewLine;
        }
        
        
        
�P���@        








C# ���o�ɮת�����T
using System.Diagnostics;
            richTextBox1.Text += "data : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n"; 
data : 10.0.17134.220 (WinBuild.160101.0800)



        public Form1()
        {
            InitializeComponent();

            /*
            //���ըS�����D�S����ت�Form
            this.Text = string.Empty;
            this.ControlBox = false;
            */

        }
        

 ���o�ثe�i�Φr���A��ܩ�ListBox�C

	this.listBox1.Items.AddRange(FontFamily.Families);


this.Cursor = System.Windows.Forms.Cursors.Hand;


���ܹ���

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.VSplit;
        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.Default;
        }
        
21. �ܧ�ƹ����йϮ� ( ���Ľd��bForm�� )�C
1             this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" �令�z�����ɡA�������v���榡��cur�Pico
        






C#������A�e�Ϫ�Ū�B�g�B��� 
https://darkblack01.blogspot.com/2014/03/c.html



vs2010��c#�䤣��Calendar����




C# �{���ǲ� �t�C	30�g
https://ithelp.ithome.com.tw/users/20023570/ironman/110


�ܦhC#�d��
http://fecbob.pixnet.net/blog/post/38088065-c%23-%E5%9C%93%E8%A7%92-panel


�ƻs�����Ϥ�


[C#] DrawRoundRetangle
//ø�s�ꨤ�x��
private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius) {
            GraphicsPath roundedRect = new GraphicsPath();
            Rectangle rect = new Rectangle((int)x, (int)y, (int)width, (int)height);
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
        }
        
        
        

[SDK] �� C#.net ���ҤU, �p��N�۾��v��ø�s�� PictureBox ��?
https://www.aisys.com.tw/web/tech/tech.php?question_id=127
[SDK] �� C#.net ���ҤU, �p��N�۾��v��ø�s�� PictureBox ��?

[�ŧi]
Graphics G;  //�s�� Control.CreateGraphics �إߪ�����
IntPtr pHdc; //�s�� Graphics.GetHdc �^�Ǫ� hdc ��}

[��l��]
G = pictureBox1.CreateGraphics(); //�ϥ� pictureBox1 �إߤ@Graphics����

[ø�s�v��]
private void axAxAltairU1_OnSurfaceDraw(object sender, AxAxAltairUDrv.IAxAltairUEvents_OnSurfaceDrawEvent e)
{   // AltairU::OnSurfaceDraw �ƥ�
    pHdc = G.GetHdc(); //���o Hdc
    axAxAltairU1.DrawSurface(e.surfaceHandle, pHdc.ToInt32(), 1, 1, 0, 0); //ø�s�v���� Hdc
    G.ReleaseHdc();    //���� Hdc
}


���s����visual studio	�ݦ��L�Ѫ�����




vcs
string�PString���󤣦P�H



vcs��ù��e���A�p��Ϥ����ù��Mactive�e���H






�ɮסGD://Xilinx_SDK_2018.3_1207_2324_Win64.exe,	


MD5�G			0E83E8251D76B51B5D311EEA2B2FB8FC
MD5 SUM Value : 	0e83e8251d76b51b5d311eea2b2fb8fc    
			0E83E8251D76B51B5D311EEA2B2FB8FC

vcs_MD5

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC




�����줸�ɹs �Q�i��ΤQ���i��

byte byteValue = 254;

// Display integer values by calling the ToString method.
richTextBox1.Text += byteValue.ToString("D8").ToString() + "\t" + byteValue.ToString("X8") + "\n";






vcs AForge

    �[�J�F�Ѧ�AForge.Video.FFMPEG�A�sĶ�٬O���L

�`�N�@�U���S���[�iFFMPEG���ѦҡA�����bVisual Studio�̥[�O���檺�A�|�����C
�n������ؿ��U���ɮ׽ƻs���X�ؿ��C

https://dahao.blogspot.com/2016/08/caforgenet.html



��_C#�MAforge.net��{�Ϲ����y�ĪG

https://blog.csdn.net/dark00800/article/details/41651499


�U��webcam�{�����
http://www.cnblogs.com/xrwang/archive/2010/02/13/HowToCaptureCameraVideoViaDotNet.html


AForge�Ұ�webcam
http://www.voidcn.com/article/p-kvujrudv-ru.html



       

vcs_WMP
richTextBox1.Text += " �q���W��G" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//�C��
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.���q���r�@��;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.���q���r;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


�Ѧ�
063_�ϥ�C#�ާ@INI���
��vcs_WMP �]�w�`�Ϊ�mp3��Ƨ�

vcs_WMP�n�令�i�H�h���ɮ�  �ο��өΦh�Ӹ�Ƨ� �@�_����








vcs

�P���X
            string[] Day = new string[] { "�P����", "�P���@", "�P���G", "�P���T", "�P���|", "�P����", "�P����" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";



vcs
ex069	Ū�������B²���B���A�O�_��OK�H
ex062	�ƻs������ܽƻs�i�סA���κC�tU�L�Ӵ�



string color
color_r
color_g
color_b




[C#]�p����Google Static Map
https://dotblogs.com.tw/larrynung/2013/01/06/86807

Supalogo-�K�O���u�WLogo�Ϥ����;�
https://dotblogs.com.tw/larrynung/2010/07/15/16580

[C#]��l��e���|��g�ʱ��D�x��API
https://dotblogs.com.tw/larrynung/2011/03/17/21890




[C#] QRCode Generator & Reader 
http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html


vcs
vcs��QR code�s�X�ѽX
�ѦҡGhttp://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html
�� zxing.dll �[�J�Ѧ�

���U���@�Ӷ}�񪺨�ܮw(DLL) "Zxing"
http://zxingnet.codeplex.com/



C#���ϥ�SendMessage�i��i�{�q�H�����
https://blog.csdn.net/yl2isoft/article/details/20227421


(C#)WinAPI��SendMessage�ǰe

[DllImport("user32.dll")]

public static extern long SendMessage(int hWnd, uint msg, uint wparam, string text);

public const uint WM_SETTEXT = 0x0c;
public const uint WM_GETTEXT = 0x0d;
public const uint WM_LBUTTONUP = 0x0202;
public const uint WM_LBUTTONDOWN = 0x0201;

SendMessage(��J��쪺Handle, WM_SETTEXT, 0, "�A�n�e���r��" );

����s���U�h���T���G

SendMessage(���s��Handle, WM_LBUTTONDOWN, 0, null);

SendMessage(���s��Handle, WM_LBUTTONUP, 0, null);


��Ӱ����ɶ��ƭȪ��ǻ��P����



vcs �� WebCam �ϥΤj����










/**
* @brief   Convert a 6 digit HTML code (hex) into a color value.
*/
#define HTML2COLOR(h)		((color_t)((((h) & 0xF80000)>>8) | (((h) & 0x00FC00)>>5) | (((h) & 0x0000F8)>>3)))
#define HTML2COLOR(h)		((COLOR_TYPE)(HTML2COLOR_R(h) | HTML2COLOR_G(h) | HTML2COLOR_B(h)))
#define HTML2COLOR(h)		((COLOR_TYPE)(((((h)&0xFF0000)>>16)+(((h)&0x00FF00)>>7)+((h)&0x0000FF)) >> (10-COLOR_BITS)))

#define COLOR_BITS		16
#define COLOR_TYPE		uint16_t
#define COLOR_TYPE_BITS		16


		
/**
 * @name   Some basic colors
 * @{
 */
#define White			HTML2COLOR(0xFFFFFF)
#define Black			HTML2COLOR(0x000000)
#define Gray			HTML2COLOR(0x808080)
#define Grey			Gray
#define Blue			HTML2COLOR(0x0000FF)
#define Red			HTML2COLOR(0xFF0000)
#define Fuchsia			HTML2COLOR(0xFF00FF)
#define Magenta			Fuchsia
#define Green			HTML2COLOR(0x008000)
#define Yellow			HTML2COLOR(0xFFFF00)
#define Aqua			HTML2COLOR(0x00FFFF)
#define Cyan			Aqua
#define Lime			HTML2COLOR(0x00FF00)
#define Maroon			HTML2COLOR(0x800000)
#define Navy			HTML2COLOR(0x000080)
#define Olive			HTML2COLOR(0x808000)
#define Purple			HTML2COLOR(0x800080)
#define Silver			HTML2COLOR(0xC0C0C0)
#define Teal			HTML2COLOR(0x008080)
#define Orange			HTML2COLOR(0xFFA500)
#define Pink			HTML2COLOR(0xFFC0CB)
#define SkyBlue			HTML2COLOR(0x87CEEB)
/** @} */
      


vcs ���oWebCam�v���G		�ϥ�Emgu

�ѦҡG
C# ���� Webcam �iusing Emgu�j 
http://blog.kenyang.net/2012/03/04/c-webcam-using-emgu
[C#] ���oWebCam�v��
http://foxktr560.blogspot.com/2013/08/c-webcam.html

OpenCV�O�@�M�j�j���v���B�zlibrary�A��INTEL�}�o�A
�D�`�j�j�A�ƦܧA�i�H�Q��OpenCV�h����OCR�A�ܤ�K�C
�]�ѩ�OpenCV�S���䴩C#�A��C#�n���ϥ�OpenCV�O?
�N�O�aEmgu�AEmgu�O�@�M���\OpenCV��function�bC#���y�����Q�ϥΡC

�}��vcs�M�סA�Ԥ@��pictureBox�A�ǳ����WebCam�^�Ǫ��v��

�M�ץ[�J�ѦҡG
C:/Emgu/emgucv-windows-x86 2.3.0.1416/bin/ ��4��dll

    Emgu.CV.dll
    Emgu.CV.ML.dll
    Emgu.CV.UI.dll
    Emgu.Util.dll
    
�[�J�H��A�Х��x�s�A���M�סA
�����H�U2��dll
    opencv_core231.dll
    opencv_highgui231.dll
���M�ת�/bin/Debug/���U

�]��Emgu.CV.dll�|�ϥΨ�W�z���dll�C


��import�|�ϥΨ쪺lib�A�p�U:

	using Emgu.CV;
	using Emgu.CV.Structure;

���ŧi�@��Capture����A�p�U:

	private Capture cap = null;                 // Webcam����

�o�Ӫ���N�O�Ψӳs����A��webcam�C



Form1_Load event�A
�s������v���H�Ϋإߤ@��event�Ψӧ���e���A�p�U:

private void Form1_Load(object sender, EventArgs e)
{
     cap = new Capture(0); // �s������v��0�A�p�G�A����x��v���A�ĤG�x�N�O1
     Application.Idle += new EventHandler(Application_Idle); // �bIdle��event�U�A��e���]�w��pictureBox�W(��M�A�]�i�H��timer�ƥ�)
}


���U�ӭn�g����e��event��code�A

void Application_Idle(object sender, EventArgs e)
{
     Image<Bgr, Byte> frame = cap.QueryFrame(); // �hquery�ӵe��
     pictureBox1.Image = frame.ToBitmap(); // ��e���ഫ��bitmap���A�A�A����pictureBox����
}

        


�[�J�|�ӰѦ� 
Emgu.CV.dll
Emgu.CV.ML.dll
Emgu.CV.UI.dll
Emgu.Util.dll
 (��dll���EmguCV�w�˧���bin���U)




3.2 �`�α��f�S��
caputure
        public Capture();			//Create a capture using the default camera
        public Capture(int camIndex);		//���،s�������D�v, �G0�{�l
        public Capture(string fileName);	//The name of a file, or an url pointed to a stream.
        





2011/5/8(SUN)
2011/5/8(��) 20:28 �۫H


string�PString���󤣦P�H



vcs��ù��e���A�p��Ϥ����ù��Mactive�e���H


bmp.Save(@"D:\ssss.jpg");


vcs_WMP
richTextBox1.Text += " �q���W��G" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//�C��
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.���q���r�@��;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.���q���r;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


�Ѧ�
063_�ϥ�C#�ާ@INI���
��vcs_WMP �]�w�`�Ϊ�mp3��Ƨ�

vcs_WMP�n�令�i�H�h���ɮ�  �ο��өΦh�Ӹ�Ƨ� �@�_����





C# �p����o��� DateTime ����������Ѽ�

���o��Ӥ���������u�Ѽơv�]�����@�Ѫ̱ġu�L����R�h�k�v�^ 

    new TimeSpan(date1.Ticks - date2.Ticks).Days

���o��Ӥ���������u�Ѽơv�]�^�ǫ��O�� double ����T�ס^

    new TimeSpan(date1.Ticks - date2.Ticks).TotalDays

���o��Ӥ���������u�p�ɼơv�]�^�ǫ��O�� double ����T�ס^

    new TimeSpan(date1.Ticks - date2.Ticks).TotalHours

���o��Ӥ���������u�����ơv�]�^�ǫ��O�� double ����T�ס^ 

    new TimeSpan(date1.Ticks - date2.Ticks).TotalMinutes




DateTime date1 = new DateTime(2008, 12,31, 23,59,59, DateTimeKind.Local);
DateTime date2 = new DateTime(2003, 2,13, 23,59,59, DateTimeKind.Local);
TimeSpan s = new TimeSpan(date1.Ticks - date2.Ticks);    







ID3�榡


�}�Y 	3 	�uTAG�v�A���ҡC
���D 	30 	�q�����D�A�̦h30�ӭ^��r���C
���N�a 	30 	�@���κt�۪̪��W�r�A�̦h30�ӭ^��r���C
�M�� 	30 	�M��W�١A�̦h30�ӭ^��r���C
�~�� 	4 	�褸�~���A�|�ӼƦr�C
���� 	28[3]��30 	�N�O���סC
�s�줸��[3] 	1 	�p�G���x�s���ءA����o�Ӧ줸�շ|�x�s�@�ӤG�i�쪺0�C
����[3] 	1 	�o���q�b�ӱM�褤�����ءA�Ϊ̬�0�C�Y�e�@�Ӧ줸�իD�s�A�h���椺�e�L�ġC
���N���� 


header 	3 	"TAG"
title 	30 	30 characters of the title
artist 	30 	30 characters of the artist name
album 	30 	30 characters of the album name
year 	4 	A four-digit year
comment 	28[7] or 30 	The comment.
zero-byte[7] 	1 	If a track number is stored, this byte contains a binary 0.
track[7] 	1 	The number of the track on the album, or 0. Invalid, if previous byte is not a binary 0.
genre 	1 	Index in a list of genres, or 255 












�ݽd�Ҿ�C# �t�C
https://ithelp.ithome.com.tw/users/20044155/ironman/241



wmp���ܵ����j�p
https://blog.csdn.net/ivan_ljf/article/details/9774231
axWindowsMediaPlayer1.DisplaySize�@�@�@�@�@�@�@?�m����?�H�j�p  
�@�@�@�@1-MpDefaultSize�@�@�@�@�@�@�@�@�@��l�j�p  
�@�@�@�@2-MpHalfSize�@�@�@�@�@�@�@�@�@�@ ��l�j�p���@�b  
�@�@�@�@3-MpDoubleSize�@�@�@�@�@�@�@�@�@ ��l�j�p��?��  
�@�@�@�@4-MpFullScreen�@�@�@�@�@�@�@�@�@ ����  
�@�@�@�@5-MpOneSixteenthScreen�@�@�@�@�@ �̹��j�p��1/16  
�@�@�@�@6-MpOneFourthScreen�@�@�@�@�@�@�@�̹��j�p��1/4  
�@�@�@�@7-MpOneHalfScreen�@�@�@�@�@�@�@�@�̹��j�p��1/2  

axWindowsMediaPlayer1.settings.balance = 1; ���
axWindowsMediaPlayer1.settings.balance = -1;���





windows media player
�b���W���񤧫�,�i�H�q�L�p�U�覡Ū�������W���e�שM����,�M��]�m���٭쬰��l���j�p.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }
         
         
         
         



//Wait
System.Threading.Thread.Sleep( 5000 ); // wait 5 seconds (5000 milliseconds)



//Take a screenshot 

// Take a screenshot
// By Ali Hamdar (http://alihamdar.com/)
// http://social.msdn.microsoft.com/Forums/en/csharpgeneral/thread/79efecc4-fa6d-4078-afe4-bb1379bb968b

// Default values for full screen
int width = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Width;
int height = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Height;
int top = 0;
int left = 0;

System.Drawing.Bitmap printscreen = new System.Drawing.Bitmap( width, height );
System.Drawing.Graphics graphics = System.Drawing.Graphics.FromImage( printscreen as Image );
graphics.CopyFromScreen( top, left, 0, 0, printscreen.Size );
printscreen.Save( outputfile, imagetype );




PNG �� BMP
using System.Drawing.Imaging;   //for PixelFormat

        private void button1_Click(object sender, EventArgs e)
        {
            System.Drawing.Image PngImg = System.Drawing.Image.FromFile(@"C:\______test_vcs\sample.png");
            Bitmap myImage = new Bitmap(PngImg.Width, PngImg.Height, PixelFormat.Format32bppRgb);
            using (Graphics g = Graphics.FromImage(myImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;
                g.DrawImage(PngImg, 0, 0);
            }
            PngImg.Save(@"C:\______test_vcs\sample.bmp", ImageFormat.Bmp);
        }



label �� cursor �i�H���ܴ�Ы���label�ɡA�|���ܪ��ƹ���СC


�ھڮɶ��إߤ��
File.Create("C:\\______test_vcs\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//�إߤ��


vcs�H������
�Ҥ���
��L


vcs�Ӥ�+��r�B�Ӥ�+�B���L



vcs history
�jscale
�pscale
�i�m��table
�B�zBC�Ʀr


VCS��Y�ϰ줺�A���д����w�ޡA�o�˥Ψ��˴��C���I��RGB��

C#	w/ XML���R



vcs
richtextbox�̡A�p�󪾹D�ثe��ЩҦb��line�Pposition

bmp
�p���bmp��Ū�X�Ҧ��I �����h��̭��Ʀr �t�s�s��
�ݯण�వ���C�⥭�����ĪG



vcs
ImageViewer is from _Yusuf Shakeel_CSharp



            
            
            
"
Bitmap Image (.bmp)|*.bmp|
Gif Image (.gif)|*.gif|
JPEG Image (.jpeg)|*.jpeg|
Png Image (.png)|*.png|
Tiff Image (.tiff)|*.tiff|
Wmf Image (.wmf)|*.wmf

";







vcs�}�Ҥ@�ӯ¤�r�ɨ�richtextbox�̭�
�ثe�S��k�B�z�����B²���B���P�ɦs�b���¤�r��


//�}���ɮ�
FileStream myFile = File.Open(@"C:\myWriter.txt", FileMode.OpenOrCreate, FileAccess.ReadWrite);

BinaryReader myReader = new BinaryReader(myFile);

int dl = System.Convert.ToInt16(myFile.Length);
//Ū���줸�}�C

byte[] myData = myReader.ReadBytes(dl);
//����귽

myReader.Close();

myFile.Close();



ImageViewer	��s���[�c


using System.Drawing.Imaging;

           Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    cnt++;
                    //get source pixel value
                    Color p = simg.GetPixel(lx, y);
                    if ((cnt % 10000) == 0)
                    {
                        richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + "  ";
                        //richTextBox1.Text += p.A.ToString() + p.R.ToString() + p.G.ToString() + p.B.ToString() + "  ";
                    }

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }

            //load mirror image in picturebox2
            pictureBox2.Image = mimg;

            //save (write) mirror image
            //mimg.Save("C:\\MirrorImage.png");
            mimg.Save("C:\\MirrorImage.jpg", ImageFormat.Jpeg);
            mimg.Save("C:\\MirrorImage.png", ImageFormat.Png);
            mimg.Save("C:\\MirrorImage.bmp", ImageFormat.Bmp);


vcs���i�e�I�A�εe�����N




//-------------------------------------------------------------------------------------

            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Bottom;


openFileDialog1.Filter = "XML�]�w��|*.xml";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.wmf";

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            

        //----���textbox�ɡA���������r
        private void TextBox_Enter(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }



        //�Y�ppictureBox1
        //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;/*AutoSize�i��L�k�Y�p�Ϥ�*/
        //���令������Y�p�Ϥ�SizeMode
        pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;












����pictureBox�j�p���ܪ���m

pictureBox1.Image.Save(@"D:\bbbbb.jpg");




���ܳ����r���C��
            richTextBox1.SelectionStart = 10;
            richTextBox1.SelectionLength = 5;
            richTextBox1.SelectionColor = Color.Red;
            richTextBox1.SelectionBackColor = Color.Green;



Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // �b���W��� bmp �O����Ϲ�
this.Refresh() ; //���� Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");


pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //�۰ʽվ�j�p
pictureBox1.Image = bmp; //��ܦb pictureBox1 �Ϥ������

// bmp ���j�p�MpictureBox1 �ۦP
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// �H�O����Ϲ� bmp �إ� myDraw �O����e��
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //�e���I����
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //�i



����Ӳ�U�q�{�A���������f�M���C
�d�M�K��I�����A�@�����n�X���Y�C
�H�@�X�^�˩��ơA�s�Ψ��ªE�H�y�C
���{�|�����a��A�G�S����Ī����C
�������䳥���A�Q��Ѥf�i���סC
�®ɤ��°�e�P�A���J�M�`�ʩm�a�C
�^�R�s�Ҥl�A���y�ѤU�D�C���C��a�áA�խ����P���C
�K���W���t�A�g�ᤣ�Ƨg�C���s�w�i���A�{�����M��C
�鸨�j��c�A�c��I����C
���Y�c�k�b�A�������ȩv�C
�\�\�T����A�W���K�}�ϡC
���y�ۤ���A��륢�]�d�C





------------------------------------------------------------------------------------------------------------------------


char[] bbv={'��','�@','�H'};

����Ӳ�U�q�{�A���������f�M���C
�d�M�K��I�����A�@�����n�X���Y�C
�H�@�X�^�˩��ơA�s�Ψ��ªE�H�y�C
���{�|�����a��A�G�S����Ī����C";



            char[] bbv={'��','�@','��'};
            string abc = "����Ӳ�U�q�{�A���������f�M���C�d�M�K��I�����A�@�����n�X���Y�C�H�@�X�^�˩��ơA�s�Ψ��ªE�H�y�C���{�|�����a��A�G�S����Ī����C";
       
            int aa = abc.IndexOfAny(bbv);
            int bb = abc.IndexOfAny(bbv, 32);
            int cc = abc.IndexOfAny(bbv, 32, 10);
            int dd = abc.IndexOfAny(bbv, 32, 20);
            int ee = abc.IndexOfAny(bbv, 32, 30);

            richTextBox2.Text += "length of abc = " + abc.Length.ToString() + "\n";
            richTextBox2.Text += "aa = " + aa.ToString() + "\n";
            richTextBox2.Text += "bb = " + bb.ToString() + "\n";
            richTextBox2.Text += "cc = " + cc.ToString() + "\n";
            richTextBox2.Text += "dd = " + dd.ToString() + "\n";
            richTextBox2.Text += "ee = " + ee.ToString() + "\n";




------------------------------------------------------------------------------------------------------------------------


this.richTextBox1.Size = new System.Drawing.Size(382, 594);



------------------------------------------------------------------------------------------------------------------------




------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


        const int GB = 1024 * 1024 * 1024;//�w�qGB���p��`�q
        const int MB = 1024 * 1024;//�w�qMBW���p��`�q
        const int KB = 1024;//�w�qKB���p��`�q
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//���Byte��
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }



------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------------------------------

            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            //MessageBox.Show("Width = " + this.panel1.Width + "  Height = " + this.panel1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //ø�s��u 
            this.panel1.BackgroundImage = bitM;

------------------------------------------------------------------------------------------------------------------------


            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
            }
            MessageBox.Show("OK");


------------------------------------------------------------




-----------------------------------------





XML ����	<!-- --> �����e�C


@"C:\______test_vcs\cat\cat2.png"

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // �b���W��� bmp �O����Ϲ�

this.Refresh() ; //���� Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");
pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //�۰ʽվ�j�p
pictureBox1.Image = bmp; //��ܦb pictureBox1 �Ϥ������

// bmp ���j�p�MpictureBox1 �ۦP
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// �H�O����Ϲ� bmp �إ� myDraw �O����e��
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //�e���I����
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //�i�Hø�ϤF






ø�s�ϧΪ��󪺤�k

Graphics���OGDI+���ѤU�C��k��ø�s�W�z�M�椤�����ءG 


DrawLines

DrawCurve
DrawClosedCurve


        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

	DrawCircle(200, 200, 100);

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }


	private void DrawPixel(int xx, int yy)
	{
		
	}
	


PictureBoxSizeMode

                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;


�إߵe��

Graphics �e�������ܼ�;
�e�������ܼ� = ����W��.CreateGraphics();

�Ҧp�G�b���W�إߵe��g�G
Graphics g;
g = this.CreateGraphics();


�Ҧp�G�b�Ϥ����pictureBox1�W�إߵe��g�G
Graphics g;
g = pictureBox1.CreateGraphics();

�e��Pen����

Pen �e�� = new Pen(�e���C��, �e���ʲ�);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

���ꪫ��]���S�B�Ϯ�T�B�᯾H�B���hL�^

�������O
SolidBrush		�إ߳�@�C�⪺����
	SolidBrush sb = new SolidBrush(Color.Red);
	Pen p = new Pen(sb, 2);
TextureBrush		�إߥH�ϧΪ����@�Ϯת�����
	TextureBrush tb = new TextureBrush("bmp1.bmp");
	Pen p = new Pen(tb, 2);
HatchBrush		�إߪ᯾����
	HatchBrush �᯾�����ܼ� = new HatchBrush(�᯾����, �e���C��, �I���C��);
	HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
	Pen p = new Pen(hb, 10);
	(�n���[�J�Gusing System.Drawing.Drawing2D;)
LinearGradienBrush	�إߺ��h����
	LinearGradientBrush ���h�����ܼ� = new LinearGradientBrush(���h�x�ΰϰ�, �e���C��, �I���C��, ���h�ɱר���);
	
	Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
	LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
	Pen p = new Pen(lgb, 10);
	(�n���[�J�Gusing System.Drawing.Drawing2D;)


Pen �e�� = new Pen(�e���C��, �e���ʲ�);






�]�w�C�⪺��k	�I�s�R�A�禡�GColor.FromArgb()

ex:
Color red= Color.FromArgb(255,0,0)
this.BackColor=Color.White;


Pen�u���@��
Brush���|��

Pen�Ω�i�DGraphics�p��ø�s�u��
Brush�Ω��R�ϰ�

Point���Ϊk
Point b=new Point(20,10);
Point a=new Point();
a.X=20;
a.Y=10;


ø�s��u�A�i�]�wPen��DashStyle�ݩʬ�Dash,Dot,DashDot�Ϊ�DashDotDot��
���ܪ��u���I���Ϊ��A�i�H�]�wStartCap�MEndCap�ݩ�

blackPen.StartCap=LineCap.ArrowAnchor;







�ۤvø�sbitmap�Ϥ��O�s,�ͦ�ico���Ϊ̹�H
���Ѧ^���@�Ӱ��D���ɭԪ��H��
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("���մ��ը���", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//�O�s�U�ӳo�ӥi�H�ݥͦ����Ϥ� 
                
                

vcs
Form2������Modifiers�n�令Internal, �w�]��private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
�b�w�]�����p�U�AC# ����ϥΫ��СA�Y�n�Ϋ��Ъ��ܡA�n�b�sĶ���]�w���ҥ� unsafe �Ҧ��~��C



�@�Ψƥ�d��	WinEventHandler

            Color cl = Color.Red;
            panel1.BackColor = cl;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";
            //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();

            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;

            Color cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";



-------------------------------------------------------------------------------------------------------------------------------------
�ھڤ��e����ɮ�

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//�Ы�StreamReader��H
            StreamReader sr2 = new StreamReader(textBox2.Text);		//�Ы�StreamReader��H
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//Ū����󤺮e�çP�_
            {
                MessageBox.Show("����ɮ׬ۦP");
            }
            else
            {
                MessageBox.Show("����ɮפ��ۦP");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
�إ��{���ɮ�

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//��ܸ�Ƨ�
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//��ܸ�Ƨ�
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//�Ыؤ��
            }


-------------------------------------------------------------------------------------------------------------------------------------
�p��ɶ����j
dtpicker_first dtpicker_second ��DateTimePicker
            MessageBox.Show("���j "+
                DateAndTime.DateDiff(	//�ϥ�DateDiff��k���������j
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" ��", "���j�ɶ�");






-------------------------------------------------------------------------------------------------------------------------------------
        //�@��@��Ū���¤�r�ɮפ������e
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.ShowDialog();
                textBox1.Text = openFileDialog1.FileName;
                StreamReader SReader = new StreamReader(textBox1.Text, Encoding.Default);
                string strLine = string.Empty;
                while ((strLine = SReader.ReadLine()) != null)
                {
                    textBox2.Text += strLine + Environment.NewLine;
                }
            }
            catch { }
        }





-------------------------------------------------------------------------------------------------------------------------------------
�ϥ�MD5�[�K

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //�Ы�MD5��H
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//�N�r��s�X���@��Byte�ǦC
            byte[] md5data = md5.ComputeHash(data);//�p��dataByte��Hash��
            md5.Clear();    //�M��MD5��H
            string str = "";//�w�q�@���ܶq�A�ΨӰO���[�K�᪺�K�X
            for (int i = 0; i < md5data.Length - 1; i++)//�M��byte�Ʋ�
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//��M���쪺Byte�i��[�K
            }
            return str;//��^�o�쪺�[�K�r��
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "�ϥ�MD5�[�K�᪺���G���G" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
�p��GB MB KB

        const int GB = 1024 * 1024 * 1024;//�w�qGB���p��`�q
        const int MB = 1024 * 1024;//�w�qMBW���p��`�q
        const int KB = 1024;//�w�qKB���p��`�q
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//���Byte��
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

�{���u��P�ɹB��@��  �bForm1_Load�[�J:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//�w�q�@��bool�ܶq �ΨӪ�ܬO�_�w�g�B��
            //�Ы�Mutex������H
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "�Ȥ@��", out Exist);
            if (Exist)//�p�G�S���B��
            {
                newMutex.ReleaseMutex();//�B��s���^
            }
            else
            {
                MessageBox.Show("���{���@���u��B��@�ӹ�ҡI", "����", MessageBoxButtons.OK, MessageBoxIcon.Information);//�u�X���ܫH��
                this.Close();//������e���^
            }

        }
        






-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------










-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------






