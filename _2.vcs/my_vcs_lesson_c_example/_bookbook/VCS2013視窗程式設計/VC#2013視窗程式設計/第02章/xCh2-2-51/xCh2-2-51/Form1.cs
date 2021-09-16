using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_51
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (Control.IsKeyLocked(Keys.CapsLock))
            {
                label1.Text = "大寫鎖鍵已按下";
            }
            else
            {
                label1.Text = "大寫鎖鍵取消";
            }

            if (Control.IsKeyLocked(Keys.NumLock))
            {
                label1.Text += Environment.NewLine + "數字鎖鍵已按下";
            }
            else
            {
                label1.Text = Environment.NewLine + "數字鎖鍵已取消";
            }
        }
    }
}


