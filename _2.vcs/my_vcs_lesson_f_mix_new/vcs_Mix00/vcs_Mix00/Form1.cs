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
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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

            //從檔案完整路徑分離出資料夾,檔案名稱,副檔名
            string full_filename = @"C:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";
            //取得資料夾路徑
            string foldername = full_filename.Substring(0, full_filename.LastIndexOf("\\") + 1);
            //取得檔案名稱
            string short_filename =
                full_filename.Substring(full_filename.LastIndexOf("\\") + 1,
                full_filename.LastIndexOf(".") -
                (full_filename.LastIndexOf("\\") + 1));
            //取得副檔名
            string ext_filename =
                full_filename.Substring(full_filename.LastIndexOf(".") + 1,
                full_filename.Length - full_filename.LastIndexOf(".") - 1);

            richTextBox1.Text += "檔案完整路徑:\t" + full_filename + "\n";
            richTextBox1.Text += "資料夾路徑:\t" + foldername + "\n";
            richTextBox1.Text += "檔案名稱:\t" + short_filename + "\n";
            richTextBox1.Text += "副檔名:\t" + ext_filename + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //取得目前的Process
            using (Process curProcess = Process.GetCurrentProcess())
            {
                richTextBox1.Text += "aaaa = " + curProcess.ProcessName + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainModule + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainWindowTitle + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.ProcessorAffinity + "\n";
                richTextBox1.Text += "處理序的名稱 :\t" + curProcess.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
                richTextBox1.Text += "主視窗標題 :\t" + curProcess.MainWindowTitle + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "處理序啟動的時間 :\t" + curProcess.StartTime.ToString() + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "這個處理序的總處理器時間 :\t" + curProcess.TotalProcessorTime.ToString() + "\n";   //取得處理序的主視窗標題

                //程序的退出
                //Process.GetCurrentProcess().Kill();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //動態驗證碼變成靜態
            //將一個gif拆成多圖

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\run.gif";

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

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\id_card_03.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\id_card_01.jpg";

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

        static float Gamma(float x)
        {
            return (float)(x > 0.04045f ? Math.Pow((x + 0.055f) / 1.055f, 2.4f) : x / 12.92f);
        }

        public static float[] rgb2lab(float var_R, float var_G, float var_B)
        {

            float[] arr = new float[3];
            float B = Gamma(var_B);
            float G = Gamma(var_G);
            float R = Gamma(var_R);
            float X = 0.412453f * R + 0.357580f * G + 0.180423f * B;
            float Y = 0.212671f * R + 0.715160f * G + 0.072169f * B;
            float Z = 0.019334f * R + 0.119193f * G + 0.950227f * B;

            X /= 0.95047f;
            Y /= 1.0f;
            Z /= 1.08883f;

            float FX = (float)(X > 0.008856f ? Math.Pow(X, 1.0f / 3.0f) : (7.787f * X + 0.137931f));
            float FY = (float)(Y > 0.008856f ? Math.Pow(Y, 1.0f / 3.0f) : (7.787f * Y + 0.137931f));
            float FZ = (float)(Z > 0.008856f ? Math.Pow(Z, 1.0f / 3.0f) : (7.787f * Z + 0.137931f));
            arr[0] = Y > 0.008856f ? (116.0f * FY - 16.0f) : (903.3f * Y);
            arr[1] = 500f * (FX - FY);
            arr[2] = 200f * (FY - FZ);
            return arr;

        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //RGB 轉 LAB

            float var_R = 255;
            float var_G = 0;
            float var_B = 0;

            float[] cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";


            var_R = 0;
            var_G = 255;
            var_B = 0;

            cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";


            var_R = 0;
            var_G = 0;
            var_B = 255;

            cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //Image Cut

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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

            System.Console.Beep(400, 500);
            System.Console.Beep(800, 500);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            ((Button)sender).Text = "改 Button Text 為 AAAA";


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

        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);
        private void button10_Click(object sender, EventArgs e)
        {
            //取得本機或網路磁碟機的磁碟訊息, 選擇磁碟或目錄
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                long fb, ftb, tfb;
                string str = fbd.SelectedPath;
                richTextBox1.Text += "path : " + str + "\n";
                if (GetDiskFreeSpaceEx(str, out fb, out ftb, out tfb) != 0)
                {
                    string strfb = Convert.ToString(fb / 1024 / 1024 / 1024) + " G";
                    string strftb = Convert.ToString(ftb / 1024 / 1024 / 1024) + " G";
                    string strtfb = Convert.ToString(tfb / 1024 / 1024 / 1024) + " G";
                    richTextBox1.Text += "總空間" + strfb + "\n";
                    richTextBox1.Text += "可用空間" + strftb + "\n";
                    richTextBox1.Text += "總剩餘空間" + strtfb + "\n";
                }
                else
                {
                    MessageBox.Show("NO");
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            richTextBox1.Text += "檔案 : " + filename + "\n";

            string strOne = System.IO.Path.GetFileNameWithoutExtension(filename);
            richTextBox1.Text += "取得前檔名\n";
            richTextBox1.Text += strOne + "\n";

            byte[] buffer = new byte[100];
            for (int i = 0; i < 26; i++)
            {
                buffer[i] = (byte)(65 + i);
            }
            richTextBox1.Text += buffer + "\n";
            richTextBox1.Text += "len = " + buffer.Length.ToString() + "\n";

            string ssss1 = System.Text.UTF8Encoding.Default.GetString(buffer);
            richTextBox1.Text += ssss1 + "\n";
            richTextBox1.Text += "len = " + ssss1.Length.ToString() + "\n";

            int length = 26;
            string ssss2 = System.Text.UTF8Encoding.Default.GetString(buffer, 0, length);
            richTextBox1.Text += ssss2 + "\n";
            richTextBox1.Text += "len = " + ssss2.Length.ToString() + "\n";

            //往上兩層的檔案
            filename = Application.StartupPath.ToString();
            filename = filename.Substring(0, filename.LastIndexOf("\\"));
            filename = filename.Substring(0, filename.LastIndexOf("\\"));
            filename += @"\SystemSet.ini";
            richTextBox1.Text += "filename : " + filename + "\n";

            string data_to_write = string.Empty;
            string contact_address_to = string.Empty;
            string camera_serial_data = "0123456789";

            int len = camera_serial_data.Length;
            richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";


            //data_to_write = camera_serial_data.Substring(0, 16); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                if (len > 16)
                    data_to_write = camera_serial_data.Substring(0, 16);
                else
                    data_to_write = camera_serial_data;
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                //MessageBox.Show(ex.Message);
                richTextBox1.Text += "發生例外 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "data_to_write : " + data_to_write + "\n";
                richTextBox1.Text += "\nlen = " + data_to_write.Length.ToString() + "\n";
            }

        }

        private void button14_Click(object sender, EventArgs e)
        {
            int i;
            //string camera_serial_data = "EC041302870012 @";
            string camera_serial_data = "ABCDEFGABCDEFGAB";
            int len = camera_serial_data.Length;
            //richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            //檢查英數字元的正確性
            bool flag_serial_data_wrong = false;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
                var kk = camera_serial_data[i];

                if (((kk >= 'A') && (kk <= 'Z')) || ((kk >= 'a') && (kk <= 'z')) || ((kk >= '0') && (kk <= '9')))
                {
                    //richTextBox1.Text += "O";
                    flag_serial_data_wrong = false;
                }
                else
                {
                    //richTextBox1.Text += "X";
                    flag_serial_data_wrong = true;
                    break;
                }
            }
            if (flag_serial_data_wrong == true)
            {
                richTextBox1.Text += "有裁剪\n";
                int cut_length = i;
                //richTextBox1.Text += cut_length.ToString() + "\n";
                camera_serial_data = camera_serial_data.Substring(0, cut_length);
            }
            else
            {
                richTextBox1.Text += "無裁剪\n";
            }

            len = camera_serial_data.Length;
            //richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            richTextBox1.Text += "序號資料 : " + camera_serial_data + "\n";



            string camera_serial_data2 = string.Empty;
            if (camera_serial_data.Length > 16)
            {
                richTextBox1.Text += "太長\n";
                camera_serial_data2 = camera_serial_data.Substring(0, 16);
            }
            else if (camera_serial_data.Length < 16)
            {
                richTextBox1.Text += "太短\n";
                camera_serial_data2 = camera_serial_data.PadRight(16, 'W'); //向長度小於16的字符串末尾添加空格，補足16個字符
            }
            else
            {
                richTextBox1.Text += "剛好\n";
                camera_serial_data2 = camera_serial_data;

            }
            richTextBox1.Text += "len of camera_serial_data2 = " + camera_serial_data2.Length.ToString() + "\n";
            richTextBox1.Text += camera_serial_data2 + "\n";


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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\english_text.txt";
            StatisticsWords(filename);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //谷歌百度以圖搜圖 感知哈希算法
            //感知哈希算法 獲取圖片的Hashcode

            string filename = string.Empty;
            string result = string.Empty;

            filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.bmp";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //檔名處理

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            richTextBox1.Text += "全檔名 : " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

            string filename2 = "tmp_" + f_name + "_new" + ext_name;

            richTextBox1.Text += "新全檔名 : " + filename2 + "\n";

            //自動檔名 與 存檔語法
            string filename3 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            richTextBox1.Text += "新全檔名 : " + filename3 + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Color Matrix的使用 1\n";
            //color_correction_matrix = 
            double[,] color_correction_matrix = new double[,] {
            { 1.36, -0.3, -0.06},
            { -0.20, 1.32, -0.12},
            { -0.04, -0.55, 1.59}
            };

            richTextBox1.Text += color_correction_matrix[0, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 2].ToString() + "\n";

            double N16 = color_correction_matrix[0, 0];
            double O16 = color_correction_matrix[0, 1];
            double P16 = color_correction_matrix[0, 2];
            double N17 = color_correction_matrix[1, 0];
            double O17 = color_correction_matrix[1, 1];
            double P17 = color_correction_matrix[1, 2];
            double N18 = color_correction_matrix[2, 0];
            double O18 = color_correction_matrix[2, 1];
            double P18 = color_correction_matrix[2, 2];

            //保留給 RGB to YUV Conversion Matrix
            //double[] B = new double[] { 1, 2, 3, 4, 5 };
            double E12 = -0.31;
            double F12 = -0.59;
            double G12 = 0.89;
            double E13 = 0.69;
            double F13 = -0.59;
            double G13 = -0.11;
            double E17 = E12 * 0.563;
            double F17 = F12 * 0.563;
            double G17 = G12 * 0.563;
            double E18 = E13 * 0.713;
            double F18 = F13 * 0.713;
            double G18 = G13 * 0.713;

            double E22 = E17 * N16 + F17 * N17 + G17 * N18;	//MMULT(E17:G17,N16:N18)
            double F22 = E17 * O16 + F17 * O17 + G17 * O18;	//MMULT(E17:G17,O16:O18)
            double G22 = E17 * P16 + F17 * P17 + G17 * P18;	//MMULT(E17:G17,P16:P18)
            double E23 = E18 * N16 + F18 * N17 + G18 * N18;	//MMULT(E18:G18,N16:N18)
            double F23 = E18 * O16 + F18 * O17 + G18 * O18;	//MMULT(E18:G18,O16:O18)
            double G23 = E18 * P16 + F18 * P17 + G18 * P18;	//MMULT(E18:G18,P16:P18)

            richTextBox1.Text += "E22 = " + E22.ToString() + "\n";
            richTextBox1.Text += "F22 = " + F22.ToString() + "\n";
            richTextBox1.Text += "G22 = " + G22.ToString() + "\n";
            richTextBox1.Text += "E23 = " + E23.ToString() + "\n";
            richTextBox1.Text += "F23 = " + F23.ToString() + "\n";
            richTextBox1.Text += "G23 = " + G23.ToString() + "\n";

            double dMTX1 = E23 * 128;
            double dMTX2 = F23 * 128;
            double dMTX3 = G23 * 128;
            double dMTX4 = E22 * 128;
            double dMTX5 = F22 * 128;
            double dMTX6 = G22 * 128;

            richTextBox1.Text += "dMTX1 = " + dMTX1.ToString() + "\n";
            richTextBox1.Text += "dMTX2 = " + dMTX2.ToString() + "\n";
            richTextBox1.Text += "dMTX3 = " + dMTX3.ToString() + "\n";
            richTextBox1.Text += "dMTX4 = " + dMTX4.ToString() + "\n";
            richTextBox1.Text += "dMTX5 = " + dMTX5.ToString() + "\n";
            richTextBox1.Text += "dMTX6 = " + dMTX6.ToString() + "\n";

            int MTX1 = (int)Math.Round(dMTX1);
            int MTX2 = (int)Math.Round(dMTX2);
            int MTX3 = (int)Math.Round(dMTX3);
            int MTX4 = (int)Math.Round(dMTX4);
            int MTX5 = (int)Math.Round(dMTX5);
            int MTX6 = (int)Math.Round(dMTX6);

            if (MTX1 >= 0)
                richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            else
                richTextBox1.Text += "MTX1 = -0x" + (-MTX1).ToString("X2") + " = " + MTX1.ToString() + "\n";
            if (MTX2 >= 0)
                richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            else
                richTextBox1.Text += "MTX2 = -0x" + (-MTX2).ToString("X2") + " = " + MTX2.ToString() + "\n";
            if (MTX3 >= 0)
                richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            else
                richTextBox1.Text += "MTX3 = -0x" + (-MTX3).ToString("X2") + " = " + MTX3.ToString() + "\n";
            if (MTX4 >= 0)
                richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            else
                richTextBox1.Text += "MTX4 = -0x" + (-MTX4).ToString("X2") + " = " + MTX4.ToString() + "\n";
            if (MTX5 >= 0)
                richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            else
                richTextBox1.Text += "MTX5 = -0x" + (-MTX5).ToString("X2") + " = " + MTX5.ToString() + "\n";
            if (MTX6 >= 0)
                richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";
            else
                richTextBox1.Text += "MTX6 = -0x" + (-MTX6).ToString("X2") + " = " + MTX6.ToString() + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Color Matrix的使用 2\n";

            int MTX1 = 0;
            int MTX2 = 83;
            int MTX3 = -84;
            int MTX4 = 0;
            int MTX5 = -29;
            int MTX6 = 28;

            richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";

            int CMXSIGN = 0;
            int CMX16 = 0;
            int CMX15 = 0;
            int CMX14 = 0;
            int CMX13 = 0;
            int CMX12 = 0;
            int CMX11 = 0;

            if (MTX1 >= 0)
            {
                CMX11 = MTX1;
            }
            else
            {
                CMX11 = -MTX1;
                CMXSIGN += 1;
            }
            if (MTX2 >= 0)
            {
                CMX12 = MTX2;
            }
            else
            {
                CMX12 = -MTX2;
                CMXSIGN += 2;
            }
            if (MTX3 >= 0)
            {
                CMX13 = MTX3;
            }
            else
            {
                CMX13 = -MTX3;
                CMXSIGN += 4;
            }
            if (MTX4 >= 0)
            {
                CMX14 = MTX4;
            }
            else
            {
                CMX14 = -MTX4;
                CMXSIGN += 8;
            }
            if (MTX5 >= 0)
            {
                CMX15 = MTX5;
            }
            else
            {
                CMX15 = -MTX5;
                CMXSIGN += 16;
            }
            if (MTX6 >= 0)
            {
                CMX16 = MTX6;
            }
            else
            {
                CMX16 = -MTX6;
                CMXSIGN += 32;
            }

            richTextBox1.Text += "CMXSIGN = 0x" + CMXSIGN.ToString("X2") + " = " + CMXSIGN.ToString() + "\n";
            richTextBox1.Text += "CMX11 = 0x" + CMX11.ToString("X2") + " = " + CMX11.ToString() + "\n";
            richTextBox1.Text += "CMX12 = 0x" + CMX12.ToString("X2") + " = " + CMX12.ToString() + "\n";
            richTextBox1.Text += "CMX13 = 0x" + CMX13.ToString("X2") + " = " + CMX13.ToString() + "\n";
            richTextBox1.Text += "CMX14 = 0x" + CMX14.ToString("X2") + " = " + CMX14.ToString() + "\n";
            richTextBox1.Text += "CMX15 = 0x" + CMX15.ToString("X2") + " = " + CMX15.ToString() + "\n";
            richTextBox1.Text += "CMX16 = 0x" + CMX16.ToString("X2") + " = " + CMX16.ToString() + "\n";

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //代碼統計

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
            string str = "(123+456)*789/123";
            float result = Calculator.dealWith(str);
            richTextBox1.Text += str + " = " + result.ToString() + "\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //tmp1


            //** 日期時間輸出

            Console.WriteLine(String.Format("{0:dddd, MMM d yyyy}", DateTime.Now));
            Console.WriteLine(String.Format("{0:HH:mm:ss}", DateTime.Now));
            Console.WriteLine(String.Format("{0:D}", DateTime.Now));
            Console.WriteLine(String.Format("{0:hh:mm:ss tt}", DateTime.Now));
            Console.WriteLine(String.Format("{0:T}", DateTime.Now));
            Console.WriteLine(String.Format("{0:h:m:s}", DateTime.Now));

            //** 自訂格式化輸出
            Console.WriteLine(String.Format("{0:##,##0.00}", 8567.1));
            Console.WriteLine(String.Format("{0:###0.00}", 566.7));
            Console.WriteLine(String.Format("{0:0.00%}", 8));



        }

        static string reverse(string str)
        {
            char[] temp;
            string strR = "";
            int i;
            temp = str.ToCharArray();
            for (i = temp.Length - 1; i >= 0; i--)
                strR += temp[i];
            return strR;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            string str;
            str = "abcdefghijk";
            richTextBox1.Text += "經反轉後的字串內容：" + reverse(str) + "\n";
        }

        static void hanoi(int n, int p1, int p2, int p3)
        {
            if (n == 1)
                Console.WriteLine("盤子從 " + p1 + " 移到 " + p3);
            else
            {
                hanoi(n - 1, p1, p3, p2);
                Console.WriteLine("盤子從 " + p1 + " 移到 " + p3);
                hanoi(n - 1, p2, p1, p3);
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            int N = 5;
            richTextBox1.Text += "請輸入盤子數量：" + N.ToString() + "\n";
            hanoi(N, 1, 2, 3);
        }

        class Book
        {
            public int books; //宣告books為公用變數
        }

        private void button27_Click(object sender, EventArgs e)
        {
            Book eng = new Book();
            eng.books = 10;
            Console.WriteLine("目前英文類書籍共有{0}本", eng.books);


        }

        static int top = -1;

        public static void Push(int[] stack, int MAX, int val)
        {
            if (top >= MAX - 1)
                Console.WriteLine("[堆疊已經滿了]");
            else
            {
                top++;
                stack[top] = val;
            }
        }

        public static int Pop(int[] stack)
        {
            if (top < 0)
                Console.WriteLine("[堆疊已經空了]");
            else
                top--;
            return stack[top];
        }

        private void button28_Click(object sender, EventArgs e)
        {
            int[] card = new int[52];
            int[] stack = new int[52];
            int i, j, k = 0, test;
            char ascVal = 'H';
            int style;
            Random intRnd = new Random();
            for (i = 0; i < 52; i++)
                card[i] = i;
            Console.WriteLine("[洗牌中...請稍後!]");
            while (k < 30)
            {
                for (i = 0; i < 51; i++)
                {
                    for (j = i + 1; j < 52; j++)
                    {
                        if ((intRnd.Next(10000) % 52) == 2)
                        {
                            test = card[i];//洗牌
                            card[i] = card[j];
                            card[j] = test;
                        }
                    }

                }
                k++;
            }
            i = 0;
            while (i != 52)
            {
                Push(stack, 52, card[i]);  //將52張牌推入堆疊
                i++;
            }
            Console.WriteLine("[逆時針發牌]");
            Console.WriteLine("[顯示各家牌子]\n 東家\t  北家\t   西家\t    南家");
            Console.WriteLine("=================================");
            while (top >= 0)
            {
                style = stack[top] / 13;   //計算牌子花色
                switch (style)          //牌子花色圖示對應
                {
                    case 0:             //梅花
                        ascVal = 'C';
                        break;
                    case 1:             //方塊
                        ascVal = 'D';
                        break;
                    case 2:             //紅心
                        ascVal = 'H';
                        break;
                    case 3:             //黑桃
                        ascVal = 'S';
                        break;
                }
                Console.WriteLine("[" + ascVal + (stack[top] % 13 + 1) + "]");
                Console.WriteLine('\t');
                if (top % 4 == 0)
                    Console.WriteLine();
                top--;
            }
            //ReadKey();
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
