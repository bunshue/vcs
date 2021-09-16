using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_8_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 清除TextBox的文字內容
            textBox1.Clear();
            foreach (Control x in Controls)
            {
                if (x.GetType().ToString() == "System.Windows.Forms.CheckBox")
                {

                    System.Windows.Forms.CheckBox myCheckbox =
                        (System.Windows.Forms.CheckBox)x;

                    // 如果CheckBox物件被點選，則將CheckBox物件
                    // 的文字內容附加在TextBox物件中
                    if (myCheckbox.Checked)
                        textBox1.AppendText(myCheckbox.Text + "\n");
                }
            }
        }
    }
}


