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
        //建立 MyDateTime 類別
        public class MyDateTime
        {
            public int year;
            public int month;
            public int day;
            public int number;
            public string name;
            public string type;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    name = type;
                    //Console.WriteLine("I am " + value);
                }
            }

            public MyDateTime Parse(string dd)
            {
                MyDateTime mdt = new MyDateTime();
                mdt.year = 2000;
                mdt.month = 1;
                mdt.day = 23;
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
            string dd2 = "20060311";
            DateTime dt;

            dt = ParseDate(dd2);

            richTextBox1.Text += "result year = " + dt.Year.ToString() + ", month = " + dt.Month.ToString() + ", day = " + dt.Day.ToString() + "\n";

        }

        private DateTime ParseDate(string date_text)
        {
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            return new DateTime(year, month, day);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MyDateTime mdt = new MyDateTime();
            mdt.year = 2006;
            mdt.month = 3;
            mdt.day = 11;
            //mdt.Show();

            string dd1 = "541年7月21日";
            //MyDateTime mdt2 = MyDateTime.Parse(dd1);

            MyDateTime mdt2 = new MyDateTime();
            mdt2 = mdt2.Parse(dd1);

            richTextBox1.Text += "after parse, yy = " + mdt2.year.ToString() + ", mm = " + mdt2.month.ToString() + ", dd = " + mdt2.day.ToString() + "\n";
        }
    }
}
