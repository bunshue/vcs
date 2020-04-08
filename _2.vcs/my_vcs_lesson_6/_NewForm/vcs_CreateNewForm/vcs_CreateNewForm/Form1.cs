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
            Form form_new = new Form();

            form_new.Cursor = System.Windows.Forms.Cursors.Cross;
            form_new.FormBorderStyle = FormBorderStyle.Sizable;
            form_new.Height = 400;
            form_new.HelpButton = true;
            form_new.MaximizeBox = true;
            form_new.MinimizeBox = true;
            form_new.Name = "New Form";
            form_new.ShowInTaskbar = true;
            form_new.StartPosition = FormStartPosition.CenterParent;
            form_new.Text = "New Form";
            form_new.Width = 500;
            form_new.WindowState = FormWindowState.Normal;
            form_new.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單, 需要等到新表單結束, 不可重複開啟新表單
            //form_new.ShowDialog();

            // 以Form類別的Show方法顯示視窗表單, 不用等到新表單結束, 可重複開啟新表單
            form_new.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用自己建立的Form2表單
            Form2 form_new = new Form2();     //實體化Form2視窗物件
            //form_new.StartPosition = FormStartPosition.CenterScreen;      //設定新表單的顯示位置, 居中顯示
            form_new.StartPosition = FormStartPosition.CenterParent;
            form_new.Show();
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
