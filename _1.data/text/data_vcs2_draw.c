/**********************************************************
 * Filename	:	vcs_data3_draw.c
 * Description	:	畫圖、圖片處理相關
 **********************************************************/


應該要能區分OnPaint與_Paint的差別
protected override void OnPaint(PaintEventArgs e)
private void Form1_Paint(object sender, PaintEventArgs e)


框線繪圖，用Pen

區域繪圖，用Brush


good draw article:
C#初體驗，畫圖的讀、寫、顯示
https://darkblack01.blogspot.tw/2014/03/c.html



利用C#來做到圖檔縮圖的方式
http://demo.tc/post/95


C#對Image縮放、旋轉與裁切
https://gnehcic.azurewebsites.net/c%E5%B0%8Dimage%E7%B8%AE%E6%94%BE%E3%80%81%E6%97%8B%E8%BD%89%E8%88%87%E8%A3%81%E5%88%87/


C#圖像處理(各種旋轉、改變大小、柔化、銳化、霧化、底片、浮雕
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/113208.html

C#圖像處理(各種旋轉、改變大小、柔化、銳化、霧化、底片、浮雕、黑白、濾鏡效果)
http://www.zendei.com/article/7891.html


(C#)Resize等比例縮放圖片





一般程式師會用下面幾種方式，比如將表單的Double Buffered屬性設置為true，或者通過繼承或者反射機制，將pictureBox的Double Buffered屬性設置為true

-註-
雙緩衝（double buffering）：

雙重的圖形輸出記憶體，以動態的方式配合螢幕輸出的速率。當一組記憶體正在讀出的時候，另一組則在寫入，如此輪流讀寫的方式使得螢幕可以即時地更新畫面資料。





畫圖、顯示圖片、在圖片上作畫


Form上		可以 畫圖
Panel上		可以 畫圖
PictureBox上	可以 畫圖、顯示圖片
Form上 		可以 畫圖
Label 		可以 	顯示圖片


圖片處理：
放大縮小、裁切、轉檔、、、、、、





圖片處理

C:\______test_vcs\bear.jpg
string Path = "C:\\______test_vcs_file_name2\\aaaa\\bbbb";

string destFileName = @"c:\______test_vcs\picture1a.jpg";

Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
pictureBox1.Image = image;
string src = @"C:\______test_vcs\bear.jpg";


轉換圖像格式
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


取得圖片大小、改變Form、pictureBox的大小，以符合圖片大小：
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
int width = image.Width;
int height = image.Height;
this.ClientSize = new Size(width + 100, height + 100);
this.pictureBox1.Size = new Size(width, height);
pictureBox1.Image = image;


修改圖片大小
Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
ImageFormat format = image.RawFormat;
int width = 800; //寬度
int heigt = 600; //高度
Bitmap imageoutput = new Bitmap(image, width, heigt); //輸出一個新圖片
imageoutput.Save("C:\______test_vcs\bear2.jpg", format); //存檔路徑,格式
//釋放資源
image.Dispose();
imageoutput.Dispose();


#region 自定方法:提取圖片顏色
//提取圖片中的顏色用作PictureBox的背景色
private void ExtractPictureColor()
{
	Color color = new Bitmap(pictureBox1.Image).GetPixel(150, 150);
	//將提取到的顏色應用到PictureBox的背景
	pictureBox1.BackColor = color;
}
#endregion



另存新圖的格式：

IMG_20170214_102309.jpg	//手機照相檔案


            string str = System.Windows.Forms.Application.StartupPath;
            image.Save("c:\\aabbcc.jpeg");
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg", ImageFormat.Jpeg);

             string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

測試裁切圖片

            //抓螢幕某區塊為檔案
            Image image = new Bitmap(410, 410);   //宣告Image類別
            Graphics g = Graphics.FromImage(image);
            g.CopyFromScreen(new Point(340, 255), new Point(0, 0), new Size(410, 410));
            //取得螢幕上x=340 y=255為左上角，長寬為410的區域
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //this.pictureBox1.Image = image;
            image.Save("c:\\aabbcc.jpeg");    //把圖片存起來

            richTextBox1.Text += "已截圖存檔完成\n";



            //建立空白畫布
            Bitmap bmpCanvas = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //取得畫布的繪圖物件用以繪圖。
            Graphics g = Graphics.FromImage(bmpCanvas);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //將裁切出的矩形存成JPG圖檔。
            Image image = (Image)bmpCanvas;
            string str = System.Windows.Forms.Application.StartupPath;
            image.Save(str + "\\" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".jpg", ImageFormat.Jpeg);

            richTextBox1.Text += "已截圖存檔完成\n";


            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(pictureBox1.Image);



Point / PointF 結構
Size / SizeF 結構
Rectangle / RectangleF 結構

塗刷brush：用來填滿一塊區域


用多個點，組合成一個陣列：
    Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };


vcs draw

1. 畫點
2. 畫直線連線
3. 畫曲線連線
畫圓、橢圓、弧形
畫長方形

4. 畫字
5. 畫圖


粗線、色線


基本初始化語法


所有畫圖指令



類似的語法，參數都是(pen, X, Y, W, H)

畫圖指令整理：	順序：直線、直線連線、曲線、矩形、橢圓形、


DrawLine(new Pen(Brushes.Black, 5), px1, px2);
DrawLines(redPen, curvePoints);	//畫直線連線
DrawCurve(redPen, curvePoints);	//畫曲線

DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

DrawRectangle(blackPen, 10, 10, 100, 50);


DrawEllipse
DrawRectangle(myPen, X, Y, W, H);


DrawRectangles(new Pen(Brushes.Red, 3), R);	//畫多個Rectangles

DrawArc

DrawLine(myPen, x1, y1, x2, y2);
DrawLine(myPen, new Point(x1, y1), new Point(x2, y2));




畫直線單一線
畫直線連線
畫曲線
畫長方形
繪製實心矩形
畫字串
畫圖



DrawArc( )函數的用法與橢圓的相似，只是後面多了兩個輸入參數


DrawArc(Pen 畫筆,int 左上角x,int 左上角y,int 寬度,int 高度,int 起始角度,int 掃描角度);
DrawPie(Pen 畫筆,int 左上角x,int 左上角y,int 寬度,int 高度,int 起始角度,int 掃描角度);

DrawPolygon(Pen 畫筆, PointF[]  點座標陣列);	//多邊形

DrawEllipse(blackPen, x, y, width, height);


二、
private void DrawEllipseRectangle(PaintEventArgs e)
{

    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    Rectangle rect = new Rectangle(0, 0, 200, 100);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}


三、
private void DrawEllipseRectangleF(PaintEventArgs e)
{
    // Create pen.
    Pen blackPen = new Pen(Color.Black, 3);

    // Create rectangle for ellipse.
    RectangleF rect = new RectangleF(0.0F, 0.0F, 200.0F, 100.0F);

    // Draw ellipse to screen.
    e.Graphics.DrawEllipse(blackPen, rect);
}

四、
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







有三種方法可以建立Graphics物件：
一、通過Paint事件處理過程中的PaintEventArgs建立Graphics物件
Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs)
Dim g As Graphics = e.Graphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("東南科技大學", Me.Font, mBrush, 50.0F, 50.0F)

二、CreateGraphics 方法

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Me.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("東南科技大學", Me.Font, mBrush, 50.0F, 50.0F)
End Sub

當然，我們也可以引用Button按鈕的Graphics物件，如下所示：
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Dim g As Graphics = Button1.CreateGraphics
Dim mBrush As New SolidBrush(Color.Red)
g.DrawString("東南科技大學", Me.Font, mBrush, 0.0F, 0.0F)
End Sub

三、從 Image 對象建立
另外，我們還可以從由 Image 類派生的任何物件建立圖形物件。
調用 Graphics.FromImage 方法，提供要從其中建立 Graphics 物件的 Image 變數的名稱，如下代碼所示：
Dim myBitmap as New Bitmap("C:\myPic.bmp")
Dim g as Graphics = Graphics.FromImage(myBitmap)
當 Graphics 物件建立後，我們可用它繪製線條和形狀、呈現文本或顯示與操作圖像。與 Graphics 物件一起使用的主體物件有：
‧	Pen 類 - 用於繪製線條、勾勒形狀輪廓或呈現其他幾何表示形式。
‧	Brush 類 - 用於填充圖形區域，如實心形狀、圖像或文本。
‧	Font 類 - 提供有關在呈現文本時要使用什麼形狀的說明。
‧	Color 結構 - 表示要顯示的不同顏色。

Pen、Brush、Color類我們將在《畫筆、畫刷和顏色》中進行了介紹，下面我們繼續看《瞭解Font類》




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


下列範例會繪製在其左上角的矩形 （10，10）。 矩形的寬度為 100，高度為 50。
第二個引數傳遞給 Pen 建構函式表示畫筆寬度為 5 像素。
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
g.DrawRectangle(blackPen, 10, 10, 100, 50);


Graphics 方法 之 DrawEllipse
一、
DrawEllipse(Pen, Int32, Int32, Int32, Int32)	繪製由矩形左上角、高度和寬度的座標指定之週框所定義的橢圓形。
二、
DrawEllipse(Pen, Rectangle)			繪製由界限 Rectangle 結構指定的橢圓形。
三、
DrawEllipse(Pen, RectangleF)			繪製由界限 RectangleF 定義的橢圓形。
四、
DrawEllipse(Pen, Single, Single, Single, Single)繪製由一對座標、高度和寬度所指定的週框定義的橢圓形。


矩形的寫法：
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


private void DrawXY()	//画X轴Y轴
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

private void DrawXY()	//画X轴Y轴
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
        private void DrawXLine()画X轴平行线
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
        private void DrawYLine()画X轴刻度
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






Pen參數

 –Pen類別除了可以設定基本的筆粗及筆色之外，還能設定繪製的方式，如畫直線或是虛線，以及線段的樣式


Pen 類別	定義用來繪製直線與曲線的物件。

Pen的寫法：
Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);
Pen pen  = new Pen(Color.Green, 3);

改變畫筆屬性：
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



Pen類別寫法：
1.Pen(Color color);
Pen  BluePen  =  new  Pen(Color.Blue,2);
2.Pen(Color color, float width);
Pen  ColorPen  =  new  Pen(Color.FromARGB(210,100,70),5);




Pen 類別	定義用來繪製直線與曲線的物件。


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

Pen的寫法：
Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);
Pen pen  = new Pen(Color.Green, 3);

改變畫筆屬性：
pen.Color = Color.Red;
pen.Width = 2;

g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
Pen greenPen = new Pen(Color.Green, 3);
Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



-------------------------------------------------------------------------------------------------------------
畫圖基本語法整理：

在Form上純畫圖

宣告，寫在Form1之外：
        Graphics g;	// 繪圖區
        Pen pen;	// 畫筆
        Font font;
        Brush brush;
        public Form1()
        {
		InitializeComponent();
		//初始化，寫在InitializeComponent();之後：
		g = this.CreateGraphics();	// 取得繪圖區物件
		pen = new Pen(Color.Black, 3);	// 設定畫筆為黑色、粗細為 3 點。
		font = new Font("標楷體", 16);
		brush = new SolidBrush(Color.Black);
        }

使用：
	g.DrawLine(pen, new Point(1, 1), new Point(300, 100));
	g.DrawRectangle(pen, new Rectangle(50, 50, 100, 100));
	g.DrawString("Hello! 你好！", font, brush, new PointF(150.0F, 150.0F));
	g.DrawString("Hello! 你好！", font, mBrush, 50.0F, 50.0F)

畫上一圖：
	Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
	g.DrawImage(image, new Point(200, 200));

在pictureBox、panel上純畫圖，
把
	g = this.CreateGraphics();	// 取得繪圖區物件
改成：
	g = pictureBox1.CreateGraphics();

	g = panel1.CreateGraphics();


寫在一起，用完廢棄：
// Create a Graphics object for the Control.
Graphics g = panel1.CreateGraphics();
//使用
g.xxxx
// Clean up the Graphics object.
g.Dispose();

寫在一起，用完廢棄：
SolidBrush myBrush = new SolidBrush(Color.Red);
Graphics g = this.CreateGraphics();
g.FillRectangle(myBrush, new Rectangle(0, 0, 200, 300));
g.FillEllipse(myBrush, new Rectangle(0, 0, 200, 300));	//繪製實心橢圓形
myBrush.Dispose();
g.Dispose();




在pictureBox上顯示一圖，並在圖上作畫
宣告，寫在Form1之外：
        Graphics g;	// 繪圖區

        public Form1()
        {
            InitializeComponent();
            Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic3.jpg");
            pictureBox1.Image = image;
            g = Graphics.FromImage(pictureBox1.Image);
        }

使用：	//需要.Refresh()
	g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
	pictureBox1.Refresh();

	g.DrawRectangle(new Pen(Color.Black), new Rectangle(200, 200, 100, 100));
	pictureBox1.Refresh();


改變背景色
g.Clear(Color.White);

恢復預設的背景色
g.Clear(BackColor);

