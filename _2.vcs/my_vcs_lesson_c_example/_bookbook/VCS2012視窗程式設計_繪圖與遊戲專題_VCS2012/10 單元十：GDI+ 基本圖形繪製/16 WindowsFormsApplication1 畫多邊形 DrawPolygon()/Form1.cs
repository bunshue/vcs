using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point[] pt = new Point[5];  // 五個點

            int Cx = this.ClientSize.Width / 2;  // 中心點
            int Cy = this.ClientSize.Height / 2;
            int D = (int)(Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 2) - 10; // 半徑
            double Theta = -Math.PI / 2.0; // 角度

            int i;
            for (i = 0; i < 5; i++)
            {
                pt[i].X = Cx + (int)(D * Math.Cos(Theta));
                pt[i].Y = Cy + (int)(D * Math.Sin(Theta));
                Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                //Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }


            e.Graphics.DrawPolygon(Pens.Black, pt); // 繪出多邊形


            for (i = 0; i < 5; i++)
            {
                pt[i].X = Cx + (int)(D * Math.Cos(Theta));
                pt[i].Y = Cy + (int)(D * Math.Sin(Theta));
                //Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }
            e.Graphics.DrawPolygon(Pens.Red, pt); // 繪出多邊形

        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}