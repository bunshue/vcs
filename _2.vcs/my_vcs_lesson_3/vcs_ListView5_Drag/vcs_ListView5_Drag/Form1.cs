using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView5_Drag
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void listView1_ItemDrag(object sender, ItemDragEventArgs e)
        {
            //起動拖放放操作，設置拖放類型
            listView1.DoDragDrop(listView1.SelectedItems, DragDropEffects.Move);
        }
        //選擇要拖動的項
        private void listView1_DragEnter(object sender, DragEventArgs e)
        {
            //獲取ListView類型數據
            for (int i = 0; i <= e.Data.GetFormats().Length - 1; i++)
            {
                if (e.Data.GetFormats()[i].Equals("System.Windows.Forms.ListView+SelectedListViewItemCollection"))
                {
                    e.Effect = DragDropEffects.Move;
                }
            }
        }
        private void listView1_DragDrop(object sender, DragEventArgs e)
        {
            //判斷是否選擇拖放的項
            if (listView1.SelectedItems.Count == 0)
            {
                return;
            }
            //定義項的坐標點
            Point cp = listView1.PointToClient(new Point(e.X, e.Y));
            ListViewItem dragToItem = listView1.GetItemAt(cp.X, cp.Y);
            if (dragToItem == null)
            {
                return;
            }
            int dragIndex = dragToItem.Index;
            ListViewItem[] sel = new ListViewItem[listView1.SelectedItems.Count];
            for (int i = 0; i <= listView1.SelectedItems.Count - 1; i++)
            {
                sel[i] = listView1.SelectedItems[i];
            }
            for (int i = 0; i < sel.GetLength(0); i++)
            {
                ListViewItem dragItem = sel[i];
                int itemIndex = dragIndex;
                if (itemIndex == dragItem.Index)
                {
                    return;
                }
                if (dragItem.Index < itemIndex)
                    itemIndex++;
                else
                    itemIndex = dragIndex + i;
                ListViewItem insertItem = (ListViewItem)dragItem.Clone();
                listView1.Items.Insert(itemIndex, insertItem);
                listView1.Items.Remove(dragItem);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}