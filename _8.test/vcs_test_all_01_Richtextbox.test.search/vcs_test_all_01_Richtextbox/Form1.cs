using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_01_Richtextbox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.Pink;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.FromName("Control");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
                //richTextBox1.SelectionBackColor
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int start = 0;
            String pattern1 = "方式";
            String pattern2 = "字";
            String pattern3 = "的";
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
