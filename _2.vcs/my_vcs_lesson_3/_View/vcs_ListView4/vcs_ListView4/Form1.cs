using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true;  // 顯示格線
            listView1.LabelEdit = true;  // 設定listView1的可編輯屬性為真 listView可修改Label
            listView1.LabelEdit = true;  // 允許使用者修改listView的資料
            listView1.MultiSelect = true;// 是否允許多行選擇
            listView1.Scrollable = true;   //需要時候顯示滾動條

            //設定欄位, 欄名, 欄寬, 對齊方式
            listView1.Columns.Add("中文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);

            //加入項目(列資料)
            ListViewItem item1 = listView1.Items.Add("mouse");
            item1.SubItems.Add("米老鼠");
            item1.SubItems.Add("3");

            ListViewItem item2 = listView1.Items.Add("ox");
            item2.SubItems.Add("班尼牛");
            item2.SubItems.Add("48");

            ListViewItem item3 = listView1.Items.Add("tiger");
            item3.SubItems.Add("跳跳虎");
            item3.SubItems.Add("33");

            ListViewItem item4 = listView1.Items.Add("rabbit");
            item4.SubItems.Add("彼得兔");
            item4.SubItems.Add("8");
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void listView1_MouseMove(object sender, MouseEventArgs e)
        {
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null)
            {
                return;
            }
            ListViewItem item = hti.Item;

            label1.Text = "列 : " + item.Index.ToString();
            label2.Text = "欄 : " + item.SubItems.IndexOf(hti.SubItem).ToString();

            ListViewItem.ListViewSubItem subitem = hti.SubItem;
            label3.Text = "內容 : " + subitem.Text.ToString();

            //此列長度
            label4.Text = "列長度 : " + item.SubItems.Count.ToString();

            string mesg = string.Empty;

            for (int i = 0; i < item.SubItems.Count; i++)
            {
                //richTextBox1.Text += item.SubItems[i].Text + " ";
                mesg += item.SubItems[i].Text + " ";
                if (item.SubItems[i] == subitem)
                {
                    //label4.Text = i.ToString();
                    //richTextBox1.Text += i.ToString() + " ";
                }
            }
            //richTextBox1.Text += "\n";

            label5.Text = mesg;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
