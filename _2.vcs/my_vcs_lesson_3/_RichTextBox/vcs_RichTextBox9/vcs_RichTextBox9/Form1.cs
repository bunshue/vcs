using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//引用與輸入輸出流有關的命名空間

namespace vcs_RichTextBox9
{
    public partial class Form1 : Form
    {
        private RichTextBoxEx richTextBox1 = new RichTextBoxEx();//聲明一個自定義類的實例

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.richTextBox1.Parent = this.groupBox1;//設置自定義類的父容器
            this.groupBox1.Controls.Add(this.richTextBox1);//向指定的父容器中添加控件
            richTextBox1.SelectionBullet = true;//設置RichTextBox控件標識項目符號的值為true
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();//聲明一個打開文件對話框的對象
            openFileDialog1.InitialDirectory = @"C:\______test_files1\__RW\_rtf";  //對話方塊的初始目錄
            openFileDialog1.Filter = "RTF文件(*.RTF)|*.RTF";//設置打開文件的格式
            if (openFileDialog1.ShowDialog() == DialogResult.OK)//當單擊「打開」按鈕時
            {
                this.richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.RichText);//在RichTextBox控件中打開文件
                MessageBox.Show("讀取成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出讀取成功的信息提示
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";

            this.richTextBox1.SaveFile(filename, RichTextBoxStreamType.RichText);//以指定的格式保存該文件

            MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的信息提示

            //richTextBox1.Text += "已存檔 : " + filename + "\n";

            this.richTextBox1.Clear();//清空RichTextBox控件中的原有內容
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionBullet)//當RichTextBox控件標識項目符號的值為true時
            {
                richTextBox1.SelectionBullet = false;//設置RichTextBox控件標識項目符號的值為false
            }
            else //當RichTextBox控件標識項目符號的值為false時
            {
                richTextBox1.SelectionBullet = true;//設置RichTextBox控件標識項目符號的值為true
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.BulletType = RichTextBoxEx.AdvRichTextBulletType.Number;//設置文件的項目編號屬性
        }
    }
}

