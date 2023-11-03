using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1205
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            lblShow.Text = "KeyDown事件";
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //屬性KeyChar取得鍵盤按下的字元
            lblShow.Text = $"KeyPress事件, " + Environment.NewLine
               + $"按了鍵盤 {e.KeyChar.ToString()}";
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            lblShow.Text = "KeyUp事件";
        }
    }
}
