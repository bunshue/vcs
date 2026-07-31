using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream
using System.Net;
using System.Net.Sockets;
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
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False

namespace vcs_Mix00
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;

        bool lastStatus = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            pictureBox1.Size = new Size(400, 400);
            pictureBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(320, 690);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1620, 750);
            this.Text = "vcs_Mix00";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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
            //richTextBox1.Text += ((Button)sender).Text + "\n";    same

            Button btn = ((Button)sender);//sender轉Button類別物件，接著再指定給btn
            richTextBox1.Text += btn.Text + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //測試 String.Format

            //自訂格式化輸出

            richTextBox1.Text += "自訂格式化輸出\n";
            richTextBox1.Text += String.Format("{0:##,##0.00}", 8567.1) + "\n";
            richTextBox1.Text += String.Format("{0:###0.00}", 566.7) + "\n";
            richTextBox1.Text += String.Format("{0:0.00%}", 8) + "\n";


            //String.Format("{0，–10}",text)
            //要将字符串向左对齐使用负数，正对齐使用正数，里面的值为当前所占字符的格子。例如:

            String aaa = String.Format("{0,-30} | {1,-20} | {2,5}", "a", "b", 3);
            String bbb = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaaaaaaaaaaaaaaaaaaaaaa", "b", 3);
            String ccc = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaa", "b", 3);

            int s32_Section45 = 123;
            int ms32_Quadrant = 456;
            string ddd = String.Format("Section: {0}  Quadrant: {1}", s32_Section45, ms32_Quadrant);

            string Name = "李";
            int Age = 2;
            string Address = "吉林";
            richTextBox1.Text += "Name : " + Name + "\tAge : " + Age.ToString() + "\tAddress : " + Address + "\n";

            string Begin = "550";
            string end = "570";
            string sqlstr = string.Format(@"WHERE 总分>{0} AND 总分<{1})", Begin, end);
            richTextBox1.Text += sqlstr + "\n";

            sqlstr = string.Format(@"WHERE 学生姓名 LIKE '{0}%' and 年龄 LIKE '{1}%' and 家庭住址 LIKE '{2}%'", Name, Age, Address);
            richTextBox1.Text += sqlstr + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //動態驗證碼變成靜態
            //將一個gif拆成多圖

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\run.gif";

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

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\id_card_03.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\id_card_01.jpg";

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
                Thread.Sleep(100);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試 PadRight / PadLeft

            int number = 1234;
            richTextBox1.Text += number.ToString() + "\n";
            richTextBox1.Text += number.ToString().PadRight(20, '-') + "\n";
            richTextBox1.Text += number.ToString().PadLeft(20, '-') + "\n";
            richTextBox1.Text += number.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //------------------------------------------------------------  # 60個

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

        [DllImport("kernel32")]
        extern static ulong GetTickCount64();

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試系統開機時間

            //呼叫 Windows API (GetTickCount64)
            //如果你想要更底層的方式，可以透過 P/Invoke 呼叫 Win32 API：

            ulong uptimeMillis = GetTickCount64();
            DateTime bootTime = DateTime.Now - TimeSpan.FromMilliseconds(uptimeMillis);

            Console.WriteLine("系統開機時間: " + bootTime);
            richTextBox1.Text += "系統開機時間: " + bootTime + "\n";

        }

        //局部圖像放大
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            int r = 20;
            int ratio = 2;
            try
            {
                //局部圖像放大                
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
            //測試網路連線狀態


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

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            //往上兩層的檔案
            string filename = Application.StartupPath.ToString();
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

        //------------------------------------------------------------  # 60個

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
                richTextBox1.Text += "文件不存在！\n";
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
                //richTextBox1.Text +=(string)item + ":" + (string)ht[item]);
                richTextBox1.Text += item.ToString() + ":" + ht[item].ToString() + "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //統計英文文本中的單詞數並排序
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\english_text.txt";
            StatisticsWords(filename);
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            char[] bbv = { '蕭', '一', '樓' };
            string abc = "王濬樓船下益州，金陵王氣黯然收。千尋鐵鎖沉江底，一片降幡出石頭。人世幾回傷往事，山形依舊枕寒流。今逢四海為家日，故壘蕭蕭蘆荻秋。";

            int aa = abc.IndexOfAny(bbv);
            int bb = abc.IndexOfAny(bbv, 32);
            int cc = abc.IndexOfAny(bbv, 32, 10);
            int dd = abc.IndexOfAny(bbv, 32, 20);
            int ee = abc.IndexOfAny(bbv, 32, 30);

            richTextBox1.Text += "length of abc = " + abc.Length.ToString() + "\n";
            richTextBox1.Text += "aa = " + aa.ToString() + "\n";
            richTextBox1.Text += "bb = " + bb.ToString() + "\n";
            richTextBox1.Text += "cc = " + cc.ToString() + "\n";
            richTextBox1.Text += "dd = " + dd.ToString() + "\n";
            richTextBox1.Text += "ee = " + ee.ToString() + "\n";

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //一個檔案的英文字母出現的字數統計

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\war_and_peace.txt";

            FileInfo f = new FileInfo(filename);
            StreamReader sr = f.OpenText();

            int[] letter = new int[26];
            int k;
            char ch;
            while (sr.Peek() >= 0)
            {
                ch = (char)sr.Read();
                if (ch >= 'A' && ch <= 'Z')
                {
                    k = (int)ch - 65;
                    letter[k]++;
                }
                else if (ch >= 'a' && ch <= 'z')
                {
                    k = (int)ch - 97;
                    letter[k]++;
                }
            }

            richTextBox1.Text += "== 本檔案 英文字母出現的字數統計如下 : \n";
            for (int i = 0; i < 26; i = i + 2)
            {
                if ((i % 2) == 0)
                {
                    richTextBox1.Text += (char)(65 + i) + ", " + (char)(97 + i) + ", " + letter[i] + "個\t";
                    richTextBox1.Text += (char)(65 + i + 1) + ", " + (char)(97 + i + 1) + ", " + letter[i + 1] + "個\n";
                }
            }
            sr.Close();
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {
            //由檔頭資料找出檔案的真實格式
            richTextBox1.Text += "由檔頭資料找出檔案的真實格式\n";

            Dictionary<string, string> ImageTypes = new Dictionary<string, string>()
            {
            { "FFD8", ".jpg" },
            { "424D", ".bmp" },
            { "474946", ".gif" },
            { "89504E470D0A1A0A", ".png" }
            };

            richTextBox1.Text += "len = " + ImageTypes.Count.ToString() + "\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            string builtHex = string.Empty;
            string ext = string.Empty;
            using (Stream S = File.OpenRead(filename))
            {
                for (int i = 0; i < 8; i++)
                {
                    builtHex += S.ReadByte().ToString("X2");
                    if (ImageTypes.ContainsKey(builtHex))
                    {
                        ext = ImageTypes[builtHex];
                        break;
                    }
                }
            }
            richTextBox1.Text += "取得真實副檔名 : " + ext + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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

                //richTextBox1.Text += de.Key.ToString()+"\n";
                //richTextBox1.Text += de.Value.ToString()+"\n";
            }
        }
        */

        //------------------------------------------------------------  # 60個

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //測試 ErrorProvider
            errorProvider1.BlinkRate = 100;
            errorProvider1.BlinkStyle = ErrorBlinkStyle.AlwaysBlink;
            errorProvider1.SetError(button39, "測試 ErrorProvider");
        }

        //------------------------------------------------------------  # 60個

        private void button25_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button26_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button27_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        static int top = -1;

        public static void Push(int[] stack, int MAX, int val)
        {
            if (top >= MAX - 1)
            {
                //richTextBox1.Text += "[堆疊已經滿了]" + "\n";
            }
            else
            {
                top++;
                stack[top] = val;
            }
        }

        public static int Pop(int[] stack)
        {
            if (top < 0)
            {
                //richTextBox1.Text += "[堆疊已經空了]" + "\n";
            }
            else
            {
                top--;
            }
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
            {
                card[i] = i;
            }
            richTextBox1.Text += "[洗牌中...請稍後!]" + "\n";
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
            richTextBox1.Text += "[逆時針發牌]" + "\n";
            richTextBox1.Text += "[顯示各家牌子]\n 東家\t  北家\t   西家\t    南家" + "\n";
            richTextBox1.Text += "=================================" + "\n";
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
                richTextBox1.Text += "[" + ascVal + (stack[top] % 13 + 1) + "]" + "\n";
                richTextBox1.Text += '\t' + "\n";
                if (top % 4 == 0)
                {
                    richTextBox1.Text += "\n";
                }
                top--;
            }
        }

        //------------------------------------------------------------  # 60個

        private void button29_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button30_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button31_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button32_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button33_Click(object sender, EventArgs e)
        {
            //取得機器名稱
            richTextBox1.Text += "Host name : " + Dns.GetHostName() + "\n";
            try
            {
                // 取得Local主機的識別名稱
                string localHostName = Dns.GetHostName();
                richTextBox1.Text += "localHostName : " + localHostName + "\n";

                //TextBox1.Text = localHostName;
            }
            catch (SocketException ex)
            {
                richTextBox1.Text += ex.StackTrace.ToString() + "\n";
            }

            /*
            //取得IP地址
            IPHostEntry ipEntry = Dns.GetHostByName(localhost);
            IPAddress[] IpAddr = ipEntry.AddressList;
            for (int i = 0; i < IpAddr.Length; i++)
            {
                //Console.WriteLine(IP Address {0}: {1} , i, IpAddr.ToString ());
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + IpAddr.ToString() + "\n";
            }
            */

            /*
            //根據IP地址得出機器名稱
            IPHostEntry ipEntr.Resolve("172.29.9.9");
            richTextBox1.Text += "Host name : "+ ipEntry.HostName+"\n";
            */
        }

        //------------------------------------------------------------  # 60個

        private void button34_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button35_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button36_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button37_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button38_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button39_Click(object sender, EventArgs e)
        {
            //輸出標頭
            String ch = new String('-', 58);
            richTextBox1.Text += ch + "\n";
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            bool status = CheckInternet();

            cnt++;
            if ((cnt % 10) == 0)
            {
                richTextBox1.Text += "網路狀態 : " + status.ToString() + ", 時間 : " + DateTime.Now.ToString() + "\n";
            }

            if (status && lastStatus == false)
            {
                richTextBox1.Text += "✅ 網路已恢復連線, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            else if (!status && lastStatus == true)
            {
                richTextBox1.Text += "⚠️ 網路斷線, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            lastStatus = status;
        }

        private bool CheckInternet()
        {
            try
            {
                using (WebClient client = new WebClient())
                {
                    // 嘗試下載 Google 首頁 (只要能成功就代表有網路)
                    client.DownloadString("https://www.google.com");
                    return true;
                }
            }
            catch
            {
                return false;
            }
        }
    }

    //------------------------------------------------------------  # 60個

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

    //------------------------------------------------------------  # 60個
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

