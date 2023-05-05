using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NewForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the dialog.
        private void btnSetName_Click(object sender, EventArgs e)
        {
            // Create and initialize the dialog.
            NameDialog dlg = new NameDialog();
            dlg.txtFirstName.Text = txtFirstName.Text;
            dlg.txtLastName.Text = txtLastName.Text;

            // Display the dialog and check the result.
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                // The user clicked OK. Save the values.
                txtFirstName.Text = dlg.txtFirstName.Text;
                txtLastName.Text = dlg.txtLastName.Text;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟新表單 並且從子表單取回回傳值
            Form2 f2 = new Form2();

            f2.ShowDialog();  //顯示表單          

            if (f2.DialogResult == DialogResult.OK)
            { //判斷使用者的動作
                richTextBox1.Text += "你在子表單上輸入了 " + f2.mInput + "\n";
                richTextBox1.Text += "你在子表單上輸入了 " + f2.getInput() + "\n";
                richTextBox1.Text += "你在子表單上輸入了 " + f2.richTextBox1.Text + "\n"; // 子表單的txtInput要宣告為public
            }
            else if (f2.DialogResult == DialogResult.Cancel)
            {
                richTextBox1.Text += "你按了取消鍵!\n";
            }
            else
            {
                richTextBox1.Text += "未知選項!\n";
            }

            f2.Dispose(); // 釋放表單資源

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //開啟新表單, 全螢幕, pictureBox放一圖

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            PictureBox pictureBox1 = new PictureBox();
            Form Form2 = new Form() { Size = new Size(1024, 768), WindowState = FormWindowState.Maximized };
            pictureBox1.Dock = DockStyle.Fill;
            pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox1.Image = Image.FromFile(filename);

            Form2.Controls.Add(pictureBox1);
            Form2.Show();

        }
    }
}
