using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form6_NotRectangle3
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_bmp\not_rectangle.bmp";

            bitmap1 = new Bitmap(filename);
            bitmap1.MakeTransparent(Color.Blue);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawImage((Image)bitmap1, new Point(0, 0));
        }


    }
}
