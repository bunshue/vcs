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
using System.Media;     //for SoundPlayer
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Globalization; //for CultureInfo
using System.Runtime.InteropServices;

using System.Xml;
using System.Xml.Linq;

using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False

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
            toolTip1.SetToolTip(button6, "顯示提示訊息");
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

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
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

            //1.建立Button物件
            Button[] btuArray = new Button[3];
            btuArray[0] = new Button();
            btuArray[1] = new Button();
            btuArray[2] = new Button();

            for (int i = 0; i != btuArray.Length; i++)
            {
                //2.加入控制項
                this.Controls.Add(btuArray[i]);
                btuArray[i].Size = new Size(80, 60);
                btuArray[i].Text = "Dynamic " + i;
                //btuArray[i].Top = 12 + btuArray[i].Height * i;
                //btuArray[i].Left = 13;
                btuArray[i].Location = new Point(550 + i * 90, 20);
                //3.為Click事件註冊
                btuArray[i].Click += new EventHandler(button_Click);
            }
        }

        private void button_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按下 :\t控件種類 : " + sender.ToString() + "\t";
            richTextBox1.Text += "文字 :  " + ((Button)(sender)).Text + "\t";
            richTextBox1.Text += "索引 :  " + ((Button)(sender)).TabIndex.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

            //MD5 校驗默認為32位的字符串， 而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，

            string data = "hello world";
            string key = "123";
            string result = Md5Sum(data + key);  // 返回
            richTextBox1.Text += result + "\n";

        }


        public static string Md5Sum(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            System.Security.Cryptography.MD5 md5;
            md5 = System.Security.Cryptography.MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += System.Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //DateTime Parse
            string str1 = "20091014223600";
            IFormatProvider ifp = new CultureInfo("zh-TW", true);
            DateTime dt1 = DateTime.ParseExact(str1, "yyyyMMddHHmmss", ifp);

            richTextBox1.Text += "原字串:\t" + str1 + "\n";
            richTextBox1.Text += "解讀後:\t" + dt1.ToString() + "\n";
            //MessageBox.Show(dt1.ToString());

            string str2 = "20091014223600";
            DateTime dt2;
            DateTime dtNow = DateTime.Now;
            richTextBox1.Text += "原字串:\t" + str2 + "\n";
            //IFormatProvider ifp = new CultureInfo("zh-TW", true);
            if (DateTime.TryParseExact(str2, "yyyyMMddHHmmss", ifp, DateTimeStyles.None, out dt2))
            {
                //MessageBox.Show(dt2.ToString());
                richTextBox1.Text += "解讀後1:\t" + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "解讀後2:\t" + dtNow.ToString() + "\n";
                //MessageBox.Show(dtNow.ToString());
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試toolTip
            richTextBox1.Text += "加入toolTip物件\n";
            richTextBox1.Text += "在Form1()的InitializeComponent()後加入訊息\n";
        }

        //根據文件頭判斷上傳的文件類型 ST
        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //根據文件頭判斷上傳的文件類型
            string filename = @"C:\______test_files\doraemon.jpg";
            string result = getFileType(filename);
            richTextBox1.Text += "File Type : " + result + "\n";
        }

        /// <summary>
        /// 根據文件頭判斷上傳的文件類型
        /// </summary>
        /// <param name="filePath">filePath是文件的完整路徑 </param>
        /// <returns>返回true或false</returns>
        public string getFileType(string filePath)
        {
            try
            {
                FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
                BinaryReader reader = new BinaryReader(fs);
                string fileClass;
                byte buffer;
                buffer = reader.ReadByte();
                fileClass = buffer.ToString();
                buffer = reader.ReadByte();
                fileClass += buffer.ToString();
                reader.Close();
                fs.Close();

                //richTextBox1.Text += "fileClass == " + fileClass + "\t";

                if (fileClass == "255216")
                    return "jpg";
                else if (fileClass == "7173")
                    return "gif";
                else if (fileClass == "13780")
                    return "png";
                else if (fileClass == "6677")
                    return "bmp";
                else if (fileClass == "80114")
                    return "csv";
                else if (fileClass == "6063")
                    return "xml";
                else if (fileClass == "3780")
                    return "pdf";
                else if (fileClass == "4948")
                    return "txt";
                else if (fileClass == "8075")
                    return "zip";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else
                {
                    return fileClass + "\tunknown";

                }
                // 7790是exe,8297是rar 
            }
            catch
            {
                return "unknown";
            }
        }
        //根據文件頭判斷上傳的文件類型 SP

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //創建唯一的訂單號, 考慮時間因素
            //C#創建唯一的訂單號, 考慮時間因素
            for (int i = 0; i < 10; i++)
            {
                string str = string.Format("{0}{1}", DateTime.Now.ToString("yyyyMMddHHmmss"), GetUniqueKey());
                richTextBox1.Text += str + "\n";
            }
        }

        //使用RNGCryptoServiceProvider類創建唯一的最多8位數字符串。
        private static string GetUniqueKey()
        {
            int maxSize = 8;
            int minSize = 5;
            char[] chars = new char[62];
            string a;
            a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            chars = a.ToCharArray();
            int size = maxSize;
            byte[] data = new byte[1];
            RNGCryptoServiceProvider crypto = new RNGCryptoServiceProvider();
            crypto.GetNonZeroBytes(data);
            size = maxSize;
            data = new byte[size];
            crypto.GetNonZeroBytes(data);
            StringBuilder result = new StringBuilder(size);
            foreach (byte b in data)
            {
                result.Append(chars[b % (chars.Length - 1)]);
            }
            return result.ToString();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //格式化列印

            Console.WriteLine("The value 99999 in different ways:");
            Console.WriteLine("c format : {0:c}", 99999);
            Console.WriteLine("d9 format : {0:d9}", 99999);
            Console.WriteLine("f format : {0:f3}", 99999);
            Console.WriteLine("g format : {0:g}", 99999);

            Console.WriteLine("n format : {0:n}", 99999);
            Console.WriteLine("E format : {0:E}", 99999);
            Console.WriteLine("e format : {0:e}", 99999);
            Console.WriteLine("X format : {0:X}", 99999);
            Console.WriteLine("x format : {0:x}", 99999);

            int x1 = 3;
            int x2 = 8;
            int x3 = 3;
            int x4 = 4;
            int x5 = 2;
            string xx = String.Format("{0}-{1}-{2}-{3}-{4}", x1, x2, x3, x4, x5);
            richTextBox1.Text += "xx = " + xx + "\n";

            richTextBox1.Text += "String.Format是將指定的 String類型的數據中的每個格式項替換為相應對象的值的文本等效項。 \n";

            string p1 = "Jackie";
            string p2 = "Aillo";

            richTextBox1.Text += String.Format("Hello {0}, I'm {1}", p1, p2) + "\n";
            richTextBox1.Text += String.Format("Hello {0}, I'm {1}", "Jackie", "Aillo") + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //特殊的字串解碼

            /*三組字串
            =?big5?B?W01WUF0gp96zTrjqt70gZnJvbSBNVlAgcHJpdmF0ZSBuZXdzZ3JvdXA=?=
            =?gb2312?B?S0BNUyDpX7Bs7ZjQ8g==?=
            =?utf-8?b?N+aciOS7veaVsOaNruW6k+W6lOeUqOeoi+W6j+W8gOWPkeS6uuWRmOaWsOmXu+W/q+iurw==?=
            */
            string str1 = "W01WUF0gp96zTrjqt70gZnJvbSBNVlAgcHJpdmF0ZSBuZXdzZ3JvdXA=";
            string str2 = "S0BNUyDpX7Bs7ZjQ8g==";
            string str3 = "N+aciOS7veaVsOaNruW6k+W6lOeUqOeoi+W6j+W8gOWPkeS6uuWRmOaWsOmXu+W/q+iurw==";

            string strParser1 = Encoding.GetEncoding("big5").GetString(Convert.FromBase64String(str1));
            string strParser2 = Encoding.GetEncoding("gb2312").GetString(Convert.FromBase64String(str2));
            string strParser3 = Encoding.GetEncoding("utf-8").GetString(Convert.FromBase64String(str3));

            richTextBox1.Text += "strParser1 = " + strParser1 + "\n";
            richTextBox1.Text += "strParser2 = " + strParser2 + "\n";
            richTextBox1.Text += "strParser3 = " + strParser3 + "\n";
        }

        //偵測原始檔案類型
        //應改用binary read
        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            if (MessageBox.Show("確定要休眠計算機嗎？") == DialogResult.OK)
            {
                //偽執行
                //Application.SetSuspendState(PowerState.Hibernate, true, true);
            }
        }

        //數字大寫顯示 ST
        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //數字大寫顯示
            int money = 123456;
            string result = MoneyToChinese(money.ToString());
            richTextBox1.Text += result + "\n";
        }

        public static string MoneyToChinese(string strAmount)
        {
            string functionReturnValue = null;
            bool IsNegative = false; // 是否是負數
            if (strAmount.Trim().Substring(0, 1) == "-")
            {
                // 是負數則先轉為正數
                strAmount = strAmount.Trim().Remove(0, 1);
                IsNegative = true;
            }
            string strLower = null;
            string strUpart = null;
            string strUpper = null;
            int iTemp = 0;
            // 保留兩位小數123.489→123.49　　123.4→123.4
            strAmount = Math.Round(double.Parse(strAmount), 2).ToString();
            if (strAmount.IndexOf(".") > 0)
            {
                if (strAmount.IndexOf(".") == strAmount.Length - 2)
                {
                    strAmount = strAmount + "0";
                }
            }
            else
            {
                strAmount = strAmount + ".00";
            }

            strLower = strAmount;
            iTemp = 1;
            strUpper = "";
            while (iTemp <= strLower.Length)
            {
                switch (strLower.Substring(strLower.Length - iTemp, 1))
                {
                    case ".":
                        strUpart = "圓";
                        break;
                    case "0":
                        strUpart = "零";
                        break;
                    case "1":
                        strUpart = "壹";
                        break;
                    case "2":
                        strUpart = "貳";
                        break;
                    case "3":
                        strUpart = "三";
                        break;
                    case "4":
                        strUpart = "肆";
                        break;
                    case "5":
                        strUpart = "伍";
                        break;
                    case "6":
                        strUpart = "陸";
                        break;
                    case "7":
                        strUpart = "柒";
                        break;
                    case "8":
                        strUpart = "捌";
                        break;
                    case "9":
                        strUpart = "玖";
                        break;
                }

                switch (iTemp)
                {
                    case 1:
                        strUpart = strUpart + "分";
                        break;
                    case 2:
                        strUpart = strUpart + "角";
                        break;
                    case 3:
                        strUpart = strUpart + "";
                        break;
                    case 4:
                        strUpart = strUpart + "";
                        break;
                    case 5:
                        strUpart = strUpart + "拾";
                        break;
                    case 6:
                        strUpart = strUpart + "佰";
                        break;
                    case 7:
                        strUpart = strUpart + "仟";
                        break;
                    case 8:
                        strUpart = strUpart + "萬";
                        break;
                    case 9:
                        strUpart = strUpart + "拾";
                        break;
                    case 10:
                        strUpart = strUpart + "佰";
                        break;
                    case 11:
                        strUpart = strUpart + "仟";
                        break;
                    case 12:
                        strUpart = strUpart + "億";
                        break;
                    case 13:
                        strUpart = strUpart + "拾";
                        break;
                    case 14:
                        strUpart = strUpart + "佰";
                        break;
                    case 15:
                        strUpart = strUpart + "仟";
                        break;
                    case 16:
                        strUpart = strUpart + "萬";
                        break;
                    default:
                        strUpart = strUpart + "";
                        break;
                }
                strUpper = strUpart + strUpper;
                iTemp = iTemp + 1;
            }

            strUpper = strUpper.Replace("零拾", "零");
            strUpper = strUpper.Replace("零佰", "零");
            strUpper = strUpper.Replace("零仟", "零");
            strUpper = strUpper.Replace("零零零", "零");
            strUpper = strUpper.Replace("零零", "零");
            strUpper = strUpper.Replace("零角零分", "整");
            strUpper = strUpper.Replace("零分", "整");
            strUpper = strUpper.Replace("零角", "零");
            strUpper = strUpper.Replace("零億零萬零圓", "億圓");
            strUpper = strUpper.Replace("億零萬零圓", "億圓");
            strUpper = strUpper.Replace("零億零萬", "億");
            strUpper = strUpper.Replace("零萬零圓", "萬圓");
            strUpper = strUpper.Replace("零億", "億");
            strUpper = strUpper.Replace("零萬", "萬");
            strUpper = strUpper.Replace("零圓", "圓");
            strUpper = strUpper.Replace("零零", "零");

            // 對壹圓以下的金額的處理

            if (strUpper.Substring(0, 1) == "圓")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "零")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "角")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "分")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "整")
            {
                strUpper = "零圓整";
            }

            functionReturnValue = strUpper;

            if (IsNegative == true)
            {
                return "負" + functionReturnValue;
            }
            else
            {
                return functionReturnValue;
            }
        }
        //數字大寫顯示 SP



        [DllImport("user32.dll")]
        static extern void keybd_event
        (
            byte bVk,// 虛擬鍵值  
            byte bScan,// 硬件掃描碼  
            uint dwFlags,// 動作標識  
            IntPtr dwExtraInfo// 與鍵盤動作關聯的輔加信息  
        );

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //模擬按下PrintScreen

            keybd_event((byte)0x2c, 0, 0x0, IntPtr.Zero);//down
            Application.DoEvents();
            keybd_event((byte)0x2c, 0, 0x2, IntPtr.Zero);//up
            Application.DoEvents();


        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //模擬按下Alt + PrintScreen

            keybd_event((byte)Keys.Menu, 0, 0x0, IntPtr.Zero);
            keybd_event((byte)0x2c, 0, 0x0, IntPtr.Zero);//down
            Application.DoEvents();
            Application.DoEvents();
            keybd_event((byte)0x2c, 0, 0x2, IntPtr.Zero);//up
            keybd_event((byte)Keys.Menu, 0, 0x2, IntPtr.Zero);
            Application.DoEvents();
            Application.DoEvents();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            String[, ,] items =
            new String[,,] {
            {
            { "A1", "A2", "A3", "☆", "○" },
            { "B1", "B2", "B3", "☆", "○" },
            { "C1", "C2", "C3", "☆", "○" },
            { "D1", "D2", "D3", "☆", "○" }
            }, {
            { "E1", "E2", "E3", "☆", "○" },
            { "F1", "F2", "F3", "☆", "○" },
            { "G1", "G2", "G3", "☆", "○" },
            { "H1", "H2", "H3", "☆", "○" }
            }
            };

            //GetUpperBound(0) 返回數組的第一維的索引上限，GetUpperBound(i)返回數組的i+1維的上限，GetUpperBound(Rank-1)返回數組的最後一維的上限，也就是列數-1

            System.Console.WriteLine("Items.Rank =" + items.Rank);
            System.Console.WriteLine("Items.GetUpperBound(0)=" + items.GetUpperBound(0));

            System.Console.WriteLine("Items.GetUpperBound(1)=" + items.GetUpperBound(1));
            System.Console.WriteLine("Items.GetUpperBound(2)=" + items.GetUpperBound(items.Rank - 1));

            System.Console.WriteLine("Items[0, 0, 0]=" + items[0, 0, 0]);
            System.Console.WriteLine("Items[0, 0, 1]=" + items[0, 0, 1]);
            System.Console.WriteLine("Items[0, 0, 2]=" + items[0, 0, 2]);
            System.Console.WriteLine("Items[0, 0, 3]=" + items[0, 0, 3]);
            System.Console.WriteLine("Items[0, 0, 4]=" + items[0, 0, 4]);


            System.Console.WriteLine("Items[0, 1, 0]=" + items[0, 1, 0]);
            System.Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 1]);
            System.Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 2]);
            System.Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 3]);

            System.Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 4]);

        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string result = appInfo();
            richTextBox1.Text += result + "\n";
        }

        public static string appInfo()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fvi = FileVersionInfo.GetVersionInfo(assembly.Location);
            string result = "File Version: " + fvi.FileVersion
                + Environment.NewLine + "Company Name: " + fvi.CompanyName
                + Environment.NewLine + "Comments: " + fvi.Comments
                + Environment.NewLine + "Product Name: " + fvi.ProductName
                + Environment.NewLine + "Copyright: " + fvi.LegalCopyright
                + Environment.NewLine + "File Name: " + fvi.FileName
                + Environment.NewLine + "Original File Name: " + fvi.OriginalFilename
                + Environment.NewLine + "Product Version: " + fvi.ProductVersion
                + Environment.NewLine + "Special build: " + fvi.SpecialBuild
                + Environment.NewLine + "" + fvi.CompanyName;
            return result;
        }

        //C#兩種方法判斷字符是否為漢字
        //一、用漢字的 UNICODE 編碼范圍判斷
        //漢字的 UNICODE 編碼范圍是4e00-9fbb，
        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //判斷是不是漢字
            string text = "判斷是不是漢字，ABC,keleyi.com";
            char[] c = text.ToCharArray();

            for (int i = 0; i < c.Length; i++)
            {
                richTextBox1.Text += c[i] + "\t";
                if (c[i] >= 0x4e00 && c[i] <= 0x9fbb)
                {
                    richTextBox1.Text += "是漢字\n";
                }
                else
                {
                    richTextBox1.Text += "不是漢字\n";
                }
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            byte bytRtuDataFlag = 0;
            byte bytRtuDataIdx;
            byte[] bytRtuData = new byte[8];

            int i;
            for (i = 0; i < 8; i++)
            {
                bytRtuData[i] = (byte)i;

            }
            //信息處理
            UInt16 intCRC16 = GetCheckCode(bytRtuData, 8 - 2);



            
            //Debug.Print("CRC:" + bytRtuData[8 - 2].ToString() + " " + ((byte)(intCRC16 & 0xFF)).ToString() +"|" + bytRtuData[8 - 1].ToString() + " " + ((byte)((intCRC16 >> 8) & 0xff)).ToString());

            string result = "CRC:" + bytRtuData[8 - 2].ToString() + " " + ((byte)(intCRC16 & 0xFF)).ToString() + "|" + bytRtuData[8 - 1].ToString() + " " + ((byte)((intCRC16 >> 8) & 0xff)).ToString();

            richTextBox1.Text += result + "\n";


            //bytSendData[3 + lngDataNum * 2] = (byte)(intCRC16 & 0xFF);                    //CRC校驗低位
            //bytSendData[4 + lngDataNum * 2] = (byte)((intCRC16 >> 8) & 0xff);             //CRC校驗高位                  


            //intCRC16 = GetCheckCode(bytSendData, 3);
            //bytSendData[3] = (byte)(intCRC16 & 0xFF); &nbsp;               //CRC校驗低位
            //bytSendData[4] = (byte)((intCRC16 >> 8) & 0xff);                //CRC校驗高位



                                //CRC16校驗檢驗
                    //if (bytRtuData[8 - 2] == (intCRC16 & 0xFF) && bytRtuData[8 - 1] == ((intCRC16 >> 8) & 0xff))


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

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            string filepath = "this is filepath";
            string timer = "ttttt 1";
            string timer2 = "ttttt 2";
            string username = "david";
            string pwd = "123456";

            StreamWriter sw = new StreamWriter("info.txt");
            sw.WriteLine(filepath);
            sw.Flush();
            sw.WriteLine(timer);
            sw.Flush();
            sw.WriteLine(timer2);
            sw.Flush();
            sw.WriteLine(username);
            sw.Flush();
            sw.WriteLine(pwd);
            sw.Flush();
            sw.Close();
            richTextBox1.Text += "寫入成功!\n";

            string filepathb = string.Empty;
            string timerb = string.Empty;
            string timer2b = string.Empty;
            string usernameb = string.Empty;
            string pwdb = string.Empty;

            StreamReader sr = new StreamReader("info.txt");


            filepathb = sr.ReadLine();
            timerb = sr.ReadLine();
            timer2b = sr.ReadLine();
            usernameb = sr.ReadLine();
            pwdb = sr.ReadLine();

            sr.Close();
            sr.Dispose();
            GC.Collect();


            richTextBox1.Text += "filepathb = " + filepathb + "\n";
            richTextBox1.Text += "timerb = " + timerb + "\n";
            richTextBox1.Text += "timer2b = " + timer2b + "\n";
            richTextBox1.Text += "usernameb = " + usernameb + "\n";
            richTextBox1.Text += "pwdb = " + pwdb + "\n";

        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //讀取exe版本號

            string filename = @"C:\______test_files\_material\_dll\AForge.Video.dll";

            Assembly currentAssembly = Assembly.LoadFile(filename);
            //Assembly updatedAssembly = Assembly.LoadFile(updatedAssemblyPath);

            AssemblyName currentAssemblyName = currentAssembly.GetName();
            //AssemblyName updatedAssemblyName = updatedAssembly.GetName();

            richTextBox1.Text += currentAssembly.GetName() + "\n";


        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            SendKeys.SendWait("{Tab}");

            SendKeys.SendWait("{Enter}");
            SendKeys.SendWait("123456789");

            SendKeys.SendWait("{Enter}");
            string name = "this is a lion-mouse";

            SendKeys.SendWait("{Enter}");
            foreach (char ArrayValue in name.ToCharArray())
            {
                SendKeys.SendWait(ArrayValue.ToString());
                Thread.Sleep(10);
            }

            SendKeys.SendWait("{Enter}");


            //SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Enter}");







        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        int cnt = 0;
        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //C# 模擬鍵盤操作--SendKey(),SendKeys()
            //https://www.cnblogs.com/wolfocme110/p/13444309.html

            //光标移至richTextBox1
            richTextBox1.Focus();

            //模拟按下"ABCDEFG"
            SendKeys.SendWait("(ABCDEFG)");
            SendKeys.SendWait("{left 5}");
            SendKeys.SendWait("{h 10}");

            /*
            更多举例:
            SendKeys.SendWait("^C");  //Ctrl+C 组合键
            SendKeys.SendWait("+C");  //Shift+C 组合键
            SendKeys.SendWait("%C");  //Alt+C 组合键
            SendKeys.SendWait("+(AX)");  //Shift+A+X 组合键
            SendKeys.SendWait("+AX");  //Shift+A 组合键,之后按X键
            SendKeys.SendWait("{left 5}");  //按←键 5次
            SendKeys.SendWait("{h 10}");   //按h键 10次
            SendKeys.Send("汉字");  //模拟输入"汉字"2个字
            */

            richTextBox1.Text += "到richTextBox裡面添加一些文字\n";
            richTextBox1.Focus();
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("{TAB}"); //按了Tab
            SendKeys.Send("123456");
            SendKeys.Send("{ENTER}");   //添加Enter
            SendKeys.Send("{ENTER}");
            SendKeys.Send("{ENTER}");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");

        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //LINQ to XML write
            /*
            //LINQ to XML操作Xml文檔


            //.Net中的System.Xml.Linq命名空間提供了linq to xml的支持。這個命名空間中的XDocument，XElement以及XText，XAttribute提供了讀寫xml文檔的關鍵方法。
            1. 使用linq to xml寫xml：
            使用XDocument的構造函數可以構造一個Xml文檔對象；使用XElement對象可以構造一個xml節點元素，使用XAttribute構造函數可以構造元素的屬性；使用XText構造函數可以構造節點內的文本。
            */


            var xDoc = new XDocument(new XElement("root",
                new XElement("dog",
                    new XText("dog said black is a beautify color"),
                    new XAttribute("color", "black")),
                new XElement("cat"),
                new XElement("pig", "pig is great")));

            //xDoc輸出xml的encoding是系統默認編碼，對於簡體中文操作系統是gb2312
            //默認是縮進格式化的xml，而無須格式化設置
            xDoc.Save("aaaa.xml");


            //LINQ to XML read


            var query = from item in xDoc.Element("root").Elements()
                        select new
                        {
                            TypeName = item.Name,
                            Saying = item.Value,
                            Color = item.Attribute("color") == null ? (string)null : item.Attribute("color").Value
                        };


            foreach (var item in query)
            {
                Console.WriteLine("{0} 's color is {1},{0} said {2}", item.TypeName, item.Color ?? "Unknown", item.Saying ?? "nothing");
                richTextBox1.Text += item.TypeName + "\t" + item.Color + "\n";
            }
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
