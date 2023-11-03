using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1206
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up)
            {
                lblState.Text = "向上";
                if (lblTarget.Top + lblTarget.Height <= 0)
                    lblTarget.Top = lblTarget.Height;
                else
                    lblTarget.Top -= 10;
            }
            else if (e.KeyCode == Keys.Down)
            {
                lblState.Text = "向下";
                if (lblTarget.Top >= this.Height)
                    lblTarget.Top = 0 - lblTarget.Height;
                else
                    lblTarget.Top += 10;
            }
            else if (e.KeyCode == Keys.Right)
            {
                lblState.Text = "向右";
                if (lblTarget.Left >= this.Width)
                    lblTarget.Left = lblTarget.Width;
                else
                    lblTarget.Left += 10;
            }
            else if (e.KeyCode == Keys.ShiftKey)
            {
                lblState.Text = "座標：" + (new Point(
                   lblTarget.Right,
                   this.lblTarget.Bottom)).ToString();
            }
            lblMsg.Text = $"按鍵值：{e.KeyValue.ToString()}";
        }
    }
}
