using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

// C#全屏随机位置显示图片的小程序

namespace vcs_ShowPicture3
{
    public partial class Form1 : Form
    {
        Rectangle bounds = Screen.GetBounds(Screen.GetBounds(Point.Empty));

        string foldername = @"C:\______test_files\_pic\";
        string filename;
        int sel_picture = -1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.WindowState = FormWindowState.Maximized;

            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            this.ShowInTaskbar = false;

            this.TopMost = true;
            this.KeyPreview = true;

            this.KeyDown += Form1_KeyDown;
            
            //this.BackgroundImage = GetNoCursor(); //複製目前桌面當背景
            this.BackColor = Color.Black;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
            {
                timer1.Enabled = false;
                this.Close();
            }
        }

        private Bitmap GetNoCursor()
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
            Random rand = new Random();
            sel_picture = rand.Next(FInfo.Length);

            filename = foldername + FInfo[sel_picture].Name;
            //richTextBox1.Text += "sel_picture = " + sel_picture.ToString() + "filename : " + filename + "\n";
            

            Image image = Image.FromFile(filename);

            if (image != null)
            {
                int W = bounds.Right;
                int H = bounds.Height;
                int w = image.Width;
                int h = image.Height;

                //richTextBox1.Text += "a1(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                while (W < (w * 3))
                {
                    //richTextBox1.Text += "X";
                    w = w * 4 / 5;
                    h = h * 4 / 5;
                }

                //richTextBox1.Text += "a2(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                while (H < (h * 3))
                {
                    //richTextBox1.Text += "Q";
                    w = w * 4 / 5;
                    h = h * 4 / 5;
                }

                //richTextBox1.Text += "b(" + W.ToString() + ", " + H.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                Graphics g = this.CreateGraphics();
                Random r = new Random();

                //richTextBox1.Text += "c(" + (W - w).ToString() + ", " + (H - h).ToString() + "\n";

                if (w > W)
                {
                    timer1.Enabled = false;
                }

                if (h > H)
                {
                    timer1.Enabled = false;
                }

                int x_st = r.Next(0, W - w);
                int y_st = r.Next(0, H - h);
                //Point ulCorner = new Point(x_st, y_st);
                //g.DrawImageUnscaled(image, ulCorner);

                //原圖貼上
                //               貼上位置x      貼上位置y      貼上大小W            貼上大小H

                //richTextBox1.Text += "c(" + x_st.ToString() + ", " + y_st.ToString() + ")-(" + w.ToString() + ", " + h.ToString() + ")\n";

                g.DrawImage(image, x_st, y_st, w, h);
                g.DrawRectangle(new Pen(Color.White, 10), x_st, y_st, w, h);
            }
            else
            {
                timer1.Enabled = false;
                MessageBox.Show("無圖片");
                this.Close();
            }
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            Application.Exit();
        }
    }
}
