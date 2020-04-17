using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class ArithmeticOp : Form
    {
        public ArithmeticOp()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Close();
        }

        bool DataChecking()
        {
            int num1, num2;
            try
            {
                num1 = Convert.ToInt32(txtN1.Text);
                if (num1 < 0 || num1 > 99)
                {
                    MessageBox.Show(label1.Text + ":範圍不符");
                    return false;
                }
            }
            catch(Exception ex){
                MessageBox.Show(label1.Text + ex.Message);
                return false;
            }
            try
            {
                num2 = Convert.ToInt32(txtN2.Text);
                if (num2 < 0 || num2 > 99)
                {
                    MessageBox.Show(label2.Text + ":範圍不符");
                    return false;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(label2.Text + ex.Message);
                return false;
            }
      
            return true;
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt32(txtN1.Text);
            if (num1 < 0) {
	            //lblResult.Text = "錯誤：數字一小於Ø";
                MessageBox.Show("數字一小於Ø", // 訊息
                                "錯誤訊息",    // 標題
                                MessageBoxButtons.OK, //確定鈕
                                MessageBoxIcon.Error  // 圖示
                               );
	            return;
            }
            if (num1 > 99) {
                //lblResult.Text = "錯誤：數字一超過99";
                MessageBox.Show("數字一超過99", // 訊息
                                "錯誤訊息",     // 標題
                                MessageBoxButtons.OK, //確定鈕
                                MessageBoxIcon.Error  // 圖示
                              );
	            return;
            }

            int num2 = Convert.ToInt32(txtN2.Text);
            if (num2 < 0) {
	           //lblResult.Text = "錯誤：數字二小於Ø";
               MessageBox.Show("數字二小於Ø", // 訊息
                               "錯誤訊息",    // 標題
                               MessageBoxButtons.OK, //確定鈕
                               MessageBoxIcon.Error  // 圖示
                              );
	           return;
            }
            if (num2 > 99) {
                //lblResult.Text = "錯誤：數字二超過99";
                MessageBox.Show("數字二超過99", // 訊息
                                "錯誤訊息",    // 標題
                                MessageBoxButtons.OK, //確定鈕
                                MessageBoxIcon.Error  // 圖示
                              );
	            return;
            }

            int res = num1 + num2;
            string output = "";

            output = output + num1 + " + " + num2 + " = " + res;
            lblResult.Text = output;
        }

        private void btnSub_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt32(txtN1.Text);

            if (num1 < 0 || num1 > 99) {
                lblResult.Text = "數字一範圍不符，必須0到99";
                return; 
            }

            int num2 = Convert.ToInt32(txtN2.Text);

            if (num2 < 0 || num2 > 99)
            {
                lblResult.Text = "數字二範圍不符，必須0到99";
                return;
            }

            string output = "";

            output = output + num1 + " - " + num2 + " = " + (num1-num2);

            lblResult.Text = output;
        }

        private void btnMul_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt32(txtN1.Text);
            int num2 = Convert.ToInt32(txtN2.Text);
            
            string output = "";

            output = output + num1 + " * " + num2 + " = " + (num1 * num2);

            lblResult.Text = output;
        }

        private void btnDiv_Click(object sender, EventArgs e)
        {
            try
            {
                int num1 = Convert.ToInt32(txtN1.Text);
                if (num1 < 0)
                {
                    //lblResult.Text = "錯誤：數字一小於Ø";
                    MessageBox.Show("數字一小於Ø", // 訊息
                                    "錯誤訊息",    // 標題
                                    MessageBoxButtons.OK, //確定鈕
                                    MessageBoxIcon.Error  // 圖示
                                   );
                    return;
                }
                if (num1 > 99)
                {
                    //lblResult.Text = "錯誤：數字一超過99";
                    MessageBox.Show("數字一超過99", // 訊息
                                    "錯誤訊息",     // 標題
                                    MessageBoxButtons.OK, //確定鈕
                                    MessageBoxIcon.Error  // 圖示
                                  );
                    return;
                }
                int num2 = Convert.ToInt32(txtN2.Text);
                if (num2 < 0)
                {
                    //lblResult.Text = "錯誤：數字二小於Ø";
                    MessageBox.Show("數字二小於Ø", // 訊息
                                    "錯誤訊息",    // 標題
                                    MessageBoxButtons.OK, //確定鈕
                                    MessageBoxIcon.Error  // 圖示
                                   );
                    return;
                }
                if (num2 > 99)
                {
                    //lblResult.Text = "錯誤：數字二超過99";
                    MessageBox.Show("數字二超過99", // 訊息
                                    "錯誤訊息",    // 標題
                                    MessageBoxButtons.OK, //確定鈕
                                    MessageBoxIcon.Error  // 圖示
                                  );
                    return;
                }

                string output = "";

                output = output + num1 + " / " + num2 + " = " + (num1 / num2);

                lblResult.Text = output;
            }
            catch (Exception ex)
            {
                //MessageBox.Show(ex.ToString(), "錯誤訊息");
                MessageBox.Show(ex.Message, "錯誤訊息",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                lblResult.Text = "";
            }
            
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtN1.Text = "";
            txtN2.Text = "";
            lblResult.Text = "";
        }

       
        private void txtNum1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == '\r')
                //MessageBox.Show("rrr");
                txtN2.Focus();
        }

        private void ArithmeticOp_Load(object sender, EventArgs e)
        {

        }

        
    }
}
