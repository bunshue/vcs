using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TextBox2
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

            //設定 TextBox 之 自動完成字串
            //設定自定義來源字串
            AutoCompleteStringCollection source = new AutoCompleteStringCollection();
            source.AddRange(new string[]
            {
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            });
            tb_auto_complete1.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            //tb_auto_complete1.AutoCompleteMode = AutoCompleteMode.Suggest;
            tb_auto_complete1.AutoCompleteSource = AutoCompleteSource.CustomSource;
            tb_auto_complete1.AutoCompleteCustomSource = source;


            tb_auto_complete2.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            tb_auto_complete2.AutoCompleteSource = AutoCompleteSource.HistoryList;

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            int W = 300;
            int H = 160;

            groupBox0.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 340);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 6);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1380, 800);
            this.Text = "vcs_TextBox";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
