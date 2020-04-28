using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization;

namespace tttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int len;
            //string和byte[]的轉換

            //string類型轉成byte[]：
            string str = "琵琶行";
            string str2;
            byte[] byteArray;
            richTextBox1.Text += "len = " + str.Length.ToString() + "\n";



            richTextBox1.Text += str + "\t轉成預設編碼 : " + "\t";
            byteArray = System.Text.Encoding.Default.GetBytes(str);  //使用預設編碼, 即Big, 把字串轉成拜列
            len = byteArray.Length;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox1.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += str + "\t轉成big5編碼 : " + "\t";
            byteArray = System.Text.Encoding.GetEncoding("big5").GetBytes(str);  //指名使用big5編碼, 把字串轉成拜列
            len = byteArray.Length;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox1.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
            
            richTextBox1.Text += str + "\t轉成gb2312編碼 : " + "\t";
            byteArray = System.Text.Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用gb2312編碼, 把字串轉成拜列
            len = byteArray.Length;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox1.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            /*
            richTextBox1.Text += str + "\t轉成unicode編碼 : " + "\t";
            byteArray = System.Text.Encoding.GetEncoding("unicode").GetBytes(str);  //指名使用unicode編碼, 把字串轉成拜列
            len = byteArray.Length;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox1.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
            */


            richTextBox1.Text += "byteArray 資料\t";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox1.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            //byte[]轉成string：
            //str2 = System.Text.Encoding.Default.GetString(byteArray);
            //richTextBox1.Text += "用預設編碼轉成字串\t" + str + "\n";

            str2 = System.Text.Encoding.GetEncoding("big5").GetString(byteArray);
            richTextBox1.Text += "用預設編碼轉成字串\t" + str2 + "\n";


            str2 = System.Text.Encoding.GetEncoding("gb2312").GetString(byteArray);
            richTextBox1.Text += "用預設編碼轉成字串\t" + str2 + "\n";


            byteArray[0] = 0x9D;
            byteArray[1] = 0x32;
            str2 = System.Text.Encoding.GetEncoding("unicode").GetString(byteArray);
            richTextBox1.Text += "用預設編碼轉成字串\t" + str2 + "\n";


        }

        private void button2_Click(object sender, EventArgs e)
        {

            TaiwanLunisolarCalendar tlc = new TaiwanLunisolarCalendar();

            // 取得目前支援的農曆日曆到幾年幾月幾日( 2051-02-10 )
            tlc.MaxSupportedDateTime.ToShortDateString();

            // 取得今天的農曆年月日
            richTextBox1.Text +=
            tlc.GetYear(DateTime.Now).ToString() + "-" +
            tlc.GetMonth(DateTime.Now).ToString() + "-" +
            tlc.GetDayOfMonth(DateTime.Now).ToString() + "\n";
        }
    }
}
