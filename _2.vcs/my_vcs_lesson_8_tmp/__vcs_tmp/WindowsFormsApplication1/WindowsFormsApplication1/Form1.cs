using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

using System.Net;   //for IPAddress
using System.Net.Sockets;   // for AddressFamily


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
            FileStream fs = File.OpenRead(@"C:\______test_vcs\ims-small-logo.png"); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            richTextBox1.Text += "len = 0x" + filelength.ToString("X6") + " = " + filelength.ToString() + "\n";

            filelength = 8;
            Byte[] w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取

            int i;

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];

            }
            richTextBox1.Text += "\n";

            filelength = 24;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

            richTextBox1.Text += "\n";

            for (i = 4; i < 8; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }
            richTextBox1.Text += "\n";

            int datasize;
            int width;
            int height;
            int bit_depth;
            int color_type;
            int compression_method;
            int filter_method;
            int interlace_method;

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }
            
            /*
            datasize = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            width = w[16] << 24 | w[17] << 16 | w[18] << 8 | w[19];
            height = w[20] << 24 | w[21] << 16 | w[22] << 8 | w[23];
            bit_depth = w[24];
            color_type = w[25];
            compression_method = w[26];
            filter_method = w[27];
            interlace_method = w[28];
            */
            datasize = w[0] << 24 | w[1] << 16 | w[2] << 8 | w[3];
            width = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            height = w[12] << 24 | w[13] << 16 | w[14] << 8 | w[15];
            bit_depth = w[16];
            color_type = w[17];
            compression_method = w[18];
            filter_method = w[19];
            interlace_method = w[20];

            richTextBox1.Text += "datasize : " + datasize.ToString() + "\n";
            richTextBox1.Text += "W : " + width.ToString() + "\n";
            richTextBox1.Text += "H : " + height.ToString() + "\n";
            richTextBox1.Text += "bit_depth : " + bit_depth.ToString() + "\n";
            richTextBox1.Text += "color_type : " + color_type.ToString() + "\n";
            richTextBox1.Text += "compression_method : " + compression_method.ToString() + "\n";
            richTextBox1.Text += "filter_method : " + filter_method.ToString() + "\n";
            richTextBox1.Text += "interlace_method : " + interlace_method.ToString() + "\n";


            //顯示圖片
            fs = File.OpenRead(@"C:\______test_vcs\ims-small-logo.png"); //OpenRead[二進位讀檔]
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = result;


            //讀前面256拜
            fs = File.OpenRead(@"C:\______test_vcs\ims-small-logo.png"); //OpenRead[二進位讀檔]

            filelength = 256;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                //richTextBox1.Text += w[i].ToString("X2");

                if (((w[i] >= '0') && (w[i] <= '9')) || ((w[i] >= 'A') && (w[i] <= 'Z')) || ((w[i] >= 'a') && (w[i] <= 'z')))
                {
                    richTextBox1.Text += (char)w[i];
                }
                else
                    richTextBox1.Text += ".";

                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

            fs.Close();
        
        
        }

        private void button6_Click(object sender, EventArgs e)
        {
            DateTime d = new DateTime(2019, 1, 1);

            richTextBox1.Text += "2019/1/1 加一段時間後 : " + d.AddDays(3125).AddSeconds(14653 * 2).ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            int yy = -280;
            int dd = -1250;
            richTextBox1.Text += "2019/1/1 減一段時間後 : " + d.AddYears(yy).AddDays(dd).AddSeconds(14653 * 2).ToString() + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            IPAddress ip = GetIP();
            if (ip != null)
            {
                richTextBox1.Text += "IP : " + ip.ToString() + "\n";
            }
        }

        IPAddress GetIP()
        {
            foreach (IPAddress ip in Dns.GetHostEntry(Dns.GetHostName()).AddressList)
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                    return ip;
            return null;
        }

    }
}
