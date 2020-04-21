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
            //string unicodeString = "unicode Pi (\u03a0) pi (\u03c0)";
            string unicodeString = "16 ????三度笠(1969.04.01-春美?";

            // Create two different encodings.
            Encoding ascii = Encoding.ASCII;
            Encoding unicode = Encoding.Unicode;

            // Convert the string into a byte array.
            byte[] unicodeBytes = unicode.GetBytes(unicodeString);

            // Perform the conversion from one encoding to the other.
            byte[] asciiBytes = Encoding.Convert(unicode, ascii, unicodeBytes); //將unicode轉成ascii

            // Convert the new byte[] into a char[] and then into a string.
            char[] asciiChars = new char[ascii.GetCharCount(asciiBytes, 0, asciiBytes.Length)];
            ascii.GetChars(asciiBytes, 0, asciiBytes.Length, asciiChars, 0);
            string asciiString = new string(asciiChars);

            // Display the strings created before and after the conversion.
            richTextBox1.Text += "Original string: " + unicodeString + "\n";
            richTextBox1.Text += "Ascii converted string: " + asciiString + "\n";
        }
    }
}
