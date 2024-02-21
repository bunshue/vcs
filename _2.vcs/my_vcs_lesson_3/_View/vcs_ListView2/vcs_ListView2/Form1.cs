using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//在ListView加入圖片

namespace vcs_ListView2
{
    public partial class Form1 : Form
    {
        ListView listView1 = new ListView();
        RichTextBox richTextBox1 = new RichTextBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            apply_listView();
        }

        void show_item_location()
        {
            listView1.Size = new Size(500, 600);
            listView1.Location = new Point(10, 10);
            this.Controls.Add(listView1);

            richTextBox1.Size = new Size(350, 600);
            richTextBox1.Location = new Point(10 + 500 + 10, 10);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(900, 700);
        }

        void apply_listView()
        {
            var list = new List<string>();
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_01.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_02.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_03.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_04.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_05.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_06.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_07.jpg");

            ImageList imglist = new ImageList();
            imglist.ImageSize = new Size(200, 200);
            imglist.ColorDepth = ColorDepth.Depth32Bit;
            foreach (var filename in list)
            {
                imglist.Images.Add(Image.FromFile(filename));
            }
            listView1.LargeImageList = imglist;

            for (int i = 0; i < imglist.Images.Count; i++)
            {
                var lvi = new ListViewItem();
                lvi.ImageIndex = 0;
                lvi.Text = "第 " + i.ToString() + " 張圖";
                //lvi.ToolTipText = "P" + i;
                listView1.Items.Add(lvi);
            }
        }
    }
}
