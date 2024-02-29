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

namespace vcs_ShowPicture
{
    public partial class Form1 : Form
    {
        //string pic_foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\";
        string pic_foldername = string.Empty;

        string filename = string.Empty;

        int flag_operation_mode = MODE_0;

        private const int MODE_0 = 0x00;   //全屏隨機位置 顯示 圖片
        private const int MODE_1 = 0x01;   //全屏單圖 置中 滿屏 顯示圖片
        private const int MODE_2 = 0x02;   //全屏單圖 靠右 顯示圖片
        private const int MODE_3 = 0x03;   //reserved

        bool debug_mode = false;
        RichTextBox rtb = new RichTextBox();

        //Rectangle bounds = Screen.GetBounds(Screen.GetBounds(Point.Empty));
        Rectangle bounds = Screen.PrimaryScreen.Bounds;
        //Rectangle bounds = new Rectangle(0, 0, Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

        int total_picture_count = 0;
        int sel_picture = -1;
        bool random_sel_picture = true;

        int show_picture_ratio_width = 30;
        int show_picture_ratio_height = 30;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int operation_mode = Properties.Settings.Default.operation_mode;

            if ((operation_mode == 0) || (operation_mode == 2))
                flag_operation_mode = operation_mode;

            string picture_folder = Properties.Settings.Default.picture_foldername;

            //tb_picture_folder_name.Text = picture_folder;
            //tb_ratio_width.Text = ratio_width.ToString();
            //tb_ratio_height.Text = ratio_height.ToString();
            //tb_play_interval.Text = play_interval.ToString();


            int ratio_width = Properties.Settings.Default.size_width;
            int ratio_height = Properties.Settings.Default.size_height;

            if ((ratio_width > 0) && (ratio_width <= 100))
            {
                show_picture_ratio_width = ratio_width;
            }

            if ((ratio_height > 0) && (ratio_height <= 100))
            {
                show_picture_ratio_height = ratio_height;
            }

            int play_interval = Properties.Settings.Default.play_interval;

            if ((play_interval > 100) && (play_interval <= 5000))
            {
                timer1.Interval = play_interval;
            }

            pic_foldername = Properties.Settings.Default.picture_foldername;

            if (Directory.Exists(pic_foldername) == false)     //確認資料夾是否存在
            {
                //richTextBox1.Text += "資料夾: " + pic_foldername + " 不存在，需要選擇\n";

                Form_Setup form_setup = new Form_Setup();    //實體化 Form_Setup 視窗物件
                form_setup.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                form_setup.ShowDialog();   //顯示 frm 視窗

                //確認資料夾
                pic_foldername = Properties.Settings.Default.picture_foldername;

                if (Directory.Exists(pic_foldername) == false)     //確認資料夾是否存在
                {
                    //richTextBox1.Text += "資料夾: " + pic_foldername + " 不存在，離開\n";

                    MessageBox.Show("圖片資料夾不存在, 離開", "ShowPicture", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    Application.Exit();
                }
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + pic_foldername + " 已存在，開啟之\n";
            }

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
            if (flag_operation_mode == MODE_0)
            {
                WindowState = FormWindowState.Maximized;
            }
            else if (flag_operation_mode == MODE_2)
            {
                this.Size = new Size(640, 480);
                WindowState = FormWindowState.Normal;

            }
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
                if (flag_operation_mode == MODE_0)
                {
                    this.WindowState = FormWindowState.Maximized;
                }
                else if (flag_operation_mode == MODE_0)
                {
                    WindowState = FormWindowState.Normal;
                }
            }
            timer1.Enabled = true;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
            {
                timer1.Enabled = false;
                this.Close();
            }
            else if (e.KeyData == Keys.F2)
            {
                timer1.Enabled = false;
                TopMost = false;

                Form_Setup form_setup = new Form_Setup();    //實體化 Form_Setup 視窗物件
                form_setup.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                form_setup.ShowDialog();   //顯示 frm 視窗

                timer1.Enabled = true;
                TopMost = true;
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
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //任選一張圖
            DirectoryInfo DInfo = new DirectoryInfo(pic_foldername);
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

            filename = pic_foldername + "\\" + FInfo[sel_picture].Name;

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

            while (W * show_picture_ratio_width / 100 < w)
            {
                //rtb.Text += "X";
                w = w * 4 / 5;
                h = h * 4 / 5;
            }

            //rtb.Text += "a2(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

            while (H * show_picture_ratio_height / 100 < h)
            {
                //rtb.Text += "Q";
                w = w * 4 / 5;
                h = h * 4 / 5;
            }

            rtb.Text += "b(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

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
                Graphics g = this.CreateGraphics();
                Random r = new Random();
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
            else if (flag_operation_mode == MODE_2)
            {
                this.Size = new Size(w, h);
                Graphics g = this.CreateGraphics();
                //g.Clear(Color.Pink);
                int x_st = 0;
                int y_st = 0;
                //Point ulCorner = new Point(x_st, y_st);
                //g.DrawImageUnscaled(image, ulCorner);

                //原圖貼上
                //    DrawImage   貼上位置x   貼上位置y   貼上大小W   貼上大小H
                g.DrawImage(image, x_st, y_st, w, h);
                //rtb.Text += "c(" + x_st.ToString() + ", " + y_st.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                g.DrawRectangle(new Pen(Color.White, 10), x_st, y_st, w, h);

                this.Size = new Size(w, h);
                this.Location = new Point(W - w, (H - h) / 2);
            }
            image.Dispose();
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            Application.Exit();
        }
    }
}
