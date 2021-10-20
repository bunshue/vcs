using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

namespace network_test2_http
{
    public partial class Form1 : Form
    {

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
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //c# 下載網頁源碼 獲取http狀態碼
            //c# 下載網頁源碼 獲取http狀態碼
            HttpWebRequest hwr = (HttpWebRequest)WebRequest.Create("http://www.baidu.com");
            hwr.AllowAutoRedirect = false; //不允許重定向
            hwr.Timeout = 10000; //連接超時時間設置
            hwr.Method = "GET"; //協議：GET、HEAD、POST、PUT、DELETE、TRACE 或OPTIONS。

            try
            {
                HttpWebResponse hwrs = (HttpWebResponse)hwr.GetResponse();
                MessageBox.Show(((int)hwrs.StatusCode).ToString()); //獲得http狀態碼 如:200但是404卻捕捉不到
                Stream stream = hwrs.GetResponseStream();
                MessageBox.Show(hwrs.CharacterSet); //獲取返回結果的字符編碼
                StreamReader sr = new StreamReader(stream, Encoding.GetEncoding(hwrs.CharacterSet)); //注意讀取的文字編碼格式要和寫入文件的文字編碼格式相同
                StreamWriter sw = new StreamWriter("c:\\b.html", false, Encoding.GetEncoding(hwrs.CharacterSet)); //寫入文字的編碼格式和讀取時候的編碼格式一樣
                sw.Write(sr.ReadToEnd());
                sw.Flush();
                sw.Close();
                sr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼
            FailCount = 0;
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188493.html";
            string result = GetHtml(url);
            richTextBox1.Text += result + "\n";
        }

        //C#下載網頁HTML源碼，
        private static int FailCount = 0; //記錄下載失敗的次數

        public static string GetHtml(string url) //傳入要下載的網址
        {
            string str = string.Empty;
            try
            {
                System.Net.WebRequest request = System.Net.WebRequest.Create(url);
                request.Timeout = 10000; //下載超時時間
                request.Headers.Set("Pragma", "no-cache");
                System.Net.WebResponse response = request.GetResponse();
                System.IO.Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("gb2312");//utf-8 網頁文字編碼
                System.IO.StreamReader streamReader = new System.IO.StreamReader(streamReceive, encoding);
                str = streamReader.ReadToEnd();
                streamReader.Close();
            }
            catch (Exception ex)
            {
                FailCount++;

                if (FailCount > 5)
                {
                    var result = System.Windows.Forms.MessageBox.Show("已下載失敗" + FailCount + "次，是否要繼續嘗試？" + Environment.NewLine + ex.ToString(), "數據下載異常", System.Windows.Forms.MessageBoxButtons.YesNo, System.Windows.Forms.MessageBoxIcon.Error);
                    if (result == System.Windows.Forms.DialogResult.Yes)
                    {
                        str = GetHtml(url);
                    }
                    else
                    {
                        System.Windows.Forms.MessageBox.Show("下載HTML失敗" + Environment.NewLine + ex.ToString(), "下載HTML失敗", System.Windows.Forms.MessageBoxButtons.OK, System.Windows.Forms.MessageBoxIcon.Error);
                        throw ex;
                    }
                }
                else
                {
                    str = GetHtml(url);
                }
            }

            FailCount = 0; //如果能執行到這一步就表示下載終於成功了
            return str;
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

    }
}

