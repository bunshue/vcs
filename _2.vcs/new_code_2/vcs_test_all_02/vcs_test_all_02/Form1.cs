using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat
using System.Diagnostics;       //for Process, Stopwatch
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_test_all_02
{

    public partial class Form1 : Form
    {
        Graphics g;     //設定一個畫布g

        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();  //這個視窗，就是畫布, 直接畫在Form上
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //轉移中
                                //三、在某圖片中，在指定的位置切裁指定的大小並另存圖片
            Image ii = vcs_test_all_02.Properties.Resources.picture1;
                                Bitmap bmp = new Bitmap(500, 500);
                                Graphics g = Graphics.FromImage(bmp);
                                g.DrawImage(ii, new Rectangle(0, 0, ii.Width, ii.Height), new Rectangle(0, 0, ii.Width, ii.Height), GraphicsUnit.Pixel);
                                //以上是指，在ii這張圖中，以指定的大小，畫在指定的位置，量測單位是Pixel

                                g.DrawImage(bmp, 0, 0);


        }


        private const int MODE1 = 0x01;
        private const int MODE2 = 0x02;

        void copy_file(int mode)
        {
            richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";
            //取得檔案資訊
            string filename = "G:\\191128-1008.mp4";
            long filesize = 0;

            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == true)      //確認檔案是否存在
            {
                //richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                //richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                filesize = fi.Length;
                //richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                //richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                //richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;

                Stopwatch stopwatch = new Stopwatch();

                // Begin timing
                stopwatch.Start();

                FileStream sourceFile = new FileStream(filename, FileMode.Open, FileAccess.Read);
                //sourceFile 來源檔要先在該路徑中準備好

                FileStream targetFile = new FileStream(@"G:\tmp.mp4", FileMode.Create, FileAccess.Write);

                if (mode == MODE1)
                {
                    int bb = -1;
                    while ((bb = sourceFile.ReadByte()) != -1)
                    {
                        //一次1 byte的讀
                        targetFile.WriteByte((byte)bb);
                    }
                }
                else
                {

                    int count = -1;
                    byte[] bb = new byte[10240];
                    while ((count = sourceFile.Read(bb, 0, bb.Length)) > 0)
                    {
                        //一次讀10240個byte，相當於10k，效率較佳
                        targetFile.Write(bb, 0, bb.Length);
                    }
                }
                sourceFile.Close();
                targetFile.Close();


                // Stop timing
                stopwatch.Stop();
                richTextBox1.Text += "檔案大小: " + (filesize / 1024 / 1024).ToString() + " MB\n";
                richTextBox1.Text += "複製完畢！ 耗時: " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                richTextBox1.Text += "速率: " + (filesize / 1024 / 1024 / stopwatch.Elapsed.TotalSeconds).ToString() + " MB/sec\n";


            }
            else
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";


            richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            copy_file(MODE1);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            copy_file(MODE2);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "cancel\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            /*
            //測不出來
            File.Encrypt(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\aaa.txt");
            richTextBox1.Text += "加密成功！\n";
            */

            File.Copy(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\aaa.txt", @"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\bbb.txt");
            //檔案複製，注意要確認C:\VS2012\TT.txt有檔案
            richTextBox1.Text += "複製成功！\n";


        }

        private void button11_Click(object sender, EventArgs e)
        {
            String result = "";
            foreach (String a in Directory.GetDirectories(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug"))
                result += "資料夾\t" + a + "\r\n";
            //取得C:\VS2012下的資料夾資訊
            foreach (String a in Directory.GetFiles(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug"))
                result += "檔案\t" + a + "\r\n";
            //取得C:\VS2012下的檔案資訊
            richTextBox1.Text += result + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            FileInfo fi = new FileInfo(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\aaa.txt");
            //取得檔案資訊
            //fi.CopyTo(@"C:\練習資料夾\TT2.txt");
            //MessageBox.Show("複製成功！");

            richTextBox1.Text += fi.Length.ToString() + " Bytes";

        }

        //長檔名轉短檔名
        [DllImport("Kernel32.dll")]//声明API函数
        private static extern Int16 GetShortPathName(string lpszLongPath, StringBuilder lpszShortPath, Int16 cchBuffer);

        private void button1_Click(object sender, EventArgs e)
        {
            string filename_long = @"C:\______test_files\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";
            StringBuilder filename_short = new System.Text.StringBuilder(256);//创建StringBuilder对象
            GetShortPathName(filename_long, filename_short, 256);//调用API函数转换成短文件名
            richTextBox1.Text += "長檔名：" + filename_long + "\n";
            richTextBox1.Text += "短檔名：" + filename_short + "\n";
        }
    }
}
