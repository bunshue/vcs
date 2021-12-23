using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FontDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            fontDialog1.AllowVerticalFonts = true;//指示對話框既顯示垂直字體又顯示水平字體
            fontDialog1.FixedPitchOnly = true; 			//只允許選擇固定間距字體
            fontDialog1.ShowApply = true;      		//包含應用按鈕
            fontDialog1.ShowEffects = true;    //允許指定刪除線、下畫線和文本顏色選項的控件
            fontDialog1.ShowColor = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = richTextBox1.Font;           //字型對話框的預設字型
            fontDialog1.Color = richTextBox1.ForeColor;     //字型對話框的預設顏色

            if (fontDialog1.ShowDialog() == DialogResult.OK)    //開啟字型對話方塊
            {
                richTextBox1.Font = fontDialog1.Font;       //以在字型對話方塊內所指定的字型來指定給richTextBox1
                richTextBox1.ForeColor = fontDialog1.Color; //以在字型對話方塊內所指定的顏色來指定給richTextBox1
            }
        }

        private void button2_Click(object sender, EventArgs e)
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
    }
}
