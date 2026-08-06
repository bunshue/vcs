using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NewForm4
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
            this.Text = "vcs_NewForm4";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            // 建立新表單1

            Form Form_new = new Form
            {
                Text = "新表單",
                BackColor = Color.Pink,  // 背景色
                FormBorderStyle = FormBorderStyle.Fixed3D,
                Size = new Size(640, 480),  // 設定表單大小
                AutoSize = true,  // 自動調整大小-依控制項放大一倍
                AutoSizeMode = AutoSizeMode.GrowOnly,
            };

            //在新表單加入控件
            Button btn = new Button
            {
                Text = "顯示",
                Font = new Font("新細明體", 14),
                AutoSize = true,
                Location = new Point(75, 40)  // 控件位置
            };

            // Form.CancelButton 屬性
            // 取得或設定使用者按下 ESC 鍵時所按下的按鈕控制項。
            Form_new.CancelButton = btn_exit;

            Form_new.Controls.Add(btn);//加入控件

            Form_new.Show();//顯示表單
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            // 建立新表單2
            Form form1 = new Form();

            //建立新控件
            Button button1 = new Button();
            button1.Text = "OK";
            button1.Location = new Point(10, 10);

            Button button2 = new Button();
            button2.Text = "Cancel";
            button2.Location = new Point(10, 100);

            form1.Text = "新建對話框";
            form1.HelpButton = true;

            // Define the border style of the form to a dialog box.
            form1.FormBorderStyle = FormBorderStyle.FixedDialog;
            // Set the MaximizeBox to false to remove the maximize box.
            form1.MaximizeBox = false;
            // Set the MinimizeBox to false to remove the minimize box.
            form1.MinimizeBox = false;
            // Set the accept button of the form to button1.
            form1.AcceptButton = button1;  // 設定AcceptButton
            // Set the cancel button of the form to button2.
            form1.CancelButton = button2;  // 設定CancelButton
            // Set the start position of the form to the center of the screen.
            form1.StartPosition = FormStartPosition.CenterScreen;

            form1.Controls.Add(button1);
            form1.Controls.Add(button2);

            form1.ShowDialog();
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            // 建立新表單3, 繼承Form類別產生新的視窗表單

            Form form_new = new Form();

            form_new.Cursor = System.Windows.Forms.Cursors.Cross;
            form_new.FormBorderStyle = FormBorderStyle.Sizable;
            form_new.Height = 400;
            form_new.HelpButton = true;
            form_new.MaximizeBox = true;
            form_new.MinimizeBox = true;
            form_new.Name = "New Form";
            form_new.ShowInTaskbar = true;
            form_new.StartPosition = FormStartPosition.CenterParent;
            form_new.Text = "New Form";
            form_new.Width = 500;
            form_new.WindowState = FormWindowState.Normal;
            form_new.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單, 需要等到新表單結束, 不可重複開啟新表單
            //form_new.ShowDialog();

            // 以Form類別的Show方法顯示視窗表單, 不用等到新表單結束, 可重複開啟新表單
            form_new.Show();
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //建立新表單4
            richTextBox1.Text += "繼承Form類別產生新的視窗表單\n";

            Form Form2 = new Form();

            Form2.Cursor = Cursors.Cross;
            Form2.FormBorderStyle = FormBorderStyle.Sizable;
            Form2.Width = 800;
            Form2.Height = 800;
            Form2.HelpButton = true;
            Form2.MaximizeBox = true;
            Form2.MinimizeBox = true;
            Form2.Name = "Form2";
            Form2.ShowInTaskbar = true;
            Form2.StartPosition = FormStartPosition.CenterParent;
            Form2.Text = "New Form";
            Form2.WindowState = FormWindowState.Normal;
            Form2.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單
            Form2.ShowDialog();
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void btn_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

