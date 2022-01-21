using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData3
{
    public partial class Form2 : Form
    {
        /* 預設 要改掉
        public Form2()
        {
            InitializeComponent();
        }
        */

        Form1 f1 = new Form1();

        public Form2(Form1 formFrm)//這個構造方法裡有參數
        {
            InitializeComponent();
            f1 = formFrm; //這個必須要有
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            f1.MessageFromChildForm = "子表單傳送一個訊息給父表單\t" + (i++).ToString() + "\t" + DateTime.Now.ToString() + "\n";

        }
    }
}
