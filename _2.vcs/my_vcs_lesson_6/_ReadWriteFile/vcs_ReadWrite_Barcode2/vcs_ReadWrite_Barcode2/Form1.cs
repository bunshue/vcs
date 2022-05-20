using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using ZXing;
using ZXing.Common;

namespace vcs_ReadWrite_Barcode2
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

        // 【生成一維碼】
        private void Create1DBtn_Click(object sender, EventArgs e)
        {
            // 1.設置條形碼規格
            EncodingOptions encodeOption = new EncodingOptions();
            encodeOption.Height = 130; // 必須制定高度、寬度
            encodeOption.Width = 240;

            // 2.生成條形碼圖片并保存
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Options = encodeOption;
            wr.Format = BarcodeFormat.EAN_13; //  條形碼規格：EAN13規格：12（無校驗位）或13位數字
            Bitmap img = wr.Write(this.ContentTxt.Text); // 生成圖片
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\EAN_13-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 3.讀取保存的圖片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }

        // 【生成二維碼】
        private void Create2DBtn_Click(object sender, EventArgs e)
        {
            // 1.設置QR二維碼的規格
            ZXing.QrCode.QrCodeEncodingOptions qrEncodeOption = new ZXing.QrCode.QrCodeEncodingOptions();
            qrEncodeOption.CharacterSet = "UTF-8"; // 設置編碼格式，否則讀取'中文'亂碼
            qrEncodeOption.Height = 200;
            qrEncodeOption.Width = 200;
            qrEncodeOption.Margin = 1; // 設置周圍空白邊距

            // 2.生成條形碼圖片并保存
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Format = BarcodeFormat.QR_CODE; // 二維碼
            wr.Options = qrEncodeOption;
            Bitmap img = wr.Write(this.ContentTxt.Text);
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\QR-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 3.讀取保存的圖片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }

        // 【讀取一維碼】
        private void Read1DBtn_Click(object sender, EventArgs e)
        {
            // 1.設置讀取條形碼規格
            DecodingOptions decodeOption = new DecodingOptions();
            decodeOption.PossibleFormats = new List<BarcodeFormat>() { 
               BarcodeFormat.EAN_13,
            };

            // 2.進行讀取操作
            ZXing.BarcodeReader br = new BarcodeReader();
            br.Options = decodeOption;
            ZXing.Result rs = br.Decode(this.barCodeImg.Image as Bitmap);
            if (rs == null)
            {
                this.ContentTxt.Text = "讀取失敗";
                MessageBox.Show("讀取失敗");
            }
            else
            {
                this.ContentTxt.Text = rs.Text;
                MessageBox.Show("讀取成功，內容：" + rs.Text);
            }
        }

        // 【讀取二維碼】
        private void Read2DBtn_Click(object sender, EventArgs e)
        {
            // 1.設置讀取條形碼規格
            DecodingOptions decodeOption = new DecodingOptions();
            decodeOption.PossibleFormats = new List<BarcodeFormat>() { 
               BarcodeFormat.QR_CODE,
           };

            // 2.進行讀取操作
            ZXing.BarcodeReader br = new BarcodeReader();
            br.Options = decodeOption;
            ZXing.Result rs = br.Decode(this.barCodeImg.Image as Bitmap);
            if (rs == null)
            {
                this.ContentTxt.Text = "讀取失敗";
                MessageBox.Show("讀取失敗");
            }
            else
            {
                this.ContentTxt.Text = rs.Text;
                MessageBox.Show("讀取成功，內容：" + rs.Text);
            }
        }

        // 【打開圖片】
        private void OpenImgBtn_Click(object sender, EventArgs e)
        {
            OpenFileDialog fileDialog = new OpenFileDialog();
            fileDialog.InitialDirectory = System.AppDomain.CurrentDomain.BaseDirectory;
            fileDialog.Filter = "圖形文件(*.jpg)|*.jpg";
            if (fileDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                string filePath = fileDialog.FileName;
                this.barCodeImg.Image = Bitmap.FromFile(filePath);
            }
        }

        private void Creat2DOfHaveLogoBtn_Click(object sender, EventArgs e)
        {
            // 1.設置QR二維碼的規格
            ZXing.QrCode.QrCodeEncodingOptions qrEncodeOption = new ZXing.QrCode.QrCodeEncodingOptions();
            qrEncodeOption.CharacterSet = "UTF-8"; // 設置編碼格式，否則讀取'中文'亂碼
            qrEncodeOption.Height = 200;
            qrEncodeOption.Width = 200;
            qrEncodeOption.Margin = 1; // 設置周圍空白邊距

            // 2.生成條形碼圖片
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Format = BarcodeFormat.QR_CODE; // 二維碼
            wr.Options = qrEncodeOption;
            Bitmap img = wr.Write(this.ContentTxt.Text);

            // 3.在二維碼的Bitmap對象上繪制logo圖片
            Bitmap logoImg = Bitmap.FromFile("../../logo.jpg") as Bitmap;
            Graphics g = Graphics.FromImage(img);
            Rectangle logoRec = new Rectangle(); // 設置logo圖片的大小和繪制位置
            logoRec.Width = img.Width / 6;
            logoRec.Height = img.Height / 6;
            logoRec.X = img.Width / 2 - logoRec.Width / 2; // 中心點
            logoRec.Y = img.Height / 2 - logoRec.Height / 2;
            g.DrawImage(logoImg, logoRec);

            // 4.保存繪制后的圖片
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\QR-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 5.讀取保存的圖片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }
    }
}


