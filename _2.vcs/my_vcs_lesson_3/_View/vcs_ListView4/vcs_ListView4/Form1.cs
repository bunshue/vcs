using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//imageList1屬性/Images/集合/加入圖片

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
            listView_use_imageList.View = View.LargeIcon;//设置显示方式
            listView_use_imageList.LargeImageList = imageList1;//设置ImageList属性

            listView_use_imageList.Items.Add("aaaa", 0);
            listView_use_imageList.Items.Add("bbbb", 1);
            listView_use_imageList.Items.Add("cccc", 2);
            listView_use_imageList.Items.Add("dddd", 3);
            listView_use_imageList.Items.Add("eeee", 4);

        }
    }
}
