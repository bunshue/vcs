using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 繪製曲線
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowPic();
        }

        private void ShowPic()
        {
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            Graphics g=Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[4];
            Random r = new Random();
            for (int i = 0; i < 4; i++)
            {
                points[i].X = r.Next(20, this.panel1.Width);
                points[i].Y = r.Next(30, this.panel1.Height);
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //繪製折線 
            this.panel1.BackgroundImage = bitM;
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            ShowPic();
        }
    }
}