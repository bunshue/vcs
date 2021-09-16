using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsFirst
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入執行
        private void Form1_Load(object sender, EventArgs e)
        {
            lblShow.Text = "";
        }
        // 按下確定鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            lblShow.Text = "Hello, " + txtName.Text;
            lblShow.BackColor = Color.Yellow;
        }
        // 按下結束鈕執行
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
