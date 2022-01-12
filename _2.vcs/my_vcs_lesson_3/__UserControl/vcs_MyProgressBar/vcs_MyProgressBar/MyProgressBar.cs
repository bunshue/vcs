using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyProgressBar
{
    public partial class MyProgressBar : UserControl
    {
        private int val;//进度值
        private Color PBackgroundColor = Color.FromArgb(217, 218, 219);//初始化颜色
        private Color PForegroundColor = Color.Green;

        public MyProgressBar()
        {
            InitializeComponent();
        }

        /// <summary>
        /// 背景色
        /// </summary>
        public Color pBackgroundColor
        {
            get
            {
                return PBackgroundColor;
            }
            set
            {
                PBackgroundColor = value;
                this.BackColor = PBackgroundColor;
            }
        }
        /// <summary>
        /// 前景色
        /// </summary>
        public Color pForegroundColor
        {
            get
            {
                return PForegroundColor;
            }
            set
            {
                PForegroundColor = value;
            }
        }
        /// <summary>
        /// 当前值
        /// </summary>
        public int Value
        {
            get
            {
                return val;
            }
            set
            {
                val = value;
                this.Invalidate();
            }
        }
        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            SolidBrush brush;
            if (val < 30)
            {
                brush = new SolidBrush(Color.Lime);
            }
            else if (val < 60)
            {
                brush = new SolidBrush(Color.DarkGreen);
            }
            else if (val < 80)
            {
                brush = new SolidBrush(Color.Red);
            }
            else
            {
                brush = new SolidBrush(Color.DarkRed);
            }
            float percent = val / 100f;
            Rectangle rect = this.ClientRectangle;
            rect.Width = (int)((float)rect.Width * percent);
            rect.Height = this.Height;
            Console.WriteLine("宽度:{0}", rect.Width);
            g.FillRectangle(brush, rect);
            brush.Dispose();
            g.Dispose();
        }
    }
}
