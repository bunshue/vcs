using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Net;   //for WebClient
using System.Net.Sockets;   //for Socket

using System.Diagnostics;   //for Stopwatch

using System.Drawing.Imaging;   //for BitmapData

using System.Runtime.InteropServices;   //for Marshal

using Microsoft.VisualBasic;    //C# 利用 VisualBasic 簡體 繁體 大小寫 轉換

using System.Globalization; //for CultureInfo

namespace WindowsFormsApplication111
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        //偵測原始檔案類型
        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            //openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                string builtHex = string.Empty;
                using (Stream S = File.OpenRead(openFileDialog1.FileName))
                {
                    for (int i = 0; i < 8; i++)
                    {
                        builtHex += S.ReadByte().ToString("X2");

                        /*
                        if (ImageTypes.ContainsKey(builtHex))
                        {
                            string 真實副檔名 = ImageTypes[builtHex];
                            break;
                        }
                        */
                    }
                    richTextBox1.Text += "get " + builtHex + "\n";


                }

                //richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

        }


        public class MyWebClient : WebClient
        {
            protected override WebRequest GetWebRequest(Uri uri)
            {
                WebRequest WR = base.GetWebRequest(uri);
                WR.Timeout = 30 * 1000;     //30秒
                return WR;
            }
        }

        //.Net C# 讓 WebClient 擁有 Timeout 功能
        private void button4_Click(object sender, EventArgs e)
        {
            MyWebClient MWC = new MyWebClient();
            string HTML = MWC.DownloadString("http://www.google.com.tw/");
            richTextBox1.Text += HTML;
            //Console.WriteLine(HTML);

        }

        static bool Check(string IPStr, int Port, int Timeout)
        {
            bool success = false;
            try
            {
                using (Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
                    success = socket.BeginConnect(IPAddress.Parse(IPStr), Port, null, null).AsyncWaitHandle.WaitOne(Timeout, true);
            }
            catch { }
            return success;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //C# 將 BitmapData 複製到 byte[] Array 陣列
            //以下有兩種方法複製 BitmapData，一個是使用 unsafe 方法，一個一個 byte 複製，另外一個是複製記憶體區塊，較為快速。
            //目前測試為，第二種方法比第一種方法快四倍。

            // Create a Bitmap object from a file.
            using (Bitmap bmp = new Bitmap(@"C:/______test_files/IMG_20200219_172550.bmp"))
            {
                int W;
                int H;
                W = bmp.Width;
                H = bmp.Height;

                int w;
                int h;
                int dataIndex = 0;

                BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
                Stopwatch sw = new Stopwatch();
                sw.Start();
                for (int xx = 0; xx < 1000; xx++)   //做一千次 為了量測時間
                {
                    //一個一個byte複製
                    w = bmpData.Width;
                    h = bmpData.Height;
                    dataIndex = 0;
                    byte[] data = new byte[w * h * 3];
                    unsafe
                    {
                        byte* p = (byte*)bmpData.Scan0.ToPointer();
                        for (int y = 0; y < h; y++)
                        {
                            for (int x = 0; x < w; x++)
                            {
                                data[dataIndex++] = p[0];
                                data[dataIndex++] = p[1];
                                data[dataIndex++] = p[2];
                                p += 3;
                            }
                        }
                    }
                }
                sw.Stop();
                richTextBox1.Text += "Time1: " + (sw.ElapsedMilliseconds / 1000).ToString() + "." + (sw.ElapsedMilliseconds % 1000).ToString("D3") + " 秒\n";
                sw.Reset();
                sw.Start();
                for (int xx = 0; xx < 1000; xx++)   //做一千次 為了量測時間
                {
                    byte[] data = new byte[bmpData.Width * bmpData.Height * 3];
                    Marshal.Copy(bmpData.Scan0, data, 0, data.Length); //複製記憶體區塊
                }
                sw.Stop();
                richTextBox1.Text += "Time2: " + (sw.ElapsedMilliseconds / 1000).ToString() + "." + (sw.ElapsedMilliseconds % 1000).ToString("D3") + " 秒\n";
                bmp.UnlockBits(bmpData);

                BitmapData bmpData2 = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);

                //一個一個byte複製
                w = bmpData2.Width;
                h = bmpData2.Height;
                dataIndex = 0;
                byte[] data2 = new byte[w * h * 4];
                unsafe
                {
                    byte* p = (byte*)bmpData2.Scan0.ToPointer();
                    for (int y = 0; y < h; y++)
                    {
                        for (int x = 0; x < w; x++)
                        {
                            data2[dataIndex++] = p[0];
                            data2[dataIndex++] = p[1];
                            data2[dataIndex++] = p[2];
                            data2[dataIndex++] = 0xFF;
                            p += 3;
                        }
                    }
                }
                bmp.UnlockBits(bmpData2);

                int i;
                int j;
                int k;

                richTextBox1.Text += "W = " + w.ToString() + "\n";
                richTextBox1.Text += "H = " + h.ToString() + "\n";
                richTextBox1.Text += "len = " + data2.Length.ToString() + "\n";

                k = 3;
                richTextBox1.Text += (k * 16).ToString("X8") + "h: ";
                richTextBox1.Text += "00 00 00 00 00 00 ";
                for (i = 0; i < (w * h / 10); i++)
                {
                    j = i + 6;
                    richTextBox1.Text += data2[i].ToString("X2");
                    if ((j % 16) == 15)
                    {
                        richTextBox1.Text += "\n";
                        k++;
                        richTextBox1.Text += (k * 16).ToString("X8") + "h: ";
                    }
                    else
                    {
                        richTextBox1.Text += " ";
                    }
                }




            }

        }

        //偵測原始檔案類型

        //應改用binary read

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "偵測原始檔案類型";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            //openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "檔案 : " + openFileDialog1.FileName + "\n";
                //richTextBox1.Text += "長度 : " + openFileDialog1.FileName.Length.ToString() + "\n";

                int len = openFileDialog1.FileName.Length;

                if (len < 10)
                {
                    richTextBox1.Text += "檔案太小, 忽略";
                    return;
                }


                len = 10;
                int[] data = new int[len];

                string builtHex = string.Empty;
                using (Stream S = File.OpenRead(openFileDialog1.FileName))
                {
                    for (int i = 0; i < 10; i++)
                    {
                        data[i] = S.ReadByte();
                        builtHex += data[i].ToString("X2") + " ";

                        /*
                        if (ImageTypes.ContainsKey(builtHex))
                        {
                            string 真實副檔名 = ImageTypes[builtHex];
                            break;
                        }
                        */
                    }
                    richTextBox1.Text += "data : " + builtHex + "\n";
                    if ((data[0] == 0x89) && (data[1] == 'P') && (data[2] == 'N') && (data[3] == 'G'))
                    {
                        richTextBox1.Text += "PNG 檔案\n";
                    }
                    else if ((data[6] == 'J') && (data[7] == 'F') && (data[8] == 'I') && (data[9] == 'F'))
                    {
                        richTextBox1.Text += "JPG 檔案\n";
                    }
                    else if ((data[0] == 'G') && (data[1] == 'I') && (data[2] == 'F') && (data[9] == '8') && (data[9] == '9'))
                    {
                        richTextBox1.Text += "GIF 檔案\n";
                    }
                    else if ((data[0] == 'B') && (data[1] == 'M'))
                    {
                        richTextBox1.Text += "BMP 檔案\n";
                    }
                    else if ((data[0] == 0xFF) && (data[1] == 0xFE))
                    {
                        richTextBox1.Text += " 純文字Unicode 檔案\n";
                    }
                    else if ((data[0] == 'I') && (data[1] == 'D') && (data[2] == '3'))
                    {
                        richTextBox1.Text += "MP3 檔案\n";
                    }
                    else
                    {
                        richTextBox1.Text += "其他 檔案\n";
                    }


                }

            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }

        }




    }
}
