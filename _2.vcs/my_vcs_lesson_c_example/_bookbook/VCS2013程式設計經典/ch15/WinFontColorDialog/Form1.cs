using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFontColorDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // ===  表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "記事本 2.0版";
            // 使richTextBox1填滿整個表單
            richTextBox1.Dock = DockStyle.Fill;
            // 使fontDialog1預設出現色彩下拉式清單
            fontDialog1.ShowColor = true;
            // 使colorDialog1預設出現自訂色彩區段
            colorDialog1.FullOpen = true;
        }

        // ===  判斷開啟字型對話方塊時是否按下 [確定] 鈕
        private void 字型ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟字型對話方塊時是否按下 [確定] 鈕
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                // 將字型對話方塊選取的字型樣式指定給richTextBox1中選取文字
                richTextBox1.SelectionFont = fontDialog1.Font;
                // ===  將字型對話方塊選取的色彩指定給richTextBox1中選取的文字色彩(即前景色)
                richTextBox1.SelectionColor = fontDialog1.Color;
            }
        }

        // ===  執行功能表的 [色彩/前景色] 指令時執行此事件處理函式
        private void 前景色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟色彩對話方塊時是否按下 [確定] 鈕
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                // 將色彩對話方塊選取的色彩指定給richTextBox1中選取文字的前景色
                richTextBox1.SelectionColor = colorDialog1.Color;
            }
        }

        // ===  執行功能表的 [色彩/背景色] 指令時執行此事件處理函式
        private void 背景色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟色彩對話方塊時是否沒有按下 [消取] 鈕
            if (colorDialog1.ShowDialog() != DialogResult.Cancel)
            {
                // 將色彩對話方塊選取的色彩指定給richTextBox1中選取文字的背景色
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }
    }
}

