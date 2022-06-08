using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;  //for InstalledFontCollection

namespace vcs_test_all_04_Font
{
    public partial class Form1 : Form
    {
        int WordSize;
        int SelectFont;

        string sample_string = "流水落花春去也，天上人間。ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()";

        public Form1()
        {
            InitializeComponent();
            WordSize = 15;
            SelectFont = 1;
            label1.Font = new Font("標楷體", WordSize);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SizeLabelFont(label2);
            SizeLabelFont(label3);
            SizeLabelFont(label4);
            SizeLabelFont(label5);

            // List the font families.
            InstalledFontCollection fonts = new InstalledFontCollection();
            foreach (FontFamily font_family in fonts.Families)
            {
                listBox2.Items.Add(font_family.Name);
            }

            // Select the first font.
            listBox2.SelectedIndex = 0;
        }

        // Copy this text into the Label using the biggest font that will fit.
        private void SizeLabelFont(Label lbl)
        {
            // Only bother if there's text.
            string txt = lbl.Text;
            if (txt.Length > 0)
            {
                int best_size = 100;

                // See how much room we have, allowing a bit
                // for the Label's internal margin.
                int wid = lbl.DisplayRectangle.Width - 3;
                int hgt = lbl.DisplayRectangle.Height - 3;

                // Make a Graphics object to measure the text.
                using (Graphics gr = lbl.CreateGraphics())
                {
                    for (int i = 1; i <= 100; i++)
                    {
                        using (Font test_font = new Font(lbl.Font.FontFamily, i))
                        {
                            // See how much space the text would
                            // need, specifying a maximum width.
                            SizeF text_size = gr.MeasureString(txt, test_font);
                            if ((text_size.Width > wid) || (text_size.Height > hgt))
                            {
                                best_size = i - 1;
                                break;
                            }
                        }
                    }
                }

                // Use that font size.
                lbl.Font = new Font(lbl.Font.FontFamily, best_size);
            }
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
                if (SelectFont == 1)
                    label1.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
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

            //顯示於RichTextBox裏
            richTextBox1.Text += "共有 " + FontFamily.Families.Length.ToString() + " 種字型, 如下:\n";
            for (int i = 0; i < FontFamily.Families.Length; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t" + FontFamily.Families[i].Name + "\n";
            }
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //C#專案中常常要獲取系統字型
            InstalledFontCollection fontCol = new InstalledFontCollection();
            foreach (FontFamily temp in fontCol.Families)
            {
                comboBox_font.Items.Add(temp.Name);
            }
            comboBox_font.SelectedIndex = 0;
            //在Visual Studio 2012下編譯執行後就會在comboBox中顯示目前安裝的所有字體。
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //取得計算機中已安裝的字體
            InstalledFontCollection myFonts = new InstalledFontCollection();
            foreach (FontFamily family in myFonts.Families)
            {
                richTextBox1.AppendText(family.Name + "\n");
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //指明使用特定字型檔
            //路徑             
            string path = @"../../font/金梅重黑浮體白字.ttf";
            //讀取字體文件             
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(path);
            //實例化字體             
            Font f = new Font(pfc.Families[0], 40);
            //設置字體            
            richTextBox2.Font = f;
        }

        private void DisPlaySelectedFont(object sender, EventArgs e)
        {
            // Compose the font style.
            FontStyle font_style = FontStyle.Regular;
            if (chkBold.Checked) font_style |= FontStyle.Bold;
            if (chkItalic.Checked) font_style |= FontStyle.Italic;
            if (chkUnderline.Checked) font_style |= FontStyle.Underline;
            if (chkStrikeout.Checked) font_style |= FontStyle.Strikeout;

            // Get the font size.
            float font_size = 8;
            try
            {
                font_size = float.Parse(txtSize.Text);
            }
            catch
            {
            }

            // Get the font family name.
            string family_name = "Times New Roman";
            if (!(listBox2.SelectedItem == null))
            {
                family_name = listBox2.SelectedItem.ToString();
            }

            // Set the sample's font.
            richTextBox2.Font = new Font(family_name, font_size, font_style);
            richTextBox2.Text = "字型: " + family_name + Environment.NewLine + sample_string;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //獲取系統字體
            InstalledFontCollection fc = new InstalledFontCollection();
            foreach (FontFamily font in fc.Families)
            {
                richTextBox1.Text += "get font : " + font.Name + "\n";
            }

        }
    }
}
