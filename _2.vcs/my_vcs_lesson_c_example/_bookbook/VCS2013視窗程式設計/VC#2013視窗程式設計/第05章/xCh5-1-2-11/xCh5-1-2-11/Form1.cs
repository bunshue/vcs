using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            // 設定可以選取多重項目，且使用者可以用 
            // SHIFT、CTRL 和方向鍵進行選取。
            listBox1.SelectionMode = SelectionMode.MultiExtended;

            // 新增ListBox物件的選項
            listBox1.Items.AddRange(
                new object[] { 
                    "滑鼠", 
                    "鍵盤", 
                    "網卡", 
                    "螢幕", 
                    "音效卡" 
                });
        }

        // 新增按鈕
        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add(textBox1.Text);
            textBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 如果沒有指定要插入的位置，就插入到最後一筆
            // 如果有指定位置，就插到指定位置
            if (textBox3.Text == "")
                listBox1.Items.Insert(listBox1.Items.Count, textBox1.Text);
            else
            {
                int ndx = Convert.ToInt32(textBox3.Text);
                listBox1.Items.Insert(ndx, textBox1.Text);
            }
            textBox1.Clear();
        }

        // 清除按鈕，清除textBox3指定的位置
        // 或者清除使用者在ListBox中挑選的項目
        private void button3_Click(object sender, EventArgs e)
        {
            // textBox3的內容是指定要移除的位置
            // 如果沒有給，表示移除已從ListBox
            // 中挑選的部份；
            // 如果有給，則刪除指定位置的選項
            if (textBox3.Text == "")
                listBox1.ClearSelected();
            else
            {
                int ndx = Convert.ToInt32(textBox3.Text);
                listBox1.Items.RemoveAt(ndx);
            }
        }

        // 清空所有的選項
        private void button4_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        // 雀屏中選按鈕，並將結果寫到textBox2
        private void button5_Click(object sender, EventArgs e)
        {
            textBox2.Clear();
            int ndx;
            System.Collections.IEnumerator myEnumerator = 
                listBox1.SelectedIndices.GetEnumerator();
            while (myEnumerator.MoveNext())
            {
                object obj = myEnumerator.Current;
                ndx = (int)obj;
                textBox2.AppendText(listBox1.Items[ndx].ToString() + '\n');
            }
        }

        // 查詢按鈕，使用textBox1的內容進行查詢
        private void button6_Click(object sender, EventArgs e)
        {
            string searchString = textBox1.Text;
            // 查詢ListBox的選項中，是否存在待搜尋的字串
            int index = listBox1.FindString(searchString);

            // 如果找不到，其傳回值為-1
            if (index != -1)
                listBox1.SetSelected(index, true);
            else
                MessageBox.Show("目前的ListBox中並沒有要查尋的「" + searchString + "」");
        }

        // 使用者於ListBox中的選項挑選時引發
        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label1.Text = "目前位置：" + listBox1.SelectedIndex + "/" +
                 listBox1.Items.Count;

            textBox2.AppendText(Environment.NewLine + listBox1.SelectedItem.ToString());
        }
    }
}
