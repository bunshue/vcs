using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_5_11
{
    public partial class Form1 : Form
    {
        internal System.Windows.Forms.ListView listView1;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建立ListView 控制項，並指定其位置與大小
            listView1 = new ListView();
            listView1.Bounds = new Rectangle(
                new Point(10, 10),
                new Size(300, 180));

            // 設定檢視模式為「詳細資訊」
            listView1.View = View.Details;
            // Allow the user to edit item text.
            listView1.LabelEdit = true;
            // 是否讓使用者重新排列各欄的位置
            listView1.AllowColumnReorder = true;
            // 是否顯示CheckBox
            listView1.CheckBoxes = true;
            // Select the item and subitems when selection is made.
            listView1.FullRowSelect = true;
            // 是否顯示水平格線
            listView1.GridLines = true;
            // 是否顯示選項的提示文字，使用時需搭配ToolTipText
            listView1.ShowItemToolTips = true;
            // 將選項依升冪排序
            listView1.Sorting = SortOrder.Ascending;

            // 建立大圖示與小圖示所需的ImageList物件
            ImageList imageListSmall = new ImageList();
            ImageList imageListLarge = new ImageList();

            // 加入圖像
            imageListSmall.Images.Add(Bitmap.FromFile("C:\\leela32x32.png"));
            imageListSmall.Images.Add(Bitmap.FromFile("C:\\user32x32.png"));
            imageListSmall.Images.Add(Bitmap.FromFile("C:\\frai32x32.png"));
            imageListLarge.Images.Add(Bitmap.FromFile("C:\\leela48x48.png"));
            imageListLarge.Images.Add(Bitmap.FromFile("C:\\user48x48.png"));
            imageListLarge.Images.Add(Bitmap.FromFile("C:\\frai48x48.png"));

            // 設定圖像的大小分別是32x32及48x48
            imageListSmall.ImageSize = new Size(32, 32);
            imageListLarge.ImageSize = new Size(48, 48);

            // 指定表示大小圖示的ImageList物件
            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;

            // 建立各選項及其附屬選項
            // 選項是使用的是ListViewItem，而非像ListBox使用Items
            // ListViewItem建構式的第一個參數是項目的名稱，
            // 第二個參數是使用圖像的索引位置
            ListViewItem item1 = new ListViewItem("滑鼠", 0);
            // 是否勾選
            item1.Checked = true;
            item1.ToolTipText = "這是USB 3.0規格的喔！ ";
            item1.SubItems.Add("20.8");
            item1.SubItems.Add("2");
            item1.SubItems.Add("嘉義廠");

            ListViewItem item2 = new ListViewItem("網卡", 1);
            item2.ToolTipText = "這是3G+WIFI無線USB行動網路卡喔！ ";
            item2.SubItems.Add("15.9");
            item2.SubItems.Add("5");
            item2.SubItems.Add("屏東廠");

            ListViewItem item3 = new ListViewItem("螢幕", 2);
            // 是否勾選
            item3.Checked = true;
            item3.ToolTipText = "這是27寸的寛螢幕";
            item3.SubItems.Add("12.5");
            item3.SubItems.Add("8");
            item3.SubItems.Add("台中廠");

            // 建立選項及其附屬選項所屬的欄位
            listView1.Columns.Add("選項欄", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("單價", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("庫存", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("倉庫", -2, HorizontalAlignment.Center);

            // 將各選項加入ListView.
            listView1.Items.AddRange(new ListViewItem[] { 
                item1, item2, item3 
            });

            // 設定事件處理程序的delegate
            this.listView1.SelectedIndexChanged +=
                new System.EventHandler(listView1_SelectedIndexChanged);

            this.listView1.ItemChecked += new ItemCheckedEventHandler(listView1_ItemChecked);

            this.listView1.ItemCheck += new ItemCheckEventHandler(listView1_ItemCheck);

            // Add the ListView to the control collection.
            this.Controls.Add(listView1);

            button1.Enabled = false;
        }

        private void listView1_SelectedIndexChanged(object sender, System.EventArgs e)
        {
            textBox1.Clear();
            ListView.SelectedListViewItemCollection selectedItem = listView1.SelectedItems;

            foreach (ListViewItem item in selectedItem)
            {
                textBox1.AppendText(item.Text);
            }
        }

        private void listView1_ItemChecked(Object sender, ItemCheckedEventArgs e)
        {
            textBox2.Clear();
            System.Text.StringBuilder messageBoxCS = new System.Text.StringBuilder();
            messageBoxCS.AppendFormat("{0} = {1}", "Item", e.Item);
            messageBoxCS.AppendLine();
            textBox2.AppendText(messageBoxCS.ToString());
        }

        private void listView1_ItemCheck(object sender, System.Windows.Forms.ItemCheckEventArgs e)
        {
            double price = 0;
            if (e.CurrentValue == CheckState.Unchecked)
            {
                price += Double.Parse(
                    this.listView1.Items[e.Index].SubItems[1].Text);
            }
            else if ((e.CurrentValue == CheckState.Checked))
            {
                price -= Double.Parse(
                    this.listView1.Items[e.Index].SubItems[1].Text);
            }

            if (price > 0)
                textBox3.Text = "選取項目的價格->" + price.ToString();
            else
                textBox3.Text = "取消項目的價格->" + Math.Abs(price).ToString();
        }

        // 以「大圖示」顯示
        private void button2_Click(object sender, EventArgs e)
        {
            listView1.View = View.LargeIcon;
        }

        // 以「小圖示」顯示
        private void button3_Click(object sender, EventArgs e)
        {
            listView1.View = View.SmallIcon;
        }

        // 以「清單」顯示
        private void button4_Click(object sender, EventArgs e)
        {
            listView1.View = View.List;
        }

        // 以「詳細資訊」顯示
        private void button5_Click(object sender, EventArgs e)
        {
            listView1.View = View.Details;
        }
        
        // 「總價」按鈕，計算所有選取項目的總價
        private void button6_Click(object sender, EventArgs e)
        {
            // ListView控制項的CheckedItems 屬性會傳回集合，
            // 這個集合包含控制項中所有已選取的項目。  
            ListView.CheckedListViewItemCollection checkedItems = listView1.CheckedItems;
            double price = 0;
            ListViewItem x = new ListViewItem();
            System.Collections.IEnumerator myEnumerator = checkedItems.GetEnumerator();
            while (myEnumerator.MoveNext())
            {
                object obj = myEnumerator.Current;
                x = (ListViewItem)obj;
                price += Double.Parse(x.SubItems[1].Text);
            }
            textBox4.Text = "已勾選項目，其總價->" + price.ToString();
        }

    }
}
