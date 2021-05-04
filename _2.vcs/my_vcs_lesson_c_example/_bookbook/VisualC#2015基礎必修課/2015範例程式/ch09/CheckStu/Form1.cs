using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CheckStu
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //定義學生的學號陣列StuId及姓名陣列StuName
        string[] StuId = new string[] { "8001", "8002", "8003", "8004", "8005" };
        string[] StuName = new string[] { "劉學有", "張杰輪", "周立宏", "王吉吉", "陶得華" };
        // 在txtId文字方塊按一鍵盤時會執行此事件處理函式
        private void txtId_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar.CompareTo('0') < 0 || e.KeyChar.CompareTo('9') > 0) && e.KeyChar != '\b')
            {
                e.Handled = true;
            }
        }
        // 按下 [確定] 鈕執行 
        private void btnOk_Click(object sender, EventArgs e)
        {
            // 使用Array.IndexOf方法搜尋txtId.Text在StuId陣列中是第幾個元素
            int search_num = Array.IndexOf(StuId, txtId.Text);
            if (search_num != -1)
            {
                lblMsg.Text = StuName[search_num] + "    歡迎光臨!!";
            }
            else
            {
                lblMsg.Text = "Sorry!   查無此學生!!";
            }
        }
    }
}
