using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using   System.Runtime.InteropServices;

namespace ���{����p���
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
        ///   �ھ�ip�o����dmac�a�}   
        ///   </summary>   
        ///   <param   name="ip">���X��ip�a�}</param>   
        ///   <returns>����ip�����dmac�a�}</returns>   
        public static Int64 GetMACByIP(string ip)
        {
            Int32 ldest = inet_addr(ip);   //�ت��a��ip     
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
            richTextBox1.Text += "���o���dMAC��} : " + str + "\n";
        }
    }
}

