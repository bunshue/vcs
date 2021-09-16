using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinToolStripContainer
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
            // 豐富文字方塊填滿整個表單
            richTextBox1.Dock = DockStyle.Fill;
        }
        // ===  按工具列的開檔鈕時執行
        private void tsbOpen_Click(object sender, EventArgs e)
        {
            // 使用try{...}catch{...}來補捉沒有檔案可能發生的例外
            try
            {
                // 將test.rtf檔的內容載入到richTextBox1豐富文字方塊內
                richTextBox1.LoadFile("Gotop.rtf", RichTextBoxStreamType.RichText);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        // ===  按工具列的存檔鈕時執行
        private void tsbSave_Click(object sender, EventArgs e)
        {
            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            richTextBox1.SaveFile("Gotop.rtf", RichTextBoxStreamType.RichText);
        }
        // ===  按工具列的清除鈕時執行
        private void tsbCls_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }
        // ===  按下工具列的項目符號鈕時執行
        private void tsbBullet_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectionBullet = !richTextBox1.SelectionBullet;
        }
        // ===  字型下拉式清單SelectedIndex屬性改變時執行即選取清單時執行
        private void cboSize_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 設定選取字型的樣式
            richTextBox1.SelectionFont = new Font(richTextBox1.Font.FontFamily.ToString(), float.Parse(cboSize.Text), richTextBox1.Font.Style);           
        }
        // ===  按 黑 項目時執行
        private void 黑ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為黑色
            richTextBox1.SelectionColor = Color.Black;  
        }
        // ===  按 紅 項目時執行
        private void 紅ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為紅色
            richTextBox1.SelectionColor = Color.Red;
        }
        // ===  按 綠 項目時執行
        private void 綠ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為綠色
            richTextBox1.SelectionColor = Color.Green;
        }
        // ===  按 藍 項目時執行
        private void 藍ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為藍色
            richTextBox1.SelectionColor = Color.Blue;
        }
    }
}
