using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;  // for IEnumerator

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
            // 建立Product陣列用來存放產品
            string[] Product = new string[] { "火影忍者", "航海王",
 				"史瑞克4", "葉問2", "鋼鐵人2", "偷心大聖PS男", "阿凡達",
 				"半夜鬼上床", "第一次愛上你", "松藥局的兒子們", "老婆，給我飯" };
            // 將Product陣列的所有選項放入checkedListBox1內
            checkedListBox1.Items.AddRange(Product);
            checkedListBox1.MultiColumn = true;	// 核取清單方塊設為多欄
            checkedListBox1.ColumnWidth = 150; 	// 核取清單方塊欄寬150
            checkedListBox1.CheckOnClick = true; // 只按一下選取

            /*
            checkedListBox1.MultiColumn = true;	// chkListLot水平欄顯示
            checkedListBox1.ColumnWidth = 100;    	// chkListLot水平欄寬
            // 在chkListLot核取清單方塊加入項目, 可讓使用者勾選
            for (int i = 1; i <= 100; i++)
            {
                checkedListBox1.Items.Add(i.ToString());
            }
            */

            /*
            checkedListBox1.Items.AddRange(
                new object[]
                { 
                    "滑鼠",
                    "鍵盤",
                    "網卡",
                    "螢幕",
                    "音效卡",
                    "數據機",
                    "外接硬碟"
                });
            checkedListBox1.MultiColumn = true;
            checkedListBox1.ColumnWidth = 120;
            checkedListBox1.CheckOnClick = true;
            */
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
            //勾選狀態
            string result;
            foreach (int indexChecked in checkedListBox1.CheckedIndices)
            {
                result = "索引 " + indexChecked.ToString() + ", 已被勾選. 勾選的狀態是->" + checkedListBox1.GetItemCheckState(indexChecked).ToString();
                richTextBox1.Text += result + "\n";
            }

            foreach (object itemChecked in checkedListBox1.CheckedItems)
            {
                result = "被勾選的項目是\"" + itemChecked.ToString() + "\"勾選的狀態是->" + checkedListBox1.GetItemCheckState(checkedListBox1.Items.IndexOf(itemChecked)).ToString();
                richTextBox1.Text += result + "\n";
            }

            //3030

            richTextBox1.Text += "訂購產品如下\n";
            // 逐一檢查每一個核取方塊是否被選取
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                // 若第i個核取方塊被選取，即將該產品顯示在textBox1
                if (checkedListBox1.GetItemChecked(i))
                {
                    richTextBox1.Text += "　．" + checkedListBox1.Items[i].ToString() + "\n";
                }
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取消勾選
            IEnumerator myEnumerator;
            myEnumerator = checkedListBox1.CheckedIndices.GetEnumerator();
            while (myEnumerator.MoveNext() != false)
            {
                int y = (int)myEnumerator.Current;
                checkedListBox1.SetItemChecked(y, false);
            }

            //3030

            // 設定所有核取方塊不勾選
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, false);
            }
        }
    }
}
