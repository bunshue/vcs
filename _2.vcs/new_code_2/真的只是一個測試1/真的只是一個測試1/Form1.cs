using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for RegistryKey

using System.Reflection;    //for Assembly

using System.IO;    //for StreamReader

using System.Net;   //for HttpWebRequest HttpWebResponse

using System.Collections;   //for DictionaryEntry
using System.Drawing.Imaging;   //for ImageFormat

using System.Text.RegularExpressions;

using System.Diagnostics;	//for Stopwatch

using System.Runtime.InteropServices;

namespace 真的只是一個測試1
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 165;
            dy = 65;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //計算二維陣列所有元素總和
            int[,] array = new int[,] { { 0, 11, 3, 45, 17 }, { 23, 41, 5, 8, 10 }, { 9, 21, 16, 84, 51 } };

            int Total = 0;
            foreach (int element in array)
            {
                Total += element;
            }
            richTextBox1.Text += "此二維陣列的各個元素總和為: " + Total.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string strpath = Environment.SystemDirectory + "\\music";
            richTextBox1.Text += "strpath = " + strpath + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string sText = this.Text;
            string sFullName = string.Format("{0} %1", Application.ExecutablePath);
            // Application.ExecutablePath 是程式執行檔的完整路徑檔案名稱
            // %1 表示傳入的檔案
            //if (this.rbFile.Checked)
            {
                // 加入檔案右鍵選單
                RegFile(sText, sFullName);
            }
            //else
            {
                // 加入目錄右鍵選單
                //RegDirectory(sText, sFullName);
            }
            MessageBox.Show("作業成功");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得專案內所有表單名稱

            Assembly a = Assembly.GetExecutingAssembly();       //取得目前組件

            richTextBox1.Text += "目前組件 : " + a.ToString() + "\n";
            richTextBox1.Text += "CodeBase : " + a.CodeBase.ToString() + "\n";
            richTextBox1.Text += "FullName : " + a.FullName.ToString() + "\n";
            richTextBox1.Text += "Location : " + a.Location.ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetType().ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetName() + "\n";
            richTextBox1.Text += "GetType : " + a.ImageRuntimeVersion + "\n";

            foreach (Type t in a.GetTypes())                    //找尋組件內所有類別型態
            {
                richTextBox1.Text += t.ToString() + "\n";

                if (t.IsSubclassOf(typeof(Form)))           //如果父類別是繼承自Form的話
                {
                    //richTextBox1.Text += t.ToString() + "\n"; //列出該類別資訊

                }
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //從檔案完整路徑分離出資料夾,檔案名稱,副檔名
            string full_filename = @"C:\______test_files\_case1\_case1a\_case1aa\eula.3081a.txt";
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

        private void button5_Click(object sender, EventArgs e)
        {
            //char可以存放中文字
            char[] gender = new char[5];
            gender[0] = '男';
            gender[1] = '女';
            gender[2] = '男';
            gender[3] = '男';
            gender[4] = '女';
            for (int i = 0; i < 5; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + gender[i] + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //一行一行讀取文字檔
            string filename = @"C:\______test_files\_case1\_case1a\_case1aa\eula.3081a.txt";

            StreamReader SReader = new StreamReader(filename, Encoding.Default);
            string strLine = string.Empty;
            while ((strLine = SReader.ReadLine()) != null)
            {
                richTextBox1.Text += strLine + "\n";
            }
        }

        private void RegFile(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"*\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue(string.Empty, sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }

        private void RegDirectory(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"directory\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue("", sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            browse_all_controls(this.Controls);
        }

        public void browse_all_controls(Control.ControlCollection cc)
        {
            foreach (Control c in cc)  //撈出所有控件
            {
                richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    richTextBox1.Text += "\t" + ((Button)c).Text + " " + ((Button)c).Size.Width.ToString() + " X " + ((Button)c).Size.Height.ToString();

                    if (((Button)c).Tag != null)
                    {
                        richTextBox1.Text += "\t" + ((Button)c).Tag.ToString().ToString();
                    }
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //分出 時:分:秒 再組合

            DateTime dt = DateTime.Now;

            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";
        }

        //根据Url地址得到网页的html源码
        private string GetWebContent(string Url)
        {
            string strResult = "";
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
                //声明一个HttpWebRequest请求
                request.Timeout = 30000;
                //设置连接超时时间
                request.Headers.Set("Pragma", "no-cache");
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("big5");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                strResult = streamReader.ReadToEnd();
            }
            catch
            {
                MessageBox.Show("出错");
            }
            return strResult;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //抓取網頁並分析數據

            //要抓取的URL地址
            //string Url = "http://list.mp3.baidu.com/topso/mp3topsong.html?id=1#top2";
            string Url = "https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG3n.Oxg00wAkRB7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZAM1cFFoWDdMWFFLbTByV2N1Z3d3WThBBG5fcnNsdAMwBG5fc3VnZwMxBG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzgEcXVlcnkDcHJlc3RpZ2UEdF9zdG1wAzE2MjYxNDI5Nzk-?p=prestige&fr=sfp&iscqry=";
            //string Url = "http://mirlab.org/jang/books/matlabProgramming4beginner/example/03-%E4%BA%8C%E7%B6%AD%E5%B9%B3%E9%9D%A2%E7%B9%AA%E5%9C%96/plotxy12.m";
            //string Url = "https://zh.wikipedia.org/wiki/%E6%98%8E%E7%A5%9E%E5%AE%97";
            //得到指定Url的源码
            string strWebContent = GetWebContent(Url);
            richTextBox1.Text = strWebContent;

            return;


            //取出和数据有关的那段源码
            int iBodyStart = strWebContent.IndexOf("<body", 0);
            int iStart = strWebContent.IndexOf("歌曲TOP500", iBodyStart);
            int iTableStart = strWebContent.IndexOf("<table", iStart);
            int iTableEnd = strWebContent.IndexOf("</table>", iTableStart);
            string strWeb = strWebContent.Substring(iTableStart, iTableEnd - iTableStart + 8);
            //生成HtmlDocument
            WebBrowser webb = new WebBrowser();
            webb.Navigate("about:blank");
            HtmlDocument htmldoc = webb.Document.OpenNew(true);
            htmldoc.Write(strWeb);
            HtmlElementCollection htmlTR = htmldoc.GetElementsByTagName("TR");
            foreach (HtmlElement tr in htmlTR)
            {
                string strID = tr.GetElementsByTagName("TD")[0].InnerText;
                richTextBox1.Text += "get : " + strID + "\n";

                //string strName = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "MusicName");
                //string strSinger = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "Singer");
                strID = strID.Replace(".", "");
                //插入DataTable
                //AddLine(strID, strName, strSinger, "0");

                string strID1 = tr.GetElementsByTagName("TD")[2].InnerText;
                //string strName1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "MusicName");
                //string strSinger1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "Singer");
                //插入DataTable
                strID1 = strID1.Replace(".", "");
                //AddLine(strID1, strName1, strSinger1, "0");
                string strID2 = tr.GetElementsByTagName("TD")[4].InnerText;
                //string strName2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "MusicName");
                //string strSinger2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "Singer");
                //插入DataTable
                strID2 = strID2.Replace(".", "");
                //AddLine(strID2, strName2, strSinger2, "0");
            }
            //插入数据库
            //InsertData(dt);

            //dataGridView1.DataSource = dt.DefaultView;


        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Environment參數\n";
            richTextBox1.Text += "CommandLine:\t" + Environment.CommandLine + "\n";
            richTextBox1.Text += "CurrentDirectory:\t" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "MachineName:\t" + Environment.MachineName + "\n";
            richTextBox1.Text += "OSVersion:\t" + Environment.OSVersion + "\n";
            //richTextBox1.Text += "StackTrace:\t" + Environment.StackTrace + "\n";
            richTextBox1.Text += "SystemDirectory:\t" + Environment.SystemDirectory + "\n";
            richTextBox1.Text += "TickCount:\t" + Environment.TickCount + "\n";
            richTextBox1.Text += "Version:\t" + Environment.Version + "\n";
            richTextBox1.Text += "WorkingSet:\t" + Environment.WorkingSet + "\n";

            richTextBox1.Text += "列出所有環境變數\n";
            foreach (DictionaryEntry var in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }

            richTextBox1.Text += "列出Logical Drives\n";
            foreach (string drive in Environment.GetLogicalDrives())
            {
                richTextBox1.Text += "\t" + drive + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立一個Hashtable\n";

            Hashtable openWith = new Hashtable();

            richTextBox1.Text += "給Hashtable賦值, key是唯一, value不唯一\n";
            //            key     value
            openWith.Add("txt", "notepad.exe");
            openWith.Add("bmp", "paint.exe");
            openWith.Add("dib", "paint.exe");
            openWith.Add("rtf", "wordpad.exe");

            // When you use foreach to enumerate hash table elements,
            // the elements are retrieved as DictionaryEntry objects.
            foreach (DictionaryEntry var in openWith)
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }
        }

        List<string> al = new List<string>(); //當前歌詞時間表

        private void button12_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_mp3\04-三月雪(&黃妃).mp3";

            string filename_lyrics = Path.Combine(Path.GetDirectoryName(filename), Path.GetFileNameWithoutExtension(filename) + ".lrc");

            richTextBox1.Text += "f1 = " + filename + "\n";
            richTextBox1.Text += "f2 = " + filename_lyrics + "\n";

            if (!File.Exists(filename_lyrics))
            {
                richTextBox1.Text = "無 歌詞檔案\n";
                return;
            }

            using (StreamReader sr = new StreamReader(new FileStream(filename_lyrics, FileMode.Open), Encoding.Default))
            {
                string tempLrc = "";
                while (!sr.EndOfStream)
                {
                    tempLrc = sr.ReadToEnd();
                }

                if (tempLrc.Trim() == "")
                {
                    this.richTextBox1.Text = "歌詞檔案內容為空";
                    return;
                }

                tempLrc = tempLrc.Trim();
                Regex rg = new Regex("\r*\n*\\[ver:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[al:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[by:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[offset:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[ar:(.*)\\]\r*\n*");
                Match mtch;
                mtch = rg.Match(tempLrc);
                tempLrc = rg.Replace(tempLrc, "\n歌手:" + mtch.Groups[1].Value + "\n");
                rg = new Regex("\r*\n*\\[ti:(.+?)\\]\r*\n*");   //這裡注意貪婪匹配問題.+?
                mtch = rg.Match(tempLrc);
                tempLrc = rg.Replace(tempLrc, "\n歌名:" + mtch.Groups[1].Value + "\n");
                rg = new Regex("\r*\n*\\[[0-9][0-9]:[0-9][0-9].[0-9][0-9]\\]");
                MatchCollection mc = rg.Matches(tempLrc);
                al.Clear();

                foreach (Match m in mc)
                {
                    string temp = m.Groups[0].Value;
                    //this.Text += temp + "+";                        
                    string mi = temp.Substring(temp.IndexOf('[') + 1, 2);
                    string se = temp.Substring(temp.IndexOf(':') + 1, 2);
                    string ms = temp.Substring(temp.IndexOf('.') + 1, 2);   //這是毫秒，其實我只精確到秒，毫秒後面並沒有用
                    //this.Text += mi + ":" + se + "+";
                    string time = Convert.ToInt32(mi) * 60 + Convert.ToInt32(se) + "";  //這裡並沒有新增毫秒
                    al.Add(time);
                }

                tempLrc = rg.Replace(tempLrc, "\n");
                char[] remove = { '\r', '\n', ' ' };
                this.richTextBox1.Text = tempLrc.TrimStart(remove);
                this.timer1.Interval = 1000;
                this.timer1.Tick += ShowLineLrc;
                this.timer1.Start();
            }




        }


        int position = 0;
        /// <summary>
        /// 定時器執行的方法，每隔1秒執行一次  歌詞逐行顯示
        private void ShowLineLrc(object sender, EventArgs e)
        {
            //int pos = al.IndexOf(trackBarValue.ToString());
            position++;
            int pos = position;
            bool isAr = this.richTextBox1.Text.Contains("歌手:");
            bool isTi = this.richTextBox1.Text.Contains("歌名:");


            if ((pos >= 0) && (pos < 25))
            {
                int n = isAr ? 1 : 0;
                int m = isTi ? 1 : 0;

                int height = 28 * (this.al.Count + m + n);
                int max = height - this.richTextBox1.Height;


                this.richTextBox1.SelectAll();
                this.richTextBox1.SelectionColor = Color.Black;
                this.richTextBox1.SelectionLength = 0;/**/

                int l = this.richTextBox1.Lines[pos + m + n].Length;
                this.richTextBox1.Select(this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n), l);
                this.richTextBox1.SelectionColor = Color.OrangeRed;
                this.richTextBox1.SelectionLength = 0;
                //this.Text = GetScrollPos(this.richTextBox1.Handle, SB_VERT).ToString() + "-" + al.Count + "-" + this.richTextBox1.Height;

                if ((pos + m + n) * 28 <= max)
                {
                    int start = this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n);
                    this.richTextBox1.SelectionStart = start;
                    this.richTextBox1.ScrollToCaret();

                }
                else
                {
                    /*
                    //this.richTextBox1.Focus();
                    SendMessage(this.richTextBox1.Handle, WM_VSCROLL, SB_BOTTOM, 0);
                    UpdateWindow(this.richTextBox1.Handle);
                    //this.richTextBox1.SelectionStart = this.richTextBox1.Text.Length;
                    //this.richTextBox1.ScrollToCaret();
                    */
                }

                /*
                if (this.lrcForm != null)
                {
                    string l1 = this.richTextBox1.Lines[pos + m + n];
                    string l2;
                    if ((pos + m + n) < this.richTextBox1.Lines.Length - 1)
                    {
                        l2 = this.richTextBox1.Lines[pos + m + n + 1];
                    }
                    else
                    {
                        l2 = "。。。。。";
                    }

                    this.lrcForm.setLrc(l1, l2, pos);
                    //this.lrcForm.setLrc(ArrayList al,);

                }
                */
            }
        }



        private void button13_Click(object sender, EventArgs e)
        {
            int len = al.Count;
            richTextBox1.Text = "len = " + len.ToString() + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            if (button14.Text == "啟動 CopyFromScreen")
            {
                button14.Text = "關閉 CopyFromScreen";
                timer1.Enabled = true;
            }
            else
            {
                button14.Text = "啟動 CopyFromScreen";
                timer1.Enabled = false;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //file info
            string filename = @"C:\______test_files\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";

            FileInfo fileInfo = new FileInfo(filename);
            string fileSize = (fileInfo.Length / 1024).ToString() + " KB";
            string temp = filename.Remove(filename.LastIndexOf('.'));
            string fileName = Path.GetFileNameWithoutExtension(filename);
            string fileExtension = Path.GetExtension(filename);

            richTextBox1.Text += "filename = " + filename + "\n";
            richTextBox1.Text += "fileSize = " + fileSize + "\n";
            richTextBox1.Text += "temp = " + temp + "\n";
            richTextBox1.Text += "fileName = " + fileName + "\n";
            richTextBox1.Text += "fileExtension = " + fileExtension + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //透明的Form背景
            this.TransparencyKey = Color.Red;
            this.BackColor = this.TransparencyKey;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //透明的RichTextBox背景
            this.TransparencyKey = Color.Red;
            richTextBox1.BackColor = this.TransparencyKey;
        }

        int x_st = 0;
        int y_st = 0;

        private void timer1_Tick(object sender, EventArgs e)
        {
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            this.Text = pt.ToString();

            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;
            int w = 200;
            int h = 200;
            Bitmap bitmap1 = new Bitmap(w, h);  //, PixelFormat.Format32bppArgb);
            Graphics g = Graphics.FromImage(bitmap1);

            //                    來源位置             目的位置      要傳輸的區域大小  判斷在像素複製作業中來源色彩如何與目的色彩結合以產生最後的色彩
            //g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h), CopyPixelOperation.SourceInvert);
            //g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h));
            g.CopyFromScreen(new Point(pt.X - w / 2, pt.Y - h / 2), new Point(0, 0), new Size(w, h));
            g.Dispose();

            pictureBox1.Image = bitmap1;
            pictureBox1.Size = bitmap1.Size;

            x_st += 50;
            if (x_st > 600)
                x_st = 0;

        }

        List<double[]> pts = new List<double[]>();    //二維List for double
        int g = 10;


        //二維List for double
        private void button20_Click(object sender, EventArgs e)
        {
            double t = 0;

            for (t = 0; t <= 10.01; t += 0.1)
            {
                //richTextBox1.Text += "t = " + t.ToString() + "\n";
                pts.Add(new double[] { t, g * t * t / 2 });
            }

            int len = pts.Count;

            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += pts[i][0].ToString("n3") + "\t" + pts[i][1].ToString("n3") + "\n";
            }



        }

        //多筆資料比較
        private const int CNT = 100;
        private void button21_Click(object sender, EventArgs e)
        {
            //int N = 10;

            pts.Clear();

            //一維陣列用法：
            double[] a = new double[CNT];
            int[] checked_array = new int[CNT]; //一維陣列用法

            int i;
            int j;

            Random r = new Random();
            for (i = 0; i < CNT; i++)
            {
                //a[i] = r.NextDouble();
                a[i] = r.Next(100, 200);
            }


            for (i = 0; i < CNT; i++)
            {
                //richTextBox1.Text += "取0.0~1.0的亂數值：" + a[i].ToString() + "\n";
                //richTextBox1.Text += "a[" + i.ToString() + "] = " + a[i].ToString() + "\n";

                //result3 += r.Next(10, 20).ToString() + " ";
            }

            Stopwatch sw = new Stopwatch();
            sw.Start();

            int equal_count = 0;

            int[] same_index = new int[10]; //一維陣列用法
            int index = 0;

            for (i = 0; i < CNT; i++)
            {
                if (checked_array[i] == 1)
                    continue;

                index = 0;
                same_index = new int[100];

                for (j = (i + 1); j < CNT; j++)
                {
                    if ((a[i] == a[j]) && (a[i] != -1))
                    {
                        equal_count++;
                        same_index[index] = j;
                        index++;
                        //richTextBox1.Text += "取得相同數字\t\ta[" + i.ToString() + "] = " + a[i].ToString() + "\t\ta[" + j.ToString() + "] = " + a[j].ToString() + "\n";
                    }
                }

                if (index > 0)
                {
                    checked_array[i] = 1;
                    richTextBox1.Text += "取得相同數字\t\ta[" + i.ToString() + "] = " + a[i].ToString();
                    int k;
                    for (k = 0; k < index; k++)
                    {
                        checked_array[same_index[k]] = 1;
                        richTextBox1.Text += "\t\ta[" + same_index[k].ToString() + "] = " + a[same_index[k]].ToString();
                    }
                    richTextBox1.Text += "\n";

                    /*
                    if (index == 1)
                    {
                        richTextBox1.Text += "a[" + same_index[0].ToString() + "] = " + a[same_index[0]].ToString() + "\n";
                    }
                    else if (index == 2)
                    {
                        richTextBox1.Text += "a[" + same_index[0].ToString() + "] = " + a[same_index[0]].ToString() + "\t\ta[" + same_index[1].ToString() + "] = " + a[same_index[1]].ToString() + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "333333333333\n";
                    }
                    //richTextBox1.Text += "index = " + index.ToString() + "\n";
                    */
                }
            }

            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";

            for (i = 0; i < CNT; i++)
            {
                //richTextBox1.Text += "取0.0~1.0的亂數值：" + a[i].ToString() + "\n";
                //richTextBox1.Text += "a[" + i.ToString() + "] = " + a[i].ToString() + "\n";

                //result3 += r.Next(10, 20).ToString() + " ";
            }

        }

        //找出資料夾內所有檔案
        private void button22_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files\_pic";

            // Enumerate the files.
            DirectoryInfo dir_info = new System.IO.DirectoryInfo(foldername);

            foreach (DirectoryInfo d_info in dir_info.GetDirectories())
            {
                richTextBox1.Text += d_info.FullName + "\n";
                richTextBox1.Text += d_info.Name + "\n";


            }

            richTextBox1.Text += "\n\n";

            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                try
                {
                    richTextBox1.Text += file_info.FullName + "\n";
                    //richTextBox1.Text += file_info.Name + "\n";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error processing file '" +
                        file_info.Name + "'\n" + ex.Message,
                        "Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            } // foreach file_info



        }

        //取得硬碟資訊 ST
        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        private void button23_Click(object sender, EventArgs e)
        {
            long fb, ftb, tfb;
            string foldername = @"C:\______test_files\__RW\_excel";

            //this.textBox4.Text = foldername;
            richTextBox1.Text += "get : " + foldername + "\n";
            if (GetDiskFreeSpaceEx(foldername, out fb, out ftb, out tfb) != 0)
            {
                richTextBox1.Text += "磁碟總容量：" + ByteConversionTBGBMBKB(Convert.ToInt64(ftb)) + "\n";
                richTextBox1.Text += "可用磁碟空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(fb)) + "\n";
                richTextBox1.Text += "磁碟剩餘空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(tfb)) + "\n";
            }
            else
            {
                MessageBox.Show("NO");
            }
        }
        //取得硬碟資訊 SP

        private void button24_Click(object sender, EventArgs e)
        {

        }

    }
}
