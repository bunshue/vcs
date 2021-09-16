using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_3_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            imageList1.ImageSize = new Size(128, 90);
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_01.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_02.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_03.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_04.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_05.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_06.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_07.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_08.png"));
            imageList1.Images.Add(Image.FromFile("c:\\PNG\\Vista_icons_08.png"));

            button1.ImageList = imageList1;
            textBox1.Text = "1";
            label2.Text = "**詢圖片編號：";
            label1.Text = "目前共有 " + imageList1.Images.Count.ToString() + " 張圖片可用";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ndx = 0;
            if (textBox1.Text != "")
            {
                ndx = Convert.ToInt32(textBox1.Text);
                if (ndx >= 0 && ndx < imageList1.Images.Count)
                {
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    pictureBox1.Image = imageList1.Images[ndx];

                    button1.ImageIndex = ndx;
                }
                else
                    MessageBox.Show("數字不正確！");
            }
            else
                MessageBox.Show("請輸入正確的數字！");
        }
    }
}
