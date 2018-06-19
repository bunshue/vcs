using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;    //for StreamWriter
using System.Diagnostics;   //for Process
using System.Security.Cryptography; //for HashAlgorithm

namespace vcs_test_all_zz_test
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void btn_test1_Click(object sender, EventArgs e)
        {
        }


        private void btn_test2_Click(object sender, EventArgs e)
        {


        }

        public class Person
        {
            public string Name;
            public int Age;
            public DateTime birthday;
        }




        public struct Age
        {
            public int Years;
            public int Months;
            public int Days;
        }
        public static Age CalculateAge(DateTime birthDate, DateTime endDate)
        {
            if (birthDate.Date > endDate.Date)
            {
                throw new ArgumentException("birthDate cannot be higher then endDate", "birthDate");
            }

            int years = endDate.Year - birthDate.Year;
            int months = 0;
            int days = 0;

            // Check if the last year, was a full year.
            if (endDate < birthDate.AddYears(years) && years != 0)
            {
                years--;
            }

            // Calculate the number of months.
            birthDate = birthDate.AddYears(years);

            if (birthDate.Year == endDate.Year)
            {
                months = endDate.Month - birthDate.Month;
            }
            else
            {
                months = (12 - birthDate.Month) + endDate.Month;
            }

            // Check if last month was a complete month.
            if (endDate < birthDate.AddMonths(months) && months != 0)
            {
                months--;
            }

            // Calculate the number of days.
            birthDate = birthDate.AddMonths(months);

            days = (endDate - birthDate).Days;
            Age result;
            result.Years = years;
            result.Months = months;
            result.Days = days;
            return result;
        }


        private void btn_test3_Click(object sender, EventArgs e)
        {
            Person av1 = new Person();
            av1.Name = "松島かえで";
            av1.birthday = DateTime.Parse("1982年11月07日");
            av1.Age = 18;
            richTextBox1.Text += "姓名：" + av1.Name + "\n";
            //richTextBox1.Text += "年齡：" + av1.Age.ToString() + "\n";
            richTextBox1.Text += "生日：" + av1.birthday.ToShortDateString() + "\n";

            DateTime flakNow = DateTime.Now;
            Age myAge = CalculateAge(av1.birthday, flakNow);
            richTextBox1.Text += "年 : " + myAge.Years.ToString() + "\n";
            richTextBox1.Text += "月 : " + myAge.Months.ToString() + "\n";
            richTextBox1.Text += "日 : " + myAge.Days.ToString() + "\n";
            if ((myAge.Months != 0) && (myAge.Days != 0))
                av1.Age = myAge.Years + 1;
            else
                av1.Age = myAge.Years;
            richTextBox1.Text += "年齡：" + av1.Age.ToString() + "\n";
        }


        private void btn_test4_Click(object sender, EventArgs e)
        {
            StreamWriter filewriter = new StreamWriter("C:\\______test_vcs\\poem.txt");
            filewriter.WriteLine("鳳凰臺上鳳凰遊，鳳去臺空江自流");
            filewriter.WriteLine("吳宮花草埋幽徑，晉代衣冠成古邱");
            filewriter.WriteLine("三山半落青又外，二水中分白鷺洲");
            filewriter.WriteLine("總為浮雲能蔽日，長安不見使人愁");
            filewriter.Close();
        }

        private void btn_test5_Click(object sender, EventArgs e)
        {
            string pdf_path = "C:\\______test_vcs\\A New Sensorless Starting Method for Brushless DC Motors without  Reversing Rotation 2007.pdf";
            Process myProcess;
            myProcess = Process.Start(pdf_path);
            myProcess.WaitForExit();

        }

        private void btn_test6_Click(object sender, EventArgs e)
        {
            //從FTP下載檔案
            System.Net.WebClient webClient = new System.Net.WebClient();
            //下載FTP檔案到D:\sample.txt
            webClient.DownloadFile("http://ftp.tku.edu.tw/Linux/Fedora/releases/27/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-27-1.6.iso", @"C:\______test_vcs\fedora27.iso");

        }

        private void btn_test7_Click(object sender, EventArgs e)
        {
            //利用檔案的MD5碼比對兩個檔案是否相同
            //第一個檔案
            string filename1 = "C:\\______test_vcs\\compare\\aaaa.txt";
            //第二個檔案
            string filename2 = "C:\\______test_vcs\\compare\\bbbb.txt";
            //第三個檔案
            string filename3 = "C:\\______test_vcs\\compare\\ssss.txt";

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

        private void btn_test8_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

    }
}
