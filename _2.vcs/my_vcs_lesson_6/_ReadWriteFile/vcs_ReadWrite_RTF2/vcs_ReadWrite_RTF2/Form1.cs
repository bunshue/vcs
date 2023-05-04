using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//需引用命名空間Using System.IO

namespace vcs_ReadWrite_RTF2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string temp = "tomorrow.RTF";//保存文件的路徑
        private void Form1_Load(object sender, EventArgs e)
        {
            if (File.Exists(temp))//當在指定路徑下存在該文件時
            {
                this.richTextBox1.LoadFile(temp, RichTextBoxStreamType.RichText);//從指定的位置加載RTF文件
                unfold.Enabled = false;//設定「打開」按鈕為不可用狀態
            }
            hold.Enabled = false;//設定「保存」按鈕為不可用狀態
        }

        private void unfold_Click(object sender, EventArgs e)
        {
            OpenFileDialog TxTOpenDialog = new OpenFileDialog();//聲明一個用於打開文件對話框的對象
            TxTOpenDialog.InitialDirectory = @"C:\______test_files1\__RW\_rtf";
            TxTOpenDialog.Filter = "RTF文件(*.RTF)|*.RTF";//定義打開文件對話框的過濾參數
            if (TxTOpenDialog.ShowDialog() == DialogResult.OK)//當在打開對話框中單擊「打開」按鈕時
            {
                temp = TxTOpenDialog.FileName;//保存打開文件的路徑
                this.richTextBox1.LoadFile(TxTOpenDialog.FileName, RichTextBoxStreamType.RichText);//從指定的位置加載RTF文件
                hold.Enabled = false;//設置「保存」按鈕為不可用狀態
                unfold.Enabled = false; //設置「打開」按鈕為不可用狀態
                MessageBox.Show("讀取成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出讀取成功時的提示信息
            }
        }

        private void hold_Click(object sender, EventArgs e)
        {
            ConserveMeasure(temp);//在指定路徑下保存文件
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            hold.Enabled = true;//
            if (this.richTextBox1.Text == "" || this.richTextBox1.Text == null)//
            {
                unfold.Enabled = true;//
            }
        }

        private void ConserveMeasure(string path)
        {
            SaveFileDialog TxTSaveDialog = new SaveFileDialog();//定義一個用於保存文件的保存對話框
            TxTSaveDialog.Filter = "RTF文件（*.RTF)|*.RTF";//設置保存文件的過濾參數
            if (File.Exists(path))//當在指定路徑下存在該路徑時
            {
                this.richTextBox1.SaveFile(path, RichTextBoxStreamType.RichText);//保存指定文件到指定位置
                MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的提示信息
                this.richTextBox1.Clear();//清空RichTextBox控件中的所有內容
                hold.Enabled = false;//設置「保存」按鈕為不可用狀態
            }
            else
            {
                if (TxTSaveDialog.ShowDialog() == DialogResult.OK)//當在保存對話框中單擊「保存」按鈕時
                {
                    this.richTextBox1.SaveFile(TxTSaveDialog.FileName, RichTextBoxStreamType.RichText);//保存文件到指定的位置
                    MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的提示信息
                    this.richTextBox1.Clear();//清空RichTextBox控件中的所有內容
                    hold.Enabled = false;//設定「保存」按鈕為不可用狀態
                }
            }
        }

        private void justifyCenter_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Center;//設置選定的文本為居中對齊
        }

        private void justifyLeft_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Left;//設置選定的文本為左對齊
        }

        private void justifyRight_Click(object sender, EventArgs e)
        {
            this.richTextBox1.SelectionAlignment = HorizontalAlignment.Right;//設置選定的文本為右對齊
        }
    }
}
