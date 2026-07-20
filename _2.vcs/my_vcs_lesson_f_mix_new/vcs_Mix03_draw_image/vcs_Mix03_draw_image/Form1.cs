using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat, ImageLockMode, Encoder, ImageCodecInfo, ImageAttributes, PixelFormat
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Collections;//for Hashtable
using System.Drawing.Text;  // for TextRenderingHint

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;

        //公用變數
        List<PointF> Points1 = new List<PointF>();
        List<PointF> Points2 = new List<PointF>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            /*
            //根據桌面大小調整視窗大小
            int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen為取得主顯示器，WorkingArea可取得顯示器的工作區(不包含工作列…等)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);
            */

            //6060

            Random r = new Random();
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            for (int i = 0; i < 1000; i++)
            {
                int x = r.Next(W);
                int y = r.Next(H);
                Points1.Add(new Point(x, y));
            }
            timer1.Enabled = true;
        }

        //直接寫一個OnPaint在此, 取代Form1_Paint

        private const string FONT_NAME = "Times New Roman";
        private const float FONT_SIZE = 12;
        private const FontStyle FONT_STYLE = FontStyle.Bold;
        private const string MENU_CAPTION = "Say Hi";
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);
            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                // See how big the text will be.
                SizeF text_size = e.Graphics.MeasureString(MENU_CAPTION, menu_font);
            }

            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                //e.Graphics.FillRectangle(Brushes.Pink, e.Bounds);

                // Draw the text.
                //e.Graphics.DrawString(MENU_CAPTION, menu_font, Brushes.AliceBlue, e.Bounds.X, e.Bounds.Y);
                // The mouse is not over the item.
                // Erase the background.
                //e.Graphics.FillRectangle(Brushes.LightGray, e.Bounds.X, e.Bounds.Y, e.Bounds.Width, e.Bounds.Height);

                // Draw the text.
                //e.Graphics.DrawString(MENU_CAPTION, menu_font, Brushes.Black, e.Bounds.X, e.Bounds.Y);
            }
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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

            pictureBox1.Size = new Size(690, 690);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox_star.Size = new Size(200, 200);
            pictureBox_star.Location = new Point(x_st + dx * 5 + 70 + 200, y_st + dy * 0);

            groupBox1.Location = new Point(x_st + dx * 5 + 70, y_st + dy * 0);
            richTextBox1.Size = new Size(440, 690 - 300);
            richTextBox1.Location = new Point(x_st + dx * 5 + 70, y_st + dy * 0 + 300);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 750);
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

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        //------------------------------------------------------------  # 60個

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fi in fileinfo)  // 遍歷獲取到的文件
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

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        int orientation = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            const int size = 120;
            Bitmap bitmap1 = new Bitmap(size, size);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Orient the result.
            switch (orientation)
            {
                case 0://ExifOrientations.TopLeft:
                    break;
                case 1://ExifOrientations.TopRight:
                    g.ScaleTransform(-1, 1);
                    break;
                case 2://ExifOrientations.BottomRight:
                    g.RotateTransform(180);
                    break;
                case 3://ExifOrientations.BottomLeft:
                    g.ScaleTransform(1, -1);
                    break;
                case 4://ExifOrientations.LeftTop:
                    g.RotateTransform(90);
                    g.ScaleTransform(-1, 1, MatrixOrder.Append);
                    break;
                case 5://ExifOrientations.RightTop:
                    g.RotateTransform(-90);
                    break;
                case 6://ExifOrientations.RightBottom:
                    g.RotateTransform(90);
                    g.ScaleTransform(1, -1, MatrixOrder.Append);
                    break;
                case 7://ExifOrientations.LeftBottom:
                    g.RotateTransform(90);
                    break;
            }

            orientation++;
            if (orientation > 7)
                orientation = 0;

            // Translate the result to the center of the bitmap.
            g.TranslateTransform(size / 2, size / 2, MatrixOrder.Append);

            StringFormat string_format = new StringFormat();
            string_format.LineAlignment = StringAlignment.Center;
            string_format.Alignment = StringAlignment.Center;

            Font font = new Font("Times New Roman", 40, GraphicsUnit.Point);

            g.DrawString("F", font, Brushes.Black, 0, 0, string_format);

            pictureBox1.Image = bitmap1;
        }

        //6060

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

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
            //MessageBox.Show("Width = " + this.pictureBox1.Width + "  Height = " + this.pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //繪製折線

            DrawCircle(g, 200, 200, 100);

            pictureBox1.Image = bitM;
        }

        private void DrawCircle(Graphics g, int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
                pictureBox1.Image = bitmap1;
            }

            pictureBox1.Image = bitmap1;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            /*
            string str = "天階夜色涼如水";

            Font f = new Font("標楷體", 48, GraphicsUnit.Point);  // 預設為 Point
            int W = g.MeasureString(str, f).ToSize().Width;
            int H = g.MeasureString(str, f).ToSize().Height;
            richTextBox1.Text += "GraphicsUnit : " + f.Unit.ToString() + "\n";
            richTextBox1.Text += "W = " + W.ToString() + "  H = " + H.ToString() + "\n";

            int x_st = 50;
            int y_st = 50;
            g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, W, H);

            pictureBox1.Image = bitmap1;
            */

            //6060
            /*
            string tmp_string = "春花秋月何時了";
            richTextBox1.Text += button18.Text + "\n";
            richTextBox1.Text += tmp_string + "\n";
            Graphics g2 = richTextBox1.CreateGraphics();
            Size sss = g2.MeasureString(tmp_string, richTextBox1.Font).ToSize();
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";

            Font f = new Font("Arial", 128);
            SolidBrush sb = new SolidBrush(Color.Red);
            g.DrawString("A", f, sb, new PointF(0, 0));

            //Graphics g2 = richTextBox1.CreateGraphics();
            sss = g.MeasureString("A", f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            */


            //6060

            //量測字體大小
            Font f = new Font("標楷體", 40);
            string str = "放大縮小";
            int w = g.MeasureString(str, f).ToSize().Width;
            int h = g.MeasureString(str, f).ToSize().Height;

        }


        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
            // Make the large image.
            //AddImageToImageList(imlLargeIcons, bm, reader[0].ToString(), imlLargeIcons.ImageSize.Width, imlLargeIcons.ImageSize.Height);

            // Make the small image.
            //AddImageToImageList(imlSmallIcons, bm, reader[0].ToString(), imlLargeIcons.ImageSize.Width, imlLargeIcons.ImageSize.Height);
        }

        // Scale the image to fit in the ImageList and add it.
        private void AddImageToImageList(ImageList iml, Bitmap bm, string key, float wid, float hgt)
        {
            // Make the bitmap.
            Bitmap iml_bm = new Bitmap(iml.ImageSize.Width, iml.ImageSize.Height);
            using (Graphics gr = Graphics.FromImage(iml_bm))
            {
                gr.Clear(Color.Transparent);
                gr.InterpolationMode = InterpolationMode.High;

                // See where we need to draw the image to scale it properly.
                RectangleF source_rect = new RectangleF(0, 0, bm.Width, bm.Height);
                RectangleF dest_rect = new RectangleF(0, 0, iml_bm.Width, iml_bm.Height);
                dest_rect = ScaleRect(source_rect, dest_rect);

                // Draw the image.
                gr.DrawImage(bm, dest_rect, source_rect, GraphicsUnit.Pixel);
            }

            // Add the image to the ImageList.
            iml.Images.Add(key, iml_bm);
        }

        // Scale an image without disorting it.
        // Return a centered rectangle in the destination area.
        private RectangleF ScaleRect(RectangleF source_rect, RectangleF dest_rect)
        {
            float source_aspect = source_rect.Width / source_rect.Height;
            float wid = dest_rect.Width;
            float hgt = dest_rect.Height;
            float dest_aspect = wid / hgt;

            if (source_aspect > dest_aspect)
            {
                // The source is relatively short and wide.
                // Use all of the available width.
                hgt = wid / source_aspect;
            }
            else
            {
                // The source is relatively tall and thin.
                // Use all of the available height.
                wid = hgt * source_aspect;
            }

            // Center it.
            float x = dest_rect.Left + (dest_rect.Width - wid) / 2;
            float y = dest_rect.Top + (dest_rect.Height - hgt) / 2;
            return new RectangleF(x, y, wid, hgt);
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            string png_filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\Angry-Birds07.png";

            //PNG 轉 BMP
            Image PngImg = Image.FromFile(png_filename);
            Bitmap myImage = new Bitmap(PngImg.Width, PngImg.Height, PixelFormat.Format32bppRgb);
            using (Graphics g = Graphics.FromImage(myImage))
            {
                g.InterpolationMode = InterpolationMode.HighQualityBicubic;
                g.SmoothingMode = SmoothingMode.HighQuality;
                g.CompositingQuality = CompositingQuality.HighQuality;
                g.DrawImage(PngImg, 0, 0);
            }
            PngImg.Save(@"tmp_png2bmp.bmp", ImageFormat.Bmp);
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        //可以累計點數，緩慢畫出的方法
        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int len = Points1.Count;
            Points2.Add(Points1[cnt]);
            pictureBox1.Invalidate();

            cnt++;
            if (cnt >= len)
            {
                timer1.Enabled = false;
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (Points2.Count > 1)
            {
                e.Graphics.DrawLines(Pens.Red, Points2.ToArray());
                foreach (PointF pt in Points2)
                {
                    e.Graphics.FillEllipse(Brushes.Red, pt.X - 5, pt.Y - 5, 10, 10);

                }
            }
        }

        private void nudPoints_ValueChanged(object sender, EventArgs e)
        {
            nudSkip.Maximum = (int)(((int)nudPoints.Value - 1) / 2.0);
            pictureBox_star.Refresh();
        }

        private void nudSkip_ValueChanged(object sender, EventArgs e)
        {
            pictureBox_star.Refresh();
        }

        // Draw the indicated star in the rectangle.
        private void DrawStar(Graphics gr, Pen the_pen, Brush the_brush, int num_points, int skip, RectangleF rect)
        {
            // Get the star's points.
            PointF[] star_points = MakeStarPoints(-Math.PI / 2, num_points, skip, rect);

            // Draw the star.
            gr.FillPolygon(the_brush, star_points);
            gr.DrawPolygon(the_pen, star_points);
        }

        // Generate the points for a star.
        private PointF[] MakeStarPoints(double start_theta, int num_points, int skip, RectangleF rect)
        {
            double theta, dtheta;
            PointF[] result;
            float rx = rect.Width / 2f;
            float ry = rect.Height / 2f;
            float cx = rect.X + rx;
            float cy = rect.Y + ry;

            // If this is a polygon, don't bother with concave points.
            if (skip == 1)
            {
                result = new PointF[num_points];
                theta = start_theta;
                dtheta = 2 * Math.PI / num_points;
                for (int i = 0; i < num_points; i++)
                {
                    result[i] = new PointF((float)(cx + rx * Math.Cos(theta)), (float)(cy + ry * Math.Sin(theta)));
                    theta += dtheta;
                }
                return result;
            }

            // Find the radius for the concave vertices.
            double concave_radius = CalculateConcaveRadius(num_points, skip);

            // Make the points.
            result = new PointF[2 * num_points];
            theta = start_theta;
            dtheta = Math.PI / num_points;
            for (int i = 0; i < num_points; i++)
            {
                result[2 * i] = new PointF(
                    (float)(cx + rx * Math.Cos(theta)),
                    (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
                result[2 * i + 1] = new PointF(
                    (float)(cx + rx * Math.Cos(theta) * concave_radius),
                    (float)(cy + ry * Math.Sin(theta) * concave_radius));
                theta += dtheta;
            }
            return result;
        }

        // Calculate the inner star radius.
        private double CalculateConcaveRadius(int num_points, int skip)
        {
            // For really small numbers of points.
            if (num_points < 5)
            {
                return 0.33f;
            }

            // Calculate angles to key points.
            double dtheta = 2 * Math.PI / num_points;
            double theta00 = -Math.PI / 2;
            double theta01 = theta00 + dtheta * skip;
            double theta10 = theta00 + dtheta;
            double theta11 = theta10 - dtheta * skip;

            // Find the key points.
            PointF pt00 = new PointF((float)Math.Cos(theta00), (float)Math.Sin(theta00));
            PointF pt01 = new PointF((float)Math.Cos(theta01), (float)Math.Sin(theta01));
            PointF pt10 = new PointF((float)Math.Cos(theta10), (float)Math.Sin(theta10));
            PointF pt11 = new PointF((float)Math.Cos(theta11), (float)Math.Sin(theta11));

            // See where the segments connecting the points intersect.
            bool lines_intersect, segments_intersect;
            PointF intersection, close_p1, close_p2;
            FindIntersection(pt00, pt01, pt10, pt11, out lines_intersect, out segments_intersect, out intersection, out close_p1, out close_p2);

            // Calculate the distance between the
            // point of intersection and the center.
            return Math.Sqrt(intersection.X * intersection.X + intersection.Y * intersection.Y);
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 = ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34) / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 = ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12) / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect = ((t1 >= 0) && (t1 <= 1) && (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }

        private void pictureBox_star_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the star.
            DrawStar(e.Graphics, Pens.Red, Brushes.Yellow, (int)nudPoints.Value, (int)nudSkip.Value, pictureBox_star.ClientRectangle);
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

