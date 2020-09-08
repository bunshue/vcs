using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;                        //for StreamReader
using System.Diagnostics;               //for process, FileVersionInfo, Stopwatch
using System.Drawing.Imaging;   //for bmp2jpg
using System.Net;           //for WebClient
using System.Reflection;    //for Assembly
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_test_all_99_tmp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            toolTip1.SetToolTip(button26, "顯示提示訊息");
       }

        private void button3_Click(object sender, EventArgs e)
        {
        }


        private void button4_Click(object sender, EventArgs e)
        {
            //偵測原始檔案類型
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

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //偵測原始檔案類型
        //應改用binary read
        private void button7_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {

            //只撈一層的所有檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_files"))
            {
                richTextBox1.Text += fname + "\n";
            }

        }

        private void button17_Click(object sender, EventArgs e)
        {
            //只撈一層的所有.txt檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_files", "*.txt"))
            {
                richTextBox1.Text += fname + "\n";
            }

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
             //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(@"C:\______test_files", "*.*", System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
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

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入toolTip物件\n";
            richTextBox1.Text += "在Form1()的InitializeComponent()後加入訊息\n";
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }


        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void richTextBox1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Up：" + e.X + " : " + e.Y;

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Down：" + e.X + " : " + e.Y;
        }

        private void button34_Click_1(object sender, EventArgs e)
        {
        }

        private void button35_Click_1(object sender, EventArgs e)
        {

        }

        private void button23_Click_1(object sender, EventArgs e)
        {

        }

        private void button32_Click_1(object sender, EventArgs e)
        {

        }

        private void button21_Click_1(object sender, EventArgs e)
        {
            var pathstr = "C://______test_files";
            if (Directory.Exists(pathstr))
            {
                //var strname=DateTime.Now.ToShortDateString().Replace("/","-")+".txt";
                var dt = DateTime.Now;
                DirectoryInfo pathinfo = new DirectoryInfo(pathstr);
                foreach (DirectoryInfo paths in pathinfo.GetDirectories())
                {
                    if (paths.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                    {
                        //paths.Delete();
                        richTextBox1.Text += "path = " + paths + "\n";
                    }
                }
            }
            else
                richTextBox1.Text += "資料夾 " + pathstr + " 不存在\n";
        }

        private void button40_Click(object sender, EventArgs e)
        {


        }

        private void button39_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo("c:\\______test_files");
            if (!dir.Exists)
            {
                dir = new DirectoryInfo("c:\\______test_files");
            }
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += "get file : " + file.Name + "\n";
            }

        }


        private void button11_Click_1(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //C# 將 BitmapData 複製到 byte[] Array 陣列
            //以下有兩種方法複製 BitmapData，一個是使用 unsafe 方法，一個一個 byte 複製，另外一個是複製記憶體區塊，較為快速。
            //目前測試為，第二種方法比第一種方法快四倍。

            // Create a Bitmap object from a file.
            using (Bitmap bmp = new Bitmap(@"C:/______test_files/test_ReadAllBytes.bmp"))
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


        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int cnt = 0;

            DirectoryInfo dir = new DirectoryInfo("c:\\______test_files");
            richTextBox1.Text += "搜尋子目錄內的所有檔案, 子目錄 : " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            cnt = 0;
            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
            }

            FileInfo[] aaaa = dir.GetFiles();
            cnt = 0;
            richTextBox1.Text += "子目錄 " + dir.Name + " 下的檔案 :\n";
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
            }
            richTextBox1.Text += "\n";
        }


    }
}
