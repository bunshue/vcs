using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1002
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //產生第二個表單並設屬性
            Form frmSecond = new Form
            {
                Text = "第二個表單",
                BackColor = Color.Pink,   //背景色
                FormBorderStyle = FormBorderStyle.Fixed3D,
                //設定表單大小，方法Size(width, height)
                Size = new Size(120, 150),
                //自動調整大小-依控制項放大一倍
                AutoSize = true,
                AutoSizeMode = AutoSizeMode.GrowOnly,
            };
            //第二個表單加入按鈕控制項並設定屬性
            Button btnSecond = new Button
            {
                Text = "顯示",
                Font = new Font("新細明體", 14),
                AutoSize = true,
                //以Location屬性設定按鈕在表單的位置
                Location = new Point(75, 40)
            };
            frmSecond.CancelButton = btnExit;
            //將按鈕加到第二個表單，呼叫Show()方法顯示表單
            frmSecond.Controls.Add(btnSecond);
            frmSecond.Show();
        }
    }
}
