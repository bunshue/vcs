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
using System.Collections;
using System.Drawing.Text;
using System.Drawing.Imaging;   //for ColorAdjustType
using System.Drawing.Drawing2D;
using System.Management;
using System.Reflection;    //for Assembly
using System.Security;
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Media;     //for SoundPlayer
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Globalization; //for CultureInfo
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Xml;
using System.Xml.Linq;

using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False

namespace vcs_Mix00
{
    public partial class Form1 : Form
    {
        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            show_item_location();
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
            dx = 170 + 10;
            dy = 70 + 10;

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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox1.Size = new Size(820, 520);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            webBrowser1.Size = new Size(640, 240);
            webBrowser1.Location = new Point(x_st + dx * 3, y_st + dy * 6 + 70);

            richTextBox1.Location = new Point(x_st + dx * 7 + 120, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            byte[] bytSendData = new byte[5];

            //協議不支持
            bytSendData[0] = 0x12;
            bytSendData[1] = 0x34;
            bytSendData[2] = 0x56;

            UInt16 intCRC16 = GetCheckCode(bytSendData, 3);
            bytSendData[3] = (byte)(intCRC16 & 0xFF);   //CRC校驗低位
            bytSendData[4] = (byte)((intCRC16 >> 8) & 0xff);                //CRC校驗高位

            //發送數據
            //serial.Write(bytSendData, 0, 5);



            //byte bytRtuDataFlag = 0;
            //byte bytRtuDataIdx;
            byte[] bytRtuData = new byte[8];

            int i;
            for (i = 0; i < 8; i++)
            {
                bytRtuData[i] = (byte)i;

            }
            //信息處理
            intCRC16 = GetCheckCode(bytRtuData, 8 - 2);

            //Debug.Print("CRC:" + bytRtuData[8 - 2].ToString() + " " + ((byte)(intCRC16 & 0xFF)).ToString() +"|" + bytRtuData[8 - 1].ToString() + " " + ((byte)((intCRC16 >> 8) & 0xff)).ToString());

            string result = "CRC:" + bytRtuData[8 - 2].ToString() + " " + ((byte)(intCRC16 & 0xFF)).ToString() + "|" + bytRtuData[8 - 1].ToString() + " " + ((byte)((intCRC16 >> 8) & 0xff)).ToString();

            richTextBox1.Text += result + "\n";


            //bytSendData[3 + lngDataNum * 2] = (byte)(intCRC16 & 0xFF);                    //CRC校驗低位
            //bytSendData[4 + lngDataNum * 2] = (byte)((intCRC16 >> 8) & 0xff);             //CRC校驗高位                  


            //intCRC16 = GetCheckCode(bytSendData, 3);
            //bytSendData[3] = (byte)(intCRC16 & 0xFF); &nbsp;               //CRC校驗低位
            //bytSendData[4] = (byte)((intCRC16 >> 8) & 0xff);                //CRC校驗高位



            //CRC16校驗檢驗
            //if (bytRtuData[8 - 2] == (intCRC16 & 0xFF) && bytRtuData[8 - 1] == ((intCRC16 >> 8) & 0xff))





        }

        //CRC16校驗
        private UInt16 GetCheckCode(byte[] buf, int nEnd)
        {
            UInt16 crc = (UInt16)0xffff;
            int i, j;
            for (i = 0; i < nEnd; i++)
            {
                crc ^= (UInt16)buf[i];
                for (j = 0; j < 8; j++)
                {
                    if ((crc & 1) != 0)
                    {
                        crc >>= 1;
                        crc ^= 0xA001;
                    }
                    else
                        crc >>= 1;
                }
            }
            return crc;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //拷貝檔案, 限定拷貝大小
            //拷貝檔案, 每次拷貝1024拜


            string filename1 = @"C:\______test_files\picture1.jpg";

            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            CopyFile(filename1, filename2, 1024);

        }


        FileStream FormerOpen;
        FileStream ToFileOpen;
        /// <summary>
        /// 文件的複製
        /// </summary>
        /// <param FormerFile="string">源文件路徑</param>
        /// <param toFile="string">目的文件路徑</param> 
        /// <param SectSize="int">傳輸大小</param> 
        /// <param progressBar="ProgressBar">ProgressBar控制元件</param> 
        public void CopyFile(string FormerFile, string toFile, int SectSize)
        {
            FileStream fileToCreate = new FileStream(toFile, FileMode.Create);		//建立目的文件，如果已存在將被覆蓋
            fileToCreate.Close();										//關閉所有資源
            fileToCreate.Dispose();										//釋放所有資源
            FormerOpen = new FileStream(FormerFile, FileMode.Open, FileAccess.Read);//以只讀方式打開源文件
            ToFileOpen = new FileStream(toFile, FileMode.Append, FileAccess.Write);	//以寫方式打開目的文件
            //根據一次傳輸的大小，計算傳輸的個數
            int FileSize;												//要拷貝的文件的大小
            //如果分段拷貝，即每次拷貝內容小於文件總長度
            if (SectSize < FormerOpen.Length)
            {
                byte[] buffer = new byte[SectSize];							//根據傳輸的大小，定義一個字節數組
                int copied = 0;										//記錄傳輸的大小
                while (copied <= ((int)FormerOpen.Length - SectSize))			//拷貝主體部分
                {
                    FileSize = FormerOpen.Read(buffer, 0, SectSize);			//從0開始讀，每次最大讀SectSize
                    FormerOpen.Flush();								//清空快取
                    ToFileOpen.Write(buffer, 0, SectSize);					//向目的文件寫入字節
                    ToFileOpen.Flush();									//清空快取
                    ToFileOpen.Position = FormerOpen.Position;				//使源文件和目的文件流的位置相同
                    copied += FileSize;									//記錄已拷貝的大小
                }
                int left = (int)FormerOpen.Length - copied;						//取得剩餘大小
                FileSize = FormerOpen.Read(buffer, 0, left);					//讀取剩餘的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, left);							//寫入剩餘的部分
                ToFileOpen.Flush();									//清空快取
            }
            //如果整體拷貝，即每次拷貝內容大於文件總長度
            else
            {
                byte[] buffer = new byte[FormerOpen.Length];				//取得文件的大小
                FormerOpen.Read(buffer, 0, (int)FormerOpen.Length);			//讀取源文件的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, (int)FormerOpen.Length);			//寫放字節
                ToFileOpen.Flush();									//清空快取
            }
            FormerOpen.Close();										//釋放所有資源
            ToFileOpen.Close();										//釋放所有資源
            richTextBox1.Text += "文件複製完成\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //動態驗證碼變成靜態
            //將一個gif拆成多圖

            string filename1 = @"C:\______test_files\__pic\_gif\run.gif";

            Image image1 = Image.FromFile(filename1);
            FrameDimension frameDimension = new FrameDimension(image1.FrameDimensionsList[0]);
            int frameCount = image1.GetFrameCount(frameDimension);
            richTextBox1.Text += "frameCount = " + frameCount.ToString() + "\n";

            int W = image1.Width;
            int H = image1.Height;
            Bitmap bitmap1 = new Bitmap(W, H);

            //將一個gif拆成多圖
            for (int i = 0; i < frameCount; i++)
            {
                image1.SelectActiveFrame(frameDimension, i);
                Bitmap bmp = new Bitmap(image1);
                string fname = "gif_fileA" + i.ToString() + ".bmp";
                bmp.Save(fname, ImageFormat.Bmp);
            }

            //把多圖疊合起來
            for (int i = 0; i < frameCount; i++)
            {
                image1.SelectActiveFrame(frameDimension, i);
                Bitmap bmp = new Bitmap(image1);

                Color dd = bmp.GetPixel(1, 1);
                if (i == 0) //設定基底
                {
                    for (int x = 0; x < bmp.Width; x++)
                    {
                        for (int y = 0; y < bmp.Height; y++)
                        {
                            bitmap1.SetPixel(x, y, dd);
                        }
                    }
                }
                for (int x = 0; x < bmp.Width; x++)
                {
                    for (int y = 0; y < bmp.Height; y++)
                    {
                        Color c = bmp.GetPixel(x, y);
                        if (c == dd)
                        {
                            continue;
                        }
                        bitmap1.SetPixel(x, y, c);
                    }
                }
            }

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //兩圖檔疊合

            string filename1 = @"C:\______test_files\__pic\_MU\id_card_03.jpg";
            string filename2 = @"C:\______test_files\__pic\_MU\id_card_01.jpg";

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename2);	//Image.FromFile出來的是Image格式

            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "W1 = " + bitmap1.Width.ToString() + ", H1 = " + bitmap1.Height.ToString() + "\n";
            richTextBox1.Text += "W2 = " + bitmap2.Width.ToString() + ", H2 = " + bitmap2.Height.ToString() + "\n";

            Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format24bppRgb);
            //Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);

            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
            //g.DrawImage(bitmap2, 200, 0, bitmap2.Width, bitmap2.Height);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W;
            int h = H;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            int i;
            int j;
            Color c1;
            Color c2;
            Color c;
            float alpha = 0.5f;
            for (alpha = 0; alpha <= 1; alpha += 0.03f)
            {
                richTextBox1.Text += "alpha = " + alpha.ToString() + "\n";
                for (j = 0; j < h; j++)
                {
                    for (i = 0; i < w; i++)
                    {
                        c1 = bitmap1.GetPixel(i, j);
                        c2 = bitmap2.GetPixel(i, j);
                        c = Color.FromArgb(
                            (int)(c1.A * alpha + c2.A * (1 - alpha)),
                            (int)(c1.R * alpha + c2.R * (1 - alpha)),
                            (int)(c1.G * alpha + c2.G * (1 - alpha)),
                            (int)(c1.B * alpha + c2.B * (1 - alpha))
                            );
                        bmp.SetPixel(i, j, c);
                    }

                }
                pictureBox1.Image = bmp;
                Application.DoEvents();
                System.Threading.Thread.Sleep(100);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //給圖片添加版權信息

            //創建一張位圖
            Bitmap bitmap = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height, System.Drawing.Imaging.PixelFormat.Format24bppRgb);

            //根據位圖獲取畫布
            Graphics g = Graphics.FromImage(bitmap);

            //清空畫布並用透明色填充
            g.Clear(Color.Transparent);


            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            //將另一幅圖片畫到畫布上
            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            //寫版權信息到圖片上。
            g.DrawString("群曜醫電", new Font("黑體", 15), new SolidBrush(Color.Red), new Rectangle(20, 20, 100, 100));

            //顯示
            this.pictureBox1.Image = bitmap;

            //保存圖片
            bitmap.Save("abc.bmp",System.Drawing.Imaging.ImageFormat.Bmp);
        }


        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //Image Cut

            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            string mesg = "lion-mouse";

            Cut(filename1, filename2, 200, 200, mesg);
        }

        /// <summary>
        /// 圖像切割
        /// </summary>
        /// <param name="filename1">原圖片路徑</param>
        /// <param name="filename2">切割後圖片路徑</param>
        /// <param name="width">切割後圖像寬度</param>
        /// <param name="height">切割後圖像高度</param>
        public void Cut(string filename1, string filename2, int width, int height, string message)
        {
            Bitmap bitmap = new Bitmap(filename1);
            Decimal MaxRow = Math.Ceiling((Decimal)bitmap.Height / height);
            Decimal MaxColumn = Math.Ceiling((decimal)bitmap.Width / width);
            for (decimal i = 0; i < MaxRow; i++)
            {
                for (decimal j = 0; j < MaxColumn; j++)
                {
                    Bitmap bitmap1 = new Bitmap(width, height);
                    for (int offsetX = 0; offsetX < width; offsetX++)
                    {
                        for (int offsetY = 0; offsetY < height; offsetY++)
                        {
                            if (((j * width + offsetX) < bitmap.Width) && ((i * height + offsetY) < bitmap.Height))
                            {
                                bitmap1.SetPixel(offsetX, offsetY, bitmap.GetPixel((int)(j * width + offsetX), (int)(i * height + offsetY)));
                            }
                        }
                    }
                    Graphics g = Graphics.FromImage(bitmap1);
                    g.DrawString(message, new Font("黑體", 20), new SolidBrush(Color.FromArgb(70, Color.WhiteSmoke)), 0, 0);//加水印

                    try
                    {
                        //bitmap1.Save(@file1, ImageFormat.Jpeg);
                        bitmap1.Save(filename2, ImageFormat.Bmp);
                        //bitmap1.Save(@file3, ImageFormat.Png);

                        //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                        //richTextBox1.Text += "已存檔 : " + filename + "\n";
                        //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //擷取部分圖片貼上

            
            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                {
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);
                }
                bitmap.Save("test.jpg", ImageFormat.Jpeg);

            }

        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            // 創建兩個大小為 8 的點陣列
            BitArray ba1 = new BitArray(8);
            BitArray ba2 = new BitArray(8);

            byte[] a = { 0xAA };
            byte[] b = { 0x55 };

            // 把值 60 和 13 存儲到點陣列中
            ba1 = new BitArray(a);
            ba2 = new BitArray(b);

            // ba1 的內容
            richTextBox1.Text += "Bit array ba1 : " + ba1.ToString() + "\n";
            for (int i = (ba1.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba1[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            // ba2 的內容
            richTextBox1.Text += "Bit array ba2 : " + ba2.ToString() + "\n";
            for (int i = (ba2.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba2[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            BitArray ba3 = new BitArray(8);

            ba3 = ba1.And(ba2);
            // ba3 的內容
            richTextBox1.Text += "Bit array ba3 after AND : " + ba3.ToString() + "\n";
            for (int i = (ba3.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba3[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            ba3 = new BitArray(8);
            ba3 = ba1.Or(ba2);
            // ba3 的內容
            richTextBox1.Text += "Bit array ba3 after OR : " + ba3.ToString() + "\n";
            for (int i = (ba3.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba3[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //局部圖像放大
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            int r = 20;
            int ratio = 2;
            try
            {
                //局部圖像放大
                Cursor.Current = myCursor;								//定義鼠標
                Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
                //聲明兩個Rectangle對象，分別用來指定要放大的區域和放大后的區域
                Rectangle sourceRectangle = new Rectangle(e.X - r, e.Y - r, r * 2, r * 2);	//要放大的區域 
                Rectangle destRectangle = new Rectangle(e.X - r * ratio, e.Y - r * ratio, r * 2 * ratio, r * 2 * ratio);
                //調用DrawImage方法對選定區域進行重新繪制，以放大該部分
                g.DrawImage(bitmap1, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch { }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //撈出所有圖片檔 並存成一個List
            string foldername = @"C:\______test_files\__pic";

            filenames.Clear();
            GetAllFiles(foldername);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        richTextBox1.Text += "短檔名: " + shortname + "\n";
                        richTextBox1.Text += "前檔名: " + forename + "\n";
                        //filenames.Add(fullname);
                    }
                }
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Point p1 = new Point(100, 100);
            Point p2 = new Point(300, 300);
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawLine(Pens.Red, p1, p2);

            richTextBox1.Text += "在pictureBox1上的座標\n";
            richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
            richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

            richTextBox1.Text += "在表單上的座標\n";
            Point p1a = this.PointToScreen(p1);
            Point p2a = this.PointToScreen(p2);
            richTextBox1.Text += "p1a : " + p1a.ToString() + "\n";
            richTextBox1.Text += "p2a : " + p2a.ToString() + "\n";

            richTextBox1.Text += "在視窗上的座標\n";
            Point p1b = this.pictureBox1.PointToScreen(p1);
            Point p2b = this.pictureBox1.PointToScreen(p2);
            richTextBox1.Text += "p1b : " + p1b.ToString() + "\n";
            richTextBox1.Text += "p2b : " + p2b.ToString() + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //.net表達式計算器

            double pi = Math.PI;

            //string expr = "3*5*8/7";
            //string expr = "sin(3.14159/2)";

            NEval neval = new NEval();

            for (int i = 0; i <= 180; i += 10)
            {
                string expr = "sin(" + (pi * i / 180).ToString() + ")";
                double result = neval.Eval(expr);
                richTextBox1.Text += "sin(" + i.ToString() + ") = " + result.ToString() + "\n";
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //實現全屏截圖
        }

        public static void Snap(int x, int y, int width, int height)
        {
            try
            {
                //這段代碼也可以實現截圖
                //Image image = new Bitmap(width, height);
                //Graphics g = Graphics.FromImage(image);
                //g.CopyFromScreen(x, y, 0, 0, new System.Drawing.Size(width, height));
                //string hour = DateTime.Now.Minute.ToString();
                //string second = DateTime.Now.Second.ToString();
                //image.Save(ScreenshotPath + "\\" + hour + "_" + second + ".jpg");

                Bitmap image = new Bitmap(640, 480);
                using (Graphics g = Graphics.FromImage(image))
                {
                    g.CopyFromScreen(0, 0, 0, 0, image.Size);
                    g.Dispose();
                    string hour = DateTime.Now.Minute.ToString();
                    string second = DateTime.Now.Second.ToString();
                    image.Save("aaa.jpg");
                }
            }
            catch
            {
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        public void StatisticsWords(string path)
        {
            if (!File.Exists(path))
            {
                Console.WriteLine("文件不存在！");
                return;
            }
            Hashtable ht = new Hashtable(StringComparer.OrdinalIgnoreCase);
            StreamReader sr = new StreamReader(path, System.Text.Encoding.UTF8);
            string line = sr.ReadLine();

            string[] wordArr = null;
            int num = 0;
            while (line.Length > 0)
            {
                //   MatchCollection mc =  Regex.Matches(line, @"\b[a-z]+", RegexOptions.Compiled | RegexOptions.IgnoreCase);
                //foreach (Match m in mc)
                //{
                //    if (ht.ContainsKey(m.Value))
                //    {
                //        num = Convert.ToInt32(ht[m.Value]) + 1;
                //        ht[m.Value] = num;
                //    }
                //    else
                //    {
                //        ht.Add(m.Value, 1);
                //    }
                //}
                //line = sr.ReadLine();

                wordArr = line.Split(' ');
                foreach (string s in wordArr)
                {
                    if (s.Length == 0)
                        continue;
                    //去除標點
                    line = Regex.Replace(line, @"[\p{P}*]", "", RegexOptions.Compiled);
                    //將單詞加入哈希表
                    if (ht.ContainsKey(s))
                    {
                        num = Convert.ToInt32(ht[s]) + 1;
                        ht[s] = num;
                    }
                    else
                    {
                        ht.Add(s, 1);
                    }
                }
                line = sr.ReadLine();
            }

            ArrayList keysList = new ArrayList(ht.Keys);
            //對Hashtable中的Keys按字母序排列
            keysList.Sort();
            //按次數進行插入排序【穩定排序】，所以相同次數的單詞依舊是字母序
            string tmp = String.Empty;
            int valueTmp = 0;
            for (int i = 1; i < keysList.Count; i++)
            {
                tmp = keysList[i].ToString();
                valueTmp = (int)ht[keysList[i]];//次數
                int j = i;
                while (j > 0 && valueTmp > (int)ht[keysList[j - 1]])
                {
                    keysList[j] = keysList[j - 1];
                    j--;
                }
                keysList[j] = tmp;//j=0
            }
            //打印出來
            foreach (object item in keysList)
            {
                //Console.WriteLine((string)item + ":" + (string)ht[item]);
                Console.WriteLine(item.ToString() + ":" + ht[item].ToString());
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //統計英文文本中的單詞數並排序
            string filename = @"C:\______test_files\__RW\_txt\english_text.txt";
            StatisticsWords(filename);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //谷歌百度以圖搜圖 感知哈希算法
            //感知哈希算法 獲取圖片的Hashcode

            string filename = string.Empty;
            string result = string.Empty;

            filename = @"C:\______test_files\picture1.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"C:\______test_files\elephant.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"C:\______test_files\picture1.bmp";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";


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

        public class Student
        {
            public long Id { get; set; }
            public string Name { get; set; }
            public short Age { get; set; }
            public DateTime DateOfCreation { get; set; }
            public bool? IsActive { get; set; }
        }

        public class Teacher
        {
            public long Id { get; set; }
            public string Name { get; set; }
            public Nullable<int> DepartmentId { get; set; }
        }


        public class Data
        {
            public static List<Student> GetStudents()
            {
                var list = new List<Student>
        {
            new Student {Id = 1, Name = "Smith", Age = 18, DateOfCreation = DateTime.Now, IsActive = true},
            new Student {Id = 2, Name = "Hook", Age = 16, DateOfCreation = DateTime.Now.AddDays(-1), IsActive = true},
            new Student {Id = 3, Name = "Jhon", Age = 15, DateOfCreation = DateTime.Now.AddDays(-2), IsActive = true},
            new Student {Id = 4, Name = "Alan", Age = 21, DateOfCreation = DateTime.Now.AddDays(-3), IsActive = true}
        };
                return list;
            }

            public static List<Teacher> GetTeachers()
            {
                var list = new List<Teacher>
        {
            new Teacher {Id = 1, Name = "Smith", DepartmentId = 18 },
            new Teacher {Id = 2, Name = "Hook", DepartmentId = 16 },
            new Teacher {Id = 3, Name = "Jhon", DepartmentId = 15 },
            new Teacher {Id = 4, Name = "Alan", DepartmentId = 21 }
        };
                return list;
            }

            public static DataTable DbNullInt()
            {
                DataTable table = new DataTable();
                table.Columns.Add("Id", typeof(long));
                table.Columns.Add("Name", typeof(string));

                DataColumn column;
                column = new DataColumn("DepartmentId", System.Type.GetType("System.Int32"));
                column.AllowDBNull = true;
                table.Columns.Add(column);

                table.Rows.Add(1, "Smith", DBNull.Value);
                table.Rows.Add(2, "Hook", 1);


                return table;
            }
        }


        private void button20_Click(object sender, EventArgs e)
        {
            /*
            List<Student> students = Data.GetStudents();
            
            //List to DataTable conversion
            DataTable studentTbl = students.ToDataTable();
            
             * //DataTable to List conversion
            List<Student> newStudents = studentTbl.ToList<Student>();//ExtensionUtility.ToList<Student>(newStudents);
            this.dataGridView1.DataSource = newStudents;

            //List to DataTable conversion
            DataTable teacherTbl = Data.DbNullInt();
            //DataTable to List conversion
            List<Teacher> newTeachers = teacherTbl.ToList<Teacher>();


            this.dataGridView2.DataSource = newTeachers;
            */
        }

        private void button21_Click(object sender, EventArgs e)
        {


        }

        private void button22_Click(object sender, EventArgs e)
        {
            //代碼統計

            //string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_f_mix_new\vcs_Mix00\vcs_Mix00\Form1.cs";
            //CountMethods(filename);

            //GetMethodNameAndLines(filename);

            //StackCount(filename);
        }


        //统计方法的个数
        public void CountMethods(string path)
        {
            int count = 0;
            Regex reg = new Regex(@"\s*\w*\s*\w*\s*\w*\s+\w+\([^=!><]*\)(//.*)?\s*\{?$");
            string[] lines = File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++)
            {
                if (reg.IsMatch(lines[i].ToString()))
                {
                    count++;
                    richTextBox1.Text += lines[i].ToString() + "\n";
                }
            }
            string info = string.Format("total methods:{0}", count);
            richTextBox1.Text += info + "\n";
        }


        //统计方法名称
        public void GetMethodNameAndLines(string path)
        {
            string[] input = File.ReadAllLines(path);
            MatchCollection mc = null;
            Regex reg = new Regex(@"\s*\w*\s*\w*\s*\w+\s+\w+\([^=!><.]*\)(//.*)?\s*\{?$");
            ArrayList al = new ArrayList();
            for (int i = 0; i < input.Length; i++)
            {
                mc = reg.Matches(input[i]);
                if (mc.Count > 0)
                {
                    al.Add(mc[0].ToString());
                }
            }

            for (int m = 0; m < al.Count; m++)
            {
                richTextBox1.Text += "第 " + (m + 1).ToString() + " 個方法：" + al[m].ToString() + "\n";
            }
        }

        /*
        //正则与栈结合，统计方法行数名称和个数
        public void StackCount(string path)
        {
            Stack stack = new Stack();
            //ht存放方法名和方法行数
            Hashtable ht = new Hashtable();
            //指示是否为有效方法行
            bool isLine = false;
            //指示方法是否结束
            bool isEnd = false;
            string methodName = "";
            //标记后续是否还有方法 0-无 1-有
            int flag = 0;
            //临时存放方法行数
            int count = 0;
            //方法之外的普通行
            int j = 0;
            //匹配方法名
            Regex regMethodName = new Regex(@"\s+\w+\s*\(");
            //匹配方法开始行
            Regex regLineStart = new Regex(@"\s*\w*\s*\w*\s*\w+\s+\w+\([^=!><.]*\)(//.*)?\s*\{?$");
            //匹配左大括号
            Regex regLeft = new Regex(@"\s+\{");
            //匹配右大括号
            Regex regRight = new Regex(@"\s+\}");
            //存放源码字符串数组
            string[] lines = File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++)
            {
                if (regLineStart.IsMatch(lines[i]))
                {
                    Match mc = regMethodName.Match(lines[i].ToString());
                    //methodName = GetMethodName(mc.ToString());
                    methodName = mc.ToString();
                    if (lines[i].ToString().Contains('{'))
                    {
                        stack.Push(lines[i].ToString());
                    }
                    isLine = true;
                    isEnd = false;
                    flag = 1;
                    count++;
                }
                else if (regLeft.IsMatch(lines[i].ToString()))
                {
                    if (isLine)
                    {
                        count++;
                        //此处避免不规范写法导致的统计失误
                        if (lines[i].Contains('{') && lines[i].Contains('}'))
                        {
                            continue;
                        }
                        stack.Push(lines[i].ToString());
                    }
                }
                else if (regRight.IsMatch(lines[i]))
                {
                    if (!isEnd)
                    {
                        stack.Pop();
                        count++;
                    }
                    if (stack.Count == 0)
                    {
                        isLine = false;
                        isEnd = true;
                        if (flag != 0)
                        {
                            //解决重载方法的重名问题
                            if (ht.ContainsKey(methodName))
                            {
                                //isOverride += 1;
                                methodName = methodName + "重载+" + i;
                            }
                            ht.Add(methodName, count);
                            count = 0;
                        }
                        else
                        {
                            j++;
                        }
                        flag = 0;
                    }
                }
                else if (isLine)
                {
                    count++;
                }
                else
                {
                    j++;
                }
            }
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key : " + de.Key.ToString() + ", value : " + de.Value.ToString() + "\n";

                //Console.WriteLine(de.Key.ToString());
                //Console.WriteLine(de.Value.ToString());
            }
        }
        */

        private void button23_Click(object sender, EventArgs e)
        {
            string str = "10/3";
            float result = Calculator.dealWith(str);
            richTextBox1.Text += str + " = " + result.ToString() + "\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }

    //3Form1之外
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }


    /// <summary>
    /// 表達式計算類。支持數學函數，支持函數嵌套
    /// 作者watsonyin
    /// 開發日期：2010年10月 版本1.0
    /// </summary>
    public class NEval
    {
        public NEval()
        {

        }

        public double Eval(string expr)
        {
            try
            {
                string tmpexpr = expr.ToLower().Trim().Replace(" ", string.Empty);
                return Calc_Internal(tmpexpr);
            }
            catch (ExpressionException eex)
            {
                throw eex;
            }
            catch
            {
                throw new Exception("表達式錯誤");
            }
        }

        private Random m_Random = null;
        private double Calc_Internal(string expr)
        {
            /*
             * 1.    初始化一个空堆栈 
             * 2.    从左到右读入后缀表达式 
             * 3.    如果字符是一个操作数，把它压入堆栈。 
             * 4.    如果字符是个操作符，弹出两个操作数，执行恰当操作，然后把结果压入堆栈。如果您不能够弹出两个操作数，后缀表达式的语法就不正确。 
             * 5.    到后缀表达式末尾，从堆栈中弹出结果。若后缀表达式格式正确，那么堆栈应该为空。
            */

            Stack post2 = ConvertExprBack(expr);
            Stack post = new Stack();
            while (post2.Count > 0)
                post.Push(post2.Pop());

            Stack stack = new Stack();
            while (post.Count > 0)
            {
                string tmpstr = post.Pop().ToString();
                char c = tmpstr[0];
                LetterType lt = JudgeLetterType(tmpstr);
                if (lt == LetterType.Number)
                {
                    stack.Push(tmpstr);
                }
                else if (lt == LetterType.SimpleOperator)
                {
                    double d1 = double.Parse(stack.Pop().ToString());
                    double d2 = double.Parse(stack.Pop().ToString());
                    double r = 0;
                    if (c == '+')
                        r = d2 + d1;
                    else if (c == '-')
                        r = d2 - d1;
                    else if (c == '*')
                        r = d2 * d1;
                    else if (c == '/')
                        r = d2 / d1;
                    else if (c == '^')
                        r = Math.Pow(d2, d1);
                    else
                        throw new Exception("不支持操作符:" + c.ToString());
                    stack.Push(r);
                }
                else if (lt == LetterType.Function)  //如果是函数
                {
                    string[] p;
                    double d = 0;
                    double d1 = 0;
                    double d2 = 0;
                    int tmpos = tmpstr.IndexOf('(');
                    string funcName = tmpstr.Substring(0, tmpos);
                    switch (funcName)
                    {
                        case "asin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Asin(d).ToString());
                            break;
                        case "acos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Acos(d).ToString());
                            break;
                        case "atan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Atan(d).ToString());
                            break;
                        case "acot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Atan(d)).ToString());
                            break;
                        case "sin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sin(d).ToString());
                            break;
                        case "cos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Cos(d).ToString());
                            break;
                        case "tan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Tan(d).ToString());
                            break;
                        case "cot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Tan(d)).ToString());
                            break;
                        case "log":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Log(d1, d2).ToString());
                            break;
                        case "ln":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Log(d, Math.E).ToString());
                            break;
                        case "abs":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Abs(d).ToString());
                            break;
                        case "round":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Round(d1, (int)d2).ToString());
                            break;
                        case "int":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((int)d);
                            break;
                        case "trunc":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Truncate(d).ToString());
                            break;
                        case "floor":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Floor(d).ToString());
                            break;
                        case "ceil":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Ceiling(d).ToString());
                            break;
                        case "random":
                            if (m_Random == null)
                                m_Random = new Random();
                            d = m_Random.NextDouble();
                            stack.Push(d.ToString());
                            break;
                        case "exp":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Exp(d).ToString());
                            break;
                        case "pow":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Pow(d1, d2).ToString());
                            break;
                        case "sqrt":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sqrt(d).ToString());
                            break;
                        default:
                            throw new Exception("未定义的函数：" + funcName);

                    }

                }
            }
            object obj = stack.Pop();
            return double.Parse(obj.ToString());
        }

        /// <summary>
        /// 将函数括号内的字符串进行分割，获得参数列表，如果参数是嵌套的函数，用递归法计算得到它的值
        /// </summary>
        /// <param name="funcstr"></param>
        /// <param name="paramCount"></param>
        /// <param name="parameters"></param>
        private void SplitFuncStr(string funcstr, int paramCount, out string[] parameters)
        {
            parameters = new string[paramCount];
            int tmpPos = funcstr.IndexOf('(', 0);
            string str = funcstr.Substring(tmpPos + 1, funcstr.Length - tmpPos - 2);
            if (paramCount == 1)
            {
                parameters[0] = str;
            }
            else
            {
                int cpnum = 0;
                int startPos = 0;
                int paramIndex = 0;
                for (int i = 0; i <= str.Length - 1; i++)
                {
                    if (str[i] == '(')
                        cpnum++;
                    else if (str[i] == ')')
                        cpnum--;
                    else if (str[i] == ',')
                    {
                        if (cpnum == 0)
                        {
                            string tmpstr = str.Substring(startPos, i - startPos);
                            parameters[paramIndex] = tmpstr;
                            paramIndex++;
                            startPos = i + 1;
                        }
                    }
                }
                if (startPos < str.Length)
                {
                    string tmpstr = str.Substring(startPos);
                    parameters[paramIndex] = tmpstr;
                }
            }

            //如果参数是函数， 进一步采用递归的方法生成函数值
            for (int i = 0; i <= paramCount - 1; i++)
            {
                double d;
                if (!double.TryParse(parameters[i], out d))
                {
                    NEval calc = new NEval();
                    d = calc.Eval(parameters[i]);
                    parameters[i] = d.ToString();
                }
            }
        }


        /// <summary>
        /// 将中缀表达式转为后缀表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <returns></returns>
        private Stack ConvertExprBack(string expr)
        {
            /*
             * 新建一个Stack栈，用来存放运算符
             * 新建一个post栈，用来存放最后的后缀表达式
             * 从左到右扫描中缀表达式：
             * 1.若读到的是操作数，直接存入post栈，以#作为数字的结束
             * 2、若读到的是(,则直接存入stack栈
             * 3.若读到的是），则将stack栈中(前的所有运算符出栈，存入post栈
             * 4 若读到的是其它运算符，则将该运算符和stack栈顶运算符作比较：若高于或等于栈顶运算符， 则直接存入stack栈，
             * 否则将栈顶运算符（所有优先级高于读到的运算符的，不包括括号）出栈，存入post栈。最后将读到的运算符入栈
             * 当扫描完后，stack栈中还在运算符时，则将所有的运算符出栈，存入post栈
             * */


            Stack post = new Stack();
            Stack stack = new Stack();
            string tmpstr;
            int pos;
            for (int i = 0; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c, expr, i);

                if (lt == LetterType.Number)  //操作数
                {
                    GetCompleteNumber(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }
                else if (lt == LetterType.OpeningParenthesis) //左括号(
                {
                    stack.Push(c);
                }
                else if (lt == LetterType.ClosingParenthesis) //右括号)
                {
                    while (stack.Count > 0)
                    {
                        if (stack.Peek().ToString() == "(")
                        {
                            stack.Pop();
                            break;
                        }
                        else
                            post.Push(stack.Pop());
                    }
                }
                else if (lt == LetterType.SimpleOperator)  //其它运算符
                {
                    if (stack.Count == 0)
                        stack.Push(c);
                    else
                    {

                        char tmpop = (char)stack.Peek();
                        if (tmpop == '(')
                        {
                            stack.Push(c);
                        }
                        else
                        {
                            if (GetPriority(c) >= GetPriority(tmpop))
                            {
                                stack.Push(c);
                            }
                            else
                            {
                                while (stack.Count > 0)
                                {
                                    object tmpobj = stack.Peek();
                                    if (GetPriority((char)tmpobj) > GetPriority(c))
                                    {
                                        if (tmpobj.ToString() != "(")
                                            post.Push(stack.Pop());
                                        else
                                            break;
                                    }
                                    else
                                        break;
                                }
                                stack.Push(c);
                            }
                        }


                    }
                }
                else if (lt == LetterType.Function)  //如果是一个函数，则完整取取出函数，当作一个操作数处理
                {
                    GetCompleteFunction(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }

            }
            while (stack.Count > 0)
            {
                post.Push(stack.Pop());
            }

            return post;
        }


        private LetterType JudgeLetterType(char c, string expr, int pos)
        {
            string op = "*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else if ((c == '-') || (c == '+'))//要判断是减号还是负数
            {
                if (pos == 0)
                    return LetterType.Number;
                else
                {
                    char tmpc = expr[pos - 1];
                    if (tmpc <= '9' && tmpc >= '0')  //如果前面一位是操作数
                        return LetterType.SimpleOperator;
                    else if (tmpc == ')')
                        return LetterType.SimpleOperator;
                    else
                        return LetterType.Number;
                }
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(char c)
        {
            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(string s)
        {
            char c = s[0];
            if ((c == '-') || (c == '+'))
            {
                if (s.Length > 1)
                    return LetterType.Number;
                else
                    return LetterType.SimpleOperator;
            }

            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        /// <summary>
        /// 计算操作符的优先级
        /// </summary>
        /// <param name="c"></param>
        /// <returns></returns>
        private int GetPriority(char c)
        {
            if (c == '+' || c == '-')
                return 0;
            else if (c == '*')
                return 1;
            else if (c == '/')  //除号优先级要设得比乘号高，否则分母可能会被先运算掉
                return 2;
            else
                return 2;
        }

        /// <summary>
        /// 获取完整的函数表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="funcStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteFunction(string expr, int startPos, out string funcStr, out int endPos)
        {
            int cpnum = 0;
            for (int i = startPos; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c);
                if (lt == LetterType.OpeningParenthesis)
                    cpnum++;
                else if (lt == LetterType.ClosingParenthesis)
                {
                    cpnum--;//考虑到函数嵌套的情况，消除掉内部括号
                    if (cpnum == 0)
                    {
                        endPos = i;
                        funcStr = expr.Substring(startPos, endPos - startPos + 1);
                        return;
                    }


                }

            }
            funcStr = "";
            endPos = -1;
        }

        /// <summary>
        /// 获取到完整的数字
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="numberStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteNumber(string expr, int startPos, out string numberStr, out int endPos)
        {
            char c = expr[startPos];
            for (int i = startPos + 1; i <= expr.Length - 1; i++)
            {
                char tmpc = expr[i];
                if (JudgeLetterType(tmpc) != LetterType.Number)
                {
                    endPos = i - 1;
                    numberStr = expr.Substring(startPos, endPos - startPos + 1);
                    return;
                }
            }
            numberStr = expr.Substring(startPos);
            endPos = expr.Length - 1;
        }
    }


    /// <summary>
    /// 可以检测到的表达式错误的Exception
    /// </summary>
    public class ExpressionException : Exception
    {
        public override string Message
        {
            get
            {
                return base.Message;
            }
        }
    }

    /// <summary>
    /// 字符类别
    /// </summary>
    public enum LetterType
    {
        Number,
        SimpleOperator,
        Function,
        OpeningParenthesis,
        ClosingParenthesis
    }

    public class PartyLogoA : System.ComponentModel.Component
    {
        private Color _color = Color.Black;
        private Color _borderColor = Color.Transparent;
        private float _borderWidth = 1f;

        private GraphicsPath _graphicsPath = null;

        protected GraphicsPath cCP = new GraphicsPath(
         new PointF[] {
        new PointF(365F, 6F),
        new PointF(531F, 54F),
        new PointF(596F, 133F),
        new PointF(622F, 250F),
        new PointF(637F, 336F),
        new PointF(627F, 412F),
        new PointF(573F, 486F),
        new PointF(323F, 234F),
        new PointF(416F, 140F),
        new PointF(376F, 100F),
        new PointF(358F, 101F),
        new PointF(343F, 118F),
        new PointF(258F, 118F),
        new PointF(88F, 288F),
        new PointF(183F, 384F),
        new PointF(248F, 320F),
        new PointF(490F, 563F),
        new PointF(408F, 629F),
        new PointF(317F, 629F),
        new PointF(210F, 583F),
        new PointF(165F, 560F),
        new PointF(134F, 537F),
        new PointF(93F, 484F),
        new PointF(37F, 539F),
        new PointF(76F, 578F),
        new PointF(67F, 591F),
        new PointF(26F, 585F),
        new PointF(-9F, 620F),
        new PointF(11F, 676F),
        new PointF(27F, 704F),
        new PointF(42F, 718F),
        new PointF(81F, 713F),
        new PointF(105F, 709F),
        new PointF(125F, 676F),
        new PointF(126F, 640F),
        new PointF(137F, 631F),
        new PointF(199F, 685F),
        new PointF(246F, 713F),
        new PointF(342F, 720F),
        new PointF(431F, 724F),
        new PointF(492F, 711F),
        new PointF(576F, 651F),
        new PointF(649F, 725F),
        new PointF(731F, 640F),
        new PointF(655F, 566F),
        new PointF(703F, 491F),
        new PointF(718F, 451F),
        new PointF(719F, 354F),
        new PointF(720F, 243F),
        new PointF(635F, 22F),
        new PointF(379F, 6F)
       },
         new System.Byte[] {
          0,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          131});

        private float _width = 100f;
        private float _height = 100f;
        private PointF _location = new PointF(0, 0);

        public float Width
        {
            get { return this._width; }
            set { this._width = value; }
        }

        public PointF Location
        {
            get { return this._location; }
            set { this._location = value; }
        }

        public float Height
        {
            get { return this._height; }
            set { this._height = value; }
        }

        public GraphicsPath GraphicsPath
        {
            get
            {
                //this._graphicsPath = this.RetrieveGraphicsPath();
                return this._graphicsPath;
            }
            set { this._graphicsPath = value; }
        }

        public Color Color
        {
            get { return this._color; }
            set { this._color = value; }
        }

        public float BorderWidth
        {
            get { return this._borderWidth; }
            set { this._borderWidth = value; }
        }

        public Color BorderColor
        {
            get { return this._borderColor; }
            set { this._borderColor = value; }
        }

        /*
        private GraphicsPath RetrieveGraphicsPath()
        {
            GraphicsPath gp = new GraphicsPath();
            gp.FillMode = FillMode.Alternate;
            gp.AddPath(this.cCP, false);

            //LogoHelper lh = new LogoHelper();
            //lh.DestRectF = new RectangleF(this._location, new SizeF(this._width, this._height));
            //lh.SrcGP = gp;
            //GraphicsPath gpResult = lh.RetrievePath();
            gp.Dispose();

            return gpResult;
        }
        */

        public PartyLogoA()
        {
            this.InitializeGraphics();
        }

        private void InitializeGraphics()
        {
        }

        public virtual void RenderGraphics(Graphics g)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;

            g.FillPath(new SolidBrush(this._color), this.GraphicsPath);
            g.DrawPath(new Pen(this._borderColor, this._borderWidth), this.GraphicsPath);
        }

        // Required to dispose of created resources
        private void DisposeGraphics()
        {
            this.cCP.Dispose();
            if (this._graphicsPath != null) this._graphicsPath.Dispose();
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                this.DisposeGraphics();
            }
        }
    }

    public static class Calculator
    {
        public static float dealWith(string number)
        {
            string operand1 = "", opreand2 = "";
            float result = 0;
            char opera = ' ', operandOrOera = ' ';
            string[,] opreandArray = new string[50, 2];
            Queue numberQueue = new Queue();

            //循環字符串中的所有字符並賦值給numberQueue隊列 
            foreach (char c in number)
            {

                numberQueue.Enqueue(c);
            }

            //拆分隊列中的字符，構成一個數字與“+”或“-”的組合，然後逐個放入二維數組opreandArray中
            while (numberQueue.Count != 0)
            {
                operandOrOera = Convert.ToChar(numberQueue.Peek());
                if (operandOrOera == '(')
                {
                    numberQueue.Dequeue();
                    string inside = null;
                    while (Convert.ToChar(numberQueue.Peek()) != ')')
                    {
                        inside += (numberQueue.Dequeue()).ToString();
                    }
                    numberQueue.Dequeue();
                    operand1 = dealWith(inside).ToString();
                }
                while (Convert.ToInt32(operandOrOera) > 47 && Convert.ToInt32(operandOrOera) < 58)//ASCII48-57對應0-9
                {
                    numberQueue.Dequeue();
                    operand1 += operandOrOera.ToString();
                    if (numberQueue.Count != 0)
                    {
                        operandOrOera = Convert.ToChar(numberQueue.Peek());
                    }
                    else
                    {
                        break;
                    }
                }
                int j = 0;
                if (operandOrOera == '+' || operandOrOera == '-' || operandOrOera == '*' || operandOrOera == '/')
                {
                    numberQueue.Dequeue();
                    opera = operandOrOera;
                    //如果是"+"或"-"
                    if (opera == '+' || opera == '-')
                    {
                        opreandArray[j, 0] = operand1;
                        opreandArray[j, 1] = opera.ToString();
                        j++;
                        operand1 = null;
                    }
                    //如果是"*"或"/"
                    else
                    {
                        char n = Convert.ToChar(numberQueue.Peek());
                        if (n == '(')
                        {

                            numberQueue.Dequeue();
                            string inside = null;
                            while (Convert.ToChar(numberQueue.Peek()) != ')')
                            {
                                inside += (numberQueue.Dequeue()).ToString();
                            }
                            numberQueue.Dequeue();
                            opreand2 = dealWith(inside).ToString();
                        }
                        while (Convert.ToInt32(n) > 47 && Convert.ToInt32(n) < 58)
                        {
                            opreand2 += n.ToString();
                            numberQueue.Dequeue();
                            if (numberQueue.Count != 0)
                            {
                                n = Convert.ToChar(numberQueue.Peek());
                            }
                            else
                            {
                                break;
                            }
                        }

                        switch (opera)
                        {
                            case ('*'):
                                {
                                    operand1 = (Convert.ToInt32(operand1) * Convert.ToInt32(opreand2)).ToString();
                                    break;
                                }
                            case ('/'):
                                {
                                    try
                                    {
                                        operand1 = (Convert.ToInt32(operand1) / Convert.ToInt32(opreand2)).ToString();
                                    }
                                    catch (Exception)
                                    {

                                    }
                                    break;
                                }

                        }
                        opreand2 = null;
                    }
                }
            }


            //把二維數組中的數計算，賦值result
            int count = 0;
            for (int i = 0; opreandArray[i, 0] != null; i++)
            {
                count++;
            }
            for (int i = 0; i < count; i++)
            {
                if (i == 0)
                {
                    result += Convert.ToInt32(opreandArray[i, 0]);

                }
                else
                {
                    if (opreandArray[i - 1, 1] == "+")
                    {
                        result += Convert.ToInt32(opreandArray[i, 0]);
                    }
                    else
                    {
                        result -= Convert.ToInt32(opreandArray[i, 0]);
                    }
                }
            }



            //最後把沒有放進數組中的加上或者減掉
            if (count != 0)
            {
                if (opreandArray[count - 1, 1] == "+")
                {
                    return result + Convert.ToInt32(operand1);
                }
                else
                {
                    return result - Convert.ToInt32(operand1);
                }
            }
            else
            {
                return Convert.ToInt32(operand1);
            }
        }
    }

    /// <summary> 
    /// 感知哈希算法 
    /// </summary> 
    public class ImageComparer
    {
        /// <summary> 
        /// 獲取圖片的Hashcode 
        /// </summary> 
        /// <param name="imageName"></param> 
        /// <returns></returns> 
        public static string GetImageHashCode(string imageName)
        {
            int width = 8;
            int height = 8;

            //  第一步 
            //  將圖片縮小到8x8的尺寸，總共64個像素。這一步的作用是去除圖片的細節， 
            //  只保留結構、明暗等基本信息，摒棄不同尺寸、比例帶來的圖片差異。 
            Bitmap bmp = new Bitmap(Thumb(imageName));
            int[] pixels = new int[width * height];

            //  第二步 
            //  將縮小後的圖片，轉為64級灰度。也就是說，所有像素點總共只有64種顏色。 
            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < height; j++)
                {
                    Color color = bmp.GetPixel(i, j);
                    pixels[i * height + j] = RGBToGray(color.ToArgb());
                }
            }

            //  第三步 
            //  計算所有64個像素的灰度平均值。 
            int avgPixel = Average(pixels);

            //  第四步 
            //  將每個像素的灰度，與平均值進行比較。大於或等於平均值，記為1；小於平均值，記為0。 
            int[] comps = new int[width * height];
            for (int i = 0; i < comps.Length; i++)
            {
                if (pixels[i] >= avgPixel)
                {
                    comps[i] = 1;
                }
                else
                {
                    comps[i] = 0;
                }
            }

            //  第五步 
            //  將上一步的比較結果，組合在一起，就構成了一個64位的整數，這就是這張圖片的指紋。組合的次序並不重要，只要保證所有圖片都采用同樣次序就行了。 
            StringBuilder hashCode = new StringBuilder();
            for (int i = 0; i < comps.Length; i += 4)
            {
                int result = comps[i] * (int)Math.Pow(2, 3) + comps[i + 1] * (int)Math.Pow(2, 2) + comps[i + 2] * (int)Math.Pow(2, 1) + comps[i + 2];
                hashCode.Append(BinaryToHex(result));
            }
            bmp.Dispose();
            return hashCode.ToString();
        }

        /// <summary> 
        /// 計算"漢明距離"（Hamming distance）。 
        /// 如果不相同的數據位不超過5，就說明兩張圖片很相似；如果大於10，就說明這是兩張不同的圖片。 
        /// </summary> 
        /// <param name="sourceHashCode"></param> 
        /// <param name="hashCode"></param> 
        /// <returns></returns> 
        public static int HammingDistance(String sourceHashCode, String hashCode)
        {
            int difference = 0;
            int len = sourceHashCode.Length;

            for (int i = 0; i < len; i++)
            {
                if (sourceHashCode[i] != hashCode[i])
                {
                    difference++;
                }
            }
            return difference;
        }

        /// <summary> 
        /// 縮放圖片
        /// </summary> 
        /// <param name="imageName"></param> 
        /// <returns></returns> 
        private static Image Thumb(string imageName)
        {
            return Image.FromFile(imageName).GetThumbnailImage(8, 8, () => { return false; }, IntPtr.Zero);
        }

        /// <summary> 
        /// 轉為64級灰度 
        /// </summary> 
        /// <param name="pixels"></param> 
        /// <returns></returns> 
        private static int RGBToGray(int pixels)
        {
            int _red = (pixels >> 16) & 0xFF;
            int _green = (pixels >> 8) & 0xFF;
            int _blue = (pixels) & 0xFF;
            return (int)(0.3 * _red + 0.59 * _green + 0.11 * _blue);
        }

        /// <summary> 
        /// 計算平均值 
        /// </summary> 
        /// <param name="pixels"></param> 
        /// <returns></returns> 
        private static int Average(int[] pixels)
        {
            float m = 0;
            for (int i = 0; i < pixels.Length; ++i)
            {
                m += pixels[i];
            }
            m = m / pixels.Length;
            return (int)m;
        }

        private static char BinaryToHex(int binary)
        {
            char ch = ' ';
            switch (binary)
            {
                case 0:
                    ch = '0';
                    break;
                case 1:
                    ch = '1';
                    break;
                case 2:
                    ch = '2';
                    break;
                case 3:
                    ch = '3';
                    break;
                case 4:
                    ch = '4';
                    break;
                case 5:
                    ch = '5';
                    break;
                case 6:
                    ch = '6';
                    break;
                case 7:
                    ch = '7';
                    break;
                case 8:
                    ch = '8';
                    break;
                case 9:
                    ch = '9';
                    break;
                case 10:
                    ch = 'a';
                    break;
                case 11:
                    ch = 'b';
                    break;
                case 12:
                    ch = 'c';
                    break;
                case 13:
                    ch = 'd';
                    break;
                case 14:
                    ch = 'e';
                    break;
                case 15:
                    ch = 'f';
                    break;
                default:
                    ch = ' ';
                    break;
            }
            return ch;
        }
    }
}
