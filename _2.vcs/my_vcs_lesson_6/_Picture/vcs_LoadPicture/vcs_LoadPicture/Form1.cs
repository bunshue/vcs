using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File, FileStream

namespace vcs_LoadPicture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox1.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
            comboBox1.SelectedIndex = 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image image1 = Image.FromFile("C:\\______test_files\\_case1\\pic1.jpg");
            pictureBox1.Image = image1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Image image1 = new Bitmap(@"C:\______test_files\_case1\\pic2.jpg", true);
            pictureBox1.Image = image1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //法一
            //ImageLocation	取得或設定路徑或影像 URL 中顯示 PictureBox
            //pictureBox1.ImageLocation = "C:\\______test_files\\_case1\\pic3.jpg";

            //法二
            //Load()		顯示所指定的影像 ImageLocation 屬性 PictureBox。
            //string ImageLocation = "C:\\______test_files\\_case1\\pic3.jpg";
            //pictureBox1.Load(ImageLocation);

            //法三
            //Load(String)	設定 ImageLocation 到指定的 URL，並顯示所指出的影像。
            pictureBox1.Load("C:\\______test_files\\_case1\\pic3.jpg");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.ImageLocation = "http://www.myson.com.tw/images/index/ad01.jpg";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            DateTime dt = DateTime.Now;
            int Minute;
            pictureBox1.ClientSize = new Size(800, 800);

            //加入這段語法忽略憑證
            System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            for (i = 0; i < 5; i++)
            {
                Minute = (dt.Minute / 10) * 10;
                string mapURL = string.Format("https://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-{0}-{1}-{2}-{3}-{4}.jpg",
                    dt.Year,
                    dt.Month.ToString("00"),
                    dt.Day.ToString("00"),
                    dt.Hour.ToString("00"),
                    Minute.ToString("00"));
                //MessageBox.Show("path: " + mapURL);

                try
                {   //可能會產生錯誤的程式區段
                    pictureBox1.Load(mapURL);
                    break;
                }
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    //MessageBox.Show("path: " + mapURL);
                    //MessageBox.Show(ex.Message);
                }
                finally
                {
                    //一定會被執行的程式區段
                    //MessageBox.Show("path: " + mapURL);
                }
                dt = dt.AddMinutes(-10);
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //圖片SizeMode
            int sizemode = comboBox1.SelectedIndex;
            switch (sizemode)
            {
                case 0:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                case 1:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 2:
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 3:
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 4:
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                default:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //錯誤的寫法, 可能會出現"記憶體不足"
            //pictureBox1.Image = Image.FromFile(@"c:\______test_files\bear.bmp");

            //正確的寫法
            FileStream fs = File.OpenRead(@"c:\______test_files\bear.bmp");
            pictureBox1.Image = Image.FromStream(fs);
            fs.Close();

        }
    }
}
