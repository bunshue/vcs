using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinAddRemoveEvent
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // ===  自訂MyTextChanged事件處理函式
        private void MyTextChanged(object sender, EventArgs e)
        {
            try
            {
                int n1, n2;
                n1 = int.Parse(textBox1.Text);
                n2 = int.Parse(textBox2.Text);
                lblAns.Text = (n1 + n2).ToString();
            }
            catch (Exception ex)
            {
            }
        }
        // ===  按下 [新增事件] 鈕執行
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.TextChanged += new EventHandler(MyTextChanged);
            textBox2.TextChanged += new EventHandler(MyTextChanged);
        }
        // ===  按下 [移除事件] 鈕執行
        private void btnRemoveEvent_Click(object sender, EventArgs e)
        {
            textBox1.TextChanged -= new EventHandler(MyTextChanged);
            textBox2.TextChanged -= new EventHandler(MyTextChanged);
        }

        private void btnAddEvent_Click(object sender, EventArgs e)
        {
            textBox1.TextChanged += new EventHandler(MyTextChanged);
            textBox2.TextChanged += new EventHandler(MyTextChanged);
        }
    }
}
