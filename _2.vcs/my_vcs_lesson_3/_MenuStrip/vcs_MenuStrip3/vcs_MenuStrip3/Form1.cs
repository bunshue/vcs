using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_MenuStrip3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 豐富文字方塊填滿整個表單
            richTextBox1.Dock = DockStyle.Fill;
        }

        private void 開檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 開檔\n";
        }

        private void 存檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 存檔\n";
        }

        private void 清除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }

        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void 項目符號ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectionBullet = !richTextBox1.SelectionBullet;
        }

        private void cboSize_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 設定選取字型的樣式
            richTextBox1.SelectionFont = new Font(richTextBox1.Font.FontFamily.ToString(), float.Parse(cboSize.Text), richTextBox1.Font.Style);
        }

        private void cboFontColor_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cboFontColor.Text == "黑")
            {
                richTextBox1.SelectionColor = Color.Black;
            }
            else if (cboFontColor.Text == "紅")
            {
                richTextBox1.SelectionColor = Color.Red;
            }
            else if (cboFontColor.Text == "綠")
            {
                richTextBox1.SelectionColor = Color.Green;
            }
            else if (cboFontColor.Text == "藍")
            {
                richTextBox1.SelectionColor = Color.Blue;
            }
        }
    }
}
