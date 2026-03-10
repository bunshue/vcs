using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_StatusStrip5
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

        private void tsbSave_Click(object sender, EventArgs e)
        {
            // 將richTextBox1豐富文字方塊內的資料儲存到test.rtf檔
            richTextBox1.SaveFile("tmp_Gotop.rtf", RichTextBoxStreamType.RichText);
        }

        private void tsbCls_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }

        private void tsbBullet_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectionBullet = !richTextBox1.SelectionBullet;
        }

        private void cboSize_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 設定選取字型的樣式
            richTextBox1.SelectionFont = new Font(richTextBox1.Font.FontFamily.ToString(), float.Parse(cboSize.Text), richTextBox1.Font.Style);
        }

        private void 黑ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為黑色
            richTextBox1.SelectionColor = Color.Black;
        }

        private void 紅ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為紅色
            richTextBox1.SelectionColor = Color.Red;
        }

        private void 綠ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為綠色
            richTextBox1.SelectionColor = Color.Green;
        }

        private void 藍ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // richTextBox1豐富文字方塊被選取部份字型色彩設為藍色
            richTextBox1.SelectionColor = Color.Blue;
        }
    }
}
