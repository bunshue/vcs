using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
全屏隨機位置顯示圖片


Form1的屬性

StartPosition改CenterScreen
WindowState改Maximized

ConrolBox改False
MaximizeBox改False
MinimizeBox改False
ShowIcon改False
ShowInTaskbar改False
TopMost改True

KeyPreview改True
*/

namespace vcs_ShowPicture5
{
    public partial class Form1 : Form
    {
        Rectangle bounds = Screen.GetBounds(Screen.GetBounds(Point.Empty));

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.BackgroundImage = GetNoCursor();

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
            string filename = @"C:\______test_files\picture1.jpg";
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

