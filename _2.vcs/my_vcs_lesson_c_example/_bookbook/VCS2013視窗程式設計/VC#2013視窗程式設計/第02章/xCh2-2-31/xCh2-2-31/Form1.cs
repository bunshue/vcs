using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_31
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            string errorMsg;

            if (!ValidEmailAddress(textBox1.Text, out errorMsg))
            {
                // 取消事件，並選取錯誤的文字
                e.Cancel = true;
                textBox1.Select(0, textBox1.Text.Length);

                // 秀出錯誤訊息
                textBox2.Text = errorMsg;
            }
        }

        public bool ValidEmailAddress(string emailAddress, out string errorMessage)
        {
            // 確定e-mail address並非空白
            if (emailAddress.Length == 0)
            {
                errorMessage = "請輸入電子郵件信箱，不可以空白";
                return false;
            }

            // 確定電子郵件信箱是否含有1個 "@" 與 "." 字元
            if (emailAddress.IndexOf("@") > -1)
            {
                if (emailAddress.IndexOf(".", emailAddress.IndexOf("@")) > emailAddress.IndexOf("@"))
                {
                    errorMessage = "";
                    return true;
                }
            }

            errorMessage = "無效的電子郵件信箱";
            return false;
        }

        private void textBox1_Validated(object sender, EventArgs e)
        {
            textBox2.Text = "電子郵信箱格式無誤";
        }
    }
}
