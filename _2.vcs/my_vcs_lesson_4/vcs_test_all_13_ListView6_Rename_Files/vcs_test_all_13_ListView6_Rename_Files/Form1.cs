using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

/*
 * ListView加入欄標題
 * 屬性 / 編輯資料行 / ColumnHeader集合編輯器 / 加入ColumnHeader
 */

namespace vcs_test_all_13_ListView6_Rename_Files
{
    public partial class Form1 : Form
    {
        string dirname = @"C:\______test_files\_case1";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int start_index = 8;
            string base_name = "ims_file";

            listView1.Items.Clear();

            string[] filenames = Directory.GetFiles(dirname);
            if (filenames.Length == 0)
                return;

            Array.Sort(filenames);

            string format = "{0:D2}";
            List<string> old_names = new List<string>();

            foreach (string filename in filenames)
            {
                string old_name = Path.GetFileName(filename);
                old_names.Add(old_name);
                ListViewItem item = listView1.Items.Add(old_name);
                richTextBox1.Text += "old = " + old_name + "\t\t";

                string new_name = base_name + string.Format(format, start_index) + Path.GetExtension(filename);
                richTextBox1.Text += "new = " + new_name + "\n";

                if (old_names.Contains(new_name))
                {
                    MessageBox.Show("Name " + new_name + " is already in use.");
                    break;
                }

                item.SubItems.Add(new_name);
                start_index++;
            }

            //listView 自動欄寬
            listView1.Columns[0].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
            listView1.Columns[1].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            foreach (ListViewItem item in listView1.Items)
            {
                string old_name = Path.Combine(dirname, item.Text);
                string new_name = Path.Combine(dirname, item.SubItems[1].Text);
                //File.Move(old_name, new_name);    //not really rename
            }
            int num_files = listView1.Items.Count;
            richTextBox1.Text += "總共改名" + num_files.ToString() + "個檔案\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
