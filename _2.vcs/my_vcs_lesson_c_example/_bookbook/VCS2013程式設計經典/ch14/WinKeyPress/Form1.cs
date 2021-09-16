using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinKeyPress
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // ===  表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            txtPrice.Text = "0"; 
            txtQty.Text = "0";
            txtTotal.Text = "0";
            txtTotal.ReadOnly = true;
        }
        // txtId產品編號文字方塊的Text屬性改變時執行
        private void txtId_TextChanged(object sender, EventArgs e)
        {
            int Loc = txtId.SelectionStart;   　 // 儲存目前游標位置       
            // 當字母轉成大寫指定給txtId.Text時游標移到字串最後
            txtId.Text = txtId.Text.ToUpper();　
            txtId.SelectionStart = Loc;　　　　　// 將游標還原到原來位置
        }
        // ===  在txtId產品編號文字方塊按鍵後再放開時執行
        private void txtId_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (txtId.Text.Length < 6)//檢查輸入的產品編號長度是否超過六個字元
            {
                if (txtId.SelectionStart == 0)//檢查輸入的第一個字元是否為字母
                {   //將輸入的字母轉成大寫
                    string S = e.KeyChar.ToString().ToUpper();　
                    if (S.CompareTo("A") < 0 || S.CompareTo("Z") > 0)
                    {
                     // 若輸入的第一個字元不是字母,取消輸入字元不顯示,游標停在原處
                        e.Handled = true;　
                    }
                }
                else　// 若輸入的字元是第2個(含)以後的字元執行此段程式碼
                {
                    if (e.KeyChar.CompareTo('0') < 0 ||
 						e.KeyChar.CompareTo('9') > 0)
                    {
                        if (e.KeyChar!='\b')//若輸入的字元非數字且不是倒退鍵
                        {
                            e.Handled=true;//取消輸入字元不顯示,游標停在原處
                        }
                    }
                }
            }
            else　　//若輸的字元的長度超過6個字元執行此區段程式碼
            {
                if (e.KeyChar!='\b')//若是倒退鍵,取消輸入字元不顯示,游標停在原處
               {
                    e.Handled = true;
                }
            }
        }
        // ===  txtPrice單價文字方塊的Text屬性改變時執行
        private void txtPrice_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int price = int.Parse(txtPrice.Text);
                int qty = int.Parse(txtQty.Text);
                txtTotal.Text = (price * qty).ToString();
            }
            catch//若輸入的資料有誤執行此空區段程式碼,不處理所發生的錯誤
            { }
        }
        // === 在txtPrice單價文字方塊按鍵後再放開時執行
        private void txtPrice_KeyPress(object sender, KeyPressEventArgs e)
        {
            //若輸入的字元是非數字且不是倒退鍵 
            if ((e.KeyChar < '0' || e.KeyChar > '9') && (e.KeyChar != '\b'))
            {
                e.Handled = true;  //取消輸入字元不顯示,游標停在原處　             
            }
        }
        // === txtQty數量文字方塊的Text屬性改變時執行
        private void txtQty_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int price = int.Parse(txtPrice.Text);
                int qty = int.Parse(txtQty.Text);
                txtTotal.Text = (price * qty).ToString();
            }
            catch
            { }

        }
        // === 在txtQty數量文字方塊按鍵後再放開時執行
        private void txtQty_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < '0' || e.KeyChar > '9') && (e.KeyChar != '\b'))
            {
                e.Handled = true;
            }
        }
    }
}
