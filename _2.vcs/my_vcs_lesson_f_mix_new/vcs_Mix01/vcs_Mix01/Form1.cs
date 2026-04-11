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
using System.Security.Cryptography;
using System.Diagnostics;   //for Process
using System.Threading;
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Globalization; //for CultureInfo
using System.Runtime.InteropServices;

using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False
using Microsoft.Win32;  //for RegistryKey

namespace vcs_Mix01
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

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(1170, 750);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Down：" + e.X + " : " + e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Up：" + e.X + " : " + e.Y;
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
            /* 創建一個進程，並為進程傳入需要的參數    * 或者說是啟動一個外部程序，並為其傳入參數    * 等待退出或者強制關閉   */

            //啟動一個外部程序
            //聲明一個程序信息類，指定啟動進程是的參數信息                   
            ProcessStartInfo Info = new ProcessStartInfo();
            //設置外部程序名
            Info.FileName = "notepad.exe";
            //設置外部程序的啟動參數（命令行參數）為test.txt                   
            Info.Arguments = "test.txt";
            //設置外部程序工作目錄為  C:\                   
            Info.WorkingDirectory = "C:\\";
            //聲明一個程序類,也就是創建一個進程                   
            Process Proc;
            try
            {
                //                   //啟動外部程序                   
                Proc = Process.Start(Info);
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。\r{0}", ex);
                return;
            }
            //打印出外部程序的開始執行時間
            Console.WriteLine("外部程序的開始執行時間：{0}", Proc.StartTime);

            //等待3秒鐘                   
            Proc.WaitForExit(3000);
            //如果這個外部程序沒有結束運行則對其強行終止                   
            if (Proc.HasExited == false)
            {
                Console.WriteLine("由主程序強行終止外部程序的運行！");
                Proc.Kill();
            }
            else
            {
                Console.WriteLine("由外部程序正常退出！");
            }
            Console.WriteLine("外部程序的結束運行時間：{0}", Proc.ExitTime);
            Console.WriteLine("外部程序在結束運行時的返回值：{0}", Proc.ExitCode);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //獲取當前行號
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
        }

        //獲取當前行號
        public static int GetLineNum()
        {
            System.Diagnostics.StackTrace st = new System.Diagnostics.StackTrace(1, true);
            return st.GetFrame(0).GetFileLineNumber();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //計算字數
            string[] words = {
                "Alabama",
                "Alaska",
                "American Samoa",
                "Arizona",
                "Arkansas",
                "California",
                "Colorado",
                "Connecticut",
                "Delaware",
                "District of Columbia",
                "Florida",
                "Georgia",
                "Guam",
                "Hawaii",
                "Idaho",
                "Illinois",
                "Indiana",
                "Iowa",
                "Kansas",
                "Kentucky",
                "Louisiana",
                "Maine",
                "Maryland",
                "Massachusetts",
                "Michigan",
                "Minnesota",
                "Mississippi",
                "Missouri",
                "Montana",
                "Nebraska",
                "Nevada",
                "New Hampshire",
                "New Jersey",
                "New Mexico",
                "New York",
                "North Carolina",
                "North Dakota",
                "Northern Marianas Islands    ",
                "Ohio",
                "Oklahoma",
                "Oregon",
                "Pennsylvania",
                "Puerto Rico",
                "Rhode Island",
                "South Carolina",
                "South Dakota",
                "Tennessee",
                "Texas",
                "Utah",
                "Vermont",
                "Virginia ",
                "Virgin Islands ",
                "Washington",
                "West Virginia",
                "Wisconsin",
                "Wyoming"
            };

            // Get a list holding each word's unique letter count and name.
            var count_query =
                from string word in words
                orderby word.ToCharArray().Distinct().Count()
                select word.ToCharArray().Distinct().Count() + ", " + word;
            //listView1.DataSource = count_query.ToArray();

            richTextBox1.Text += count_query.ToArray().Length.ToString() + "\n";

            int len = count_query.ToArray().Length;
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (count_query.ToArray())[i].ToString() + "\n";


            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //分析文章
            string text =
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse lobortis blandit mauris, a sagittis libero. Proin a posuere justo, vel scelerisque risus.\n" +
"Sed condimentum suscipit est in sagittis. Maecenas ac nulla in metus gravida feugiat nec vel odio. Aenean vulputate urna vel gravida rhoncus.\n" +
"Etiam vel lacinia urna, non ultrices arcu. Curabitur eget neque nec felis facilisis lacinia. Donec sit amet neque vel ligula scelerisque cursus et quis nisl.\n" +
"Proin convallis metus elit, eu condimentum nunc ultrices vel. Maecenas elementum orci tellus, quis pretium risus fringilla non.\n" +
"Quisque eget diam a erat vestibulum cursus ut nec nisi. Duis non velit quis augue mattis consectetur pharetra sed dolor.\n" +
"Pellentesque luctus tempor ornare.\n" +
"Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin pellentesque dolor in leo porttitor, dignissim sollicitudin nulla bibendum.\n" +
"Nullam sit amet faucibus nunc, nec laoreet orci. Etiam nec rutrum mauris. Integer sapien felis, placerat id orci eu, fermentum porta dui.\n" +
"Nam in pharetra orci, sed sollicitudin urna. Suspendisse sit amet tellus sagittis, lobortis ante quis, consectetur est.\n" +
"Aliquam tempor ligula in augue facilisis, vehicula fermentum sem elementum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.";

            // Split the text into paragraphs.
            string[] paragraphs = text.Split('\n');

            int i = 1;
            // Draw each paragraph.
            foreach (string paragraph in paragraphs)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 行\t" + paragraph + "\n";
                // Break the text into words.
                string[] words = paragraph.Split(' ');
                foreach (string word in words)
                {
                    richTextBox1.Text += word + "_";

                }
                richTextBox1.Text += "\n";

                i++;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //DirectoryInfo
            //儲存要回傳的檔案路徑和檔案類型
            string path2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook";
            string fnShow = "檔案清單---<*.jpg>\n\n";

            //判斷資料夾是否存在，若是不存在會擲出例外情形
            try
            {    //取得檔案路徑訊息
                DirectoryInfo currentDir = new DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.jpg");
                //設定檔案的標題
                string sign = new string('-', 37);
                string fnName = "檔名", fnLength = "檔案長度";
                string fnDate = "修改日期";
                string header = fnShow + "\t" + fnName + "\t" + fnLength + "\t" + fnDate + "\n";
                richTextBox1.Text += header + "\n";
                richTextBox1.Text += sign + "\n";

                foreach (FileInfo getInfo in listFile)
                {
                    string dt = getInfo.LastWriteTime.ToShortDateString();
                    richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + dt + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無此資料夾 : " + ex.Message + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試toolTip
            richTextBox1.Text += "加入toolTip物件\n";
            richTextBox1.Text += "在Form1()的InitializeComponent()後加入訊息\n";
        }

        private void button7_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //最短路徑分析 ST
        static int length = 6;
        static string[] shortedPath = new string[length];
        static int noPath = 2000;
        static int MaxSize = 1000;
        static int[,] G =
         {
             { noPath, noPath, 10, noPath, 30, 100 },
             { noPath, noPath, 5, noPath, noPath, noPath },
             { noPath, noPath, noPath, 50, noPath, noPath },
             { noPath, noPath, noPath, noPath, noPath, 10 },
             { noPath, noPath, noPath, 20, noPath, 60 },
             { noPath, noPath, noPath, noPath, noPath, noPath }
         };
        static string[] PathResult = new string[length];

        static int[] path1 = new int[length];
        static int[,] path2 = new int[length, length];
        static int[] distance2 = new int[length];

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //最短路徑分析

            int dist1 = getShortedPath(G, 0, 1, path1);
            richTextBox1.Text += "點0到點5路徑:" + "\n";
            for (int i = 0; i < path1.Length; i++)
            {
                Console.Write(path1[i].ToString() + " ");
            }
            richTextBox1.Text += "長度:" + dist1 + "\n";


            richTextBox1.Text += "\r\n-----------------------------------------\r\n";

            int[] pathdist = getShortedPath(G, 0, path2);
            richTextBox1.Text += "點0到任意點的路徑:" + "\n";
            for (int j = 0; j < pathdist.Length; j++)
            {
                richTextBox1.Text += "點0到" + j + "的路徑:" + "\n";
                for (int i = 0; i < length; i++)
                    richTextBox1.Text += path2[j, i].ToString() + " ";
                richTextBox1.Text += "長度:" + pathdist[j] + "\n";
            }
        }

        //從某一源點出發，找到到某一結點的最短路徑
        static int getShortedPath(int[,] G, int start, int end, int[] path)
        {
            bool[] s = new bool[length]; //表示找到起始結點與當前結點間的最短路徑
            int min;  //最小距離臨時變量
            int curNode = 0; //臨時結點，記錄當前正計算結點
            int[] dist = new int[length];
            int[] prev = new int[length];

            //初始結點信息
            for (int v = 0; v < length; v++)
            {
                s[v] = false;
                dist[v] = G[start, v];
                if (dist[v] > MaxSize)
                    prev[v] = 0;
                else
                    prev[v] = start;
            }
            path[0] = end;
            dist[start] = 0;
            s[start] = true;
            //主循環
            for (int i = 1; i < length; i++)
            {
                min = MaxSize;
                for (int w = 0; w < length; w++)
                {
                    if (!s[w] && dist[w] < min)
                    {
                        curNode = w;
                        min = dist[w];
                    }
                }

                s[curNode] = true;
                for (int j = 0; j < length; j++)
                    if (!s[j] && min + G[curNode, j] < dist[j])
                    {
                        dist[j] = min + G[curNode, j];
                        prev[j] = curNode;
                    }

            }
            //輸出路徑結點
            int e = end, step = 0;
            while (e != start)
            {
                step++;
                path[step] = prev[e];
                e = prev[e];
            }
            for (int i = step; i > step / 2; i--)
            {
                int temp = path[step - i];
                path[step - i] = path[i];
                path[i] = temp;
            }
            return dist[end];
        }

        //從某一源點出發，找到到所有結點的最短路徑
        static int[] getShortedPath(int[,] G, int start, int[,] path)
        {
            int[] PathID = new int[length];//路徑（用編號表示）
            bool[] s = new bool[length]; //表示找到起始結點與當前結點間的最短路徑
            int min;  //最小距離臨時變量
            int curNode = 0; //臨時結點，記錄當前正計算結點
            int[] dist = new int[length];
            int[] prev = new int[length];
            //初始結點信息
            for (int v = 0; v < length; v++)
            {
                s[v] = false;
                dist[v] = G[start, v];
                if (dist[v] > MaxSize)
                    prev[v] = 0;
                else
                    prev[v] = start;
                path[v, 0] = v;
            }

            dist[start] = 0;
            s[start] = true;
            //主循環
            for (int i = 1; i < length; i++)
            {
                min = MaxSize;
                for (int w = 0; w < length; w++)
                {
                    if (!s[w] && dist[w] < min)
                    {
                        curNode = w;
                        min = dist[w];
                    }
                }

                s[curNode] = true;

                for (int j = 0; j < length; j++)
                {
                    if (!s[j] && min + G[curNode, j] < dist[j])
                    {
                        dist[j] = min + G[curNode, j];
                        prev[j] = curNode;
                    }
                }
            }
            //輸出路徑結點
            for (int k = 0; k < length; k++)
            {
                int e = k, step = 0;
                while (e != start)
                {
                    step++;
                    path[k, step] = prev[e];
                    e = prev[e];
                }
                for (int i = step; i > step / 2; i--)
                {
                    int temp = path[k, step - i];
                    path[k, step - i] = path[k, i];
                    path[k, i] = temp;
                }
            }
            return dist;
        }
        //最短路徑分析 SP

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //把這個檔案的註解抓出來
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

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //搜尋檔案內的文字

            string txtDirectory = @"D:\_git\vcs\_1.data\______test_files1\_case1";
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

        //多筆資料比較
        private const int CNT = 100;
        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //多筆資料比較
            //int N = 10;

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

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //氣泡排序法
        private void BubbleSort(ref int[] vArray)
        {
            int i, j, temp;
            for (i = vArray.GetUpperBound(0); i > 0; i--)  // 第幾輪Pass
            {
                for (j = 0; j < i; j++)
                {
                    if (vArray[j] > vArray[j + 1])
                    {
                        temp = vArray[j];  // 兩陣列元素內容互換
                        vArray[j] = vArray[j + 1];
                        vArray[j + 1] = temp;
                    }
                }
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //氣泡排序法

            //傳一個陣列給函數 做 氣泡排序法
            int[] myArray = new int[] { 33, 25, 16, 78, 12 };
            richTextBox1.Text += "排序前: \n";
            // 顯示排序前的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                richTextBox1.Text += myArray[i] + ",  ";
            }
            richTextBox1.Text += "\n";

            // 呼叫BubbleSort進行由小到大排序，傳遞的參數為myArray陣列
            BubbleSort(ref myArray);

            richTextBox1.Text += "排序後: \n";
            // 顯示排序後的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                richTextBox1.Text += myArray[i] + ",  ";
            }
            richTextBox1.Text += "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            // above
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //加入檔案右鍵選單

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

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }
    }
}

//6060
//------------------------------------------------------------  # 60個

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個



