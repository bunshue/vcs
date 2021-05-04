using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace IndexOf
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] stu = new string[] { "趙一", "林二", "張三", "李四", "王五" };
            int[] score = new int[] { 95, 100, 100, 92, 100 };
            string msg = "一百分學生：";
            int index = Array.IndexOf(score, 100);   //搜尋第一個滿分學生
            while (index >= 0)                   //當index >= 0繼續迴圈
            {
                msg += stu[index] + ", ";                   // 顯示學生姓名
                index = Array.IndexOf(score, 100, index + 1);  // 從下一筆繼續搜尋
            };
            MessageBox.Show(msg);
            Application.Exit();
        }
    }
}
