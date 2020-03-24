using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace richtextbox_find
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            i = richTextBox1.Find("a", i, RichTextBoxFinds.None);
            richTextBox2.Text += "Found pattern at i = " + i.ToString() + "\n";
            if (i == -1)
                richTextBox2.Text += "己至最後, 重新搜尋\n";

            i++;


        }

        private void button2_Click(object sender, EventArgs e)
        {
            int ret;
            ret = FindMyText(new char[] { 'D', 'e', 'l', 't', 'a' });
            richTextBox2.Text += "ret = " + ret.ToString() + "\n";
            
        }

        public int FindMyText(char[] text)
        {
            // Initialize the return value to false by default.     
            int returnValue = -1;
            // Ensure that a search string has been specified and a valid start point.     
            if (text.Length > 0)
            {
                // Obtain the location of the first character found in the control     
                // that matches any of the characters in the char array.     
                int indexToText = richTextBox1.Find(text);
                // Determine whether the text was found in richTextBox1.     
                if (indexToText >= 0)
                {
                    // Return the location of the character.     
                    returnValue = indexToText;
                }
            }
            return returnValue;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            try
            {
                richTextBox1.LoadFile("my_2d_array.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("File not found!");
            }  

        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                //richTextBox1.SaveFile(@"test.txt");
                richTextBox1.SaveFile(@"test.txt", RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔
            }
            catch (System.Exception err)
            {
                MessageBox.Show(err.Message);
            }  
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < 48 || e.KeyChar > 57) && e.KeyChar != 8 && e.KeyChar != 13)
            {
                e.Handled = true;
            }
            else if (e.KeyChar == 13)
            {
                TextBox txt = (TextBox)sender;
                if (txt.Text.Length > 0)
                    ApplyTextSize(txt.Text);
                e.Handled = true;
                this.richTextBox1.Focus();
            }  

        }


        //改变字体大小  
        private void ApplyTextSize(string textSize)
        {
            richTextBox2.Text += "aaaaaaaaaaaaaaa\n";
            float newSize = Convert.ToSingle(textSize);
            FontFamily currentFontFamily;
            Font newFont;
            currentFontFamily = this.richTextBox1.SelectionFont.FontFamily;
            newFont = new Font(currentFontFamily, newSize);
            this.richTextBox1.SelectionFont = newFont;
        }  


    }
}
