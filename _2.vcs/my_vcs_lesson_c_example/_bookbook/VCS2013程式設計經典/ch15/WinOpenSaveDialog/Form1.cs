using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinOPenSaveDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // ==== 表單載入時執行
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
        // 執行功能表的 [字型] 指令時執行此事件處理函式
        private void 字型ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟字型對話方塊時是否按下 [確定] 鈕
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                // 將字型對話方塊選取的字型樣式指定給richTextBox1中選取文字
                richTextBox1.SelectionFont = fontDialog1.Font;
                // 將字型對話方塊選取的色彩指定給richTextBox1中選取的文字色彩(即前景色)
                richTextBox1.SelectionColor = fontDialog1.Color;
            }
        }
        // 執行功能表的 [色彩/前景色] 指令時執行此事件處理函式
        private void 前景色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟色彩對話方塊時是否按下 [確定] 鈕
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                // 將色彩對話方塊選取的色彩指定給richTextBox1中選取文字的前景色
                richTextBox1.SelectionColor = colorDialog1.Color;
            }
        }
        // 執行功能表的 [色彩/背景色] 指令時執行此事件處理函式
        private void 背景色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 判斷開啟色彩對話方塊時是否沒有按下 [消取] 鈕
            if (colorDialog1.ShowDialog() != DialogResult.Cancel)
            {
                // 將色彩對話方塊選取的色彩指定給richTextBox1中選取文字的背景色
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }
        // 執行功能表的 [檔案/開啟舊檔] 指令時執行此事件處理函式
        private void 開啟舊檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 打開開啟舊檔對話方塊並判斷是否按下 [確定] 鈕 
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 使用richTextBox1的LoadFile方法載入開啟舊檔對話方塊指定的檔案
                richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.RichText);
            }
        }
         // 執行功能表的 [檔案/儲存檔案] 指令時執行此事件處理函式
        private void 儲存檔案ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 打開另存新增對話方塊並判斷是否按下 [確定] 鈕 
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 使用richTextBox1的SaveFile方法將richTextBox1內的資料
                // 存入另存新檔對話方塊指定的檔案內
                richTextBox1.SaveFile(saveFileDialog1.FileName, RichTextBoxStreamType.RichText);
            }
        }
        // 執行功能表的 [檔案/清除] 指令時執行此事件處理函式
        private void 清除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }
        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)        
        {
            Application.Exit();
        }
    }
}
