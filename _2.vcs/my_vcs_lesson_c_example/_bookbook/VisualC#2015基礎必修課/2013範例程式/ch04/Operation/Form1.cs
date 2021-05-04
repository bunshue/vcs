using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Operation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 按 [確定] 鈕執行
        private void btnOK_Click(object sender, EventArgs e)
        {
            int num1, num2;
            try
            {   // 將輸入的兩個資料轉成整數
                num1 = Convert.ToInt32(txtNum1.Text);
                num2 = Convert.ToInt32(txtNum2.Text);
            }
            catch
            {
                lblMsg.Text = "輸入錯誤!  請輸入數值";
                return;
            }
            switch (txtOperator.Text)
            {
                case "+":         // 判斷運算子是否為 "+" 
                    lblResult.Text = Convert.ToString(num1 + num2);
                    break;
                case "-":         // 判斷運算子是否為 "-"
                    lblResult.Text = Convert.ToString(num1 - num2);
                    break;
                case "*":        // 判斷運算子是否為 "**"
                    lblResult.Text = Convert.ToString(num1 * num2);
                    break;
                case "/":        // 判斷運算子是否為 "/"
                    if (num2 != 0)  //除數不可為0
                    {
                        lblResult.Text = Convert.ToString(num1 / num2);
                    }
                    else
                    {
                        lblMsg.Text = "除數不可為0!";
                    }
                    break;
                default:
                    lblMsg.Text = "輸入錯誤!  限 +,-, *, / 四則運算子..";
                    break;
            }
        }
    }
}
