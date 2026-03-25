using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat, ImageLockMode, Encoder, ImageCodecInfo, ImageAttributes
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Collections;//for Hashtable

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        /*
        //直接寫一個OnPaint在此, 取代Form1_Paint
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);
        }
        */

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(600, 600);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1560, 710);
            this.Text = "vcs_Mix03_draw_image";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                        filenames.Add(fullname);
                    }
                }
            }
        }

        // See: Search for files that match multiple patterns in C#
        //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
        // Search for files matching the patterns.
        private List<string> FindFiles(string dir_name, string patterns, bool search_subdirectories)
        {
            // Make the result list.
            List<string> files = new List<string>();

            // Get the patterns.
            string[] pattern_array = patterns.Split(';');

            // Search.
            SearchOption search_option = SearchOption.TopDirectoryOnly;
            if (search_subdirectories) search_option = SearchOption.AllDirectories;
            foreach (string pattern in pattern_array)
            {
                foreach (string filename in Directory.GetFiles(dir_name, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //撈出所有圖片檔 並存成一個List 1

            //撈出所有圖片檔 並存成一個List
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            filenames.Clear();

            GetAllFiles(foldername);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //撈出所有圖片檔 並存成一個List 2

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";

            filenames.Clear();

            if (Directory.Exists(foldername) == false)
            {
                richTextBox1.Text += "圖片資料夾不存在, 離開\n";
                return;
            }

            // Load the list of files.
            filenames = FindFiles(foldername, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);

            for (int i = 0; i < filenames.Count; i++)
            {
                richTextBox1.Text += "get file \t" + filenames[i] + "\n";
            }
            richTextBox1.Text += "共有 " + filenames.Count.ToString() + " 個檔案\n";
        }


        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string dir_name = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony2";

            // The list of files we will pick from.
            List<string> FileNames = new List<string>();

            // Load the list of files.
            if (Directory.Exists(dir_name))
            {
                FileNames = FindFiles(dir_name, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);
            }
            else
            {
                FileNames = new List<string>();
            }

            for (int i = 0; i < FileNames.Count; i++)
            {
                richTextBox1.Text += "get file \t" + FileNames[i] + "\n";
            }

            Random Rand = new Random();

            // Repeat until we succeed or run out of files.
            for (; ; )
            {
                // Pick a random image.
                int file_num = Rand.Next(FileNames.Count);

                // Try to use that image.
                try
                {
                    richTextBox1.Text += "使用圖片 : " + FileNames[file_num] + "\n";
                    // Set the desktop picture.
                    //DisplayPicture(FileNames[file_num], checkBox1.Checked);
                    break;
                }
                catch
                {
                    // This file doesn't work. Remove it from the list.
                    FileNames.RemoveAt(file_num);

                    // If there are no more files, stop trying.
                    if (FileNames.Count == 0)
                    {
                        break;
                    }
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //放大圖片
            //由 r X r 放大到 R X R

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Bitmap bitmap2 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap2);    //以記憶體圖像 bitmap2 建立 記憶體畫布g

            int x_st = 255;
            int y_st = 115;
            int r = 100;
            int R = 200;

            Rectangle rect1 = new Rectangle(x_st - r / 2, y_st - r / 2, r, r); //要放大的區域, 來源矩形
            Rectangle rect2 = new Rectangle(x_st - R / 2, y_st - R / 2, R, R);  //貼上的地方, 目標矩形

            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);  // 貼上原圖
            g.DrawImage(bitmap1, rect2, rect1, GraphicsUnit.Pixel);

            g.DrawRectangle(Pens.Red, rect1);
            g.DrawRectangle(Pens.Green, rect2);

            pictureBox1.Image = bitmap2;
        }


        //聲明一個API函數
        [System.Runtime.InteropServices.DllImportAttribute("gdi32.dll")]
        private static extern bool BitBlt(IntPtr hdcDest, int nXDest, int nYDest, int nWidth, int nHeight, IntPtr hdcSrc, int nXSrc, int nYSrc, System.Int32 dwRop);

        public void SnatchScreen(Form Frm, string FilePath)
        {
            Point Var_Loc = Frm.Location;//取得目前視窗的位置

            richTextBox1.Text += "aaaa : " + Var_Loc.ToString() + "\n";
            richTextBox1.Text += "bbbb : " + this.Location.ToString() + "\n";

            int Frm_left = -Var_Loc.X;
            int Frm_right = -Var_Loc.Y;

            Rectangle Var_rect = new Rectangle();//實例化Rectangle類
            Var_rect = Screen.GetWorkingArea(Frm);//獲得目前螢幕的大小
            Graphics g = Frm.CreateGraphics();//建立一個以目前螢幕為模板的圖片
            Image Var_Image = new Bitmap(Var_rect.Width, Var_rect.Height, g);//建立以螢幕大小為標準的位圖 
            Graphics Var_G_Image = Graphics.FromImage(Var_Image);//根據圖片實例化Graphics類
            IntPtr Screen_dc = g.GetHdc();//得到螢幕的句柄
            IntPtr Bitmap_dc = Var_G_Image.GetHdc();//得到Bitmap的句柄
            BitBlt(Bitmap_dc, 0, 0, Var_rect.Width, Var_rect.Height, Screen_dc, Frm_left, Frm_right, 13369376);//呼叫此API函數，完成螢幕擷取
            g.ReleaseHdc(Screen_dc);//釋放掉螢幕的句柄
            Var_G_Image.ReleaseHdc(Bitmap_dc);//釋放掉Bitmap的句柄
            ImageFormat ImageF = ImageFormat.Jpeg;//實例化ImageFormat類

            ImageF = ImageFormat.Jpeg;
            Var_Image.Save(FilePath, ImageF);//以指定的文件格式來保存
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //本程式截圖

            //執行螢幕截圖的操作
            //本程式截圖
            SnatchScreen(this, "tmp_aaaaaaa.jpg");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //Rectangle 的 Union
            Graphics g = this.pictureBox1.CreateGraphics();

            Rectangle rec1 = new Rectangle(100, 10, 200, 200);
            Rectangle rec2 = new Rectangle(150, 100, 200, 200);
            Rectangle rec3 = new Rectangle(30, 150, 200, 200);
            g.DrawRectangle(Pens.Red, rec1);
            g.DrawRectangle(Pens.Green, rec2);
            g.DrawRectangle(Pens.Blue, rec3);

            Rectangle new_rect = Rectangle.Union(rec1, rec2);
            new_rect = Rectangle.Union(new_rect, rec3);
            g.DrawRectangle(Pens.Magenta, new_rect);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //亂畫一通
            Graphics g = pictureBox1.CreateGraphics();

            //畫箭頭
            Pen myPen2 = new Pen(Color.Blue, 20);
            myPen2.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(myPen2, 20, 100, 300, 100); // 繪製箭形直線

            //3030

            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString("畫字串畫直的", this.Font, new SolidBrush(Color.Black), 300, 100, drawFormat);

            //6060

            Pen p = new Pen(Color.Red);  // 建立一支紅色的筆

            g.DrawEllipse(p, 90, 30, 90, 90);      // 畫圓
            g.DrawLine(p, 90, 50, 180, 100);       // 畫線
            g.DrawArc(p, 90, 30, 90, 90, 0, 250);  // 畫弧形

            //3030

            //從pictureBox開始畫圖

            //Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類

            //g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 256);

            Point[] curvePoints = new Point[220];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 220; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = i * 2;
            }

            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線

            //3030

        }

        //繪製圓角矩形 DrawRoundRetangle
        private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius)
        {
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

        private void button12_Click(object sender, EventArgs e)
        {
            //交集聯集互斥

            Graphics g = pictureBox1.CreateGraphics();

            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int Cx = 200;
            int Cy = 70;
            int R = 60;
            int dd = 30;

            g.DrawString("聯集", new Font("標楷體", 24), new SolidBrush(Color.Blue), new PointF(5, Cy));

            GraphicsPath gp1 = new GraphicsPath(); // 圖形軌跡
            gp1.AddEllipse(Cx - dd - R, Cy - R, R * 2, R * 2);

            GraphicsPath gp2 = new GraphicsPath(); // 圖形軌跡
            gp2.AddEllipse(Cx + dd - R, Cy - R, R * 2, R * 2);

            Region r1 = new Region(gp1); // Region 區域表面 物件
            Region r2 = new Region(gp2); // Region 區域表面 物件

            r1.Union(r2);  // r1 = r1 + r2  聯集

            g.FillRegion(Brushes.Silver, r1); // r1 區域表面 繪出
            g.DrawPath(Pens.Black, gp1); // 圖形軌跡 繪出
            g.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出

            //6060

            Cx = 200;
            Cy = 200;

            g.DrawString("交集\n排除", new Font("標楷體", 24), new SolidBrush(Color.Blue), new PointF(5, Cy));

            gp1 = new GraphicsPath(); // 圖形軌跡
            gp1.AddEllipse(Cx - dd - R, Cy - R, R * 2, R * 2);

            gp2 = new GraphicsPath(); // 圖形軌跡
            gp2.AddEllipse(Cx + dd - R, Cy - R, R * 2, R * 2);

            r1 = new Region(gp1); // Region 區域表面 物件
            r2 = new Region(gp2); // Region 區域表面 物件
            Region r3 = new Region(gp1); // Region 區域表面 物件

            r3.Intersect(r2);  // r3 = r1 - r2   交集
            r1.Exclude(r3);    // r1 = r1 - r3   排除
            r2.Exclude(r3);    // r2 = r2 - r3   排除

            g.FillRegion(Brushes.Red, r1);  // r1 區域表面  繪出
            g.FillRegion(Brushes.Blue, r2); // r2 區域表面 繪出
            g.FillRegion(Brushes.Yellow, r3); // r3 區域表面 繪出

            g.DrawPath(Pens.Black, gp1); // 圖形軌跡 繪出
            g.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出

            //6060

            Cx = 200;
            Cy = 330;

            g.DrawString("互斥或", new Font("標楷體", 24), new SolidBrush(Color.Blue), new PointF(5, Cy));

            gp1 = new GraphicsPath(); // 圖形軌跡
            gp1.AddEllipse(Cx - dd - R, Cy - R, R * 2, R * 2);

            gp2 = new GraphicsPath(); // 圖形軌跡
            gp2.AddEllipse(Cx + dd - R, Cy - R, R * 2, R * 2);

            r1 = new Region(gp1); // Region 區域表面 物件
            r2 = new Region(gp2); // Region 區域表面 物件

            r1.Xor(r2);  // r1 = r1 + r2 - (r1 Intersect r2)  互斥

            g.FillRegion(Brushes.Silver, r1); // r1 區域表面  繪出
            g.DrawPath(Pens.Black, gp1); // 圖形軌跡 繪出
            g.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出
        }

        private void PaintImage(Graphics g)
        {
            //绘图
            GraphicsPath path = new GraphicsPath(new Point[]{ new Point(100,60),new Point(350,200),new Point(105,225),new Point(190,ClientRectangle.Bottom),
                new Point(50,ClientRectangle.Bottom),new Point(50,180)}, new byte[]{
                    (byte)PathPointType.Start,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Line,
                    (byte)PathPointType.Line});
            PathGradientBrush pgb = new PathGradientBrush(path);
            pgb.SurroundColors = new Color[] { Color.Green, Color.Yellow, Color.Red, Color.Blue, Color.Orange, Color.LightBlue };
            g.FillPath(pgb, path);
            g.DrawString("明日科技欢迎您", new Font("宋体", 18, FontStyle.Bold), new SolidBrush(Color.Red), new PointF(110, 20));
            g.DrawBeziers(new Pen(new SolidBrush(Color.Green), 2), new Point[] { new Point(220, 100), new Point(250, 180), new Point(300, 70), new Point(350, 150) });
            g.DrawArc(new Pen(new SolidBrush(Color.Blue), 5), new Rectangle(new Point(250, 170), new Size(60, 60)), 0, 360);
            g.DrawRectangle(new Pen(new SolidBrush(Color.Orange), 3), new Rectangle(new Point(240, 260), new Size(90, 50)));
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //畫圖 mix
            Bitmap localBitmap = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
            //创建位图实例
            Graphics bitmapGraphics = Graphics.FromImage(localBitmap);
            bitmapGraphics.Clear(BackColor);
            bitmapGraphics.SmoothingMode = SmoothingMode.AntiAlias;
            PaintImage(bitmapGraphics);
            Graphics g = Graphics.FromImage(localBitmap);
            g.DrawImage(localBitmap, 0, 0); //在窗体的画布中绘画出内存中的图像
            //bitmapGraphics.Dispose();
            //localBitmap.Dispose();
            //g.Dispose();

            pictureBox1.Image = localBitmap;
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}
