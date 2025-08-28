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
using Microsoft.Win32;  //for RegistryKey
using System.ServiceProcess;    //參考/加入參考/.NET/System.ServiceProcess

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

        enum Animal { mouse, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, chicken, dog, pig };

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            richTextBox1.Text += "enum的用法\n";

            Animal my_animal = Animal.chicken;

            int animalNo = (int)my_animal;
            richTextBox1.Text += my_animal.ToString() + "的列舉值為 : " + animalNo + "\n";
        }

        struct person
        {
            public int age;
            public float salary;
            public string skin;
        };
        struct female
        {
            public person mary;
            public string hair;
        };

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            female female1;
            female1.mary.age = 50;
            female1.mary.salary = 23000;
            female1.mary.skin = "黃色";
            female1.hair = "直髮";
            richTextBox1.Text += "年齡："+ female1.mary.age+"\n";
            richTextBox1.Text += "收入："+ female1.mary.salary+"\n";
            richTextBox1.Text += "膚色："+ female1.mary.skin+"\n";
            richTextBox1.Text += "髮型："+ female1.hair+"\n";

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

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //多筆資料比較
        private const int CNT = 100;
        private void button7_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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


        //C# 在winform中查找控件

        /// <summary>
        /// 在winform中查找控件
        /// </summary>
        /// <param ></param>
        /// <param ></param>
        /// <returns></returns>
        private Control findControl(Control control, string controlName)
        {
            Control c1;
            foreach (Control c in control.Controls)
            {
                if (c.Name == controlName)
                {
                    return c;
                }
                else if (c.Controls.Count > 0)
                {
                    c1 = findControl(c, controlName);
                    if (c1 != null)
                    {
                        return c1;
                    }
                }
            }
            return null;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //在winform中查找控件

            //調用
            for (int i = 1; i <= 5; i++)
            {
                string _box = "button" + i.ToString();
                Button btn = (Button)this.findControl(this, _box);

                btn.BackColor = Color.Pink;
                //tb.Text = i.ToString();


                richTextBox1.Text += "i = " + i.ToString() + "\n";
            }
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

        private void button12_Click(object sender, EventArgs e)
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

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button14_Click(object sender, EventArgs e)
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

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

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
            string url = @"D:/_git/vcs/_1.data/_html/朱冶蕙老師的電腦教室.html";
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
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
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
        }
    }
}
