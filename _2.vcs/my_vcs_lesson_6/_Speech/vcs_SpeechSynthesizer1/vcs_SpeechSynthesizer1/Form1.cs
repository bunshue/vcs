using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//實現語音朗讀功能
//參考/加入參考/.NET/System.Speech
using System.Speech.Synthesis;

namespace vcs_SpeechSynthesizer1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(richTextBox1.Text))
            {
                return;
            }
            // 一new一speech就搞定  
            SpeechSynthesizer sp = new SpeechSynthesizer();
            sp.SpeakCompleted += (s, arg) => button1.Enabled = true;

            // 開始讀啦  
            button1.Enabled = false;
            sp.SpeakAsync(richTextBox1.Text);

            /*            
            調用Speak方法就可以開始聆聽MM講話了，我這裡調用的是異步版本。

            運行一下，輸 入一些文本，開始閱讀，你會聽到一位MM的天籁之音的。
            */

        }

    }
}
