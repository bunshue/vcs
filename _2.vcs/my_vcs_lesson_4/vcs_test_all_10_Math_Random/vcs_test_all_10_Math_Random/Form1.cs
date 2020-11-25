using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_10_Math_Random
{
    public partial class Form1 : Form
    {

        /*  準備做標準差的數字 70 個
        sd_num = [16  19  14  17  4  4  11  27  9  8  8  12  29  28  5  18  13  7  8  4  26  25  15  6  8  12  26  13  13  27  12  3  1  8  4  22  28  23  23  19  29  17  12  17  28  19  25  16  12  7  23  1  19  24  1  21  4  8  9  22  8  27  15  12  25  6  11  22  25  13  ];
        int[] sd_num = new int[] {16, 19, 14, 17, 4, 4, 11, 27, 9, 8, 8, 12, 29, 28, 5, 18, 13, 7, 8, 4, 26, 25, 15, 6, 8, 12, 26, 13, 13, 27, 12, 3, 1, 8, 4, 22, 28, 23, 23, 19, 29, 17, 12, 17, 28, 19, 25, 16, 12, 7, 23, 1, 19, 24, 1, 21, 4, 8, 9, 22, 8, 27, 15, 12, 25, 6, 11, 22, 25, 13};
        Average	15.04285714
        StdDev(true)	8.30651170	same as Matlab
        StdDev(false)	8.24696605
        */

        int[] sd_num = new int[] { 16, 19, 14, 17, 4, 4, 11, 27, 9, 8, 8, 12, 29, 28, 5, 18, 13, 7, 8, 4, 26, 25, 15, 6, 8, 12, 26, 13, 13, 27, 12, 3, 1, 8, 4, 22, 28, 23, 23, 19, 29, 17, 12, 17, 28, 19, 25, 16, 12, 7, 23, 1, 19, 24, 1, 21, 4, 8, 9, 22, 8, 27, 15, 12, 25, 6, 11, 22, 25, 13 };

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
            dy = 50;

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

            bt_random1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_random2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_random3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_random4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_random5.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_random6.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_random7.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_random8.Location = new Point(x_st + dx * 0, y_st + dy * 8);



            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }


        private void button0_Click(object sender, EventArgs e)
        {
            int r = 5;
            int value = -5;
            int aa = 123;
            int bb = 456;

            richTextBox1.Text += "圓面積 = " + (Math.PI * Math.Pow(r, 2)).ToString() + "\n";
            richTextBox1.Text += "-5的絕對值 = " + (Math.Abs(value)).ToString() + "\n";
            richTextBox1.Text += "兩者取大 = " + (Math.Max(aa, bb)).ToString() + "\n";
            richTextBox1.Text += "兩者取小 = " + (Math.Min(aa, bb)).ToString() + "\n";
            richTextBox1.Text += "根號2 = " + (Math.Sqrt(2)).ToString() + "\n";

            float result = 0;
            int a = 11;
            int b = 3;
            int c = 0;
            result = (float)a / b;
            richTextBox1.Text += "result = " + result.ToString() + "\n";
            c = (int)Math.Round(result);
            richTextBox1.Text += "四捨五入c = " + c.ToString() + "\n";
            c = (int)Math.Floor(result);
            richTextBox1.Text += "無條件捨去c = " + c.ToString() + "\n";
            c = (int)Math.Ceiling(result);
            richTextBox1.Text += "無條件進位c = " + c.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pi = " + Math.PI.ToString() + "\n";
            richTextBox1.Text += "e = " + Math.E.ToString() + "\n";
        
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "冪運算(Exponentiation), 又稱指數運算\n";

            richTextBox1.Text += "2^10 =\t" + Math.Pow(2, 10).ToString() + "\n";
            richTextBox1.Text += "3^8 =\t" + Math.Pow(3, 8).ToString() + "\n";
            richTextBox1.Text += "2 的平方根 = \t" + Math.Pow(2, 0.5).ToString() + "\n";
            richTextBox1.Text += "8 的(-1/3)方根 = \t" + Math.Pow(8, -1 / 3).ToString() + "\n"; //error, should be 1/2

            richTextBox1.Text += "\n對數運算\n";
            richTextBox1.Text += "log2 = \t" + Math.Log10(2).ToString() + "\n";
            richTextBox1.Text += "ln2 = \t" + Math.Log(2).ToString() + "\n";

            richTextBox1.Text += "exp(1) = \t" + Math.Exp(1).ToString() + "\n";
            richTextBox1.Text += "exp(2) = \t" + Math.Exp(2).ToString() + "\n";

        }



        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int x;
            int y;
            richTextBox1.Text += "y = sin(x)\n";
            for (x = 0; x <= 360; x += 30)
            {
                y = (int)(100 * sind(x));
                richTextBox1.Text += "x = " + x.ToString() + ", y = " + y.ToString() + "\n";
            }

            for (x = 0; x <= 360; x += 30)
            {
                richTextBox1.Text += "x = " + x.ToString() + "\t" + (rad(x) / Math.PI).ToString() + " pi rad\t" + 100 * sind(x) + "\n";
            }

        }

        /// <summary> 
        /// 標準差(StandardDifference) 
        /// </summary> 
        /// <param name="val"></param> 
        /// <returns></returns> 
        public double SD(double[] a)
        {
            int len;
            double avg;
            double sd;
            int i;

            len = a.Length;
            avg = a.Average();
            if (len <= 1)
            {
                sd = 0;
                richTextBox1.Text += "SD = " + sd.ToString() + "\n";
                return sd;
            }

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            richTextBox1.Text += "average = " + avg.ToString() + "\n";
            sd = 0;
            for (i = 0; i < len; i++)
            {
                sd += Math.Pow((a[i] - avg), 2);
            }
            sd /= (len - 1);
            sd = Math.Sqrt(sd);

            return sd;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //一維陣列用法：
            double[] sd_num = new double[] { 16, 19, 14, 17, 4, 4, 11, 27, 9, 8, 8, 12, 29, 28, 5, 18, 13, 7, 8, 4, 26, 25, 15, 6, 8, 12, 26, 13, 13, 27, 12, 3, 1, 8, 4, 22, 28, 23, 23, 19, 29, 17, 12, 17, 28, 19, 25, 16, 12, 7, 23, 1, 19, 24, 1, 21, 4, 8, 9, 22, 8, 27, 15, 12, 25, 6, 11, 22, 25, 13 };
            double sd;
            sd = SD(sd_num);
            richTextBox1.Text += "SD = " + sd.ToString() + "\n";
        }


        /// <summary> 
        /// 標準差(StandardDifference) 
        /// </summary> 
        /// <param name="val"></param> 
        /// <returns></returns> 
        public double SD2(List<double> val)
        {
            if (val.Count > 1)
            {
                double avg = val.Average();
                double _result = (from a in val select Math.Pow(a - avg, 2)).Sum();
                if (avg > 0 && _result > 0)
                {
                    double _sum = _result / (double)(val.Count - 1);
                    double _Sqrt = Math.Sqrt(_sum);
                    return _Sqrt;
                }
                else
                    return 0;
            }
            else if (val.Count == 1)
            {
                return 0;
            }
            else
            {
                return 0;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            double[] sd_num = new double[] { 16, 19, 14, 17, 4, 4, 11, 27, 9, 8, 8, 12, 29, 28, 5, 18, 13, 7, 8, 4, 26, 25, 15, 6, 8, 12, 26, 13, 13, 27, 12, 3, 1, 8, 4, 22, 28, 23, 23, 19, 29, 17, 12, 17, 28, 19, 25, 16, 12, 7, 23, 1, 19, 24, 1, 21, 4, 8, 9, 22, 8, 27, 15, 12, 25, 6, 11, 22, 25, 13 };

            List<double> arrays = new List<double>();

            int i;
            for (i = 0; i < sd_num.Length; i++)
                arrays.Add(sd_num[i]);

            double sd;
            sd = SD2(arrays);
            richTextBox1.Text += "SD = " + sd.ToString() + "\n";
        }

        private const int CNT = 70;
        private void button6_Click(object sender, EventArgs e)
        {
            //一維陣列用法：
            double[] sd_num = new double[] { 16, 19, 14, 17, 4, 4, 11, 27, 9, 8, 8, 12, 29, 28, 5, 18, 13, 7, 8, 4, 26, 25, 15, 6, 8, 12, 26, 13, 13, 27, 12, 3, 1, 8, 4, 22, 28, 23, 23, 19, 29, 17, 12, 17, 28, 19, 25, 16, 12, 7, 23, 1, 19, 24, 1, 21, 4, 8, 9, 22, 8, 27, 15, 12, 25, 6, 11, 22, 25, 13 };

            //一維陣列用法：
            double[] a = new double[CNT];

            int i;
            Random r = new Random();
            for (i = 0; i < CNT; i++)
            {
                a[i] = r.NextDouble();
            }

            for (i = 0; i < CNT; i++)
            {
                a[i] = sd_num[i];
            }

            double sd;
            sd = SD(a);
            richTextBox1.Text += "SD = " + sd.ToString() + "\n";
        }

        private const int RND = 20;
        double[] awb_r = new double[RND];
        double[] awb_b = new double[RND];
        double[] right_left_point_cnt = new double[RND];
        double[] down_up_point_cnt = new double[RND];
        double[] awb_block = new double[RND];

        private void button7_Click(object sender, EventArgs e)
        {
            awb_r[0] = 1578; awb_b[0] = 1594; right_left_point_cnt[0] = 60; down_up_point_cnt[0] = -60; awb_block[0] = 28;	//for vcs
            awb_r[1] = 1583; awb_b[1] = 1591; right_left_point_cnt[1] = 60; down_up_point_cnt[1] = -60; awb_block[1] = 28;	//for vcs
            awb_r[2] = 1586; awb_b[2] = 1600; right_left_point_cnt[2] = 70; down_up_point_cnt[2] = -60; awb_block[2] = 24;	//for vcs
            awb_r[3] = 1573; awb_b[3] = 1589; right_left_point_cnt[3] = 60; down_up_point_cnt[3] = -60; awb_block[3] = 32;	//for vcs
            awb_r[4] = 1575; awb_b[4] = 1590; right_left_point_cnt[4] = 70; down_up_point_cnt[4] = -55; awb_block[4] = 24;	//for vcs
            awb_r[5] = 1571; awb_b[5] = 1599; right_left_point_cnt[5] = 60; down_up_point_cnt[5] = -60; awb_block[5] = 32;	//for vcs
            awb_r[6] = 1582; awb_b[6] = 1597; right_left_point_cnt[6] = 70; down_up_point_cnt[6] = -60; awb_block[6] = 24;	//for vcs
            awb_r[7] = 1573; awb_b[7] = 1595; right_left_point_cnt[7] = 60; down_up_point_cnt[7] = -60; awb_block[7] = 32;	//for vcs
            awb_r[8] = 1571; awb_b[8] = 1587; right_left_point_cnt[8] = 60; down_up_point_cnt[8] = -55; awb_block[8] = 24;	//for vcs
            awb_r[9] = 1577; awb_b[9] = 1590; right_left_point_cnt[9] = 60; down_up_point_cnt[9] = -60; awb_block[9] = 32;	//for vcs
            awb_r[10] = 1581; awb_b[10] = 1580; right_left_point_cnt[10] = 60; down_up_point_cnt[10] = -60; awb_block[10] = 24;	//for vcs
            awb_r[11] = 1576; awb_b[11] = 1600; right_left_point_cnt[11] = 60; down_up_point_cnt[11] = -60; awb_block[11] = 32;	//for vcs
            awb_r[12] = 1531; awb_b[12] = 1491; right_left_point_cnt[12] = -10; down_up_point_cnt[12] = 70; awb_block[12] = 24;	//for vcs
            awb_r[13] = 1566; awb_b[13] = 1583; right_left_point_cnt[13] = 60; down_up_point_cnt[13] = -55; awb_block[13] = 24;	//for vcs
            awb_r[14] = 1575; awb_b[14] = 1599; right_left_point_cnt[14] = 60; down_up_point_cnt[14] = -60; awb_block[14] = 32;	//for vcs
            awb_r[15] = 1574; awb_b[15] = 1603; right_left_point_cnt[15] = 60; down_up_point_cnt[15] = -60; awb_block[15] = 32;	//for vcs
            awb_r[16] = 1572; awb_b[16] = 1596; right_left_point_cnt[16] = 60; down_up_point_cnt[16] = -60; awb_block[16] = 32;	//for vcs
            awb_r[17] = 1589; awb_b[17] = 1590; right_left_point_cnt[17] = 70; down_up_point_cnt[17] = -60; awb_block[17] = 24;	//for vcs
            awb_r[18] = 1569; awb_b[18] = 1598; right_left_point_cnt[18] = 60; down_up_point_cnt[18] = -60; awb_block[18] = 32;	//for vcs
            awb_r[19] = 1571; awb_b[19] = 1592; right_left_point_cnt[19] = 60; down_up_point_cnt[19] = -60; awb_block[19] = 32;	//for vcs

            double sd;

            sd = SD(awb_r);
            richTextBox1.Text += "awb_r SD = " + sd.ToString() + "\n";

            sd = SD(awb_b);
            richTextBox1.Text += "awb_b SD = " + sd.ToString() + "\n";

            /*
            sd = SD(right_left_point_cnt);
            richTextBox1.Text += "right_left_point_cnt SD = " + sd.ToString() + "\n";

            sd = SD(down_up_point_cnt);
            richTextBox1.Text += "down_up_point_cnt SD = " + sd.ToString() + "\n";

            sd = SD(awb_block);
            richTextBox1.Text += "awb_block SD = " + sd.ToString() + "\n";
            */

        }


        private void button8_Click(object sender, EventArgs e)
        {
            //By C# Helper

            // Make the values.
            Random rand = new Random();
            const int num_values = 70;

            //Array version.
            int[] values = new int[num_values];

            for (int i = 0; i < num_values; i++)
            {
                values[i] = rand.Next(1, 30);
            }

            for (int i = 0; i < num_values; i++)
            {
                values[i] = sd_num[i];
            }

            richTextBox1.Text += "aaa=[";
            for (int i = 0; i < num_values; i++)
            {
                richTextBox1.Text += values[i].ToString() + "  ";
            }
            richTextBox1.Text += "];\n";

            richTextBox1.Text += "int[] bbb = new int[] {";
            for (int i = 0; i < num_values; i++)
            {
                richTextBox1.Text += values[i].ToString();
                if (i != (num_values - 1))
                    richTextBox1.Text += ", ";
            }
            richTextBox1.Text += "};\n";

            // Display statistics.
            richTextBox1.Text += "Average\t" + values.Average().ToString("0.00000000") + "\n";
            richTextBox1.Text += "StdDev(true)\t" + values.StdDev(true).ToString("0.00000000") + "\tsame as Matlab\n";
            richTextBox1.Text += "StdDev(false)\t" + values.StdDev(false).ToString("0.00000000") + "\n";


        }




        int GCD(int a, int b)
        {
            if (a % b == 0)
                return b;
            else
                return GCD(b, a % b);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //最大公因數
            int w = 1920;
            int h = 1080;
            int gcd = GCD(w, h);
            richTextBox1.Text += "gcd = " + gcd.ToString() + "\n";
            richTextBox1.Text += "ratio = " + (w / gcd).ToString() + " : " + (h / gcd).ToString() + "\n";

            w = 1280;
            h = 720;
            gcd = GCD(w, h);
            richTextBox1.Text += "gcd = " + gcd.ToString() + "\n";
            richTextBox1.Text += "ratio = " + (w / gcd).ToString() + " : " + (h / gcd).ToString() + "\n";


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

        private void button10_Click(object sender, EventArgs e)
        {
            nudgeWindow();
        }


        private void button11_Click(object sender, EventArgs e)
        {
            Point now_p = this.Location;
            Random r = new Random();

            for (int i = 0; i < 50; i++)
            {
                Point new_p = new Point(now_p.X + r.Next(-10, 10), now_p.Y + r.Next(-10, 10)); //新的位置
                this.Location = new_p;
                System.Threading.Thread.Sleep(20);
                this.Location = now_p; //還原位置
            }

        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        public static string GetRandomString2(int length)
        {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            //var next = new Random();
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[Rnd.Next(0, str.Length)]);
            }
            return builder.ToString();
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


        private void button14_Click(object sender, EventArgs e)
        {
        }


        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        
        private void button17_Click(object sender, EventArgs e)
        {

        }



        private void button18_Click(object sender, EventArgs e)
        {
        }

        private const int SEARCH_NUMBER = 10;
        private void button19_Click(object sender, EventArgs e)
        {
            //TBD

            /*
            int i;
            int j;
            bool flag_digit_0_ok = false;
            bool flag_digit_7_ok = false;
            for (i = 1; i < SEARCH_NUMBER; i++)
            {
                for (j = i; j < 10000; j++)
                {



                }


            }
            */
        }



        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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


        //不用宣告長度的陣列(Array)
        // 宣告searchinfos 為List
        // 以下List 裡為MyFileInfo 型態
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

    }
}
