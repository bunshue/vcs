using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;      //for StreamReader

namespace my_vcs_01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OperatingSystem myOS = Environment.OSVersion;
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        MessageBox.Show("系統版本：" + "Windows 2000 " + myOS.ServicePack);
                        break;
                    case 1:
                        MessageBox.Show("系統版本：" + "Windows XP " + myOS.ServicePack);
                        break;
                    case 2:
                        MessageBox.Show("系統版本：" + "Windows Server 2003 " + " " + myOS.ServicePack);
                        break;
                    default:
                        MessageBox.Show("系統版本：" + myOS.ToString() + " " + myOS.ServicePack);
                        break;
                }
            }
            else
                MessageBox.Show("系統版本：" + myOS.VersionString + " " + myOS.ServicePack);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //StreamReader sr = new StreamReader(openFileDialog1.FileName);
                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox1.Text = sr.ReadToEnd();	//讀取所有文字內容
                sr.Close();
            }
        }

        Image myImage;
        private void button5_Click(object sender, EventArgs e)
        {
            openFileDialog2.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            if (openFileDialog2.ShowDialog() == DialogResult.OK)
            {
                myImage = System.Drawing.Image.FromFile(openFileDialog2.FileName);
                pictureBox1.Image = myImage;
                pictureBox1.Height = myImage.Height;
                pictureBox1.Width = myImage.Width;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            OperatingSystem myOS = Environment.OSVersion;
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        label2.Text = "系統版本：" + "Windows 2000 " + myOS.ServicePack;
                        break;
                    case 1:
                        label2.Text = "系統版本：" + "Windows XP " + myOS.ServicePack;
                        break;
                    case 2:
                        label2.Text = "系統版本：" + "Windows Server 2003 " + " " + myOS.ServicePack;
                        break;
                    default:
                        label2.Text = "系統版本：" + myOS.ToString() + " " + myOS.ServicePack;
                        break;
                }
            }
            else
                label2.Text = "系統版本：" + myOS.VersionString + " " + myOS.ServicePack;
        }




    }
}
