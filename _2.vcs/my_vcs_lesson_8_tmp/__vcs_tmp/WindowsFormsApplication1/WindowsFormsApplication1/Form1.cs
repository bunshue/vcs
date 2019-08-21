using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
    }
}
