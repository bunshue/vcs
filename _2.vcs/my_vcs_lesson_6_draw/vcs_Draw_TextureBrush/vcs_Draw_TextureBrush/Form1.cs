using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_TextureBrush
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //使用TextureBrush類繪製圖像

            string filename = @"C:\______test_files\_icon\唐.ico";

            Image theimage;
            Image smallimage;
            SetStyle(ControlStyles.Opaque, true);
            Bounds = new Rectangle(0, 0, 1300, 850);
            theimage = new Bitmap(filename);
            smallimage = new Bitmap(theimage, new Size(theimage.Width, theimage.Height));

            Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, ClientRectangle);

            Brush brush = new TextureBrush(smallimage, new Rectangle(0, 0, smallimage.Width, smallimage.Height));
            //用圖像創建畫筆,來繪制圖像
            g.FillEllipse(brush, new Rectangle(0, 200, 200, 200));
            //用圖像創建剛筆,來繪制圖像
            Pen pen = new Pen(brush, 20);
            g.DrawRectangle(pen, new Rectangle(250, 200, 200, 200));
            //用圖像繪製文本
            Font font = new Font("Times New Roman", 60, FontStyle.Bold | FontStyle.Italic);
            g.DrawString("Hello Image !!", font, brush, new Rectangle(0, 0, 500, font.Height));

            brush.Dispose();
            font.Dispose();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

    }
}
