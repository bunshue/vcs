using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_Big_Bitmap
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {


            bitmap1 = new Bitmap(this.Width, this.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);
            g.DrawRectangle(Pens.Red, 0, 0, this.Width - 100, this.Height - 100);
            this.BackgroundImage = bitmap1;
        }

        int aaa = 100;
        private void button1_Click(object sender, EventArgs e)
        {
            g.DrawRectangle(Pens.Red, aaa, aaa, 200, 100);
            aaa += 10;



            this.BackgroundImage = bitmap1;
        }
    }
}
