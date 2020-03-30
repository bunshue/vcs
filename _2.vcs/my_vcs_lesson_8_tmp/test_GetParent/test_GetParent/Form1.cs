using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;



namespace test_GetParent
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            GetLogicalDrives();
        }

        // Print out all logical drives on the system.
        void GetLogicalDrives()
        {
            try
            {
                string[] drives = System.IO.Directory.GetLogicalDrives();

                foreach (string str in drives)
                {
                    System.Console.WriteLine(str);
                    richTextBox1.Text += "drive : " + str + "\n";
                }
            }
            catch (System.IO.IOException)
            {
                System.Console.WriteLine("An I/O error occurs.");
            }
            catch (System.Security.SecurityException)
            {
                System.Console.WriteLine("The caller does not have the " +
                    "required permission.");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_case1\pic1.jpg";
            FileStream fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            Byte[] image = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(image, 0, filelength); //按位元組流讀取
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();

            //pictureBox1.Image = (Image)image;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            for (int i = 1; i <= 10; i++)
            {
                this.Controls["label" + i.ToString()].Text = "這是label" + i.ToString();

            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            System.Globalization.CultureInfo cuinfo = new System.Globalization.CultureInfo("zh-TW");
            cuinfo.DateTimeFormat.Calendar = cuinfo.OptionalCalendars[2];
            //richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd", cuinfo) + "\n";
            MessageBox.Show(DateTime.Now.ToString("yyyy/MM/dd", cuinfo));

        }

        private void button9_Click(object sender, EventArgs e)
        {
            String strOrg = "ABCDE";
            // Encoding.GetBytes方法，將 String 轉為 Byte 序列
            byte[] stringConvByte = Encoding.Default.GetBytes(strOrg);
            // Encoding.GetString方法，將 Byte 序列 轉為 String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);

            int i;
            richTextBox1.Text += "len of strOrg = " + strOrg.Length.ToString() + "\n";
            for (i = 0; i < strOrg.Length; i++)
            {
                richTextBox1.Text += "value is " + strOrg[i] + "\n";
                richTextBox1.Text += "value is " + strOrg[i].ToString() + "\n";
                //richTextBox1.Text += "value is\n";

            }
            richTextBox1.Text += "len of stringConvByte = " + stringConvByte.Length.ToString() + "\n";
            for (i = 0; i < stringConvByte.Length; i++)
            {
                richTextBox1.Text += "value is " + stringConvByte[i].ToString("X2") + "\n";
                //richTextBox1.Text += "value is\n";

            }
            richTextBox1.Text += "len of byteConvStrig = " + byteConvStrig.Length.ToString() + "\n";


        }






    }
}
