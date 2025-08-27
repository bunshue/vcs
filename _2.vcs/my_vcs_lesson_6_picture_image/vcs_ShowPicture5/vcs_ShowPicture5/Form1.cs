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

Form1的屬性

StartPosition 改 CenterScreen
WindowState 改 Maximized

ConrolBox 改 False
MaximizeBox 改 False
MinimizeBox 改 False
ShowIcon 改 False
ShowInTaskbar 改 False
TopMost 改 True

KeyPreview 改 True
*/

namespace vcs_ShowPicture5
{
    public partial class Form1 : Form
    {
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\";
        string filename = string.Empty;
        int total_picture_count = 0;
        int sel_picture = -1;
        bool random_sel_picture = true;

        Rectangle bounds = Screen.GetBounds(Screen.GetBounds(Point.Empty));

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;
            this.BackgroundImage = GetNoCursor();   //複製目前桌面當背景

            timer1.Interval = 500;
            timer1.Enabled = true;
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            /*
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
            */

            //看似有點問題
            //應改只要撈出圖片檔即可


            Image image = Image.FromFile(filename);
            if (image != null)
            {
                Graphics g = this.CreateGraphics();
                Random rd = new Random();
                int picXPoint = rd.Next(0, bounds.Right - image.Width);
                int picYPoint = rd.Next(0, bounds.Height - image.Height);
                Point ulCorner = new Point(picXPoint, picYPoint);
                g.DrawImageUnscaled(image, ulCorner);
            }
            else
            {
                timer1.Enabled = false;
                MessageBox.Show("無圖片, 離開...");
                this.Close();
            }
        }
    }
}

