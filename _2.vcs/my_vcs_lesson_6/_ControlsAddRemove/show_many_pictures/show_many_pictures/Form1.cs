using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace show_many_pictures
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            int W = 640;
            int H = 480;

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox1.ClientSize = new Size(W, H);        //設定pictureBox的大小
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox2.ClientSize = new Size(W, H);        //設定pictureBox的大小
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox3.ClientSize = new Size(W, H);        //設定pictureBox的大小
            pictureBox4.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox4.ClientSize = new Size(W, H);        //設定pictureBox的大小
            pictureBox5.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox5.ClientSize = new Size(W, H);        //設定pictureBox的大小
            pictureBox6.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox6.ClientSize = new Size(W, H);        //設定pictureBox的大小

            pictureBox1.Location = new Point(0, 0);
            pictureBox2.Location = new Point(W, 0);
            pictureBox3.Location = new Point(W * 2, 0);
            pictureBox4.Location = new Point(0, H);
            pictureBox5.Location = new Point(W, H);
            pictureBox6.Location = new Point(W * 2, H);

            this.ClientSize = new Size(W * 3 + 1, H * 2 + 1);

            show_pictures();


        }

        void show_pictures()
        {
            String filename1 = string.Empty;
            String filename2 = string.Empty;
            String filename3 = string.Empty;
            String filename4 = string.Empty;
            String filename5 = string.Empty;
            String filename6 = string.Empty;

            filename1 = Application.StartupPath + "\\picture\\a01.bmp";
            filename2 = Application.StartupPath + "\\picture\\a02.bmp";
            filename3 = Application.StartupPath + "\\picture\\a03.bmp";
            filename4 = Application.StartupPath + "\\picture\\a04.bmp";
            filename5 = Application.StartupPath + "\\picture\\a05.bmp";
            filename6 = Application.StartupPath + "\\picture\\a06.bmp";

            pictureBox1.Image = Image.FromFile(filename1);
            pictureBox2.Image = Image.FromFile(filename2);
            pictureBox3.Image = Image.FromFile(filename3);
            pictureBox4.Image = Image.FromFile(filename4);
            pictureBox5.Image = Image.FromFile(filename5);
            pictureBox6.Image = Image.FromFile(filename6);


        }

    }
}
