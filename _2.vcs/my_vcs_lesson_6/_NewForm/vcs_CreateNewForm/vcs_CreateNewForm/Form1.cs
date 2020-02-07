using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CreateNewForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 繼承Form類別產生新的視窗表單
            Form Form2 = new Form();

            Form2.Cursor = System.Windows.Forms.Cursors.Cross;
            Form2.FormBorderStyle = FormBorderStyle.Sizable;
            Form2.Height = 400;
            Form2.HelpButton = true;
            Form2.MaximizeBox = true;
            Form2.MinimizeBox = true;
            Form2.Name = "Form2";
            Form2.ShowInTaskbar = true;
            Form2.StartPosition = FormStartPosition.CenterParent;
            Form2.Text = "New Form 2";
            Form2.Width = 500;
            Form2.WindowState = FormWindowState.Normal;
            Form2.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單, 需要等到新表單結束, 不可重複開啟新表單
            //Form2.ShowDialog();

            // 以Form類別的Show方法顯示視窗表單, 不用等到新表單結束, 可重複開啟新表單
            Form2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用自己建立的Form2表單
            Form2 f2 = new Form2();     //實體化Form2視窗物件
            f2.StartPosition = FormStartPosition.CenterScreen;      //設定新表單的顯示位置, 居中顯示
            f2.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }
    }
}
