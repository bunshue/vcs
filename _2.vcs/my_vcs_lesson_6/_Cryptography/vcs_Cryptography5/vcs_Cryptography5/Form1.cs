using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;

namespace vcs_Cryptography5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MD5 md5 = MD5.Create();
            byte[] input = Encoding.Default.GetBytes(textBox1.Text);
            byte[] output = md5.ComputeHash(input);
            string result = Convert.ToBase64String(output);
            textBox2.Text = result;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(textBox1.Text);
            byte[] output = sha1.ComputeHash(input);
            string result = Convert.ToBase64String(output);
            textBox2.Text = result;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SHA256 sha256 = new SHA256CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(textBox1.Text);
            byte[] output = sha256.ComputeHash(input);
            string result = Convert.ToBase64String(output);
            textBox2.Text = result;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            SHA384 sha384 = new SHA384CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(textBox1.Text);
            byte[] output = sha384.ComputeHash(input);
            string result = Convert.ToBase64String(output);
            textBox2.Text = result;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            SHA512 sha512 = new SHA512CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(textBox1.Text);
            byte[] output = sha512.ComputeHash(input);
            string result = Convert.ToBase64String(output);
            textBox2.Text = result;
        }
    }
}
