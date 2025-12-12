using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for BitmapData
using System.Drawing.Drawing2D; //for InterpolationMode
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessing4
{
    public partial class Form1 : Form
    {
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\naruto.jpg";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\_image_processing\isinbaeva.jpg";

        Bitmap bitmap1;

        // for cmx
        Graphics g3;
        Graphics g_cmx;

        //pictureBox3 initial location
        private const int PB3_DEFAULT_POSITION_X = 600 - 10;
        private const int PB3_DEFAULT_POSITION_Y = 700;
        int pictureBox3_position_x_old = PB3_DEFAULT_POSITION_X;
        int pictureBox3_position_y_old = PB3_DEFAULT_POSITION_Y;

        //pictureBox4 initial location
        private const int PB4_DEFAULT_POSITION_X = 600 - 10;
        private const int PB4_DEFAULT_POSITION_Y = 700;
        int pictureBox4_position_x_old = PB4_DEFAULT_POSITION_X;
        int pictureBox4_position_y_old = PB4_DEFAULT_POSITION_Y;

        //pictureBox3
        Button btn1 = new Button();
        Button btn2 = new Button();
        Button btn3 = new Button();
        Button btn_return = new Button();
        HScrollBar hsbar = new HScrollBar();

        CheckBox cb_average = new CheckBox();
        CheckBox cb_show_r = new CheckBox();
        CheckBox cb_show_g = new CheckBox();
        CheckBox cb_show_b = new CheckBox();
        CheckBox cb_show_y = new CheckBox();

        RadioButton rb_select_r = new RadioButton();
        RadioButton rb_select_g = new RadioButton();
        RadioButton rb_select_b = new RadioButton();
        RadioButton rb_select_y = new RadioButton();
        RadioButton rb_select_none = new RadioButton();

        //做 Color Matrix ST
        private const int ADDR_CMX11 = 0x5600;
        private const int ADDR_CMX12 = 0x5601;
        private const int ADDR_CMX13 = 0x5602;
        private const int ADDR_CMX14 = 0x5603;
        private const int ADDR_CMX15 = 0x5604;
        private const int ADDR_CMX16 = 0x5605;
        private const int ADDR_CMXSIGN = 0x5612;

        Label lb_main_mesg_cmx_lenc = new Label();
        TrackBar tbar0 = new TrackBar();
        TrackBar tbar1 = new TrackBar();
        TrackBar tbar2 = new TrackBar();
        TrackBar tbar3 = new TrackBar();
        TrackBar tbar4 = new TrackBar();
        TrackBar tbar5 = new TrackBar();

        TextBox tb0 = new TextBox();
        TextBox tb1 = new TextBox();
        TextBox tb2 = new TextBox();
        TextBox tb3 = new TextBox();
        TextBox tb4 = new TextBox();
        TextBox tb5 = new TextBox();
        TextBox tb6 = new TextBox();
        TextBox tb7 = new TextBox();
        TextBox tb8 = new TextBox();

        TextBox tb0h = new TextBox();
        TextBox tb1h = new TextBox();
        TextBox tb2h = new TextBox();
        TextBox tb3h = new TextBox();
        TextBox tb4h = new TextBox();
        TextBox tb5h = new TextBox();
        TextBox tb6h = new TextBox();
        TextBox tb7h = new TextBox();
        TextBox tb8h = new TextBox();

        Label lb_color_correction_matrix = new Label();
        Label lb_cmx = new Label();
        TextBox tb_color_correction_matrix00 = new TextBox();
        TextBox tb_color_correction_matrix01 = new TextBox();
        TextBox tb_color_correction_matrix02 = new TextBox();
        TextBox tb_color_correction_matrix10 = new TextBox();
        TextBox tb_color_correction_matrix11 = new TextBox();
        TextBox tb_color_correction_matrix12 = new TextBox();
        TextBox tb_color_correction_matrix20 = new TextBox();
        TextBox tb_color_correction_matrix21 = new TextBox();
        TextBox tb_color_correction_matrix22 = new TextBox();
        TextBox tb_cmx11 = new TextBox();
        TextBox tb_cmx12 = new TextBox();
        TextBox tb_cmx13 = new TextBox();
        TextBox tb_cmx14 = new TextBox();
        TextBox tb_cmx15 = new TextBox();
        TextBox tb_cmx16 = new TextBox();
        TextBox tb_cmxsign1 = new TextBox();
        TextBox tb_cmxsign2 = new TextBox();

        Button btn_cmx_calculate = new Button();
        Button btn_cmx_apply = new Button();
        Button btn_cmx_recover = new Button();
        Button btn_ok6 = new Button();
        Button btn_ok7 = new Button();
        Button btn_ok8 = new Button();
        Button btn_read_cmx = new Button();
        Button btn_reset_cmx = new Button();

        CheckBox cb5a = new CheckBox();
        CheckBox cb4a = new CheckBox();
        CheckBox cb3a = new CheckBox();
        CheckBox cb2a = new CheckBox();
        CheckBox cb1a = new CheckBox();
        CheckBox cb0a = new CheckBox();

        CheckBox cb2b = new CheckBox();
        CheckBox cb1b = new CheckBox();
        CheckBox cb0b = new CheckBox();

        CheckBox cb7c = new CheckBox();
        CheckBox cb6c = new CheckBox();
        CheckBox cb5c = new CheckBox();
        CheckBox cb4c = new CheckBox();
        CheckBox cb3c = new CheckBox();
        CheckBox cb2c = new CheckBox();
        CheckBox cb1c = new CheckBox();
        CheckBox cb0c = new CheckBox();

        PictureBox pbox_cmx = new PictureBox();
        Label lb_cmx_u_r = new Label();
        Label lb_cmx_u_g = new Label();
        Label lb_cmx_u_b = new Label();
        Label lb_cmx_v_r = new Label();
        Label lb_cmx_v_g = new Label();
        Label lb_cmx_v_b = new Label();
        TextBox tb_cmx_u_r = new TextBox();
        TextBox tb_cmx_u_g = new TextBox();
        TextBox tb_cmx_u_b = new TextBox();
        TextBox tb_cmx_v_r = new TextBox();
        TextBox tb_cmx_v_g = new TextBox();
        TextBox tb_cmx_v_b = new TextBox();
        TextBox tb_cmx_00 = new TextBox();
        TextBox tb_cmx_01 = new TextBox();
        TextBox tb_cmx_02 = new TextBox();
        TextBox tb_cmx_10 = new TextBox();
        TextBox tb_cmx_11 = new TextBox();
        TextBox tb_cmx_12 = new TextBox();
        TextBox tb_cmx_20 = new TextBox();
        TextBox tb_cmx_21 = new TextBox();
        TextBox tb_cmx_22 = new TextBox();

        Button btn_read_cmx_registers = new Button();
        Button btn_calculate_cmx_registers = new Button();
        Button btn_write_cmx_registers = new Button();

        //做 Color Matrix SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            reset_pictureBox();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(600, 600);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            pictureBox2.Size = new Size(600, 600);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 12);

            richTextBox1.Location = new Point(x_st + dx * 7 + 120, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 600);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();

            button0.Text = "";
            button1.Text = "";
            button2.Text = "";
            button3.Text = "";
            button4.Text = "";
            button5.Text = "";
            //button6.Text = "";
            button7.Text = "";
            button8.Text = "";
            button9.Text = "";
            button10.Text = "";
            button11.Text = "";
            button12.Text = "";
            button13.Text = "";
            button14.Text = "";
            button15.Text = "";
            button16.Text = "";
            button17.Text = "";
            button18.Text = "";
            button19.Text = "";
            //button20.Text = "";
            button21.Text = "";
            button22.Text = "";
            button23.Text = "";
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
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
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
                reset_pictureBox();
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
            bt_exit.Name = "bt_exit";
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

        void reset_pictureBox()
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //旋轉（90度/180度/270度, 3種）
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = RotateImage(bitmap1, 90);
            pictureBox1.Image = bitmap2;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //重設大小
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = ResizeImage(bitmap1, new Size(bitmap1.Width / 2, bitmap1.Height / 2));
            pictureBox1.Image = bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //水平Mirror
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "水平Mirror處理中~~~~~~\n";

            Bitmap bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 1;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap1.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap1.SetPixel(bitmap1.Width - xx - 1, yy, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //垂直Mirror
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "垂直Mirror處理中~~~~~~\n";

            Bitmap bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 1;
            hh = bitmap1.Height / 2;

            for (xx = 0; xx < ww; xx++)
            {
                for (yy = 0; yy < hh; yy++)
                {
                    Color pp = bitmap1.GetPixel(xx, bitmap1.Height - yy - 1);
                    bitmap1.SetPixel(xx, bitmap1.Height - yy - 1, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //找過亮
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims_image.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int xx;
            int yy;
            Color p;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    p = bitmap1.GetPixel(xx, yy);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    if (yyy.Y > 252)
                    {
                        //bitmap1.SetPixel(xx, yy, Color.FromArgb((int)yyy.Y, (int)yyy.Y, (int)yyy.Y));
                        bitmap1.SetPixel(xx, yy, Color.Red);
                    }
                    else
                    {
                    }
                }
            }
            pictureBox1.Image = bitmap1;
        }

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        /* old
        public static RGB YUVToRGB(YUV yuv)
        {
            byte r = (byte)(yuv.Y + 1.4075 * (yuv.V - 128));
            byte g = (byte)(yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128)));
            byte b = (byte)(yuv.Y + 1.7790 * (yuv.U - 128));

            return new RGB(r, g, b);
        }
        */

        public static RGB YUVToRGB(YUV yuv)
        {
            double r = yuv.Y + 1.4075 * (yuv.V - 128);
            double g = yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128));
            double b = yuv.Y + 1.7790 * (yuv.U - 128);
            if (r > 255)
                r = 255;
            if (g > 255)
                g = 255;
            if (b > 255)
                b = 255;
            if (r < 0)
                r = 0;
            if (g < 0)
                g = 0;
            if (b < 0)
                b = 0;

            return new RGB((byte)r, (byte)g, (byte)b);
        }


        private void button6_Click(object sender, EventArgs e)
        {
            //降亮度

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\ims_image.bmp";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int xx;
            int yy;
            Color p;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    p = bitmap1.GetPixel(xx, yy);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    RGB rrr = new RGB();
                    yyy = RGBToYUV(pp);

                    if (yyy.Y > 50)
                    {
                        yyy.Y -= 10;
                    }
                    else
                    {
                        yyy.Y = 50;
                    }

                    rrr = YUVToRGB(yyy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(rrr.R, rrr.G, rrr.B));
                }
            }
            pictureBox1.Image = bitmap1;
        }

        //public void bitSlicing(Bitmap Image)
        public void bitSlicing()
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            pictureBox1.Image = bitmap1;

            //Bitmap GrayImg = imop.getGrayImage8(Image);

            int width = bitmap1.Width;
            int height = bitmap1.Height;

            Bitmap level1 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level2 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level3 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level4 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level5 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level6 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level7 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level8 = new Bitmap(width, height, PixelFormat.Format24bppRgb);


            BitmapData level1Data = level1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level2Data = level2.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level3Data = level3.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level4Data = level4.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level5Data = level5.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level6Data = level6.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level7Data = level7.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level8Data = level8.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData GrayImgData = bitmap1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int size = GrayImgData.Stride * GrayImgData.Height;

            IntPtr intPtr = GrayImgData.Scan0;
            IntPtr intPtr1 = level1Data.Scan0;
            IntPtr intPtr2 = level2Data.Scan0;
            IntPtr intPtr3 = level3Data.Scan0;
            IntPtr intPtr4 = level4Data.Scan0;
            IntPtr intPtr5 = level5Data.Scan0;
            IntPtr intPtr6 = level6Data.Scan0;
            IntPtr intPtr7 = level7Data.Scan0;
            IntPtr intPtr8 = level8Data.Scan0;


            byte[] GrayImgBytes = new byte[size];
            byte[] level1Bytes = new byte[size];
            byte[] level2Bytes = new byte[size];
            byte[] level3Bytes = new byte[size];
            byte[] level4Bytes = new byte[size];
            byte[] level5Bytes = new byte[size];
            byte[] level6Bytes = new byte[size];
            byte[] level7Bytes = new byte[size];
            byte[] level8Bytes = new byte[size];

            Marshal.Copy(intPtr, GrayImgBytes, 0, size);
            Marshal.Copy(intPtr1, level1Bytes, 0, size);
            Marshal.Copy(intPtr2, level2Bytes, 0, size);
            Marshal.Copy(intPtr3, level3Bytes, 0, size);
            Marshal.Copy(intPtr4, level4Bytes, 0, size);
            Marshal.Copy(intPtr5, level5Bytes, 0, size);
            Marshal.Copy(intPtr6, level6Bytes, 0, size);
            Marshal.Copy(intPtr7, level7Bytes, 0, size);
            Marshal.Copy(intPtr8, level8Bytes, 0, size);

            int k = 3;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    byte R = GrayImgBytes[i * GrayImgData.Stride + j * k];
                    int L1 = R & 1;
                    if (L1 != 0) { L1 = 255; }
                    int L2 = R & 2;
                    if (L2 != 0) { L2 = 255; }
                    int L3 = R & 4;
                    if (L3 != 0) { L3 = 255; }
                    int L4 = R & 8;
                    if (L4 != 0) { L4 = 255; }
                    int L5 = R & 16;
                    if (L5 != 0) { L5 = 255; }
                    int L6 = R & 32;
                    if (L6 != 0) { L6 = 255; }
                    int L7 = R & 64;
                    if (L7 != 0) { L7 = 255; }
                    int L8 = R & 128;
                    if (L8 != 0) { L8 = 255; }
                    level1Bytes[i * GrayImgData.Stride + j * k] = (byte)L1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L1;
                    level2Bytes[i * GrayImgData.Stride + j * k] = (byte)L2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L2;
                    level3Bytes[i * GrayImgData.Stride + j * k] = (byte)L3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L3;
                    level4Bytes[i * GrayImgData.Stride + j * k] = (byte)L4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L4;
                    level5Bytes[i * GrayImgData.Stride + j * k] = (byte)L5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L5;
                    level6Bytes[i * GrayImgData.Stride + j * k] = (byte)L6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L6;
                    level7Bytes[i * GrayImgData.Stride + j * k] = (byte)L7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L7;
                    level8Bytes[i * GrayImgData.Stride + j * k] = (byte)L8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L8;
                }
            }
            Marshal.Copy(level1Bytes, 0, intPtr1, level1Bytes.Length);
            Marshal.Copy(level2Bytes, 0, intPtr2, level2Bytes.Length);
            Marshal.Copy(level3Bytes, 0, intPtr3, level3Bytes.Length);
            Marshal.Copy(level4Bytes, 0, intPtr4, level4Bytes.Length);
            Marshal.Copy(level5Bytes, 0, intPtr5, level5Bytes.Length);
            Marshal.Copy(level6Bytes, 0, intPtr6, level6Bytes.Length);
            Marshal.Copy(level7Bytes, 0, intPtr7, level7Bytes.Length);
            Marshal.Copy(level8Bytes, 0, intPtr8, level8Bytes.Length);

            level1.UnlockBits(level1Data);
            level2.UnlockBits(level2Data);
            level3.UnlockBits(level3Data);
            level4.UnlockBits(level4Data);
            level5.UnlockBits(level5Data);
            level6.UnlockBits(level6Data);
            level7.UnlockBits(level7Data);
            level8.UnlockBits(level8Data);
            bitmap1.UnlockBits(GrayImgData);

            int W = pictureBox1.Size.Width;
            int H = pictureBox1.Size.Height;
            Bitmap bmp = new Bitmap(W - 50, H - 50);

            Graphics g = Graphics.FromImage(bmp);
            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            int w = 640 * 3 / 8;
            int h = 480 * 3 / 9;
            int x_st = 20;
            int y_st = 20;
            int dx = w + 20;
            int dy = h + 20;

            g.DrawImage(level1, x_st + dx * 0, y_st + dy * 0, w, h);
            g.DrawImage(level2, x_st + dx * 0, y_st + dy * 1, w, h);
            g.DrawImage(level3, x_st + dx * 0, y_st + dy * 2, w, h);
            g.DrawImage(level4, x_st + dx * 0, y_st + dy * 3, w, h);
            g.DrawImage(level5, x_st + dx * 1, y_st + dy * 0, w, h);
            g.DrawImage(level6, x_st + dx * 1, y_st + dy * 1, w, h);
            g.DrawImage(level7, x_st + dx * 1, y_st + dy * 2, w, h);
            g.DrawImage(level8, x_st + dx * 1, y_st + dy * 3, w, h);

            pictureBox1.Image = bmp;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //灰階位圖分割 (bit-plane slicing)
            //自然二進位分割

            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Size = new Size(512 * 2 - 250, 800);

            bitSlicing();
        }

        //public void grayCodeSlicing(Bitmap Image)
        public void grayCodeSlicing()
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            pictureBox1.Image = bitmap1;

            //Bitmap GrayImg = imop.getGrayImage8(Image);

            int width = bitmap1.Width;
            int height = bitmap1.Height;

            Bitmap level1 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level2 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level3 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level4 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level5 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level6 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level7 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level8 = new Bitmap(width, height, PixelFormat.Format24bppRgb);


            BitmapData level1Data = level1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level2Data = level2.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level3Data = level3.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level4Data = level4.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level5Data = level5.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level6Data = level6.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level7Data = level7.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level8Data = level8.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData GrayImgData = bitmap1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int size = GrayImgData.Stride * GrayImgData.Height;

            IntPtr intPtr = GrayImgData.Scan0;
            IntPtr intPtr1 = level1Data.Scan0;
            IntPtr intPtr2 = level2Data.Scan0;
            IntPtr intPtr3 = level3Data.Scan0;
            IntPtr intPtr4 = level4Data.Scan0;
            IntPtr intPtr5 = level5Data.Scan0;
            IntPtr intPtr6 = level6Data.Scan0;
            IntPtr intPtr7 = level7Data.Scan0;
            IntPtr intPtr8 = level8Data.Scan0;


            byte[] GrayImgBytes = new byte[size];
            byte[] level1Bytes = new byte[size];
            byte[] level2Bytes = new byte[size];
            byte[] level3Bytes = new byte[size];
            byte[] level4Bytes = new byte[size];
            byte[] level5Bytes = new byte[size];
            byte[] level6Bytes = new byte[size];
            byte[] level7Bytes = new byte[size];
            byte[] level8Bytes = new byte[size];

            Marshal.Copy(intPtr, GrayImgBytes, 0, size);
            Marshal.Copy(intPtr1, level1Bytes, 0, size);
            Marshal.Copy(intPtr2, level2Bytes, 0, size);
            Marshal.Copy(intPtr3, level3Bytes, 0, size);
            Marshal.Copy(intPtr4, level4Bytes, 0, size);
            Marshal.Copy(intPtr5, level5Bytes, 0, size);
            Marshal.Copy(intPtr6, level6Bytes, 0, size);
            Marshal.Copy(intPtr7, level7Bytes, 0, size);
            Marshal.Copy(intPtr8, level8Bytes, 0, size);

            int k = 3;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    byte R = GrayImgBytes[i * GrayImgData.Stride + j * k];
                    int L1 = R & 1;
                    if (L1 != 0) { L1 = 1; }
                    int L2 = R & 2;
                    if (L2 != 0) { L2 = 1; }
                    int L3 = R & 4;
                    if (L3 != 0) { L3 = 1; }
                    int L4 = R & 8;
                    if (L4 != 0) { L4 = 1; }
                    int L5 = R & 16;
                    if (L5 != 0) { L5 = 1; }
                    int L6 = R & 32;
                    if (L6 != 0) { L6 = 1; }
                    int L7 = R & 64;
                    if (L7 != 0) { L7 = 1; }
                    int L8 = R & 128;
                    if (L8 != 0) { L8 = 1; }

                    int G8 = L8;
                    if (G8 != 0) { G8 = 255; }
                    int G7 = L8 ^ L7;
                    if (G7 != 0) { G7 = 255; }
                    int G6 = L7 ^ L6;
                    if (G6 != 0) { G6 = 255; }
                    int G5 = L6 ^ L5;
                    if (G5 != 0) { G5 = 255; }
                    int G4 = L5 ^ L4;
                    if (G4 != 0) { G4 = 255; }
                    int G3 = L4 ^ L3;
                    if (G3 != 0) { G3 = 255; }
                    int G2 = L3 ^ L2;
                    if (G2 != 0) { G2 = 255; }
                    int G1 = L2 ^ L1;
                    if (G1 != 0) { G1 = 255; }

                    level1Bytes[i * GrayImgData.Stride + j * k] = (byte)G1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G1;
                    level2Bytes[i * GrayImgData.Stride + j * k] = (byte)G2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G2;
                    level3Bytes[i * GrayImgData.Stride + j * k] = (byte)G3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G3;
                    level4Bytes[i * GrayImgData.Stride + j * k] = (byte)G4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G4;
                    level5Bytes[i * GrayImgData.Stride + j * k] = (byte)G5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G5;
                    level6Bytes[i * GrayImgData.Stride + j * k] = (byte)G6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G6;
                    level7Bytes[i * GrayImgData.Stride + j * k] = (byte)G7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G7;
                    level8Bytes[i * GrayImgData.Stride + j * k] = (byte)G8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G8;
                }
            }
            Marshal.Copy(level1Bytes, 0, intPtr1, level1Bytes.Length);
            Marshal.Copy(level2Bytes, 0, intPtr2, level2Bytes.Length);
            Marshal.Copy(level3Bytes, 0, intPtr3, level3Bytes.Length);
            Marshal.Copy(level4Bytes, 0, intPtr4, level4Bytes.Length);
            Marshal.Copy(level5Bytes, 0, intPtr5, level5Bytes.Length);
            Marshal.Copy(level6Bytes, 0, intPtr6, level6Bytes.Length);
            Marshal.Copy(level7Bytes, 0, intPtr7, level7Bytes.Length);
            Marshal.Copy(level8Bytes, 0, intPtr8, level8Bytes.Length);

            level1.UnlockBits(level1Data);
            level2.UnlockBits(level2Data);
            level3.UnlockBits(level3Data);
            level4.UnlockBits(level4Data);
            level5.UnlockBits(level5Data);
            level6.UnlockBits(level6Data);
            level7.UnlockBits(level7Data);
            level8.UnlockBits(level8Data);
            bitmap1.UnlockBits(GrayImgData);


            int W = pictureBox1.Size.Width;
            int H = pictureBox1.Size.Height;
            Bitmap bmp = new Bitmap(W - 50, H - 50);

            Graphics g = Graphics.FromImage(bmp);
            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            int w = 640 * 3 / 8;
            int h = 480 * 3 / 9;
            int x_st = 20;
            int y_st = 20;
            int dx = w + 20;
            int dy = h + 20;

            g.DrawImage(level1, x_st + dx * 0, y_st + dy * 0, w, h);
            g.DrawImage(level2, x_st + dx * 0, y_st + dy * 1, w, h);
            g.DrawImage(level3, x_st + dx * 0, y_st + dy * 2, w, h);
            g.DrawImage(level4, x_st + dx * 0, y_st + dy * 3, w, h);
            g.DrawImage(level5, x_st + dx * 1, y_st + dy * 0, w, h);
            g.DrawImage(level6, x_st + dx * 1, y_st + dy * 1, w, h);
            g.DrawImage(level7, x_st + dx * 1, y_st + dy * 2, w, h);
            g.DrawImage(level8, x_st + dx * 1, y_st + dy * 3, w, h);

            pictureBox1.Image = bmp;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //格雷碼風格

            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Size = new Size(512 * 2 - 250, 800);

            grayCodeSlicing();
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //旋轉 90, 180, 270 度
        public Bitmap RotateImage(Bitmap bmp, int angle)
        {
            if (angle != 90 && angle != 180 && angle != 270)
            {
                return null;
            }
            int W = bmp.Width;
            int H = bmp.Height;

            if (angle == 90)
            {
                Bitmap newbmp = new Bitmap(H, W);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints =
                    {
                        new Point(H, 0), // destination for upper-left point of original
                        new Point(H, W),// destination for upper-right point of original
                        new Point(0, 0)     // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }

            if (angle == 180)
            {
                Bitmap newbmp = new Bitmap(W, H);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints =
                    {
                        new Point(W, H), // destination for upper-left point of original
                        new Point(0, H),// destination for upper-right point of original
                        new Point(W, 0)     // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }

            if (angle == 270)
            {
                Bitmap newbmp = new Bitmap(H, W);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints = 
                    {
                        new Point(0, W), // destination for upper-left point of original
                        new Point(0, 0),// destination for upper-right point of original
                        new Point(H, W)    // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }
            return null;
        }

        //重設大小
        public Bitmap ResizeImage(Bitmap bmp, Size size)
        {
            Bitmap newbmp = new Bitmap(size.Width, size.Height);
            using (Graphics g = Graphics.FromImage(newbmp))
            {
                g.DrawImage(bmp, new Rectangle(Point.Empty, size));
            }
            return newbmp;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //向右旋轉圖像90°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(400, 0), // destination for upper-left point of original
new Point(400, 305),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //旋轉圖像180°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 400), // destination for upper-left point of original
new Point(305, 400),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //圖像切變
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 0), // destination for upper-left point of original
new Point(305, 0), // destination for upper-right point of original
new Point(100, 400)};// destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //圖像截取

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle sr = new Rectangle(80, 60, 400, 400);//要截取的矩形區域
            Rectangle dr = new Rectangle(0, 0, 200, 200);//要顯示到Form的矩形區域
            g.DrawImage(bitmap1, dr, sr, GraphicsUnit.Pixel);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //改變圖像大小

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;

            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle
            new Rectangle(0, 0, W, H), // destination rectangle
            GraphicsUnit.Pixel);

            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.DrawImage(bitmap1, new Rectangle(130, 10, 120, 120), new Rectangle(0, 0, W, H), GraphicsUnit.Pixel);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //轉成灰階
            pictureBox1.Image = ConvertToGrayscale(filename);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //轉成灰階
            pictureBox1.Image = ConvertToGrayscale_CM(filename);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //透明度
            pictureBox1.Image = ConvertToTransparency(filename);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //旋轉
            pictureBox1.Image = ConvertToRotate(filename);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //轉成藍色系
            // Retrieve the image.
            Bitmap image1 = new Bitmap(filename, true);

            int x, y;

            // Loop through the images pixels to reset color.
            for (x = 0; x < image1.Width; x++)
            {
                for (y = 0; y < image1.Height; y++)
                {
                    Color pixelColor = image1.GetPixel(x, y);
                    //Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    //Color newColor = Color.FromArgb(0, pixelColor.G, 0);
                    Color newColor = Color.FromArgb(0, 0, pixelColor.B);
                    image1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            pictureBox1.Image = image1;

            richTextBox1.Text += "圖片大小 " + image1.Width.ToString() + " X " + image1.Height.ToString() + "\n";

            // Display the pixel format in Label1.
            richTextBox1.Text += "Pixel format: " + image1.PixelFormat.ToString() + "\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            do_cmx();


            update_cmx_data();

            return;



            //Color Matrix測試
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\ims_image.bmp";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int xx;
            int yy;
            Color p;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    p = bitmap1.GetPixel(xx, yy);

                    //RGB 轉 YUV, 使用 Color Matrix
                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    RGB rrr = new RGB();
                    yyy = RGBToYUV(pp);





                    //YUV 轉 RGB, 固定
                    rrr = YUVToRGB(yyy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(rrr.R, rrr.G, rrr.B));
                }
            }
            pictureBox1.Image = bitmap1;
        }

        void do_cmx()
        {
            int pbx3_w = 750 + 150+150;       //最後顯示出來的圖的大小
            int pbx3_h = 500 + 300+150;
            richTextBox1.Text += "pbx3_w = " + pbx3_w.ToString() + ", pbx3_h = " + pbx3_h.ToString() + "\n";
            pictureBox3.Visible = true;
            pictureBox3.BackColor = Color.White;

            pictureBox3.Size = new Size(pbx3_w, pbx3_h);
            pictureBox3.BringToFront();
            pictureBox3.Location = new Point(10, 70);

            Bitmap bmp3 = new Bitmap(pbx3_w, pbx3_h);
            g3 = Graphics.FromImage(bmp3);
            g3.FillRectangle(new SolidBrush(Color.White), 0, 0, bmp3.Width, bmp3.Height);   //整個背景
            g3.DrawString("Color Matrix", new Font("標楷體", 26), new SolidBrush(Color.Red), new PointF(60, 10));

            pictureBox3.Image = bmp3;

            GC.Collect();       //回收資源

            delay(10);

            add_cmx_controls();
            pictureBox4.Visible = true;
            pictureBox4_position_x_old = PB4_DEFAULT_POSITION_X;
            pictureBox4_position_y_old = PB4_DEFAULT_POSITION_Y;
            pictureBox4.Location = new Point(pictureBox4_position_x_old, pictureBox4_position_y_old);
            return;
        }

        void add_cmx_controls()
        {
            btn1.Visible = false;
            btn2.Visible = false;
            hsbar.Visible = false;
            richTextBox1.Visible = false;

            int x_st = 30;
            int y_st = 60;
            int dx = 250;
            int dy = 50;
            int offset = 0;
            int w = 0;  //控件寬度
            int h = 0;  //控件高度

            // 實例化控件

            lb_main_mesg_cmx_lenc.Text = "";
            lb_main_mesg_cmx_lenc.Font = new Font("標楷體", 22);
            lb_main_mesg_cmx_lenc.ForeColor = Color.Red;
            lb_main_mesg_cmx_lenc.Location = new Point(x_st + dx * 2 + 100, y_st + dy * (-1));
            lb_main_mesg_cmx_lenc.AutoSize = true;
            this.pictureBox3.Controls.Add(lb_main_mesg_cmx_lenc);     // 將控件加入表單

            Label lb0 = new Label();
            lb0.Text = "0x5600    CMX11    0x";
            lb0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb0.AutoSize = true;
            this.pictureBox3.Controls.Add(lb0);     // 將控件加入表單

            Label lb1 = new Label();
            lb1.Text = "0x5601    CMX12    0x";
            lb1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb1.AutoSize = true;
            this.pictureBox3.Controls.Add(lb1);     // 將控件加入表單

            Label lb2 = new Label();
            lb2.Text = "0x5602    CMX13    0x";
            lb2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb2.AutoSize = true;
            this.pictureBox3.Controls.Add(lb2);     // 將控件加入表單

            Label lb3 = new Label();
            lb3.Text = "0x5603    CMX14    0x";
            lb3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb3.AutoSize = true;
            this.pictureBox3.Controls.Add(lb3);     // 將控件加入表單

            Label lb4 = new Label();
            lb4.Text = "0x5604    CMX15    0x";
            lb4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb4.AutoSize = true;
            this.pictureBox3.Controls.Add(lb4);     // 將控件加入表單

            Label lb5 = new Label();
            lb5.Text = "0x5605    CMX16    0x";
            lb5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb5.AutoSize = true;
            this.pictureBox3.Controls.Add(lb5);     // 將控件加入表單

            Label lb6 = new Label();
            lb6.Text = "0x5612    CMXSIGN    0x";
            lb6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            lb6.AutoSize = true;
            this.pictureBox3.Controls.Add(lb6);     // 將控件加入表單

            Label lb7 = new Label();
            lb7.Text = "0x5615    CMXCTRL    0x";
            lb7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            lb7.AutoSize = true;
            this.pictureBox3.Controls.Add(lb7);     // 將控件加入表單

            Label lb8 = new Label();
            lb8.Text = "0x5001    ISP CTRL01    0x";
            lb8.Location = new Point(x_st + dx * 0 - 20, y_st + dy * 8);
            lb8.AutoSize = true;
            this.pictureBox3.Controls.Add(lb8);     // 將控件加入表單

            w = 50;
            h = 50;
            offset = -70;
            tb0.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 0);
            tb0.Width = w;
            tb0.Height = h;
            this.pictureBox3.Controls.Add(tb0);     // 將控件加入表單
            tb0h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 0);
            tb0h.Width = w;
            tb0h.Height = h;
            this.pictureBox3.Controls.Add(tb0h);     // 將控件加入表單

            tb1.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 1);
            tb1.Width = w;
            tb1.Height = h;
            this.pictureBox3.Controls.Add(tb1);     // 將控件加入表單
            tb1h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 1);
            tb1h.Width = w;
            tb1h.Height = h;
            this.pictureBox3.Controls.Add(tb1h);     // 將控件加入表單

            tb2.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 2);
            tb2.Width = w;
            tb2.Height = h;
            this.pictureBox3.Controls.Add(tb2);     // 將控件加入表單
            tb2h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 2);
            tb2h.Width = w;
            tb2h.Height = h;
            this.pictureBox3.Controls.Add(tb2h);     // 將控件加入表單

            tb3.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 3);
            tb3.Width = w;
            tb3.Height = h;
            this.pictureBox3.Controls.Add(tb3);     // 將控件加入表單
            tb3h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 3);
            tb3h.Width = w;
            tb3h.Height = h;
            this.pictureBox3.Controls.Add(tb3h);     // 將控件加入表單

            tb4.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 4);
            tb4.Width = w;
            tb4.Height = h;
            this.pictureBox3.Controls.Add(tb4);     // 將控件加入表單
            tb4h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 4);
            tb4h.Width = w;
            tb4h.Height = h;
            this.pictureBox3.Controls.Add(tb4h);     // 將控件加入表單

            tb5.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 5);
            tb5.Width = w;
            tb5.Height = h;
            this.pictureBox3.Controls.Add(tb5);     // 將控件加入表單
            tb5h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 5);
            tb5h.Width = w;
            tb5h.Height = h;
            this.pictureBox3.Controls.Add(tb5h);     // 將控件加入表單

            tb6.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 6);
            tb6.Width = w;
            tb6.Height = h;
            this.pictureBox3.Controls.Add(tb6);     // 將控件加入表單
            tb6h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 6);
            tb6h.Width = w;
            tb6h.Height = h;
            this.pictureBox3.Controls.Add(tb6h);     // 將控件加入表單

            tb7.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 7);
            tb7.Width = w;
            tb7.Height = h;
            this.pictureBox3.Controls.Add(tb7);     // 將控件加入表單
            tb7h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 7);
            tb7h.Width = w;
            tb7h.Height = h;
            this.pictureBox3.Controls.Add(tb7h);     // 將控件加入表單

            tb8.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 8);
            tb8.Width = w;
            tb8.Height = h;
            this.pictureBox3.Controls.Add(tb8);     // 將控件加入表單
            tb8h.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 8);
            tb8h.Width = w;
            tb8h.Height = h;
            this.pictureBox3.Controls.Add(tb8h);     // 將控件加入表單

            w = 250;
            h = 30;
            offset = -170;
            tbar0.Width = w;
            tbar0.Height = h;
            tbar0.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 0);
            tbar0.Minimum = 0;
            tbar0.Maximum = 255;
            tbar0.Value = 0x41;
            tbar0.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar0.MouseDown += tbar_mouse_down_cmx;
            tbar0.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar0);	// 將控件加入表單

            tbar1.Width = w;
            tbar1.Height = h;
            tbar1.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 1);
            tbar1.Minimum = 0;
            tbar1.Maximum = 255;
            tbar1.Value = 0x3C;
            tbar1.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar1.MouseDown += tbar_mouse_down_cmx;
            tbar1.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar1);	// 將控件加入表單

            tbar2.Width = w;
            tbar2.Height = h;
            tbar2.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 2);
            tbar2.Minimum = 0;
            tbar2.Maximum = 255;
            tbar2.Value = 0x06;
            tbar2.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar2.MouseDown += tbar_mouse_down_cmx;
            tbar2.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar2);	// 將控件加入表單

            tbar3.Width = w;
            tbar3.Height = h;
            tbar3.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 3);
            tbar3.Minimum = 0;
            tbar3.Maximum = 255;
            tbar3.Value = 0x17;
            tbar3.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar3.MouseDown += tbar_mouse_down_cmx;
            tbar3.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar3);	// 將控件加入表單

            tbar4.Width = w;
            tbar4.Height = h;
            tbar4.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 4);
            tbar4.Minimum = 0;
            tbar4.Maximum = 255;
            tbar4.Value = 0x3A;
            tbar4.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar4.MouseDown += tbar_mouse_down_cmx;
            tbar4.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar4);	// 將控件加入表單

            tbar5.Width = w;
            tbar5.Height = h;
            tbar5.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 5);
            tbar5.Minimum = 0;
            tbar5.Maximum = 255;
            tbar5.Value = 0x52;
            tbar5.Scroll += tbar_scroll_cmx;	// 加入事件
            tbar5.MouseDown += tbar_mouse_down_cmx;
            tbar5.MouseUp += tbar_mouse_up_cmx;
            this.pictureBox3.Controls.Add(tbar5);	// 將控件加入表單

            w = 50;
            h = 50;
            offset = -120;

            int offset_y = -50 + 10;

            lb_color_correction_matrix.Text = "Color Correction Matrix";
            lb_color_correction_matrix.Font = new Font("標楷體", 12);
            lb_color_correction_matrix.ForeColor = Color.Red;
            lb_color_correction_matrix.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            lb_color_correction_matrix.AutoSize = true;
            this.pictureBox3.Controls.Add(lb_color_correction_matrix);     // 將控件加入表單

            offset_y = -20;
            tb_color_correction_matrix00.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_color_correction_matrix00.Width = w;
            tb_color_correction_matrix00.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix00);     // 將控件加入表單
            tb_color_correction_matrix01.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_color_correction_matrix01.Width = w;
            tb_color_correction_matrix01.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix01);     // 將控件加入表單
            tb_color_correction_matrix02.Location = new Point(x_st + dx * 3 + offset + 120, y_st + offset_y);
            tb_color_correction_matrix02.Width = w;
            tb_color_correction_matrix02.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix02);     // 將控件加入表單

            offset_y = 10;
            tb_color_correction_matrix10.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_color_correction_matrix10.Width = w;
            tb_color_correction_matrix10.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix10);     // 將控件加入表單
            tb_color_correction_matrix11.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_color_correction_matrix11.Width = w;
            tb_color_correction_matrix11.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix11);     // 將控件加入表單
            tb_color_correction_matrix12.Location = new Point(x_st + dx * 3 + offset + 120, y_st + offset_y);
            tb_color_correction_matrix12.Width = w;
            tb_color_correction_matrix12.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix12);     // 將控件加入表單

            offset_y = 40;
            tb_color_correction_matrix20.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_color_correction_matrix20.Width = w;
            tb_color_correction_matrix20.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix20);     // 將控件加入表單
            tb_color_correction_matrix21.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_color_correction_matrix21.Width = w;
            tb_color_correction_matrix21.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix21);     // 將控件加入表單
            tb_color_correction_matrix22.Location = new Point(x_st + dx * 3 + offset + 120, y_st + offset_y);
            tb_color_correction_matrix22.Width = w;
            tb_color_correction_matrix22.Height = h;
            this.pictureBox3.Controls.Add(tb_color_correction_matrix22);     // 將控件加入表單

            offset_y = 70 + 10;
            lb_cmx.Text = "CMX Control Registers";
            lb_cmx.Font = new Font("標楷體", 12);
            lb_cmx.ForeColor = Color.Red;
            lb_cmx.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            lb_cmx.AutoSize = true;
            this.pictureBox3.Controls.Add(lb_cmx);     // 將控件加入表單

            offset_y = 100;
            tb_cmx11.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_cmx11.Width = w;
            tb_cmx11.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx11);     // 將控件加入表單
            tb_cmx12.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_cmx12.Width = w;
            tb_cmx12.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx12);     // 將控件加入表單
            tb_cmx13.Location = new Point(x_st + dx * 3 + offset + 120, y_st + offset_y);
            tb_cmx13.Width = w;
            tb_cmx13.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx13);     // 將控件加入表單

            offset_y = 130;
            tb_cmx14.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_cmx14.Width = w;
            tb_cmx14.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx14);     // 將控件加入表單
            tb_cmx15.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_cmx15.Width = w;
            tb_cmx15.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx15);     // 將控件加入表單
            tb_cmx16.Location = new Point(x_st + dx * 3 + offset + 120, y_st + offset_y);
            tb_cmx16.Width = w;
            tb_cmx16.Height = h;
            this.pictureBox3.Controls.Add(tb_cmx16);     // 將控件加入表單

            offset_y = 160;
            tb_cmxsign1.Location = new Point(x_st + dx * 3 + offset, y_st + offset_y);
            tb_cmxsign1.Width = w;
            tb_cmxsign1.Height = h;
            this.pictureBox3.Controls.Add(tb_cmxsign1);     // 將控件加入表單

            tb_cmxsign2.Location = new Point(x_st + dx * 3 + offset + 60, y_st + offset_y);
            tb_cmxsign2.Width = w;
            tb_cmxsign2.Height = h;
            this.pictureBox3.Controls.Add(tb_cmxsign2);     // 將控件加入表單

            tb_color_correction_matrix00.Text = "0";
            tb_color_correction_matrix01.Text = "1.15";
            tb_color_correction_matrix02.Text = "-0.15";
            tb_color_correction_matrix10.Text = "0";
            tb_color_correction_matrix11.Text = "-0.16";
            tb_color_correction_matrix12.Text = "1.16";
            tb_color_correction_matrix20.Text = "0";
            tb_color_correction_matrix21.Text = "-0.16";
            tb_color_correction_matrix22.Text = "1.16";

            w = 50;
            h = 30;

            offset = -120;

            btn_cmx_calculate.Width = w;
            btn_cmx_calculate.Height = h;
            btn_cmx_calculate.Text = "計算";
            btn_cmx_calculate.Location = new Point(x_st + dx * 3 + offset, y_st + dy * 4);
            btn_cmx_calculate.Click += btn_cmx_calculate_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_cmx_calculate);	// 將控件加入表單

            btn_cmx_apply.Width = w;
            btn_cmx_apply.Height = h;
            btn_cmx_apply.Text = "套用";
            btn_cmx_apply.Location = new Point(x_st + dx * 3 + 60 + offset, y_st + dy * 4);
            btn_cmx_apply.Click += btn_cmx_apply_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_cmx_apply);	// 將控件加入表單

            btn_cmx_recover.Width = w;
            btn_cmx_recover.Height = h;
            btn_cmx_recover.Text = "恢復";
            btn_cmx_recover.Location = new Point(x_st + dx * 3 + 120 + offset, y_st + dy * 4);
            btn_cmx_recover.Click += btn_cmx_recover_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_cmx_recover);	// 將控件加入表單

            w = 80;

            btn_ok6.Width = w;
            btn_ok6.Height = h;
            btn_ok6.Text = "Write";
            btn_ok6.Location = new Point(x_st + dx * 3 + offset, y_st + dy * 6);
            btn_ok6.Click += btn_cmx_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_ok6);	// 將控件加入表單

            btn_ok7.Width = w;
            btn_ok7.Height = h;
            btn_ok7.Text = "Write";
            btn_ok7.Location = new Point(x_st + dx * 3 + offset, y_st + dy * 7);
            btn_ok7.Click += btn_cmx_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_ok7);	// 將控件加入表單

            btn_ok8.Width = w;
            btn_ok8.Height = h;
            btn_ok8.Text = "Write";
            btn_ok8.Location = new Point(x_st + dx * 3 + offset, y_st + dy * 8);
            btn_ok8.Click += btn_cmx_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_ok8);	// 將控件加入表單

            btn_read_cmx.Width = w;
            btn_read_cmx.Height = h;
            btn_read_cmx.Text = "Read";
            btn_read_cmx.Location = new Point(x_st + dx * 2 - 100, y_st + dy * (-1));
            btn_read_cmx.Click += btn_read_cmx_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_read_cmx);	// 將控件加入表單

            btn_reset_cmx.Width = w;
            btn_reset_cmx.Height = h;
            btn_reset_cmx.Text = "Reset";
            btn_reset_cmx.Location = new Point(x_st + dx * 2 - 100 + w + 5, y_st + dy * (-1));
            btn_reset_cmx.Click += btn_reset_cmx_click;	// 加入事件
            this.pictureBox3.Controls.Add(btn_reset_cmx);	// 將控件加入表單

            tb0.Text = tbar0.Value.ToString();
            tb1.Text = tbar1.Value.ToString();
            tb2.Text = tbar2.Value.ToString();
            tb3.Text = tbar3.Value.ToString();
            tb4.Text = tbar4.Value.ToString();
            tb5.Text = tbar5.Value.ToString();
            tb0h.Text = tbar0.Value.ToString("X2");
            tb1h.Text = tbar1.Value.ToString("X2");
            tb2h.Text = tbar2.Value.ToString("X2");
            tb3h.Text = tbar3.Value.ToString("X2");
            tb4h.Text = tbar4.Value.ToString("X2");
            tb5h.Text = tbar5.Value.ToString("X2");

            tb0.ForeColor = Color.Black;
            tb1.ForeColor = Color.Black;
            tb2.ForeColor = Color.Black;
            tb3.ForeColor = Color.Black;
            tb4.ForeColor = Color.Black;
            tb5.ForeColor = Color.Black;
            tb6.ForeColor = Color.Black;
            tb7.ForeColor = Color.Black;

            tb0h.ForeColor = Color.Black;
            tb1h.ForeColor = Color.Black;
            tb2h.ForeColor = Color.Black;
            tb3h.ForeColor = Color.Black;
            tb4h.ForeColor = Color.Black;
            tb5h.ForeColor = Color.Black;
            tb6h.ForeColor = Color.Black;
            tb7h.ForeColor = Color.Black;

            int dxx = 22;
            w = 20;
            h = 18;
            offset = -120;

            cb5a.Width = w;
            cb5a.Height = h;
            cb5a.Checked = false;
            cb5a.Location = new Point(x_st + dx * 2 + dxx * (8 - 5) + offset, y_st + dy * 6);
            cb5a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb5a);	// 將控件加入表單

            cb4a.Width = w;
            cb4a.Height = h;
            cb4a.Checked = false;
            cb4a.Location = new Point(x_st + dx * 2 + dxx * (8 - 4) + offset, y_st + dy * 6);
            cb4a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb4a);	// 將控件加入表單

            cb3a.Width = w;
            cb3a.Height = h;
            cb3a.Checked = false;
            cb3a.Location = new Point(x_st + dx * 2 + dxx * (8 - 3) + offset, y_st + dy * 6);
            cb3a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb3a);	// 將控件加入表單

            cb2a.Width = w;
            cb2a.Height = h;
            cb2a.Checked = false;
            cb2a.Location = new Point(x_st + dx * 2 + dxx * (8 - 2) + offset, y_st + dy * 6);
            cb2a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb2a);	// 將控件加入表單

            cb1a.Width = w;
            cb1a.Height = h;
            cb1a.Checked = false;
            cb1a.Location = new Point(x_st + dx * 2 + dxx * (8 - 1) + offset, y_st + dy * 6);
            cb1a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb1a);	// 將控件加入表單

            cb0a.Width = w;
            cb0a.Height = h;
            cb0a.Checked = false;
            cb0a.Location = new Point(x_st + dx * 2 + dxx * (8 - 0) + offset, y_st + dy * 6);
            cb0a.CheckedChanged += cmx_data_bit_change1;	// 加入事件
            this.pictureBox3.Controls.Add(cb0a);	// 將控件加入表單

            cb2b.Width = w;
            cb2b.Height = h;
            cb2b.Checked = false;
            cb2b.Location = new Point(x_st + dx * 2 + dxx * (8 - 2) + offset, y_st + dy * 7);
            cb2b.CheckedChanged += cmx_data_bit_change2;	// 加入事件
            this.pictureBox3.Controls.Add(cb2b);	// 將控件加入表單
            cb2b.Enabled = false;
            cb2b.Checked = true;

            cb1b.Width = w;
            cb1b.Height = h;
            cb1b.Checked = false;
            cb1b.Location = new Point(x_st + dx * 2 + dxx * (8 - 1) + offset, y_st + dy * 7);
            cb1b.CheckedChanged += cmx_data_bit_change2;	// 加入事件
            this.pictureBox3.Controls.Add(cb1b);	// 將控件加入表單
            cb1b.Enabled = false;
            cb1b.Checked = true;

            cb0b.Width = w;
            cb0b.Height = h;
            cb0b.Checked = false;
            cb0b.Location = new Point(x_st + dx * 2 + dxx * (8 - 0) + offset, y_st + dy * 7);
            cb0b.CheckedChanged += cmx_data_bit_change2;	// 加入事件
            this.pictureBox3.Controls.Add(cb0b);	// 將控件加入表單

            cb7c.Width = w;
            cb7c.Height = h;
            cb7c.Checked = false;
            cb7c.Location = new Point(x_st + dx * 2 + dxx * (8 - 7) + offset, y_st + dy * 8);
            cb7c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb7c);	// 將控件加入表單
            cb7c.Enabled = false;

            cb6c.Width = w;
            cb6c.Height = h;
            cb6c.Checked = false;
            cb6c.Location = new Point(x_st + dx * 2 + dxx * (8 - 6) + offset, y_st + dy * 8);
            cb6c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb6c);	// 將控件加入表單
            cb6c.Enabled = false;

            cb5c.Width = w;
            cb5c.Height = h;
            cb5c.Checked = false;
            cb5c.Location = new Point(x_st + dx * 2 + dxx * (8 - 5) + offset, y_st + dy * 8);
            cb5c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb5c);	// 將控件加入表單
            cb5c.Enabled = false;

            cb4c.Width = w;
            cb4c.Height = h;
            cb4c.Checked = false;
            cb4c.Location = new Point(x_st + dx * 2 + dxx * (8 - 4) + offset, y_st + dy * 8);
            cb4c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb4c);	// 將控件加入表單
            cb4c.Enabled = false;

            cb3c.Width = w;
            cb3c.Height = h;
            cb3c.Checked = false;
            cb3c.Location = new Point(x_st + dx * 2 + dxx * (8 - 3) + offset, y_st + dy * 8);
            cb3c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb3c);	// 將控件加入表單
            cb3c.Enabled = false;

            cb2c.Width = w;
            cb2c.Height = h;
            cb2c.Checked = false;
            cb2c.Location = new Point(x_st + dx * 2 + dxx * (8 - 2) + offset, y_st + dy * 8);
            cb2c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb2c);	// 將控件加入表單
            cb2c.Enabled = false;

            cb1c.Width = w;
            cb1c.Height = h;
            cb1c.Checked = false;
            cb1c.Location = new Point(x_st + dx * 2 + dxx * (8 - 1) + offset, y_st + dy * 8);
            cb1c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb1c);	// 將控件加入表單

            cb0c.Width = w;
            cb0c.Height = h;
            cb0c.Checked = false;
            cb0c.Location = new Point(x_st + dx * 2 + dxx * (8 - 0) + offset, y_st + dy * 8);
            cb0c.CheckedChanged += cmx_data_bit_change3;	// 加入事件
            this.pictureBox3.Controls.Add(cb0c);	// 將控件加入表單
            cb0c.Enabled = false;

            pbox_cmx.Width = 900;
            pbox_cmx.Height = 260;
            pbox_cmx.Location = new Point(x_st + dx * 0 - 20, y_st + dy * 9);
            pbox_cmx.BackColor = Color.Pink;
            pbox_cmx.SizeMode = PictureBoxSizeMode.Normal;
            this.pictureBox3.Controls.Add(pbox_cmx);	// 將控件加入表單

            w = 150;
            h = 100;
            int dd = 20;
            int ddy = 50;
            lb_cmx_u_r.Location = new Point(x_st + dx * 0 - dd, y_st + dy * 2 - ddy);
            lb_cmx_u_r.Text = "1";
            tb_cmx_u_r.Location = new Point(x_st + dx * 0, y_st + dy * 2 - ddy);
            tb_cmx_u_r.Font = new Font("標楷體", 20);
            tb_cmx_u_r.Width = w;
            tb_cmx_u_r.Height = h;
            tb_cmx_u_r.Text = "1111111";
            this.pbox_cmx.Controls.Add(tb_cmx_u_r);     // 將控件加入表單
            lb_cmx_u_g.Location = new Point(x_st + dx * 1 - 60 - dd, y_st + dy * 2 - ddy);
            lb_cmx_u_g.Text = "2";
            tb_cmx_u_g.Location = new Point(x_st + dx * 1 - 60, y_st + dy * 2 - ddy);
            tb_cmx_u_g.Font = new Font("標楷體", 20);
            tb_cmx_u_g.Width = w;
            tb_cmx_u_g.Height = h;
            tb_cmx_u_g.Text = "2222222";
            this.pbox_cmx.Controls.Add(tb_cmx_u_g);     // 將控件加入表單
            lb_cmx_u_b.Location = new Point(x_st + dx * 2 - 120 - dd, y_st + dy * 2 - ddy);
            lb_cmx_u_b.Text = "3";
            tb_cmx_u_b.Location = new Point(x_st + dx * 2 - 120, y_st + dy * 2 - ddy);
            tb_cmx_u_b.Font = new Font("標楷體", 20);
            tb_cmx_u_b.Width = w;
            tb_cmx_u_b.Height = h;
            tb_cmx_u_b.Text = "3333333";
            this.pbox_cmx.Controls.Add(tb_cmx_u_b);     // 將控件加入表單
            lb_cmx_v_r.Location = new Point(x_st + dx * 0 - dd, y_st + dy * 3 - ddy);
            lb_cmx_v_r.Text = "4";
            tb_cmx_v_r.Location = new Point(x_st + dx * 0, y_st + dy * 3 - ddy);
            tb_cmx_v_r.Font = new Font("標楷體", 20);
            tb_cmx_v_r.Width = w;
            tb_cmx_v_r.Height = h;
            tb_cmx_v_r.Text = "4444444";
            this.pbox_cmx.Controls.Add(tb_cmx_v_r);     // 將控件加入表單
            lb_cmx_v_g.Location = new Point(x_st + dx * 1 - 60 - dd, y_st + dy * 3 - ddy);
            lb_cmx_v_g.Text = "5";
            tb_cmx_v_g.Location = new Point(x_st + dx * 1 - 60, y_st + dy * 3 - ddy);
            tb_cmx_v_g.Font = new Font("標楷體", 20);
            tb_cmx_v_g.Width = w;
            tb_cmx_v_g.Height = h;
            tb_cmx_v_g.Text = "5555555";
            this.pbox_cmx.Controls.Add(tb_cmx_v_g);     // 將控件加入表單
            lb_cmx_v_b.Location = new Point(x_st + dx * 2 - 120 - dd, y_st + dy * 3 - ddy);
            lb_cmx_v_b.Text = "6";
            tb_cmx_v_b.Location = new Point(x_st + dx * 2 - 120, y_st + dy * 3 - ddy);
            tb_cmx_v_b.Font = new Font("標楷體", 20);
            tb_cmx_v_b.Width = w;
            tb_cmx_v_b.Height = h;
            tb_cmx_v_b.Text = "6666666";
            this.pbox_cmx.Controls.Add(tb_cmx_v_b);     // 將控件加入表單

            this.pbox_cmx.Controls.Add(lb_cmx_u_r);     // 將控件加入表單
            this.pbox_cmx.Controls.Add(lb_cmx_u_g);     // 將控件加入表單
            this.pbox_cmx.Controls.Add(lb_cmx_u_b);     // 將控件加入表單
            this.pbox_cmx.Controls.Add(lb_cmx_v_r);     // 將控件加入表單
            this.pbox_cmx.Controls.Add(lb_cmx_v_g);     // 將控件加入表單
            this.pbox_cmx.Controls.Add(lb_cmx_v_b);     // 將控件加入表單

            w = 80;
            h = 40;
            btn_read_cmx_registers.Width = w;
            btn_read_cmx_registers.Height = h;
            btn_read_cmx_registers.Text = "讀CMX";
            btn_read_cmx_registers.Location = new Point(x_st + dx * 0, y_st + dy * 4 - ddy - 10);
            //btn_read_cmx_registers.Click += btn_read_cmx_click;	// 加入事件
            this.pbox_cmx.Controls.Add(btn_read_cmx_registers);	// 將控件加入表單

            btn_calculate_cmx_registers.Width = w;
            btn_calculate_cmx_registers.Height = h;
            btn_calculate_cmx_registers.Text = "轉係數";
            btn_calculate_cmx_registers.Location = new Point(x_st + dx * 0 + 120 * 1, y_st + dy * 4 - ddy - 10);
            //btn_calculate_cmx_registers.Click += btn_calculate_cmx_registers_click;	// 加入事件
            this.pbox_cmx.Controls.Add(btn_calculate_cmx_registers);	// 將控件加入表單

            btn_write_cmx_registers.Width = w;
            btn_write_cmx_registers.Height = h;
            btn_write_cmx_registers.Text = "寫CMX";
            btn_write_cmx_registers.Location = new Point(x_st + dx * 0 + 120 * 2, y_st + dy * 4 - ddy - 10);
            //btn_write_cmx_registers.Click += btn_write_cmx_registers_click;	// 加入事件
            this.pbox_cmx.Controls.Add(btn_write_cmx_registers);	// 將控件加入表單


            x_st = 600;
            y_st = 130;
            w = 60;
            h = 80;
            dx = 80;
            dy = 40;
            dd = 20;
            tb_cmx_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            tb_cmx_00.Font = new Font("標楷體", 16);
            tb_cmx_00.Width = w;
            tb_cmx_00.Height = h;
            tb_cmx_00.Text = "AAAAA";
            this.pbox_cmx.Controls.Add(tb_cmx_00);     // 將控件加入表單
            tb_cmx_01.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            tb_cmx_01.Font = new Font("標楷體", 16);
            tb_cmx_01.Width = w;
            tb_cmx_01.Height = h;
            tb_cmx_01.Text = "BBBBB";
            this.pbox_cmx.Controls.Add(tb_cmx_01);     // 將控件加入表單
            tb_cmx_02.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            tb_cmx_02.Font = new Font("標楷體", 16);
            tb_cmx_02.Width = w;
            tb_cmx_02.Height = h;
            tb_cmx_02.Text = "CCCCC";
            this.pbox_cmx.Controls.Add(tb_cmx_02);     // 將控件加入表單

            tb_cmx_10.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            tb_cmx_10.Font = new Font("標楷體", 16);
            tb_cmx_10.Width = w;
            tb_cmx_10.Height = h;
            tb_cmx_10.Text = "AAAAA";
            this.pbox_cmx.Controls.Add(tb_cmx_10);     // 將控件加入表單
            tb_cmx_11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            tb_cmx_11.Font = new Font("標楷體", 16);
            tb_cmx_11.Width = w;
            tb_cmx_11.Height = h;
            tb_cmx_11.Text = "BBBBB";
            this.pbox_cmx.Controls.Add(tb_cmx_11);     // 將控件加入表單
            tb_cmx_12.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            tb_cmx_12.Font = new Font("標楷體", 16);
            tb_cmx_12.Width = w;
            tb_cmx_12.Height = h;
            tb_cmx_12.Text = "CCCCC";
            this.pbox_cmx.Controls.Add(tb_cmx_12);     // 將控件加入表單


            tb_cmx_20.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            tb_cmx_20.Font = new Font("標楷體", 16);
            tb_cmx_20.Width = w;
            tb_cmx_20.Height = h;
            tb_cmx_20.Text = "AAAAA";
            this.pbox_cmx.Controls.Add(tb_cmx_20);     // 將控件加入表單
            tb_cmx_21.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            tb_cmx_21.Font = new Font("標楷體", 16);
            tb_cmx_21.Width = w;
            tb_cmx_21.Height = h;
            tb_cmx_21.Text = "BBBBB";
            this.pbox_cmx.Controls.Add(tb_cmx_21);     // 將控件加入表單
            tb_cmx_22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            tb_cmx_22.Font = new Font("標楷體", 16);
            tb_cmx_22.Width = w;
            tb_cmx_22.Height = h;
            tb_cmx_22.Text = "CCCCC";
            this.pbox_cmx.Controls.Add(tb_cmx_22);     // 將控件加入表單


            x_st = 1195;
            y_st = 10;
            dy = 20;
            w = 95;
            h = 20;
            cb_average.Text = "20張平均";
            cb_average.ForeColor = Color.Black;
            cb_average.BackColor = Color.White;
            cb_average.Width = w;
            cb_average.Height = h;
            cb_average.Checked = true;
            cb_average.Location = new Point(x_st, y_st + dy * 0);
            this.pictureBox4.Controls.Add(cb_average);	// 將控件加入表單

            cb_show_r.Text = "R";
            cb_show_r.ForeColor = Color.Red;
            cb_show_r.BackColor = Color.White;
            cb_show_r.Width = w;
            cb_show_r.Height = h;
            cb_show_r.Checked = true;
            cb_show_r.Location = new Point(x_st, y_st + dy * 1);
            this.pictureBox4.Controls.Add(cb_show_r);	// 將控件加入表單

            cb_show_g.Text = "G";
            cb_show_g.ForeColor = Color.Green;
            cb_show_g.BackColor = Color.White;
            cb_show_g.Width = w;
            cb_show_g.Height = h;
            cb_show_g.Checked = true;
            cb_show_g.Location = new Point(x_st, y_st + dy * 2);
            this.pictureBox4.Controls.Add(cb_show_g);	// 將控件加入表單

            cb_show_b.Text = "B";
            cb_show_b.ForeColor = Color.Blue;
            cb_show_b.BackColor = Color.White;
            cb_show_b.Width = w;
            cb_show_b.Height = h;
            cb_show_b.Checked = true;
            cb_show_b.Location = new Point(x_st, y_st + dy * 3);
            this.pictureBox4.Controls.Add(cb_show_b);	// 將控件加入表單

            cb_show_y.Text = "Y";
            cb_show_y.ForeColor = Color.Orange;
            cb_show_y.BackColor = Color.White;
            cb_show_y.Width = w;
            cb_show_y.Height = h;
            cb_show_y.Checked = false;
            cb_show_y.Location = new Point(x_st, y_st + dy * 4);
            this.pictureBox4.Controls.Add(cb_show_y);	// 將控件加入表單

            // 實例化按鈕
            btn_return.Width = 35;
            btn_return.Height = 35;
            btn_return.Text = "回";
            //btn_return.BackColor = Color.Red;
            btn_return.Name = "bt_return";
            btn_return.Location = new Point(x_st + 50, y_st + dy * 1 + dy / 2);
            // 加入按鈕事件
            //btn_return.Click += new EventHandler(btn_return_pbx4_Click);   //same
            //btn_return.Click += btn_return_pbx4_Click;
            // 將按鈕加入表單
            //this.AcceptButton = btn_return;
            this.pictureBox4.Controls.Add(btn_return);
            btn_return.BringToFront();
        }

        private void btn_cmx_click(object sender, EventArgs e)
        {
            byte SendData = 0;
            /*
            if (sender.Equals(btn_ok6))
            {
                tb6.ForeColor = Color.Black;
                tb6h.ForeColor = Color.Black;
                SendData = (byte)(int.Parse(tb6.Text));
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x12;    //CMX SIGN
            }
            else if (sender.Equals(btn_ok7))
            {
                tb7.ForeColor = Color.Black;
                tb7h.ForeColor = Color.Black;
                SendData = (byte)(int.Parse(tb7.Text));
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x15;    //CMX CTRL
            }
            else if (sender.Equals(btn_ok8))
            {
                tb8.ForeColor = Color.Black;
                tb8h.ForeColor = Color.Black;
                SendData = (byte)(int.Parse(tb8.Text));
                DongleAddr_h = 0x50;
                DongleAddr_l = 0x01;    //ISP CTRL01
            }

            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);
            */
        }

        private void btn_cmx_calculate_click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Color Matrix的使用 1\n";
            //color_correction_matrix = 
            double[,] color_correction_matrix = new double[,] {
            { 1.36, -0.3, -0.06},
            { -0.20, 1.32, -0.12},
            { -0.04, -0.55, 1.59}
            };

            richTextBox1.Text += color_correction_matrix[0, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 2].ToString() + "\n";

            /*
            double ccm00 = color_correction_matrix[0, 0];
            double ccm01 = color_correction_matrix[0, 1];
            double ccm02 = color_correction_matrix[0, 2];
            double ccm10 = color_correction_matrix[1, 0];
            double ccm11 = color_correction_matrix[1, 1];
            double ccm12 = color_correction_matrix[1, 2];
            double ccm20 = color_correction_matrix[2, 0];
            double ccm21 = color_correction_matrix[2, 1];
            double ccm22 = color_correction_matrix[2, 2];
            */

            double ccm00 = double.Parse(tb_color_correction_matrix00.Text);
            double ccm01 = double.Parse(tb_color_correction_matrix01.Text);
            double ccm02 = double.Parse(tb_color_correction_matrix02.Text);
            double ccm10 = double.Parse(tb_color_correction_matrix10.Text);
            double ccm11 = double.Parse(tb_color_correction_matrix11.Text);
            double ccm12 = double.Parse(tb_color_correction_matrix12.Text);
            double ccm20 = double.Parse(tb_color_correction_matrix20.Text);
            double ccm21 = double.Parse(tb_color_correction_matrix21.Text);
            double ccm22 = double.Parse(tb_color_correction_matrix22.Text);

            richTextBox1.Text += "Color Correction Matrix 內容\n";
            richTextBox1.Text += ccm00.ToString() + "\t" + ccm01.ToString() + "\t" + ccm02.ToString() + "\n";
            richTextBox1.Text += ccm10.ToString() + "\t" + ccm11.ToString() + "\t" + ccm12.ToString() + "\n";
            richTextBox1.Text += ccm20.ToString() + "\t" + ccm21.ToString() + "\t" + ccm22.ToString() + "\n";

            //保留給 RGB to YUV Conversion Matrix
            //double[] B = new double[] { 1, 2, 3, 4, 5 };
            double E12 = -0.31;
            double F12 = -0.59;
            double G12 = 0.89;
            double E13 = 0.69;
            double F13 = -0.59;
            double G13 = -0.11;
            double E17 = E12 * 0.563;
            double F17 = F12 * 0.563;
            double G17 = G12 * 0.563;
            double E18 = E13 * 0.713;
            double F18 = F13 * 0.713;
            double G18 = G13 * 0.713;

            double E22 = E17 * ccm00 + F17 * ccm10 + G17 * ccm20;
            double F22 = E17 * ccm01 + F17 * ccm11 + G17 * ccm21;
            double G22 = E17 * ccm02 + F17 * ccm12 + G17 * ccm22;
            double E23 = E18 * ccm00 + F18 * ccm10 + G18 * ccm20;
            double F23 = E18 * ccm01 + F18 * ccm11 + G18 * ccm21;
            double G23 = E18 * ccm02 + F18 * ccm12 + G18 * ccm22;

            richTextBox1.Text += "E22 = " + E22.ToString() + "\n";
            richTextBox1.Text += "F22 = " + F22.ToString() + "\n";
            richTextBox1.Text += "G22 = " + G22.ToString() + "\n";
            richTextBox1.Text += "E23 = " + E23.ToString() + "\n";
            richTextBox1.Text += "F23 = " + F23.ToString() + "\n";
            richTextBox1.Text += "G23 = " + G23.ToString() + "\n";

            double dMTX1 = E23 * 128;
            double dMTX2 = F23 * 128;
            double dMTX3 = G23 * 128;
            double dMTX4 = E22 * 128;
            double dMTX5 = F22 * 128;
            double dMTX6 = G22 * 128;

            richTextBox1.Text += "dMTX1 = " + dMTX1.ToString() + "\n";
            richTextBox1.Text += "dMTX2 = " + dMTX2.ToString() + "\n";
            richTextBox1.Text += "dMTX3 = " + dMTX3.ToString() + "\n";
            richTextBox1.Text += "dMTX4 = " + dMTX4.ToString() + "\n";
            richTextBox1.Text += "dMTX5 = " + dMTX5.ToString() + "\n";
            richTextBox1.Text += "dMTX6 = " + dMTX6.ToString() + "\n";

            int MTX1 = (int)Math.Round(dMTX1);
            int MTX2 = (int)Math.Round(dMTX2);
            int MTX3 = (int)Math.Round(dMTX3);
            int MTX4 = (int)Math.Round(dMTX4);
            int MTX5 = (int)Math.Round(dMTX5);
            int MTX6 = (int)Math.Round(dMTX6);



            richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";

            int CMXSIGN = 0;
            int CMX16 = 0;
            int CMX15 = 0;
            int CMX14 = 0;
            int CMX13 = 0;
            int CMX12 = 0;
            int CMX11 = 0;

            if (MTX1 >= 0)
            {
                CMX11 = MTX1;
            }
            else
            {
                CMX11 = -MTX1;
                CMXSIGN += 1;
            }
            if (MTX2 >= 0)
            {
                CMX12 = MTX2;
            }
            else
            {
                CMX12 = -MTX2;
                CMXSIGN += 2;
            }
            if (MTX3 >= 0)
            {
                CMX13 = MTX3;
            }
            else
            {
                CMX13 = -MTX3;
                CMXSIGN += 4;
            }
            if (MTX4 >= 0)
            {
                CMX14 = MTX4;
            }
            else
            {
                CMX14 = -MTX4;
                CMXSIGN += 8;
            }
            if (MTX5 >= 0)
            {
                CMX15 = MTX5;
            }
            else
            {
                CMX15 = -MTX5;
                CMXSIGN += 16;
            }
            if (MTX6 >= 0)
            {
                CMX16 = MTX6;
            }
            else
            {
                CMX16 = -MTX6;
                CMXSIGN += 32;
            }

            richTextBox1.Text += "CMXSIGN = 0x" + CMXSIGN.ToString("X2") + " = " + CMXSIGN.ToString() + "\n";
            richTextBox1.Text += "CMX11 = 0x" + CMX11.ToString("X2") + " = " + CMX11.ToString() + "\n";
            richTextBox1.Text += "CMX12 = 0x" + CMX12.ToString("X2") + " = " + CMX12.ToString() + "\n";
            richTextBox1.Text += "CMX13 = 0x" + CMX13.ToString("X2") + " = " + CMX13.ToString() + "\n";
            richTextBox1.Text += "CMX14 = 0x" + CMX14.ToString("X2") + " = " + CMX14.ToString() + "\n";
            richTextBox1.Text += "CMX15 = 0x" + CMX15.ToString("X2") + " = " + CMX15.ToString() + "\n";
            richTextBox1.Text += "CMX16 = 0x" + CMX16.ToString("X2") + " = " + CMX16.ToString() + "\n";

            tb_cmx11.Text = MTX1.ToString();
            tb_cmx12.Text = MTX2.ToString();
            tb_cmx13.Text = MTX3.ToString();
            tb_cmx14.Text = MTX4.ToString();
            tb_cmx15.Text = MTX5.ToString();
            tb_cmx16.Text = MTX6.ToString();
            tb_cmxsign1.Text = "0x" + CMXSIGN.ToString("X2");
            tb_cmxsign2.Text = CMXSIGN.ToString();

            if (MTX1 >= 0)
                richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            else
                richTextBox1.Text += "MTX1 = -0x" + (-MTX1).ToString("X2") + " = " + MTX1.ToString() + "\n";
            if (MTX2 >= 0)
                richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            else
                richTextBox1.Text += "MTX2 = -0x" + (-MTX2).ToString("X2") + " = " + MTX2.ToString() + "\n";
            if (MTX3 >= 0)
                richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            else
                richTextBox1.Text += "MTX3 = -0x" + (-MTX3).ToString("X2") + " = " + MTX3.ToString() + "\n";
            if (MTX4 >= 0)
                richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            else
                richTextBox1.Text += "MTX4 = -0x" + (-MTX4).ToString("X2") + " = " + MTX4.ToString() + "\n";
            if (MTX5 >= 0)
                richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            else
                richTextBox1.Text += "MTX5 = -0x" + (-MTX5).ToString("X2") + " = " + MTX5.ToString() + "\n";
            if (MTX6 >= 0)
                richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";
            else
                richTextBox1.Text += "MTX6 = -0x" + (-MTX6).ToString("X2") + " = " + MTX6.ToString() + "\n";
        }

        private void btn_cmx_apply_click(object sender, EventArgs e)
        {
            byte SendData = 0;

            int MTX1 = 0;
            int MTX2 = 83;
            int MTX3 = -84;
            int MTX4 = 0;
            int MTX5 = -29;
            int MTX6 = 28;
            int CMXSIGN = 0x14;

            MTX1 = int.Parse(tb_cmx11.Text);
            MTX2 = int.Parse(tb_cmx12.Text);
            MTX3 = int.Parse(tb_cmx13.Text);
            MTX4 = int.Parse(tb_cmx14.Text);
            MTX5 = int.Parse(tb_cmx15.Text);
            MTX6 = int.Parse(tb_cmx16.Text);
            CMXSIGN = int.Parse(tb_cmxsign2.Text);

            int CMX11 = Math.Abs(MTX1);
            int CMX12 = Math.Abs(MTX2);
            int CMX13 = Math.Abs(MTX3);
            int CMX14 = Math.Abs(MTX4);
            int CMX15 = Math.Abs(MTX5);
            int CMX16 = Math.Abs(MTX6);

            richTextBox1.Text += "btn_cmx_apply_click\n";
            richTextBox1.Text += "MTX1 = " + MTX1.ToString() + "\n";
            richTextBox1.Text += "MTX2 = " + MTX2.ToString() + "\n";
            richTextBox1.Text += "MTX3 = " + MTX3.ToString() + "\n";
            richTextBox1.Text += "MTX4 = " + MTX4.ToString() + "\n";
            richTextBox1.Text += "MTX5 = " + MTX5.ToString() + "\n";
            richTextBox1.Text += "MTX6 = " + MTX6.ToString() + "\n";
            richTextBox1.Text += "SIGN = 0x" + CMXSIGN.ToString("X2") + "\n";
            /*
            DongleAddr_h = (byte)(ADDR_CMXSIGN / 256);
            DongleAddr_l = (byte)(ADDR_CMXSIGN % 256);
            SendData = (byte)CMXSIGN;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX11 / 256);
            DongleAddr_l = (byte)(ADDR_CMX11 % 256);
            SendData = (byte)CMX11;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX12 / 256);
            DongleAddr_l = (byte)(ADDR_CMX12 % 256);
            SendData = (byte)CMX12;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX13 / 256);
            DongleAddr_l = (byte)(ADDR_CMX13 % 256);
            SendData = (byte)CMX13;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX14 / 256);
            DongleAddr_l = (byte)(ADDR_CMX14 % 256);
            SendData = (byte)CMX14;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX15 / 256);
            DongleAddr_l = (byte)(ADDR_CMX15 % 256);
            SendData = (byte)CMX15;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX16 / 256);
            DongleAddr_l = (byte)(ADDR_CMX16 % 256);
            SendData = (byte)CMX16;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */
            /* old
            DongleAddr_h = 0x56;

            DongleAddr_l = 0x12;
            SendData = 0x14;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x00;
            SendData = 0x00;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x01;
            SendData = 0x53;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x02;
            SendData = 0x54;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x03;
            SendData = 0x00;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x04;
            SendData = 0x1D;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_l = 0x05;
            SendData = 0x1C;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */
        }

        private void btn_cmx_recover_click(object sender, EventArgs e)
        {
            byte SendData = 0;

            int CMXSIGN = 0x1E;
            int CMX11 = 0x41;
            int CMX12 = 0x3C;
            int CMX13 = 0x06;
            int CMX14 = 0x17;
            int CMX15 = 0x3A;
            int CMX16 = 0x52;

            tb_cmx11.Text = CMX11.ToString();
            tb_cmx12.Text = CMX12.ToString();
            tb_cmx13.Text = CMX13.ToString();
            tb_cmx14.Text = CMX14.ToString();
            tb_cmx15.Text = CMX15.ToString();
            tb_cmx16.Text = CMX16.ToString();

            tb_cmxsign1.Text = "0x" + CMXSIGN.ToString("X2");
            tb_cmxsign2.Text = CMXSIGN.ToString();

            /*
            DongleAddr_h = (byte)(ADDR_CMXSIGN / 256);
            DongleAddr_l = (byte)(ADDR_CMXSIGN % 256);
            SendData = (byte)CMXSIGN;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX11 / 256);
            DongleAddr_l = (byte)(ADDR_CMX11 % 256);
            SendData = (byte)CMX11;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX12 / 256);
            DongleAddr_l = (byte)(ADDR_CMX12 % 256);
            SendData = (byte)CMX12;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX13 / 256);
            DongleAddr_l = (byte)(ADDR_CMX13 % 256);
            SendData = (byte)CMX13;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX14 / 256);
            DongleAddr_l = (byte)(ADDR_CMX14 % 256);
            SendData = (byte)CMX14;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX15 / 256);
            DongleAddr_l = (byte)(ADDR_CMX15 % 256);
            SendData = (byte)CMX15;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = (byte)(ADDR_CMX16 / 256);
            DongleAddr_l = (byte)(ADDR_CMX16 % 256);
            SendData = (byte)CMX16;
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */
        }

        private void setup_cmx(object sender, EventArgs e)
        {
            byte SendData = 0;
            /*
            if (sender.Equals(tbar0))
            {
                tb0.ForeColor = Color.Black;
                tb0h.ForeColor = Color.Black;
                SendData = (byte)tbar0.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x00;    //CMX11
            }
            else if (sender.Equals(tbar1))
            {
                tb1.ForeColor = Color.Black;
                tb1h.ForeColor = Color.Black;
                SendData = (byte)tbar1.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x01;    //CMX12
            }
            else if (sender.Equals(tbar2))
            {
                tb2.ForeColor = Color.Black;
                tb2h.ForeColor = Color.Black;
                SendData = (byte)tbar2.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x02;    //CMX13
            }
            else if (sender.Equals(tbar3))
            {
                tb3.ForeColor = Color.Black;
                tb3h.ForeColor = Color.Black;
                SendData = (byte)tbar3.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x03;    //CMX14
            }
            else if (sender.Equals(tbar4))
            {
                tb4.ForeColor = Color.Black;
                tb4h.ForeColor = Color.Black;
                SendData = (byte)tbar4.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x04;    //CMX15
            }
            else if (sender.Equals(tbar5))
            {
                tb5.ForeColor = Color.Black;
                tb5h.ForeColor = Color.Black;
                SendData = (byte)tbar5.Value;
                DongleAddr_h = 0x56;
                DongleAddr_l = 0x05;    //CMX16
            }

            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);
            */
        }

        private void btn_reset_cmx_click(object sender, EventArgs e)
        {
            byte SendData = 0;
            /*
            tbar0.Value = 0x41;
            tb0.ForeColor = Color.Black;
            tb0h.ForeColor = Color.Black;
            SendData = (byte)tbar0.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x00;    //CMX11
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            tbar1.Value = 0x3C;
            tb1.ForeColor = Color.Black;
            tb1h.ForeColor = Color.Black;
            SendData = (byte)tbar1.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x01;    //CMX12
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            tbar2.Value = 0x06;
            tb2.ForeColor = Color.Black;
            tb2h.ForeColor = Color.Black;
            SendData = (byte)tbar2.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x02;    //CMX13
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            tbar3.Value = 0x17;
            tb3.ForeColor = Color.Black;
            tb3h.ForeColor = Color.Black;
            SendData = (byte)tbar3.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x03;    //CMX14
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            tbar4.Value = 0x3A;
            tb4.ForeColor = Color.Black;
            tb4h.ForeColor = Color.Black;
            SendData = (byte)tbar4.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x04;    //CMX15
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            tbar5.Value = 0x52;
            tb5.ForeColor = Color.Black;
            tb5h.ForeColor = Color.Black;
            SendData = (byte)tbar5.Value;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x05;    //CMX16
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            //tbar5.Value = 0x52;
            //tb5.ForeColor = Color.Black;
            //tb5h.ForeColor = Color.Black;
            SendData = 0x1E;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x12;    //CMX SIGN
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            //tbar5.Value = 0x52;
            //tb5.ForeColor = Color.Black;
            //tb5h.ForeColor = Color.Black;
            SendData = 0x07;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x15;    //CMX CTRL
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            //tbar5.Value = 0x52;
            //tb5.ForeColor = Color.Black;
            //tb5h.ForeColor = Color.Black;
            SendData = 0x3F;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x01;    //ISP CTRL01
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);
            */
        }

        private void btn_calculate_cmx_registers_click(object sender, EventArgs e)
        {
            update_cmx_data();
        }

        private void btn_write_cmx_registers_click(object sender, EventArgs e)
        {
            richTextBox1.Text += "UR = " + tb_cmx_u_r.Text + "\n";
            richTextBox1.Text += "UG = " + tb_cmx_u_g.Text + "\n";
            richTextBox1.Text += "UB = " + tb_cmx_u_b.Text + "\n";
            richTextBox1.Text += "VR = " + tb_cmx_v_r.Text + "\n";
            richTextBox1.Text += "VG = " + tb_cmx_v_g.Text + "\n";
            richTextBox1.Text += "VB = " + tb_cmx_v_b.Text + "\n";

            int UR = (int)Math.Round(float.Parse(tb_cmx_u_r.Text) * 128);
            int UG = (int)Math.Round(float.Parse(tb_cmx_u_g.Text) * 128);
            int UB = (int)Math.Round(float.Parse(tb_cmx_u_b.Text) * 128);
            int VR = (int)Math.Round(float.Parse(tb_cmx_v_r.Text) * 128);
            int VG = (int)Math.Round(float.Parse(tb_cmx_v_g.Text) * 128);
            int VB = (int)Math.Round(float.Parse(tb_cmx_v_b.Text) * 128);

            tb_cmx_u_r.Text = UR.ToString();
            tb_cmx_u_g.Text = UG.ToString();
            tb_cmx_u_b.Text = UB.ToString();

            tb_cmx_v_r.Text = VR.ToString();
            tb_cmx_v_g.Text = VG.ToString();
            tb_cmx_v_b.Text = VB.ToString();

            byte SendData = 0;
            /*
            SendData = (byte)VR;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x00;    //CMX11, VR
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            SendData = (byte)VG;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x01;    //CMX12, VG
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            SendData = (byte)VB;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x02;    //CMX13, VB
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            SendData = (byte)UR;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x03;    //CMX14, UR
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            SendData = (byte)UG;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x04;    //CMX15, UG
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);

            SendData = (byte)UB;
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x05;    //CMX16, UB
            richTextBox1.Text += "位址 0x" + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t數值 : 0x " + SendData.ToString("X2") + " = " + SendData.ToString() + "\n";
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            show_main_message_cmx_lenc("寫入", S_OK, 10);
            */
        }

        private void btn_read_cmx_click(object sender, EventArgs e)
        {
            /*
            if (get_comport_status() == false)
                return;

            show_main_message_cmx_lenc("讀取", S_OK, 20);
            */
            tb0.Text = "";
            tb1.Text = "";
            tb2.Text = "";
            tb3.Text = "";
            tb4.Text = "";
            tb5.Text = "";
            tb6.Text = "";
            tb7.Text = "";
            tb8.Text = "";
            tb0h.Text = "";
            tb1h.Text = "";
            tb2h.Text = "";
            tb3h.Text = "";
            tb4h.Text = "";
            tb5h.Text = "";
            tb6h.Text = "";
            tb7h.Text = "";
            tb8h.Text = "";
            tb_cmx_u_r.Text = "";
            tb_cmx_u_g.Text = "";
            tb_cmx_u_b.Text = "";
            tb_cmx_v_r.Text = "";
            tb_cmx_v_g.Text = "";
            tb_cmx_v_b.Text = "";
            /*
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x00;    //CMX11
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x01;    //CMX12
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x02;    //CMX13
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x03;    //CMX14
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x04;    //CMX15
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x05;    //CMX16
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x56;
            DongleAddr_l = 0x12;    //CMX SIGN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);
            DongleAddr_h = 0x56;
            DongleAddr_l = 0x15;    //CMX CTRL
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x50;
            DongleAddr_l = 0x01;    //ISP CTRL01
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);
            */
        }

        private void tbar_mouse_down_cmx(object sender, EventArgs e)
        {
            if (sender.Equals(tbar0))
            {
                tb0.ForeColor = Color.Red;
                tb0h.ForeColor = Color.Red;
            }
            else if (sender.Equals(tbar1))
            {
                tb1.ForeColor = Color.Red;
                tb1h.ForeColor = Color.Red;
            }
            else if (sender.Equals(tbar2))
            {
                tb2.ForeColor = Color.Red;
                tb2h.ForeColor = Color.Red;
            }
            else if (sender.Equals(tbar3))
            {
                tb3.ForeColor = Color.Red;
                tb3h.ForeColor = Color.Red;
            }
            else if (sender.Equals(tbar4))
            {
                tb4.ForeColor = Color.Red;
                tb4h.ForeColor = Color.Red;
            }
            else if (sender.Equals(tbar5))
            {
                tb5.ForeColor = Color.Red;
                tb5h.ForeColor = Color.Red;
            }
            update_cmx_data();
        }

        private void tbar_scroll_cmx(object sender, EventArgs e)
        {
            if (sender.Equals(tbar0))
            {
                tb0.Text = tbar0.Value.ToString();
                tb0h.Text = tbar0.Value.ToString("X2");
            }
            else if (sender.Equals(tbar1))
            {
                tb1.Text = tbar1.Value.ToString();
                tb1h.Text = tbar1.Value.ToString("X2");
            }
            else if (sender.Equals(tbar2))
            {
                tb2.Text = tbar2.Value.ToString();
                tb2h.Text = tbar2.Value.ToString("X2");
            }
            else if (sender.Equals(tbar3))
            {
                tb3.Text = tbar3.Value.ToString();
                tb3h.Text = tbar3.Value.ToString("X2");
            }
            else if (sender.Equals(tbar4))
            {
                tb4.Text = tbar4.Value.ToString();
                tb4h.Text = tbar4.Value.ToString("X2");
            }
            else if (sender.Equals(tbar5))
            {
                tb5.Text = tbar5.Value.ToString();
                tb5h.Text = tbar5.Value.ToString("X2");
            }
        }

        private void tbar_mouse_up_cmx(object sender, EventArgs e)
        {
            //setup_cmx(sender, e);
        }



        private void cmx_data_bit_change1(object sender, EventArgs e)
        {
            int value = 0;
            if (cb5a.Checked == true)
                value |= (1 << 5);
            if (cb4a.Checked == true)
                value |= (1 << 4);
            if (cb3a.Checked == true)
                value |= (1 << 3);
            if (cb2a.Checked == true)
                value |= (1 << 2);
            if (cb1a.Checked == true)
                value |= (1 << 1);
            if (cb0a.Checked == true)
                value |= (1 << 0);
            //richTextBox1.Text += "value = 0x " + value.ToString("X2") + " = " + value.ToString() + "\n";
            tb6h.Text = value.ToString("X2");
            tb6.Text = value.ToString();
            tb6h.ForeColor = Color.Red;
            tb6.ForeColor = Color.Red;
        }

        private void cmx_data_bit_change2(object sender, EventArgs e)
        {
            int value = 0;
            if (cb0b.Checked == true)
                value |= (1 << 0);
            //richTextBox1.Text += "value = 0x " + value.ToString("X2") + " = " + value.ToString() + "\n";

            value |= 0x06;

            tb7h.Text = value.ToString("X2");
            tb7.Text = value.ToString();
            tb7h.ForeColor = Color.Red;
            tb7.ForeColor = Color.Red;
        }

        private void cmx_data_bit_change3(object sender, EventArgs e)
        {
            int value = 0;

            if (cb7c.Checked == true)
                value |= (1 << 7);
            if (cb6c.Checked == true)
                value |= (1 << 6);
            if (cb5c.Checked == true)
                value |= (1 << 5);
            if (cb4c.Checked == true)
                value |= (1 << 4);
            if (cb3c.Checked == true)
                value |= (1 << 3);
            if (cb2c.Checked == true)
                value |= (1 << 2);
            if (cb1c.Checked == true)
                value |= (1 << 1);
            if (cb0c.Checked == true)
                value |= (1 << 0);

            //richTextBox1.Text += "value = 0x " + value.ToString("X2") + " = " + value.ToString() + "\n";
            tb8h.Text = value.ToString("X2");
            tb8.Text = value.ToString();
            tb8h.ForeColor = Color.Red;
            tb8.ForeColor = Color.Red;
        }

        void show_hex2bit1(int value)
        {
            //richTextBox1.Text += "show_hex2bit\n";
            if (((value >> 5) & 0x01) == 0x01)
                cb5a.Checked = true;
            else
                cb5a.Checked = false;
            if (((value >> 4) & 0x01) == 0x01)
                cb4a.Checked = true;
            else
                cb4a.Checked = false;
            if (((value >> 3) & 0x01) == 0x01)
                cb3a.Checked = true;
            else
                cb3a.Checked = false;
            if (((value >> 2) & 0x01) == 0x01)
                cb2a.Checked = true;
            else
                cb2a.Checked = false;
            if (((value >> 1) & 0x01) == 0x01)
                cb1a.Checked = true;
            else
                cb1a.Checked = false;
            if (((value >> 0) & 0x01) == 0x01)
                cb0a.Checked = true;
            else
                cb0a.Checked = false;
        }

        void show_hex2bit2(int value)
        {
            //richTextBox1.Text += "show_hex2bit\n";
            if (((value >> 0) & 0x01) == 0x01)
                cb0b.Checked = true;
            else
                cb0b.Checked = false;
        }

        void show_hex2bit3(int value)
        {
            //richTextBox1.Text += "show_hex2bit\n";
            if (((value >> 7) & 0x01) == 0x01)
                cb7c.Checked = true;
            else
                cb7c.Checked = false;
            if (((value >> 6) & 0x01) == 0x01)
                cb6c.Checked = true;
            else
                cb6c.Checked = false;
            if (((value >> 5) & 0x01) == 0x01)
                cb5c.Checked = true;
            else
                cb5c.Checked = false;
            if (((value >> 4) & 0x01) == 0x01)
                cb4c.Checked = true;
            else
                cb4c.Checked = false;
            if (((value >> 3) & 0x01) == 0x01)
                cb3c.Checked = true;
            else
                cb3c.Checked = false;
            if (((value >> 2) & 0x01) == 0x01)
                cb2c.Checked = true;
            else
                cb2c.Checked = false;
            if (((value >> 1) & 0x01) == 0x01)
                cb1c.Checked = true;
            else
                cb1c.Checked = false;
            if (((value >> 0) & 0x01) == 0x01)
                cb0c.Checked = true;
            else
                cb0c.Checked = false;
        }



        void update_cmx_data()
        {
            int pbox_cmx_w = pbox_cmx.Width;
            int pbox_cmx_h = pbox_cmx.Height;
            Bitmap bmp = new Bitmap(pbox_cmx_w, pbox_cmx_h);
            g_cmx = Graphics.FromImage(bmp);

            Bitmap bmp_cmx = new Bitmap("cmx.jpg");
            g_cmx.DrawImage(bmp_cmx, 550, 10, bmp_cmx.Width, bmp_cmx.Height);

            if ((tb0.Text != "") && (tb1.Text != "") && (tb2.Text != "") &&
                (tb3.Text != "") && (tb4.Text != "") && (tb5.Text != ""))
            {
                //show_main_message0("OK", S_OK, 30);

                richTextBox1.Text += "got cmx11 = " + tb0.Text + "\n";
                richTextBox1.Text += "got cmx12 = " + tb1.Text + "\n";
                richTextBox1.Text += "got cmx13 = " + tb2.Text + "\n";
                richTextBox1.Text += "got cmx14 = " + tb3.Text + "\n";
                richTextBox1.Text += "got cmx15 = " + tb4.Text + "\n";
                richTextBox1.Text += "got cmx16 = " + tb5.Text + "\n";

                //int ADDR_CMXSIGN = 0x5612;
                int CMXSIGN_Value = 0x1E;
                bool flag_sign_U_R = false;//-,bit3
                bool flag_sign_U_G = false;//-,bit4
                bool flag_sign_U_B = false;//-,bit5
                bool flag_sign_V_R = false;//-,bit0
                bool flag_sign_V_G = false;//-,bit1
                bool flag_sign_V_B = false;//-,bit2

                if (((CMXSIGN_Value >> 5) & 0x01) == 0x01)
                {
                    cb5a.Checked = true;
                    flag_sign_U_B = false;
                    lb_cmx_u_b.Text = "-";
                }
                else
                {
                    cb5a.Checked = false;
                    flag_sign_U_B = true;
                    lb_cmx_u_b.Text = "+";
                }
                if (((CMXSIGN_Value >> 4) & 0x01) == 0x01)
                {
                    cb4a.Checked = true;
                    flag_sign_U_G = false;
                    lb_cmx_u_g.Text = "-";
                }
                else
                {
                    cb4a.Checked = false;
                    flag_sign_U_G = true;
                    lb_cmx_u_g.Text = "+";
                }
                if (((CMXSIGN_Value >> 3) & 0x01) == 0x01)
                {
                    cb3a.Checked = true;
                    flag_sign_U_R = false;
                    lb_cmx_u_r.Text = "-";
                }
                else
                {
                    cb3a.Checked = false;
                    flag_sign_U_R = true;
                    lb_cmx_u_r.Text = "+";
                }
                if (((CMXSIGN_Value >> 2) & 0x01) == 0x01)
                {
                    cb2a.Checked = true;
                    flag_sign_V_B = false;
                    lb_cmx_v_b.Text = "-";
                }
                else
                {
                    cb2a.Checked = false;
                    flag_sign_V_B = true;
                    lb_cmx_v_b.Text = "+";
                }
                if (((CMXSIGN_Value >> 1) & 0x01) == 0x01)
                {
                    cb1a.Checked = true;
                    flag_sign_V_G = false;
                    lb_cmx_v_g.Text = "-";
                }
                else
                {
                    cb1a.Checked = false;
                    flag_sign_V_G = true;
                    lb_cmx_v_g.Text = "+";
                }
                if (((CMXSIGN_Value >> 0) & 0x01) == 0x01)
                {
                    cb0a.Checked = true;
                    flag_sign_V_R = false;
                    lb_cmx_v_r.Text = "-";
                }
                else
                {
                    cb0a.Checked = false;
                    flag_sign_V_R = true;
                    lb_cmx_v_r.Text = "+";
                }

                richTextBox1.Text += "UR : " + flag_sign_U_R + "\n";//-,bit3
                richTextBox1.Text += "UG : " + flag_sign_U_G + "\n";//-,bit4
                richTextBox1.Text += "UB : " + flag_sign_U_B + "\n";//-,bit5
                richTextBox1.Text += "VR : " + flag_sign_V_R + "\n";//-,bit0
                richTextBox1.Text += "VG : " + flag_sign_V_G + "\n";//-,bit1
                richTextBox1.Text += "VB : " + flag_sign_V_B + "\n";//-,bit2





                int MTX1 = int.Parse(tb0.Text);//R for V
                int MTX2 = int.Parse(tb1.Text);//G for V
                int MTX3 = int.Parse(tb2.Text);//B for V
                int MTX4 = int.Parse(tb3.Text);//R gor U
                int MTX5 = int.Parse(tb4.Text);//G gor U
                int MTX6 = int.Parse(tb5.Text);//B gor U
                int x_st = 20;
                int y_st = 20;
                int dx = 150;
                int dy = 50;

                float U_R = (float)MTX4 / 128;
                float U_G = (float)MTX5 / 128;
                float U_B = (float)MTX6 / 128;
                float V_R = (float)MTX1 / 128;
                float V_G = (float)MTX2 / 128;
                float V_B = (float)MTX3 / 128;

                tb_cmx_u_r.Text = U_R.ToString("F6");
                tb_cmx_u_g.Text = U_G.ToString("F6");
                tb_cmx_u_b.Text = U_B.ToString("F6");
                tb_cmx_v_r.Text = V_R.ToString("F6");
                tb_cmx_v_g.Text = V_G.ToString("F6");
                tb_cmx_v_b.Text = V_B.ToString("F6");

                if (flag_sign_U_R == true)
                {
                    g_cmx.DrawString("+" + U_R.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 0, y_st + dy * 0));
                }
                else
                {
                    g_cmx.DrawString("-" + U_R.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 0, y_st + dy * 0));
                }

                if (flag_sign_U_G == true)
                {
                    g_cmx.DrawString("+" + U_G.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 1, y_st + dy * 0));
                }
                else
                {
                    g_cmx.DrawString("-" + U_G.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 1, y_st + dy * 0));
                }

                if (flag_sign_U_B == true)
                {
                    g_cmx.DrawString("+" + U_B.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 2, y_st + dy * 0));
                }
                else
                {
                    g_cmx.DrawString("-" + U_B.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 2, y_st + dy * 0));
                }

                if (flag_sign_V_R == true)
                {
                    g_cmx.DrawString("+" + V_R.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 0, y_st + dy * 1));
                }
                else
                {
                    g_cmx.DrawString("-" + V_R.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 0, y_st + dy * 1));
                }

                if (flag_sign_V_G == true)
                {
                    g_cmx.DrawString("+" + V_G.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 1, y_st + dy * 1));
                }
                else
                {
                    g_cmx.DrawString("-" + V_G.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 1, y_st + dy * 1));
                }

                if (flag_sign_V_B == true)
                {
                    g_cmx.DrawString("+" + V_B.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 2, y_st + dy * 1));
                }
                else
                {
                    g_cmx.DrawString("-" + V_B.ToString("F6"), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + dx * 2, y_st + dy * 1));
                }
            }
            else
            {
                //show_main_message0("XXXXXXXXXXXXX", S_OK, 30);
                g_cmx.FillRectangle(new SolidBrush(Color.Red), 0, 0, 100, 100);
            }
            pbox_cmx.Image = bmp;
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //擷取其中一塊
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "擷取其中一塊處理中~~~~~~, 九宮格之正中央\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 3;
            hh = bitmap1.Height / 3;

            Bitmap bitmap2 = new Bitmap(ww, hh);

            int x_st = ww;
            int y_st = hh;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    bitmap2.SetPixel(xx, yy, bitmap1.GetPixel(x_st + xx, y_st + yy));
                }
            }
            pictureBox2.Image = bitmap2;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            richTextBox1.Text += "處理完成\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //縮圖成一半
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "縮圖成一半\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 2;

            Bitmap bitmap2 = new Bitmap(ww, hh);

            int x_st = 0;
            int y_st = 0;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    bitmap2.SetPixel(xx, yy, bitmap1.GetPixel(x_st + xx * 2 + 1, y_st + yy * 2 + 1));
                }
            }

            pictureBox2.Image = bitmap2;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            richTextBox1.Text += "處理完成\n";
        }

        public Bitmap ConvertToGrayscale(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    Color c = bitmap1.GetPixel(x, y); // 得到 原始像素 的 Color
                    int luma = (int)(c.R * 0.3 + c.G * 0.6 + c.B * 0.1);  // 以 3:6:1 的比例得到設定值
                    bitmap2.SetPixel(x, y, Color.FromArgb(luma, luma, luma)); // 寫入 像素値
                }
            }
            return bitmap2;
        }

        // 使用色彩矩陣來調整影像色彩
        public Bitmap ConvertToGrayscale_CM(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2); // 從點陣圖 建立 新的畫布

            // 定義含有 RGBA 空間座標的 5 x 5 矩陣
            // (R, G, B, A, 1) 乘上 此矩陣
            ColorMatrix cm = new ColorMatrix(
                   new float[][]{ new float[]{0.3f, 0.3f, 0.3f, 0, 0},
                                  new float[]{0.6f, 0.6f, 0.6f, 0, 0},
                                  new float[]{0.1f, 0.1f, 0.1f, 0, 0},
                                  new float[]{  0,    0,    0,  1, 0},
                                  new float[]{  0,    0,    0,  0, 1}});

            // ImageAttributes 類別的多個方法會使用色彩矩陣來調整影像色彩
            ImageAttributes ia = new ImageAttributes();

            // 設定預設分類的色彩調整矩陣。
            ia.SetColorMatrix(cm);
            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return bitmap2;
        }

        float alpha = 0f;
        public Bitmap ConvertToTransparency(string filename)
        {
            alpha += 0.1f;
            if (alpha >= 1)
                alpha = 0;
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            ImageAttributes ia = new ImageAttributes();

            ColorMatrix cm = new ColorMatrix();

            cm.Matrix33 = alpha; // 透明度

            ia.SetColorMatrix(cm);

            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return bitmap2;
        }

        int angle = 0;
        public Bitmap ConvertToRotate(string filename)
        {
            angle += 30;
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            Matrix mx = new Matrix();
            //mx.Rotate(30);//以左上角為圓心順時鐘旋轉角度
            mx.RotateAt(angle, new PointF(W / 2, H / 2));//以(cx,cy)為圓心順時鐘旋轉角度
            g.Transform = mx;

            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H));

            g.Dispose();

            return bitmap2;
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(double delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {

        }

        bool flag_pictureBox3_mouse_down = false;
        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox3_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox3_position_x_old = e.X;
            pictureBox3_position_y_old = e.Y;
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox3_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox3_position_x_old;
                int dy = e.Y - pictureBox3_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                pictureBox3.Location = new Point(pictureBox3.Location.X + dx, pictureBox3.Location.Y + dy);
            }
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox3_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pictureBox3_position_x_old;
            int dy = e.Y - pictureBox3_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            pictureBox3.Location = new Point(pictureBox3.Location.X + dx, pictureBox3.Location.Y + dy);
        }

        bool flag_pictureBox4_mouse_down = false;
        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox4_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox4_position_x_old = e.X;
            pictureBox4_position_y_old = e.Y;
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox4_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox4_position_x_old;
                int dy = e.Y - pictureBox4_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                pictureBox4.Location = new Point(pictureBox4.Location.X + dx, pictureBox4.Location.Y + dy);
            }
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox4_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pictureBox4_position_x_old;
            int dy = e.Y - pictureBox4_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            pictureBox4.Location = new Point(pictureBox4.Location.X + dx, pictureBox4.Location.Y + dy);
        }


    }
}
