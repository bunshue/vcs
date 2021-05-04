using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace DynamicTailorControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public int counter = 1;
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            TextBox txtx = new TextBox();
            //設定他的名稱和Text屬性，以及產生的位置
            txtx.Left = e.X;
            txtx.Top = e.Y;
            txtx.Name = "TextBox " + counter;
            txtx.Text = "文本框" + counter;
            //為產生的新的TextBox組件設定事件，本文中為產生的文本框設定了２個事件
            txtx.Click += new EventHandler(txtx_Click);
            txtx.MouseEnter += new EventHandler(txtx_MouseEnter);
            //在窗體中顯示此文本框
            this.Controls.Add(txtx);
            counter++;
        }
        //定義事件
        private void txtx_Click(object sender, System.EventArgs e)
        {
            if (sender.GetType() == typeof(TextBox))
            {
                TextBox control = (TextBox)sender;
                MessageBox.Show(control.Text + "被按動了！");
            }
        }
        private void txtx_MouseEnter(object sender, System.EventArgs e)
        {
            //出箱

            TextBox currentTextBox = (TextBox)sender;
            //設定按鈕的背景色
            currentTextBox.BackColor = Color.Yellow;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}