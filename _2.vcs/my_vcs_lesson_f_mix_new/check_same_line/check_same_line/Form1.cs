using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace check_same_line
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
            int i;
            int len;
            len = richTextBox1.Lines.Length;
            richTextBox2.Text += "len =  " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox2.Text += "i=" + (i + 1).ToString() + "\t" + richTextBox1.Lines[i].Length.ToString() + "\t" + richTextBox1.Lines[i] + "\n";

            }

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //檢查相同行
            int i;
            int j;
            int len = richTextBox1.Lines.Length;
            for (i = 0; i < (len-1); i++)
            {
                if (richTextBox1.Lines[i].Trim().Length == 0)
                    continue;
                for (j = (i + 1); j < len; j++)
                {
                    if (richTextBox1.Lines[j].Trim().Length == 0)
                        continue;

                    if (richTextBox1.Lines[i].Trim() == richTextBox1.Lines[j].Trim())
                    {
                        richTextBox2.Text += "第 " + i.ToString() + " 行 和 第 " + j.ToString() + " 行 相同\n";


                    }



                }
                
                //richTextBox2.Text += "i=" + (i + 1).ToString() + "\t" + richTextBox1.Lines[i].Length.ToString() + "\t" + richTextBox1.Lines[i] + "\n";

            }

            richTextBox2.Text += "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectionStart = 30;
            richTextBox1.SelectionLength = 60;
            richTextBox1.SelectionBackColor = Color.Red;




        }



    }
}
