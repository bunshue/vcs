using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip1.InitialDelay = 10;
            toolTip1.ReshowDelay = 500;

            toolTip1.IsBalloon = true;
            toolTip1.ToolTipIcon = ToolTipIcon.Info;
            toolTip1.ToolTipTitle = "小提示";

            toolTip1.ShowAlways = true;

            toolTip1.SetToolTip(textBox1, "textBox1預設的文字");
            toolTip1.SetToolTip(button1, "button1預設的文字");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(textBox1, textBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = toolTip1.GetToolTip(textBox1); 
        }

        private void button3_Click(object sender, EventArgs e)
        {
            toolTip1.RemoveAll();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                if (textBox1.Text != "")
                    Convert.ToInt32(textBox1.Text);
            }
            catch (Exception ex)
            {
                toolTip1.ToolTipIcon = ToolTipIcon.Error;
                toolTip1.Show("請輸入數字 ！", textBox1, 2000);
            }
        }
    }
}
