using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_Tictactoe5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void clickMe(object sender, EventArgs e)
        {
            System.Windows.Forms.PictureBox obj = ((System.Windows.Forms.PictureBox)sender);
            if(obj.Image==null)
            {
                if (state )
                {
                    ((System.Windows.Forms.PictureBox)sender).Image = global::vcs_Tictactoe5.Properties.Resources.O;
                }
                else 
                {
                    ((System.Windows.Forms.PictureBox)sender).Image = global::vcs_Tictactoe5.Properties.Resources.X;
                }
                this.state = !this.state;
            }
        }
    }
}
