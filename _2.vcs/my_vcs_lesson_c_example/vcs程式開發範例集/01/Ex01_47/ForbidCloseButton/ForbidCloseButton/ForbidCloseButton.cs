using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ForbidCloseButton
{
    public partial class ForbidCloseButton : Form
    {
        public ForbidCloseButton()
        {
            InitializeComponent();
        }

        protected override void WndProc(ref Message m)
        {
            const int WM_SYSCOMMAND = 0x0112;
            const int SC_CLOSE = 0xF060;
            if((m.Msg == WM_SYSCOMMAND) && ((int)m.WParam == SC_CLOSE))
            {
                return;
            }
            base.WndProc(ref m);
        }

        private void ExitProgram_Click(object sender,EventArgs e)
        {
            Application.Exit();
        }
    }
}
