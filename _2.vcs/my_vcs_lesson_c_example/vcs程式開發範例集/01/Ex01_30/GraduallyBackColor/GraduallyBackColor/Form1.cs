using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace GraduallyBackColor
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
        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            this.Visible=true;
        }
        protected override void OnPaintBackground(PaintEventArgs e)
        {
            int y, dy;
            y = this.ClientRectangle.Location.Y;
            dy = this.ClientRectangle.Height / 256;
            for (int i = 255; i >= 0; i--)
            {
              
                Color c = new Color();
                c = Color.FromArgb(Convert.ToInt32(textBox1.Text.ToString()), i,Convert.ToInt32(textBox2.Text.ToString()));
                SolidBrush sb = new SolidBrush(c);
                Pen p = new Pen(sb, 1);
                e.Graphics.DrawRectangle(p,this.ClientRectangle.X, y, this.Width,y+dy);
                y = y + dy;
            }
        }
    }
}