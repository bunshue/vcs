using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using ZXing.Common;
using ZXing;

namespace EX30
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 【生成一维码】
        private void Create1DBtn_Click(object sender, EventArgs e)
        {
            // 1.设置条形码规格
            EncodingOptions encodeOption = new EncodingOptions();
            encodeOption.Height = 130; // 必须制定高度、宽度
            encodeOption.Width = 240;

            // 2.生成条形码图片并保存
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Options = encodeOption;
            wr.Format = BarcodeFormat.EAN_13; //  条形码规格：EAN13规格：12（无校验位）或13位数字
            Bitmap img = wr.Write(this.ContentTxt.Text); // 生成图片
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\EAN_13-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 3.读取保存的图片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }

        // 【生成二维码】
        private void Create2DBtn_Click(object sender, EventArgs e)
        {
            // 1.设置QR二维码的规格
            ZXing.QrCode.QrCodeEncodingOptions qrEncodeOption = new ZXing.QrCode.QrCodeEncodingOptions();
            qrEncodeOption.CharacterSet = "UTF-8"; // 设置编码格式，否则读取'中文'乱码
            qrEncodeOption.Height = 200;
            qrEncodeOption.Width = 200;
            qrEncodeOption.Margin = 1; // 设置周围空白边距

            // 2.生成条形码图片并保存
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Format = BarcodeFormat.QR_CODE; // 二维码
            wr.Options = qrEncodeOption;
            Bitmap img = wr.Write(this.ContentTxt.Text);
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\QR-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 3.读取保存的图片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }

        // 【读取一维码】
        private void Read1DBtn_Click(object sender, EventArgs e)
        {
            // 1.设置读取条形码规格
            DecodingOptions decodeOption = new DecodingOptions();
            decodeOption.PossibleFormats = new List<BarcodeFormat>() { 
               BarcodeFormat.EAN_13,
            };

            // 2.进行读取操作
            ZXing.BarcodeReader br = new BarcodeReader();
            br.Options = decodeOption;
            ZXing.Result rs = br.Decode(this.barCodeImg.Image as Bitmap);
            if (rs == null)
            {
                this.ContentTxt.Text = "读取失败";
                MessageBox.Show("读取失败");
            }
            else
            {
                this.ContentTxt.Text = rs.Text;
                MessageBox.Show("读取成功，内容：" + rs.Text);
            }
        }

        // 【读取二维码】
        private void Read2DBtn_Click(object sender, EventArgs e)
        {
            // 1.设置读取条形码规格
            DecodingOptions decodeOption = new DecodingOptions();
            decodeOption.PossibleFormats = new List<BarcodeFormat>() { 
               BarcodeFormat.QR_CODE,
           };

            // 2.进行读取操作
            ZXing.BarcodeReader br = new BarcodeReader();
            br.Options = decodeOption;
            ZXing.Result rs = br.Decode(this.barCodeImg.Image as Bitmap);
            if (rs == null)
            {
                this.ContentTxt.Text = "读取失败";
                MessageBox.Show("读取失败");
            }
            else
            {
                this.ContentTxt.Text = rs.Text;
                MessageBox.Show("读取成功，内容：" + rs.Text);
            }
        }

        // 【打开图片】
        private void OpenImgBtn_Click(object sender, EventArgs e)
        {
            OpenFileDialog fileDialog = new OpenFileDialog();
            fileDialog.InitialDirectory = System.AppDomain.CurrentDomain.BaseDirectory;
            fileDialog.Filter = "图形文件(*.jpg)|*.jpg";
            if (fileDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                string filePath = fileDialog.FileName;
                this.barCodeImg.Image = Bitmap.FromFile(filePath);
            }
        }

        private void Creat2DOfHaveLogoBtn_Click(object sender, EventArgs e)
        {
            // 1.设置QR二维码的规格
            ZXing.QrCode.QrCodeEncodingOptions qrEncodeOption = new ZXing.QrCode.QrCodeEncodingOptions();
            qrEncodeOption.CharacterSet = "UTF-8"; // 设置编码格式，否则读取'中文'乱码
            qrEncodeOption.Height = 200;
            qrEncodeOption.Width = 200;
            qrEncodeOption.Margin = 1; // 设置周围空白边距

            // 2.生成条形码图片
            ZXing.BarcodeWriter wr = new BarcodeWriter();
            wr.Format = BarcodeFormat.QR_CODE; // 二维码
            wr.Options = qrEncodeOption;
            Bitmap img = wr.Write(this.ContentTxt.Text);

            // 3.在二维码的Bitmap对象上绘制logo图片
            Bitmap logoImg = Bitmap.FromFile(System.AppDomain.CurrentDomain.BaseDirectory + "\\logo.jpg") as Bitmap;
            Graphics g = Graphics.FromImage(img);
            Rectangle logoRec = new Rectangle(); // 设置logo图片的大小和绘制位置
            logoRec.Width = img.Width / 6;
            logoRec.Height = img.Height / 6;
            logoRec.X = img.Width / 2 - logoRec.Width / 2; // 中心点
            logoRec.Y = img.Height / 2 - logoRec.Height / 2;
            g.DrawImage(logoImg, logoRec);

            // 4.保存绘制后的图片
            string filePath = System.AppDomain.CurrentDomain.BaseDirectory + "\\QR-" + this.ContentTxt.Text + ".jpg";
            img.Save(filePath, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 5.读取保存的图片
            this.ImgPathTxt.Text = filePath;
            this.barCodeImg.Image = img;
            MessageBox.Show("保存成功：" + filePath);
        }

    }
}
