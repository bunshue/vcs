using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewF
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LoadImageList();
        }

        private void LoadImageList()
        {
            var list = new List<string>();
            list.Add(@"C:\______test_files\_pic\poster_01.jpg");
            list.Add(@"C:\______test_files\_pic\poster_02.jpg");
            list.Add(@"C:\______test_files\_pic\poster_03.jpg");
            list.Add(@"C:\______test_files\_pic\poster_04.jpg");
            list.Add(@"C:\______test_files\_pic\poster_05.jpg");
            list.Add(@"C:\______test_files\_pic\poster_06.jpg");
            list.Add(@"C:\______test_files\_pic\poster_07.jpg");

            ImageList imglist = new ImageList();
            imglist.ImageSize = new Size(200, 200);
            imglist.ColorDepth = ColorDepth.Depth32Bit;
            foreach (var filename in list)
            {
                imglist.Images.Add(Image.FromFile(filename));
            }
            picListView.LargeImageList = imglist;

            for (int i = 0; i < imglist.Images.Count; i++)
            {
                var lvi = new ListViewItem();
                lvi.ImageIndex = 0;
                lvi.Text = "P" + i;
                //lvi.ToolTipText = "P" + i;
                picListView.Items.Add(lvi);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            CreateMyListView();
        }

        private void CreateMyListView()
        {
            // Create a new ListView control.
            ListView listView1 = new ListView();
            listView1.Bounds = new Rectangle(new Point(50, 50), new Size(600, 400));

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

            // Create three items and three sets of subitems for each item.
            ListViewItem item1 = new ListViewItem("item1", 0);
            // Place a check mark next to the item.
            item1.Checked = true;
            item1.SubItems.Add("1");
            item1.SubItems.Add("2");
            item1.SubItems.Add("3");
            ListViewItem item2 = new ListViewItem("item2", 1);
            item2.SubItems.Add("4");
            item2.SubItems.Add("5");
            item2.SubItems.Add("6");
            ListViewItem item3 = new ListViewItem("item3", 0);
            // Place a check mark next to the item.
            item3.Checked = true;
            item3.SubItems.Add("7");
            item3.SubItems.Add("8");
            item3.SubItems.Add("9");

            // Create columns for the items and subitems.
            // Width of -2 indicates auto-size.
            listView1.Columns.Add("Item Column", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("Column 2", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("Column 3", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("Column 4", -2, HorizontalAlignment.Center);

            //Add the items to the ListView.
            listView1.Items.AddRange(new ListViewItem[] { item1, item2, item3 });

            // Create two ImageList objects.
            ImageList imageListSmall = new ImageList();
            ImageList imageListLarge = new ImageList();

            // Initialize the ImageList objects with bitmaps.
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\______test_files\_pic\poster_01.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\______test_files\_pic\poster_02.jpg"));
            imageListLarge.Images.Add(Bitmap.FromFile(@"C:\______test_files\_pic\poster_03.jpg"));
            imageListLarge.Images.Add(Bitmap.FromFile(@"C:\______test_files\_pic\poster_04.jpg"));

            //Assign the ImageList objects to the ListView.
            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;

            // Add the ListView to the control collection.
            this.Controls.Add(listView1);
        }



    }
}
