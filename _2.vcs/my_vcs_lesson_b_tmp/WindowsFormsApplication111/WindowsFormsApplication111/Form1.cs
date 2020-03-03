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

        private void button3_Click(object sender, EventArgs e)
        {
            //Dictionary的用法

            Dictionary<string, string> AnimalData = new Dictionary<string, string>() {
            { "mouse", "Mickey" },
            { "bull", "Benny" },
            { "tiger", "Eric" },
            { "rabbit", "Cony" }
            };
            string animal_type;
            string animal_name;

            animal_type = "mouse";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "bull";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "tiger";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "rabbit";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "dragon";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";



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

        private void button5_Click(object sender, EventArgs e)
        {
            //.Net C# 檢查 Socket Port 是否正常


        }

        private void button6_Click(object sender, EventArgs e)
        {
            //.Net C# 取得電腦名稱
            //Windows 及 LINUX 都正常

            richTextBox1.Text += "電腦名稱 1 : " + Environment.MachineName + "\n";
            richTextBox1.Text += "電腦名稱 2 : " + System.Net.Dns.GetHostName() + "\n";
            richTextBox1.Text += "電腦名稱 3 : " + System.Windows.Forms.SystemInformation.ComputerName + "\n";
            richTextBox1.Text += "電腦名稱 4 : " + System.Environment.GetEnvironmentVariable("COMPUTERNAME") + "\n";
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

        private class eraNameList
        {
            public string EraName { get; set; }
            public int Year_ST { get; set; }
            public int Year_SP { get; set; }
            public int Year_length { get; set; }
        }

        List<eraNameList> eraName = new List<eraNameList>();


        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "類似sprintf的寫法\n";
            int number = 123;
            string name = "david";
            string information = string.Empty;
            information = string.Format("ID = {0}, Name = {1}", number.ToString(), name);
            richTextBox1.Text += "information1 : " + information + "\n";
            richTextBox1.Text += "information2 : " + string.Format("ID = {0}, Name = {1}", number.ToString(), name) + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //取得上一層資料夾的名稱

            richTextBox1.Text += "原目錄 : " + Application.StartupPath + "\n";

            string str = Application.StartupPath;
            string[] split_str = new string[20];
            split_str = str.Split('\\'); //以\當分隔符號
            //richTextBox1.Text += "\n";
            //richTextBox1.Text += "共有 : " + split_str.Length.ToString() + " 個項目\n";

            richTextBox1.Text += "上一層資料夾的名稱 : " + split_str[split_str.Length - 1] + "\n";

            /*
            int i = 0;
            foreach (string tmp in split_str)
            {
                i++;
                richTextBox1.Text += i.ToString() + "\t" + tmp + "\n";
            }
            */
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Graphics buttonGraphics = button11.CreateGraphics();
            Pen myPen = new Pen(Color.ForestGreen, 4.0F);
            myPen.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;

            Rectangle theRectangle = button11.ClientRectangle;
            theRectangle.Inflate(-2, -2);
            buttonGraphics.DrawRectangle(myPen, theRectangle);
            buttonGraphics.DrawRectangle(myPen, 10, 10, button11.Width - 20, button11.Height - 20);
            buttonGraphics.Dispose();
            myPen.Dispose();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //顯示百分比
            //要using System.Globalization; //for CultureInfo
            int a = 2;
            int b = 3;
            richTextBox1.Text += "顯示一位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P1", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示兩位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示十位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P10", CultureInfo.InvariantCulture) + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            int a, b, c, d, ee, f;

            a = 123456;
            b = 2006;
            c = 3;
            d = 11;
            ee = 1234567890;
            f = 2468;

            richTextBox1.Text += "數字保留10位, 向左靠齊\n";
            richTextBox1.Text += string.Format("{0,-10}{1,-10}{2,-10}{3,-10}{4,-10}{5,-10}", a.ToString(), b.ToString(), c.ToString(), d.ToString(), ee.ToString(), f.ToString()) + "\n";
            richTextBox1.Text += "數字保留10位, 向右靠齊\n";
            richTextBox1.Text += string.Format("{0,10}{1,10}{2,10}{3,10}{4,10}{5,10}", a.ToString(), b.ToString(), c.ToString(), d.ToString(), ee.ToString(), f.ToString()) + "\n";
            richTextBox1.Text += "字串保留10位, 向左靠齊\n";
            richTextBox1.Text += string.Format("{0,-10}{1,-10}{2,-10}{3,-10}{4,-10}{5,-10}", "David", "Mary", "Doraemon", "Cat", "Dog", "Lion") + "\n";

            Random rnd = new Random();
            // Create new thread and display three random numbers.
            richTextBox1.Text += "Some currency values:\n";
            for (int ctr = 0; ctr <= 3; ctr++)
            {
                richTextBox1.Text += string.Format("{0:C2}", rnd.NextDouble() * 100) + "\n";
            }

            double aa = 123456789012345.456789;
            richTextBox1.Text += aa.ToString("N0", CultureInfo.InvariantCulture) + "\n";

            int bb = 1234567890;
            richTextBox1.Text += bb.ToString("N0", CultureInfo.InvariantCulture) + "\n";


            double used = 197594525696;

            double used2 = 184.02;

            //已使用空間 :	197,593,485,312 個位元組	184.02 GB
            richTextBox1.Text += string.Format("{0,-15}{1,20}{2,-10}{3,-10}",
                "已使用空間 :", used.ToString("N0", CultureInfo.InvariantCulture), " 個位元組", used2.ToString() + " GB") + "\n";



            //richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString("N0", CultureInfo.InvariantCulture) + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";



        }

    }
}
