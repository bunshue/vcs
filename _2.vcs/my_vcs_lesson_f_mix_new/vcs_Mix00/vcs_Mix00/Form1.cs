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
using System.Drawing.Imaging;
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
        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定义鼠标 
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

            show_item_location();

            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


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
            dx = 180;
            dy = 80;

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

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            webBrowser1.Size = new Size(640, 240);
            webBrowser1.Location = new Point(x_st + dx * 1, y_st + dy * 6 + 70);

            richTextBox1.Location = new Point(x_st + dx * 5 - 50, y_st + dy * 0);

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
            //長方形的Contains功能
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawRectangle(Pens.Red, 100, 100, 150, 150);
            Rectangle rec = new Rectangle(100, 100, 150, 150);
            Point pt1 = new Point(180, 180);
            Point pt2 = new Point(280, 280);
            g.FillEllipse(Brushes.Green, pt1.X, pt1.Y, 20, 20);
            g.FillEllipse(Brushes.Red, pt2.X, pt2.Y, 20, 20);

            if (rec.Contains(pt1))
            {
                richTextBox1.Text += "pt1 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt1 在 rec 之外\n";
            }

            if (rec.Contains(pt2))
            {
                richTextBox1.Text += "pt2 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt2 在 rec 之外\n";
            }

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


            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定义鼠标 

            //使用WMI取得USB資訊

            ManagementObjectSearcher search = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = search.Get();
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
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }


        string strCode;
        ArrayList alLinks;
        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //抓取網頁裡面的所有鏈接

            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190697.html";
            if (url.Substring(0, 7) != @"http://")
            {
                url = @"http://" + url;
            }
            MessageBox.Show("正在獲取頁面代碼，請稍後...");
            strCode = GetPageSource(url);
            MessageBox.Show("正在提取超鏈接，請稍侯...");
            alLinks = GetHyperLinks(strCode);
            MessageBox.Show("正在寫入文件，請稍侯...");
            WriteToXml(url, alLinks);
        }

        // 獲取指定網頁的HTML代碼
        public static string GetPageSource(string URL)
        {
            Uri uri = new Uri(URL);

            HttpWebRequest hwReq = (HttpWebRequest)WebRequest.Create(uri);
            HttpWebResponse hwRes = (HttpWebResponse)hwReq.GetResponse();

            hwReq.Method = "Get";

            hwReq.KeepAlive = false;

            StreamReader reader = new StreamReader(hwRes.GetResponseStream(), System.Text.Encoding.GetEncoding("GB2312"));

            return reader.ReadToEnd();
        }

        // 提取HTML代碼中的網址
        public static ArrayList GetHyperLinks(string htmlCode)
        {
            ArrayList al = new ArrayList();

            string strRegex = @"http://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?";

            Regex r = new Regex(strRegex, RegexOptions.IgnoreCase);
            MatchCollection m = r.Matches(htmlCode);

            for (int i = 0; i <= m.Count - 1; i++)
            {
                bool rep = false;
                string strNew = m[i].ToString();

                // 過濾重復的URL
                foreach (string str in al)
                {
                    if (strNew == str)
                    {
                        rep = true;
                        break;
                    }
                }

                if (!rep) al.Add(strNew);
            }

            al.Sort();

            return al;
        }

        // 把網址寫入xml文件
        static void WriteToXml(string strURL, ArrayList alHyperLinks)
        {
            XmlTextWriter writer = new XmlTextWriter("HyperLinks.xml", Encoding.UTF8);

            writer.Formatting = Formatting.Indented;
            writer.WriteStartDocument(false);
            writer.WriteDocType("HyperLinks", null, "urls.dtd", null);
            writer.WriteComment("提取自" + strURL + "的超鏈接");
            writer.WriteStartElement("HyperLinks");
            writer.WriteStartElement("HyperLinks", null);
            writer.WriteAttributeString("DateTime", DateTime.Now.ToString());


            foreach (string str in alHyperLinks)
            {
                string title = GetDomain(str);
                string body = str;
                writer.WriteElementString(title, null, body);
            }

            writer.WriteEndElement();
            writer.WriteEndElement();

            writer.Flush();
            writer.Close();
        }

        // 獲取網址的域名後綴
        static string GetDomain(string strURL)
        {
            string retVal;

            string strRegex = @"(\.com/|\.net/|\.cn/|\.org/|\.gov/)";

            Regex r = new Regex(strRegex, RegexOptions.IgnoreCase);
            Match m = r.Match(strURL);
            retVal = m.ToString();

            strRegex = @"\.|/$";
            retVal = Regex.Replace(retVal, strRegex, "").ToString();

            if (retVal == "")
                retVal = "other";

            return retVal;
        }
        





        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //根據url獲取遠程html源碼
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190697.html";
            string result = GetSearchHtml(url);
            richTextBox1.Text += result + "\n";

        }

        /// <summary>
        /// 根據url獲取遠程html源碼
        /// </summary>
        /// <param name="url">搜索url</param>
        /// <returns>返回DownloadData</returns>
        public static string GetSearchHtml(string url)
        {
            WebClient MyWebClient = new WebClient();
            MyWebClient.Credentials = CredentialCache.DefaultCredentials;   //獲取或設置用於對向Internet資源的請求進行身份驗證的網絡憑據。
            Byte[] pageData = MyWebClient.DownloadData(url);                //從指定url下載數據
            return Encoding.UTF8.GetString(pageData);                       //獲取網站頁面采用的是UTF-8
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
                Cursor.Current = myCursor;								//定义鼠标
                Graphics graphics = pictureBox1.CreateGraphics();				//实例化pictureBox1控件的Graphics类
                //声明两个Rectangle对象，分别用来指定要放大的区域和放大后的区域
                Rectangle sourceRectangle = new Rectangle(e.X - r, e.Y - r, r * 2, r * 2);	//要放大的区域 
                Rectangle destRectangle = new Rectangle(e.X - r * ratio, e.Y - r * ratio, r * 2 * ratio, r * 2 * ratio);
                //调用DrawImage方法对选定区域进行重新绘制，以放大该部分
                graphics.DrawImage(bitmap1, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch { }

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
}
