using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//加入 / 類別 / AquaButton.cs

/*
自定義Button
重繪按鍵
定義 AquaButton 類別 繼承 Button 進行重繪
重編後, 工具箱出現 AquaButton 控件
*/

namespace vcs_MyButton
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.aquaButton1.Focus();

            this.AcceptButton = this.aquaButton2;
            this.AutoScaleBaseSize = new System.Drawing.Size(6, 18);
            this.BackColor = System.Drawing.Color.White;
        }

        private void aquaButton_Click(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            richTextBox1.Text += "你按了 : " + btn.Name + "\n";
        }
    }
}
