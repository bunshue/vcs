using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
namespace SpecialSharpWindows
{
    public partial class Form1 : Form
    {
        Bitmap bit;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bit = new Bitmap("heart.bmp");
            bit.MakeTransparent(Color.Blue);
        }
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawImage((Image)bit, new Point(0, 0));
        }

        private void label1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}