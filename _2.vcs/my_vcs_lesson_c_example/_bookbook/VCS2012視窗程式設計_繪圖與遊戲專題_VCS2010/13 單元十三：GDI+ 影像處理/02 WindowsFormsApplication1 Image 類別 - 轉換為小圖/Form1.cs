using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Image img; // Image 影像
        Image imgThumbnail; // Image 影像 小圖
        public Form1()
        {
            InitializeComponent();
        }

        // 開啟檔案按鈕
        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)  // 開啟影像檔
            {
                String input = openFileDialog1.FileName;
                img = Image.FromFile(input); // 產生一個Image物件

                // 呈現 影像 的寬高資訊
                label1.Text = "(" + img.Width.ToString() + ", " + img.Height.ToString() + ")";
                this.Invalidate(); // 要求重畫
            }
        }

        // 轉換成小圖 按鈕
        private void button2_Click(object sender, EventArgs e)
        {
            //img.RotateFlip(RotateFlipType.Rotate90FlipNone); // 影像旋轉90度
            imgThumbnail = img.GetThumbnailImage(50, (int)(50 * img.Height / img.Width), null, (IntPtr)0);
            this.Invalidate(); // 要求重畫
        }

        // 儲存檔案按鈕
        private void button3_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK) // 儲存影像檔
            {
                String output = saveFileDialog1.FileName;
                imgThumbnail.Save(output, System.Drawing.Imaging.ImageFormat.Png); // .Png 格式
            }
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (img != null)  // 呈現 Image 影像
                e.Graphics.DrawImage(img, 10, 100, img.Width, img.Height);

            if (imgThumbnail != null) // 呈現 Image 影像 小圖
                e.Graphics.DrawImage(imgThumbnail, 200, 10, imgThumbnail.Width, imgThumbnail.Height);
        }
    }
}