using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1eeeeee
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Print the header.
            //richTextBox1.Text += 
            richTextBox1.Text += "Info.CodePage      ";
            richTextBox1.Text += "Info.Name                    ";
            richTextBox1.Text += "Info.DisplayName";
            richTextBox1.Text += "\n";

            // Display the EncodingInfo names for every encoding, and compare with the equivalent Encoding names.
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                Encoding enc = ei.GetEncoding();

                richTextBox1.Text += ei.CodePage;
                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += ei.Name;
                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += ei.DisplayName;
                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //string string_old = "unicode Pi (\u03a0) pi (\u03c0)";
            //string string_old = "16 ????三度笠(1969.04.01-春美?";
            string string_old = "都はるみ全曲集２ Disc 2";
            string encoding_old = "unicode";
            string encoding_new = "big5";
            string string_new = transform_encoding(string_old, encoding_old, encoding_new);
            // Display the strings created before and after the conversion.
            richTextBox1.Text += "old string: " + string_old + "\n";
            richTextBox1.Text += "new string: " + string_new + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string string_old = "都はるみ全曲集２ Disc 2";
            string encoding_old = "unicode";
            string encoding_new = "gb2312";
            string string_new = transform_encoding(string_old, encoding_old, encoding_new);
            // Display the strings created before and after the conversion.
            richTextBox1.Text += "old string: " + string_old + "\n";
            richTextBox1.Text += "new string: " + string_new + "\n";
        }

        string transform_encoding(string string_old, string enc_old, string enc_new)
        {
            int i;

            //richTextBox1.Text += "len = " + string_old.Length.ToString() + "\n";
            for (i = 0; i < string_old.Length; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + string_old[i] + "\tvalue\t" + ((int)string_old[i]).ToString("X4") + "\n";
            }
            //richTextBox1.Text += "\n文字編碼都是Unicode編碼\n";

            // Create two different encodings.
            Encoding encoding_old = Encoding.Unicode;
            //Encoding ascii = Encoding.ASCII;
            Encoding encoding_new = Encoding.GetEncoding(enc_new);

            // Convert the string into a byte array.
            byte[] bytes_old = encoding_old.GetBytes(string_old);

            // Perform the conversion from one encoding to the other.
            byte[] bytes_new = Encoding.Convert(encoding_old, encoding_new, bytes_old); //將old轉成new

            // Convert the new byte[] into a char[] and then into a string.
            char[] chars_new = new char[encoding_new.GetCharCount(bytes_new, 0, bytes_new.Length)];
            encoding_new.GetChars(bytes_new, 0, bytes_new.Length, chars_new, 0);
            string string_new = new string(chars_new);

            //richTextBox1.Text += "len = " + string_new.Length.ToString() + "\n";
            for (i = 0; i < string_new.Length; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }

            return string_new;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int i;
            string string_old = "都はるみ全曲集２";
            string string_new;
            string encoding_old = "unicode";
            string encoding_new;

            richTextBox1.Text += "\nvcs之RichTextBox只能顯示Unicode編碼, 原Unicode編碼字串:\t" + string_old + "\n";

            for (i = 0; i < string_old.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + string_old[i] + "\tvalue\t" + ((int)string_old[i]).ToString("X4") + "\n";
            }

            richTextBox1.Text += "轉成big5\n";
            encoding_new = "big5";
            string_new = transform_encoding(string_old, encoding_old, encoding_new);
            for (i = 0; i < string_new.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }

            richTextBox1.Text += "轉成gb2312\n";
            encoding_new = "gb2312";
            string_new = transform_encoding(string_old, encoding_old, encoding_new);
            for (i = 0; i < string_new.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }



        }


    }
}
