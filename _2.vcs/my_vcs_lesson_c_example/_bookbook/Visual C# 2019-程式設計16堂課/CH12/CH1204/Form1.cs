using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1204
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void lblCheck_MouseLeave(object sender, EventArgs e)
        {
            lblCheck.BackColor = Color.PapayaWhip;
        }

        private void lblCheck_MouseEnter(object sender, EventArgs e)
        {
            lblCheck.BackColor = Color.Pink;
        }
        //移動滑鼠時取得座標值
        private void lblCheck_MouseMove(object sender, MouseEventArgs e)
        {
            lblCheck.Left = lblCheck.Left + e.X -
               (lblCheck.Width / 2);
            lblCheck.Top = lblCheck.Top + e.Y -
               (lblCheck.Top / 2);
            lblCheck.Text = $"X:{lblCheck.Left}, " +
               $"Y:{lblCheck.Top}";
        }
    }
}
