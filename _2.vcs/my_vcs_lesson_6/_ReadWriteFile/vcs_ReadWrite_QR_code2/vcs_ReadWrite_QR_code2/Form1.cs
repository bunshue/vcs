using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

namespace vcs_ReadWrite_QR_code2
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
            System.Drawing.Bitmap bitmap = null;
            //要轉成QRCode 的內容
            string content = textBox1.Text;
            //QRCode的設定
            ZXing.BarcodeWriter writer = new ZXing.BarcodeWriter
            {
                Format = ZXing.BarcodeFormat.QR_CODE,
                Options = new ZXing.QrCode.QrCodeEncodingOptions
                {
                    //產生出圖片的高度
                    Height = 180,
                    //產生出圖片的寬度
                    Width = 180,
                    //文字是使用哪種編碼方式
                    CharacterSet = "UTF-8",

                    //錯誤修正容量
                    //L水平	7%的字碼可被修正
                    //M水平	15%的字碼可被修正
                    //Q水平	25%的字碼可被修正
                    //H水平	30%的字碼可被修正
                    ErrorCorrection = ZXing.QrCode.Internal.ErrorCorrectionLevel.H

                }
            };
            //將要編碼的文字產生出QRCode的圖檔
            bitmap = writer.Write(content);
            //儲存圖片
            string filename = Application.StartupPath + "\\qr_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
            bitmap.Save(filename, System.Drawing.Imaging.ImageFormat.Png);
            //顯示在畫面中
            pictureBox1.Image = bitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Drawing.Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();
            // bitmap = (System.Drawing.Bitmap)System.Drawing.Bitmap.FromFile(@"D:\Test\QRCode\temp.png");

            //讀取要解碼的圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_qr_code\vcs_ReadWrite_QR_code.png";
            FileStream fs = new FileStream(filename, FileMode.Open);
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
                label1.Text = result.Text;
            }
        }
    }
}
