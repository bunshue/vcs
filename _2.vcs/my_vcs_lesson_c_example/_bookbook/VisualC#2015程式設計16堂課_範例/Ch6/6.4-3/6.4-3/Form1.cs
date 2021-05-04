using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void judgeButton_Click(object sender, EventArgs e)
        {
            resultText.Text = "判斷中...";
            int input = int.Parse(inputText.Text);

            int ceiling = input;
            for (int i=2; i<ceiling; i++) {
                if (input%i == 0) {
                    resultText.Text = "可以被" + i + "整除";
                    break;
                }
                else {
                    ceiling = input / i;
                }
            }

            if (input == 1)
                resultText.Text = "1不為質數";
            else if(resultText.Text == "判斷中...")
                resultText.Text = "本數為質數";
        }
      
    }
}
