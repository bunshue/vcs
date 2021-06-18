using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1111
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //抓 Ctrl + R
            byte asc = Convert.ToByte(e.KeyChar);
            label1.Text = "|  " + e.KeyChar.ToString() + "  |  " + asc.ToString() + "  |  " + asc.ToString("X2") + "  |";
            if (asc == 18)  //ctrl + A = 1, ctrl + B = 2, ..., ctrl + R = 18
            {
                label1.Text += "你按了ctrl + R";
            }

            //抓 Enter 鍵
            if (e.KeyChar == (char)Keys.Enter)
            {
                e.Handled = true;
                label1.Text += "你按了 Enter";
            }



        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            ShowPropertiesOfSlateBlue(e);

        }

        private void ShowPropertiesOfSlateBlue(PaintEventArgs e)
        {
            Color slateBlue = Color.FromName("SlateBlue");
            byte g = slateBlue.G;
            byte b = slateBlue.B;
            byte r = slateBlue.R;
            byte a = slateBlue.A;
            string text = String.Format("Slate Blue has these ARGB values: Alpha:{0}, " +
                "red:{1}, green: {2}, blue {3}", new object[] { a, r, g, b });
            e.Graphics.DrawString(text,
                new Font(this.Font, FontStyle.Italic),
                new SolidBrush(slateBlue),
                new RectangleF(new PointF(0.0F, 0.0F), this.Size));

            //this.Font = new Font(
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


    }
}
