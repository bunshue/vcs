using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_1_11
{
    public partial class Form2 : Form
    {
        static int count = 0;

        private void Form2_Load(object sender, EventArgs e)
        {
            count += 1;
            this.Text = "第 " + count.ToString() + " 張表單";
        }

        private void Form2_Activated(object sender, EventArgs e)
        {
            label1.Text = "目前已開啟的表單數：" + count;
        }

        private void Form2_Shown(object sender, EventArgs e)
        {
            MessageBox.Show("已引發 Form.Shown 事件");
        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            DialogResult result = MessageBox.Show("是否要關閉表單？",
                "FormClosing事件" + e.CloseReason.ToString(),
                MessageBoxButtons.OKCancel, MessageBoxIcon.Warning,
                MessageBoxDefaultButton.Button2);

            if (result == DialogResult.Cancel)
                e.Cancel = true;
        }

        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
        {
            MessageBox.Show("關閉表單的原因：" + e.CloseReason.ToString(), "FormClosed事件");

            count -= 1;
            label1.Text = "目前已開啟的表單數：" + count;
        }

        public Form2()
        {
            InitializeComponent();
        }
    }
}


