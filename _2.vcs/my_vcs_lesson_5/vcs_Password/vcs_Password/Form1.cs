using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Password
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //PasswordForm的button1的DialogResult要改成OK;

            // Get the password from the user.
            PasswordForm frm = new PasswordForm();
            if (frm.ShowDialog() == DialogResult.Cancel)
                this.Close();

            // See if the password is correct.
            string password = frm.textBox1.Text;
            if (password != "iloveims")
                this.Close();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


