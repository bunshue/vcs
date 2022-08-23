using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace _client
{
    public partial class Form2 : Form
    {
        int cnt_name = 0, right_num = 0, score = 0, x1 = 0, a = 0;

        private Hashtable name_score = new Hashtable(); // 使用hashtable 來記錄暱稱與分數 的資訊
        public static string namescore;
        public string NAMESCORE
        {

            set { namescore = value; }


            get { return namescore; }

        }

        static string Sname;
        public string SNAME
        {

            set { Sname = value; }


            get { return Sname; }

        }

        public Form2()
        {
            InitializeComponent();

        }

        private void Form2_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            right_num += 1;
            button3.Enabled = false;
            label3.Visible = true;
            label4.Visible = true;
            timer1.Enabled = true;
            timer2.Enabled = false;
            a = 10;
            label4.Text = "玩家" + Sname + " 的分數為 :" + score.ToString();
            label3.Text = "你已答了" + right_num.ToString() + "題";
            label6.Text = "放棄了...";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            if (x1 == 1)
            {
                if (radioButton1.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                    a = 10;
                }
                right_num += 1;
            }
            else if (x1 == 2)
            {
                if (radioButton2.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                    a = 10;
                }
                right_num += 1;
            }
            else if (x1 == 3)
            {
                if (radioButton3.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                }
                right_num += 1;
            }
            else if (x1 == 4)
            {
                if (radioButton4.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                    a = 10;
                }
                right_num += 1;
            }
            else if (x1 == 5)
            {
                if (radioButton4.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                    a = 10;
                }
                right_num += 1;
            }
            else if (x1 == 6)
            {
                if (radioButton4.Checked == true)
                {
                    label6.Text = Sname + " 恭喜你答對了 ";
                    score = score + 20;
                    a = 10;
                }
                else
                {
                    label6.Text = Sname + " 你答錯了 ";
                    score -= 5;
                    a = 10;
                }
                right_num += 1;
            }
            button2.Enabled = false;
            label3.Visible = true;
            label4.Visible = true;
            label6.Visible = true;

            timer1.Enabled = true; //出題目
            timer2.Enabled = false;//秒數

            label4.Text = "玩家" + Sname + " 的分數為 :" + score.ToString();
            label3.Text = "你已答了" + right_num.ToString() + "題";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            
            int[] avg = new int[5];
            string[] name = new string[5];
            string[] str = new string[10];
            string tempAVG;

            int i = 0, num = 0;
            int[] found = new int[5];
            foreach (DictionaryEntry de in name_score)
            {
                str[num] = (string)de.Key;
                ++num;
            }

            foreach (string t in str) //分解字串存入陣列
            {
                if (str[i] != null)
                {

                    found[i] = t.IndexOf("|");
                    name[i] = t.Substring(0, (found[i]));
                    tempAVG = t.Substring(found[i] + 1);
                    avg[i] = int.Parse(tempAVG);
                    ++i;
                }

            }

            Array.Sort(avg, name);

            for (i = 0; i < num; ++i)
            {
                label18.Text = label18.Text + "第" + (i + 1) + "名" + name[4 - i] + "   " + avg[4 - i].ToString() + "分\n";
            }
           
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            label7.Text = a.ToString();
            a -= 1;

            if (label7.Text != "0")
            {
                timer1.Enabled = false;//出題目
                timer2.Enabled = true; //秒數
            }
            else
            {
                timer1.Enabled = true;//出題目
                timer2.Enabled = false;//秒數
                a = 10;
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
           // label2.Text = "玩家" + Sname;
            label3.Text = " 你已答了" + right_num + " 題";
            timer1.Enabled = false;
            timer2.Enabled = false;

            if (cnt_name == 1)
            {
                label8.Text = "參賽者 :" + Sname;
                label13.Text = score.ToString() + "分";

            }
           // label8.Text = label8.Text;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            button2.Enabled = true;
            string s1;
            button3.Enabled = true;


            string[] a = new string[] {"世界高樓之ㄧ台北101高度為何? A:508 B:408 C:500 D:498 請作答?",
                                       "中正紀念館改為何名? A:馬英九紀念館 B:台灣民主紀念館 C:陳水扁紀念館 D:228紀念館 請作答?",
                                       "請問 2012年度奧運哪一地方舉辦? A:北京 B:新加坡 C:倫敦 D:雪梨 請作答?",
                                       "請問 目前全球首富是誰? A:趙建銘 B:郭台銘 C:麥可喬登 D:比爾蓋茲 請作答?",
                                       "2007年度台灣之光王建明勝投數幾場 A:17 B:18 C:20 D:19 請作答?",
                                       "請問2008年度奧運是在哪裡舉辦? A:北京 B:新加坡 C:倫敦 D:雪梨 請作答?"
                                      };

            Random rndobj1 = new Random();
            int rndNum1 = rndobj1.Next();
            x1 = rndobj1.Next(1, 6);

            richTextBox3.Text += "x1 = " + x1.ToString() + "\n";

            if (x1 == 1)
            {
                s1 = a[0];
                richTextBox1.Text = s1;
            }
            else if (x1 == 2)
            {
                s1 = a[1];
                richTextBox1.Text = s1;
            }
            else if (x1 == 3)
            {
                s1 = a[2];
                richTextBox1.Text = s1;
            }
            else if (x1 == 4)
            {
                s1 = a[3];
                richTextBox1.Text = s1;
            }
            else if (x1 == 5)
            {
                s1 = a[4];
                richTextBox1.Text = s1;
            }
            else if (x1 == 6)
            {
                s1 = a[5];
                richTextBox1.Text = s1;
            }

            if (right_num == 6)
            {
                timer4.Enabled = true;
                button2.Enabled = false;
                button3.Enabled = false;
                button4.Visible = true;
                richTextBox1.ReadOnly = true;
                timer3.Enabled = true;
             
                f1.NAMESCORE = Sname + "|" + score.ToString();
            }
            timer2.Enabled = true;
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
            if (namescore != null)
            {
                name_score.Add(namescore , null);
                namescore = null;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Visible = true;
            groupBox1.Visible = true;
            groupBox2.Visible = true;
            label5.Visible = true;
            label6.Visible = true;
            label7.Visible = true;

            cnt_name = (cnt_name < 5) ? cnt_name + 1 : 1;
            right_num = 0;
            score = 0;
            richTextBox1.Text = string.Empty;

            timer1.Enabled = true;
            timer2.Enabled = false;
            timer3.Enabled = false;

            a = 10;
        }

        private void timer5_Tick(object sender, EventArgs e)
        {

        }


    }
}
