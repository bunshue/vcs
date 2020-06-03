using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1tttttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int match = 0;
            int position = 0;

            string str = textBox1.Text;

            while (true)
            {
                position = FindMyText(str, position);

                if (position == -1)
                {
                    richTextBox2.Text += "搜尋到底了, 搜尋字串\t" + str + "\t共出現 " + match.ToString() + " 次\n";
                    break;
                }
                else
                {
                    match++;
                    richTextBox2.Text += "position = " + position.ToString() + "\n";
                    position++;
                }
            }
        }

        public int FindMyText(string text, int start)
        {
            // Initialize the return value to false by default.
            int returnValue = -1;

            // Ensure that a search string and a valid starting point are specified.
            if (text.Length > 0 && start >= 0)
            {
                // Obtain the location of the search string in richTextBox1.
                int indexToText = richTextBox1.Find(text, start, RichTextBoxFinds.MatchCase);
                // Determine whether the text was found in richTextBox1.
                if (indexToText >= 0)
                {
                    // Return the index to the specified search text.
                    returnValue = indexToText;
                }
            }
            return returnValue;
        }

        public int FindMyText(string text, int start, int end)
        {
            // Initialize the return value to false by default.
            int returnValue = -1;

            // Ensure that a search string and a valid starting point are specified.
            if (text.Length > 0 && start >= 0)
            {
                // Ensure that a valid ending value is provided.
                if (end > start || end == -1)
                {
                    // Obtain the location of the search string in richTextBox1.
                    int indexToText = richTextBox1.Find(text, start, end, RichTextBoxFinds.MatchCase);
                    // Determine whether the text was found in richTextBox1.
                    if (indexToText >= 0)
                    {
                        // Return the index to the specified search text.
                        returnValue = indexToText;
                    }
                }
            }
            return returnValue;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int match = 0;
            int position = 0;

            string str = textBox1.Text;

            while (true)
            {
                position = FindMyText(str, position, richTextBox1.Text.Length / 2);

                if (position == -1)
                {
                    richTextBox2.Text += "搜尋到底了, 搜尋字串\t" + str + "\t共出現 " + match.ToString() + " 次\n";
                    break;
                }
                else
                {
                    match++;
                    richTextBox2.Text += "position = " + position.ToString() + "\n";
                    position++;
                }
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string str = textBox1.Text;

            bool flag_found = false;

            flag_found = FindMyText(str);

            if (flag_found == true)
                richTextBox2.Text += "有找到字串\t" + str + "\n";
            else
                richTextBox2.Text += "找不到字串\t" + str + "\n";


        }

        public bool FindMyText(string text)
        {
            // Initialize the return value to false by default.
            bool returnValue = false;

            // Ensure a search string has been specified.
            if (text.Length > 0)
            {
                // Obtain the location of the search string in richTextBox1.
                int indexToText = richTextBox1.Find(text);
                richTextBox2.Text += "index = " + indexToText.ToString() + "\n";
                // Determine whether the text was found in richTextBox1.
                if (indexToText >= 0)
                {
                    returnValue = true;
                }
            }

            return returnValue;
        }



    }
}
