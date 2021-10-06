using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using   System.Runtime.InteropServices;

namespace 遠程控制計算機
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        [DllImport("Iphlpapi.dll")]
        private static extern int SendARP(Int32 dest, Int32 host, ref   Int64 mac, ref   Int32 length);
        [DllImport("Ws2_32.dll")]
        private static extern Int32 inet_addr(string ip);

        ///   <summary>   
        ///   根據ip得到網卡mac地址   
        ///   </summary>   
        ///   <param   name="ip">給出的ip地址</param>   
        ///   <returns>對應ip的網卡mac地址</returns>   
        public static Int64 GetMACByIP(string ip)
        {
            Int32 ldest = inet_addr(ip);   //目的地的ip     
            try
            {
                Int64 macinfo = new Int64();
                Int32 len = 6;
                int res = SendARP(ldest, 0, ref   macinfo, ref   len);
                return macinfo;
            }
            catch (Exception err)
            {
                return -1;

            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str = Convert.ToString(GetMACByIP(this.textBox1.Text));
            richTextBox1.Text += "取得網卡MAC位址 : " + str + "\n";
        }
    }
}

