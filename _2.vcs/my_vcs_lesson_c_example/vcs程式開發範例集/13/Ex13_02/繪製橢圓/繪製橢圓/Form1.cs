using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 繪製橢圓
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
            ShowPic1();
            ShowPic2();
            ShowPic3();
        }

        private void ShowPic()
        {

            Bitmap bitM = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
                Graphics g = Graphics.FromImage(bitM);
                g.Clear(Color.White);
                g.DrawEllipse(new Pen(Color.Blue), 10, 10, 100, 60);
                this.pictureBox1.BackgroundImage = bitM;
        }
        private void ShowPic1()
        {
            
            Bitmap bitM = new Bitmap(this.pictureBox2.Width, this.pictureBox2.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.White);
            g.DrawEllipse(new Pen(Color.Blue), 30, 10, 70, 70);
            this.pictureBox2.BackgroundImage = bitM;
        }

        private void ShowPic2()
        {
            
            Bitmap bitM = new Bitmap(this.pictureBox3.Width, this.pictureBox3.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.White);
            g.DrawArc(new Pen(Color.Blue), 10, 20, 100, 50, 30, 180);
            this.pictureBox3.BackgroundImage = bitM;
        }

        private void ShowPic3()
        {
         
            Bitmap bitM = new Bitmap(this.pictureBox4.Width, this.pictureBox4.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.White);
            g.FillPie(new SolidBrush(Color.Red),10, 20, 100, 50, 90, 270);
            g.FillPie(new SolidBrush(Color.Yellow), 10, 20, 100, 50, 90+270, 90);
            this.pictureBox4.BackgroundImage = bitM;
        }

    
      
    }
}