using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//將一圖拆成 3X2 共六圖

namespace vcs_PictureSpilit2
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
            //將一圖拆成 3X2 共六圖, 像素法

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bmpRes = null;

            try
            {
                bmpRes = new Bitmap(filename);

                //窗體上顯示加載圖片
                pictureBox0.Width = bmpRes.Width;
                pictureBox0.Height = bmpRes.Height;
                pictureBox0.Image = bmpRes;

            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show("圖片資源加載失敗！/r/n" + ex.ToString());
            }

            //裁剪圖片(裁成2行3列的6張圖片)
            int nYClipNum = 2, nXClipNum = 3;
            Bitmap[] bmpaClipBmpArr = new Bitmap[nYClipNum * nXClipNum];
            for (int nYClipNumIndex = 0; nYClipNumIndex < nYClipNum; nYClipNumIndex++)
            {
                for (int nXClipNumIndex = 0; nXClipNumIndex < nXClipNum; nXClipNumIndex++)
                {
                    int nClipWidth = bmpRes.Width / nXClipNum;
                    int nClipHight = bmpRes.Height / nYClipNum;
                    int nBmpIndex = nXClipNumIndex + nYClipNumIndex * nYClipNum + (nYClipNumIndex > 0 ? 1 : 0);
                    bmpaClipBmpArr[nBmpIndex] = new Bitmap(nClipWidth, nClipHight);

                    for (int nY = 0; nY < nClipHight; nY++)
                    {
                        for (int nX = 0; nX < nClipWidth; nX++)
                        {
                            int nClipX = nX + nClipWidth * nXClipNumIndex;
                            int nClipY = nY + nClipHight * nYClipNumIndex;
                            Color cClipPixel = bmpRes.GetPixel(nClipX, nClipY);
                            bmpaClipBmpArr[nBmpIndex].SetPixel(nX, nY, cClipPixel);
                        }
                    }
                }
            }

            PictureBox[] picbShow = new PictureBox[nYClipNum * nXClipNum];
            picbShow[0] = pictureBox1;
            picbShow[1] = pictureBox2;
            picbShow[2] = pictureBox3;
            picbShow[3] = pictureBox4;
            picbShow[4] = pictureBox5;
            picbShow[5] = pictureBox6;

            for (int nLoop = 0; nLoop < nYClipNum * nXClipNum; nLoop++)
            {
                picbShow[nLoop].Width = bmpRes.Width / nXClipNum;
                picbShow[nLoop].Height = bmpRes.Height / nYClipNum;
                picbShow[nLoop].Image = bmpaClipBmpArr[nLoop];
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //將一圖拆成 3X2 共六圖, Clone法, 運用Clone函數局部複製

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bmpRes = null;

            try
            {
                bmpRes = new Bitmap(filename);

                //窗體上顯示加載圖片
                pictureBox0.Width = bmpRes.Width;
                pictureBox0.Height = bmpRes.Height;
                pictureBox0.Image = bmpRes;

            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show("圖片資源加載失敗！/r/n" + ex.ToString());
            }

            //裁剪圖片(裁成2行3列的6張圖片)
            int nYClipNum = 2, nXClipNum = 3;
            Bitmap[] bmpaClipBmpArr = new Bitmap[nYClipNum * nXClipNum];


            //僅此不同 兩個 for 不同
            for (int nYClipNumIndex = 0; nYClipNumIndex < nYClipNum; nYClipNumIndex++)
            {
                for (int nXClipNumIndex = 0; nXClipNumIndex < nXClipNum; nXClipNumIndex++)
                {
                    int nClipWidth = bmpRes.Width / nXClipNum;
                    int nClipHight = bmpRes.Height / nYClipNum;
                    int nBmpIndex = nXClipNumIndex + nYClipNumIndex * nYClipNum + (nYClipNumIndex > 0 ? 1 : 0);
                    Rectangle rClipRect = new Rectangle(nClipWidth * nXClipNumIndex, nClipHight * nYClipNumIndex, nClipWidth, nClipHight);
                    bmpaClipBmpArr[nBmpIndex] = bmpRes.Clone(rClipRect, bmpRes.PixelFormat);
                }
            }

            PictureBox[] picbShow = new PictureBox[nYClipNum * nXClipNum];
            picbShow[0] = pictureBox1;
            picbShow[1] = pictureBox2;
            picbShow[2] = pictureBox3;
            picbShow[3] = pictureBox4;
            picbShow[4] = pictureBox5;
            picbShow[5] = pictureBox6;

            for (int nLoop = 0; nLoop < nYClipNum * nXClipNum; nLoop++)
            {
                picbShow[nLoop].Width = bmpRes.Width / nXClipNum;
                picbShow[nLoop].Height = bmpRes.Height / nYClipNum;
                picbShow[nLoop].Image = bmpaClipBmpArr[nLoop];
            }
        }
    }
}
