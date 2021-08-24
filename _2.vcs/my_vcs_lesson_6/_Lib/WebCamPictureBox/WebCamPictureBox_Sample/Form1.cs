using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace WebCamPictureBox_Sample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.webCamPictureBox1.TestConnect())
            {
                richTextBox1.Text += "測試連線 OK\n";
            }
            else
            {
                richTextBox1.Text += "測試連線 NG\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.webCamPictureBox1.Start();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.webCamPictureBox1.Stop();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.webCamPictureBox2.Image = this.webCamPictureBox1.Image;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (this.webCamPictureBox1.Image != this.webCamPictureBox1.Image)
            {
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    this.webCamPictureBox1.Image.Save(filename, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

        private void webCamPictureBox1_WebCamConnectStateChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += this.webCamPictureBox1.IsStarted ? "Start" : "Stop" + "\n";
        }
    }
}

