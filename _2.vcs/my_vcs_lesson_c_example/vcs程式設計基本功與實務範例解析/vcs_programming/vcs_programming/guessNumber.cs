using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class guessNumber : Form
    {
        Random rd = new Random();
        int answer;

        public guessNumber()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnNewNumber_Click(object sender, EventArgs e)
        {
            answer = rd.Next(0, 100);
            txtAnswer.Text = "";
            txtMessage.Text = "";
        }

        private void guessNumber_Load(object sender, EventArgs e)
        {
            answer = rd.Next(0, 100);
            txtAnswer.Text = "";
            txtMessage.Text = "";
        }

        private void btnAnswer_Click(object sender, EventArgs e)
        {
            MessageBox.Show(answer.ToString(), "答案",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
            
        }

        private void btnInput_Click(object sender, EventArgs e)
        {
            if (txtAnswer.Text == "")
            {
                MessageBox.Show("沒有輸入答案", "答案",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
                return;
            }

            int input = Convert.ToInt32(txtAnswer.Text);
            string output = "";
            /*
            if (input == answer) output = "你答對了!答案是" + answer;
            if (input < answer) output = "答案比" + input + "大";
            if(input > answer) output = "答案比" + input + "小";
            */
            if (input == answer) output = "你答對了!答案是" + answer;
            else if (input < answer) output = "答案比" + input + "大";
            else output = "答案比" + input + "小";

            txtMessage.Text += output + "\r\n";

            txtMessage.SelectionStart = txtMessage.TextLength;
            txtMessage.ScrollToCaret();

            txtAnswer.Text = "";
            txtAnswer.Focus();
        }
    }
}
