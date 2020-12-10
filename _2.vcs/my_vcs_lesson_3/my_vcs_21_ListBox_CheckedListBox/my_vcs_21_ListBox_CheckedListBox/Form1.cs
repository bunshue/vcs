using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_21_ListBox_CheckedListBox
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
            string[] itemStr = { "ListBox項目1", "ListBox項目2", "ListBox項目3", "ListBox項目4", "ListBox項目5", "ListBox項目6", "ListBox項目7", "ListBox項目8", "ListBox項目9" };
            foreach (string str in itemStr)
                listBox1.Items.Add(str);

            listBox1.SelectedIndex = 3;

            label1.Text = "第四項是：" + listBox1.SelectedItem;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(textBox1.Text.Length >0)
                listBox1.Items.Add(textBox1.Text);
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //把選到的項目顯示到textBox裡面。
        }

        private void button3_Click(object sender, EventArgs e)
        {
            checkedListBox1.Items.Add("Alpha");
            checkedListBox1.Items.Add("Bravo");
            checkedListBox1.Items.Add("Charlie");
            checkedListBox1.Items.Add("Delta");
            checkedListBox1.Items.Add("Echo");
            checkedListBox1.Items.Add("Foxtrot");
            checkedListBox1.Items.Add("Golf");

            // Display the count.
            label2.Text = checkedListBox1.Items.Count + " items, 0 selected";

            // Check items when the user clicks on them.
            checkedListBox1.CheckOnClick = true;
        }

        // Update the display of files checked.
        private void checkedListBox1_ItemCheck(object sender, ItemCheckEventArgs e)
        {
            // Get the current number checked.
            int num_checked = checkedListBox1.CheckedItems.Count;

            // See if the item is being checked or unchecked.
            if ((e.CurrentValue != CheckState.Checked) &&
                (e.NewValue == CheckState.Checked))
                num_checked++;
            if ((e.CurrentValue == CheckState.Checked) &&
                (e.NewValue != CheckState.Checked))
                num_checked--;

            // Display the count.
            label2.Text = checkedListBox1.Items.Count + " items, " + num_checked + " selected";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            richTextBox1.Text += "CheckedListBox Info\n";

            richTextBox1.Text += "checkedListBox1.Items.Count = " + checkedListBox1.Items.Count.ToString() + "\n";
            for (i = 0; i < checkedListBox1.Items.Count; i++)
            {
                richTextBox1.Text += checkedListBox1.Items[i] + "\n";
            }

            richTextBox1.Text += "checkedListBox1.CheckedItems.Count = " + checkedListBox1.CheckedItems.Count.ToString() + "\n";
            for (i = 0; i < checkedListBox1.CheckedItems.Count; i++)
            {
                richTextBox1.Text += checkedListBox1.CheckedItems[i] + "\n";
            }
            //richTextBox1.Text += "CheckedListBox Info\n";
            //richTextBox1.Text += "CheckedListBox Info\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            int i;
            int len = listBox1.Items.Count;
            string[] items = new string[len];
            listBox1.Items.CopyTo(items, 0);    //listBox內容 拷貝 成 字串陣列

            richTextBox1.Text += "共 " + len.ToString() + " 項\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項\t" + items[i] + "\n";
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
