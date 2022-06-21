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

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            webBrowser1.Size = new Size(640, 240);
            webBrowser1.Location = new Point(x_st + dx * 3, y_st + dy * 6 + 70);

            richTextBox1.Location = new Point(x_st + dx * 7 - 50, y_st + dy * 0);

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

        private string GetStringValue(byte[] Byte)
        {
            string tmpString = "";

            /*
            //1111
            ASCIIEncoding Asc = new ASCIIEncoding();
            tmpString = Asc.GetString(Byte);
            */

            //2222
            int iCounter;
            for (iCounter = 0; iCounter < Byte.Length; iCounter++)
            {
                tmpString = tmpString + Byte[iCounter].ToString();
            }

            return tmpString;
        }
        private byte[] GetKeyByteArray(string strKey)
        {
            ASCIIEncoding Asc = new ASCIIEncoding();
            int tmpStrLen = strKey.Length;
            byte[] tmpByte = new byte[tmpStrLen - 1];
            tmpByte = Asc.GetBytes(strKey);
            return tmpByte;
        }

        /// <summary>
        /// 使用DES加密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="originalValue">待加密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">初始化向量(最大長度8)</param>
        /// <returns>加密後的字符串</returns>
        public string DESEncrypt(string originalValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateEncryptor();
            byt = Encoding.UTF8.GetBytes(originalValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Convert.ToBase64String(ms.ToArray());
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }
        /// <summary>
        /// 使用DES解密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="encryptedValue">待解密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">m初始化向量(最大長度8)</param>
        /// <returns>解密後的字符串</returns>
        public string DESDecrypt(string encryptedValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateDecryptor();
            byt = Convert.FromBase64String(encryptedValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Encoding.UTF8.GetString(ms.ToArray());
        }



        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string initial_data = "12345";
            byte[] tmpByte;
            MD5 md5 = new MD5CryptoServiceProvider();
            tmpByte = md5.ComputeHash(GetKeyByteArray(initial_data));
            md5.Clear();
            string md5_result = GetStringValue(tmpByte);


            richTextBox1.Text += "MD5 = " + md5_result + "\n";



            //byte[] tmpByte;
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            tmpByte = sha1.ComputeHash(GetKeyByteArray(initial_data));
            sha1.Clear();
            string sha1_result = GetStringValue(tmpByte);

            richTextBox1.Text += "SHA1 = " + sha1_result + "\n";


            //byte[] tmpByte;
            SHA256 sha256 = new SHA256Managed();
            tmpByte = sha256.ComputeHash(GetKeyByteArray(initial_data));
            sha256.Clear();
            string sha256_result = GetStringValue(tmpByte);

            richTextBox1.Text += "SHA256 = " + sha256_result + "\n";


            //byte[] tmpByte;
            SHA512 sha512 = new SHA512Managed();
            tmpByte = sha512.ComputeHash(GetKeyByteArray(initial_data));
            sha512.Clear();
            string sha512_result = GetStringValue(tmpByte);
            richTextBox1.Text += "SHA512 = " + sha512_result + "\n";


            string key = "abc";
            string DES_result = DESEncrypt(initial_data, key);
            richTextBox1.Text += "DES Enc = " + DES_result + "\n";


            string DES_decrypt_result = DESDecrypt(DES_result, key, "0");
            richTextBox1.Text += "DES Dec = " + DES_decrypt_result + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //編碼轉換範例

            string string_old = "方法";   //原字串
            string string_by_big5 = "群曜";   //使用 big5 的字串
            string string_by_gb2312 = "醫電"; //使用 gb2312 的字串
            string string_by_utf8 = "股份"; //使用 UTF8 的字串
            string string_by_ascii = "有限"; //使用 ASCII 的字串
            string string_by_default = "公司"; //使用 預設編碼 的字串

            byte[] bytes_big5;      //存放 big5 轉換出來的拜列
            byte[] bytes_gb2312;    //存放 gb2312 轉換出來的拜列
            byte[] bytes_utf8;      //存放 UTF8 轉換出來的拜列
            byte[] bytes_ascii;     //存放 ASCII 轉換出來的拜列
            byte[] bytes_default;   //存放 預設編碼 轉換出來的拜列
            int len = 0;

            richTextBox1.Text += "用gb2312寫\"方法\"二字, 就是寫B7BD B7A8\n";
            //使用gb2312將字串轉成拜列
            bytes_gb2312 = Encoding.GetEncoding("gb2312").GetBytes(string_old);
            len = bytes_gb2312.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\tdata : \t";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += bytes_gb2312[i].ToString("X2");

            }
            richTextBox1.Text += "\n";

            //B7BD B7A8用big5解開, 得到"源楊"二字.
            //用gb2312將拜列解開成字串
            string_by_gb2312 = Encoding.GetEncoding("gb2312").GetString(bytes_gb2312);
            //用big5將拜列解開成字串
            string_by_big5 = Encoding.GetEncoding("big5").GetString(bytes_gb2312);

            richTextBox1.Text += "拜列用gb2312解開 : \t" + string_by_gb2312 + "\t正確\n";
            //B7BD B7A8用big5解開, 得到"源楊"二字.
            richTextBox1.Text += "拜列用big解開 : \t" + string_by_big5 + "\t錯誤\n";



            //以下就不展開了

            //使用UTF8將字串轉成拜列
            bytes_utf8 = Encoding.UTF8.GetBytes(string_by_utf8);
            //用UTF8將拜列解開成字串
            string string_by_utf8_new = Encoding.UTF8.GetString(bytes_utf8);

            //使用ASCII將字串轉成拜列
            bytes_ascii = Encoding.ASCII.GetBytes(string_by_ascii);
            //用ASCII將拜列解開成字串
            string string_by_ascii_new = Encoding.ASCII.GetString(bytes_ascii);

            //使用預設編碼將字串轉成拜列
            bytes_default = Encoding.Default.GetBytes(string_by_default);
            //用預設編碼將拜列解開成字串
            string string_by_default_new = Encoding.Default.GetString(bytes_default);





            //在 C# 中使用 BitConverter.ToString() 方法將字串轉換為十六進位制
            string decString = "0123456789";
            byte[] bytes = Encoding.Default.GetBytes(decString);
            string hexString = BitConverter.ToString(bytes);
            hexString = hexString.Replace("-", "");
            Console.WriteLine(hexString);
            richTextBox1.Text += hexString + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            richTextBox1.Text += "測試移除邊緣\n";

            string filename = @"C:\______test_files\picture1.jpg";

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int i;
            int j;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    byte ggg = bitmap1.GetPixel(i, j).G;
                    byte bbb = bitmap1.GetPixel(i, j).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(i, j, zz);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string strServiceName = string.Empty;


            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";


            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

            //使用WMI取得USB資訊

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = mos.Get();
            var usbList = from u in collection.Cast<ManagementBaseObject>()
                          select new
                          {
                              id = u.GetPropertyValue("DeviceID"),
                              name = u.GetPropertyValue("Name"),
                              status = u.GetPropertyValue("Status"),
                              system = u.GetPropertyValue("SystemName"),
                              caption = u.GetPropertyValue("Caption"),
                              pnp = u.GetPropertyValue("PNPDeviceID"),
                              description = u.GetPropertyValue("Description")
                          };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }




        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //Image Cut
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
        public static void Cut(string filename1, string filename2, int width, int height, string message)
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
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //clone 範例
            /*
            在Bitmap中可以找到

            Clone（）方法，該方法有三個重載方法。
            Clone（）
            Clone（Rectangle， PixelFormat）
            Clone（RectangleF， PixelFormat）
            */

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            Bitmap bitmap2 = (Bitmap)bitmap1.Clone();

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            Rectangle rect = new Rectangle(w / 2, h / 2, w / 2, h / 2);

            //Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, PixelFormat.Format32bppArgb);    //same
            Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, bitmap1.PixelFormat);

            pictureBox1.Image = bitmap3;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //抓屏將生成的圖片顯示在pictureBox

            Image image = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

            Graphics g = Graphics.FromImage(image);

            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));

            //IntPtr dc1 = g.GetHdc();      //此處這兩句多餘，具體看最後GetHdc()定義

            //g.ReleaseHdc(dc1);           

            g.Dispose();

            this.pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            this.pictureBox1.Image = image;
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

            //獲得處理器參數程序代碼
            get_ProcessorInfo();
        }

        void get_ProcessorInfo()
        {
            string[] 制造商;
            string[] 型號;
            string[] 序列號;

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            制造商 = new string[mos.Get().Count];
            型號 = new string[mos.Get().Count];
            序列號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                    序列號[i] = mo.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "制造商[" + i.ToString() + "] : " + 制造商[i].ToString() + "\n";
                    richTextBox1.Text += "序列號[" + i.ToString() + "] : " + 序列號[i].ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
                i++;
            }
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
                Graphics graphics = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
                //聲明兩個Rectangle對象，分別用來指定要放大的區域和放大后的區域
                Rectangle sourceRectangle = new Rectangle(e.X - r, e.Y - r, r * 2, r * 2);	//要放大的區域 
                Rectangle destRectangle = new Rectangle(e.X - r * ratio, e.Y - r * ratio, r * 2 * ratio, r * 2 * ratio);
                //調用DrawImage方法對選定區域進行重新繪制，以放大該部分
                graphics.DrawImage(bitmap1, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch { }

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //昨天在給豆瓣電台加皮膚功能的時候考慮的，需要遍歷圖像的每個像素，然後算出均值。
            //如果圖片比較暗，那麼文字就變成白色的，如果圖片比較亮，文字就變成黑色的。
            //直接在C#用計算這樣的計算是需要付出一定性能代價的（相比非托管代碼），而且圖片越大，性能損耗就越嚴重。
            //所以考慮把這部分代碼寫到unsafe語句中，讓它在內存裡直接計算。

            string filename = @"C:\______test_files\picture1.jpg";

            Bitmap image = new Bitmap(filename);

            BitmapData data = image.LockBits(

            new Rectangle(0, 0, image.Width, image.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                long r = 0;
                long g = 0;
                long b = 0;
                long pixelCount = data.Height * data.Width;

                byte* ptr = (byte*)(data.Scan0);

                for (int i = 0; i < data.Height; i++)
                {
                    for (int j = 0; j < data.Width; j++)
                    {
                        r += *ptr;
                        g += *(ptr + 1);
                        b += *(ptr + 2);
                        ptr += 3;
                    } ptr += data.Stride - data.Width * 3;
                }

                double totalRGB = (r / pixelCount + g / pixelCount + b / pixelCount) / 3;

                if (totalRGB > 127)
                {
                    this.BackColor = Color.FromArgb(0, 0, 0);
                }
                else
                {
                    this.BackColor = Color.FromArgb(255, 2552, 55);
                }
            }
        }

        string getVid(string url)
        {
            string strRegex = "(?<=id_)(\\w+)";
            Regex reg = new Regex(strRegex);
            Match match = reg.Match(url);
            return match.ToString();
        }

        private void button11_Click(object sender, EventArgs e)
        {

            string url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
            string vid = getVid(url);
            richTextBox1.Text += "vid : " + vid + "\n";
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
            /// 利用C#來解讀MP3文件的TAG區信息。
            //string mp3_filename = @"C:\______test_files\_mp3\aaaa.mp3";

            // TBD
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //表單預設參數
            richTextBox1.Text += "AAA = " + SystemInformation.FrameBorderSize.Width.ToString() + "\n";  //8
            richTextBox1.Text += "BBB = " + SystemInformation.FrameBorderSize.Height.ToString() + "\n"; //8
            richTextBox1.Text += "CCC = " + SystemInformation.CaptionHeight.ToString() + "\n";          //23
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

        private void button20_Click(object sender, EventArgs e)
        {
            //從windows剪貼板獲取內容

            //從windows剪貼板獲取內容
            IDataObject iData = Clipboard.GetDataObject();
            if (iData.GetDataPresent(DataFormats.Text))
            {
                richTextBox1.Text += "取得文字:\n";
                Console.WriteLine((String)iData.GetData(DataFormats.Text));
            }
            if (iData.GetDataPresent(DataFormats.Bitmap))
            {
                richTextBox1.Text += "取得圖片\n";
                Image img = (Bitmap)iData.GetData(DataFormats.Bitmap);
                //pictureBox1.Image = img;
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

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



    public class clsMP3TAG
    {
        private byte[] TAGBody = new byte[128];

        private byte[] sTag = new byte[3];
        private byte[] sTitle = new byte[30];
        private byte[] sArtist = new byte[30];
        private byte[] sAlbum = new byte[30];
        private byte[] sYear = new byte[4];
        private byte[] sComment = new byte[30];
        private byte[] sGenre = new byte[1];

        System.Exception myException;

        public clsMP3TAG(byte[] TAG)
        {
            if (TAG.Length != 128)
            {
                myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG長度應該是 128 Byte。");
                throw (myException);
            }
            else
            {
                Array.Copy(TAG, 0, sTag, 0, 3);
                if (!Encoding.Default.GetString(sTag).Equals("TAG"))
                {
                    myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG位校驗出錯。");
                    throw (myException);
                }

                Array.Copy(TAG, 3, sTitle, 0, 30);
                Array.Copy(TAG, 33, sArtist, 0, 30);
                Array.Copy(TAG, 63, sAlbum, 0, 30);
                Array.Copy(TAG, 93, sYear, 0, 4);
                Array.Copy(TAG, 97, sComment, 0, 30);
                Array.Copy(TAG, 127, sGenre, 0, 1);


            }
        }

        /**/
        //////////////////////////////////////////////////////
        /// 以下是屬性，只讀
        //////////////////////////////////////////////////////
        public string Title
        {
            get
            {
                return Encoding.Default.GetString(sTitle);
            }
        }

        public string Artist
        {
            get
            {
                return Encoding.Default.GetString(sArtist);
            }
        }

        public string Album
        {
            get
            {
                return Encoding.Default.GetString(sAlbum);
            }
        }

        public string Year
        {
            get
            {
                return Encoding.Default.GetString(sYear);
            }
        }

        public string Comment
        {
            get
            {
                return Encoding.Default.GetString(sComment);
            }
        }

        public string Genre
        {
            get
            {
                switch (Convert.ToInt16(sGenre[0]))
                {
                    case 0: return "Blues";
                    case 20: return "Alternative";
                    case 40: return "AlternRock";
                    case 60: return "Top 40";
                    case 1: return "Classic Rock";
                    case 21: return "Ska";
                    case 41: return "Bass";
                    case 61: return "Christian Rap";
                    case 2: return "Country";
                    case 22: return "Death Metal";
                    case 42: return "Soul";
                    case 62: return "Pop/Funk";
                    case 3: return "Dance";
                    case 23: return "Pranks";
                    case 43: return "Punk";
                    case 63: return "Jungle";
                    case 4: return "Disco";
                    case 24: return "Soundtrack";
                    case 44: return "Space";
                    case 64: return "Native American";
                    case 5: return "Funk";
                    case 25: return "Euro-Techno";
                    case 45: return "Meditative";
                    case 65: return "Cabaret";
                    case 6: return "Grunge";
                    case 26: return "AmbIEnt";
                    case 46: return "Instrumental Pop";
                    case 66: return "New Wave";
                    case 7: return "Hip-Hop";
                    case 27: return "Trip-Hop";
                    case 47: return "Instrumental Rock";
                    case 67: return "Psychadelic";
                    case 8: return "Jazz";
                    case 28: return "Vocal";
                    case 48: return "Ethnic";
                    case 68: return "Rave";
                    case 9: return "Metal";
                    case 29: return "Jazz+Funk";
                    case 49: return "Gothic";
                    case 69: return "Showtunes";
                    case 10: return "New Age";
                    case 30: return "Fusion";
                    case 50: return "Darkwave";
                    case 70: return "Trailer";
                    case 11: return "OldIEs";
                    case 31: return "Trance";
                    case 51: return "Techno-Industrial";
                    case 71: return "Lo-Fi";
                    case 12: return "Other";
                    case 32: return "Classical";
                    case 52: return "Electronic";
                    case 72: return "Tribal";
                    case 13: return "Pop";
                    case 33: return "Instrumental";
                    case 53: return "Pop-Folk";
                    case 73: return "Acid Punk";
                    case 14: return "R&B";
                    case 34: return "Acid";
                    case 54: return "Eurodance";
                    case 74: return "Acid Jazz";
                    case 15: return "Rap";
                    case 35: return "House";
                    case 55: return "Dream";
                    case 75: return "Polka";
                    case 16: return "Reggae";
                    case 36: return "Game";
                    case 56: return "Southern Rock";
                    case 76: return "Retro";
                    case 17: return "Rock";
                    case 37: return "Sound Clip";
                    case 57: return "Comedy";
                    case 77: return "Musical";
                    case 18: return "Techno";
                    case 38: return "Gospel";
                    case 58: return "Cult";
                    case 78: return "Rock & Roll";
                    case 19: return "Industrial";
                    case 39: return "Noise";
                    case 59: return "Gangsta";
                    case 79: return "Hard Rock";


                    default:
                        return "未知類型";
                }
            }
        }
    }
}




