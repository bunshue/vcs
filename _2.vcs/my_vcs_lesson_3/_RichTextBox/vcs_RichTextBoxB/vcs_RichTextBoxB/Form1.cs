using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_RichTextBoxB
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

        private void richTextBox1_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟RTF檔案
            string filename = @"C:\_git\vcs\_2.vcs\______test_files\__RW\_rtf\text.rtf";

            try
            {
                richTextBox1.LoadFile(filename);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("沒找到相關文件");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //另存RTF檔案
            try
            {
                richTextBox1.SaveFile("aaaa.rtf");
            }
            catch (Exception err)
            {

                MessageBox.Show(err.Message);
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            //粗體
            try
            {
                Font oldFont;
                Font newFont;
                oldFont = richTextBox1.SelectionFont;
                if (oldFont.Bold == true)
                {
                    newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Bold);
                }
                else
                {
                    newFont = new Font(oldFont, oldFont.Style | FontStyle.Bold);
                }
                richTextBox1.SelectionFont = newFont;
                this.richTextBox1.Focus();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //斜體
            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;

            if (richTextBox1.SelectionFont.Italic == true)
            {
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Italic);
            }
            else
            {
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Italic);
            }
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //居中
            if (this.richTextBox1.SelectionAlignment == HorizontalAlignment.Center)
            {
                richTextBox1.SelectionAlignment = HorizontalAlignment.Left;
            }
            else
            {
                richTextBox1.SelectionAlignment = HorizontalAlignment.Center;
            }
            richTextBox1.Focus();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //下劃線
            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;
            if (oldFont.Underline == true)
            {
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Underline);
            }
            else
            {
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Underline);
            }
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength <= 0)
            {
                return;
            }

            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;

            float font_size = richTextBox1.SelectionFont.Size;
            font_size++;
            newFont = new Font(oldFont.Name, font_size);
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
            
            /*
            FontFamily currentFontFamily = richTextBox1.SelectionFont.FontFamily;
            Font newFont = new Font(currentFontFamily, font_size);
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
            */
        }

    }
}

