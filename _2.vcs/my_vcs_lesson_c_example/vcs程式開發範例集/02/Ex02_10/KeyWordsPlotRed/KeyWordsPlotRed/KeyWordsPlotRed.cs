using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;//需引用命名空間Using System.IO

namespace KeyWordsPlotRed
{
    public partial class KeyWordsPlotRed : Form
    {
        public KeyWordsPlotRed()
        {
            InitializeComponent();
        }

        private void KeyWordsPlotRed_Load(object sender, EventArgs e)
        {
            richTextBox1.ReadOnly = true;//設置文本為只讀格式
            string filePath = "tomorrow.TXT";//設置打開文件的路徑
            if (File.Exists(filePath)) //當存在該文件時
            {
                FetchFile(filePath);//在RichTextBox控件中顯示指定路徑下的文件
                unfold.Enabled = false;//設置「打開」按鈕為不可用狀態
            }
            plotRed.Enabled = false;//設置「描紅」按鈕為不可用狀態
            keyWord.Focus();//使焦點位於文本框中
        }
        private void FetchFile(string path)
        {
            StreamReader UTF_8Reader = new StreamReader(path, Encoding.Default);//實現一個 TextReader，使其以一種特定的編碼從字節流中讀取字符。
            richTextBox1.Text = UTF_8Reader.ReadToEnd();//在RichTextBox控件中顯示從字節流中讀取的字符
        }

        private void unfold_Click(object sender, EventArgs e)
        {
            OpenFileDialog UTF_8File = new OpenFileDialog();//表示一個通用對話框，用戶可以使用此對話框來指定一個或多個要打開的文件的文件名。
            UTF_8File.Filter = "TXT文件（*.TXT）|*.TXT";//設置打開對話框的打開過濾參數
            if (UTF_8File.ShowDialog() == DialogResult.OK)//當在打開對話框中點擊「打開」按鈕時
            {
                richTextBox1.LoadFile(UTF_8File.FileName, RichTextBoxStreamType.PlainText);//從指定的位置加載TxT文件
                MessageBox.Show("讀取成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出讀取成共的信息提示
                unfold.Enabled = false;//設置「打開」按鈕為不可用狀態
            }
        }

        private int flag = 0;//定義一個int型的標識符
        private void plotRed_Click(object sender, EventArgs e)
        {
            if ((flag = richTextBox1.Text.IndexOf(keyWord.Text, flag)) == -1)//當文件中不存在要搜索的關鍵字時
            {
                MessageBox.Show("沒有要查找的結果", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出對應的信息提示
                keyWord.Clear();//清空文本框中的內容
                flag = 0;//重新為flag賦值
            }
            else//當在文件中存在對應的關鍵字時
            {
                richTextBox1.Select(flag, keyWord.Text.Length);//在RichTextBox控件中搜索關鍵字
                flag = flag + keyWord.Text.Length;//遞增標識查詢關鍵字的初始長度
                richTextBox1.SelectionColor = Color.Red;//設定關鍵字為紅色
            }
        }

        private void keyWord_TextChanged(object sender, EventArgs e)
        {
            if (keyWord.Text == "" || keyWord.Text == null)//當文本框中不存在內容或者內容為空時
            {
                plotRed.Enabled = false;//設定「描紅」按鈕為不可用狀態
            }
            else//當文本框中存在內容時
            {
                plotRed.Enabled = true;//設定「描紅」按鈕為可用狀態
            }
        }
    }
}
