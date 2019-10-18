using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_QR_code
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            System.Drawing.Bitmap bitmap = null;
            //要轉成QRCode 的內容
            string content = richTextBox1.Text;
            if (content.Length == 0)
            {
                richTextBox1.Text += "無資料，無法做QR code";
                return;
            }

            //QRCode的設定
            ZXing.BarcodeWriter writer = new ZXing.BarcodeWriter
            {
                Format = ZXing.BarcodeFormat.QR_CODE,
                Options = new ZXing.QrCode.QrCodeEncodingOptions
                {
                    //產生出圖片的高度
                    Height = 280,
                    //產生出圖片的寬度
                    Width = 280,
                    //文字是使用哪種編碼方式
                    CharacterSet = "UTF-8",

                    //錯誤修正容量
                    //L水平    7%的字碼可被修正
                    //M水平    15%的字碼可被修正
                    //Q水平    25%的字碼可被修正
                    //H水平    30%的字碼可被修正
                    ErrorCorrection = ZXing.QrCode.Internal.ErrorCorrectionLevel.H
                }
            };
            //將要編碼的文字產生出QRCode的圖檔
            bitmap = writer.Write(content);
            //儲存圖片
            bitmap.Save(@"C:\______test_files\temp.png", System.Drawing.Imaging.ImageFormat.Png);
            bitmap.Save(@"C:\______test_files\temp.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
            //顯示在畫面中
            pictureBox1.Image = bitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Drawing.Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();

            //讀取要解碼的圖片
            FileStream fs = new FileStream(@"C:\______test_files\temp.png", FileMode.Open);
            Byte[] data = new Byte[fs.Length];
            // 把檔案讀取到位元組陣列
            fs.Read(data, 0, data.Length);
            fs.Close();
            // 實例化一個記憶體資料流 MemoryStream，將位元組陣列放入
            MemoryStream ms = new MemoryStream(data);
            // 將記憶體資料流的資料放到 BitMap的物件中
            bitmap = (Bitmap)Image.FromStream(ms);

            //將圖片顯示於 PictureBox 中
            pictureBox2.Image = bitmap;
            //進行解碼的動作
            ZXing.Result result = reader.Decode(bitmap);

            if (result != null)
            {   //如果有成功解讀，則顯示文字
                richTextBox2.Text = result.Text;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
        }
    }
}
