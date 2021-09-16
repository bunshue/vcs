using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_4_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            numericUpDown1.Maximum = new System.Decimal(new int[] { 150, 0, 0, 0 });

            comboBox1.Items.AddRange(new object[] { 
                "無", 
                "國中小", 
                "高中職", 
                "大專",
                "碩士", 
                "博士" }
            );

            errorProvider1.SetIconAlignment(textBox1, ErrorIconAlignment.MiddleRight);
            errorProvider1.SetIconPadding(textBox1, 2);
            errorProvider1.BlinkRate = 1000;
            errorProvider1.BlinkStyle = ErrorBlinkStyle.AlwaysBlink;

            errorProvider2.SetIconAlignment(numericUpDown1, ErrorIconAlignment.MiddleRight);
            errorProvider2.SetIconPadding(numericUpDown1, 2);
            errorProvider2.BlinkStyle = ErrorBlinkStyle.BlinkIfDifferentError;

            errorProvider3.SetIconAlignment(comboBox1, ErrorIconAlignment.MiddleRight);
            errorProvider3.SetIconPadding(comboBox1, 2);
            errorProvider3.BlinkRate = 1000;
            errorProvider3.BlinkStyle = ErrorBlinkStyle.NeverBlink;
        }

        // 驗證資料用的公用方法
        private bool IsNameValid()
        {
            // 判斷使用者是否有輸入資料
            return (textBox1.Text.Length > 0);
        }

        private bool IsAgeTooYoung()
        {
            // 判斷年齡資料是否比3小
            return (numericUpDown1.Value < 3);
        }

        private bool IsAgeTooOld()
        {
            // 判斷年齡資料是否比100小
            return (numericUpDown1.Value > 100);
        }

        private bool IsSchoolValid()
        {
            // 判斷使用者是否已選擇學歷資料
            return ((comboBox1.SelectedItem != null) &&
                (!comboBox1.SelectedItem.ToString().Equals("無")));
        }

        private void textBox1_Validated(object sender, EventArgs e)
        {
            if (IsNameValid())
            {
                errorProvider1.SetError(textBox1, "");
            }
            else
            {
                errorProvider1.SetError(textBox1, "姓名不得為空白");
            }
        }

        private void numericUpDown1_Validated(object sender, EventArgs e)
        {
            if (IsAgeTooYoung())
            {
                errorProvider2.SetError(numericUpDown1, "年齡不夠大");
            }
            else if (IsAgeTooOld())
            {
                errorProvider2.SetError(numericUpDown1, "年齡太大");
            }
            else
            {
                errorProvider2.SetError(numericUpDown1, "");
            }
        }

        private void comboBox1_Validated(object sender, EventArgs e)
        {
            if (!IsSchoolValid())
            {
                errorProvider3.SetError(comboBox1, "請選擇學歷");
            }
            else
            {
                errorProvider3.SetError(comboBox1, "");
            }
        }
    }
}
