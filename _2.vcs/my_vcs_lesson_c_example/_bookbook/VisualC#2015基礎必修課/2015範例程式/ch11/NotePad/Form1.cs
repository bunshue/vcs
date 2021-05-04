using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NotePad
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            rtxtNote.Dock = DockStyle.Fill;    //rtxtNote填滿整個表單
        }
        //執行功能表 [檔案/開檔] 時執行
        private void 開檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            String filename;
            openFileDialog1.Filter = "文書檔 (*.rtf)|*.rtf|所有檔案 (*.*)|*.*";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.DefaultExt = ".rtf";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                filename = openFileDialog1.FileName;
                rtxtNote.LoadFile(filename, RichTextBoxStreamType.RichText);
            }
        }
        //執行功能表 [檔案/存檔] 時執行
        private void 存檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            String filename;
            saveFileDialog1.Filter = "文書檔 (*.rtf)|*.rtf|所有檔案 (*.*)|*.*";
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.DefaultExt = ".rtf";
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                filename = saveFileDialog1.FileName;
                rtxtNote.SaveFile(filename, RichTextBoxStreamType.RichText);
            }
        }
        //執行功能表 [檔案/清除] 時執行
        private void 清除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.Clear();   //清除rtxtNote控制項的內容
        }
        //執行功能表 [檔案/結束] 時執行
        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
        //執行功能表 [編輯/複製] 時執行
        private void 複製ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.Copy();   //將選取的範圍複製到剪貼簿
        }
        //執行功能表 [編輯/貼上] 時執行
        private void 貼上ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.Paste();   //將剪貼簿的內容貼到目前的插入點
        }
        //執行功能表 [編輯/剪下] 時執行
        private void 剪下ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.Cut();   //將選取的範圍剪下到剪貼簿
        }
        // 執行功能表的 [項目符號/設定] 時執行
        private void 設定ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.SelectionBullet = true;   //選取範圍設定項目符號
        }
        //執行功能表的 [項目符號/取消項目符號] 時執行
        private void 取消ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtNote.SelectionBullet = false;  //選取範圍取消項目符號
        }
        //執行功能表的 [字型] 時執行
        private void 字型ToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                rtxtNote.SelectionFont = fontDialog1.Font;
            }
        }
        //執行功能表的 [顏色/前景色] 時執行
        private void 前背色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                rtxtNote.SelectionColor = colorDialog1.Color;
            }
        }
        // 執行功能表的 [顏色/前景色] 時執行
        private void 背景色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                rtxtNote.SelectionBackColor = colorDialog1.Color;
            }
        }
    }
}
