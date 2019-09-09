using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyUltraEdit
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
                richTextBox1.Text = System.IO.File.ReadAllText(openFileDialog1.FileName, System.Text.Encoding.Default);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (fontDialog1.ShowDialog().Equals(DialogResult.OK))
            {
                // RichTextBox.SelectionFont取得目前選擇的文字，並且將FontDialog所設定的字型結果套入 
                //richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.Font = fontDialog1.Font;
            }   

        }
    }
}
