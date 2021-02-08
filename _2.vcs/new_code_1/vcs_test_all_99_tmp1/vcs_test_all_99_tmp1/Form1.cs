using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;                        //for StreamReader, SearchOption
using System.Drawing.Imaging;   //for bmp2jpg
using System.Net;           //for WebClient
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process

using System.Net.NetworkInformation;    //for Ping & PingReply

namespace vcs_test_all_99_tmp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            show_item_location();
            toolTip1.SetToolTip(button6, "顯示提示訊息");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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
            dx = 160;
            dy = 60;

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

        private void richTextBox1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Up：" + e.X + " : " + e.Y;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Down：" + e.X + " : " + e.Y;
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int cnt = 0;

            DirectoryInfo dir = new DirectoryInfo("c:\\______test_files");
            richTextBox1.Text += "搜尋子目錄內的所有檔案, 子目錄 : " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            cnt = 0;
            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
            }

            FileInfo[] aaaa = dir.GetFiles();
            cnt = 0;
            richTextBox1.Text += "子目錄 " + dir.Name + " 下的檔案 :\n";
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo("c:\\______test_files");
            if (!dir.Exists)
            {
                dir = new DirectoryInfo("c:\\______test_files");
            }
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += "get file : " + file.Name + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //利用檔案的MD5碼比對兩個檔案是否相同
            //第一個檔案
            string filename1 = "C:\\______test_files\\compare\\aaaa.txt";
            //第二個檔案
            string filename2 = "C:\\______test_files\\compare\\bbbb.txt";
            //第三個檔案
            string filename3 = "C:\\______test_files\\compare\\ssss.txt";

            //第一個檔案的MD5碼
            string FileMD5_1 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] Hash1 = algorithm.ComputeHash(File.ReadAllBytes(filename1));
            //建立第一個檔案的MD5碼
            foreach (byte b in Hash1)
            {
                FileMD5_1 += b.ToString("X2");
            }

            //第二個檔案的MD5碼
            string FileMD5_2 = string.Empty;
            //取得第二個檔案MD5演算後的陣列
            byte[] Hash2 = algorithm.ComputeHash(File.ReadAllBytes(filename2));
            ///建立第二個檔案的MD5碼
            foreach (byte b in Hash2)
            {
                FileMD5_2 += b.ToString("X2");
            }

            //第三個檔案的MD5碼
            string FileMD5_3 = string.Empty;
            //取得第三個檔案MD5演算後的陣列
            byte[] Hash3 = algorithm.ComputeHash(File.ReadAllBytes(filename3));
            ///建立第三個檔案的MD5碼
            foreach (byte b in Hash3)
            {
                FileMD5_3 += b.ToString("X2");
            }

            if (FileMD5_1.Equals(FileMD5_2))
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 不相同\n";

            if (FileMD5_1.Equals(FileMD5_3))
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 不相同\n";

            if (FileMD5_2.Equals(FileMD5_3))
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 不相同\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //偵測原始檔案類型
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            //openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                string builtHex = string.Empty;
                using (Stream S = File.OpenRead(openFileDialog1.FileName))
                {
                    for (int i = 0; i < 8; i++)
                    {
                        builtHex += S.ReadByte().ToString("X2");

                        /*
                        if (ImageTypes.ContainsKey(builtHex))
                        {
                            string 真實副檔名 = ImageTypes[builtHex];
                            break;
                        }
                        */
                    }
                    richTextBox1.Text += "get " + builtHex + "\n";


                }

                //richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            var pathstr = "C://______test_files";
            if (Directory.Exists(pathstr))
            {
                //var strname=DateTime.Now.ToShortDateString().Replace("/","-")+".txt";
                var dt = DateTime.Now;
                DirectoryInfo pathinfo = new DirectoryInfo(pathstr);
                foreach (DirectoryInfo paths in pathinfo.GetDirectories())
                {
                    if (paths.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                    {
                        //paths.Delete();
                        richTextBox1.Text += "path = " + paths + "\n";
                    }
                }
            }
            else
                richTextBox1.Text += "資料夾 " + pathstr + " 不存在\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入toolTip物件\n";
            richTextBox1.Text += "在Form1()的InitializeComponent()後加入訊息\n";
        }

        //偵測原始檔案類型
        //應改用binary read
        private void button7_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "偵測原始檔案類型";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            //openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "檔案 : " + openFileDialog1.FileName + "\n";
                //richTextBox1.Text += "長度 : " + openFileDialog1.FileName.Length.ToString() + "\n";

                int len = openFileDialog1.FileName.Length;

                if (len < 10)
                {
                    richTextBox1.Text += "檔案太小, 忽略";
                    return;
                }


                len = 10;
                int[] data = new int[len];

                string builtHex = string.Empty;
                using (Stream S = File.OpenRead(openFileDialog1.FileName))
                {
                    for (int i = 0; i < 10; i++)
                    {
                        data[i] = S.ReadByte();
                        builtHex += data[i].ToString("X2") + " ";

                        /*
                        if (ImageTypes.ContainsKey(builtHex))
                        {
                            string 真實副檔名 = ImageTypes[builtHex];
                            break;
                        }
                        */
                    }
                    richTextBox1.Text += "data : " + builtHex + "\n";
                    if ((data[0] == 0x89) && (data[1] == 'P') && (data[2] == 'N') && (data[3] == 'G'))
                    {
                        richTextBox1.Text += "PNG 檔案\n";
                    }
                    else if ((data[6] == 'J') && (data[7] == 'F') && (data[8] == 'I') && (data[9] == 'F'))
                    {
                        richTextBox1.Text += "JPG 檔案\n";
                    }
                    else if ((data[0] == 'G') && (data[1] == 'I') && (data[2] == 'F') && (data[9] == '8') && (data[9] == '9'))
                    {
                        richTextBox1.Text += "GIF 檔案\n";
                    }
                    else if ((data[0] == 'B') && (data[1] == 'M'))
                    {
                        richTextBox1.Text += "BMP 檔案\n";
                    }
                    else if ((data[0] == 0xFF) && (data[1] == 0xFE))
                    {
                        richTextBox1.Text += " 純文字Unicode 檔案\n";
                    }
                    else if ((data[0] == 'I') && (data[1] == 'D') && (data[2] == '3'))
                    {
                        richTextBox1.Text += "MP3 檔案\n";
                    }
                    else
                    {
                        richTextBox1.Text += "其他 檔案\n";
                    }
                }
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
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

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //取得上一層資料夾的名稱

            richTextBox1.Text += "原目錄 : " + Application.StartupPath + "\n";

            string str = Application.StartupPath;
            string[] split_str = new string[20];
            split_str = str.Split('\\'); //以\當分隔符號
            //richTextBox1.Text += "\n";
            //richTextBox1.Text += "共有 : " + split_str.Length.ToString() + " 個項目\n";

            richTextBox1.Text += "上一層資料夾的名稱 : " + split_str[split_str.Length - 1] + "\n";

            /*
            int i = 0;
            foreach (string tmp in split_str)
            {
                i++;
                richTextBox1.Text += i.ToString() + "\t" + tmp + "\n";
            }
            */

        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
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



        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //只撈一層的所有檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_files"))
            {
                richTextBox1.Text += fname + "\n";
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //只撈一層的所有.txt檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_files", "*.txt"))
            {
                richTextBox1.Text += fname + "\n";
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(@"C:\______test_files", "*.*", System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button19_Click_1(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        string directory = @"C:\______test_files\__test_directory_to_grayscale";
        private void button21_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            SearchOption search_option;
            search_option = SearchOption.TopDirectoryOnly;
            // Look for graphic files.
            string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(directory, pattern, search_option))
                {
                    richTextBox1.Text += "find file : " + filename + "\n";
                }
            }

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(多層)
            SearchOption search_option;
            search_option = SearchOption.AllDirectories;
            // Look for graphic files.
            string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(directory, pattern, search_option))
                {
                    richTextBox1.Text += "find file : " + filename + "\n";
                }
            }

        }

        private void button23_Click(object sender, EventArgs e)
        {
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

        private void button24_Click(object sender, EventArgs e)
        {
            //C# Ping a hostname on the network

            Ping ping = new Ping();

            PingReply reply = ping.Send("www.google.com");
            if (reply.Status == IPStatus.Success)
            {
                MessageBox.Show("ok");
            } 

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //列出所有的Process
            Process[] all = Process.GetProcesses();
            int length = all.Length;
            for (int index = 0; index < length; index++)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", all[index].ProcessName, all[index].Id) + "\n";
            }

        }

        private void button26_Click(object sender, EventArgs e)
        {
            //列出firefox的Process
            Process[] ps = Process.GetProcessesByName("firefox");
            foreach (Process p in ps)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", p.ProcessName, p.Id) + "\n";
            } 
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
}
