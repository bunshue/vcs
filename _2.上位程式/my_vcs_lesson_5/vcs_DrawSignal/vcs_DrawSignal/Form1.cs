using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawSignal
{
    public partial class Form1 : Form
    {
        Graphics g;
        int y_positon;
        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();
            y_positon = this.ClientSize.Height / 2;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Point[] pt = new Point[360];    //一維陣列內有360個Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = y_positon - (int)(amplitude * Math.Sin(angle*3 * Math.PI / 180));

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Point[] pt = new Point[360];    //一維陣列內有360個Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                if (angle <= 120)
                {
                    if ((angle % 10) < 5)
                        pt[angle].Y = y_positon - amplitude;
                    else
                        pt[angle].Y = y_positon;

                    //pt[angle].Y = amplitude;
                }
                else if (angle <= 180)
                {
                    if ((angle % 10) < 5)
                    {
                        pt[angle].Y = y_positon - amplitude / 2;
                    }
                    else
                        pt[angle].Y =  y_positon;
                }
                else if (angle <= 300)
                {
                    pt[angle].Y =  y_positon;
                }
                else if (angle <= 360)
                {
                    if ((angle % 10) < 5)
                    {
                        pt[angle].Y = y_positon - amplitude / 2;
                    }
                    else
                        pt[angle].Y =  y_positon;

                }
            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);

        }
    }
}
