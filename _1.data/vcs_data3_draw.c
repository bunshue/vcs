/**********************************************************
 * Filename	:	vcs_data3_draw.c
 * Description	:	�e�ϡB�Ϥ��B�z����
 **********************************************************/


���ӭn��Ϥ�OnPaint�P_Paint���t�O
protected override void OnPaint(PaintEventArgs e)
private void Form1_Paint(object sender, PaintEventArgs e)


�ؽuø�ϡA��Pen

�ϰ�ø�ϡA��Brush


good draw article:
C#������A�e�Ϫ�Ū�B�g�B���
https://darkblack01.blogspot.tw/2014/03/c.html



�Q��C#�Ӱ�������Y�Ϫ��覡
http://demo.tc/post/95


C#��Image�Y��B����P����
https://gnehcic.azurewebsites.net/c%E5%B0%8Dimage%E7%B8%AE%E6%94%BE%E3%80%81%E6%97%8B%E8%BD%89%E8%88%87%E8%A3%81%E5%88%87/


C#�Ϲ��B�z(�U�ر���B���ܤj�p�B�X�ơB�U�ơB���ơB�����B�B�J
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/113208.html

C#�Ϲ��B�z(�U�ر���B���ܤj�p�B�X�ơB�U�ơB���ơB�����B�B�J�B�¥աB�o��ĪG)
http://www.zendei.com/article/7891.html


(C#)Resize������Y��Ϥ�





�@��{���v�|�ΤU���X�ؤ覡�A��p�N��檺Double Buffered�ݩʳ]�m��true�A�Ϊ̳q�L�~�өΪ̤Ϯg����A�NpictureBox��Double Buffered�ݩʳ]�m��true

-��-
���w�ġ]double buffering�^�G

�������ϧο�X�O����A�H�ʺA���覡�t�X�ù���X���t�v�C��@�հO���饿�bŪ�X���ɭԡA�t�@�իh�b�g�J�A�p�����yŪ�g���覡�ϱo�ù��i�H�Y�ɦa��s�e����ơC





�e�ϡB��ܹϤ��B�b�Ϥ��W�@�e


Form�W		�i�H �e��
Panel�W		�i�H �e��
PictureBox�W	�i�H �e�ϡB��ܹϤ�
Form�W 		�i�H �e��
Label 		�i�H 	��ܹϤ�


�Ϥ��B�z�G
��j�Y�p�B�����B���ɡB�B�B�B�B�B





�Ϥ��B�z

C:\______test_vcs\bear.jpg
string Path = "C:\\______test_vcs_file_name2\\aaaa\\bbbb";

string destFileName = @"c:\______test_vcs\picture1a.jpg";

Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
pictureBox1.Image = image;
string src = @"C:\______test_vcs\bear.jpg";


�ഫ�Ϲ��榡
public String Any2Jpg(String src)
{
    String ret = "";
    if (File.Exists(src))
    {
        Image image = Image.FromFile(src);
        ret = src.Substring(0, src.LastIndexOf(".")) + ".jpg";
        if (File.Exists(ret)) File.Delete(ret);
        image.Save(ret, System.Drawing.Imaging.ImageFormat.Jpeg);
        image.Dispose();
        image = null;
    }
    return (ret);
}


���o�Ϥ��j�p�B����Form�BpictureBox���j�p�A�H�ŦX�Ϥ��j�p�G
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
int width = image.Width;
int height = image.Height;
this.ClientSize = new Size(width + 100, height + 100);
this.pictureBox1.Size = new Size(width, height);
pictureBox1.Image = image;


�ק�Ϥ��j�p
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
ImageFormat format = image.RawFormat;
int width = 800; //�e��
int heigt = 600; //����
Bitmap imageoutput = new Bitmap(image, width, heigt); //��X�@�ӷs�Ϥ�
imageoutput.Save("C:\______test_vcs\bear2.jpg", format); //�s�ɸ��|,�榡
//����귽
image.Dispose();
imageoutput.Dispose();


#region �۩w��k:�����Ϥ��C��
//�����Ϥ������C��Χ@PictureBox���I����
private void ExtractPictureColor()
{
	Color color = new Bitmap(pictureBox1.Image).GetPixel(150, 150);
	//�N�����쪺�C�����Ψ�PictureBox���I��
	pictureBox1.BackColor = color;
}
#endregion



�t�s�s�Ϫ��榡�G

IMG_20170214_102309.jpg	//����Ӭ��ɮ�


            string str = System.Windows.Forms.Application.StartupPath;
            image.Save("c:\\aabbcc.jpeg");
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg", ImageFormat.Jpeg);

             string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

���յ����Ϥ�

            //��ù��Y�϶����ɮ�
            Image image = new Bitmap(410, 410);   //�ŧiImage���O
            Graphics g = Graphics.FromImage(image);
            g.CopyFromScreen(new Point(340, 255), new Point(0, 0), new Size(410, 410));
            //���o�ù��Wx=340 y=255�����W���A���e��410���ϰ�
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //this.pictureBox1.Image = image;
            image.Save("c:\\aabbcc.jpeg");    //��Ϥ��s�_��

            richTextBox1.Text += "�w�I�Ϧs�ɧ���\n";



            //�إߪťյe��
            Bitmap bmpCanvas = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //���o�e����ø�Ϫ���ΥHø�ϡC
            Graphics g = Graphics.FromImage(bmpCanvas);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //�N�����X���x�Φs��JPG���ɡC
            Image image = (Image)bmpCanvas;
            string str = System.Windows.Forms.Application.StartupPath;
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".jpg", ImageFormat.Jpeg);

            richTextBox1.Text += "�w�I�Ϧs�ɧ���\n";


            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(pictureBox1.Image);



Point / PointF ���c
Size / SizeF ���c
Rectangle / RectangleF ���c

���brush�G�ΨӶ񺡤@���ϰ�


�Φh���I�A�զX���@�Ӱ}�C�G
    Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };


vcs draw

1. �e�I
2. �e���u�s�u
3. �e���u�s�u
�e��B���B����
�e�����

4. �e�r
5. �e��


�ʽu�B��u


�򥻪�l�ƻy�k


�Ҧ��e�ϫ��O



�������y�k�A�ѼƳ��O(pen, X, Y, W, H)

�e�ϫ��O��z�G	���ǡG���u�B���u�s�u�B���u�B�x�ΡB���ΡB


DrawLine(new Pen(Brushes.Black, 5), px1, px2);
DrawLines(redPen, curvePoints);	//�e���u�s�u
DrawCurve(redPen, curvePoints);	//�e���u

DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

DrawRectangle(blackPen, 10, 10, 100, 50);


DrawEllipse
DrawRectangle(myPen, X, Y, W, H);


DrawRectangles(new Pen(Brushes.Red, 3), R);	//�e�h��Rectangles

DrawArc

DrawLine(myPen, x1, y1, x2, y2);
DrawLine(myPen, new Point(x1, y1), new Point(x2, y2));




�e���u��@�u
�e���u�s�u
�e���u
�e�����
ø�s��߯x��
�e�r��
�e��



DrawArc( )��ƪ��Ϊk�P��ꪺ�ۦ��A�u�O�᭱�h�F��ӿ�J�Ѽ�


DrawArc(Pen �e��,int ���W��x,int ���W��y,int �e��,int ����,int �_�l����,int ���y����);
DrawPie(Pen �e��,int ���W��x,int ���W��y,int �e��,int ����,int �_�l����,int ���y����);

DrawPolygon(Pen �e��, PointF[]  �I�y�а}�C);	//�h���

DrawEllipse(blackPen, x, y, width, height);


�G�B
private void DrawEllipseRectangle(PaintEventArgs e)
{

    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    Rectangle rect = new Rectangle(0, 0, 200, 100);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}


�T�B
private void DrawEllipseRectangleF(PaintEventArgs e)
{
    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    RectangleF rect = new RectangleF(0.0F, 0.0F, 200.0F, 100.0F);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}

�|�B
private void DrawEllipseFloat(PaintEventArgs e)
{
    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create location and size of ellipse.
    float x = 0.0F;
    float y = 0.0F;
    float width = 200.0F;
    float height = 100.0F;

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, x, y, width, height);
}







���T�ؤ�k�i�H�إ�Graphics����G
�@�B�q�LPaint�ƥ�B�z�L�{����PaintEventArgs�إ�Graphics����
Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs)
Dim g As Graphics = e.Graphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("�F�n��ޤj��", Me.Font, mBrush, 50.0F, 50.0F)

�G�BCreateGraphics ��k

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Me.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("�F�n��ޤj��", Me.Font, mBrush, 50.0F, 50.0F)
End Sub

��M�A�ڭ̤]�i�H�ޥ�Button���s��Graphics����A�p�U�ҥܡG
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Button1.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("�F�n��ޤj��", Me.Font, mBrush, 0.0F, 0.0F)
End Sub

�T�B�q Image ��H�إ�
�t�~�A�ڭ��٥i�H�q�� Image �����ͪ����󪫥�إ߹ϧΪ���C
�ե� Graphics.FromImage ��k�A���ѭn�q�䤤�إ� Graphics ���� Image �ܼƪ��W�١A�p�U�N�X�ҥܡG
Dim myBitmap as New Bitmap("C:\myPic.bmp")
Dim g as Graphics = Graphics.FromImage(myBitmap)
�� Graphics ����إ߫�A�ڭ̥i�Υ�ø�s�u���M�Ϊ��B�e�{�奻����ܻP�ާ@�Ϲ��C�P Graphics ����@�_�ϥΪ��D�骫�󦳡G
�E	Pen �� - �Ω�ø�s�u���B�İǧΪ������Χe�{��L�X���ܧΦ��C
�E	Brush �� - �Ω��R�ϧΰϰ�A�p��ߧΪ��B�Ϲ��Τ奻�C
�E	Font �� - ���Ѧ����b�e�{�奻�ɭn�ϥΤ���Ϊ��������C
�E	Color ���c - ��ܭn��ܪ����P�C��C

Pen�BBrush�BColor���ڭ̱N�b�m�e���B�e��M�C��n���i��F���СA�U���ڭ��~��ݡm�A��Font���n




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


�U�C�d�ҷ|ø�s�b�䥪�W�����x�� �]10�A10�^�C �x�Ϊ��e�׬� 100�A���׬� 50�C
�ĤG�Ӥ޼ƶǻ��� Pen �غc�禡��ܵe���e�׬� 5 �����C
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
g.DrawRectangle(blackPen, 10, 10, 100, 50);


Graphics ��k �� DrawEllipse
�@�B
DrawEllipse(Pen, Int32, Int32, Int32, Int32)	ø�s�ѯx�Υ��W���B���שM�e�ת��y�Ы��w���g�ةҩw�q�����ΡC
�G�B
DrawEllipse(Pen, Rectangle)			ø�s�Ѭɭ� Rectangle ���c���w�����ΡC
�T�B
DrawEllipse(Pen, RectangleF)			ø�s�Ѭɭ� RectangleF �w�q�����ΡC
�|�B
DrawEllipse(Pen, Single, Single, Single, Single)ø�s�Ѥ@��y�СB���שM�e�שҫ��w���g�ةw�q�����ΡC


�x�Ϊ��g�k�G
    // Create rectangle for ellipse.
    Rectangle rect = new Rectangle(0, 0, 200, 100);


    g.DrawEllipse(blackPen, 0, 0, 200, 100);
    Rectangle rect = new Rectangle(0, 0, 200, 100);
    g.DrawEllipse(blackPen, rect);

    RectangleF rect = new RectangleF(0.0F, 0.0F, 200.0F, 100.0F);
    g.DrawEllipse(blackPen, rect);

    // Create location and size of ellipse.
    float x = 0.0F;
    float y = 0.0F;
    float width = 200.0F;
    float height = 100.0F;

    g.DrawEllipse(blackPen, x, y, width, height);


private void DrawXY()	//��X�lY�l
{
    Graphics g = this.panel4.CreateGraphics();
    Point px1 = new Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
    Point px2 = new Point(this.panel4.Width * 90 / 100, this.panel4.Height * 90 / 100);
    g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
    Point py1 = new Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
    Point py2 = new Point(this.panel4.Width * 10 / 100, this.panel4.Height * 10 / 100);
    g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
    g.Dispose();
}

private void DrawXY()	//��X�lY�l
        {
            Graphics g = this.panel1.CreateGraphics();
            Point px1 = new Point(0, this.panel1.Height);
            Point px2 = new Point(this.panel1.Width, this.panel1.Height);
            g.DrawLine(new Pen(Brushes.Black, 2), px1, px2);
            Point py1 = new Point(0, this.panel1.Height);
            Point py2 = new Point(0, 0);
            g.DrawLine(new Pen(Brushes.Black, 1), py1, py2);
            g.Dispose();
        }
        private void DrawXLine()��X�l����E
        {
            Graphics g = this.panel1.CreateGraphics();
            for (int i = 1; i < 4; i++)
            {
                Point px1 = new Point(0, this.panel1.Height - i * 50);
                Point px2 = new Point(this.panel1.Width, this.panel1.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            g.Dispose();
        }
        private void DrawYLine()��X�l���
        {
            Graphics g = this.panel1.CreateGraphics();
            for (int i = 1; i < 5; i++)
            {
                Point py1 = new Point(100 * i, this.panel1.Height - 5);
                Point py2 = new Point(100 * i, this.panel1.Height);
                g.DrawLine(new Pen(Brushes.Black, 1), py1, py2);
            }
            g.Dispose();
        }






Pen�Ѽ�

 �VPen���O���F�i�H�]�w�򥻪����ʤε��⤧�~�A�ٯ�]�wø�s���覡�A�p�e���u�άO��u�A�H�νu�q���˦�


Pen ���O	�w�q�Ψ�ø�s���u�P���u������C

Pen���g�k�G
Pen �e�� = new Pen(�e���C��, �e���ʲ�);
Pen pen  = new Pen(Color.Green, 3);

���ܵe���ݩʡG
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



Pen���O�g�k�G
1.Pen(Color color);
Pen  BluePen  =  new  Pen(Color.Blue,2);
2.Pen(Color color, float width);
Pen  ColorPen  =  new  Pen(Color.FromARGB(210,100,70),5);




Pen ���O	�w�q�Ψ�ø�s���u�P���u������C


private void ShowLineJoin(PaintEventArgs e)
{

    // Create a new pen.
    Pen skyBluePen = new Pen(Brushes.DeepSkyBlue);

    // Set the pen's width.
    skyBluePen.Width = 8.0F;

    // Set the LineJoin property.
    skyBluePen.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;

    // Draw a rectangle.
    e.Graphics.DrawRectangle(skyBluePen,
        new Rectangle(40, 40, 150, 200));

    //Dispose of the pen.
    skyBluePen.Dispose();

}

Pen���g�k�G
Pen �e�� = new Pen(�e���C��, �e���ʲ�);
Pen pen  = new Pen(Color.Green, 3);

���ܵe���ݩʡG
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



-------------------------------------------------------------------------------------------------------------
�e�ϰ򥻻y�k��z�G

�bForm�W�µe��

�ŧi�A�g�bForm1���~�G
        Graphics g;	// ø�ϰ�
        Pen pen;	// �e��
        Font font;
        Brush brush;
        public Form1()
        {
		InitializeComponent();
		//��l�ơA�g�bInitializeComponent();����G
		g = this.CreateGraphics();	// ���oø�ϰϪ���
		pen = new Pen(Color.Black, 3);	// �]�w�e�����¦�B�ʲӬ� 3 �I�C
		font = new Font("�з���", 16);
		brush = new SolidBrush(Color.Black);
        }

�ϥΡG
	g.DrawLine(pen, new Point(1, 1), new Point(300, 100));
	g.DrawRectangle(pen, new Rectangle(50, 50, 100, 100));
	g.DrawString("Hello! �A�n�I", font, brush, new PointF(150.0F, 150.0F));
	g.DrawString("Hello! �A�n�I", font, mBrush, 50.0F, 50.0F)

�e�W�@�ϡG
	Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
	g.DrawImage(image, new Point(200, 200));

�bpictureBox�Bpanel�W�µe�ϡA
��
	g = this.CreateGraphics();	// ���oø�ϰϪ���
�令�G
	g = pictureBox1.CreateGraphics();

	g = panel1.CreateGraphics();


�g�b�@�_�A�Χ��o��G
// Create a Graphics object for the Control.
Graphics g = panel1.CreateGraphics();
//�ϥ�
g.xxxx
// Clean up the Graphics object.
g.Dispose();

�g�b�@�_�A�Χ��o��G
SolidBrush myBrush = new SolidBrush(Color.Red);
Graphics g = this.CreateGraphics();
g.FillRectangle(myBrush, new Rectangle(0, 0, 200, 300));
g.FillEllipse(myBrush, new Rectangle(0, 0, 200, 300));	//ø�s��߾���
myBrush.Dispose();
g.Dispose();




�bpictureBox�W��ܤ@�ϡA�æb�ϤW�@�e
�ŧi�A�g�bForm1���~�G
        Graphics g;	// ø�ϰ�

        public Form1()
        {
            InitializeComponent();
            Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
            pictureBox1.Image = image;
            g = Graphics.FromImage(pictureBox1.Image);
        }

�ϥΡG	//�ݭn.Refresh()
	g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
	pictureBox1.Refresh();

	g.DrawRectangle(new Pen(Color.Black), new Rectangle(200, 200, 100, 100));
	pictureBox1.Refresh();


���ܭI����
g.Clear(Color.White);

��_�w�]���I����
g.Clear(BackColor);

