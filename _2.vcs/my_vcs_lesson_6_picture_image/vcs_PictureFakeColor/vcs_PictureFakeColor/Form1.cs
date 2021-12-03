using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureFakeColor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string filename = @"C:\______test_files\elephant.jpg";
            string filename = @"C:\______test_files\fakecolor.jpg";
            //string filename = @"C:\______test_files\ims3.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //偽彩色處理
            /*
            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            bitmap1 = gcTrans(bitmap1, true, 5);
            pictureBox2.Image = bitmap1;
            */

            string filename = @"C:\______test_files\fakecolor.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap2 = gcTrans(bitmap1, true, 255 / 10);
            pictureBox2.Image = bitmap2;
        }

        #region 偽彩色圖像處理

        /// <summary>
        /// 偽彩色圖像處理
        /// 博客園-初行 http://www.cnblogs.com/zxlovenet
        /// 日期：2014.2.14
        /// </summary>
        /// <param name="bmp">傳入的灰度圖像</param>
        /// <param name="method">使用何種方法，false強度分層法,true灰度級-彩色變換法</param>
        /// <param name="seg">強度分層中的分層數</param>
        /// <returns>返回偽彩色圖像</returns>
        private Bitmap gcTrans(Bitmap bmp, bool method, byte seg)
        {
            if (bmp != null)
            {
                if (System.Drawing.Imaging.PixelFormat.Format24bppRgb == bmp.PixelFormat)
                {
                    Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
                    System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
                    IntPtr ptr = bmpData.Scan0;
                    int bytes = bmp.Width * bmp.Height * 3;
                    byte[] grayValues = new byte[bytes];
                    System.Runtime.InteropServices.Marshal.Copy(ptr, grayValues, 0, bytes);
                    bmp.UnlockBits(bmpData);

                    byte[] rgbValues = new byte[bytes];
                    //清零
                    Array.Clear(rgbValues, 0, bytes);
                    byte tempB;

                    if (method == false)
                    {
                        //強度分層法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            byte ser = (byte)(256 / seg);
                            tempB = (byte)(grayValues[i] / ser);
                            //分配任意一種顏色
                            rgbValues[i + 1] = (byte)(tempB * ser);
                            rgbValues[i] = (byte)((seg - 1 - tempB) * ser);
                            rgbValues[i + 2] = 0;
                        }
                    }
                    else
                    {
                        //灰度級-彩色變換法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            if (grayValues[i] < 64)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = (byte)(4 * grayValues[i]);
                                rgbValues[i] = 255;
                            }
                            else if (grayValues[i] < 128)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = (byte)(-4 * grayValues[i] + 2 * 255);
                            }
                            else if (grayValues[i] < 192)
                            {
                                rgbValues[i + 2] = (byte)(4 * grayValues[i] - 2 * 255);
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = 0;
                            }
                            else
                            {
                                rgbValues[i + 2] = 255;
                                rgbValues[i + 1] = (byte)(-4 * grayValues[i] + 4 * 255);
                                rgbValues[i] = 0;
                            }
                        }

                    }
                    bmp = new Bitmap(bmp.Width, bmp.Height, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
                    bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
                    ptr = bmpData.Scan0;

                    System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);
                    bmp.UnlockBits(bmpData);

                    return bmp;
                }
                else
                {
                    return null;
                }
            }
            else
            {
                return null;
            }
        }
        #endregion
    }
}

