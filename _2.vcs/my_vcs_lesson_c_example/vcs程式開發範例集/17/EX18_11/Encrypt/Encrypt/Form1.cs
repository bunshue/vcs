using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace Encrypt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text=Encrypt(textBox1.Text);
        }
        private string Encrypt(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string EncryptString;
            EncryptString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j + 5;
                b[0] = Convert.ToByte(j);
                EncryptString = EncryptString + ascii.GetString(b);
            }
            return EncryptString;
        }
        private string Decryptor(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string DecryptorString;
            DecryptorString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j - 5;
                b[0] = Convert.ToByte(j);
                DecryptorString = DecryptorString + ascii.GetString(b);
            }
            return DecryptorString;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox2.Text=Decryptor(textBox2.Text);
        }
    }
}