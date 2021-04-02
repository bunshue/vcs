using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

namespace 透過計算機名取得IP地址
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

        private void button2_Click(object sender, EventArgs e)
        {
            IPAddress[] ip=null;
            try
            {
              ip  = Dns.GetHostAddresses(this.textBox1.Text);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                this.textBox1.Focus();
                this.textBox1.SelectAll();
                return;
            }
           this.textBox2.Text = ip[0].ToString();
        }
    }
}