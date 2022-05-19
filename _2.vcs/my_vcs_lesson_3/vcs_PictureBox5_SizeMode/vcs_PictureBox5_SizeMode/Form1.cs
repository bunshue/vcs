using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox5_SizeMode
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "pictureBox1 大小 W = " + pictureBox1.Width.ToString() + ", H = " + pictureBox1.Height.ToString() + "\n";
            richTextBox1.Text += "圖片 大小 W = " + pictureBox1.Image.Width.ToString() + ", H = " + pictureBox1.Image.Height.ToString() + "\n";
        }

        int flag_radiobutton_old = 0;
        private void change_size_mode(object sender, EventArgs e)
        {
            if (radioButton0.Checked == true)
            {
                if (flag_radiobutton_old == 0)
                    return;
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                flag_radiobutton_old = 0;
            }
            else if (radioButton1.Checked == true)
            {
                if (flag_radiobutton_old == 1)
                    return;
                flag_radiobutton_old = 1;
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            }
            else if (radioButton2.Checked == true)
            {
                if (flag_radiobutton_old == 2)
                    return;
                flag_radiobutton_old = 2;
                pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            }
            else if (radioButton3.Checked == true)
            {
                if (flag_radiobutton_old == 3)
                    return;
                flag_radiobutton_old = 3;
                pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
            }
            else if (radioButton4.Checked == true)
            {
                if (flag_radiobutton_old == 4)
                    return;
                flag_radiobutton_old = 4;
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            }
            else
            {
                flag_radiobutton_old = 0;
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            }
        }
    }
}
