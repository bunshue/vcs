using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for DashStyle

//在 pictureBox 上用滑鼠畫矩形
//mode 0 : pictureBox 無圖片, 空白模式
//mode 1 : pictureBox 有圖片, 圖片模式

namespace vcs_PictureCrop
{
    public partial class Form1 : Form
    {
        int flag_operation_mode = 1;    //0 : 空白模式, 1 : 圖片模式

        //string filename = @"C:\______test_files1\picture1.jpg";
        string filename = @"C:\______test_files1\__report\connection1.jpg";

        private int intStartX = 0;
        private int intStartY = 0;

        private bool flag_mouse_down = false;   //是否開始圈選
        private Point pt_st = new Point(0, 0);  //記錄鼠標按下時的坐標，用來確定繪圖起點, 鼠標第一點 
        private Point pt_sp = new Point(0, 0);  //記錄鼠標放開時的坐標，用來確定繪圖終點, 鼠標第二點 

        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        //private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形
        //private int X0, Y0, X1, Y1;

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        //private int w = 0;  //擷取圖的寬
        //private int h = 0;  //擷取圖的高

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //跟隨鼠標在 pictureBox 的圖片上畫矩形
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);

            nud_x_st.ValueChanged += new EventHandler(select_crop_area);
            nud_y_st.ValueChanged += new EventHandler(select_crop_area);
            nud_w.ValueChanged += new EventHandler(select_crop_area);
            nud_h.ValueChanged += new EventHandler(select_crop_area);

            show_item_location();

            if (flag_operation_mode == 0)
            {
                W = pictureBox1.Width;
                H = pictureBox1.Height;
            }
            else if (flag_operation_mode == 1)
            {
                bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                pictureBox1.Image = bitmap1;
                W = bitmap1.Width;
                H = bitmap1.Height;
                nud_x_st.Maximum = W;
                nud_y_st.Maximum = H;
                nud_w.Maximum = W;
                nud_h.Maximum = H;
            }
            else //test
            {
                W = pictureBox1.Width;
                H = pictureBox1.Height;
            }
        }

        private void select_crop_area(object sender, EventArgs e)
        {
            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            SelectionRectangle = MakeRectangle(x_st, y_st, x_st + w, y_st + h);

            if ((SelectionRectangle.X < 0) || (SelectionRectangle.X >= W))
                return;
            if ((SelectionRectangle.Y < 0) || (SelectionRectangle.Y >= H))
                return;
            if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                return;
            if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                return;
            if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                return;

            draw_pictureBox1();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int pbx_W = 1550;
            int pbx_H = 900;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox2.Size = new Size(300, 400);
            //pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            button0.Location = new Point(x_st + dx * 1 - 100, y_st + dy * 0);

            groupBox_selection.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 400);
            groupBox_selection.BringToFront();

            bt_open_folder.BackgroundImage = Properties.Resources.folder_open;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;


            richTextBox1.Size = new Size(300, 450);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + groupBox_selection.Height + 400);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();


            pictureBox1.Size = new Size(600, 700);
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = @"c:\______test_files1";  //預設開啟的路徑
            openFileDialog1.InitialDirectory = @"C:\______test_files1\__pic\_ntuh";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                filename = openFileDialog1.FileName;

                reset_picture();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void reset_picture()
        {
            if (flag_operation_mode == 0)
            {
                W = pictureBox1.Width;
                H = pictureBox1.Height;
            }
            else if (flag_operation_mode == 1)
            {
                bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                pictureBox1.Image = bitmap1;
                W = bitmap1.Width;
                H = bitmap1.Height;
                nud_x_st.Maximum = W;
                nud_y_st.Maximum = H;
                nud_w.Maximum = W;
                nud_h.Maximum = H;
            }
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;

            nud_x_st.ValueChanged -= new EventHandler(select_crop_area);
            nud_y_st.ValueChanged -= new EventHandler(select_crop_area);
            nud_w.ValueChanged -= new EventHandler(select_crop_area);
            nud_h.ValueChanged -= new EventHandler(select_crop_area);

            pt_st = e.Location; //起始點座標
            intStartX = e.X;
            intStartY = e.Y;

            nud_w.Value = 0;
            nud_h.Value = 0;
            nud_x_st.Value = 0;
            nud_y_st.Value = 0;

            //label2.Text = "";
            SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));

            nud_x_st.Value = e.X;
            nud_y_st.Value = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                pt_sp = e.Location; //終點座標

                SelectionRectangle = MakeRectangle(pt_st, pt_sp);

                nud_x_st.Value = SelectionRectangle.X;
                nud_y_st.Value = SelectionRectangle.Y;
                nud_w.Value = SelectionRectangle.Width;
                nud_h.Value = SelectionRectangle.Height;
                //richTextBox1.Text += "選取區域 : " + SelectionRectangle.ToString() + "\n";

                if ((SelectionRectangle.X < 0) || (SelectionRectangle.X >= W))
                    return;
                if ((SelectionRectangle.Y < 0) || (SelectionRectangle.Y >= H))
                    return;
                if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                    return;
                if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                    return;
                if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                    return;

                draw_pictureBox1();
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == false)
            {
                return;
            }

            flag_mouse_down = false;

            nud_x_st.ValueChanged += new EventHandler(select_crop_area);
            nud_y_st.ValueChanged += new EventHandler(select_crop_area);
            nud_w.ValueChanged += new EventHandler(select_crop_area);
            nud_h.ValueChanged += new EventHandler(select_crop_area);

            intStartX = 0;
            intStartY = 0;

            /*
            // Display the original image.
            //pictureBox1.Image = bitmap1;  //仍應保留選取區域

            int w = SelectionRectangle.Width;
            int h = SelectionRectangle.Height;

            if (w < 1)
                return;
            if (h < 1)
                return;

            bitmap2 = new Bitmap(w, h);  //擷取部分位圖Bitmap
            using (Graphics g2 = Graphics.FromImage(bitmap2))
            {
                Rectangle dest_rectangle = new Rectangle(0, 0, w, h);
                g2.DrawImage(bitmap1, dest_rectangle, SelectionRectangle, GraphicsUnit.Pixel);
            }

            //pictureBox2.Image = bitmap2;
            */

            pt_sp = e.Location; //終點座標

            SelectionRectangle = MakeRectangle(pt_st, pt_sp);

            if ((SelectionRectangle.X <= 0) || (SelectionRectangle.X >= W))
                return;
            if ((SelectionRectangle.Y <= 0) || (SelectionRectangle.Y >= H))
                return;
            if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                return;
            if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                return;
            if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                return;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Info
            richTextBox1.Text += "SelectionRectangle = " + SelectionRectangle.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //截圖存檔

            reset_picture();    //為消除邊框

            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            if ((x_st < 0) || (y_st < 0) || (w <= 0) || (h <= 0))
            {
                richTextBox1.Text += "選取位置錯誤\n";
                return;
            }

            SelectionRectangle = new Rectangle(x_st, y_st, w, h);
            //richTextBox1.Text += SelectionRectangle.ToString() + "\n";

            if ((SelectionRectangle.X < 0) || (SelectionRectangle.X >= W))
                return;
            if ((SelectionRectangle.Y < 0) || (SelectionRectangle.Y >= H))
                return;
            if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                return;
            if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                return;
            if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                return;


            string filename = string.Empty;
            if (rb_filetype1.Checked == true)
            {
                filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            }
            else
            {
                filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            }

            Bitmap bitmap1 = new Bitmap(pictureBox1.Image);
            Bitmap bitmap2 = bitmap1.Clone(SelectionRectangle, PixelFormat.DontCare);  //或是 PixelFormat.Format32bppArgb

            if (rb_filetype1.Checked == true)
            {
                bitmap2.Save(filename, ImageFormat.Jpeg);
            }
            else
            {
                bitmap2.Save(filename, ImageFormat.Bmp);
            }

            richTextBox1.Text += "存截圖，存檔檔名：" + filename + "\n";

            richTextBox1.Text += "將圖片資料放置到Clipboard中\n";
            Clipboard.SetImage(bitmap2);

            richTextBox1.Text += "rect = " + SelectionRectangle.ToString() + "\n";
            richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            try
            {
                if (flag_operation_mode == 0)	//空白模式
                {
                    Graphics g = this.pictureBox1.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    //g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.DrawRectangle(pen, SelectionRectangle);
                    g.Dispose();
                    //this.pictureBox_Src.Image = tmp;
                }
                else if (flag_operation_mode == 1)  //圖片模式
                {
                    Graphics g = this.pictureBox1.CreateGraphics();
                    g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
                    g.DrawRectangle(pen, SelectionRectangle);
                    g.Dispose();
                }
                else //test
                {
                    Image tmp = Image.FromFile(filename);
                    Graphics g = this.pictureBox1.CreateGraphics();
                    g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, SelectionRectangle);
                    g.Dispose();
                    this.pictureBox1.Image = tmp;
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        void draw_pictureBox1()
        {
            //richTextBox1.Text += "draw_pictureBox1()\n";
            try
            {
                if (flag_operation_mode == 0)	//空白模式
                {
                    Graphics g = this.pictureBox1.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Dash;
                    //g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.DrawRectangle(pen, SelectionRectangle);
                    //g.Dispose();

                    /* 另法
                    //獲取兩個數中的大者或小者
                    int minX = Math.Min(pt_st.X, pt_sp.X);
                    int minY = Math.Min(pt_st.Y, pt_sp.Y);
                    int maxX = Math.Max(pt_st.X, pt_sp.X);
                    int maxY = Math.Max(pt_st.Y, pt_sp.Y);

                    x_st = minX;
                    y_st = minY;
                    w = maxX - minX;
                    h = maxY - minY;

                    //畫矩形
                    g.DrawRectangle(new Pen(Color.Red), x_st, y_st, w, h);

                    //畫矩形
                    g.DrawRectangle(new Pen(Color.Lime, 5), minX, minY, maxX - minX, maxY - minY);
                    */

                    g.Dispose();
                }
                else if (flag_operation_mode == 1)  //圖片模式
                {
                    Graphics g = this.pictureBox1.CreateGraphics();
                    g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Dash;
                    //g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.DrawRectangle(pen, SelectionRectangle);
                    g.Dispose();

                    pictureBox2.Image = bitmap1.Clone(SelectionRectangle, PixelFormat.Format32bppArgb);
                    //pictureBox2.Image = bitmap1.Clone(SelectionRectangle, PixelFormat.DontCare);  //或是 PixelFormat.Format32bppArgb
                }
                else //test
                {
                    Image tmp = Image.FromFile(filename);
                    Graphics g = this.pictureBox1.CreateGraphics();
                    g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Dash;
                    //g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.DrawRectangle(pen, SelectionRectangle);
                    g.Dispose();
                    this.pictureBox1.Image = tmp;
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            string foldername = Application.StartupPath;
            //開啟檔案總管
            Process.Start(foldername);
        }

        //不同的SizeMode, 滑鼠座標對應的點會不一樣(AutoSize和Nomal一樣)
        private void ConvertCoordinates(PictureBox pbx, out int X, out int Y, int x, int y)
        {
            int W = pbx.ClientSize.Width;
            int H = pbx.ClientSize.Height;
            int w = pbx.Image.Width;
            int h = pbx.Image.Height;

            X = x;
            Y = y;
            switch (pbx.SizeMode)
            {
                case PictureBoxSizeMode.AutoSize:
                case PictureBoxSizeMode.Normal:
                    // These are okay. Leave them alone.
                    break;
                case PictureBoxSizeMode.CenterImage:
                    X = x - (W - w) / 2;
                    Y = y - (H - h) / 2;
                    break;
                case PictureBoxSizeMode.StretchImage:
                    X = (int)(w * x / (float)W);
                    Y = (int)(h * y / (float)H);
                    break;
                case PictureBoxSizeMode.Zoom:
                    float pic_aspect = W / (float)H;
                    float img_aspect = w / (float)h;
                    if (pic_aspect > img_aspect)
                    {
                        // The PictureBox is wider/shorter than the image.
                        Y = (int)(h * y / (float)H);

                        // The image fills the height of the PictureBox.
                        // Get its width.
                        float scaled_width = w * H / h;
                        float dx = (W - scaled_width) / 2;
                        X = (int)((x - dx) * h / (float)H);
                    }
                    else
                    {
                        // The PictureBox is taller/thinner than the image.
                        X = (int)(w * x / (float)W);

                        // The image fills the height of the PictureBox.
                        // Get its height.
                        float scaled_height = h * W / w;
                        float dy = (H - scaled_height) / 2;
                        Y = (int)((y - dy) * w / W);
                    }
                    break;
                default:
                    break;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //測試圖框位置與圖片位置轉換


            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            int X, Y;
            int x_st = 200;
            int y_st = 200;
            ConvertCoordinates(pictureBox1, out X, out Y, x_st, y_st);

            richTextBox1.Text += "SizeMode : " + pictureBox1.SizeMode.ToString() + "\n";
            richTextBox1.Text += "圖框位置 : (" + x_st.ToString() + ", " + y_st.ToString() + ")\n";
            richTextBox1.Text += "圖片位置 : (" + X.ToString() + ", " + Y.ToString() + ")\n";
        }
    }
}
