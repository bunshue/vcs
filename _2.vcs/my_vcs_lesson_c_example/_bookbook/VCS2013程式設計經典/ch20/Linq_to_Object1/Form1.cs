using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;

using System.Text;
using System.Windows.Forms;

using System.Linq;  // 使用LINQ查詢必須引用System.Linq命名空間

namespace Linq_to_Object1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int[] score = new int[] { 89, 45, 100, 78, 60, 54, 37 };
        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            lstScore.DataSource = score;
            lblMsg.Text = "";

        }
        // 按 [查詢] 鈕執行此事件處理函式
        private void btnSearch_Click(object sender, EventArgs e)
        {
            var result = from s in score orderby s ascending where s > int.Parse(txtInput.Text) select s;
            lblMsg.Text = "共 " + (result.Count()).ToString() + " 筆資料大於等於 " + txtInput.Text + "\n";
            if (result.Count() > 0)
            {
                lblMsg.Text += "大於等於 " + txtInput.Text + " 資料：";
                foreach (var s in result)
                {
                    lblMsg.Text += s + ", ";
                }
            }
        }
    }
}