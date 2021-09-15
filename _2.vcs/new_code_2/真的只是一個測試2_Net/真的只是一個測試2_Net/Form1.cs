using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Runtime.InteropServices;


namespace 真的只是一個測試2_Net
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
        }

        static void download()
        {


            string url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Breathe-face-smile.svg/1200px-Breathe-face-smile.svg.png";

            using (WebClient client = new WebClient())
            {
                client.DownloadFile(new Uri(url), "Image.png");
            }
        }
        

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                download();
            }
            catch (ExternalException ex)
            {
                Console.WriteLine(ex.Message);

            }
            catch (ArgumentNullException ex)
            {
                Console.WriteLine(ex.Message);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {

            //在 C# 中使用 DownloadFile() 方法從一個 URL 下載檔案
            WebClient mywebClient = new WebClient();
            mywebClient.DownloadFile("https://wiki.linuxfoundation.org/_media/wiki/logo.png", @"C:\dddddddddd\aaaaa.png");


        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
