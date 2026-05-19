using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NewForm1
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            show_item_location();

            button0.DialogResult = System.Windows.Forms.DialogResult.OK;
            button1.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            button2.DialogResult = System.Windows.Forms.DialogResult.Retry;
            button3.DialogResult = System.Windows.Forms.DialogResult.Ignore;
            button4.DialogResult = System.Windows.Forms.DialogResult.Yes;

            button0.Text = "直接回傳 OK";
            button1.Text = "直接回傳 Cancel";
            button2.Text = "直接回傳 Retry";
            button3.Text = "直接回傳 Ignore";
            button4.Text = "直接回傳 Yes";
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

            this.Size = new Size(500, 500);
            this.Text = "vcs_NewForm1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) * 4 / 5, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

    }
}
