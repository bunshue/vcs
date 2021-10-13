using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_DoubleBuffer
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

        //直接寫一個OnPaint在此
        protected override void OnPaint(PaintEventArgs e)
        {
            //test_double_buffer1(e); //不使用雙倍緩衝
            test_double_buffer2(e); //使用雙倍緩衝
        }

        void test_double_buffer1(PaintEventArgs e)
        {
            label3.Text = "不使用雙倍緩衝";
            e.Graphics.FillRectangle(Brushes.White, ClientRectangle);
            Random r = new Random();
            for (int x = 0; x < ClientRectangle.Width; x++)
            {
                for (int y = 0; y < ClientRectangle.Height; y += 10)
                {
                    Color c = Color.FromArgb(r.Next(255), r.Next(255), r.Next(255));
                    using (Pen pen = new Pen(c, 1))
                    {
                        e.Graphics.DrawLine(pen, new Point(0, 0), new Point(x, y));
                    }
                }
            }
        }

        void test_double_buffer2(PaintEventArgs e)
        {
            label3.Text = "使用雙倍緩衝";
            Random r = new Random();
            Image im = new Bitmap(ClientRectangle.Width, ClientRectangle.Height);
            Graphics g = Graphics.FromImage(im);//建立一張新的GDI+繪圖介面
            g.FillRectangle(Brushes.White, ClientRectangle);
            for (int x = 0; x < ClientRectangle.Width; x++)
            {
                for (int y = 0; y < ClientRectangle.Height; y += 10)
                {
                    Color c = Color.FromArgb(r.Next(255), r.Next(255), r.Next(255));
                    using (Pen pen = new Pen(c, 1))
                    {
                        g.DrawLine(pen, new Point(0, 0), new Point(x, y));//線條先繪製到新建的那張不可見的介面上
                    }
                }
            }
            e.Graphics.DrawImage(im, ClientRectangle);
            im.Dispose();
        }
    }
}
