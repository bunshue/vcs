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


            _serialNumber.Clear();
            matchDriveLetterWithSerial();
            richTextBox1.Text += "len = " + _serialNumber.Count.ToString() + "\n";

            int len = _serialNumber.Count;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得序號 : " + _serialNumber[i] + "\n";

            }
        }


        //讀取U盤序列號


        private List<string> _serialNumber = new List<string>();

        /// <summary>
        /// 調用這個函數將本機所有U盤序列號存儲到_serialNumber中
        /// </summary>
        private void matchDriveLetterWithSerial()
        {
            string[] diskArray;
            string driveNumber;
            var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
            foreach (ManagementObject dm in searcher.Get())
            {
                getValueInQuotes(dm["Dependent"].ToString());
                diskArray = getValueInQuotes(dm["Antecedent"].ToString()).Split(',');
                driveNumber = diskArray[0].Remove(0, 6).Trim();
                var disks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
                foreach (ManagementObject disk in disks.Get())
                {
                    if (disk["Name"].ToString() == ("\\\\.\\PHYSICALDRIVE" + driveNumber) & disk["InterfaceType"].ToString() == "USB")
                    {
                        _serialNumber.Add(parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()));
                    }
                }
            }
        }
        private static string parseSerialFromDeviceID(string deviceId)
        {
            var splitDeviceId = deviceId.Split('\\');
            var arrayLen = splitDeviceId.Length - 1;
            var serialArray = splitDeviceId[arrayLen].Split('&');
            var serial = serialArray[0];
            return serial;
        }

        private static string getValueInQuotes(string inValue)
        {
            var posFoundStart = inValue.IndexOf("\"");
            var posFoundEnd = inValue.IndexOf("\"", posFoundStart + 1);
            var parsedValue = inValue.Substring(posFoundStart + 1, (posFoundEnd - posFoundStart) - 1);
            return parsedValue;
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
            string filename = @"C:\______test_files\red.bmp";

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            Rectangle rect = new Rectangle(100, 100, 20, 20);
            BitmapData data = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int w = data.Width;
            int h = data.Height;

            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            unsafe
            {
                long r = 0;
                long g = 0;
                long b = 0;
                long pixelCount = h * w;

                byte* ptr = (byte*)(data.Scan0);

                for (int i = 0; i < h; i++)
                {
                    for (int j = 0; j < w; j++)
                    {
                        //排列是BGR
                        b += *ptr;
                        g += *(ptr + 1);
                        r += *(ptr + 2);
                        ptr += 3;
                    }
                    ptr += data.Stride - w * 3;
                }

                double totalRGB = (r / pixelCount + g / pixelCount + b / pixelCount) / 3;

                richTextBox1.Text += "平均 R : " + (r / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 G : " + (g / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 B : " + (b / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均亮度 : " + totalRGB.ToString() + "\n";
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
            //Md5和Sha1两种加密方式

            const string s = "123456";
            Console.WriteLine("密码：" + s);

            Console.WriteLine("Md5：" + s.Md5());
            Console.WriteLine("长度：" + s.Md5().Length);

            Console.WriteLine("Sha1：" + s.Sha1());
            Console.WriteLine("长度：" + s.Sha1().Length);


            richTextBox1.Text += "密码：" + s + "\n";

            richTextBox1.Text += "Md5：" + s.Md5() + "\n";
            richTextBox1.Text += "长度：" + s.Md5().Length + "\n";

            richTextBox1.Text += "Sha1：" + s.Sha1() + "\n";
            richTextBox1.Text += "长度：" + s.Sha1().Length + "\n";


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
            int[] gray = new int[220];
            gray[0] = 4;
            gray[1] = 6;
            gray[2] = 9;
            gray[3] = 11;
            gray[4] = 14;
            gray[5] = 16;
            gray[6] = 18;
            gray[7] = 20;
            gray[8] = 22;
            gray[9] = 24;
            gray[10] = 26;
            gray[11] = 28;
            gray[12] = 30;
            gray[13] = 32;
            gray[14] = 33;
            gray[15] = 35;
            gray[16] = 37;
            gray[17] = 38;
            gray[18] = 40;
            gray[19] = 41;
            gray[20] = 43;
            gray[21] = 44;
            gray[22] = 46;
            gray[23] = 47;
            gray[24] = 49;
            gray[25] = 50;
            gray[26] = 51;
            gray[27] = 53;
            gray[28] = 54;
            gray[29] = 55;
            gray[30] = 57;
            gray[31] = 58;
            gray[32] = 59;
            gray[33] = 61;
            gray[34] = 62;
            gray[35] = 63;
            gray[36] = 65;
            gray[37] = 66;
            gray[38] = 67;
            gray[39] = 68;
            gray[40] = 70;
            gray[41] = 71;
            gray[42] = 72;
            gray[43] = 73;
            gray[44] = 74;
            gray[45] = 75;
            gray[46] = 77;
            gray[47] = 78;
            gray[48] = 79;
            gray[49] = 80;
            gray[50] = 81;
            gray[51] = 82;
            gray[52] = 83;
            gray[53] = 84;
            gray[54] = 85;
            gray[55] = 86;
            gray[56] = 87;
            gray[57] = 88;
            gray[58] = 89;
            gray[59] = 90;
            gray[60] = 91;
            gray[61] = 92;
            gray[62] = 93;
            gray[63] = 94;
            gray[64] = 95;
            gray[65] = 96;
            gray[66] = 97;
            gray[67] = 98;
            gray[68] = 99;
            gray[69] = 99;
            gray[70] = 100;
            gray[71] = 101;
            gray[72] = 102;
            gray[73] = 103;
            gray[74] = 103;
            gray[75] = 104;
            gray[76] = 105;
            gray[77] = 106;
            gray[78] = 106;
            gray[79] = 107;
            gray[80] = 108;
            gray[81] = 109;
            gray[82] = 109;
            gray[83] = 110;
            gray[84] = 111;
            gray[85] = 111;
            gray[86] = 112;
            gray[87] = 113;
            gray[88] = 113;
            gray[89] = 114;
            gray[90] = 115;
            gray[91] = 115;
            gray[92] = 116;
            gray[93] = 116;
            gray[94] = 117;
            gray[95] = 118;
            gray[96] = 118;
            gray[97] = 119;
            gray[98] = 119;
            gray[99] = 120;
            gray[100] = 120;
            gray[101] = 121;
            gray[102] = 122;
            gray[103] = 122;
            gray[104] = 123;
            gray[105] = 123;
            gray[106] = 124;
            gray[107] = 124;
            gray[108] = 125;
            gray[109] = 125;
            gray[110] = 126;
            gray[111] = 126;
            gray[112] = 127;
            gray[113] = 127;
            gray[114] = 128;
            gray[115] = 128;
            gray[116] = 129;
            gray[117] = 129;
            gray[118] = 130;
            gray[119] = 130;
            gray[120] = 130;
            gray[121] = 131;
            gray[122] = 131;
            gray[123] = 132;
            gray[124] = 132;
            gray[125] = 133;
            gray[126] = 133;
            gray[127] = 134;
            gray[128] = 134;
            gray[129] = 134;
            gray[130] = 135;
            gray[131] = 135;
            gray[132] = 136;
            gray[133] = 136;
            gray[134] = 140;
            gray[135] = 143;
            gray[136] = 145;
            gray[137] = 149;
            gray[138] = 151;
            gray[139] = 153;
            gray[140] = 156;
            gray[141] = 159;
            gray[142] = 161;
            gray[143] = 163;
            gray[144] = 165;
            gray[145] = 168;
            gray[146] = 169;
            gray[147] = 171;
            gray[148] = 173;
            gray[149] = 176;
            gray[150] = 179;
            gray[151] = 182;
            gray[152] = 184;
            gray[153] = 187;
            gray[154] = 189;
            gray[155] = 191;
            gray[156] = 193;
            gray[157] = 196;
            gray[158] = 197;
            gray[159] = 199;
            gray[160] = 200;
            gray[161] = 202;
            gray[162] = 203;
            gray[163] = 204;
            gray[164] = 206;
            gray[165] = 207;
            gray[166] = 209;
            gray[167] = 211;
            gray[168] = 212;
            gray[169] = 214;
            gray[170] = 215;
            gray[171] = 216;
            gray[172] = 217;
            gray[173] = 218;
            gray[174] = 219;
            gray[175] = 219;
            gray[176] = 220;
            gray[177] = 220;
            gray[178] = 221;
            gray[179] = 221;
            gray[180] = 221;
            gray[181] = 222;
            gray[182] = 222;
            gray[183] = 223;
            gray[184] = 223;
            gray[185] = 223;
            gray[186] = 223;
            gray[187] = 224;
            gray[188] = 224;
            gray[189] = 223;
            gray[190] = 224;
            gray[191] = 224;
            gray[192] = 225;
            gray[193] = 225;
            gray[194] = 225;
            gray[195] = 225;
            gray[196] = 226;
            gray[197] = 226;
            gray[198] = 226;
            gray[199] = 226;
            gray[200] = 226;
            gray[201] = 226;
            gray[202] = 226;
            gray[203] = 226;
            gray[204] = 226;
            gray[205] = 226;
            gray[206] = 226;
            gray[207] = 226;
            gray[208] = 226;
            gray[209] = 226;
            gray[210] = 226;
            gray[211] = 226;
            gray[212] = 226;
            gray[213] = 226;
            gray[214] = 226;
            gray[215] = 226;
            gray[216] = 226;
            gray[217] = 226;
            gray[218] = 226;
            gray[219] = 226;

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 256);
            Point[] curvePoints = new Point[220];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 220; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = 255 - (gray[i]);
            }


            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線


        }

        private void button21_Click(object sender, EventArgs e)
        {
            //string.Format 格式化日期

            //c# 日期函數

            DateTime dt = DateTime.Now;

            richTextBox1.Text += "日期 1:\t" + dt.ToString() + "\n";//2005-11-5 13:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToFileTime().ToString() + "\n";//127756416859912816
            richTextBox1.Text += "日期 1:\t" + dt.ToFileTimeUtc().ToString() + "\n";//127756704859912816
            richTextBox1.Text += "日期 1:\t" + dt.ToLocalTime().ToString() + "\n";//2005-11-5 21:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToLongDateString().ToString() + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.ToLongTimeString().ToString() + "\n";//13:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToOADate().ToString() + "\n";//38661.5565508218
            richTextBox1.Text += "日期 1:\t" + dt.ToShortDateString().ToString() + "\n";//2005-11-5
            richTextBox1.Text += "日期 1:\t" + dt.ToShortTimeString().ToString() + "\n";//13:21
            richTextBox1.Text += "日期 1:\t" + dt.ToUniversalTime().ToString() + "\n";//2005-11-5 5:21:25

            //?2005-11-5 13:30:28.4412864
            richTextBox1.Text += "日期 1:\t" + dt.Year.ToString() + "\n";//2005
            richTextBox1.Text += "日期 1:\t" + dt.Date.ToString() + "\n";//2005-11-5 0:00:00
            richTextBox1.Text += "日期 1:\t" + dt.DayOfWeek.ToString() + "\n";//Saturday
            richTextBox1.Text += "日期 1:\t" + dt.DayOfYear.ToString() + "\n";//309
            richTextBox1.Text += "日期 1:\t" + dt.Hour.ToString() + "\n";//13
            richTextBox1.Text += "日期 1:\t" + dt.Millisecond.ToString() + "\n";//441
            richTextBox1.Text += "日期 1:\t" + dt.Minute.ToString() + "\n";//30
            richTextBox1.Text += "日期 1:\t" + dt.Month.ToString() + "\n";//11
            richTextBox1.Text += "日期 1:\t" + dt.Second.ToString() + "\n";//28
            richTextBox1.Text += "日期 1:\t" + dt.Ticks.ToString() + "\n";//632667942284412864
            richTextBox1.Text += "日期 1:\t" + dt.TimeOfDay.ToString() + "\n";//13:30:28.4412864
            richTextBox1.Text += "日期 1:\t" + dt.ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += "日期 1:\t" + dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += "日期 1:\t" + dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += "日期 1:\t" + dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.CompareTo(dt).ToString() + "\n";//0
            //richTextBox1.Text +="日期 1:\t"+ dt.Add(?).ToString()+"\n";//問號為一個時間段

            richTextBox1.Text += "日期 1:\t" + dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += "日期 1:\t" + dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += "日期 1:\t" + dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += "日期 1:\t" + dt.GetType().ToString() + "\n";//System.DateTime
            richTextBox1.Text += "日期 1:\t" + dt.GetTypeCode().ToString() + "\n";//DateTime

            /*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(s)[0].ToString() + "\n";//2005-11-05T14:06:25
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(t)[0].ToString() + "\n";//14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(y)[0].ToString() + "\n";//2005年11月
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[0].ToString() + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[1].ToString() + "\n";//2005 11 05
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[2].ToString() + "\n";//星期六 2005 11 05
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[3].ToString() + "\n";//星期六 2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(M)[0].ToString() + "\n";//11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(f)[0].ToString() + "\n";//2005年11月5* 14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(g)[0].ToString() + "\n";//2005-11-5 14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(r)[0].ToString() + "\n";//Sat, 05 Nov 2005 14:06:25 GMT
            */

            /*
            或者dt.ToString("yyyy年MM月dd*");//2005年11月5*
            dt.ToString("yyyy-MM-dd");//2005-11-5*
            以此類推……
            */

            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:d｝", dt) + "\n";//2005-11-5
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:D｝", dt) + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:f｝", dt) + "\n";//2005年11月5* 14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:F｝", dt) + "\n";//2005年11月5* 14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:g｝", dt) + "\n";//2005-11-5 14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:G｝", dt) + "\n";//2005-11-5 14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:M｝", dt) + "\n";//11月5*
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:R｝", dt) + "\n";//Sat, 05 Nov 2005 14:23:23 GMT
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:s｝", dt) + "\n";//2005-11-05T14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:t｝", dt) + "\n";//14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:T｝", dt) + "\n";//14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:u｝", dt) + "\n";//2005-11-05 14:23:23Z
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:U｝", dt) + "\n";//2005年11月5* 6:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:Y｝", dt) + "\n";//2005年11月
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0｝", dt) + "\n";//2005-11-5 14:23:23?
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:yyyyMMddHHmmssffff｝", dt) + "\n";
            //yyyymm等可以設置,比如Label16.Text = string.Format("｛0:yyyyMMdd｝",dt)+"\n";
            //綁定也適用:例:<%# string.Format("｛0:yyyy.MM.dd｝",eval_r("sj"))%>
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //代碼統計

            string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_f_mix_new\vcs_Mix00\vcs_Mix00\Form1.cs";
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
            string str ="10/3";
            float result = Calculator.dealWith(str);
            richTextBox1.Text += str + " = " + result.ToString() + "\n";


        }

        private void button24_Click(object sender, EventArgs e)
        {
            string random_chinese_word = CreateCode(10);
            richTextBox1.Text += random_chinese_word + "\n";

        }

        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼

        /// <summary>
        /// 隨機生成漢字
        /// </summary>
        /// <param name="strlength">長度（4位）</param>
        /// <returns></returns>
        public string CreateCode(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素
            string[] r = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };
            Random rnd = new Random();
            //定義一個object數組用來
            object[] bytes = new object[strlength];
            /**/
            /*每循環一次產生一個含兩個元素的十六進制字節數組，並將其放入bject數組中
            每個漢字有四個區位碼組成
            區位碼第1位和區位碼第2位作為字節數組第一個元素
            區位碼第3位和區位碼第4位作為字節數組第二個元素
            */
            for (int i = 0; i < strlength; i++)
            {
                //區位碼第1位
                int r1 = rnd.Next(11, 14);
                string str_r1 = r[r1].Trim();
                //區位碼第2位
                rnd = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);//更換隨機數發生器的種子避免產生重復值
                int r2;
                if (r1 == 13)
                    r2 = rnd.Next(0, 7);
                else
                    r2 = rnd.Next(0, 16);
                string str_r2 = r[r2].Trim();
                //區位碼第3位
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);
                int r3 = rnd.Next(10, 16);
                string str_r3 = r[r3].Trim();
                //區位碼第4位
                rnd = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);
                int r4;
                if (r3 == 10)
                {
                    r4 = rnd.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rnd.Next(0, 15);
                }
                else
                {
                    r4 = rnd.Next(0, 16);
                }
                string str_r4 = r[r4].Trim();
                //定義兩個字節變量存儲產生的隨機漢字區位碼
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //將兩個字節變量存儲在字節數組中
                byte[] str_r = new byte[] { byte1, byte2 };
                //將產生的一個漢字的字節數組放入object數組中
                bytes.SetValue(str_r, i);
            }


            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //根據漢字編碼的字節數組解碼出中文漢字

            string txt = string.Empty;

            for (int i = 0; i < strlength; i++)
            {
                string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));
                txt += str1;
            }
            return txt;
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

        public System.Drawing.PointF Location
        {
            get { return this._location; }
            set { this._location = value; }
        }

        public float Height
        {
            get { return this._height; }
            set { this._height = value; }
        }

        public System.Drawing.Drawing2D.GraphicsPath GraphicsPath
        {
            get
            {
                //this._graphicsPath = this.RetrieveGraphicsPath();
                return this._graphicsPath;
            }
            set { this._graphicsPath = value; }
        }

        public System.Drawing.Color Color
        {
            get { return this._color; }
            set { this._color = value; }
        }

        public float BorderWidth
        {
            get { return this._borderWidth; }
            set { this._borderWidth = value; }
        }

        public System.Drawing.Color BorderColor
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

    public static class EncryptHelper
    {
        /// <summary>
        /// 基于Md5的自定义加密字符串方法：输入一个字符串，返回一个由32个字符组成的十六进制的哈希散列（字符串）。
        /// </summary>
        /// <param name="str">要加密的字符串</param>
        /// <returns>加密后的十六进制的哈希散列（字符串）</returns>
        public static string Md5(this string str)
        {
            //将输入字符串转换成字节数组
            var buffer = Encoding.Default.GetBytes(str);
            //接着，创建Md5对象进行散列计算
            var data = MD5.Create().ComputeHash(buffer);

            //创建一个新的Stringbuilder收集字节
            var sb = new StringBuilder();

            //遍历每个字节的散列数据
            foreach (var t in data)
            {
                //格式每一个十六进制字符串
                sb.Append(t.ToString("X2"));
            }

            //返回十六进制字符串
            return sb.ToString();
        }

        /// <summary>
        /// 基于Sha1的自定义加密字符串方法：输入一个字符串，返回一个由40个字符组成的十六进制的哈希散列（字符串）。
        /// </summary>
        /// <param name="str">要加密的字符串</param>
        /// <returns>加密后的十六进制的哈希散列（字符串）</returns>
        public static string Sha1(this string str)
        {
            var buffer = Encoding.UTF8.GetBytes(str);
            var data = SHA1.Create().ComputeHash(buffer);

            var sb = new StringBuilder();
            foreach (var t in data)
            {
                sb.Append(t.ToString("X2"));
            }

            return sb.ToString();
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
}
