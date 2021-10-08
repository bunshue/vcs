using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_PictureThumbnail2
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
            //圖片縮為 100 X 100
            richTextBox1.Text += "建立縮圖\t圖片縮為 100 X 100\n";
            string filename = @"C:\______test_files\picture1.jpg";
            int w = 100;
            int h = 100;
            int flag = 100;
            GetPicThumbnail(filename, w, h, flag);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片縮為 一半 X 一半
            richTextBox1.Text += "建立縮圖\t圖片縮為 一半 X 一半\n";
            string filename = @"C:\______test_files\picture1.jpg";

            //讀圖片檔案至記憶體
            //read image
            Bitmap bitmap1 = new Bitmap(filename);

            int w = bitmap1.Width / 2;
            int h = bitmap1.Height / 2;
            int flag = 100;
            GetPicThumbnail(filename, w, h, flag);
        }

        /// <summary>
        /// 根據指定尺寸得到按比例縮放的尺寸,返回true表示已更改尺寸
        /// </summary>
        /// <param name="picWidth">圖片寬度</param>
        /// <param name="picHeight">圖片高度</param>
        /// <param name="specifiedWidth">指定寬度</param>
        /// /// <param name="specifiedHeight">指定高度</param>
        /// <returns>返回true表示以更改尺寸</returns>
        private bool GetPicZoomSize(ref int picWidth, ref int picHeight, int specifiedWidth, int specifiedHeight)
        {
            int sW = 0, sH = 0;
            Boolean isZoomSize = false;
            //按比例縮放
            Size tem_size = new Size(picWidth, picHeight);
            if (tem_size.Width > specifiedWidth || tem_size.Height > specifiedHeight) //將**改成c#中的或者操作符號
            {
                if ((tem_size.Width * specifiedHeight) > (tem_size.Height * specifiedWidth))
                {
                    sW = specifiedWidth;
                    sH = (specifiedWidth * tem_size.Height) / tem_size.Width;
                }
                else
                {
                    sH = specifiedHeight;
                    sW = (tem_size.Width * specifiedHeight) / tem_size.Height;
                }
                isZoomSize = true;
            }
            else
            {
                sW = tem_size.Width;
                sH = tem_size.Height;
            }
            picHeight = sH;
            picWidth = sW;
            return isZoomSize;
        }
        /// <summary>
        /// 無損壓縮圖片
        /// </summary>
        /// <param name="sFile">原圖片</param>
        /// <param name="dWidth">寬度</param>
        /// <param name="dHeight">高度</param>
        /// <param name="flag">壓縮質量 1-100</param>
        /// <returns></returns>

        public bool GetPicThumbnail(string sFile, int dWidth, int dHeight, int flag)
        {
            System.Drawing.Image iSource = System.Drawing.Image.FromFile(sFile);
            ImageFormat tFormat = iSource.RawFormat;
            int sW = iSource.Width, sH = iSource.Height;

            GetPicZoomSize(ref sW, ref sH, dWidth, dHeight);

            Bitmap ob = new Bitmap(dWidth, dHeight);
            Graphics g = Graphics.FromImage(ob);
            g.Clear(Color.WhiteSmoke);
            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.DrawImage(iSource, new Rectangle((dWidth - sW) / 2, (dHeight - sH) / 2, sW, sH), 0, 0, iSource.Width, iSource.Height, GraphicsUnit.Pixel);
            g.Dispose();
            //以下代碼為保存圖片時，設置壓縮質量
            EncoderParameters ep = new EncoderParameters();
            long[] qy = new long[1];
            qy[0] = flag;//設置壓縮的比例1-100
            EncoderParameter eParam = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, qy);
            ep.Param[0] = eParam;
            try
            {
                ImageCodecInfo[] arrayICI = ImageCodecInfo.GetImageEncoders();

                ImageCodecInfo jpegICIinfo = null;

                for (int x = 0; x < arrayICI.Length; x++)
                {
                    if (arrayICI[x].FormatDescription.Equals("JPEG"))
                    {
                        jpegICIinfo = arrayICI[x];
                        break;
                    }
                }

                if (jpegICIinfo != null)
                {
                    string filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    //richTextBox1.Text += "save file " + dFile + "\n";
                    ob.Save(filename, jpegICIinfo, ep);
                    //ob.Save(@file1, ImageFormat.Jpeg);
                }
                else
                {
                    string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                    //ob.Save(dFile, tFormat);
                    ob.Save(filename, tFormat);
                }
                return true;
            }
            catch
            {
                return false;
            }
            finally
            {
                iSource.Dispose();
                ob.Dispose();
            }
        }
    }
}
