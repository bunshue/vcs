using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form5_OnPaintBackground
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

        //表單背景作圖, 只要補這一段就好
        protected override void OnPaintBackground(PaintEventArgs e)
        {
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            e.Graphics.DrawRectangle(Pens.Red, 50, 50, W - 50 * 2, H - 50 * 2);

            Font f = new Font("微軟正黑體", 22, FontStyle.Bold);//建立字體物件
            e.Graphics.DrawString("OnPaintBackground,\n直接寫 override", f, Brushes.Black, 100, 100);
        }
    }
}
