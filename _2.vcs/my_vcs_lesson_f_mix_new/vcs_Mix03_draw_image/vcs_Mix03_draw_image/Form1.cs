using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat, ImageLockMode, Encoder, ImageCodecInfo, ColorMatrix, ImageAttributes
using System.Drawing.Drawing2D;  // for GraphicsPath, Matrix, MatrixOrder
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

        //測試矩陣旋轉 ST
        PointF RotationMatrix(PointF pt, double theta)
        {
            float xx = (float)(Math.Cos(theta) * pt.X - Math.Sin(theta) * pt.Y);
            float yy = (float)(Math.Sin(theta) * pt.X + Math.Cos(theta) * pt.Y);

            return new PointF(xx, yy);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //測試矩陣旋轉
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 10);
            Point point1a = new Point(0, 0);
            Point point2a = new Point(500, 0);
            //g.DrawLine(p, point1a, point2a);

            p = new Pen(Color.Green, 10);

            double theta = Math.PI / 6;
            PointF point1aa = RotationMatrix(point1a, theta);
            PointF point2aa = RotationMatrix(point2a, theta);
            //g.DrawLine(p, point1aa, point2aa);
            richTextBox1.Text += "point1aa=" + point1aa + "\n";
            richTextBox1.Text += "point2aa=" + point2aa + "\n";

            PointF[] curvePoints = new PointF[8];    //一維陣列內有 8 個Point
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i].X = 50 * i;
                curvePoints[i].Y = 0;
            }
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 10);
            g.DrawLines(grayPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i] = RotationMatrix(curvePoints[i], theta);
            }

            g.DrawLines(redPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                g.FillEllipse(Brushes.Red, curvePoints[i].X - 10, curvePoints[i].Y - 10, 20, 20);
            }

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);
            Rectangle src_area = new Rectangle(100, 100, 100, 100);//要截取的矩形區域
            Rectangle dst_area = new Rectangle(400, 50, 100, 100);//要截取的矩形區域
            //g.DrawImage(bmp, dst_area, src_area, GraphicsUnit.Pixel);
            g.DrawImage(bmp, src_area, src_area, GraphicsUnit.Pixel);

            int x_st = 100;
            int y_st = 100;
            int w = 100;
            int h = 100;
            for (int j = 0; j < h; j++)
            {
                for (int i = 0; i < w; i++)
                {
                    Color clr = bitmap1.GetPixel(x_st + i, y_st + j);
                    PointF new_pt = RotationMatrix(new PointF(x_st + i, y_st + j), theta);
                    if ((new_pt.X > 0) && (new_pt.Y > 0))
                    {
                        bitmap1.SetPixel((int)new_pt.X, (int)new_pt.Y, clr);
                    }

                }
            }

            pictureBox1.Image = bitmap1;
        }

        //測試矩陣旋轉 SP

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

        float theta = 0; // 旋轉角度

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bm = new Bitmap(filename);

            theta = theta + 2;  // 旋轉角度 遞增

            Graphics g = this.pictureBox1.CreateGraphics();

            //畫布轉換矩陣的旋轉設定 - 在固定點自轉
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.pictureBox1.ClientSize.Height / 2;//

            g.ResetTransform(); // 畫布的矩陣 = 單位矩陣

            g.TranslateTransform(-bm.Width / 2, -bm.Height / 2, MatrixOrder.Append);
            g.RotateTransform(theta, MatrixOrder.Append);  // 乘上 旋轉矩陣
            g.TranslateTransform(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            g.DrawImage(bm, 0, 0); // 繪出圖形

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //using System.Collections;//for Hashtable

            Hashtable imageList = new Hashtable();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image1 = Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Image image2 = Image.FromFile(filename2);	//Image.FromFile出來的是Image格式

            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            Image image3 = Image.FromFile(filename3);	//Image.FromFile出來的是Image格式

            imageList.Add(imageList.Count + 1, image1);
            imageList.Add(imageList.Count + 1, image2);
            imageList.Add(imageList.Count + 1, image3);

            object obj = imageList[3];
            pictureBox1.Image = (Image)obj;
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


            //3030

            float x = 100;
            float y = 100;
            float width = 200;
            float height = 100;
            float cornerRadius = 20;
            //GraphicsPath gp = new GraphicsPath();  // GraphicsPath物件
            GraphicsPath gp = DrawRoundRect(x, y, width, height, cornerRadius);

            //g.DrawPath(Pens.Red, gp); // 繪出圖形軌跡
            g.FillPath(Brushes.Lime, gp); // 繪出圖形軌跡


            //6060

            gp = new GraphicsPath();  // GraphicsPath物件

            int x_st = 100;
            int y_st = 100;

            PointF[] pt = new PointF[]
            {
                new PointF(x_st, y_st),
                new PointF(x_st+50, y_st-50),
                new PointF(x_st+100, y_st-100),
                new PointF(x_st+150, y_st+50),
                new PointF(x_st+200, y_st-50),
            };

            gp.AddCurve(pt, 0.6f); // 加入曲線

            /*
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);
            */
            //gp.CloseFigure(); //  封閉目前的圖形
            g.DrawPath(Pens.Black, gp); // 繪出圖形軌跡
            g.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件

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

        private void button13_Click(object sender, EventArgs e)
        {

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
