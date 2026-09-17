using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_search_history
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

            //------------------------------------------------------------  # 60個

            string old_search_history = Properties.Settings.Default.search_pattern;

            richTextBox1.Text += "old_search_history : " + old_search_history + "\n";

            string[] patterns = old_search_history.Split(';');
            foreach (string pattern in patterns)
            {
                richTextBox1.Text += pattern + "\n";
                listBox1.Items.Add(pattern);
            }
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 50 + 10;

            listBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_add_pattern.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 0);
            bt_remove_pattern.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 0 + 30);
            bt_clear_pattern.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 0 + 60);

            //tb_search

            richTextBox1.Size = new Size(600, 400);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(700, 800);
            this.Text = "vcs_search_history";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            int len = listBox1.Items.Count;
            richTextBox1.Text += "len : " + len.ToString() + "\n";

            //儲存搜尋歷史資料
            string search_history = string.Empty;
            for (int i = 0; i < len; i++)
            {
                search_history += listBox1.Items[i];
                if (i < (listBox1.Items.Count - 1))
                {
                    search_history += ";";
                }
            }
            richTextBox1.Text += "save : " + search_history + "\n";
            Properties.Settings.Default.search_pattern = search_history;
            Properties.Settings.Default.Save();
        }

        //------------------------------------------------------------  # 60個

        private void tb_search_KeyPress(object sender, KeyPressEventArgs e)
        {
            //e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                //button5_Click(sender, e);
                string new_search_pattern = tb_search.Text;
                listBox1.Items.Add(new_search_pattern);
                tb_search.Clear();

            }

        }

        private void bt_add_pattern_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("AAAAAA");
        }

        private void bt_remove_pattern_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "移除了 " + listBox1.SelectedItem + "\n";
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void bt_clear_pattern_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


