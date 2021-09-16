using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace xCh5_1_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 新增ListBox物件的選項
            checkedListBox1.Items.AddRange(
                 new object[] { 
                    "滑鼠", 
                    "鍵盤", 
                    "網卡", 
                    "螢幕", 
                    "音效卡", 
                    "數據機", 
                    "外接硬碟"                   
                });
            checkedListBox1.MultiColumn = true;
            checkedListBox1.ColumnWidth = 80;
            checkedListBox1.CheckOnClick = true;

            button1.Text = "勾選狀態";
            button2.Text = "取消勾選";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string result;
            foreach (int indexChecked in checkedListBox1.CheckedIndices)
            {
                result = "索引 " + indexChecked.ToString() + ", 已被勾選. 勾選的狀態是->" +
                                checkedListBox1.GetItemCheckState(indexChecked).ToString();
                textBox1.AppendText(result + '\n');
            }

            foreach (object itemChecked in checkedListBox1.CheckedItems)
            {
                result = "被勾選的項目是\"" +
                    itemChecked.ToString() + 
                    "\"勾選的狀態是->" +
                    checkedListBox1.GetItemCheckState(
                        checkedListBox1.Items.IndexOf(itemChecked)
                    ).ToString();

                textBox1.AppendText(result + '\n');
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            IEnumerator myEnumerator;
            myEnumerator = checkedListBox1.CheckedIndices.GetEnumerator();
            int y;
            while (myEnumerator.MoveNext() != false)
            {
                y = (int)myEnumerator.Current;
                checkedListBox1.SetItemChecked(y, false);
            }

            textBox1.Clear();
        }
    }
}
