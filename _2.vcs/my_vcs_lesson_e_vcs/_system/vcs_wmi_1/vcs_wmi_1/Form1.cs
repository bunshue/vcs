using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;

using System.Runtime.InteropServices;

using System.Net;
using System.IO;

namespace vcs_wmi_1
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
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
    }
}

