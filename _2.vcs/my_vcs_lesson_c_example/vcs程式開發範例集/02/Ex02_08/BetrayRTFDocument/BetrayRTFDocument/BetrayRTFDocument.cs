using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;//引用命名空間Using System.IO

namespace BetrayRTFDocument
{
    public partial class BetrayRTFDocument : Form
    {
        public BetrayRTFDocument()
        {
            InitializeComponent();
        }

        private static string fileName = ""; //該變量用來保存文件的內容
        private void unwrap_Click(object sender, EventArgs e)
        {
            kept.Enabled = true;//設置「保存」按鈕為不可用狀態
            openRTFImplement.Filter = "RTF文件(*.RTF)|*.RTF";//設置打開文件的過濾參數
            if (openRTFImplement.ShowDialog() == DialogResult.OK && openRTFImplement.FileName.Length > 0)//當打開的文件內容不為空且點擊「打開」按鈕時
            {
                fileName = openRTFImplement.FileName;//保存打開文件的文件名
                this.richTextBox1.LoadFile(fileName, RichTextBoxStreamType.RichText);//從指定位置加載RTF文件
            }
        }

        private void kept_Click(object sender, EventArgs e)
        {
            if (File.Exists(fileName))//如果存在該文件
            {
                richTextBox1.SaveFile(fileName, RichTextBoxStreamType.RichNoOleObjs);//在指定路徑下保存
                MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的提示信息
                richTextBox1.Clear();//清空RichTextBox控件中的內容
            }
            else//當不存在該文件時
            {
                saveRTFImplement.Filter = "RTF文件(*.RTF)|*.RTF";//設置保存文件的保存格式
                if (saveRTFImplement.ShowDialog() == DialogResult.OK && saveRTFImplement.FileName.Length > 0)//當保存文件的文件名存在且點擊的是「保存」按鈕時
                {
                    richTextBox1.SaveFile(saveRTFImplement.FileName + ".RTF");//在指定位置下保存RTF文件
                }
            }
        }

        private void liquidate_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();//清空RichTextBox控件中的內容
            richTextBox1.Focus();//時RichTextBox控件獲得焦點
        }

        private void Exit_Click(object sender, EventArgs e)
        {
            Application.Exit();//退出應用程序
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            if (richTextBox1.Text != "")//當RichTextBox控件中存在內容時
            {
                kept.Enabled = true;//設置「保存」按鈕為可用狀態
            }
            else//當RichTextBox控件中不存在內容時
            {
                kept.Enabled = false;//設置「保存」按鈕為不可用狀態
            }
        }

        private void BetrayRTFDocument_Load(object sender, EventArgs e)
        {

        }
    }
}
