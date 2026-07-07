using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form4_MouseWheel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.MouseWheel += new MouseEventHandler(Form1_MouseWheel);
        }

        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            //this.Width += e.Delta;
            //this.Height += e.Delta;
            if (e.Delta > 0)
            {
                this.Width++;
                this.Height++;
            }
            else
            {
                this.Width--;
                this.Height--;
            }
            this.Invalidate();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            Graphics g = e.Graphics;
            g.DrawRectangle(Pens.Red, 5, 5, W - 10, H - 10);

            Font f = new Font("標楷體", 15);
            g.DrawString("隨滑鼠滾輪滾動改變大小", f, new SolidBrush(Color.Red), new PointF(100, 100));

            //隨滑鼠滾輪滾動改變大小
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

 */

