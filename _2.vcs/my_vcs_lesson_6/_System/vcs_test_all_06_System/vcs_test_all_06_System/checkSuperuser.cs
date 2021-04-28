using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_06_System
{
    public partial class checkSuperuser : Form
    {
        public checkSuperuser()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string id = user_id.Text;
            string pw = password.Text;

            //check id and pw
            if (id == "" || pw == "")
            {
                MessageBox.Show("ID and Password could not be null");
                //result.Text = "please check input value";
                return;
            }

            if (id == "david" || pw == "jp6rmp4")
            {
                richTextBox1.Text += "登入成功\n";


            }
            else
            {
                richTextBox1.Text += "登入失敗\n";
                user_id.Clear();
                password.Clear();
            }

            //MessageBox.Show("Login Successful");
            //this.Hide();
            //frmMain fm = new frmMain();
            //fm.Show();


        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
