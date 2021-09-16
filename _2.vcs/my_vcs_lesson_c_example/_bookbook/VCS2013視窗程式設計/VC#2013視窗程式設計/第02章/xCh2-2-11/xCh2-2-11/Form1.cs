using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_Enter(object sender, EventArgs e)
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

        private void textBox1_Leave(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵離開textBox1物件時，
            // 更換前景與背景色
            textBox1.ForeColor = Color.Black;
            textBox1.BackColor = Color.White;
            textBox1.Select(0, 0);
        }
    }
}
