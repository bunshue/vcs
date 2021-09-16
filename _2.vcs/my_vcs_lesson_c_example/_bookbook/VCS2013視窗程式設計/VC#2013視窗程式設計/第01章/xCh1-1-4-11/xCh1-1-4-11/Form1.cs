using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh1_1_4_11
{
    public partial class Form1 : Form
    {
        Point mouseOffset;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;
            this.Width = this.BackgroundImage.Width;
            this.Height = this.BackgroundImage.Height;
            this.TransparencyKey = Color.FromArgb(0, 255,0);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            mouseOffset = new Point(e.X, e.Y);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Left += e.X - mouseOffset.X;
                this.Top += e.Y - mouseOffset.Y;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
