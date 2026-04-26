using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 切換輸入法
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //取得系統中已經安裝的文字輸入法
            richTextBox1.Text += "取得系統中已經安裝的文字輸入法\n";

            InputLanguageCollection mInputs = InputLanguage.InstalledInputLanguages;
            foreach (InputLanguage mInput in mInputs)
            {
                this.comboBox1.Items.Add(mInput.LayoutName);
                richTextBox1.Text += mInput.LayoutName + "\n";
            }

            //取得目前輸入法訊息
            InputLanguage CurrentInput = InputLanguage.CurrentInputLanguage;
            this.textBox1.Text = CurrentInput.LayoutName;
            richTextBox1.Text += "aaa" + CurrentInput.LayoutName + "\n";

            //取得輸入法的語言區域
            this.textBox3.Text = CurrentInput.Culture.DisplayName;
            richTextBox1.Text += "bbb" + CurrentInput.Culture.DisplayName + "\n";

            //取得預設的輸入法訊息
            InputLanguage dInput = InputLanguage.DefaultInputLanguage;
            this.textBox2.Text = dInput.LayoutName;
            richTextBox1.Text += "ccc" + dInput.LayoutName + "\n";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //取得選擇的輸入法
            InputLanguage mInput = InputLanguage.InstalledInputLanguages[comboBox1.SelectedIndex];

            //設定目前輸入法
            InputLanguage.CurrentInputLanguage = mInput;

            //取得目前輸入法訊息
            InputLanguage CurrentInput = InputLanguage.CurrentInputLanguage;
            this.textBox1.Text = CurrentInput.LayoutName;

            //取得輸入法的語言區域
            this.textBox3.Text = CurrentInput.Culture.DisplayName;

            //取得預設的輸入法訊息
            InputLanguage dInput = InputLanguage.DefaultInputLanguage;
            this.textBox2.Text = dInput.LayoutName;
        }
    }
}
