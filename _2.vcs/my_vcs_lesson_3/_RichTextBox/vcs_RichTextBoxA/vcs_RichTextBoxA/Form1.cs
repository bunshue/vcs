using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//C# richTextBox顯示不同顏色文字

namespace vcs_RichTextBoxA
{
    public partial class Form1 : Form
    {
        public delegate void LogAppendDelegate(Color color, string text);

        /// <summary>  
        /// 追加顯示文本  
        /// </summary>  
        /// <param name="color">文本顏色</param>  
        /// <param name="text">顯示文本</param>  
        public void LogAppend(Color color, string text)
        {
            richTextBox1.AppendText(" ");
            richTextBox1.SelectionColor = color;
            richTextBox1.AppendText(text);
        }

        /// <summary>  
        /// 顯示錯誤信息
        /// </summary>  
        /// <param name="text"></param>  
        public void LogError(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Red, DateTime.Now.ToString("HH:mm:ss ") + text);
        }

        /// <summary>  
        /// 顯示警告信息  
        /// </summary>  
        /// <param name="text"></param>  
        public void LogWarning(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Violet, DateTime.Now.ToString("HH:mm:ss ") + text);
        }

        /// <summary>  
        /// 顯示一般信息  
        /// </summary>  
        /// <param name="text"></param>  
        public void LogMessage(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Black, DateTime.Now.ToString("HH:mm:ss ") + text);
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //顯示一般信息
            string message = string.Empty;
            message = "顯示一般信息\n";
            LogMessage(message);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //顯示警告信息
            string message = string.Empty;
            message = "顯示警告信息\n";
            LogWarning(message);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //顯示錯誤信息
            string message = string.Empty;
            message = "顯示錯誤信息\n";
            LogError(message);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}

