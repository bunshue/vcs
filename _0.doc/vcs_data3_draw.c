/**********************************************************
 * Filename	:	vcs_data3_draw.c
 * Description	:	µe¹Ï¡B¹Ï¤ù³B²z¬ÛÃö
 **********************************************************/


À³¸Ó­n¯à°Ï¤ÀOnPaint»P_Paintªº®t§O
protected override void OnPaint(PaintEventArgs e)
private void Form1_Paint(object sender, PaintEventArgs e)


®Ø½uÃ¸¹Ï¡A¥ÎPen

°Ï°ìÃ¸¹Ï¡A¥ÎBrush


good draw article:
C#ªìÅéÅç¡Aµe¹ÏªºÅª¡B¼g¡BÅã¥Ü
https://darkblack01.blogspot.tw/2014/03/c.html



§Q¥ÎC#¨Ó°µ¨ì¹ÏÀÉÁY¹Ïªº¤è¦¡
http://demo.tc/post/95


C#¹ïImageÁY©ñ¡B±ÛÂà»Pµô¤Á
https://gnehcic.azurewebsites.net/c%E5%B0%8Dimage%E7%B8%AE%E6%94%BE%E3%80%81%E6%97%8B%E8%BD%89%E8%88%87%E8%A3%81%E5%88%87/


C#¹Ï¹³³B²z(¦UºØ±ÛÂà¡B§ïÅÜ¤j¤p¡B¬X¤Æ¡B¾U¤Æ¡BÃú¤Æ¡B©³¤ù¡B¯BÀJ
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/113208.html

C#¹Ï¹³³B²z(¦UºØ±ÛÂà¡B§ïÅÜ¤j¤p¡B¬X¤Æ¡B¾U¤Æ¡BÃú¤Æ¡B©³¤ù¡B¯BÀJ¡B¶Â¥Õ¡BÂoÃè®ÄªG)
http://www.zendei.com/article/7891.html


(C#)Resizeµ¥¤ñ¨ÒÁY©ñ¹Ï¤ù





¤@¯ëµ{¦¡®v·|¥Î¤U­±´XºØ¤è¦¡¡A¤ñ¦p±Nªí³æªºDouble BufferedÄÝ©Ê³]¸m¬°true¡A©ÎªÌ³q¹LÄ~©Ó©ÎªÌ¤Ï®g¾÷¨î¡A±NpictureBoxªºDouble BufferedÄÝ©Ê³]¸m¬°true

-µù-
Âù½w½Ä¡]double buffering¡^¡G

Âù­«ªº¹Ï§Î¿é¥X°O¾ÐÅé¡A¥H°ÊºAªº¤è¦¡°t¦X¿Ã¹õ¿é¥Xªº³t²v¡C·í¤@²Õ°O¾ÐÅé¥¿¦bÅª¥Xªº®É­Ô¡A¥t¤@²Õ«h¦b¼g¤J¡A¦p¦¹½ü¬yÅª¼gªº¤è¦¡¨Ï±o¿Ã¹õ¥i¥H§Y®É¦a§ó·sµe­±¸ê®Æ¡C





µe¹Ï¡BÅã¥Ü¹Ï¤ù¡B¦b¹Ï¤ù¤W§@µe


Form¤W		¥i¥H µe¹Ï
Panel¤W		¥i¥H µe¹Ï
PictureBox¤W	¥i¥H µe¹Ï¡BÅã¥Ü¹Ï¤ù
Form¤W 		¥i¥H µe¹Ï
Label 		¥i¥H 	Åã¥Ü¹Ï¤ù


¹Ï¤ù³B²z¡G
©ñ¤jÁY¤p¡Bµô¤Á¡BÂàÀÉ¡B¡B¡B¡B¡B¡B





¹Ï¤ù³B²z

C:\______test_vcs\bear.jpg
string Path = "C:\\______test_vcs_file_name2\\aaaa\\bbbb";

string destFileName = @"c:\______test_vcs\picture1a.jpg";

Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
pictureBox1.Image = image;
string src = @"C:\______test_vcs\bear.jpg";


Âà´«¹Ï¹³®æ¦¡
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


¨ú±o¹Ï¤ù¤j¤p¡B§ïÅÜForm¡BpictureBoxªº¤j¤p¡A¥H²Å¦X¹Ï¤ù¤j¤p¡G
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
int width = image.Width;
int height = image.Height;
this.ClientSize = new Size(width + 100, height + 100);
this.pictureBox1.Size = new Size(width, height);
pictureBox1.Image = image;


­×§ï¹Ï¤ù¤j¤p
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
ImageFormat format = image.RawFormat;
int width = 800; //¼e«×
int heigt = 600; //°ª«×
Bitmap imageoutput = new Bitmap(image, width, heigt); //¿é¥X¤@­Ó·s¹Ï¤ù
imageoutput.Save("C:\______test_vcs\bear2.jpg", format); //¦sÀÉ¸ô®|,®æ¦¡
//ÄÀ©ñ¸ê·½
image.Dispose();
imageoutput.Dispose();


#region ¦Û©w¤èªk:´£¨ú¹Ï¤ùÃC¦â
//´£¨ú¹Ï¤ù¤¤ªºÃC¦â¥Î§@PictureBoxªº­I´º¦â
private void ExtractPictureColor()
{
	Color color = new Bitmap(pictureBox1.Image).GetPixel(150, 150);
	//±N´£¨ú¨ìªºÃC¦âÀ³¥Î¨ìPictureBoxªº­I´º
	pictureBox1.BackColor = color;
}
#endregion



¥t¦s·s¹Ïªº®æ¦¡¡G

IMG_20170214_102309.jpg	//¤â¾÷·Ó¬ÛÀÉ®×


            string str = System.Windows.Forms.Application.StartupPath;
            image.Save("c:\\aabbcc.jpeg");
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg", ImageFormat.Jpeg);

             string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

´ú¸Õµô¤Á¹Ï¤ù

            //§ì¿Ã¹õ¬Y°Ï¶ô¬°ÀÉ®×
            Image image = new Bitmap(410, 410);   //«Å§iImageÃþ§O
            Graphics g = Graphics.FromImage(image);
            g.CopyFromScreen(new Point(340, 255), new Point(0, 0), new Size(410, 410));
            //¨ú±o¿Ã¹õ¤Wx=340 y=255¬°¥ª¤W¨¤¡Aªø¼e¬°410ªº°Ï°ì
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //this.pictureBox1.Image = image;
            image.Save("c:\\aabbcc.jpeg");    //§â¹Ï¤ù¦s°_¨Ó

            richTextBox1.Text += "¤wºI¹Ï¦sÀÉ§¹¦¨\n";



            //«Ø¥ßªÅ¥Õµe¥¬
            Bitmap bmpCanvas = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //¨ú±oµe¥¬ªºÃ¸¹Ïª«¥ó¥Î¥HÃ¸¹Ï¡C
            Graphics g = Graphics.FromImage(bmpCanvas);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //±Nµô¤Á¥Xªº¯x§Î¦s¦¨JPG¹ÏÀÉ¡C
            Image image = (Image)bmpCanvas;
            string str = System.Windows.Forms.Application.StartupPath;
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".jpg", ImageFormat.Jpeg);

            richTextBox1.Text += "¤wºI¹Ï¦sÀÉ§¹¦¨\n";


            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(pictureBox1.Image);



Point / PointF µ²ºc
Size / SizeF µ²ºc
Rectangle / RectangleF µ²ºc

¶î¨êbrush¡G¥Î¨Ó¶ñº¡¤@¶ô°Ï°ì


¥Î¦h­ÓÂI¡A²Õ¦X¦¨¤@­Ó°}¦C¡G
    Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };


vcs draw

1. µeÂI
2. µeª½½u³s½u
3. µe¦±½u³s½u
µe¶ê¡B¾ò¶ê¡B©·§Î
µeªø¤è§Î

4. µe¦r
5. µe¹Ï


²Ê½u¡B¦â½u


°ò¥»ªì©l¤Æ»yªk


©Ò¦³µe¹Ï«ü¥O



Ãþ¦üªº»yªk¡A°Ñ¼Æ³£¬O(pen, X, Y, W, H)

µe¹Ï«ü¥O¾ã²z¡G	¶¶§Ç¡Gª½½u¡Bª½½u³s½u¡B¦±½u¡B¯x§Î¡B¾ò¶ê§Î¡B


DrawLine(new Pen(Brushes.Black, 5), px1, px2);
DrawLines(redPen, curvePoints);	//µeª½½u³s½u
DrawCurve(redPen, curvePoints);	//µe¦±½u

DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

DrawRectangle(blackPen, 10, 10, 100, 50);


DrawEllipse
DrawRectangle(myPen, X, Y, W, H);


DrawRectangles(new Pen(Brushes.Red, 3), R);	//µe¦h­ÓRectangles

DrawArc

DrawLine(myPen, x1, y1, x2, y2);
DrawLine(myPen, new Point(x1, y1), new Point(x2, y2));




µeª½½u³æ¤@½u
µeª½½u³s½u
µe¦±½u
µeªø¤è§Î
Ã¸»s¹ê¤ß¯x§Î
µe¦r¦ê
µe¹Ï



DrawArc( )¨ç¼Æªº¥Îªk»P¾ò¶êªº¬Û¦ü¡A¥u¬O«á­±¦h¤F¨â­Ó¿é¤J°Ñ¼Æ


DrawArc(Pen µeµ§,int ¥ª¤W¨¤x,int ¥ª¤W¨¤y,int ¼e«×,int °ª«×,int °_©l¨¤«×,int ±½´y¨¤«×);
DrawPie(Pen µeµ§,int ¥ª¤W¨¤x,int ¥ª¤W¨¤y,int ¼e«×,int °ª«×,int °_©l¨¤«×,int ±½´y¨¤«×);

DrawPolygon(Pen µeµ§, PointF[]  ÂI®y¼Ð°}¦C);	//¦hÃä§Î

DrawEllipse(blackPen, x, y, width, height);


¤G¡B
private void DrawEllipseRectangle(PaintEventArgs e)
{

    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    Rectangle rect = new Rectangle(0, 0, 200, 100);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}


¤T¡B
private void DrawEllipseRectangleF(PaintEventArgs e)
{
    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    RectangleF rect = new RectangleF(0.0F, 0.0F, 200.0F, 100.0F);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}

¥|¡B
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







¦³¤TºØ¤èªk¥i¥H«Ø¥ßGraphicsª«¥ó¡G
¤@¡B³q¹LPaint¨Æ¥ó³B²z¹Lµ{¤¤ªºPaintEventArgs«Ø¥ßGraphicsª«¥ó
Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs)
Dim g As Graphics = e.Graphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("ªF«n¬ì§Þ¤j¾Ç", Me.Font, mBrush, 50.0F, 50.0F)

¤G¡BCreateGraphics ¤èªk

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Me.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("ªF«n¬ì§Þ¤j¾Ç", Me.Font, mBrush, 50.0F, 50.0F)
End Sub

·íµM¡A§Ú­Ì¤]¥i¥H¤Þ¥ÎButton«ö¶sªºGraphicsª«¥ó¡A¦p¤U©Ò¥Ü¡G
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Button1.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("ªF«n¬ì§Þ¤j¾Ç", Me.Font, mBrush, 0.0F, 0.0F)
End Sub

¤T¡B±q Image ¹ï¶H«Ø¥ß
¥t¥~¡A§Ú­ÌÁÙ¥i¥H±q¥Ñ Image Ãþ¬£¥Íªº¥ô¦óª«¥ó«Ø¥ß¹Ï§Îª«¥ó¡C
½Õ¥Î Graphics.FromImage ¤èªk¡A´£¨Ñ­n±q¨ä¤¤«Ø¥ß Graphics ª«¥óªº Image ÅÜ¼Æªº¦WºÙ¡A¦p¤U¥N½X©Ò¥Ü¡G
Dim myBitmap as New Bitmap("C:\myPic.bmp")
Dim g as Graphics = Graphics.FromImage(myBitmap)
·í Graphics ª«¥ó«Ø¥ß«á¡A§Ú­Ì¥i¥Î¥¦Ã¸»s½u±ø©M§Îª¬¡B§e²{¤å¥»©ÎÅã¥Ü»P¾Þ§@¹Ï¹³¡C»P Graphics ª«¥ó¤@°_¨Ï¥Îªº¥DÅéª«¥ó¦³¡G
¡E	Pen Ãþ - ¥Î©óÃ¸»s½u±ø¡B¤Ä°Ç§Îª¬½ü¹ø©Î§e²{¨ä¥L´X¦óªí¥Ü§Î¦¡¡C
¡E	Brush Ãþ - ¥Î©ó¶ñ¥R¹Ï§Î°Ï°ì¡A¦p¹ê¤ß§Îª¬¡B¹Ï¹³©Î¤å¥»¡C
¡E	Font Ãþ - ´£¨Ñ¦³Ãö¦b§e²{¤å¥»®É­n¨Ï¥Î¤°»ò§Îª¬ªº»¡©ú¡C
¡E	Color µ²ºc - ªí¥Ü­nÅã¥Üªº¤£¦PÃC¦â¡C

Pen¡BBrush¡BColorÃþ§Ú­Ì±N¦b¡mµeµ§¡Bµe¨ê©MÃC¦â¡n¤¤¶i¦æ¤F¤¶²Ð¡A¤U­±§Ú­ÌÄ~Äò¬Ý¡mÁA¸ÑFontÃþ¡n




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


¤U¦C½d¨Ò·|Ã¸»s¦b¨ä¥ª¤W¨¤ªº¯x§Î ¡]10¡A10¡^¡C ¯x§Îªº¼e«×¬° 100¡A°ª«×¬° 50¡C
²Ä¤G­Ó¤Þ¼Æ¶Ç»¼µ¹ Pen «Øºc¨ç¦¡ªí¥Üµeµ§¼e«×¬° 5 ¹³¯À¡C
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
g.DrawRectangle(blackPen, 10, 10, 100, 50);


Graphics ¤èªk ¤§ DrawEllipse
¤@¡B
DrawEllipse(Pen, Int32, Int32, Int32, Int32)	Ã¸»s¥Ñ¯x§Î¥ª¤W¨¤¡B°ª«×©M¼e«×ªº®y¼Ð«ü©w¤§¶g®Ø©Ò©w¸qªº¾ò¶ê§Î¡C
¤G¡B
DrawEllipse(Pen, Rectangle)			Ã¸»s¥Ñ¬É­­ Rectangle µ²ºc«ü©wªº¾ò¶ê§Î¡C
¤T¡B
DrawEllipse(Pen, RectangleF)			Ã¸»s¥Ñ¬É­­ RectangleF ©w¸qªº¾ò¶ê§Î¡C
¥|¡B
DrawEllipse(Pen, Single, Single, Single, Single)Ã¸»s¥Ñ¤@¹ï®y¼Ð¡B°ª«×©M¼e«×©Ò«ü©wªº¶g®Ø©w¸qªº¾ò¶ê§Î¡C


¯x§Îªº¼gªk¡G
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


private void DrawXY()	//„øX…lY…l
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

private void DrawXY()	//„øX…lY…l
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
        private void DrawXLine()„øX…l¥­¦æˆE
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
        private void DrawYLine()„øX…l¨è«×
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






Pen°Ñ¼Æ

 ¡VPenÃþ§O°£¤F¥i¥H³]©w°ò¥»ªºµ§²Ê¤Îµ§¦â¤§¥~¡AÁÙ¯à³]©wÃ¸»sªº¤è¦¡¡A¦pµeª½½u©Î¬Oµê½u¡A¥H¤Î½u¬qªº¼Ë¦¡


Pen Ãþ§O	©w¸q¥Î¨ÓÃ¸»sª½½u»P¦±½uªºª«¥ó¡C

Penªº¼gªk¡G
Pen µeµ§ = new Pen(µeµ§ÃC¦â, µeµ§²Ê²Ó);
Pen pen  = new Pen(Color.Green, 3);

§ïÅÜµeµ§ÄÝ©Ê¡G
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



PenÃþ§O¼gªk¡G
1.Pen(Color color);
Pen  BluePen  =  new  Pen(Color.Blue,2);
2.Pen(Color color, float width);
Pen  ColorPen  =  new  Pen(Color.FromARGB(210,100,70),5);




Pen Ãþ§O	©w¸q¥Î¨ÓÃ¸»sª½½u»P¦±½uªºª«¥ó¡C


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

Penªº¼gªk¡G
Pen µeµ§ = new Pen(µeµ§ÃC¦â, µeµ§²Ê²Ó);
Pen pen  = new Pen(Color.Green, 3);

§ïÅÜµeµ§ÄÝ©Ê¡G
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



-------------------------------------------------------------------------------------------------------------
µe¹Ï°ò¥»»yªk¾ã²z¡G

¦bForm¤W¯Âµe¹Ï

«Å§i¡A¼g¦bForm1¤§¥~¡G
        Graphics g;	// Ã¸¹Ï°Ï
        Pen pen;	// µeµ§
        Font font;
        Brush brush;
        public Form1()
        {
		InitializeComponent();
		//ªì©l¤Æ¡A¼g¦bInitializeComponent();¤§«á¡G
		g = this.CreateGraphics();	// ¨ú±oÃ¸¹Ï°Ïª«¥ó
		pen = new Pen(Color.Black, 3);	// ³]©wµeµ§¬°¶Â¦â¡B²Ê²Ó¬° 3 ÂI¡C
		font = new Font("¼Ð·¢Åé", 16);
		brush = new SolidBrush(Color.Black);
        }

¨Ï¥Î¡G
	g.DrawLine(pen, new Point(1, 1), new Point(300, 100));
	g.DrawRectangle(pen, new Rectangle(50, 50, 100, 100));
	g.DrawString("Hello! §A¦n¡I", font, brush, new PointF(150.0F, 150.0F));
	g.DrawString("Hello! §A¦n¡I", font, mBrush, 50.0F, 50.0F)

µe¤W¤@¹Ï¡G
	Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
	g.DrawImage(image, new Point(200, 200));

¦bpictureBox¡Bpanel¤W¯Âµe¹Ï¡A
§â
	g = this.CreateGraphics();	// ¨ú±oÃ¸¹Ï°Ïª«¥ó
§ï¦¨¡G
	g = pictureBox1.CreateGraphics();

	g = panel1.CreateGraphics();


¼g¦b¤@°_¡A¥Î§¹¼o±ó¡G
// Create a Graphics object for the Control.
Graphics g = panel1.CreateGraphics();
//¨Ï¥Î
g.xxxx
// Clean up the Graphics object.
g.Dispose();

¼g¦b¤@°_¡A¥Î§¹¼o±ó¡G
SolidBrush myBrush = new SolidBrush(Color.Red);
Graphics g = this.CreateGraphics();
g.FillRectangle(myBrush, new Rectangle(0, 0, 200, 300));
g.FillEllipse(myBrush, new Rectangle(0, 0, 200, 300));	//Ã¸»s¹ê¤ß¾ò¶ê§Î
myBrush.Dispose();
g.Dispose();




¦bpictureBox¤WÅã¥Ü¤@¹Ï¡A¨Ã¦b¹Ï¤W§@µe
«Å§i¡A¼g¦bForm1¤§¥~¡G
        Graphics g;	// Ã¸¹Ï°Ï

        public Form1()
        {
            InitializeComponent();
            Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
            pictureBox1.Image = image;
            g = Graphics.FromImage(pictureBox1.Image);
        }

¨Ï¥Î¡G	//»Ý­n.Refresh()
	g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
	pictureBox1.Refresh();

	g.DrawRectangle(new Pen(Color.Black), new Rectangle(200, 200, 100, 100));
	pictureBox1.Refresh();


§ïÅÜ­I´º¦â
g.Clear(Color.White);

«ì´_¹w³]ªº­I´º¦â
g.Clear(BackColor);

