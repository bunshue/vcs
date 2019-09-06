using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //C# 可以實作 ping 網路連線檢查
            //INIT PING OBJECT
            System.Net.NetworkInformation.Ping objPing = new System.Net.NetworkInformation.Ping();

            //設定測試連線及逾時時間
            System.Net.NetworkInformation.PingReply PingResult = objPing.Send("www.google.com.tw", 5000);

            //取得結果
            string pingMsg = (PingResult.Status == System.Net.NetworkInformation.IPStatus.Success) ? "連線成功" : "無法連線";

            richTextBox1.Text += pingMsg + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //比較兩個時間

            DateTime date1 = new DateTime(2016, 12, 9, 0, 0, 0);
            DateTime date2 = new DateTime(2016, 12, 9, 11, 0, 0);
            int result = DateTime.Compare(date1, date2);
            string relationship;

            if (result < 0)
                relationship = "is earlier than";
            else if (result == 0)
                relationship = "is the same time as";
            else
                relationship = "is later than";

            //Console.WriteLine("{0} {1} {2}", date1, relationship, date2);
            richTextBox1.Text += date1 + " " + relationship + " " + date2 + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //string st1 = "2010/05/30 12:13:50";
            //string st2 = "2018/09/20 14:14:30";
            string st1 = "2010/05/30";
            string st2 = "2018/09/20";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            if (DateTime.Compare(dt1, dt2) > 0)
            {
                richTextBox1.Text = st1 + " 晚於 " + st2 + "\n";
            }
            else
            {
                richTextBox1.Text = st1 + " 早於 " + st2 + "\n";
            }
        }


        private void button4_Click(object sender, EventArgs e)
        {
            //計算兩個時間差值的函數，傳回時間差的絕對值

            //韓戰	 1950年 6月25日	———————————————————1953年7月27日 簽署停戰協定	4yr
            string st1 = "1950/6/25";
            string st2 = "1953/7/27";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            string result = DateDiff(dt1, dt2);
            richTextBox1.Text += "result = " + result + "\n";

        
        }

        private string DateDiff(DateTime DateTime1, DateTime DateTime2)
        {
            string dateDiff = null;
            try
            {
                TimeSpan ts1 = new TimeSpan(DateTime1.Ticks);
                TimeSpan ts2 = new TimeSpan(DateTime2.Ticks);
                TimeSpan ts = ts1.Subtract(ts2).Duration();
                dateDiff = ts.Days.ToString() + "天"
                + ts.Hours.ToString() + "小時"
                + ts.Minutes.ToString() + "分鐘"
                + ts.Seconds.ToString() + "秒";
            }
            catch
            {

            }
            return dateDiff;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            FileStream fs = File.OpenRead(@"C:\______test_vcs\mipony.png"); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            richTextBox1.Text += "len = 0x" + filelength.ToString("X6") + " = " + filelength.ToString() + "\n";

            filelength /= 4;
            Byte[] image = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(image, 0, filelength); //按位元組流讀取
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = result;

            for (int i = 0; i < 300; i++)
            {
                richTextBox1.Text += image[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

        }
    }
}
