using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

/*
全屏隨機位置顯示圖片
*/

namespace vcs_ShowPicture3
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files\__pic\_MU\";
        string filename = string.Empty;

        int flag_operation_mode = MODE_0;
        private const int MODE_0 = 0x00;   //全屏隨機位置顯示圖片
        private const int MODE_1 = 0x01;   //全屏單圖置中顯示圖片
        private const int MODE_2 = 0x02;   //reserved

        bool debug_mode = false;
        RichTextBox rtb = new RichTextBox();

        //Rectangle bounds = Screen.GetBounds(Screen.GetBounds(Point.Empty));
        Rectangle bounds = Screen.PrimaryScreen.Bounds;
        //Rectangle bounds = new Rectangle(0, 0, Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

        int total_picture_count = 0;
        int sel_picture = -1;
        bool random_sel_picture = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //全屏空白表單
            this.BackColor = Color.Black;
            //this.Size = new Size(800, 600);
            ControlBox = false;
            MaximizeBox = false;
            MinimizeBox = false;
            ShowIcon = false;
            ShowInTaskbar = false;
            FormBorderStyle = FormBorderStyle.None;
            StartPosition = FormStartPosition.CenterScreen;
            WindowState = FormWindowState.Maximized;
            TopMost = true;
            KeyPreview = true;

            this.KeyDown += Form1_KeyDown;

            //this.BackColor = Color.Black;   //背景為黑
            //this.BackgroundImage = GetNoCursor(); //複製目前桌面當背景

            if (debug_mode == true)
            {
                rtb.Width = 300;
                rtb.Height = 800;
                rtb.Location = new Point(0, 0);
                this.Controls.Add(rtb);

                this.Size = new Size(Screen.PrimaryScreen.Bounds.Width * 4 / 5, Screen.PrimaryScreen.Bounds.Height * 4 / 5);
                this.WindowState = FormWindowState.Normal;
            }
            else
            {
                this.WindowState = FormWindowState.Maximized;
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
            {
                timer1.Enabled = false;
                this.Close();
            }
        }

        private Bitmap GetNoCursor()    //複製目前桌面當背景
        {
            Bitmap Source = new Bitmap(bounds.Width, bounds.Height);    //根据屏幕大小创建Bitmap对象
            Graphics g = Graphics.FromImage(Source);
            g.CopyFromScreen(0, 0, 0, 0, Source.Size);  //获取没有鼠标的屏幕截图
            g.Dispose();    //释放资源
            return Source;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //固定一張圖
            //string filename = @"C:\______test_files\picture1.jpg";

            //任選一張圖
            DirectoryInfo DInfo = new DirectoryInfo(foldername);
            FileInfo[] FInfo = DInfo.GetFiles();

            total_picture_count = FInfo.Length;

            if (random_sel_picture == true)
            {
                Random rand = new Random();
                sel_picture = rand.Next(FInfo.Length);
            }
            else
            {
                sel_picture++;
                if (sel_picture >= total_picture_count)
                    sel_picture = 0;
            }

            filename = foldername + FInfo[sel_picture].Name;

            rtb.Text += "sel_picture = " + sel_picture.ToString() + "filename : " + filename + "\n";

            string ext = Path.GetExtension(filename);

            if ((ext != ".jpg") && (ext != ".bmp") && (ext != ".png"))
            {
                return;
            }

            Image image = Image.FromFile(filename);

            if (image == null)
                return;

            int W = bounds.Right;
            int H = bounds.Height;
            int w = image.Width;
            int h = image.Height;

            //rtb.Text += "a1(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

            while (W < (w * 3))
            {
                //rtb.Text += "X";
                w = w * 4 / 5;
                h = h * 4 / 5;
            }

            //rtb.Text += "a2(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

            while (H < (h * 3))
            {
                //rtb.Text += "Q";
                w = w * 4 / 5;
                h = h * 4 / 5;
            }

            rtb.Text += "b(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

            Graphics g = this.CreateGraphics();
            Random r = new Random();

            rtb.Text += "c(" + (W - w).ToString() + ", " + (H - h).ToString() + "\n";

            if (w > W)
            {
                timer1.Enabled = false;
            }

            if (h > H)
            {
                timer1.Enabled = false;
            }


            if (flag_operation_mode == MODE_0)
            {
                int x_st = r.Next(0, W - w);
                int y_st = r.Next(0, H - h);
                //Point ulCorner = new Point(x_st, y_st);
                //g.DrawImageUnscaled(image, ulCorner);

                //原圖貼上
                //    DrawImage   貼上位置x   貼上位置y   貼上大小W   貼上大小H
                g.DrawImage(image, x_st, y_st, w, h);
                rtb.Text += "c(" + x_st.ToString() + ", " + y_st.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                g.DrawRectangle(new Pen(Color.White, 10), x_st, y_st, w, h);
            }

            image.Dispose();
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            Application.Exit();
        }
    }
}

