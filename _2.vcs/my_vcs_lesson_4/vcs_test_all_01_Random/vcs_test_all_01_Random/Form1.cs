using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;  //for TextRenderingHint
using System.Security.Cryptography;     //for RNGCryptoServiceProvider

namespace vcs_test_all_01_Random
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
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 48;


            pictureBox1.Size = new Size(256, 256);
            pictureBox1.Location = new Point(550, 20);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            bt_random1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_random2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_random3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_random4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_random5.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_random6.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_random_color.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_random_text1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_random7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_random8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_random9.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_random10.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_random11.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_random12.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            richTextBox1.Location = new Point(x_st + dx * 7 + 20, y_st + dy * 0);
            richTextBox1.Size = new Size(680, 1000);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }


        private void bt_random1_Click(object sender, EventArgs e)
        {
            Random r = new Random();
            string result1 = "";
            string result2 = "";
            string result3 = "";
            string result4 = "";
            for (int i = 0; i < 5; i++)
            {
                result1 += r.Next().ToString() + " ";
                result2 += r.Next(10).ToString() + " ";
                result3 += r.Next(10, 20).ToString() + " ";
                result4 += r.NextDouble().ToString() + " ";
            }
            richTextBox1.Text += "取>=0的亂數值：" + result1 + "\n";
            richTextBox1.Text += "取0~10的亂數值：" + result2 + "\n";
            richTextBox1.Text += "取10~20的亂數值：" + result3 + "\n";
            richTextBox1.Text += "取0.0~1.0的亂數值：" + result4 + "\n";
        }

        private void bt_random2_Click(object sender, EventArgs e)
        {
            Random r = new Random();

            int[] cards = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int tmp;

            for (int i = 0; i < cards.Length; i++)
            {
                int n = r.Next(cards.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = cards[i];
                cards[i] = cards[n];
                cards[n] = tmp;
            }
            richTextBox1.Text += "方法一結果：";
            for (int i = 0; i < cards.Length; i++)
            {
                richTextBox1.Text += cards[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < cards.Length; i++)
            {
                cards[i] = i;
            }

            for (int i = cards.Length - 1; i > 0; i--)
            {
                int n = r.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = cards[i];
                cards[i] = cards[n];
                cards[n] = tmp;
            }

            richTextBox1.Text += "方法二結果：";
            for (int i = 0; i < cards.Length; i++)
            {
                richTextBox1.Text += cards[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";



        }

        public static string GetRandomString(int length)
        {
            var str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var next = new Random();
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[next.Next(0, str.Length)]);
            }
            return builder.ToString();
        }

        private void bt_random3_Click(object sender, EventArgs e)
        {
            string random_string = GetRandomString(16);
            richTextBox1.Text += "產生任意字串 : " + random_string + "\n";

        }

        private void bt_random4_Click(object sender, EventArgs e)
        {
            //C# 產生亂數的方式(Random)
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += "number:" + Rnd.Next(10, 21).ToString() + "\n";
                //Console.WriteLine("number:" + Rnd.Next(10, 21).ToString());
            }
        }

        private void bt_random5_Click(object sender, EventArgs e)
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.

            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[8];
            var random = new Random();
            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }
            var finalString = new String(stringChars);
            richTextBox1.Text += "產生8位數亂數：" + finalString + "\n";
        }

        private void bt_random6_Click(object sender, EventArgs e)
        {
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            string name_string;
            int score_chi;
            int score_eng;
            int score_math;
            int i;

            for (i = 0; i < 20; i++)
            {
                var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                //var next = new Random();
                //Random Rnd = new Random(); //加入Random，產生的數字不會重覆
                var builder = new StringBuilder();
                int length = 5;
                int j;
                for (j = 0; j < length; j++)
                {
                    builder.Append(str[Rnd.Next(0, str.Length)]);
                }
                name_string = builder.ToString();

                score_chi = Rnd.Next(80, 100) + 1;
                score_eng = Rnd.Next(70, 100) + 1;
                score_math = Rnd.Next(60, 100) + 1;

                richTextBox1.Text += "Name : " + name_string + "\t" + score_chi.ToString() + "\t" + score_eng.ToString() + "\t" + score_math.ToString() + "\n";
            }
        }

        public static string GetRandomString3(int length)
        {
            //var str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var str = "ABCDE";
            var next = new Random();
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[next.Next(0, str.Length)]);
            }
            return builder.ToString();
        }

        private const int ROUND = 1000;
        int[] useless = new int[ROUND];

        public class MySearchInfo
        {
            public char c;
            public int cnt;
            public MySearchInfo(char c, int cc)
            {
                this.c = c;
                this.cnt = cc;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告searchinfos 為List
        // 以下List 裡為 MySearchInfo 型態
        List<MySearchInfo> result = new List<MySearchInfo>();
        private void bt_random7_Click(object sender, EventArgs e)
        {
            int i;
            int j;

            for (i = 0; i < ROUND; i++)
            {
                useless[i] = 0;
            }
            result.Clear();

            string str = GetRandomString3(ROUND);
            richTextBox1.Text += "產生任意字串 : " + str + "\n";

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += "取得字元 " + str[i] + "\n";
            }

            for (i = 0; i < ROUND; i++)
            {
                for (j = i + 1; j < ROUND; j++)
                {
                    if (useless[i] != -1)
                    {
                        //richTextBox1.Text += "compare i = " + i.ToString() + ", j = " + j.ToString() + "\n";
                        if (str[i] == str[j])
                        {
                            //richTextBox1.Text += "X";
                            useless[i]++;
                            useless[j] = -1;
                        }
                        else
                        {

                        }
                    }
                }
            }

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += useless[i].ToString() + " ";
                if (useless[i] != -1)
                {
                    //richTextBox1.Text += "found " + str[i] + " at i = " + i.ToString() + ", cnt = " + useless[i].ToString() + "\n";
                    result.Add(new MySearchInfo(str[i], (useless[i] + 1)));
                }
            }

            richTextBox1.Text += "結果:\n";
            for (i = 0; i < result.Count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 種, 字元 : " + result[i].c.ToString() + ", 出現次數 : " + result[i].cnt.ToString() + ", 比例 : " + ((double)result[i].cnt * 100 / ROUND).ToString() + " %\n";
            }

        }

        private void bt_random8_Click(object sender, EventArgs e)
        {
            byte[] data = new byte[100];
            new Random().NextBytes(data);

            richTextBox1.Text += "亂數陣列內容:\n";
            int i;
            for (i = 0; i < data.Length; i++)
            {
                richTextBox1.Text += data[i].ToString();
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                {
                    richTextBox1.Text += " ";
                }
            }
            richTextBox1.Text += "\n";
        }


        private void bt_random9_Click(object sender, EventArgs e)
        {
            int i;
            int N = 30;
            // Make an array to hold the assignment.
            int[] aa = new int[N];
            for (i = 0; i < N; i++)
                aa[i] = i;
            richTextBox1.Text += "原陣列\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += aa[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //Randomize the array
            RandomizeArray(aa);
            richTextBox1.Text += "新陣列\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += aa[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

        }

        //Randomize the array
        void RandomizeArray(int[] items)
        {
            Random Rand = new Random();
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = Rand.Next(i, items.Length);
                int temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        private void bt_random10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "整個string array都變成亂數陣列\n";
            int i;
            int N = 10;

            string[] names = new string[N];
            names[0] = "AAA";
            names[1] = "BBB";
            names[2] = "CCC";
            names[3] = "DDD";
            names[4] = "EEE";
            names[5] = "FFF";
            names[6] = "GGG";
            names[7] = "HHH";
            names[8] = "III";
            names[9] = "JJJ";

            richTextBox1.Text += "原陣列\t";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += names[i] + " ";
            }
            richTextBox1.Text += "\n";

            // Randomize.
            //Randomizer.Randomize<string>(names);  //same
            Randomizer.Randomize(names);

            richTextBox1.Text += "新陣列\t";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += names[i] + " ";
            }
            richTextBox1.Text += "\n";

            int groups = 4;
            richTextBox1.Text += "分成 " + groups.ToString() + " 組\n";
            int groupNum = 0;
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += "第 " + groupNum.ToString() + " 組\t" + names[i] + "\n";
                groupNum = ++groupNum % groups;
            }
        }

        private void bt_random11_Click(object sender, EventArgs e)
        {
            // Make the random words.
            // Get the number of words and letters per word.
            int num_letters = 10;
            int num_words = 6;
            richTextBox1.Text += "產生任意字串，每字串 " + num_letters.ToString() + " 字, 共 " + num_words.ToString() + " 個字串\n";

            // Make an array of the letters we will use.
            char[] letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();

            // Make a random number generator.
            Random rand = new Random();

            // Make the words.
            for (int i = 1; i <= num_words; i++)
            {
                // Make a word.
                string word = "";
                for (int j = 1; j <= num_letters; j++)
                {
                    // Pick a random number between 0 and 25
                    // to select a letter from the letters array.
                    int letter_num = rand.Next(0, letters.Length - 1);

                    // Append the letter.
                    word += letters[letter_num];
                }

                // Add the word to the list.
                //lstWords.Items.Add(word);
                richTextBox1.Text += word + "\n";
            }
        }

        //亂數方法比較 ST
        private void bt_random12_Click(object sender, EventArgs e)
        {
            int num_numbers;
            int min;
            int max;

            num_numbers = 20;
            min = 1;
            max = 100;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            int[] rand_numbers = new int[num_numbers];

            richTextBox1.Text += "使用內建的Random()函數建立亂數資料\n";
            Random rand = new Random();
            for (int i = 0; i < num_numbers; i++)
            {
                rand_numbers[i] = rand.Next(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "使用RNGCryptoServiceProvider函數建立亂數資料\n";

            for (int i = 0; i < num_numbers; i++)
            {
                rand_numbers[i] = RandomInteger(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        // The random number provider.
        private RNGCryptoServiceProvider Rand = new RNGCryptoServiceProvider();

        // Return a random integer between a min and max value.
        private int RandomInteger(int min, int max)
        {
            uint scale = uint.MaxValue;
            while (scale == uint.MaxValue)
            {
                // Get four random bytes.
                byte[] four_bytes = new byte[4];
                Rand.GetBytes(four_bytes);

                // Convert that into an uint.
                scale = BitConverter.ToUInt32(four_bytes, 0);
            }

            // Add min to the scaled difference between max and min.
            return (int)(min + (max - min) * (scale / (double)uint.MaxValue));
        }
        //亂數方法比較 SP

        private void bt_random_color_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "隨機顏色\t顏色陣列與使用\n";
        }


        private Color[] Colors = new Color[]
        {
            Color.AliceBlue,
            Color.AntiqueWhite,
            Color.Aqua,
            Color.Aquamarine,
            Color.Azure,
            Color.Beige,
            Color.Bisque,

            Color.Black,
            Color.BlanchedAlmond,
            Color.Blue,
            Color.BlueViolet,
            Color.Brown,
            Color.BurlyWood,
            Color.CadetBlue,

            Color.Chartreuse,
            Color.Chocolate,
            Color.Coral,
            Color.CornflowerBlue,
            Color.Cornsilk,
            Color.Crimson,
            Color.Cyan,

            Color.DarkBlue,
            Color.DarkCyan,
            Color.DarkGoldenrod,
            Color.DarkGray,
            Color.DarkGreen,
            Color.DarkKhaki,
            Color.DarkMagenta,


            Color.DarkOliveGreen,
            Color.DarkOrange,
            Color.DarkOrchid,
            Color.DarkRed,
            Color.DarkSalmon,
            Color.DarkSeaGreen,
            Color.DarkSlateBlue,

            Color.DarkSlateGray,
            Color.DarkTurquoise,
            Color.DarkViolet,
            Color.DeepPink,
            Color.DeepSkyBlue,
            Color.DimGray,
            Color.DodgerBlue,

            Color.Firebrick,
            Color.FloralWhite,
            Color.ForestGreen,
            Color.Fuchsia,
            Color.Gainsboro,
            Color.GhostWhite,
            Color.Gold,

            Color.Goldenrod,
            Color.Gray,
            Color.Green,
            Color.GreenYellow,
            Color.Honeydew,
            Color.HotPink,
            Color.IndianRed,

            Color.Indigo,
            Color.Ivory,
            Color.Khaki,
            Color.Lavender,
            Color.LavenderBlush,
            Color.LawnGreen,
            Color.LemonChiffon,

            Color.LightBlue,
            Color.LightCoral,
            Color.LightCyan,
            Color.LightGoldenrodYellow,
            Color.LightGreen,
            Color.LightGray,
            Color.LightPink,

            Color.LightSalmon,
            Color.LightSeaGreen,
            Color.LightSkyBlue,
            Color.LightSlateGray,
            Color.LightSteelBlue,
            Color.LightYellow,
            Color.Lime,

            Color.LimeGreen,
            Color.Linen,
            Color.Magenta,
            Color.Maroon,
            Color.MediumAquamarine,
            Color.MediumBlue,
            Color.MediumOrchid,

            Color.MediumPurple,
            Color.MediumSeaGreen,
            Color.MediumSlateBlue,
            Color.MediumSpringGreen,
            Color.MediumTurquoise,
            Color.MediumVioletRed,
            Color.MidnightBlue,

            Color.MintCream,
            Color.MistyRose,
            Color.Moccasin,
            Color.NavajoWhite,
            Color.Navy,
            Color.OldLace,
            Color.Olive,

            Color.OliveDrab,
            Color.Orange,
            Color.OrangeRed,
            Color.Orchid,
            Color.PaleGoldenrod,
            Color.PaleGreen,
            Color.PaleTurquoise,

            Color.PaleVioletRed,
            Color.PapayaWhip,
            Color.PeachPuff,
            Color.Peru,
            Color.Pink,
            Color.Plum,
            Color.PowderBlue,

            Color.Purple,
            Color.Red,
            Color.RosyBrown,
            Color.RoyalBlue,
            Color.SaddleBrown,
            Color.Salmon,
            Color.SandyBrown,

            Color.SeaGreen,
            Color.SeaShell,
            Color.Sienna,
            Color.Silver,
            Color.SkyBlue,
            Color.SlateBlue,
            Color.SlateGray,

            Color.Snow,
            Color.SpringGreen,
            Color.SteelBlue,
            Color.Tan,
            Color.Teal,
            Color.Thistle,
            Color.Tomato,

            Color.Turquoise,
            Color.Violet,
            Color.Wheat,
            Color.White,
            Color.WhiteSmoke,
            Color.Yellow,
            Color.YellowGreen,
        };


        private Random random = new Random();

        private Color RandomColor()
        {
            return Colors[random.Next(0, Colors.Length)];
        }

        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼
        /*
        此函数在汉字编码范围内随机创建含两个元素的十六进制字节数组，每个字节数组代表一个汉字，并将
        四个字节数组存储在object数组中。
        参数：strlength，代表需要产生的汉字个数
        */
        public static object[] CreateRegionCode(int strlength)
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
                {
                    r2 = rnd.Next(0, 7);
                }
                else
                {
                    r2 = rnd.Next(0, 16);
                }
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
            return bytes;
        }

        private string RandomText1()
        {
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //调用函数产生4个随机中文汉字编码
            object[] bytes = CreateRegionCode(4);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[0], typeof(byte[])));
            string str2 = gb.GetString((byte[])Convert.ChangeType(bytes[1], typeof(byte[])));
            string str3 = gb.GetString((byte[])Convert.ChangeType(bytes[2], typeof(byte[])));
            string str4 = gb.GetString((byte[])Convert.ChangeType(bytes[3], typeof(byte[])));
            string txt = str1 + str2 + str3 + str4;
            return "隨機文字 : " + txt;
        }

        // 產生任意矩陣
        // Some random values.
        private int[,] Values =
        {
            {1, 2, 3, 4, 5},
            {6, 7, 8, 9, 10},
            {11, 12, 13, 14, 15},
            {16, 17, 18, 19, 20},
        };

        private void timer1_Tick(object sender, EventArgs e)
        {
            //製作random color的方法
            int len;
            len = Colors.Length;

            Random r = new Random();
            int index = r.Next(len);

            //richTextBox1.Text += index.ToString() + " ";

            //bt_random_color.BackColor = Colors[index % len];  //same
            bt_random_color.BackColor = RandomColor();          //same

            bt_random_text1.Text = RandomText1();

            // 產生任意矩陣
            // Randomize.
            Values.Randomize2();
            this.pictureBox1.Refresh();

        }

        // Draw the values.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int num_rows = Values.GetUpperBound(0) + 1;
            int num_cols = Values.GetUpperBound(1) + 1;
            int col_wid = this.pictureBox1.ClientSize.Width / num_cols;
            int row_hgt = this.pictureBox1.ClientSize.Height / num_rows;

            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            using (Font the_font = new Font("Times New Roman", 20))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    int y = 0;
                    for (int row = 0; row < num_rows; row++)
                    {
                        int x = 0;
                        for (int col = 0; col < num_cols; col++)
                        {
                            Rectangle rect = new Rectangle(x, y, col_wid, row_hgt);
                            e.Graphics.DrawString(Values[row, col].ToString(), the_font, Brushes.Blue, rect, string_format);
                            x += col_wid;
                        }
                        y += row_hgt;
                    }
                }
            }
        }

        private void bt_random_text1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "隨機文字\t產生隨機簡體中文字\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //產生隨機字串
            int len = 10;
            string result = GenCode(len);

            richTextBox1.Text += "產生隨機字串 : " + result + "\n";
        }

        private string GenCode(int num)
        {
            //string str = "的一是在不123456789了Q有和人這Q中大為W上個國我以要他時來E用ASDFGHJKLIUYTREWQZXCVBNM3們生到作地R於出就分對成會可主發年動同工也能下2過子2說產43種ASDFGHJKLIUYTREWQZXCVBNM3面而方後多定行學法0所民得經十三之進著等部度sASDFGHJKLIUYTREWQZXCVBNM3家電力裡如水化高自二k123456789q加量都兩體制機9當使點從業1本去把性3好應開它E合R還因由其D些然前外天政ASDFGHJKLIUYTREWQZXCVBNM3W四日那社E義事平SWQ形RFE相a全h表間樣與關j各重新線內數正心反8你明l看原又麼z利比或T但質123456789氣第4向道命W3此變43條只DF沒結0S解a問A意建8月公0無7系軍很情AUF者4W最立代想D1已L通G並提7g直4L34題H黨123456789程展五U3果料U象員革4位入常文2總次品式活設U及AY管A特件長求w老頭基資5邊流2路F級S少圖3山統接知5TK較S將0組3見計F別她手5角期b根0論ASDFGHJKLIUYTREWQZXCVBNM3油思s術極交受U123456789聯20什認六共S權F收asdecvrrtfghujnmkiolpz證改F清D己美4再采轉更7單SD風5切U8打白J2教速花帶安IM場123456789身車J例真務具萬每目至達G走積r,示345議聲U報N斗完類0八離ASDFGHJKLIUYTREWQ123456789ZXCVBNM3華名確A才SS科張CDXG信U馬節話XZ米U整空Z元Y況D今集a溫傳土許步pGBY群廣J石記asdecvrrtfghujnmk123456789iolpz需段H4研界拉J林律叫K且究O觀越H織K6裝U影casdecvr123456789rtfghujnmkiolpzL算低持v音眾o3書t布A復TV容兒8際商Z非驗連斷HJ深難近礦千周委素M技備半辦V青VT5省PD列n習響B約s支般史d感I勞便團9往5酸歷市克何除消構府u稱太准精值號Zi率族G維XB劃選標C寫存候毛3親快2效M斯Masdecvrrtfghujnmkiolpz3院C查江4型眼5王4B按格5養N易5置M派5層片U始C卻專狀育7廠U京asdecvrrtfghujnmkiolpz識7適屬圓8包火住調m滿縣局7照參紅細引聽該鐵價嚴";
            string str = "123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ";//去掉的O容易混淆的字母
            char[] chastr = str.ToCharArray();
            // string[] source ={ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "#", "$", "%", "&", "@" };
            string code = "";
            Random rd = new Random();
            int i;
            for (i = 0; i < num; i++)
            {
                //code += source[rd.Next(0, source.Length)];
                code += str.Substring(rd.Next(0, str.Length), 1);

            }
            return code;
        }
    }

    class Randomizer
    {
        public static void Randomize<T>(T[] items)
        {
            Random rand = new Random();

            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
    }


}
