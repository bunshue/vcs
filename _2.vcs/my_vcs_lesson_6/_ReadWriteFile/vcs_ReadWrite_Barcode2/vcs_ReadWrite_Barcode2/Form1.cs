using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat

using ZXing;
using ZXing.QrCode;
using ZXing.Common;
using System.Text.RegularExpressions;
using ZXing.QrCode.Internal;

namespace vcs_ReadWrite_Barcode2
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1 = null;
        Bitmap bitmap2 = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //要轉成QRCode 的內容
            string content = richTextBox1.Text;
            //儲存圖片
            string filename1 = Application.StartupPath + "\\qr_code_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
            string filename2 = Application.StartupPath + "\\qr_code_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            bitmap1.Save(filename1, ImageFormat.Png);
            bitmap1.Save(filename2, ImageFormat.Jpeg);
            //顯示在畫面中
            pictureBox1.Image = bitmap1;
            */
            string contents = "123456";
            string path = @"C:\dddddddddd\";
            string result = CreateBarCode(contents, path);
            richTextBox1.Text += result + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        /// <summary>
        /// 一維碼生成
        /// </summary>
        public static string CreateBarCode(string contents, string tempPath)
        {
            EncodingOptions options = null;
            BarcodeWriter writer = null;
            options = new EncodingOptions { Width = 200, Height = 200 };
            writer = new BarcodeWriter();
            writer.Format = BarcodeFormat.ITF;
            writer.Options = options;
            Bitmap bitmap = writer.Write(contents);
            string fileName = Guid.NewGuid().ToString() + ".png";
            bitmap.Save(tempPath + fileName);
            return fileName;
        }
    }
}
