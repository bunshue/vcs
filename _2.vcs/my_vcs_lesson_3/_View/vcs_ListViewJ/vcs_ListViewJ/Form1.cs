using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//引用與文件輸入輸出流有關的命名空間

namespace vcs_ListViewJ
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files1\__pic";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.CheckBoxes = true;//設置listView1的復選框屬性為真
            listView1.View = View.Details;//設置listView1的視圖方式
            listView1.GridLines = true;//設置listView1顯示網格線
            listView1.Columns.Add("文件名稱", 150, HorizontalAlignment.Left);//向listView1中添加「文件名稱」列
            listView1.Columns.Add("創建時間", 200, HorizontalAlignment.Left);//向listView1中添加「創建時間」列

            foreach (String fileName in Directory.GetFiles(foldername)) //循環遍歷指定資料夾的內容
            {
                FileInfo file = new FileInfo(fileName);//定義一個操作文件的實例
                ListViewItem OptionItem = new ListViewItem(file.Name);//定義一個listView選擇項的實例
                OptionItem.SubItems.Add(file.CreationTime.ToString());//向listView控件中添加文件創建時間列
                listView1.Items.Add(OptionItem);//執行添加操作
                richTextBox1.Text += "加入listView : " + file.Name + "\t" + file.CreationTime.ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "全選\n";
            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (tempItem.Checked == false)//如果當前項處於未選中狀態
                {
                    tempItem.Checked = true;//設置當前項為選中狀態
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "清空\n";
            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (tempItem.Checked == true)//如果當前項處於選中狀態
                {
                    tempItem.Checked = false;//設置當前項為未選中狀態
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int len = listView1.Items.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 項\n";
            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                richTextBox1.Text += "項目 : " + tempItem.Text + "\t" + tempItem.SubItems[1].Text + "\t";

                if (tempItem.Checked == true)//如果當前項處於選中狀態
                {
                    richTextBox1.Text += "已選取\n";
                }
                else
                {
                    richTextBox1.Text += "未選取\n";
                }
            }
        }
    }
}
