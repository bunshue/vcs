using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Line
{
    public partial class Form1 : Form
    {
        int x1 = 0;
        int y1 = 0;
        bool flag_mouse_down = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            //this.Invalidate();
            x1 = e.X;
            y1 = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {

                Graphics g = this.CreateGraphics();
                g.Clear(Color.White);//清除
                using (Pen p = new Pen(Brushes.Blue, 10))
                {
                    g.DrawLine(p, x1, y1, e.X, e.Y);
                }
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            //this.Invalidate();

            Graphics g = Graphics.FromHwnd(this.Handle);//Graphics g = this.CreateGraphics();

            using (Pen p = new Pen(Brushes.Blue, 10))
            {
                g.DrawLine(p, x1, y1, e.X, e.Y);
            }
        }
    }
}
