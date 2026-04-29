using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData5
{
    public partial class Form2 : Form
    {
        public Form2(string strname)
        {
            InitializeComponent();
            this.Text = strname + "表結構";
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            show_item_location();

            // listView1 屬性 的 Modifiers 改成  Public
            listView1.GridLines = true;
            listView1.View = View.Details;

            //設定欄位
            listView1.Columns.Add("英文名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("中文名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 120, HorizontalAlignment.Left);

            pictureBox1.Image = Form1.imgPhoto;
            this.Text = "圖片檔案 : " + Form1.filename;
        }

        private void show_item_location()
        {
            listView1.Size = new Size(460, 440);
            listView1.Location = new Point(10, 10);

            pictureBox1.Size = new Size(310, 440);
            pictureBox1.Location = new Point(10 + 460 + 10, 10);

            this.Size = new Size(830, 500);
            this.Text = "vcs_FormSendData5 2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(100+710, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }
    }
}
