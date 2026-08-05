using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData1
{
    public partial class Form8_ListView : Form
    {
        public Form8_ListView(string strname)
        {
            InitializeComponent();

            this.Text = "新表單名稱 : " + strname;
        }

        private void Form8_ListView_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            // listView1 屬性 的 Modifiers 改成  Public
            listView1.GridLines = true;
            listView1.View = View.Details;

            //設定欄位
            listView1.Columns.Add("英文名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("中文名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 120, HorizontalAlignment.Left);

            pictureBox1.Image = Form1.imgPhoto;
            //this.Text = "圖片檔案 : " + Form1.filename;
        }

        private void show_item_location()
        {
            listView1.Size = new Size(460, 440);
            listView1.Location = new Point(10, 10);

            pictureBox1.Size = new Size(310, 440);
            pictureBox1.Location = new Point(10 + 460 + 10, 10);

            richTextBox1.Size = new Size(300, 300);
            richTextBox1.Location = new Point(10 + 460 + 10, 460);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(830, 820);
            //this.Text = "vcs_FormSendData1 2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(100 + 710+300, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
