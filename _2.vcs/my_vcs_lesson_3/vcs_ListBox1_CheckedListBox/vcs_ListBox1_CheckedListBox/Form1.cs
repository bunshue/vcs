using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ListBox1_CheckedListBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            string[] itemStr = { "ListBox項目1", "ListBox項目2", "ListBox項目3", "ListBox項目4", "ListBox項目5", "ListBox項目6", "ListBox項目7", "ListBox項目8", "ListBox項目9" };
            foreach (string str in itemStr)
            {
                listBox1.Items.Add(str);
            }

            listBox1.SelectedIndex = 3;

            label1.Text = "第四項是：" + listBox1.SelectedItem;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length > 0)
            {
                listBox1.Items.Add(textBox1.Text);
            }
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
            if ((e.CurrentValue != CheckState.Checked) && (e.NewValue == CheckState.Checked))
            {
                num_checked++;
            }
            if ((e.CurrentValue == CheckState.Checked) && (e.NewValue != CheckState.Checked))
            {
                num_checked--;
            }

            // Display the count.
            label2.Text = checkedListBox1.Items.Count + " items, " + num_checked + " selected";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            richTextBox1.Text += "CheckedListBox Info\n";

            richTextBox1.Text += "checkedListBox1 總共有 " + checkedListBox1.Items.Count.ToString() + " 項, 依序是 :\n";
            for (i = 0; i < checkedListBox1.Items.Count; i++)
            {
                richTextBox1.Text += checkedListBox1.Items[i] + "\n";
            }

            richTextBox1.Text += "checkedListBox1 選取 " + checkedListBox1.CheckedItems.Count.ToString() + " 項, 依序是 :\n";
            for (i = 0; i < checkedListBox1.CheckedItems.Count; i++)
            {
                richTextBox1.Text += checkedListBox1.CheckedItems[i] + "\n";
            }
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

        private void button8_Click(object sender, EventArgs e)
        {
            CheckUncheckAll(true);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            CheckUncheckAll(false);
        }

        private void CheckUncheckAll(bool check)
        {
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, check);
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //添加項目不防止閃爍
            AddToMyListBox1();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //添加項目防止閃爍
            //多了BeginUpdate() 和 EndUpdate()

            AddToMyListBox2();
        }

        public void AddToMyListBox1()
        {
            listBox1.Items.Clear();

            for (int x = 1; x < 5000; x++)
            {
                listBox1.Items.Add("listBox項目  " + x.ToString());
            }
        }

        public void AddToMyListBox2()
        {
            listBox1.Items.Clear();
            listBox1.BeginUpdate();

            for (int x = 1; x < 5000; x++)
            {
                listBox1.Items.Add("listBox項目  " + x.ToString());
            }
            listBox1.EndUpdate();
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //文字檔  => listBox
            listBox1.Items.Clear();

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            //按行讀取文件：

            int fileCount = 0;
            StreamReader sr = new StreamReader(filename, Encoding.Default);
            while (sr.Peek() > -1)//StreamReader.Peek()返回下一個可用字符，但不使用它
            {
                listBox1.Items.Add(sr.ReadLine());
                fileCount++;
            }
            sr.Close();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //listBox => 文件檔

            int i;
            int len = listBox1.Items.Count;
            if (len <= 0)
            {
                richTextBox1.Text += "listBox無資料, 不存檔\n";
                return;
            }

            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            //按行寫入文件：

            string[] items = new string[len];
            listBox1.Items.CopyTo(items, 0);    //listBox內容 拷貝 成 字串陣列

            StreamWriter sw = new StreamWriter(filename);
            for (i = 0; i < len; i++)
            {
                sw.WriteLine("第 " + i.ToString() + " 項 :\t" + items[i]);
            }
            sw.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //清除listBox
            listBox1.DataSource = null;
            listBox1.Items.Clear();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //做一個字串陣列 一次賦值給ListBox

            //字串陣列的寫法(一維)：
            String[] weekday = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };

            //清除listBox
            listBox1.DataSource = null;
            listBox1.Items.Clear();

            listBox1.DataSource = weekday;



            // 將Product陣列的所有選項放入checkedListBox1內
            checkedListBox1.Items.AddRange(weekday);



        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }
    }
}
