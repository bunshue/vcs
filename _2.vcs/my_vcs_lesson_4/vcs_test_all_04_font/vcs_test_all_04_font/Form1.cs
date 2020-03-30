using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_04_Font
{
    public partial class Form1 : Form
    {
        int WordSize;
        int SelectFont;
        public Form1()
        {
            InitializeComponent();
            WordSize = 15;
            SelectFont = 1;
            label1.Font = new Font("標楷體", WordSize);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            WordSize = 10;
            label1.Font = new Font("標楷體", WordSize);
            //label1.Font.Size = 10F;
            //this.comboBox_drive.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));

        }

        private void button2_Click(object sender, EventArgs e)
        {
            WordSize = 20;
            label1.Font = new Font("標楷體", WordSize);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            WordSize = 30;
            label1.Font = new Font("標楷體", WordSize);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            WordSize = 40;
            label1.Font = new Font("標楷體", WordSize);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            WordSize = 50;
            label1.Font = new Font("標楷體", WordSize);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            SelectFont = 1;
            label1.Font = new Font("標楷體", WordSize);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            SelectFont = 2;
            label1.Font = new Font("新細明體", WordSize);
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if ((checkBox1.Checked == true) && (checkBox2.Checked == true) && (checkBox3.Checked == true))
            {
                if(SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Bold|FontStyle.Italic|FontStyle.Underline);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
            }
            else if ((checkBox1.Checked == true) && (checkBox2.Checked == true) && (checkBox3.Checked == false))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Italic);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Italic);
            }
            else if ((checkBox1.Checked == true) && (checkBox2.Checked == false) && (checkBox3.Checked == true))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Underline);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Underline);
            }
            else if ((checkBox1.Checked == false) && (checkBox2.Checked == true) && (checkBox3.Checked == true))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Italic | FontStyle.Underline);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Italic | FontStyle.Underline);
            }
            else if ((checkBox1.Checked == true) && (checkBox2.Checked == false) && (checkBox3.Checked == false))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Bold);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Bold);
            }
            else if ((checkBox1.Checked == false) && (checkBox2.Checked == false) && (checkBox3.Checked == true))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Underline);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Underline);
            }
            else if ((checkBox1.Checked == false) && (checkBox2.Checked == true) && (checkBox3.Checked == false))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Italic);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Italic);
            }
            else if ((checkBox1.Checked == false) && (checkBox2.Checked == false) && (checkBox3.Checked == false))
            {
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Regular);
                else if (SelectFont == 2)
                    label1.Font = new Font("新細明體", WordSize, FontStyle.Regular);
            }

        
        }

        private void button8_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = label1.Font;
            fontDialog1.Color = label1.ForeColor;

            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                label1.Font = fontDialog1.Font;
                label1.ForeColor = fontDialog1.Color;
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
            float font_size = label1.Font.Size;
            if (font_size > 5)
            {
                font_size--;
                //字體變小
                label1.Font = new Font("新細明體", font_size);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            float font_size = label1.Font.Size;
            if (font_size < 100)
            {
                font_size++;
                //字體變大
                label1.Font = new Font("新細明體", font_size);
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //列出所有已安裝字型

            //一樣
            //this.listBox1.Items.AddRange(FontFamily.Families);

            //一樣
            foreach (FontFamily oneFontFamily in FontFamily.Families)
            {
                listBox1.Items.Add(oneFontFamily.Name);
            }
        }
    }
}
