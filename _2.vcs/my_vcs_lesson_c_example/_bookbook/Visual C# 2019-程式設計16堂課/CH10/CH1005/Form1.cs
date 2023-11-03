using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1005
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnShow_Click(object sender, EventArgs e)
        {
            string msg = "要儲存檔案？";
            string caption = "第10章";
            MessageBoxButtons btns = MessageBoxButtons.YesNo;
            //只顯示訊息
            MessageBox.Show(msg);
            //訊息、標題、兩個按鈕
            MessageBox.Show(msg, caption, btns);
        }
    }
}
