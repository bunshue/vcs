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

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
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
            string str1 = "https://ja.wikipedia.org/wiki/和 製 英 語";

            richTextBox1.Text += "原字串(a)\t\t" + str1 + "\n";
            richTextBox1.Text += "原字串空白轉nbsp(b)\t" + str1.SpaceToNbsp() + "\n";

            string str2 = str1.UrlEncode();

            richTextBox1.Text += "原字串特殊符號編碼(c)\t" + str2 + "\n";

            richTextBox1.Text += "(c)再解碼\t\t" + str2.UrlDecode() + "\n";

            richTextBox1.Text += "(b)目前無法解碼\n";
            richTextBox1.Text += "\n";

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
            richTextBox1.Text += "僅顯示上下午幾點幾分幾秒:\t" + DateTime.Now.ToString("T") + "\n";
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

        //由日期找出星座 ST
        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //由日期找出星座
            int month = 3;
            int day = 11;
            string result = getAstro(month, day);
            richTextBox1.Text += result + "\n";
        }

        private static String getAstro(int month, int day)
        {
            String[] starArr = { "魔羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座" };
            int[] DayArr = { 22, 20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22 };  // 兩個星座分割日
            int index = month;
            // 所查詢日期在分割日之前，索引-1，否則不變
            if (day < DayArr[month - 1])
            {
                index = index - 1;
            }
            index = index % 12;
            // 返回索引指向的星座string
            return starArr[index];
        }
        //由日期找出星座 SP

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲得中文星期名稱
            richTextBox1.Text += "今天是 : " + GetCnWeek() + "\n";
        }

        /// <summary>
        /// 獲得中文星期名稱
        /// </summary>
        /// <returns></returns>
        public static string GetCnWeek()
        {
            switch (DateTime.Now.DayOfWeek)
            {
                case DayOfWeek.Monday:
                    return "星期一";
                case DayOfWeek.Tuesday:
                    return "星期二";
                case DayOfWeek.Wednesday:
                    return "星期三";
                case DayOfWeek.Thursday:
                    return "星期四";
                case DayOfWeek.Friday:
                    return "星期五";
                case DayOfWeek.Saturday:
                    return "星期六";
                case DayOfWeek.Sunday:
                    return "星期日";
                default:
                    return "星期一";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //星期幾
            richTextBox1.Text += CaculateWeekDay(2021, 10, 28);


            //C#獲取當前星期幾的三種方法

            //第一種：

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string weekday = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += weekday + "\n";

            //第二種：

            richTextBox1.Text += System.Globalization.CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(DateTime.Now.DayOfWeek) + "\n";

            //第三種：

            string dt;
            string week = string.Empty;
            dt = DateTime.Today.DayOfWeek.ToString();
            switch (dt)
            {
                case "Monday":
                    week = "星期一";
                    break;
                case "Tuesday":
                    week = "星期二";
                    break;
                case "Wednesday":
                    week = "星期三";
                    break;
                case "Thursday":
                    week = "星期四";
                    break;
                case "Friday":
                    week = "星期五";
                    break;
                case "Saturday":
                    week = "星期六";
                    break;
                case "Sunday":
                    week = "星期日";
                    break;
                default:
                    week = "星期日";
                    break;
            }
            richTextBox1.Text += week + "\n";
        }

        /*
        C#實現的根據年月日計算星期幾的函數

        基姆拉爾森計算公式

        W= (d 2*m 3*(m 1)/5 y y/4-y/100 y/400) mod 7

        在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。
        */

        //y－年，m－月，d－日期
        string CaculateWeekDay(int y, int m, int d)
        {
            if (m == 1) m = 13;
            if (m == 2) m = 14;
            int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7 + 1;

            string weekstr = "";
            switch (week)
            {
                case 1: weekstr = "星期一"; break;
                case 2: weekstr = "星期二"; break;
                case 3: weekstr = "星期三"; break;
                case 4: weekstr = "星期四"; break;
                case 5: weekstr = "星期五"; break;
                case 6: weekstr = "星期六"; break;
                case 7: weekstr = "星期日"; break;
            } return weekstr;
        }

        //生成大量隨機碼 ST
        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
        //生成大量隨機碼 SP

        //批量生成隨機密碼, 存檔 ST
        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
            for (int j = 0; j < 1000; j++)
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
        //批量生成隨機密碼, 存檔 SP

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
            //從mp3中提取信息 1
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

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //從mp3中提取信息 2
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

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //播放wav檔
            string filename = @"C:\______test_files\_wav\start.wav";
            SoundPlayer player = new SoundPlayer(); //声明一个控制WAV文件的声音播放文件对象
            player.SoundLocation = filename; //指定声音文件的路径
            player.LoadAsync();  //设置播放的方法
            player.Play(); //播放声音文件
        }

        //GPS定位，经纬度附近地点查询–C#实现方法 ST


        /// <summary>
        /// 经纬度坐标
        /// </summary>

        public class Degree
        {
            public Degree(double x, double y)
            {
                X = x;
                Y = y;
            }
            private double x;

            public double X
            {
                get { return x; }
                set { x = value; }
            }
            private double y;

            public double Y
            {
                get { return y; }
                set { y = value; }
            }
        }


        public class CoordDispose
        {
            private const double EARTH_RADIUS = 6378137.0;//地球半径(米)

            /// <summary>
            /// 角度数转换为弧度公式
            /// </summary>
            /// <param name="d"></param>
            /// <returns></returns>
            private static double radians(double d)
            {
                return d * Math.PI / 180.0;
            }

            /// <summary>
            /// 弧度转换为角度数公式
            /// </summary>
            /// <param name="d"></param>
            /// <returns></returns>
            private static double degrees(double d)
            {
                return d * (180 / Math.PI);
            }

            /// <summary>
            /// 计算两个经纬度之间的直接距离
            /// </summary>

            public static double GetDistance(Degree Degree1, Degree Degree2)
            {
                double radLat1 = radians(Degree1.X);
                double radLat2 = radians(Degree2.X);
                double a = radLat1 - radLat2;
                double b = radians(Degree1.Y) - radians(Degree2.Y);

                double s = 2 * Math.Asin(Math.Sqrt(Math.Pow(Math.Sin(a / 2), 2) +
                 Math.Cos(radLat1) * Math.Cos(radLat2) * Math.Pow(Math.Sin(b / 2), 2)));
                s = s * EARTH_RADIUS;
                s = Math.Round(s * 10000) / 10000;
                return s;
            }

            /// <summary>
            /// 计算两个经纬度之间的直接距离(google 算法)
            /// </summary>
            public static double GetDistanceGoogle(Degree Degree1, Degree Degree2)
            {
                double radLat1 = radians(Degree1.X);
                double radLng1 = radians(Degree1.Y);
                double radLat2 = radians(Degree2.X);
                double radLng2 = radians(Degree2.Y);

                double s = Math.Acos(Math.Cos(radLat1) * Math.Cos(radLat2) * Math.Cos(radLng1 - radLng2) + Math.Sin(radLat1) * Math.Sin(radLat2));
                s = s * EARTH_RADIUS;
                s = Math.Round(s * 10000) / 10000;
                return s;
            }

            /// <summary>
            /// 以一个经纬度为中心计算出四个顶点
            /// </summary>
            /// <param name="distance">半径(米)</param>
            /// <returns></returns>
            public static Degree[] GetDegreeCoordinates(Degree Degree1, double distance)
            {
                double dlng = 2 * Math.Asin(Math.Sin(distance / (2 * EARTH_RADIUS)) / Math.Cos(Degree1.X));
                dlng = degrees(dlng);//一定转换成角度数  原PHP文章这个地方说的不清楚根本不正确 后来lz又查了很多资料终于搞定了

                double dlat = distance / EARTH_RADIUS;
                dlat = degrees(dlat);//一定转换成角度数

                return new Degree[] { new Degree(Math.Round(Degree1.X + dlat,6), Math.Round(Degree1.Y - dlng,6)),//left-top
                                  new Degree(Math.Round(Degree1.X - dlat,6), Math.Round(Degree1.Y - dlng,6)),//left-bottom
                                  new Degree(Math.Round(Degree1.X + dlat,6), Math.Round(Degree1.Y + dlng,6)),//right-top
                                  new Degree(Math.Round(Degree1.X - dlat,6), Math.Round(Degree1.Y + dlng,6)) //right-bottom
            };

            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //GPS定位，经纬度附近地点查询–C#实现方法
            double a = CoordDispose.GetDistance(new Degree(116.412007, 39.947545), new Degree(116.412924, 39.947918));//116.416984,39.944959
            double b = CoordDispose.GetDistanceGoogle(new Degree(116.412007, 39.947545), new Degree(116.412924, 39.947918));
            Degree[] dd = CoordDispose.GetDegreeCoordinates(new Degree(116.412007, 39.947545), 102);

            richTextBox1.Text += a + " " + b + "\n";
            richTextBox1.Text += dd[0].X + "," + dd[0].Y + "\n";
            richTextBox1.Text += dd[3].X + "," + dd[3].Y + "\n";
        }
        //GPS定位，经纬度附近地点查询–C#实现方法 SP

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


        // 顏色模板
        //  黑、白、紅、綠、藍、黃/ 棕 、灰
        private const int BLACK = 0;
        private const int WHITE = 1;
        private const int RED1 = 2;
        private const int RED2 = 3;
        private const int GREEN1 = 4;
        private const int GREEN2 = 5;
        private const int BLUE1 = 6;
        private const int BLUE2 = 7;
        private const int YELLOW1 = 8;
        private const int YELLOW2 = 9;
        private const int BROWN = 10;
        private const int GRAY = 11;

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //顯示顏色
            int[,] colorVelue = null;
            colorVelue = new int[,] {
            {50,50,50},    //黑
            {255,255,255},  //白
            {240,80,80}, //紅小
            {240,160,160},  //紅大
            {60,180,60}, //綠小
            {160,240,160},  //綠大
            {80,80,240}, //藍小
            {160,160,240},  //藍大
            {240,190,80}, //黃小
            {240,240,160},  //黃大
            {205,133,63},   //棕/褐
            //{162,162,162},//灰，特殊
            };

            int total_colors = colorVelue.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_colors = " + total_colors.ToString() + "\n";

            int i;
            for (i = 0; i < total_colors; i++)
            {
                switch (i)
                {
                    case -1:
                        richTextBox1.Text += "無此色\n";
                        break;
                    case 0:
                        richTextBox1.Text += "黑\n";
                        break;
                    case 1:
                        richTextBox1.Text += "白\n";
                        break;
                    case 2:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 3:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 4:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 5:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 6:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 7:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 8:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 9:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 10:
                        richTextBox1.Text += "棕\n";
                        break;
                    case 11:
                        richTextBox1.Text += "灰\n";
                        break;
                    default:
                        richTextBox1.Text += "其他\n";
                        break;
                }

                int R = colorVelue[i, 0];
                int G = colorVelue[i, 1];
                int B = colorVelue[i, 2];
                richTextBox1.Text += "show color " + i.ToString() + " " + R.ToString() + " " + G.ToString() + " " + B.ToString() + "\n";

                ((Button)sender).BackColor = Color.FromArgb(R, G, B);
                Application.DoEvents();
                Thread.Sleep(1000);

            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //建立亂七八糟陣列
            byte[] dataArray = new byte[100];//字節

            new Random().NextBytes(dataArray);//創建隨機字節

            for (int i = 0; i < dataArray.Length; i++)
            {

                //sf.WriteByte(dataArray[i]);//將字節寫入文件理.
                richTextBox1.Text += dataArray[i].ToString() + " ";

            }

        }


    }

    static class StringExtensions
    {
        // Extension to replace spaces with &nbsp;
        public static string SpaceToNbsp(this string s)
        {
            return s.Replace(" ", "&nbsp;");
        }

        // Url encode an ASCII string.
        public static string UrlEncode(this string s)
        {
            return HttpUtility.UrlEncode(s);
        }

        // Url decode an ASCII string.
        public static string UrlDecode(this string s)
        {
            return HttpUtility.UrlDecode(s);
        }
    }
}
