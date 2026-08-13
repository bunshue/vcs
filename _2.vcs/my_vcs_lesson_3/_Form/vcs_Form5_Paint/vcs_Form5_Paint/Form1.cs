using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form5_Paint
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

        //------------------------------------------------------------  # 60個
        /*
        protected override void OnSizeChanged(EventArgs e)
        {
            Invalidate();
            base.OnSizeChanged(e);

            this.Text = this.Size.ToString();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Pen p = new Pen(Color.Red, 10);
            e.Graphics.DrawRectangle(p, 50, 50, this.ClientSize.Width - 100, this.ClientSize.Height - 100);

            base.OnPaint(e);
        }
        */
        //------------------------------------------------------------  # 60個

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
            //this.Refresh(); //執行 Form1_Paint()
        }

        //------------------------------------------------------------  # 60個

        //表單背景作圖, 只要補這一段就好
        protected override void OnPaintBackground(PaintEventArgs e)
        {
            e.Graphics.Clear(Color.Pink);
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            e.Graphics.DrawRectangle(Pens.Red, 50, 50, W - 50 * 2, H - 50 * 2);

            Font f = new Font("微軟正黑體", 22, FontStyle.Bold);//建立字體物件
            e.Graphics.DrawString("OnPaintBackground,\n直接寫 override", f, Brushes.Black, 100, 100);
        }

        /*
        protected override void OnPaintBackground(PaintEventArgs e)
        {
            //不進行背景的繪制
        }
        */

        //------------------------------------------------------------  # 60個

        /*
        //重定義基類OnPaint()方法
        //直接寫一個OnPaint在此, 取代Form1_Paint
        //重寫表單的OnPaint範例, 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            //畫邊框
            e.Graphics.DrawRectangle(new Pen(Color.Green, 10), new Rectangle(5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10));

            //寫字
            int x_st = 50;
            int y_st = 150;
            e.Graphics.DrawString("用 OnPaint 寫字", new Font("標楷體", 20, FontStyle.Italic), new SolidBrush(Color.Green), x_st, y_st);
        }
        */

        //------------------------------------------------------------  # 60個

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //畫邊框
            e.Graphics.DrawRectangle(new Pen(Color.Red, 10), new Rectangle(5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10));

            //寫字
            int x_st = 50;
            int y_st = 100;
            e.Graphics.DrawString("用 Form1_Paint 寫字", new Font("標楷體", 20, FontStyle.Italic), new SolidBrush(Color.Red), x_st, y_st);
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*

*/
