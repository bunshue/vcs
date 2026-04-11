using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form1_NewForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            btn_exit.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            richTextBox1.Size = new Size(300, 680);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 784);
            this.Text = "vcs_test_all_00_Usually";





        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立新表單
            Form Form_new = new Form
            {
                Text = "新表單",
                BackColor = Color.Pink,   //背景色
                FormBorderStyle = FormBorderStyle.Fixed3D,
                //設定表單大小，方法Size(width, height)
                Size = new Size(640, 480),
                //自動調整大小-依控制項放大一倍
                AutoSize = true,
                AutoSizeMode = AutoSizeMode.GrowOnly,
            };

            //在新表單加入控件
            Button btn = new Button
            {
                Text = "顯示",
                Font = new Font("新細明體", 14),
                AutoSize = true,
                //以Location屬性設定按鈕在表單的位置
                Location = new Point(75, 40)
            };

            //Form.CancelButton 屬性
            //取得或設定使用者按下 ESC 鍵時所按下的按鈕控制項。
            Form_new.CancelButton = btn_exit;

            Form_new.Controls.Add(btn);//加入控件

            Form_new.Show();//顯示表單

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立新表單2
            //建立新表單
            Form form1 = new Form();

            //建立新控件
            Button button1 = new Button();
            Button button2 = new Button();

            button1.Text = "OK";
            button1.Location = new Point(10, 10);

            button2.Text = "Cancel";
            button2.Location = new Point(10, 100);

            form1.Text = "My Dialog Box";
            form1.HelpButton = true;

            // Define the border style of the form to a dialog box.
            form1.FormBorderStyle = FormBorderStyle.FixedDialog;
            // Set the MaximizeBox to false to remove the maximize box.
            form1.MaximizeBox = false;
            // Set the MinimizeBox to false to remove the minimize box.
            form1.MinimizeBox = false;
            // Set the accept button of the form to button1.
            form1.AcceptButton = button1;
            // Set the cancel button of the form to button2.
            form1.CancelButton = button2;
            // Set the start position of the form to the center of the screen.
            form1.StartPosition = FormStartPosition.CenterScreen;

            // Add button1 to the form.
            form1.Controls.Add(button1);
            // Add button2 to the form.
            form1.Controls.Add(button2);

            // Display the form as a modal dialog box.
            form1.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void btn_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
