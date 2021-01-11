using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyDateTime
{
    public partial class Form1 : Form
    {
        //建立 HDateTime 類別
        public class HDateTime
        {
            public int year;
            public int month;
            public int day;
            //public string name;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                //get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    //name = type;
                    //Console.WriteLine("I am " + value);
                }
            }

            public HDateTime Parse(string dd)
            {
                HDateTime mdt = new HDateTime();

                int index_year;
                int index_month;
                int index_day;

                index_year = dd.IndexOf("年", 0);
                index_month = dd.IndexOf("月", index_year + 1);
                index_day = dd.IndexOf("日", index_month + 1);

                int year = 0;
                int month = 0;
                int day = 0;

                if ((index_year == -1) || (index_month == -1) || (index_day == -1))
                {
                    //return new HDateTime(0, 0, 0);
                }
                else
                {
                    year = int.Parse(dd.Substring(0, index_year - 0));
                    month = int.Parse(dd.Substring(index_year + 1, index_month - index_year - 1));
                    day = int.Parse(dd.Substring(index_month + 1, index_day - index_month - 1));
                    //return new DateTime(year, month, day);
                }

                mdt.year = year;
                mdt.month = month;
                mdt.day = day;
                return mdt;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string dd1 = "541年7月21日";
            string dd2 = "-541年7月21日";
            DateTime dt;

            dt = ParseDate(dd1);
            richTextBox1.Text += "result year = " + dt.Year.ToString() + ", month = " + dt.Month.ToString() + ", day = " + dt.Day.ToString() + "\n";


            dt = ParseDate(dd2);
            richTextBox1.Text += "result year = " + dt.Year.ToString() + ", month = " + dt.Month.ToString() + ", day = " + dt.Day.ToString() + "\n";
        
        }

        private DateTime ParseDate(string date_text)
        {
            int index_year;
            int index_month;
            int index_day;

            richTextBox1.Text += "\n原字串:\t" + date_text + "\n";
            index_year = date_text.IndexOf("年", 0);
            richTextBox1.Text += "找到年在 " + index_year.ToString() + "\n";

            index_month = date_text.IndexOf("月", index_year + 1);
            richTextBox1.Text += "找到月在 " + index_month.ToString() + "\n";

            index_day = date_text.IndexOf("日", index_month + 1);
            richTextBox1.Text += "找到日在 " + index_day.ToString() + "\n";


            if ((index_year == -1) || (index_month == -1) || (index_day == -1))
            {
                richTextBox1.Text += "格式錯誤\n";
                return new DateTime(0, 0, 0);
            }
            else
            {
                int year = int.Parse(date_text.Substring(0, index_year - 0));
                int month = int.Parse(date_text.Substring(index_year + 1, index_month - index_year - 1));
                int day = int.Parse(date_text.Substring(index_month + 1, index_day - index_month - 1));
                //return new DateTime(year, month, day);
            }

            /*
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            */
            return new DateTime(2006, 3, 11);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string dd1 = "541年7月21日";
            string dd2 = "-541年17月21日";
            string dd3 = "41年7月-20日";

            HDateTime hdt = new HDateTime();

            richTextBox1.Text += "原字串\t" + dd1 + "\n";
            hdt = hdt.Parse(dd1);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

            richTextBox1.Text += "原字串\t" + dd2 + "\n";
            hdt = hdt.Parse(dd2);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

            richTextBox1.Text += "原字串\t" + dd3 + "\n";
            hdt = hdt.Parse(dd3);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

        }
    }
}
