using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DynamicAddRemoveControls7
{
    public partial class Form1 : Form
    {
        int cnt = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Button btn = new Button();

            //設定新控件的名稱和Text屬性，以及產生的位置
            btn.Left = e.X;
            btn.Top = e.Y;
            btn.Name = "Button " + cnt;
            btn.Text = "Button" + cnt;
            btn.Size = new Size(70, 35);

            //為產生的新的Button控件設定事件
            btn.Click += new EventHandler(btn_Click);
            btn.MouseEnter += new EventHandler(btn_MouseEnter);
            btn.MouseLeave += new EventHandler(btn_MouseLeave);

            //在窗體中顯示此控件
            this.Controls.Add(btn);

            richTextBox1.Text += "新增控件 " + btn.Text + "\n";
            cnt++;
        }

        //定義事件
        private void btn_Click(object sender, System.EventArgs e)
        {
            if (sender.GetType() == typeof(Button))
            {
                Button control = (Button)sender;
                richTextBox1.Text += "你按了 " + control.Text + "\n";
            }
        }

        private void btn_MouseEnter(object sender, System.EventArgs e)
        {
            Button currentTextBox = (Button)sender;
            currentTextBox.BackColor = Color.Yellow;    //設定按鈕的背景色
        }

        private void btn_MouseLeave(object sender, System.EventArgs e)
        {
            Button currentTextBox = (Button)sender;
            currentTextBox.BackColor = System.Drawing.SystemColors.ControlLight;    //設定按鈕的背景色
        }
    }
}
