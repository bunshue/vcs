


vs2010��c#�䤣��Calendar����





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


//Read text from clipboard 
string cliptext = System.String.Empty;
if ( System.Windows.Forms.Clipboard.ContainsText( ) )
{
	clipText = System.Windows.Forms.Clipboard.GetText( );
}


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






