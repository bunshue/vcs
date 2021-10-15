using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Management;

using System.Xml;

using System.IO;    //for MemoryStream

namespace WindowsFormsApplication1ccc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

            ImgReduceCutOut(200, 200, filename1, filename2);


        }

        //C# 圖片裁剪代碼，
        /// <summary>
        /// 縮小裁剪圖片
        /// </summary>
        /// <param name="int_Width">要縮小裁剪圖片寬度</param>
        /// <param name="int_Height">要縮小裁剪圖片長度</param>
        /// <param name="filename_old">要處理圖片路徑</param>
        /// <param name="filename_new">處理完畢圖片路徑</param>
        public void ImgReduceCutOut(int int_Width, int int_Height, string filename_old, string filename_new)
        {
            // ＝＝＝上傳標准圖大小＝＝＝
            int int_Standard_Width = 160;
            int int_Standard_Height = 160;

            int Reduce_Width = 0; // 縮小的寬度
            int Reduce_Height = 0; // 縮小的高度
            int CutOut_Width = 0; // 裁剪的寬度
            int CutOut_Height = 0; // 裁剪的高度
            int level = 100; //縮略圖的質量 1-100的范圍

            // ＝＝＝獲得縮小，裁剪大小＝＝＝
            if (int_Standard_Height * int_Width / int_Standard_Width > int_Height)
            {
                Reduce_Width = int_Width;
                Reduce_Height = int_Standard_Height * int_Width / int_Standard_Width;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }
            else if (int_Standard_Height * int_Width / int_Standard_Width < int_Height)
            {
                Reduce_Width = int_Standard_Width * int_Height / int_Standard_Height;
                Reduce_Height = int_Height;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }
            else
            {
                Reduce_Width = int_Width;
                Reduce_Height = int_Height;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }

            // ＝＝＝通過連接創建Image對象＝＝＝
            Image oldimage = Image.FromFile(filename_old);

            // ＝＝＝縮小圖片＝＝＝
            Image thumbnailImage = oldimage.GetThumbnailImage(Reduce_Width, Reduce_Height, new Image.GetThumbnailImageAbort(ThumbnailCallback), IntPtr.Zero);
            Bitmap bm = new Bitmap(thumbnailImage);

            // ＝＝＝處理JPG質量的函數＝＝＝
            ImageCodecInfo[] codecs = ImageCodecInfo.GetImageEncoders();
            ImageCodecInfo ici = null;
            foreach (ImageCodecInfo codec in codecs)
            {
                if (codec.MimeType == "image/jpeg")
                    ici = codec;
            }
            EncoderParameters ep = new EncoderParameters();

            //Encoder myEncoder = Encoder.Quality;

            // Create an Encoder object based on the GUID  
            // for the Quality parameter category.  
            System.Drawing.Imaging.Encoder myEncoder = System.Drawing.Imaging.Encoder.Quality;

            ep.Param[0] = new EncoderParameter(myEncoder, (long)level);

            //bm.Save(Server.MapPath("2.jpg"), ici, ep);

            // ＝＝＝裁剪圖片＝＝＝
            Rectangle cloneRect = new Rectangle(0, 0, CutOut_Width, CutOut_Height);
            PixelFormat format = bm.PixelFormat;
            Bitmap cloneBitmap = bm.Clone(cloneRect, format);

            // ＝＝＝保存圖片＝＝＝
            cloneBitmap.Save(filename_new, ici, ep);
        }

        public bool ThumbnailCallback()
        {
            return true;
        }

        private void GetThumbnail(PaintEventArgs e)
        {
            Image.GetThumbnailImageAbort callback =
                new Image.GetThumbnailImageAbort(ThumbnailCallback);
            Image image = new Bitmap(@"c:\dddddddddd\FakePhoto.jpg");
            Image pThumbnail = image.GetThumbnailImage(100, 100, callback, new
               IntPtr());
            e.Graphics.DrawImage(
               pThumbnail,
               10,
               10,
               pThumbnail.Width,
               pThumbnail.Height);
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            FailCount = 0;
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188493.html";
            string result = GetHtml(url);
            richTextBox1.Text += result + "\n";
        }

        //C#下載網頁HTML源碼，
        private static int FailCount = 0; //記錄下載失敗的次數

        public static string GetHtml(string url) //傳入要下載的網址
        {
            string str = string.Empty;
            try
            {
                System.Net.WebRequest request = System.Net.WebRequest.Create(url);
                request.Timeout = 10000; //下載超時時間
                request.Headers.Set("Pragma", "no-cache");
                System.Net.WebResponse response = request.GetResponse();
                System.IO.Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("gb2312");//utf-8 網頁文字編碼
                System.IO.StreamReader streamReader = new System.IO.StreamReader(streamReceive, encoding);
                str = streamReader.ReadToEnd();
                streamReader.Close();
            }
            catch (Exception ex)
            {
                FailCount++;

                if (FailCount > 5)
                {
                    var result = System.Windows.Forms.MessageBox.Show("已下載失敗" + FailCount + "次，是否要繼續嘗試？" + Environment.NewLine + ex.ToString(), "數據下載異常", System.Windows.Forms.MessageBoxButtons.YesNo, System.Windows.Forms.MessageBoxIcon.Error);
                    if (result == System.Windows.Forms.DialogResult.Yes)
                    {
                        str = GetHtml(url);
                    }
                    else
                    {
                        System.Windows.Forms.MessageBox.Show("下載HTML失敗" + Environment.NewLine + ex.ToString(), "下載HTML失敗", System.Windows.Forms.MessageBoxButtons.OK, System.Windows.Forms.MessageBoxIcon.Error);
                        throw ex;
                    }
                }
                else
                {
                    str = GetHtml(url);
                }
            }

            FailCount = 0; //如果能執行到這一步就表示下載終於成功了
            return str;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = "aaaaa.xml";

            // XmlTextWriter 寫文件
            XmlTextWriter writeXml = new XmlTextWriter(filename, Encoding.UTF8);
            writeXml.WriteStartDocument(false);
            writeXml.WriteStartElement("NetWork");  //根結點
            writeXml.WriteComment("網絡配置信息");    //註解

            writeXml.WriteStartElement("configration");

            writeXml.WriteElementString("IpAddress", "192.168.2.168");
            writeXml.WriteElementString("Netmask", "255.255.255.0");
            writeXml.WriteElementString("Gateway", "202.103.24.68");

            writeXml.WriteEndElement();
            writeXml.WriteEndElement();

            writeXml.Flush();
            writeXml.Close();




        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = "aaaaa.xml";

            // XmlTextReader 讀文件
            XmlTextReader readerXml = new XmlTextReader(filename);
            while (readerXml.Read())
            {
                if (readerXml.NodeType == XmlNodeType.Element)
                {

                    if (readerXml.Name == "IpAddress")
                    {
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Netmask")
                    {
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Gateway")
                    {
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                }
            }

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //QR write

        }




        private void button6_Click(object sender, EventArgs e)
        {
            //QR read


        }




    }
}

