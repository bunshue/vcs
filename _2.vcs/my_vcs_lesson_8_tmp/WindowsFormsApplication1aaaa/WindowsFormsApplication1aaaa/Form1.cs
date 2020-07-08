using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Net;

using System.Drawing.Imaging;   //for ImageFormat
using System.Diagnostics;       //for Process, Stopwatch

namespace WindowsFormsApplication1aaaa
{

    public partial class Form1 : Form
    {
        Graphics g;     //設定一個畫布g

        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();  //這個視窗，就是畫布
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Pen pp = new Pen(Color.Black, 8);
            pp.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(pp, 50, 400, 50, 100);
            g.DrawLine(pp, 50, 400, 350, 400);
            //畫出X軸及y軸

            pp = new Pen(Color.Blue, 6);
            //重新設定pp的線條樣式
            //pp.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //設定為圓頭

            pp.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            //g.DrawLine(pp, 50, 50, 250, 250);//只畫一條
            g.DrawLines(pp, new Point[] {//一次畫好多條
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)
        });
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
Brush bb = new SolidBrush(Color.Pink);
gg.FillEllipse(bb, 50, 50, 200, 200);
//畫個圓，顏色是bb,位置的x、y在50，大小為200*200
*/

            Brush bb = new SolidBrush(Color.Pink);
            g.FillPie(bb, 50, 50, 200, 200, 0, 90);
            //畫個Pie，顏色是Pink,位置的x、y在50，大小為200*200，角度為從0度開始，畫90度

            bb = new SolidBrush(Color.Green);
            g.FillPie(bb, 50, 50, 200, 200, 90, 135);
            //畫個Pie，顏色是Green,位置大小同上，角度為接著從90度開始，畫135度

            bb = new SolidBrush(Color.Purple);
            g.FillPie(bb, 50, 50, 200, 200, 225, 135);
            //畫個Pie，顏色是Purple,位置大小同上，角度為接著從90+135=225度開始 畫135度
            //如此，這3個pie就會合成一個圓


            bb = new SolidBrush(Color.Blue);
            g.DrawString("哭笑不得", new Font("標楷體", 24, FontStyle.Bold | FontStyle.Italic), bb, 20, 20);
            //畫字就比較簡單了，會產生一個標楷體，24的大小，粗加斜，顏色為bb，位置在(20,20)
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //一、圖片的應用，將圖片縮放

            Image ii = WindowsFormsApplication1aaaa.Properties.Resources.picture1;
            Bitmap bmp = new Bitmap(ii, ii.Width, ii.Height);   //用Bitmap直接進行縮放，比例自行調整，範例為1：1
            g.DrawImage(bmp, 50, 50);

            if (bmp != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                bmp.Save(@filename1, ImageFormat.Jpeg);
                bmp.Save(@filename2, ImageFormat.Bmp);
                bmp.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

          
            

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //二、自行繪製一張圖，並另存在硬碟上

            Bitmap bmp = new Bitmap(240, 320);
            //new出一個bitmap，大小為240*320

            Graphics g = Graphics.FromImage(bmp);
            //將Graphics g畫布 畫在bmp上

            Brush bb = new SolidBrush(Color.Pink);
            g.FillRectangle(bb, 0, 0, 240, 320);
            bb = new SolidBrush(Color.Orange);
            g.FillEllipse(bb, 20, 20, 100, 100);

            g.DrawImage(bmp, 50, 50);
            //將bmp畫在gg畫布中

            if (bmp != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                bmp.Save(@filename1, ImageFormat.Jpeg);
                bmp.Save(@filename2, ImageFormat.Bmp);
                bmp.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
            //另存

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //三、在某圖片中，在指定的位置切裁指定的大小並另存圖片
            Image ii = WindowsFormsApplication1aaaa.Properties.Resources.picture1;
            Bitmap bmp = new Bitmap(500, 500);
            Graphics g = Graphics.FromImage(bmp);
            g.DrawImage(ii, new Rectangle(0, 0, ii.Width, ii.Height), new Rectangle(0, 0, ii.Width, ii.Height), GraphicsUnit.Pixel);
            //以上是指，在ii這張圖中，以指定的大小，畫在指定的位置，量測單位是Pixel

            g.DrawImage(bmp, 0, 0);

            if (bmp != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                bmp.Save(@filename1, ImageFormat.Jpeg);
                bmp.Save(@filename2, ImageFormat.Bmp);
                bmp.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

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

        private void button9_Click(object sender, EventArgs e)
        {
            String result = "";
            foreach (DriveInfo di in DriveInfo.GetDrives())
            {
                //取得磁碟的資訊，並逐一列出
                if (di.IsReady)
                    //表示有東西，若不是可能是光碟、軟碟機
                    result += String.Format("{0}\t{1}\t{2}\t{3}\r\n", di.Name, di.DriveType, di.TotalSize, di.TotalFreeSpace);
                //印出資訊
                else
                    result += String.Format("{0}\t{1}\r\n", di.Name, di.DriveType);
            }
            richTextBox1.Text += result + "\n";


        }

        private void button10_Click(object sender, EventArgs e)
        {
            /*
            //測不出來
            File.Encrypt(@"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug\aaa.txt");
            richTextBox1.Text += "加密成功！\n";
            */

            File.Copy(@"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug\aaa.txt", @"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug\bbb.txt");
            //檔案複製，注意要確認C:\VS2012\TT.txt有檔案
            richTextBox1.Text += "複製成功！\n";


        }

        private void button11_Click(object sender, EventArgs e)
        {
            String result = "";
            foreach (String a in Directory.GetDirectories(@"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug"))
                result += "資料夾\t" + a + "\r\n";
            //取得C:\VS2012下的資料夾資訊
            foreach (String a in Directory.GetFiles(@"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug"))
                result += "檔案\t" + a + "\r\n";
            //取得C:\VS2012下的檔案資訊
            richTextBox1.Text += result + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            FileInfo fi = new FileInfo(@"C:\_git\WindowsFormsApplication1aaaa\WindowsFormsApplication1aaaa\bin\Debug\aaa.txt");
            //取得檔案資訊
            //fi.CopyTo(@"C:\練習資料夾\TT2.txt");
            //MessageBox.Show("複製成功！");

            richTextBox1.Text += fi.Length.ToString() + " Bytes";

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //列印出所有的編碼方式
            StringBuilder sb = new StringBuilder();
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                sb.Append(ei.CodePage).Append("\t")
                    .Append(ei.Name).Append("\t")
                    .Append(ei.DisplayName).Append("\r\n");
            }

            richTextBox1.Text += sb.ToString() + "\n";
        }



        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {
            Brush bb = new SolidBrush(Color.Orange);
            g.FillRectangle(bb, 70, 70, 200, 100);
            //畫出一個填滿的方框

            Pen pp = new Pen(Color.Black, 4);
            g.DrawRectangle(pp, 70, 70, 200, 100);
            //在同樣起點畫出黑色的長方型線，即實現加外框            


            Random rr = new Random();
            Brush db;
            for (int i = 1; i <= 7; i++)
            {
                db = new SolidBrush(Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256)));
                //Color.FromArgb() 可以設定3原色，這裡3原色的代碼是亂數產生的

                g.FillRectangle(db, 70 + (i * 40), 70 + (i * 40), 200, 100);
                //畫布上畫出方框，每次位置的X及Y值都加70，以實現往右下角移動
            }
        }



    }
}
