using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Area
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string uName = Microsoft.VisualBasic.Interaction.InputBox("請輸入姓名", "輸入");
            DialogResult dr = MessageBox.Show(uName + "歡迎您！", "歡迎",
                MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            this.Text = uName;	//表單標題顯示姓名
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            try
            {
                int w = Convert.ToInt32(txtW.Text);
                int h = Convert.ToInt32(txtH.Text);
                lblArea.Text = "面積等於：" + Convert.ToString(w * h) + "平方公分";
            }
            catch
            {
                MessageBox.Show("請輸入寬和高度！", "注意",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }
}
