using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 繪製矩形
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
            
                Bitmap bitM = new Bitmap(this.groupBox1.Width, this.groupBox1.Height);
                Graphics g = Graphics.FromImage(bitM);
                g.Clear(Color.White);
                g.DrawRectangle(new Pen(Color.Blue), 20, 20, this.groupBox1.Width - 40, this.groupBox1.Height - 30);
                this.groupBox1.BackgroundImage = bitM;

                Bitmap bitM2 = new Bitmap(this.groupBox2.Width, this.groupBox2.Height);
                Graphics g2 = Graphics.FromImage(bitM2);
                g2.Clear(Color.White);
                g2.FillRectangle(new SolidBrush(Color.Red), 20, 20, this.groupBox2.Width - 40, this.groupBox2.Height - 30);
                this.groupBox2.BackgroundImage = bitM2;

        }
    }
}