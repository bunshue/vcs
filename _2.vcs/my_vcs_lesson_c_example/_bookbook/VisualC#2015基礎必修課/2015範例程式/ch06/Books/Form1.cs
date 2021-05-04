using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Books
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] books = new string[] { "還是好朋友/作者：橘子", "揮霍/作者：藤井樹",
            "後初戀的道別/作者：穹風", "目送/作者：龍應台","戒不了甜/作者：張曼娟",
            "愛的小動作/作者：鄭華娟","面具之上/作者：許常德", "第二十一頁/作者：李家同", };
            clstBooks.Items.AddRange(books);    //將books陣列加入clstBooks項目
            clstBooks.CheckOnClick = true;  //設clstBooks按一次就勾選
            clstBorrow.CheckOnClick = true; //設clstBorrow按一次就勾選
        }
        //按 借書 鈕時
        private void btnBorrow_Click(object sender, EventArgs e)
        {   //如果clstBooks勾選的項目個數+clstBorrow的項目個數>= 3
            if (clstBooks.CheckedItems.Count + clstBorrow.Items.Count >= 3)
            {   //顯示提示訊息
                MessageBox.Show("最多借兩本書", "注意");
                for (int i = 0; i < clstBooks.Items.Count; i++)
                {   //逐一設項目不勾選
                    clstBooks.SetItemChecked(i, false);
                }
            }
            else   //其餘即勾選項目和借書項目地個數<3
            {   //逐一讀取clstBooks勾選項目的註標值集合
                foreach (int i in clstBooks.CheckedIndices)
                {   //clstBorrow增加勾選的項目
                    clstBorrow.Items.Add(clstBooks.Items[i]);
                    clstBooks.Items.RemoveAt(i);//移除clstBooks勾選的項目
                }
            }
        }
        //按 還書 鈕時
        private void btnReturn_Click(object sender, EventArgs e)
        {   //逐一檢查clstBorrow項目是否被勾選
            for (int i = 0; i < clstBorrow.Items.Count; i++)
            {   //若該項目被勾選
                if (clstBorrow.GetItemChecked(i) == true)
                {   //clstBooks增加勾選的項目
                    clstBooks.Items.Add(clstBorrow.Items[i]);
                    clstBorrow.Items.RemoveAt(i);//移除clstBorrow勾選的項目
                    i--;    //i-1
                }
            }
        }
    }
}
