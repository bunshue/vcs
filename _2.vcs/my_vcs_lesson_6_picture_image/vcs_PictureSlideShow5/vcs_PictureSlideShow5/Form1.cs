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
        int width = 0;
        int heigh = 0;
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_MU";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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
            Graphics g = this.CreateGraphics();
            g.Clear(Color.Black);
            Bitmap bitmap1 = new Bitmap(foldername + "\\id_card_0" + new Random().Next(1, 6).ToString() + ".jpg");
            //richTextBox1.Text += "filename " + foldername + "\\id_card_0" + new Random().Next(1, 6).ToString() + ".jpg" + "\n";

            g.DrawImage(bitmap1, new Random().Next(0, width - bitmap1.Width), new Random().Next(0, heigh - bitmap1.Height));
            //richTextBox1.Text += "a " + (new Random().Next(0, width - bitmap1.Width)).ToString() + "\n";
            //richTextBox1.Text += "b " + (new Random().Next(0, heigh - bitmap1.Height)).ToString() + "\n";
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



