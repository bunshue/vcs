using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinMonthcalendar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            // 建立Product陣列用來存放產品
            string[] Product = new string[] { "火影忍者", "航海王",
 				"史瑞克4", "葉問2", "鋼鐵人2", "偷心大聖PS男", "阿凡達",
 				"半夜鬼上床", "第一次愛上你", "松藥局的兒子們", "老婆，給我飯" };
            // 將Product陣列的所有選項放入checkedListBox1內
            checkedListBox1.Items.AddRange(Product); 
            checkedListBox1.MultiColumn = true;	// 核取清單方塊設為多欄
            checkedListBox1.ColumnWidth = 150; 	// 核取清單方塊欄寬150
            monthCalendar1.MinDate=DateTime.Now;// 日曆控制項最小可選日期為今日
            checkedListBox1.CheckOnClick = true; // 只按一下選取

        }
        // 按 [確定] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            textBox1.Text = "訂購產品如下" + Environment.NewLine + Environment.NewLine;
            // 逐一檢查每一個核取方塊是否被選取
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                // 若第i個核取方塊被選取，即將該產品顯示在textBox1
                if (checkedListBox1.GetItemChecked(i)) 
                {
                    textBox1.Text += "　．" + checkedListBox1.Items[i].ToString() + 	Environment.NewLine;
                }
            }
            // 在textBox1上顯示送貨日期的範圍
            textBox1.Text +=  Environment.NewLine + "指定送貨日期為"+
 				monthCalendar1.SelectionRange .Start.ToShortDateString()+
 				"至" + monthCalendar1.SelectionRange.End.
 				ToShortDateString() + " 送達貴處" ;
        }
        // 按 [重選] 鈕執行
        private void btnReSet_Click(object sender, EventArgs e)
        {
            // 設定所有核取方塊不勾選
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked (i, false);
            }
            textBox1.Text = "";
        }
        // 按 [結束] 鈕執行
        private void btnEnd_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
