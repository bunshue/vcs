using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureSlideShow5
{
    public partial class Form1 : Form
    {
        int width = 0, heigh = 0;
        string strpath;
        string foldername = @"C:\______test_files\_pic";

        public Form1()
        {
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            strpath = foldername;
            Cursor.Hide();
            this.timer1.Enabled = true;
            width = this.Width;
            heigh = this.Height;
            drowImage();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.timer1.Interval = new Random().Next(500, 2000);
            drowImage();
        }

        private void drowImage()
        {
            Graphics myGraphics = this.CreateGraphics();
            myGraphics.Clear(Color.Black);
            Bitmap myBitmap = new Bitmap(strpath + "\\id_card_0" + new Random().Next(1, 6).ToString() + ".jpg");
            //richTextBox1.Text += "filename " + strpath + "\\id_card_0" + new Random().Next(1, 6).ToString() + ".jpg" + "\n";

            myGraphics.DrawImage(myBitmap, new Random().Next(0, width - myBitmap.Width), new Random().Next(0, heigh - myBitmap.Height));
            //richTextBox1.Text += "a " + (new Random().Next(0, width - myBitmap.Width)).ToString() + "\n";
            //richTextBox1.Text += "b " + (new Random().Next(0, heigh - myBitmap.Height)).ToString() + "\n";
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            ExitWindows();
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            ExitWindows();
        }

        private void ExitWindows()
        {
            this.timer1.Enabled = false;
            Application.Exit();
        }
    }
}


