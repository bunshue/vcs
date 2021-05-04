using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _3._4_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void myButton_Click(object sender, EventArgs e)
        {
            myTextBox.Text = "您點擊了「這個按鈕」";
        }
        private void myTextBox_MouseHover(object sender, EventArgs e)
        {
            myTextBox.Text = "您的滑鼠游標現在在文字方塊上面";
        }
    }
}
