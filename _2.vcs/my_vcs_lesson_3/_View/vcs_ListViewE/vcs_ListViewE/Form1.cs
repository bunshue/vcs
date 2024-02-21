using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewE
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            CreateMyListView();
        }

        private void CreateMyListView()
        {
            // Create a new ListView control.
            ListView listView1 = new ListView();
            listView1.Bounds = new Rectangle(new Point(10, 10), new Size(600, 400));

            // Set the view to show details.
            listView1.View = View.Details;
            // Allow the user to edit item text.
            listView1.LabelEdit = true;
            // Allow the user to rearrange columns.
            listView1.AllowColumnReorder = true;
            // Display check boxes.
            listView1.CheckBoxes = true;
            // Select the item and subitems when selection is made.
            listView1.FullRowSelect = true;
            // Display grid lines.
            listView1.GridLines = true;
            // Sort the items in the list in ascending order.
            listView1.Sorting = SortOrder.Ascending;

            //加入欄資料 標題
            // Create columns for the items and subitems.
            // Width of -2 indicates auto-size.
            listView1.Columns.Add("中文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listView1.Columns.Add("代表", 120, HorizontalAlignment.Center);

            //加入列資料
            // Create three items and three sets of subitems for each item.
            ListViewItem item1 = new ListViewItem("鼠", 0);
            // Place a check mark next to the item.
            item1.Checked = true;
            item1.SubItems.Add("mouse");
            item1.SubItems.Add("3");
            item1.SubItems.Add("米老鼠");
            ListViewItem item2 = new ListViewItem("牛", 1);
            item2.SubItems.Add("ox");
            item2.SubItems.Add("48");
            item2.SubItems.Add("班尼牛");
            ListViewItem item3 = new ListViewItem("虎", 0);
            // Place a check mark next to the item.
            item3.Checked = true;
            item3.SubItems.Add("tiger");
            item3.SubItems.Add("33");
            item3.SubItems.Add("跳跳虎");
            ListViewItem item4 = new ListViewItem("兔", 0);
            // Place a check mark next to the item.
            item4.Checked = true;
            item4.SubItems.Add("rabbit");
            item4.SubItems.Add("8");
            item4.SubItems.Add("彼得兔");

            //Add the items to the ListView.
            listView1.Items.AddRange(new ListViewItem[] { item1, item2, item3, item4 });

            // Create two ImageList objects.
            ImageList imageListSmall = new ImageList();
            ImageList imageListLarge = new ImageList();

            // Initialize the ImageList objects with bitmaps.
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic1.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic2.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic4.jpg"));

            //Assign the ImageList objects to the ListView.
            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;

            // Add the ListView to the control collection.
            this.Controls.Add(listView1);
        }
    }
}

