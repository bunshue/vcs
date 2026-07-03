using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FullScreenSetup
{
    public partial class Form1 : Form
    {
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

            this.DoubleClick += new EventHandler(Form1_DoubleClick);
        }

        void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //重定義基類OnPaint()方法
        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            int y = 0;
            g.FillRectangle(Brushes.Wheat, ClientRectangle);    //繪制窗體背景色

            //g.FillRectangle(Brushes.Blue, rect);//墳充一個矩形

            Font f = new Font("微軟正黑體", 50, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(0, y, 400, f.Height);
            g.DrawString("全屏空白表單", f, Brushes.Black, rect);
            rect.Y += 80;
            g.DrawString("雙擊表單離開", f, Brushes.Black, rect);
            f.Dispose();

            using (Pen pen = new Pen(Color.Red, 1))
            {
                for (y = 0; y <= ClientRectangle.Height; y += ClientRectangle.Height / 12)
                {

                    g.DrawLine(pen, new Point(0, 0), new Point(ClientRectangle.Width, y));
                }
            }
            g.FillEllipse(Brushes.Red, new Rectangle(100, 100, 50, 50));

            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }
    }
}
