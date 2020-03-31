using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_01_Richtextbox4_TextSearch
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int start = 0;
            String pattern1 = "閭左";
            String pattern2 = "居，";
            String pattern3 = "，";
            int end1 = richTextBox1.Text.LastIndexOf(pattern1);
            int end2 = richTextBox1.Text.LastIndexOf(pattern2);
            int end3 = richTextBox1.Text.LastIndexOf(pattern3);

            richTextBox1.SelectAll();
            richTextBox1.SelectionBackColor = Color.White;

            richTextBox2.Text += "end1 = " + end1.ToString() + "\n";

            start = 0;
            while (start < end1)
            {
                richTextBox2.Text += "start = " + start.ToString() + ", len = " + richTextBox1.TextLength.ToString() + "\n";

                richTextBox1.Find(pattern1, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern1, start) + 1;
            }

            start = 0;
            while (start < end2)
            {
                richTextBox2.Text += "---start = " + start.ToString() + ", len = " + richTextBox1.TextLength.ToString() + "\n";
                richTextBox1.Find(pattern2, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern2, start) + 1;
            }


            start = 0;
            while (start < end3)
            {
                richTextBox1.Find(pattern3, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern3, start) + 1;
            }


        }
    }
}
