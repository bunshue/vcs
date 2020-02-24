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

        private void button1_Click(object sender, EventArgs e)
        {
            //找資料夾所在的硬碟
            string path = String.Empty;

            path = "C:\\______test_files\\_case1";

            richTextBox1.Text += "\n搜尋路徑" + path + "\n";

            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX1\n\n";
                //ProcessFile(path, 0);
                //richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                richTextBox1.Text += "XXXXXXXXXXXXXXX2\n\n";

                DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                richTextBox1.Text += "Name : " + d.Name + "\n";
                richTextBox1.Text += "FullName : " + d.FullName + "\n";
                richTextBox1.Text += "Parent : " + d.Parent + "\n";
                richTextBox1.Text += "Root : " + d.Root + "\n";


                //FolederName = path;
                //ProcessDirectory(path);
                //richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";

                //show_file_info();
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
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
            richTextBox1.Text += "information : " + information + "\n";
        }

        void load_eraData()
        {
            eraName.Add(new eraNameList { EraName = "順治", Year_ST = 1644, Year_SP = 1661 });
            eraName.Add(new eraNameList { EraName = "康熙", Year_ST = 1662, Year_SP = 1722 });
            eraName.Add(new eraNameList { EraName = "雍正", Year_ST = 1723, Year_SP = 1735 });
            eraName.Add(new eraNameList { EraName = "乾隆", Year_ST = 1736, Year_SP = 1795 });
            /*
            eraName.Add(new eraNameList { EraName = "嘉慶", Year_ST = 1796, Year_SP = 1820 });
            eraName.Add(new eraNameList { EraName = "道光", Year_ST = 1821, Year_SP = 1850 });
            eraName.Add(new eraNameList { EraName = "咸豐", Year_ST = 1851, Year_SP = 1861 });
            eraName.Add(new eraNameList { EraName = "同治", Year_ST = 1862, Year_SP = 1874 });
            eraName.Add(new eraNameList { EraName = "光緒", Year_ST = 1875, Year_SP = 1908 });
            eraName.Add(new eraNameList { EraName = "宣統", Year_ST = 1909, Year_SP = 1911 });
            */
        }

        private void button9_Click(object sender, EventArgs e)
        {
            load_eraData();

            int year;
            int era_start = 0;
            int total_year = 0;
            richTextBox1.Text += "年號\t起\t迄\t年\n";
            foreach (var showlist in eraName)
            {
                if (era_start == 0)
                    era_start = showlist.Year_ST;
                year = showlist.Year_SP - showlist.Year_ST + 1;
                total_year += year;
                showlist.Year_length = year;
                richTextBox1.Text += showlist.EraName + "\t" + showlist.Year_ST.ToString() + "\t" + showlist.Year_SP.ToString() + "\t" + showlist.Year_length.ToString() + "\n";
            }
            richTextBox1.Text += "總年數 : " + total_year.ToString() + "\n";

            int W = panel1.Width;
            int H = panel1.Height;

            int ratio;
            ratio = W / total_year;

            richTextBox1.Text += "W : " + W.ToString() + "\n";
            richTextBox1.Text += "H : " + H.ToString() + "\n";
            richTextBox1.Text += "ratio : " + ratio.ToString() + "\n";

            Graphics g = panel1.CreateGraphics();
            Pen p = new Pen(Color.Red, 1);
            Font f;

            int x_st = 0;
            int y_st = 0;
            int w = 0;
            int h = 0;

            h = 50;
            y_st = 0;
            total_year = 0;

            foreach (var showlist in eraName)
            {
                year = showlist.Year_SP - showlist.Year_ST + 1;
                total_year += year;
                showlist.Year_length = year;
                //richTextBox1.Text += showlist.EraName + "\t" + showlist.Year_ST.ToString() + "\t" + showlist.Year_SP.ToString() + "\t" + showlist.Year_length.ToString() + "\n";

                x_st = (showlist.Year_ST - era_start) * ratio;
                w = year * ratio;
                p = new Pen(Color.Red, 1);
                g.DrawRectangle(p, x_st, y_st, w, h);
                richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";

                f = new Font("標楷體", 12);
                g.DrawString((total_year - year + 1).ToString(), f, new SolidBrush(Color.Blue), new PointF(x_st, y_st + h));



                string name = showlist.EraName + "(" + year.ToString() + ")";
                int font_size = 20;
                int ww = 0;
                int hh = 0;

                bool flag_font_size_ok = false;

                f = new Font("標楷體", font_size);
                while (flag_font_size_ok == false)
                {
                    ww = g.MeasureString(name, f).ToSize().Width;
                    hh = g.MeasureString(name, f).ToSize().Height;
                    if ((ww > w) || (hh > h))
                    {
                        font_size--;
                        richTextBox1.Text += "font太大, 減為" + font_size.ToString() + "\n";
                        f = new Font("標楷體", font_size);
                    }
                    else
                    {
                        flag_font_size_ok = true;
                    }
                }

                richTextBox1.Text += "ww = " + ww.ToString() + "  hh = " + hh.ToString() + "\n";

                g.DrawString(name, f, new SolidBrush(Color.Blue), new PointF(x_st + (w - ww) / 2, y_st + (h - hh) / 2));

                p = new Pen(Color.Green, 1);
                g.DrawRectangle(p, x_st + (w - ww) / 2, y_st + (h - hh) / 2, ww, hh);



            }
           



        }
    }
}
