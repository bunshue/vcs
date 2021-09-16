using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_GotFocus(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵移到textBox1物件時，
            // 更換前景與背景顏色
            if (textBox1.Text != String.Empty)
            {
                textBox1.ForeColor = Color.Red;
                textBox1.BackColor = Color.Black;
                // 移動插入點(selection pointer)到最後
                textBox1.Select(textBox1.Text.Length, 0);
            }
        }

        private void textBox1_LostFocus(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵離開textBox1物件時，
            // 更換前景與背景色
            textBox1.ForeColor = Color.Black;
            textBox1.BackColor = Color.White;
            textBox1.Select(0, 0);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.GotFocus += new EventHandler(textBox1_GotFocus);
            textBox1.LostFocus += new EventHandler(textBox1_LostFocus);
        }
    }
}



