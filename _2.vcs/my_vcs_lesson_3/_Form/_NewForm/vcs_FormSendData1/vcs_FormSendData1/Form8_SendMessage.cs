using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData1
{
    public partial class Form8_SendMessage : Form
    {
        /* 預設 要改掉
        public Form8_SendMessage()
        {
            InitializeComponent();
        }
        */

        Form1 f1 = new Form1();

        public Form8_SendMessage(Form1 formFrm)//這個構造方法裡有參數
        {
            InitializeComponent();
            f1 = formFrm; //這個必須要有
        }

        private void Form8_SendMessage_Load(object sender, EventArgs e)
        {

        }

        int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            f1.MessageFromChildForm = "子表單傳送一個訊息給父表單\t" + (i++).ToString() + "\t" + DateTime.Now.ToString() + "\n";
        }
    }
}
