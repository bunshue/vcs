using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CheckedListBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            checkedListBox1.MultiColumn = true;	// chkListLot水平欄顯示
            checkedListBox1.ColumnWidth = 100;    	// chkListLot水平欄寬
            // 在chkListLot核取清單方塊加入項目, 可讓使用者勾選
            for (int i = 1; i <= 100; i++)
            {
                checkedListBox1.Items.Add(i.ToString());
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //全選


            //全不選



            //Info

            // 宣告 count變數，用來記錄使用者勾選大樂透幾個號碼
            int count = 0;
            // 使用for 迴圈記錄目前共勾選幾個號碼
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    richTextBox1.Text += "你選擇了 : " + checkedListBox1.GetItemChecked(i).ToString() + "\n";
                    count++;
                }
            }

            // 將使用者在chkListLot所選號碼逐一指定給myNumStr字串變數
            // 以便將來和大樂透號碼pcNumStr字串比對
            string myNumStr = string.Empty;
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    myNumStr += checkedListBox1.Items[i].ToString() + ", ";
                }
            }

            richTextBox1.Text += "myNumStr = " + myNumStr + "\n";




        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
