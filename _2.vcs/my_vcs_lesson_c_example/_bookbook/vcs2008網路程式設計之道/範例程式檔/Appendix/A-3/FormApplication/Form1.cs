using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace FormApplication
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
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
            Form2.Text = "New Form";
            Form2.Width = 500;
            Form2.WindowState = FormWindowState.Normal;
            Form2.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單
            Form2.ShowDialog();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
