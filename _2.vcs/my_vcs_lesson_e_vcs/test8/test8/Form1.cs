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
using System.Xml;
using System.Management;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

using System.IO.Ports;
using System.Threading;
using System.Security;
using System.Security.Cryptography;
using System.Media;     //for SoundPlayer

using Shell32;
using Microsoft.Win32;  //for Registry

namespace test8
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //生成大量隨機碼
            StreamWriter swriter = new StreamWriter("1.txt", true);
            for (int i = 0; i < 100; i++)
            {
                swriter.Write(generateRandomString(20));
                swriter.WriteLine();
                Console.WriteLine("Number: {0}", i);
            }
            swriter.Flush();
            swriter.Close();

        }

        static Random random = new Random();
        static string generateRandomString(int length)
        {
            var chars = "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < length; i++)
            {
                int index = random.Next(chars.Length);
                result.Append(chars[index]);
            }
            return result.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //過濾html標簽 

        }

        //C#過濾html標簽 
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");

            //htmlStr = htmlStr.Replace(""", ""); //去除異常的引號" " "
            //htmlStr = htmlStr.Replace(""", "");//去除异常的引号" " "
            //htmlStr = htmlStr.Replace("'", ""); //去除異常的引號" " "
            //htmlStr = htmlStr.Replace(""", "");
            return htmlStr.Trim();
        }


        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //批量生成隨機密碼, 存檔

            //批量生成隨機密碼，必須包含數字和字母，並用加密算法加密
            /*
            要求：密碼必須包含數字和字母

            思路：1.列出數字和字符。 組成字符串 ：chars

            2.利用randrom.Next(int i)返回一個小於所指定最大值的非負隨機數。

            3. 隨機取不小於chars長度的隨機數a,取字符串chars的第a位字符。

            4.循環 8次，得到8位密碼

            5.循環N次，批量得到密碼。
            */
            string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            Random randrom = new Random((int)DateTime.Now.Ticks);
            string path1 = "pwd.txt";
            for (int j = 0; j < 10000; j++)
            {
                string str = "";
                for (int i = 0; i < 8; i++)
                {
                    str += chars[randrom.Next(chars.Length)];//randrom.Next(int i)返回一個小於所指定最大值的非負隨機數
                }
                if (IsNumber(str))//判斷是否全是數字
                    continue;
                if (IsLetter(str))//判斷是否全是字母
                    continue;
                File.AppendAllText(path1, str);
                string pws = Md5(str, 32);//MD5加密
                File.AppendAllText(path1, "," + pws + "\r\n");
            }

            richTextBox1.Text += "批量生成隨機密碼，必須包含數字和字母，並用加密算法加密，完成\n";

        }

        //判斷是否全是數字
        static bool IsNumber(string str)
        {
            if (str.Trim("0123456789".ToCharArray()) == "")
                return true;
            return false;
        }
        //判斷是否全是字母
        static bool IsLetter(string str)
        {
            if (str.Trim("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".ToCharArray()) == "")
                return true;
            return false;
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="str">加密字元</param>
        /// <param name="code">加密位數16/32</param>
        /// <returns></returns>
        public static string Md5(string str, int code)
        {
            string strEncrypt = string.Empty;

            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] fromData = Encoding.GetEncoding("GB2312").GetBytes(str);
            byte[] targetData = md5.ComputeHash(fromData);
            for (int i = 0; i < targetData.Length; i++)
            {
                strEncrypt += targetData[i].ToString("X2");
            }
            if (code == 16)
            {
                strEncrypt = strEncrypt.Substring(8, 16);
            }
            return strEncrypt;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //從mp3中提取信息

            string filename = @"C:\______test_files\_mp3\aaaa.mp3";

            byte[] b = new byte[128];
            string sTitle;
            string sSinger;
            string sAlbum;
            string sYear;
            string sComm;

            FileStream fs = new FileStream(filename, FileMode.Open);

            fs.Seek(-128, SeekOrigin.End);
            fs.Read(b, 0, 128);

            bool isSet = false;
            String sFlag = System.Text.Encoding.Default.GetString(b, 0, 3);
            if (sFlag.CompareTo("TAG") == 0)
            {
                System.Console.WriteLine("Tag is setted!Replica Watches");
                richTextBox1.Text += "Tag is setted!Replica Watches\n";
                isSet = true;
            }

            if (isSet)
            {
                //http://study.pctoday.net.cn/3_Visual+Studio.aspx

                sTitle = System.Text.Encoding.Default.GetString(b, 3, 30);

                System.Console.WriteLine("标题:" + sTitle);
                richTextBox1.Text += "標題:" + sTitle + "\n";

                //Exclusive Replica Rolex Watches;

                sSinger = System.Text.Encoding.Default.GetString(b, 33, 30);

                System.Console.WriteLine("艺术家:" + sSinger);
                richTextBox1.Text += "藝術家:" + sSinger + "\n";

                //get album;

                sAlbum = System.Text.Encoding.Default.GetString(b, 63, 30);

                System.Console.WriteLine("唱片标题:" + sAlbum);
                richTextBox1.Text += "唱片標題:" + sAlbum + "\n";

                //egacn.com/Watches/Tag-Heuer;

                sYear = System.Text.Encoding.Default.GetString(b, 93, 4);

                System.Console.WriteLine("发行年:" + sYear);
                richTextBox1.Text += "發行年:" + sYear + "\n";

                //watchstylish.com;

                sComm = System.Text.Encoding.Default.GetString(b, 97, 30);

                System.Console.WriteLine("备注:" + sComm);
                richTextBox1.Text += "備註:" + sComm + "\n";

            }



        }

        private void button10_Click(object sender, EventArgs e)
        {
            //get mp3 info

            //string filename = @"C:\______test_files\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\______test_files\_mp3\aaaa.mp3";

            byte[] b = new byte[128];
            string sTitle;
            string sSinger;
            string sAlbum;
            string sYear;
            string sComm;

            FileStream fs = new FileStream(filename, FileMode.Open);

            fs.Seek(-128, SeekOrigin.End);

            fs.Read(b, 0, 128);

            bool isSet = false;

            String sFlag = System.Text.Encoding.Default.GetString(b, 0, 3);

            if (sFlag.CompareTo("TAG") == 0)
            {
                System.Console.WriteLine("Tag is setted!Replica Watches");
                richTextBox1.Text += "Tag is setted!Replica Watches" + "\n";
                isSet = true;
            }

            if (isSet)
            {
                //http://study.pctoday.net.cn/3_Visual+Studio.aspx

                sTitle = System.Text.Encoding.Default.GetString(b, 3, 30);

                System.Console.WriteLine("标题:" + sTitle);
                richTextBox1.Text += "标题:" + sTitle + "\n";

                //Exclusive Replica Rolex Watches;

                sSinger = System.Text.Encoding.Default.GetString(b, 33, 30);

                System.Console.WriteLine("艺术家:" + sSinger);
                richTextBox1.Text += "艺术家:" + sSinger + "\n";

                //get album;

                sAlbum = System.Text.Encoding.Default.GetString(b, 63, 30);

                System.Console.WriteLine("唱片标题:" + sAlbum);
                richTextBox1.Text += "唱片标题:" + sAlbum + "\n";

                //egacn.com/Watches/Tag-Heuer;

                sYear = System.Text.Encoding.Default.GetString(b, 93, 4);

                System.Console.WriteLine("发行年:" + sYear);
                richTextBox1.Text += "发行年:" + sYear + "\n";

                //watchstylish.com;

                sComm = System.Text.Encoding.Default.GetString(b, 97, 30);

                System.Console.WriteLine("备注:" + sComm);
                richTextBox1.Text += "备注:" + sComm + "\n";

                fs.Close();
            }

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //取得媒體資訊
            //使用Shell32讀取影音文件屬性
            /*
            由於需要用到實時讀取影音文件(mp3、wma、wmv …)播放時間長度的功能，搜索到的結果有：
            （1）硬編碼分析影音文件，需要分析各種媒體格式，代價最大；
            （2）使用WMLib SDK，需要熟悉SDK各個接口，且不同版本的WM接口有別，代價次之；
            （3）使用系統Shell32的COM接口，直接訪問媒體文體屬性，取其特定內容，代價最小。
            顯然第3種方案見效最快，立即操刀：
            ①引用Shell32底層接口c:\windows\system32\shell32.dll，VS自動轉換成Interop.Shell32.dll（注：64位系統和32位系統生成的Interop.Shell32.dll不一樣）
            ②編碼讀取播放時間長度：
            */

            //取得媒體資訊
            //string filename = @"C:\______test_files\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\______test_files\_mp3\aaaa.mp3";
            int i;
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + GetMediaInfo(filename, i) + "\n";
            }
        }

        public string GetMediaInfo(string path, int item)
        {
            //參考/Shell32/右鍵/屬性/內嵌Interop型別改成False
            try
            {
                string result = string.Empty;
                Shell32.Shell shell = new Shell32.ShellClass();
                Shell32.Folder folder = shell.NameSpace(path.Substring(0, path.LastIndexOf("\\")));
                Shell32.FolderItem folderItem = folder.ParseName(path.Substring(path.LastIndexOf("\\") + 1));
                return folder.GetDetailsOf(folderItem, item);
            }
            catch (Exception ex)
            {
                return null;
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //播放wav檔
            string filename = @"C:\______test_files\_wav\start.wav";
            SoundPlayer player = new SoundPlayer(); //声明一个控制WAV文件的声音播放文件对象
            player.SoundLocation = filename; //指定声音文件的路径
            player.LoadAsync();  //设置播放的方法
            player.Play(); //播放声音文件
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
    }
}
