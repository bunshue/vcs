using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ZoomPicture_Lanczos
{
    public partial class Form2 : Form
    {
        string filename = string.Empty;
        public Form2(string pic_filename)
        {
            InitializeComponent();

            filename = pic_filename;
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            pictureBox1.Image = bitmap1;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.ClientSize = new Size(W, H);
            this.ClientSize = new Size(W, H);
            this.Text = "W = " + W.ToString() + ", H = " + H.ToString();

        }
    }
}
