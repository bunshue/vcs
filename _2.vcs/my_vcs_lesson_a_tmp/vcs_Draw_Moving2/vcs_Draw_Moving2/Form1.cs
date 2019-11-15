using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Moving2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_case1\\pic1.jpg";

        Graphics g;
        Pen p;
        Bitmap bitmap1;


        public Form1()
        {
            InitializeComponent();
        }

        int tt = 0;
        int xx = 0;
        int yy = 0;
        double gg = 9.8;

        private void button1_Click(object sender, EventArgs e)
        {
            tt = 0;
            xx = 0;
            yy = 0;
            timer1.Enabled = true;

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

            /*
            xx += 2;
            yy += 2;
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx, yy, 20, 20));

            if (xx >= 300)
                yy -= 4;

            if (xx >= 600)
                timer1.Enabled = false;
            */

            tt++;
            xx = tt * 40;
            yy = (int)(gg * tt * tt / 2);
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx, yy, 20, 20));

            if (xx >= 200)
                yy -= 4;

            if (xx >= 400)
                timer1.Enabled = false;

        }
    }
}
