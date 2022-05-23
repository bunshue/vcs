using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Management;    //for ManagementObjectSearcher
using System.Net;
using System.Collections;   //for DictionaryEntry, HashTable
using System.Text.RegularExpressions;
using Microsoft.VisualBasic.Devices;    //for Computer

namespace vcs_Mix02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > c:\dddddddddd\port.txt");

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

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 25);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 50);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 75);
            label4.Location = new Point(x_st + dx * 3, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string filename1 = @"C:\______test_files\compare\aaaa.txt";
            string filename2 = @"C:\______test_files\compare\bbbb.txt";

            StreamReader sr1 = new StreamReader(filename1);
            StreamReader sr2 = new StreamReader(filename2);
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()) == true)
            {
                richTextBox1.Text += "兩個檔案相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案不相同\n";
            }
            sr1.Close();
            sr2.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = System.IO.Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string name = "www.google.com";

            //透過計算機名取得IP地址
            IPAddress[] ip = null;
            try
            {
                ip = Dns.GetHostAddresses(name);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "電腦名稱 : " + name + "\n";
            richTextBox1.Text += "IP位址 : " + ip[0].ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string ip_addr = "140.114.29.100";
            IPHostEntry hostInfo;
            try
            {
                hostInfo = Dns.Resolve(ip_addr);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "IP位址 : " + ip_addr + "\n";
            richTextBox1.Text += "電腦名稱 : " + hostInfo.HostName + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得本機MAC地址

            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if (Convert.ToBoolean(mo["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            richTextBox1.Text += "取得系統開啟的端口和狀態\n";
            try
            {
                string path = @"c:\dddddddddd\port.txt";
                using (StreamReader sr = new StreamReader(path))
                {
                    while (sr.Peek() >= 0)
                    {
                        this.richTextBox1.Text += sr.ReadLine() + "\r\n";
                    }
                }
            }
            catch (Exception hy)
            {
                MessageBox.Show(hy.Message);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string filename1 = @"C:\______test_files\compare\aaaa.txt";
            string filename2 = @"C:\______test_files\compare\bbbb.txt";

            if (FileCompare(filename1, filename2) == true)
            {
                richTextBox1.Text += "兩個檔案相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案不相同\n";
            }
        }

        private bool FileCompare(string file1, string file2)
        {
            //　判斷相同的文件是否被參考兩次。
            if (file1 == file2)
            {
                return true;
            }
            int file1byte = 0;
            int file2byte = 0;
            using (FileStream fs1 = new FileStream(file1, FileMode.Open), fs2 = new FileStream(file2, FileMode.Open))
            {
                //　檢查文件大小。如果兩個文件的大小並不相同,則視為不相同。
                if (fs1.Length != fs2.Length)
                {
                    // 關閉文件。
                    fs1.Close();
                    fs2.Close();
                    return false;
                }
                //　逐一比較兩個文件的每一個字節，直到發現不相符或已到達文件尾端為止。
                do
                {
                    // 從每一個文件讀取一個字節。
                    file1byte = fs1.ReadByte();
                    file2byte = fs2.ReadByte();
                }
                while ((file1byte == file2byte) && (file1byte != -1));
                // 關閉文件。
                fs1.Close();
                fs2.Close();
            }
            //　返回比較的結果。在這個時候，只有當兩個文件的內容完全相同時， "file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //計算二維陣列所有元素總和
            int[,] array = new int[,] { { 0, 11, 3, 45, 17 }, { 23, 41, 5, 8, 10 }, { 9, 21, 16, 84, 51 } };

            int Total = 0;
            foreach (int element in array)
            {
                Total += element;
            }
            richTextBox1.Text += "此二維陣列的各個元素總和為: " + Total.ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //主線程中啟動一個支線程,執行doSomething這樣的一個方法。
            Thread thread = new Thread(new ThreadStart(ThreadRun));
            thread.IsBackground = true;//這樣能隨主程序一起結束
            thread.Start();
        }

        delegate void Delegate_do();

        static void ThreadRun()
        {
            try
            {
                Delegate_do Delegate_do = new Delegate_do(FindAllProduct);
                IAsyncResult result = Delegate_do.BeginInvoke(null, null);
                while (!result.IsCompleted)
                {
                    Console.WriteLine("子線程未完成");
                    Thread.Sleep(1000);//每隔1秒判斷一下是否完成
                }
                while (true)
                {
                    if (result.IsCompleted)
                    {
                        Console.WriteLine("-------子線程已完成-------");
                        break;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        static void FindAllProduct()
        {
            List<int> array = new List<int>();   //宣告int型態的List
            for (int i = 0; i < 100000000; i++)
            {
                array.Add(i);
            }

            int m = 0;
            foreach (var i in array)
            {
                m++;
            }
            Console.WriteLine(m);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //一行一行讀取文字檔
            string filename = @"C:\______test_files\_case1\_case1a\_case1aa\eula.3081a.txt";

            StreamReader SReader = new StreamReader(filename, Encoding.Default);
            string strLine = string.Empty;
            while ((strLine = SReader.ReadLine()) != null)
            {
                richTextBox1.Text += strLine + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

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

            int len = al.Count;
            richTextBox1.Text = "len = " + len.ToString() + "\n";
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

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //richTextBox 內文變色

            richTextBox1.SelectionColor = Color.Red;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Orange;
            richTextBox1.AppendText("多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Yellow;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Green;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Blue;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Purple;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");
            richTextBox1.AppendText("恢復原色\n");
            richTextBox1.AppendText("恢復原色\n");
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //在 C# 中獲取 2D 陣列的長度

            int[,] array2D;
            //使用 C# 中的 Array.GetLength() 函式獲取 2D 陣列的寬度和高度
            //使用 C# 中的 Array.GetUpperBound() 函式獲取二維陣列的寬度和高度
            array2D = new int[5, 10];
            Console.WriteLine(array2D.GetLength(0));	//5
            Console.WriteLine(array2D.GetLength(1));	//10

            //使用 C# 中的 Array.GetUpperBound() 函式獲取二維陣列的寬度和高度
            array2D = new int[5, 10];
            Console.WriteLine(array2D.GetUpperBound(0) + 1);	//5
            Console.WriteLine(array2D.GetUpperBound(1) + 1);	//10
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //使用 GetBytes() 方法將字串轉換為位元組陣列

            string myString = "This is a string.";
            byte[] byteArray = Encoding.ASCII.GetBytes(myString);
            richTextBox1.Text += "The Byte Array is:\n";
            foreach (byte bytes in byteArray)
            {
                richTextBox1.Text += bytes.ToString() + "\n";
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            richTextBox1.Text += "目前應用程式路徑: \t" + Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location) + "\n";

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string filename = Path.Combine(Application.StartupPath, @"..\..\Form1.cs");

            richTextBox1.Text = "把這個檔案的註解抓出來\n";
            richTextBox1.Text += "檔案" + filename + "\n";

            // Extract the comments.
            // A weirder comment.   /* Not a multi-line comment

            // Display the comments.
            richTextBox1.Text += ExtractComments(filename);
        }

        // Return a file's comments.
        private string ExtractComments(string filename)
        {
            // Get the file's contents.
            string all_text = File.ReadAllText(filename);

            // Get rid of \" escape sequences.
            all_text = all_text.Replace("\\\"", "");

            // Process the file.
            string comments = "";
            while (all_text.Length > 0)
            {
                // Find the next string or comment.
                int string_pos = all_text.IndexOf("\"");
                int end_line_pos = all_text.IndexOf("//");
                int multi_line_pos = all_text.IndexOf("/*");

                // If there are none of these, we're done.
                if ((string_pos < 0) && (end_line_pos < 0) && (multi_line_pos < 0)) break;

                if (string_pos < 0) string_pos = all_text.Length;
                if (end_line_pos < 0) end_line_pos = all_text.Length;
                if (multi_line_pos < 0) multi_line_pos = all_text.Length;

                // See which comes first.
                if ((string_pos < end_line_pos) && (string_pos < multi_line_pos))
                {
                    // String.
                    // Find its end.
                    int end_pos = all_text.IndexOf("\"", string_pos + 1);

                    // Extract and discard everything up to the string.
                    if (end_pos < 0)
                    {
                        all_text = "";
                    }
                    else
                    {
                        all_text = all_text.Substring(end_pos + 1);
                    }
                }
                else if (end_line_pos < multi_line_pos)
                {
                    // End of line comment.
                    // Find its end.
                    int end_pos = all_text.IndexOf("\r\n", end_line_pos + 2);

                    // Extract the comment.
                    if (end_pos < 0)
                    {
                        comments += all_text.Substring(end_line_pos) + "\r\n";
                        all_text = "";
                    }
                    else
                    {
                        comments += all_text.Substring(end_line_pos, end_pos - end_line_pos) + "\r\n";
                        all_text = all_text.Substring(end_pos + 2);
                    }
                }
                else
                {
                    // Multi-line comment.
                    // Find its end.
                    int end_pos = all_text.IndexOf("*/", multi_line_pos + 2);

                    // Extract the comment.
                    if (end_pos < 0)
                    {
                        comments += all_text.Substring(multi_line_pos) + "\r\n";
                        all_text = "";
                    }
                    else
                    {
                        comments += all_text.Substring(multi_line_pos, end_pos - multi_line_pos + 2) + "\r\n";
                        all_text = all_text.Substring(end_pos + 2);
                    }
                }
            }
            return comments;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //搜尋檔案內的文字

            string txtDirectory = @"C:\______test_files\_case1";
            string type = "*.*";
            string pattern = "";

            richTextBox1.Clear();
            DirectoryInfo dir_info = new DirectoryInfo(txtDirectory);

            ListFiles(type, dir_info, pattern);
        }

        // Add the files in this directory's subtree 
        // that match the pattern to the ListBox.
        private void ListFiles(string pattern, DirectoryInfo dir_info, string target)
        {
            // Get the files in this directory.
            FileInfo[] fs_infos = dir_info.GetFiles(pattern);
            foreach (FileInfo fs_info in fs_infos)
            {
                if (target.Length == 0)
                {
                    richTextBox1.Text += fs_info.FullName + "\n";
                }
                else
                {
                    string txt = File.ReadAllText(fs_info.FullName);
                    if (txt.IndexOf(target, StringComparison.OrdinalIgnoreCase) >= 0)
                    {
                        richTextBox1.Text += fs_info.FullName + "\n";
                    }
                }
            }

            // Search subdirectories.
            DirectoryInfo[] subdirs = dir_info.GetDirectories();
            foreach (DirectoryInfo subdir in subdirs)
            {
                ListFiles(pattern, subdir, target);
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //將純文字檔拆成一行一行的字串陣列, 可以去除前後空白
            string filename = @"C:\______test_files\__RW\_txt\poem.txt";
            string[] patterns;
            patterns = File.ReadAllLines(filename).Select(i => i.Trim()).Where(i => i != string.Empty).ToArray();
            int len = patterns.Length;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            int ii;
            for (ii = 0; ii < len; ii++)
            {
                richTextBox1.Text += patterns[ii] + "\n";
            }


        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string foldername = @"C:\______test_files\__pic";

            IEnumerable<FileInfo> images = null;
            if (Directory.Exists(foldername) == true)
            {
                DirectoryInfo dirInfo = new DirectoryInfo(foldername);
                images = dirInfo.EnumerateFiles("*.jpg").OrderBy(i => i.Name[0]).ThenBy(i => i.Name.Length).ThenBy(i => i.Name);

                int len = images.Count();
                richTextBox1.Text += "len = " + len.ToString() + "\n";

                if (images != null && images.Count() > 0)
                {

                }

                foreach (var image in images)
                {
                    richTextBox1.Text += image.Name + "\n";
                    richTextBox1.Text += image.FullName + "\n";
                    richTextBox1.Text += image.Extension + "\n";
                    richTextBox1.Text += image.Length.ToString() + "\n";
                }
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string url = @"C:/_git/vcs/_1.data/_html/朱冶蕙老師的電腦教室.html";
            //foreach (var fileName in fileNameList)
            {
                MemoryStream ms = GetResponse(url);
                File.WriteAllBytes("aaaaa.html", ms.ToArray());
            }
        }

        private MemoryStream GetResponse(string url)
        {
            while (true)
            {
                try
                {
                    HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
                    //request.Headers.Add("Cookie", cookie);
                    request.Method = "GET";
                    request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                    HttpWebResponse response = request.GetResponse() as HttpWebResponse;

                    MemoryStream ms = new MemoryStream();
                    response.GetResponseStream().CopyTo(ms);

                }
                catch (Exception ex)
                {
                }
            }
        }

        //计算两点GPS坐标距离 
        /// <summary>
        ///计算两点GPS坐标的距离
        /// </summary>
        /// <param name="n1">第一点的纬度坐标</param>
        /// <param name="e1">第一点的经度坐标</param>
        /// <param name="n2">第二点的纬度坐标</param>
        /// <param name="e2">第二点的经度坐标</param>
        /// <returns></returns>
        public static double Distance(double n1, double e1, double n2, double e2)
        {
            double jl_jd = 102834.74258026089786013677476285;   // 米/度
            double jl_wd = 111712.69150641055729984301412873;   // 米/度
            double b = Math.Abs((e1 - e2) * jl_jd);
            double a = Math.Abs((n1 - n2) * jl_wd);
            return Math.Sqrt((a * a + b * b));
        }


        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int i;
            int j;
            List<string[]> fileNameList = new List<string[]>();

            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";
            for (i = 0; i < 10; i++)
            {
                fileNameList.Add(new string[] { i.ToString(), "aaaaaaa", "bbbbb", "cccccc" });
            }
            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";

            for (i = 0; i < fileNameList.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (j = 0; j < 4; j++)
                {
                    richTextBox1.Text += fileNameList[i][j] + "\t";
                }
                richTextBox1.Text += "\n";

            }

            foreach (var fileName in fileNameList)
            {
                string imgURL = fileName[0];
                richTextBox1.Text += imgURL + "\n";
            }

        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            /*
            實際上，全角字符的第一個字節總是被置為163，
            而第二個字節則是相同半角字符碼加上128（不包括空格）。
            如半角A為65，則全角A則是163（第一個字節）、193（第二個字節，128+65）。
            */

            richTextBox1.Text += "全形ASCII\n";
            for (byte k = 0x00; k < 0x7f; k++)
            {
                byte[] ch = new byte[2];
                ch[0] = 163;
                ch[1] = (byte)(128 + k);
                Console.Write(Encoding.GetEncoding("GB2312").GetString(ch));
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(ch);
            }
            richTextBox1.Text += "\n";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string senderEmail = @"david@insighteyes.com";
            string[] sendFromUser = senderEmail.Split('@');
            int len = sendFromUser.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + sendFromUser[i] + "\n";
            }


            richTextBox1.Text += "用Regular Expression拆解e-mail帳號\n";

            List<string> emailList = new List<string>();
            string email = "xue@163.,xue@163.com12,2707@qq.com,,xue@yahoo.com.cn,xue@163.com,xue@163.com12";
            //  Regex reg2 = new Regex(@"^\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,}$");驗證email的正則表達式  

            Regex reg = new Regex(@"(?<email>[\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,})");
            Match m = reg.Match(email);
            foreach (Match item in reg.Matches(email))
            {
                emailList.Add(item.Groups["email"].Value);
            }
            len = emailList.Count;
            richTextBox1.Text += "共取得 : " + len.ToString() + " 個帳號\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + emailList[i] + "\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //參考/加入參考/.Net/Microsoft.VisualBasic
            Computer myComputer = new Computer();
            label0.Text = "物理內存總量（M）：" + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            label1.Text = "可用物理內存（M）：" + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            label2.Text = "虛擬內存總量（M）：" + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            label3.Text = "可用虛擬內存（M）：" + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);

            label4.Text = "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + " 秒";
        }
    }
}



