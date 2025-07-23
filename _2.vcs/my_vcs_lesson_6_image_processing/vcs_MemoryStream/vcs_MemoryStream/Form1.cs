/*

//圖片檔案 => Image => MemoryStream(ms) => 拜列
//拜列 => MemoryStream(ms) => Image => 圖片檔案
// bmp/png 資料長度 4*W*H + 檔頭54拜
// jpg     資料長度 3*W*H + 檔頭54拜

*/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for MemoryStream
using System.Drawing.Imaging;   //for BitmapData, ImageLockMode, PixelFormat
using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;   //for Stopwatch

namespace vcs_MemoryStream
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_map_city/global.c.gif";   //超大圖, 要很久
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Stopwatch sw = new Stopwatch();

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            pictureBox1.Image = Image.FromFile(filename);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 140;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            bt_restore.Location = new Point(x_st + dx * 8, y_st + dy * 0);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(640, 480);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 480 + 10);
            pictureBox2.Size = new Size(640, 480);

            richTextBox1.Size = new Size(700, 900);
            richTextBox1.Location = new Point(x_st + dx * 8 + 80, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Name = "bt_exit";
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_restore_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //MemoryStream 1
            //部分code
            richTextBox1.Text += "使用byte[]數據，生成Bitmap\n";

            //使用byte[]數據，生成Bitmap

            int W = 512;
            int H = 512;

            //建立 byte[] Array 一維陣列
            int byte_data_len = W * H;
            byte[] byte_data = new byte[byte_data_len];

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    byte_data[j * H + i] = (byte)((i + j) % 256);
                }
            }

            //指定8位格式，即256色
            Bitmap bmp = new Bitmap(W, H, PixelFormat.Format8bppIndexed);

            //將該位圖存入內存中
            MemoryStream ms = new MemoryStream();
            bmp.Save(ms, ImageFormat.Bmp);
            ms.Flush();

            //最終生成的位圖數據大小
            //int bmpDataSize = ((W * 8 + 31) / 32 * 4) * H;
            int bmpDataSize = 512 * 512;
            //數據部分相對文件開始偏移，具體可以參考位圖文件格式

            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整
            //建立 byte[] Array 一維陣列
            byte[] byte_data_new = new byte[bmpDataSize];

            ms.Write(byte_data_new, 0, bmpDataSize);
            ms.Flush();

            //將內存中的位圖寫入Bitmap對象
            bmp = new Bitmap(ms);
            pictureBox1.Image = bmp;


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //MemoryStream 2
            richTextBox1.Text += "圖片 轉 拜列\n";

            //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
            Image image = Image.FromFile(filename);

            //方法一
            MemoryStream ms = new MemoryStream();
            Bitmap bmp = new Bitmap(image);
            bmp.Save(ms, ImageFormat.Bmp);//將圖像以指定的格式存入緩存內存流

            int byte_data_len = (int)ms.Length;
            richTextBox1.Text += "取得 MemoryStream 長度 : " + byte_data_len.ToString() + "\t多了檔頭54拜\n";

            byte[] byte_data = new byte[byte_data_len];
            ms.Position = 0;//設置留的初始位置
            ms.Read(byte_data, 0, byte_data_len);

            /*
            //方法二
            MemoryStream ms = new MemoryStream();
            image.Save(ms, image.RawFormat);
            Byte[] byte_data = ms.ToArray();
            */

            /*
            //方法三
            Image image = new Bitmap(filename);
            MemoryStream ms = new MemoryStream();
            image.Save(ms, ImageFormat.Bmp);
            int byte_data_len = (int)ms.Length;
            richTextBox1.Text += "取得 MemoryStream 長度 : " + byte_data_len.ToString() + "\t多了檔頭54拜\n";
            byte[] byte_data = ms.GetBuffer();
            */

            int i;
            for (i = 54; i < (54 + 256 * 2); i++)
            {
                richTextBox1.Text += byte_data[i].ToString("D03");
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            for (i = 54; i < (54 + 256 * 2); i++)
            {
                byte_data[i] = 255;

            }
            for (i = 54; i < (54 + 256 * 2); i++)
            {
                richTextBox1.Text += byte_data[i].ToString("D03");
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            //拜列轉Image

            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整
            //建立 byte[] Array 一維陣列
            byte[] byte_data_new = new byte[byte_data_len];

            ms.Write(byte_data_new, 0, byte_data_len);
            ms.Flush();

            //將內存中的位圖寫入Bitmap對象
            bmp = new Bitmap(ms);
            pictureBox1.Image = bmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片 拜列 MemoryStream Bitmap轉換

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            richTextBox1.Text += "圖檔 轉 Bitmap\n";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            richTextBox1.Text += "Bitmap 轉 MemoryStream\n";
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);

            richTextBox1.Text += "MemoryStream 轉 拜列\n";
            byte[] pic_array1 = ms.ToArray();


            richTextBox1.Text += "建立空白 Bitmap\n";
            bitmap1 = new Bitmap(100, 100);

            richTextBox1.Text += "對此Bitmap畫圖\n";
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Bmp);
            byte[] pic_array2 = ms.ToArray();

            richTextBox1.Text += "len = " + pic_array2.Length.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //格式轉換
            //Stream 和 byte[] 之間的轉換

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            // 打開文件
            FileStream fileStream = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.Read);

            // 讀取文件的 byte[]
            byte[] bytes1 = new byte[fileStream.Length];
            fileStream.Read(bytes1, 0, bytes1.Length);
            fileStream.Close();

            // 把 byte[] 轉換成 Stream
            Stream stream = new MemoryStream(bytes1);

            // 將 Stream 轉成 byte[]
            byte[] bytes2 = new byte[stream.Length];
            stream.Read(bytes2, 0, bytes2.Length);
            // 設置當前流的位置為流的開始
            stream.Seek(0, SeekOrigin.Begin);

            // 將 byte[] 轉成 Stream
            Stream stream2 = new MemoryStream(bytes2);


            //將 Stream 寫入文件
            // 把 Stream 轉換成 byte[]
            byte[] bytes3 = new byte[stream.Length];
            stream.Read(bytes3, 0, bytes3.Length);
            // 設置當前流的位置為流的開始
            stream.Seek(0, SeekOrigin.Begin);

            // 把 byte[] 寫入文件
            FileStream fs = new FileStream("tmp_aaaaaa.jpg", FileMode.Create);
            BinaryWriter bw = new BinaryWriter(fs);
            bw.Write(bytes3);
            bw.Close();
            fs.Close();

            //二進制轉換成圖片

            MemoryStream ms = new MemoryStream(bytes3);
            ms.Position = 0;

            //MemoryStream轉Image
            Image img = Image.FromStream(ms);

            ms.Close();

            pictureBox1.Image = img;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
            Bitmap bmp = new Bitmap(filename);

            // 輸出圖片
            MemoryStream ms = new MemoryStream();
            bmp.Save(ms, ImageFormat.Jpeg);
            ms.Close();

            richTextBox1.Text += "done\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X10.bmp";

            Image image = Image.FromFile(filename);
            MemoryStream ms = new MemoryStream();
            image.Save(ms, ImageFormat.Bmp);

            var cc = ms.ToArray();
            richTextBox1.Text += "len = " + cc.Length.ToString() + "\n";

            /*
            //全部資料以HEX表示出來
            StringBuilder sb = new StringBuilder();
            foreach (byte b in ms.ToArray())
            {
                sb.AppendFormat("{0:X2}", b);
            }
            string all_data = sb.ToString();
            richTextBox1.Text += all_data + "\n";
            */

            // bmp/png 資料長度 4*256*10 + 檔頭54 = 10294 拜
            // jpg     資料長度 3*256*10 + 檔頭54 =  7734 拜

            //建立 byte[] Array 一維陣列
            byte[] byte_data = ms.GetBuffer();
            richTextBox1.Text += "len = " + byte_data.Length.ToString() + "\n";

            //對 byte_data 做處理, 反相
            int i;
            for (i = 54; i < byte_data.Length; i++)
            {
                if ((i % 4) == 2)//B
                    byte_data[i] = (byte)(255 - byte_data[i]);
                else if ((i % 4) == 3)//G
                    byte_data[i] = (byte)(255 - byte_data[i]);
                else if ((i % 4) == 0)//R
                    byte_data[i] = (byte)(255 - byte_data[i]);
            }

            MemoryStream ms2 = new MemoryStream();
            ms2.Write(byte_data, 0, byte_data.Length);

            //MemoryStream轉Image
            Image image2 = Image.FromStream(ms2);

            pictureBox1.Image = image2;

            image2.Save("tmp_test.bmp");
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }
    }
}



/*
    

                            Bitmap bm = BytesToImage((byte[])reader.GetValue(6));


        // Convert a byte array into an image.
        private Bitmap BytesToImage(byte[] bytes)
        {
            using (MemoryStream image_stream = new MemoryStream(bytes))
            {
                Bitmap bm = new Bitmap(image_stream);
                return bm;
            }
        }


                MemoryStream image_stream = new MemoryStream(wc.DownloadData(url));
                return Image.FromStream(image_stream);


            string imgURL = @"https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes("aaaaaaa.jpg", ms.ToArray());


            string imgURL = domain + imgBaseURL + fileName[0] + "?.&uf=ssr&zoom=2";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes(string.Format(@"Download\{0}.jpg", fileName[1]), ms.ToArray());


            Image image = barcode.Encode(TYPE.CODE128B, Code);
            using (MemoryStream ms = new MemoryStream())
            {
                image.Save(ms, ImageFormat.Jpeg);

                image.Save("lion.jpg", ImageFormat.Jpeg);

                pictureBox4.Image = image;

                //Response.ClearContent();
                //Response.ContentType = "image/png";
                //Response.BinaryWrite(ms.ToArray());
            }


            Image img = barcode.Encode(TYPE.CODE128B, Code);
            using (MemoryStream ms = new MemoryStream())
            {
                img.Save(ms, ImageFormat.Jpeg);
                img.Save("lion.jpg", ImageFormat.Jpeg);
                //Response.ClearContent();
                //Response.ContentType = "image/png";
                //Response.BinaryWrite(ms.ToArray());
            }


            Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();

            //讀取要解碼的圖片
            FileStream fs = new FileStream(filename, FileMode.Open);
            Byte[] data = new Byte[fs.Length];
            // 把檔案讀取到位元組陣列
            fs.Read(data, 0, data.Length);
            fs.Close();

            // 實例化一個記憶體資料流 MemoryStream，將位元組陣列放入
            MemoryStream ms = new MemoryStream(data);
            // 將記憶體資料流的資料放到 BitMap的物件中
            bitmap = (Bitmap)Image.FromStream(ms);

            //pictureBox2.Image = bitmap;       //將圖片顯示於 PictureBox 中





*/