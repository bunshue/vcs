using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//專案/加入/Windows Form(F), 新增子表單Form2

namespace vcs_FormSendData3
{
    public partial class Form1 : Form
    {
        #region 子窗口刷新父窗口的值

        private string message = "";

        public string MessageFromChildForm
        {
            get
            {
                return message;
            }
            set
            {
                message = value;
                this.richTextBox1.Text += message;
            }
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2(this);//這裡注意傳個this
            f2.Show();
            f2.Location = new Point(this.Location.X + this.Width, this.Location.Y);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}

