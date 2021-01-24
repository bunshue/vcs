using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Debug

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

        #region 任意陣列
        private string[] ItemArray;
        private List<string> ItemList;
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            textBox2.Text = "123";

            #region 任意陣列
            // Initialize the array and list.
            ItemArray = new string[] { "Apple", "Banana", "Cherry", "Date", "Eagle", "Fish", "Golf", "Harp", "Ibex", "Jackel", "Kangaroo" };
            ItemList = new List<string>(ItemArray);

            // Display the array and list in ListBoxes.
            lstArray.DataSource = ItemArray;
            lstList.DataSource = ItemList;
            #endregion

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 11+10);
            label2.Location = new Point(x_st + dx * 1 / 2, y_st + dy * 11+10);
            textBox_A.Location = new Point(x_st + dx * 0 + 20, y_st + dy * 11+10);
            textBox_B.Location = new Point(x_st + dx * 1 / 2 + 20, y_st + dy * 11+10);

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
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            txtNumber.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 7);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            textBox2.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            lb_ordinal.Location = new Point(x_st + dx * 2 + dx / 6, y_st + dy * 11);

            bt_random1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_random2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_random3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_random4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_random5.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_random6.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_random7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_random8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_random9.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_random10.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_random11.Location = new Point(x_st + dx * 1, y_st + dy * 5);

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


            richTextBox1.Text += "求log以a為底的b\n";
            double b = 1024;
            double a = 2;
            double c = Math.Log(b) / Math.Log(a);
            richTextBox1.Text += "a = " + a.ToString() + "\n";
            richTextBox1.Text += "b = " + b.ToString() + "\n";
            richTextBox1.Text += "結果\tc = " + c.ToString() + "\n";
            richTextBox1.Text += "驗算\ta^c = " + Math.Pow(a, c).ToString() + "\n";
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

        // Use Euclid's algorithm to calculate the
        // greatest common divisor (GCD) of two numbers.
        private long GCD2(long a, long b)
        {
            a = Math.Abs(a);
            b = Math.Abs(b);

            // Pull out remainders.
            for (; ; )
            {
                long remainder = a % b;
                if (remainder == 0) return b;
                a = b;
                b = remainder;
            };
        }

        // Return the least common multiple
        // (LCM) of two numbers.
        private long LCM2(long a, long b)
        {
            return a * b / GCD2(a, b);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //最大公因數
            int w = 1920;
            int h = 1080;
            int gcd = GCD(w, h);
            richTextBox1.Text += "最大公因數 = " + gcd.ToString() + "\n";
            richTextBox1.Text += "ratio = " + (w / gcd).ToString() + " : " + (h / gcd).ToString() + "\n";

            w = 1280;
            h = 720;
            gcd = GCD(w, h);
            richTextBox1.Text += "最大公因數 = " + gcd.ToString() + "\n";
            richTextBox1.Text += "ratio = " + (w / gcd).ToString() + " : " + (h / gcd).ToString() + "\n";


            richTextBox1.Text += "最大公因數 另法\n";
            long A = 36;
            long B = 84;
            richTextBox1.Text += A.ToString() + " 和 " + B.ToString() + " 的最大公因數 = " + GCD2(A, B).ToString() + "\n";
            richTextBox1.Text += A.ToString() + " 和 " + B.ToString() + " 的最小公倍數 = " + LCM2(A, B).ToString() + "\n";
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
            int[] aaa = new int[] { 16, 19, 14, 17, 27, 37, 47 };
            for (int i = 0; i < aaa.Length; i++)
            {
                bool result;
                result = IsPrime(aaa[i]);
                if (result == true)
                    richTextBox1.Text += "數字 " + aaa[i] + " 質數\n";
                else
                    richTextBox1.Text += "數字 " + aaa[i] + " ----\n";
            }
        }

        // Return true if the number is prime.
        private bool IsPrime(int num)
        {
            // Handle 1 and 2 separately.
            if (num == 1) return false;
            if (num == 2) return true;
            if (num % 2 == 0) return false;

            // See if the number is divisible by odd values up to Sqrt(number).
            int sqrt = (int)(Math.Sqrt(num) + 1);
            for (int i = 3; i < sqrt; i++)
                if (num % i == 0) return false;

            // If we get here, the number is prime.
            return true;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            double number;
            double root;
            double result;
            double check;

            number = 125;
            root = 3;
            result = Math.Pow(number, 1 / root);
            richTextBox1.Text += "計算 :\t" + number.ToString() + " 的 " + root.ToString() + " 次方根 :\t" + result.ToString() + "\n";
            check = Math.Pow(result, root);
            richTextBox1.Text += "驗算 :\t" + result.ToString() + " 的 " + root.ToString() + " 次方 :\t" + check.ToString() + "\n";

            number = 123;
            root = 2.34;
            result = Math.Pow(number, 1 / root);
            richTextBox1.Text += "計算 :\t" + number.ToString() + " 的 " + root.ToString() + " 次方根 :\t" + result.ToString() + "\n";
            check = Math.Pow(result, root);
            richTextBox1.Text += "驗算 :\t" + result.ToString() + " 的 " + root.ToString() + " 次方 :\t" + check.ToString() + "\n";

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
            long A;
            long max_B;
            long remainder;
            long C;

            A = 96679683;
            richTextBox1.Text += "數字 " + A.ToString() + " 拆成立方和\n";
            max_B = (long)Math.Pow(A / 2.0, 1.0 / 3.0);
            if (2 * max_B * max_B * max_B < A)
                max_B++;

            // Try numbers up to the cube root of A.
            for (int B = 0; B <= max_B; B++)
            {
                remainder = A - (B * B * B);
                C = (long)Math.Round(Math.Pow(remainder, 1.0 / 3.0));
                if (C * C * C == remainder)
                {
                    richTextBox1.Text +=
                        B + "^3 + " +
                        C + "^3 = " +
                        (B * B * B) + " + " + (C * C * C) + "\n";
                }
            }

            A = 87539319;
            richTextBox1.Text += "數字 " + A.ToString() + " 拆成立方和\n";
            max_B = (long)Math.Pow(A / 2.0, 1.0 / 3.0);
            if (2 * max_B * max_B * max_B < A)
                max_B++;

            // Try numbers up to the cube root of A.
            for (int B = 0; B <= max_B; B++)
            {
                remainder = A - (B * B * B);
                C = (long)Math.Round(Math.Pow(remainder, 1.0 / 3.0));
                if (C * C * C == remainder)
                {
                    richTextBox1.Text +=
                        B + "^3 + " +
                        C + "^3 = " +
                        (B * B * B) + " + " + (C * C * C) + "\n";
                }
            }


        }


        private void button15_Click(object sender, EventArgs e)
        {
            //因數分解
            long number;

            number = 1234567890;
            // Get the factors.
            List<long> factors = FindFactors(number);
            List<string> strings = factors.ConvertAll<string>(x => x.ToString());

            richTextBox1.Text += "數字: " + number.ToString() + ", 因數分解\n";
            richTextBox1.Text += string.Join(" x ", strings.ToArray()) + "\n";
        }

        // Return the number's prime factors.
        private List<long> FindFactors(long num)
        {
            List<long> result = new List<long>();

            // Take out the 2s.
            while (num % 2 == 0)
            {
                result.Add(2);
                num /= 2;
            }

            // Take out other primes.
            long factor = 3;
            while (factor * factor <= num)
            {
                if (num % factor == 0)
                {
                    // This is a factor.
                    result.Add(factor);
                    num /= factor;
                }
                else
                {
                    // Go to the next odd number.
                    factor += 2;
                }
            }

            // If num is not 1, then whatever is left is prime.
            if (num > 1) result.Add(num);

            return result;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "排列\n";
            string pattern = "apple banana cat dog";

            // Get the items.
            string[] items = pattern.Split(' ');

            int i;
            int len = items.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += items[i] + "\n";
            }

            // Generate the permutations.
            List<List<string>> results = GeneratePermutations<string>(items.ToList());

            // Display the results.
            foreach (List<string> combination in results)
            {
                richTextBox1.Text += string.Join(" ", combination.ToArray()) + "\n";
            }

            // Calculate the number of permutations.
            long num_permutations = Factorial(items.Length);
            richTextBox1.Text += "共有 " + num_permutations.ToString() + " 種排列\n";
        }

        // Generate permutations.
        private List<List<T>> GeneratePermutations<T>(List<T> items)
        {
            // Make an array to hold the
            // permutation we are building.
            T[] current_permutation = new T[items.Count];

            // Make an array to tell whether
            // an item is in the current selection.
            bool[] in_selection = new bool[items.Count];

            // Make a result list.
            List<List<T>> results = new List<List<T>>();

            // Build the combinations recursively.
            PermuteItems<T>(items, in_selection,
                current_permutation, results, 0);

            // Return the results.
            return results;
        }

        // Recursively permute the items that are
        // not yet in the current selection.
        private void PermuteItems<T>(List<T> items, bool[] in_selection,
            T[] current_permutation, List<List<T>> results, int next_position)
        {
            // See if all of the positions are filled.
            if (next_position == items.Count)
            {
                // All of the positioned are filled.
                // Save this permutation.
                results.Add(current_permutation.ToList());
            }
            else
            {
                // Try options for the next position.
                for (int i = 0; i < items.Count; i++)
                {
                    if (!in_selection[i])
                    {
                        // Add this item to the current permutation.
                        in_selection[i] = true;
                        current_permutation[next_position] = items[i];

                        // Recursively fill the remaining positions.
                        PermuteItems<T>(items, in_selection,
                            current_permutation, results, next_position + 1);

                        // Remove the item from the current permutation.
                        in_selection[i] = false;
                    }
                }
            }
        }

        // Calculate N!
        private long Factorial(long n)
        {
            long result = 1;
            for (int i = 2; i <= n; i++) result *= i;
            return result;
        }
        
        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "M項中取N項\n";
            string pattern = "apple banana cat dog elephant";

            // Get the items.
            string[] items = pattern.Split(' ');

            int i;
            int len = items.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += items[i] + "\n";
            }

            int M = len;
            int N = 3;

            // Generate the selections.
            List<List<string>> results = GenerateSelections<string>(items.ToList(), N);

            richTextBox1.Text += M.ToString() + " 項中取 " + N.ToString() + " 項：\n";

            // Display the results.
            foreach (List<string> combination in results)
            {
                richTextBox1.Text += string.Join(" ", combination.ToArray()) + "\n";
            }

            // Calculate the number of items.
            decimal num_combinations = MChooseK(M, N);
            richTextBox1.Text += "共有 " + num_combinations.ToString() + " 種組合\n";
        }

        // Generate selections of n items.
        private List<List<T>> GenerateSelections<T>(List<T> items, int n)
        {
            // Make an array to tell whether
            // an item is in the current selection.
            bool[] in_selection = new bool[items.Count];

            // Make a result list.
            List<List<T>> results = new List<List<T>>();

            // Build the combinations recursively.
            SelectItems<T>(items, in_selection, results, n, 0);

            // Return the results.
            return results;
        }

        // Recursively select n additional items with indexes >= first_item.
        // If n == 0, add the current combination to the results.
        private void SelectItems<T>(List<T> items, bool[] in_selection,
            List<List<T>> results, int n, int first_item)
        {
            if (n == 0)
            {
                // Add the current selection to the results.
                List<T> selection = new List<T>();
                for (int i = 0; i < items.Count; i++)
                {
                    // If this item is selected, add it to the selection.
                    if (in_selection[i]) selection.Add(items[i]);
                }
                results.Add(selection);
            }
            else
            {
                // Try adding each of the remaining items.
                for (int i = first_item; i < items.Count; i++)
                {
                    // Try adding this item.
                    in_selection[i] = true;

                    // Recursively add the rest of the required items.
                    SelectItems(items, in_selection, results, n - 1, i + 1);

                    // Remove this item from the selection.
                    in_selection[i] = false;
                }
            }
        }

        // Return M choose N calculated directly.
        // For a description of the algorithm, see:
        //      http://csharphelper.com/blog/2014/08/calculate-the-binomial-coefficient-n-choose-k-efficiently-in-c/
        private decimal MChooseK(decimal M, decimal N)
        {
            //Debug.Assert(M >= 0);
            //Debug.Assert(N >= 0);
            //Debug.Assert(M >= N);

            decimal result = 1;
            for (int i = 1; i <= N; i++)
            {
                result *= M - (N - i);
                result /= i;
            }
            return result;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_all_cases();
        }

        void show_all_cases()
        {
            int i;
            // Display the original values.
            string[] value_array =
            {
                //"Ankylosaurus", "Brachiosaurus", "Caenagnathus",
                //"Diplodocus", "Enigmosaurus","Fabrosaurus",
                "A", "B", "C",
                "D", "E","F",
            };
            int len = value_array.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += value_array[i] + "\n";
            }

            richTextBox1.Text += "From Array\n";
            // Display pairs from the array.
            foreach (PairsTools.Pair<string> pair in value_array.Pairs())
            {
                richTextBox1.Text += pair + "\n";
            }

            // Make a list holding the values.
            List<string> value_list = new List<string>();
            foreach (string value in value_array)
            {
                value_list.Add(value);
            }

            richTextBox1.Text += "From IEnumerable\n";

            // Display pairs from the list.
            foreach (PairsTools.Pair<string> pair in value_list.Pairs())
            {
                richTextBox1.Text += pair + "\n";
            }
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(@"C:\______test_files\_material\sddev1.png");
            e.Graphics.DrawImage(bitmap1, 8, this.ClientSize.Height - bitmap1.Height - 8);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //埃及分數

            // Calculate the Eqgyptian fraction representation
            // for the original fraction.

            // Get the fraction (and make it positive).
            Fraction frac = new Fraction(textBox1.Text);
            if (frac < 0) frac = -frac;

            // Get the Egyptian fraction.
            List<Fraction> fractions = GetEgyptianFraction(frac);

            // Display the result as a string
            string result = "";
            foreach (Fraction unit_fraction in fractions)
            {
                result = result + unit_fraction.ToString() + " + ";
            }
            if (result.Length > 0) result = result.Substring(0, result.Length - 3);

            //txtResult.Text = result;
            richTextBox1.Text += result + "\n";


        }

        // Return a string representation of the Egyptian fraction.
        private List<Fraction> GetEgyptianFraction(Fraction frac)
        {
            List<Fraction> result = new List<Fraction>();

            // Remove any whole number part.
            int whole_part = (int)(frac.Numerator / frac.Denominator);
            if (whole_part > 0)
            {
                result.Add(whole_part);
                frac = frac - whole_part;
            }

            // Pull out unit fractions.
            long denom = 2;
            while (frac > 0)
            {
                // Make the unit fraction smaller until it fits.
                Fraction unit_fraction = new Fraction(1, denom);
                while (unit_fraction > frac)
                {
                    denom++;
                    unit_fraction = new Fraction(1, denom);
                }

                // Remove the unit fraction.
                result.Add(unit_fraction);
                frac -= unit_fraction;
                denom++;
            }

            return result;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            try
            {
                Fraction a = new Fraction(textBox_A.Text);
                Fraction b = new Fraction(textBox_B.Text);

                richTextBox1.Text += "A加B\t" + (a + b).ToString() + "\n";
                richTextBox1.Text += "A減B\t" + (a - b).ToString() + "\n";
                richTextBox1.Text += "A乘B\t" + (a * b).ToString() + "\n";
                richTextBox1.Text += "A除B\t" + (a / b).ToString() + "\n";
                richTextBox1.Text += "A反相\t" + (-a).ToString() + "\n";
                richTextBox1.Text += "A轉小數\t" + ((double)a).ToString() + "\n";



            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

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

        private void button22_Click(object sender, EventArgs e)
        {
            //把數字讀出來
            double num = double.Parse(txtNumber.Text);
            richTextBox1.Text += "原數字:\t" + num.ToString() + "\n";
            richTextBox1.Text += "讀出來:\t" + num.ToWords() + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "使用 Euler's Sieve 計算質數\n";

            // Make the sieve.
            int max = 5000;
            richTextBox1.Text += "數字 " + max.ToString() + " 以下的質數\n";
            bool[] is_prime = MakeSieve(max);

            // Display the primes.
            int num_primes = 0;
            for (int i = 2; i <= max; i++)
            {
                if (is_prime[i])
                {
                    if (num_primes <= 10000)
                    {
                        richTextBox1.Text += i.ToString() + " ";
                    }
                    num_primes++;
                }
            }
            if (num_primes > 10000)
            {
                richTextBox1.Text += "...";
            }
            richTextBox1.Text += "\n";

            // Display the estimated and actual number of primes.
            // Display a Legendre estimate ?(n) = n/(log(n) - 1.08366).
            // See http://mathworld.wolfram.com/PrimeCountingFunction.html.
            double est = (max / (Math.Log(max) - 1.08366));
            richTextBox1.Text += "預估質數 : " + est.ToString("0") + " 個\n";
            richTextBox1.Text += "實際質數 : " + num_primes.ToString() + " 個\n";
        }

        // Build Euler's Sieve.
        private bool[] MakeSieve(int max)
        {
            // Make an array indicating whether numbers are prime.
            bool[] is_prime = new bool[max + 1];
            is_prime[2] = true;
            for (int i = 3; i <= max; i += 2) is_prime[i] = true;

            // Cross out multiples of odd primes.
            for (int p = 3; p <= max; p += 2)
            {
                // See if i is prime.
                if (is_prime[p])
                {
                    // Knock out multiples of p.
                    int max_q = max / p;
                    if (max_q % 2 == 0) max_q--;    // Make it odd.
                    for (int q = max_q; q >= p; q -= 2)
                    {
                        // Only use q if it is prime.
                        if (is_prime[q]) is_prime[p * q] = false;
                    }
                }
            }
            return is_prime;
        }

        #region 各種進位轉換
        // Get the value from the sender and
        // display it in the other TextBoxes.
        private bool ignore_events = false;
        private void TextBox_TextChanged(object sender, EventArgs e)
        {
            // Don't recurse.
            if (ignore_events) return;
            ignore_events = true;

            // Get the sender as a TextBox.
            TextBox source = sender as TextBox;

            // Get the value.
            long value = 0;
            try
            {
                switch (source.Name)
                {
                    case "txtDecimal":
                        // Parse a decimal value.
                        value = long.Parse(source.Text);
                        break;
                    case "txtHexadecimal":
                        // Parse a hexadecimal value.
                        value = Convert.ToInt64(source.Text, 16);
                        break;
                    case "txtOctal":
                        // Parse an octal value.
                        value = Convert.ToInt64(source.Text, 8);
                        break;
                    case "txtBinary":
                        // Parse a binary value.
                        value = Convert.ToInt64(source.Text, 2);
                        break;
                    default:
                        throw new Exception("Unknown control " + source.Name);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error parsing input\n\n" + ex.Message,
                    "Input Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

            // Display the value in different formats.
            if (source.Name != "txtDecimal")
            {
                txtDecimal.Text = value.ToString();
            }
            if (source.Name != "txtHexadecimal")
            {
                txtHexadecimal.Text = Convert.ToString(value, 16);
            }
            if (source.Name != "txtOctal")
            {
                txtOctal.Text = Convert.ToString(value, 8);
            }
            if (source.Name != "txtBinary")
            {
                txtBinary.Text = Convert.ToString(value, 2);
            }

            ignore_events = false;
        }
        #endregion

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

        #region 任意陣列
        // Randomize the array and list.
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
        #endregion

        // Display the ordinal version of the number.
        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            // Parse the value and display its ordinal extension.
            try
            {
                int value = int.Parse(textBox2.Text, System.Globalization.NumberStyles.Any);
                lb_ordinal.Text = "序數 : " + value.ToString("#,##0 ") + value.ToOrdinal();
            }
            catch
            {
                textBox2.Clear();
            }
        }

        //N階乘 ST
        private void button24_Click(object sender, EventArgs e)
        {
            decimal N = 10;
            try
            {
                richTextBox1.Text += N.ToString() + " 階乘 = " + Factorial(N).ToString() + "\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
            }
        }

        // Calculate N!
        private decimal Factorial(decimal N)
        {
            decimal result = 1;
            for (decimal i = 2; i <= N; i++)
                result *= i;
            return result;
        }
        //N階乘 SP

        //找質數個數 ST
        private void button25_Click(object sender, EventArgs e)
        {
            // Make the sieve.
            int max = 10000;

            richTextBox1.Text += "尋找從 2 到 " + max.ToString() + " 之間的質數\n";

            // Display a Legendre estimate ?(n) = n/(log(n) - 1.08366).
            // See http://mathworld.wolfram.com/PrimeCountingFunction.html.
            double est = (max / (Math.Log(max) - 1.08366));
            richTextBox1.Text += "預估的質數有 " + est.ToString("0") + " 個\n";

            richTextBox1.Text += "前100個\n";
            bool[] is_prime = MakeSieve2(max);
            // Display the primes.
            int num_primes = 0;
            for (int i = 2; i <= max; i++)
                if (is_prime[i])
                {
                    if (num_primes <= 100)
                    {
                        richTextBox1.Text += i.ToString() + "   ";
                    }
                    num_primes++;
                }

            richTextBox1.Text += "\n";
            richTextBox1.Text += "總共找到 " + num_primes.ToString() + " 個質數\n";

        }


        // Build a Sieve of Eratosthenes.
        private bool[] MakeSieve2(int max)
        {
            // Make an array indicating whether numbers are prime.
            bool[] is_prime = new bool[max + 1];
            is_prime[2] = true;
            for (int i = 3; i <= max; i += 2) is_prime[i] = true;

            // Cross out multiples of odd primes.
            for (int i = 3; i <= max; i += 2)
            {
                // See if i is prime.
                if (is_prime[i])
                {
                    // Knock out multiples of i.
                    for (int j = i * 3; j <= max; j += i)
                        is_prime[j] = false;
                }
            }
            return is_prime;
        }

        //找質數個數 SP

        private void button26_Click(object sender, EventArgs e)
        {
            // Get N and K.
            decimal M = 10;
            decimal N = 3;
            decimal result;

            richTextBox1.Text += "C(M, N) = C(" + M.ToString() + ", " + N.ToString() + "), 使用方法1\n";
            // Calculate using factorials.
            try
            {
                result = MChooseNFactorial(M, N);
                richTextBox1.Text += "結果 = " + result.ToString() + "\n";
            }
            catch
            {
                richTextBox1.Text += "錯誤.....1\n";
            }

            richTextBox1.Text += "C(M, N) = C(" + M.ToString() + ", " + N.ToString() + "), 使用方法2\n";
            // Calculate using the more direct method.
            try
            {
                result = NChooseK(M, N);
                richTextBox1.Text += "結果 = " + result.ToString() + "\n";
            }
            catch
            {
                richTextBox1.Text += "錯誤.....2\n";
            }


            M = 26;
            N = 3;

            richTextBox1.Text += "C(M, N) = C(" + M.ToString() + ", " + N.ToString() + "), 使用方法1\n";
            // Calculate using factorials.
            try
            {
                result = MChooseNFactorial(M, N);
                richTextBox1.Text += "結果 = " + result.ToString() + "\n";
            }
            catch
            {
                richTextBox1.Text += "錯誤.....1\n";
            }

            richTextBox1.Text += "C(M, N) = C(" + M.ToString() + ", " + N.ToString() + "), 使用方法2\n";
            // Calculate using the more direct method.
            try
            {
                result = NChooseK(M, N);
                richTextBox1.Text += "結果 = " + result.ToString() + "\n";
            }
            catch
            {
                richTextBox1.Text += "錯誤.....2\n";
            }
        }

        // Return N choose K calculated directly.
        // For a description of the algorithm, see:
        //      http://csharphelper.com/blog/2014/08/calculate-the-binomial-coefficient-n-choose-k-efficiently-in-c/
        private decimal NChooseK(decimal N, decimal K)
        {
            Debug.Assert(N >= 0);
            Debug.Assert(K >= 0);
            Debug.Assert(N >= K);

            decimal result = 1;
            for (int i = 1; i <= K; i++)
            {
                result *= N - (K - i);
                result /= i;
            }
            return result;
        }

        // Use the Factorial function to calculate M choose N.
        private decimal MChooseNFactorial(decimal M, decimal N)
        {
            Debug.Assert(M >= 0);
            Debug.Assert(N >= 0);
            Debug.Assert(M >= N);
            richTextBox1.Text += "MChooseNFactorial M = " + M.ToString() + "\tN = " + N.ToString() + "\n";

            return Factorial(M) / Factorial(N) / Factorial(M - N);
        }




    }
}
