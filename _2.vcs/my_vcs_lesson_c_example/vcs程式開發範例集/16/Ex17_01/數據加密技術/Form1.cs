using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Security.Cryptography;
namespace 數據加密技術
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
            if (textBox1.Text == "")
            { MessageBox.Show("請輸入加密數據"); return; }
            MD5CryptoServiceProvider M5 = new MD5CryptoServiceProvider();
            textBox2.Text = ASCIIEncoding.ASCII.GetString(M5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(textBox1.Text)));
        }
    }
}