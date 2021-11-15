using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RichTextBox5_Conversion
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Convert the string into an array of bytes and display it.
        private void button1_Click(object sender, EventArgs e)
        {
            // Convert the string into bytes.
            UnicodeEncoding ascii_encoder = new UnicodeEncoding();
            byte[] bytes = ascii_encoder.GetBytes(richTextBox1.Text);

            // Display the result as a string of hexadecimal values.
            richTextBox2.Text = bytes.ToHex(' ');
        }

        // Converrt the string of hexadecimal values back into a string.
        private void button2_Click(object sender, EventArgs e)
        {
            // Convert the string of hexadecimal values into an array of bytes.
            byte[] bytes = richTextBox2.Text.ToBytes();

            // Convert the bytes into a string and display the result.
            UnicodeEncoding ascii_encoder = new UnicodeEncoding();
            richTextBox3.Text = ascii_encoder.GetString(bytes);
        }
    }
}
