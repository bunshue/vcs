using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Drawing.Text;              //for TextRenderingHint
using System.Security.Cryptography;     //for RNGCryptoServiceProvider

namespace vcs_test_all_01_Random
{
    public partial class Form1 : Form
    {
        //任意陣列
        private string[] ItemArray;
        private List<string> ItemList;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //任意陣列
            // Initialize the array and list.
            ItemArray = new string[] { "Apple", "Banana", "Cherry", "Date", "Eagle", "Fish", "Golf", "Harp", "Ibex", "Jackel", "Kangaroo" };
            ItemList = new List<string>(ItemArray);

            // Display the array and list in ListBoxes.
            lstArray.DataSource = ItemArray;
            lstList.DataSource = ItemList;
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
            dx = 160;
            dy = 70;

            pictureBox1.Size = new Size(256, 256);
            pictureBox1.Location = new Point(750, 20);

            pictureBox2.Size = new Size(256 / 2, 50);
            pictureBox2.Location = new Point(750, 20 + 256 + 10);

            pictureBox3.Size = new Size(256 / 2, 50);
            pictureBox3.Location = new Point(750 + 256 / 2, 20 + 256 + 10);

            pictureBox4.Size = new Size(256 / 2, 50);
            pictureBox4.Location = new Point(750, 20 + 256 + 10 + 50 + 10);

            pictureBox5.Size = new Size(256 / 2, 50);
            pictureBox5.Location = new Point(750 + 256 / 2, 20 + 256 + 10 + 50 + 10);

            groupBox1.Size = new Size(1060, 900);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            bt_random0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_random1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_random2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_random3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_random4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_random5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_random6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_random7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_random8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_random9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_random10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_random11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_random12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_random13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_random14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_random15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_random16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_random17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_random18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            bt_random19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(380, 900);
            richTextBox1.Location = new Point(x_st + dx * 7 - 40, y_st + dy * 0);

            int w = 280;
            int h = 50;
            x_st = 360;
            y_st = 430;
            dx = w + 10;
            dy = 46;

            tb_random_text0.Size = new Size(w, h);
            tb_random_text1.Size = new Size(w, h);
            tb_random_text2.Size = new Size(w, h);
            tb_random_text3.Size = new Size(w, h);
            tb_random_text4.Size = new Size(w, h);
            tb_random_text5.Size = new Size(w, h);
            tb_random_text6.Size = new Size(w, h);
            tb_random_text7.Size = new Size(w, h);
            tb_random_text8.Size = new Size(w, h);
            tb_random_text9.Size = new Size(w, h);
            tb_random_text10.Size = new Size(w, h);
            tb_random_text11.Size = new Size(w, h);
            tb_random_text12.Size = new Size(w, h);
            tb_random_text13.Size = new Size(w, h);
            tb_random_text14.Size = new Size(w, h);
            tb_random_text15.Size = new Size(w, h);
            tb_random_text16.Size = new Size(w, h);
            tb_random_text17.Size = new Size(w, h);
            tb_random_text18.Size = new Size(w, h);
            tb_random_text19.Size = new Size(w, h);

            tb_random_text0.Location = new Point(x_st, y_st + dy * 0);
            tb_random_text1.Location = new Point(x_st, y_st + dy * 1);
            tb_random_text2.Location = new Point(x_st, y_st + dy * 2);
            tb_random_text3.Location = new Point(x_st, y_st + dy * 3);
            tb_random_text4.Location = new Point(x_st, y_st + dy * 4);
            tb_random_text5.Location = new Point(x_st, y_st + dy * 5);
            tb_random_text6.Location = new Point(x_st, y_st + dy * 6);
            tb_random_text7.Location = new Point(x_st, y_st + dy * 7);
            tb_random_text8.Location = new Point(x_st, y_st + dy * 8);
            tb_random_text9.Location = new Point(x_st, y_st + dy * 9);
            tb_random_text10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            tb_random_text11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            tb_random_text12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            tb_random_text13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            tb_random_text14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            tb_random_text15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            tb_random_text16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            tb_random_text17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            tb_random_text18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            tb_random_text19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 960);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_random0_Click(object sender, EventArgs e)
        {
            //取得亂數的方法
            int[] rs = new int[10];
            for (int i = 0; i < 10; i++)
                rs[i] = GetRandom1();

            richTextBox1.Text += "方法一, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";

            }
            richTextBox1.Text += "\t大部分都一樣\n";


            for (int i = 0; i < 10; i++)
                rs[i] = GetRandom2();

            richTextBox1.Text += "方法二, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";

            }
            richTextBox1.Text += "\t可取得亂數\n";
        }

        private int GetRandom1()
        {
            Random r = new Random();
            return r.Next(0, 1000);
        }

        //定義一個自增的數字作為種子
        private static int _RandomSeed = (int)DateTime.Now.Ticks;
        private int GetRandom2()
        {
            if (_RandomSeed == int.MaxValue)
            {
                _RandomSeed = 1;
            }

            Random r = new Random(_RandomSeed++);
            return r.Next(0, 1000);
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

        private void bt_random3_Click(object sender, EventArgs e)
        {
        }

        private void bt_random4_Click(object sender, EventArgs e)
        {
            //C# 產生亂數的方式(Random)
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            for (int i = 0; i < 20; i++)
            {
                richTextBox1.Text += Rnd.Next(10, 21).ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void bt_random5_Click(object sender, EventArgs e)
        {
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
            //隨機產生一些英文字母, 統計各種字母出現次數

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

        private void bt_random13_Click(object sender, EventArgs e)
        {
            //建立亂七八糟陣列
            byte[] dataArray = new byte[100];//字節

            new Random().NextBytes(dataArray);//創建隨機字節

            for (int i = 0; i < dataArray.Length; i++)
            {

                //sf.WriteByte(dataArray[i]);//將字節寫入文件理.
                richTextBox1.Text += dataArray[i].ToString() + " ";

            }

        }

        private void bt_random14_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗1

            int rand = 50;
            int recordx = this.Left;　//保存原來窗體的左上角的x坐標
            int recordy = this.Top;　//保存原來窗體的左上角的y坐標

            Random random = new Random();

            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }

                this.Left = recordx;　//還原原始窗體的左上角的x坐標
                this.Top = recordy;　//還原原始窗體的左上角的y坐標
            }
            this.WindowState = FormWindowState.Maximized;
        }

        private void bt_random15_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗2
            int rand = 10;
            int recordx = this.Left;
            int recordy = this.Top;
            Random random = new Random();
            for (int i = 0; i < 50; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }
                Thread.Sleep(1);
            }
            this.Left = recordx;
            this.Top = recordy;

            this.WindowState = FormWindowState.Maximized;
        }

        private void nudgeWindow()
        {
            // 記錄視窗舊位置
            int oldLeft = Left;
            int oldTop = Top;
            // 變動位置
            Random r = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = r.Next(Left - 20, Left + 20);
                Left = left;
                int top = r.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }

        private void bt_random16_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗3
            nudgeWindow();
            this.WindowState = FormWindowState.Maximized;
        }

        private void bt_random17_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗4
            Point now_p = this.Location;
            Random r = new Random();

            for (int i = 0; i < 50; i++)
            {
                Point new_p = new Point(now_p.X + r.Next(-10, 10), now_p.Y + r.Next(-10, 10)); //新的位置
                this.Location = new_p;
                System.Threading.Thread.Sleep(20);
                this.Location = now_p; //還原位置
            }
            this.WindowState = FormWindowState.Maximized;
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

        private Color GetRandomColor2()
        {
            return Colors[random.Next(0, Colors.Length)];
        }

        //隨機顏色如下
        public static Color GetRandomColor5()
        {
            Random randomFirst = new Random((int)DateTime.Now.Ticks);
            System.Threading.Thread.Sleep(300);
            Random randomSencond = new Random((int)DateTime.Now.Ticks);
            System.Threading.Thread.Sleep(300);
            Random randomThird = new Random((int)DateTime.Now.Ticks);
            int intRed = randomFirst.Next(256);
            int intGreen = randomSencond.Next(256);
            int intBlue = randomThird.Next(256);
            return Color.FromArgb(intRed, intGreen, intBlue);
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

        void show_random_color()
        {
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
            //richTextBox1.Text += "total_colors = " + total_colors.ToString() + "\n";

            Random r = new Random();
            int sel = r.Next(total_colors);
            /*
            switch (sel)
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
            */
            int R = colorVelue[sel, 0];
            int G = colorVelue[sel, 1];
            int B = colorVelue[sel, 2];
            //richTextBox1.Text += "show color " + sel.ToString() + " " + R.ToString() + " " + G.ToString() + " " + B.ToString() + "\n";

            pictureBox4.BackColor = Color.FromArgb(R, G, B);
        }

        // 產生隨機二維陣列
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
            int i;
            int len;
            len = Colors.Length;

            Random r = new Random();
            int index = r.Next(len);

            //richTextBox1.Text += index.ToString() + " ";

            //pictureBox2.BackColor = Colors[index % len];  //same
            pictureBox2.BackColor = GetRandomColor2();          //same

            Random rd = new Random();
            pictureBox3.BackColor = Color.FromArgb(
                (byte)rd.Next(0, 255),
                (byte)rd.Next(0, 255),
                (byte)rd.Next(0, 255));

            show_random_color();

            pictureBox5.BackColor = GetRandomColor5();

            tb_random_text0.Text = RandomText0();

            tb_random_text1.Text = RandomText1();
            tb_random_text2.Text = RandomText2();

            tb_random_text5.Text = RandomText5(10);
            tb_random_text6.Text = RandomText6(10);
            tb_random_text7.Text = RandomText7();
            tb_random_text8.Text = RandomText8();
            tb_random_text9.Text = RandomText9();
            tb_random_text10.Text = RandomText10();
            tb_random_text11.Text = RandomText11();

            string result = string.Empty;
            /*
            //任意中文字, 有點問題
            int lower = 0x20;
            int upper = 0xD7FF;

            result = NextString(lower, upper, 4);
            richTextBox1.Text += result + "\n";
            */

            //亂數產生Unicode中文範圍的中文字元
            //呼叫視窗使用Unicode字串來顯示
            Console.OutputEncoding = System.Text.Encoding.Unicode;
            //產生1000字Unicode中文字
            tb_random_text3.Text = "";
            for (i = 0; i < 4; i++)
            {
                tb_random_text3.Text += getRandomUnicode().Substring(0, 1);
            }

            result = VerficationText(10);
            tb_random_text4.Text = result;

            // 產生隨機二維陣列
            Values.Randomize2();
            this.pictureBox1.Refresh();
        }

        /// <summary>  
        /// 獲取驗證碼【字符串】  
        /// </summary>  
        /// <param name="Length">驗證碼長度【必須大於0】</param>  
        /// <returns></returns>  
        public static string VerficationText(int Length)
        {
            char[] _verfication = new char[Length];
            Random _random = new Random();
            char[] _dictionary = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            for (int i = 0; i < Length; i++)
            {
                _verfication[i] = _dictionary[_random.Next(_dictionary.Length - 1)];
            }
            return new string(_verfication);
        }

        public string NextString(int charLowerBound, int charUpperBound, int length)
        {
            Random r = new Random();
            return new String(Enumerable.Repeat(0, length).Select(p => (char)r.Next(charLowerBound, charUpperBound)).ToArray());
        }

        //取得一個亂數的Unicode中文字
        private static string getRandomUnicode()
        {
            //Unicode中文字範圍
            int iMin = Convert.ToInt32("4E00", 16);
            int iMax = Convert.ToInt32("9FFF", 16); //不考慮最末16個空白
            //隨機一個中文字之整數
            System.Random oRnd = new System.Random(System.Guid.NewGuid().GetHashCode());
            int iChar = oRnd.Next(iMin, iMax);
            //整數轉成Byte[]，再轉成字串
            return System.Text.Encoding.Unicode.GetString(System.BitConverter.GetBytes(iChar));
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

        //生成大量隨機碼 ST
        private void bt_random18_Click(object sender, EventArgs e)
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

        static Random random2 = new Random();
        static string generateRandomString(int length)
        {
            var chars = "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < length; i++)
            {
                int index = random2.Next(chars.Length);
                result.Append(chars[index]);
            }
            return result.ToString();
        }
        //生成大量隨機碼 SP

        //批量生成隨機密碼, 存檔 ST
        private void bt_random19_Click(object sender, EventArgs e)
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

        private void btnPick_Click(object sender, EventArgs e)
        {
            // Pick a random line from the TextBox.
            txtResult.Text = txtNames.Lines.PickRandom();
        }

        private void button31_Click(object sender, EventArgs e)
        {
            // Pick some items.
            int num_values = 5;
            txtResult.Lines = txtNames.Lines.PickRandom(num_values).ToArray();
        }

        //任意陣列
        private void btnRandomize_Click(object sender, EventArgs e)
        {
            RandomizeLists();
        }

        private void RandomizeLists()
        {
            ItemArray.Randomize();
            ItemList.Randomize();

            // Redisplay the values.
            lstArray.DataSource = null;
            lstArray.DataSource = ItemArray;
            lstList.DataSource = null;
            lstList.DataSource = ItemList;
        }

        //RandomText ST

        //--- RandomText0 --- ST

        private string RandomText0()
        {
            //取得任意字串
            int len = 20;
            string random_pattern = CreateAndCheckCode(real_random, len);
            return random_pattern;
        }

        Random real_random = new Random(~unchecked((int)DateTime.Now.Ticks));
        private string CreateAndCheckCode(Random random, int length) // code 激活碼前綴
        {
            //char[] Pattern = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
            char[] Pattern = new char[] { '1', '2', '3', 'A', 'B', 'C' };
            string result = string.Empty;
            int n = Pattern.Length;
            for (int i = 0; i < length; i++)
            {
                int rnd = random.Next(0, n);
                result += Pattern[rnd];
            }
            return result;
        }
        //--- RandomText0 --- SP


        //--- RandomText1 --- ST
        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼
        /*
        此函數在漢字編碼范圍內隨機創建含兩個元素的十六進制字節數組，每個字節數組代表一個漢字，並將
        四個字節數組存儲在object數組中。
        參數：strlength，代表需要產生的漢字個數
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
            //產生隨機漢字
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //int len = 20;
            //調用函數產生隨機中文漢字編碼
            object[] bytes = CreateRegionCode(4);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[0], typeof(byte[])));
            string str2 = gb.GetString((byte[])Convert.ChangeType(bytes[1], typeof(byte[])));
            string str3 = gb.GetString((byte[])Convert.ChangeType(bytes[2], typeof(byte[])));
            string str4 = gb.GetString((byte[])Convert.ChangeType(bytes[3], typeof(byte[])));
            string txt = str1 + str2 + str3 + str4;
            return "隨機文字 : " + txt;
        }
        //--- RandomText1 --- SP

        //--- RandomText2 --- ST
        private string RandomText2()
        {
            //產生隨機字串
            int len = 10;
            return GenCode(len);
        }

        //--- RandomText2 --- SP


        //--- RandomText3 --- ST


        //--- RandomText3 --- SP




        //--- RandomText4 --- ST


        //--- RandomText4 --- SP


        //--- RandomText5 --- ST

        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼
        /// <summary>
        /// 隨機生成漢字
        /// </summary>
        /// <param name="strlength">長度（4位）</param>
        /// <returns></returns>
        public string RandomText5(int strlength)
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
                    r2 = rnd.Next(0, 7);
                else
                    r2 = rnd.Next(0, 16);
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

            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //根據漢字編碼的字節數組解碼出中文漢字

            string txt = string.Empty;

            for (int i = 0; i < strlength; i++)
            {
                string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));
                txt += str1;
            }
            return txt;
        }



        //--- RandomText5 --- SP




        //--- RandomText6 --- ST
        public string RandomText6(int len)
        {
            int i;
            //產生隨機漢字
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //調用函數產生隨機中文漢字編碼
            object[] bytes = CreateRegionCode2(len);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str = string.Empty;
            for (i = 0; i < len; i++)
            {
                str += gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));

            }
            return str;
        }

        /*
        此函數在漢字編碼范圍內隨機創建含兩個元素的十六進制字節數組，每個字節數組代表一個漢字，並將
        四個字節數組存儲在object數組中。
        參數：strlength，代表需要產生的漢字個數
        */
        public static object[] CreateRegionCode2(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素
            string[] rBase = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };

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
                string str_r1 = rBase[r1].Trim();

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
                string str_r2 = rBase[r2].Trim();

                //區位碼第3位
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);
                int r3 = rnd.Next(10, 16);
                string str_r3 = rBase[r3].Trim();

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
                string str_r4 = rBase[r4].Trim();

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
        //--- RandomText6 --- SP



        //--- RandomText7 --- ST
        private string RandomText7()
        {
            string random_string = GetRandomString(16);
            return random_string;
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
        //--- RandomText7 --- SP


        //--- RandomText8 --- ST
        private string RandomText8()
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

            return finalString;
        }
        //--- RandomText8 --- SP

        //--- RandomText9 --- ST
        private string RandomText9()
        {
            //隨機生成四位驗證碼（0~9，a~Z）
            int LEN = 4;
            Random r = new Random();
            string code = "0123456789abcdefghjklmnopqistuvwxyzABCDEFGHIJKLMNOPQISTUVWXYZ";
            string captcha = "";
            for (int i = 0; i < LEN; i++)
            {
                int ra = r.Next(code.Length);
                captcha = code.Substring(ra, 1) + captcha;
            }
            //richTextBox1.Text += captcha + "\n";
            return captcha;
        }
        //--- RandomText9 --- SP

        //--- RandomText10 --- ST
        private string RandomText10()
        {
            // Make the random words.
            // Get the number of words and letters per word.
            int num_letters = 10;

            // Make an array of the letters we will use.
            char[] letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();

            // Make a random number generator.
            Random rand = new Random();

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

            return word;
        }
        //--- RandomText10 --- SP

        //--- RandomText11 --- ST
        private string RandomText11()
        {
            //生成隨機字符串
            string random_str = RandomStringGenerator.GetRandomString();
            return random_str;
        }

        /// <summary> 
        /// 生成隨機字符串
        /// </summary> 
        private class RandomStringGenerator
        {
            static readonly Random r = new Random();
            const string _chars = "0123456789";
            public static string GetRandomString()
            {
                char[] buffer = new char[5];
                for (int i = 0; i < 5; i++)
                {
                    buffer[i] = _chars[r.Next(_chars.Length)];
                }
                return new string(buffer);
            }

        }

        //--- RandomText11 --- SP


        //RandomText SP
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

    public static class RandomTools
    {
        // The Random object this method uses.
        private static Random Rand = null;

        // Return a random value.
        public static T PickRandom<T>(this T[] values)
        {
            // Create the Random object if it doesn't exist.
            if (Rand == null) Rand = new Random();

            // Pick an item and return it.
            return values[Rand.Next(0, values.Length)];
        }

        // Return num_items random values.
        public static List<T> PickRandom<T>(this T[] values, int num_values)
        {
            // Create the Random object if it doesn't exist.
            if (Rand == null) Rand = new Random();

            // Don't exceed the array's length.
            if (num_values >= values.Length)
                num_values = values.Length - 1;

            // Make an array of indexes 0 through values.Length - 1.
            int[] indexes = Enumerable.Range(0, values.Length).ToArray();

            // Build the return list.
            List<T> results = new List<T>();

            // Randomize the first num_values indexes.
            for (int i = 0; i < num_values; i++)
            {
                // Pick a random entry between i and values.Length - 1.
                int j = Rand.Next(i, values.Length);

                // Swap the values.
                int temp = indexes[i];
                indexes[i] = indexes[j];
                indexes[j] = temp;

                // Save the ith value.
                results.Add(values[indexes[i]]);
            }

            // Return the selected items.
            return results;
        }
    }

    // Extension methods to randomize different kinds of collections.
    public static class RandomizationExtensions
    {
        private static Random Rand = new Random();

        // Randomize an array.
        public static void Randomize<T>(this T[] items)
        {
            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = Rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        // Randomize a list.
        public static void Randomize<T>(this List<T> items)
        {
            // Convert into an array.
            T[] item_array = items.ToArray();

            // Randomize.
            item_array.Randomize();

            // Copy the items back into the list.
            items.Clear();
            items.AddRange(item_array);
        }

        // Randomize a 2D array.
        public static void Randomize<T>(this T[,] values)
        {
            // Get the dimensions.
            int num_rows = values.GetUpperBound(0) + 1;
            int num_cols = values.GetUpperBound(1) + 1;
            int num_cells = num_rows * num_cols;

            // Randomize the array.
            for (int i = 0; i < num_cells - 1; i++)
            {
                // Pick a random cell between i and the end of the array.
                int j = Rand.Next(i, num_cells);

                // Convert to row/column indexes.
                int row_i = i / num_cols;
                int col_i = i % num_cols;
                int row_j = j / num_cols;
                int col_j = j % num_cols;

                // Swap cells i and j.
                T temp = values[row_i, col_i];
                values[row_i, col_i] = values[row_j, col_j];
                values[row_j, col_j] = temp;
            }
        }
    }
}
