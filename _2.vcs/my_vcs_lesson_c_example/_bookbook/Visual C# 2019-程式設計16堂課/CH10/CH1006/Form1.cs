using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1006
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }

        //屬性-自動實作
        public int num1 { get; set; }
        public int num2 { get; set; }
        public int outcome { get; set; }

        //兩數相加
        private void btnAdd_Click(object sender, EventArgs e)
        {
            //將文字方塊取得的字串轉為數值
            num1 = Convert.ToInt32(txtNum1.Text);
            num2 = Convert.ToInt32(txtNum2.Text);
            if (num1 == 0 || num2 == 0)
            {
                Display();   //呼叫方法
            }
            else
            {
                NumCalc(num1, num2, 1);   //呼叫方法
            }
        }

        //兩數相減
        private void btnSubtract_Click(object sender, EventArgs e)
        {
            num1 = Convert.ToInt32(txtNum1.Text);
            num2 = Convert.ToInt32(txtNum2.Text);
            if (num1 == 0 || num2 == 0)
            {
                Display();
            }
            else
            {
                NumCalc(num1, num2, 2);
            }
        }
        //求餘數
        private void btnMod_Click(object sender, EventArgs e)
        {
            num1 = Convert.ToInt32(txtNum1.Text);
            num2 = Convert.ToInt32(txtNum2.Text);
            if (num1 == 0 || num2 == 0)
            {
                Display();   //呼叫方法處理訊息方塊
            }
            else
            {
                NumCalc(num1, num2, 3);   //呼叫方法做數值運算
            }
        }

        //處理MessageBox
        private void Display()
        {
            //設定MessageBox的相關參數
            string st1 = "是否繼續？";   //訊息內容
            string caption = "無法計算"; //標題列
            MessageBoxButtons buttons =    //確認和取消兩個按鈕
               MessageBoxButtons.OKCancel;
            //設定訊息方塊的圖示
            MessageBoxIcon warn = MessageBoxIcon.Warning;
            DialogResult result;   //取得訊息方塊的回傳值
            result = MessageBox.Show(
               st1, caption, buttons, warn);
            InfoNumber(result);   //訊息方塊的回應處理
        }

        //傳入DialogResult引數：按Yes繼續，按No結束表單
        private void InfoNumber(DialogResult info)
        {
            if (info == DialogResult.OK)
            {
                //清除文字方塊內容並將焦點放在第一個文字方塊
                txtNum1.Clear();
                txtNum2.Clear();
                txtNum1.Focus();
            }
            else
                this.Close();   //關閉表單
        }

        //定義方法-進行簡單的運算
        public void NumCalc(int n1, int n2, int n3)
        {
            int num1 = n1;
            int num2 = n2;

            //依據傳入參數值做運算
            switch (n3)
            {
                case 1:
                    outcome = num1 + num2;
                    break;
                case 2:
                    outcome = num1 - num2;
                    break;
                default:
                    outcome = num1 % num2;
                    break;
            }
            string st2 = $"結果 {outcome:N0}";
            MessageBox.Show(st2);
        }
    }
}
