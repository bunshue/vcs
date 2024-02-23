using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//方案總管/右鍵/加入/現有項目, 選擇ListViewEx.cs
//編譯後, 工具箱出現ListViewEx控件

namespace vcs_ListViewEx2
{
    public partial class Form1 : Form
    {
        ListViewEx listViewEx1 = new ListViewEx();
        RichTextBox richTextBox1 = new RichTextBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            apply_listView0();
        }

        void show_item_location()
        {
            listViewEx1.Size = new Size(500, 600);
            listViewEx1.Location = new Point(10, 10);
            this.Controls.Add(listViewEx1);

            richTextBox1.Size = new Size(350, 600);
            richTextBox1.Location = new Point(10 + 500 + 10, 10);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(900, 700);
        }

        void apply_listView0()
        {
            /*
            richTextBox1.Text += "目前listView1共有 " + listView1.Items.Count.ToString() + " 個項目\n";
            foreach (ListViewItem i in listView1.Items)
            {
                int cnt = 123;
                i.SubItems.Add(cnt.ToString());
                //cnt = 234;
                //i.SubItems.Add(cnt.ToString());
            }

            ListViewItem i1 = new ListViewItem("aaaaa");
            i1.UseItemStyleForSubItems = false;

            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1d = new ListViewItem.ListViewSubItem();

            sub_i1a.Text = "111";
            i1.SubItems.Add(sub_i1a);
            sub_i1b.Text = total_page.ToString();
            i1.SubItems.Add(sub_i1b);
            sub_i1c.Text = file_size;
            i1.SubItems.Add(sub_i1c);
            sub_i1d.Text = long_foldername;
            i1.SubItems.Add(sub_i1d);

            sub_i1a.ForeColor = Color.Blue;
            sub_i1b.ForeColor = Color.Blue;
            sub_i1c.ForeColor = Color.Blue;
            sub_i1d.ForeColor = Color.Blue;
            sub_i1a.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1b.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1c.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1d.Font = new Font("Times New Roman", 12, FontStyle.Bold);

            listView1.Items.Add(i1);

            Button btn0 = new Button();
            btn0.Text = "";
            btn0.BackColor = SystemColors.Control;
            btn0.Font = this.Font;
            btn0.Click += new EventHandler(btn_Click);
            listView1.AddEmbeddedControl(btn0, 2, 0);
            */


            //基本設定
            //this.listViewEx1.AllowColumnReorder = true;
            this.listViewEx1.FullRowSelect = true;
            this.listViewEx1.View = View.Details;
            this.listViewEx1.Font = new Font("Microsoft Sans Serif", 12.75F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(0)));

            //設定欄位
            listViewEx1.Columns.Add("中文名", 80, HorizontalAlignment.Left);
            listViewEx1.Columns.Add("英文名", 80, HorizontalAlignment.Left);
            listViewEx1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listViewEx1.Columns.Add("取消", 60, HorizontalAlignment.Left);
            listViewEx1.Columns.Add("代表人物", 100, HorizontalAlignment.Left);

            //加入項目
            ListViewItem listViewItem1 = new ListViewItem("鼠");
            listViewItem1.SubItems.Add("mouse");
            listViewItem1.SubItems.Add("3");
            listViewEx1.Items.Add(listViewItem1);

            ListViewItem listViewItem2 = new ListViewItem("牛");
            listViewItem2.SubItems.Add("ox");
            listViewItem2.SubItems.Add("48");
            listViewEx1.Items.Add(listViewItem2);

            ListViewItem listViewItem3 = new ListViewItem("虎");
            listViewItem3.SubItems.Add("tiger");
            listViewItem3.SubItems.Add("33");
            listViewEx1.Items.Add(listViewItem3);

            ListViewItem listViewItem4 = new ListViewItem("兔");
            listViewItem4.SubItems.Add("rabbit");
            listViewItem4.SubItems.Add("8");
            listViewEx1.Items.Add(listViewItem4);

            ListViewItem listViewItem5 = new ListViewItem("龍");
            listViewItem5.SubItems.Add("dragon");
            listViewItem5.SubItems.Add("38");
            listViewEx1.Items.Add(listViewItem5);

            //製作lsitview內的按鈕
            Button btn0 = new Button();
            btn0.Name = "btn0";
            btn0.Text = "";
            btn0.BackgroundImage = vcs_ListViewEx2.Properties.Resources.x;
            btn0.BackgroundImageLayout = ImageLayout.Zoom;
            btn0.BackColor = SystemColors.Control;
            //btn0.Size = new Size(30, 30); 目前設定大小還不行
            btn0.Font = this.Font;
            btn0.Click += new EventHandler(btn_Click);
            listViewEx1.AddEmbeddedControl(btn0, 3, 0);

            Button btn1 = new Button();
            btn1.Name = "btn1";
            btn1.Text = "";
            btn1.BackgroundImage = vcs_ListViewEx2.Properties.Resources.x;
            btn1.BackgroundImageLayout = ImageLayout.Zoom;
            btn1.BackColor = SystemColors.Control;
            //btn1.Size = new Size(30, 30); 目前設定大小還不行
            btn1.Font = this.Font;
            btn1.Click += new EventHandler(btn_Click);
            listViewEx1.AddEmbeddedControl(btn1, 3, 1);

            Button btn2 = new Button();
            btn2.Name = "btn2";
            btn2.Text = "";
            btn2.BackgroundImage = vcs_ListViewEx2.Properties.Resources.x;
            btn2.BackgroundImageLayout = ImageLayout.Zoom;
            btn2.BackColor = SystemColors.Control;
            btn2.Font = this.Font;
            btn2.Click += new EventHandler(btn_Click);
            listViewEx1.AddEmbeddedControl(btn2, 3, 2);

            Button btn3 = new Button();
            btn3.Name = "btn3";
            btn3.Text = "";
            btn3.BackgroundImage = vcs_ListViewEx2.Properties.Resources.x;
            btn3.BackgroundImageLayout = ImageLayout.Zoom;
            btn3.BackColor = SystemColors.Control;
            btn3.Font = this.Font;
            btn3.Click += new EventHandler(btn_Click);
            listViewEx1.AddEmbeddedControl(btn3, 3, 3);

            RichTextBox rtb0 = new RichTextBox();
            rtb0.ScrollBars = RichTextBoxScrollBars.None;
            rtb0.BorderStyle = BorderStyle.None;
            rtb0.WordWrap = false;
            rtb0.BackColor = Color.White;
            rtb0.Cursor = Cursors.Default;
            rtb0.Text = "米老鼠";
            listViewEx1.AddEmbeddedControl(rtb0, 4, 0);

            RichTextBox rtb1 = new RichTextBox();
            rtb1.ScrollBars = RichTextBoxScrollBars.None;
            rtb1.BorderStyle = BorderStyle.None;
            rtb1.WordWrap = false;
            rtb1.BackColor = Color.White;
            rtb1.Cursor = Cursors.Default;
            rtb1.Text = "班尼牛";
            listViewEx1.AddEmbeddedControl(rtb1, 4, 1);

            RichTextBox rtb2 = new RichTextBox();
            rtb2.ScrollBars = RichTextBoxScrollBars.None;
            rtb2.BorderStyle = BorderStyle.None;
            rtb2.WordWrap = false;
            rtb2.BackColor = Color.White;
            rtb2.Cursor = Cursors.Default;
            rtb2.Text = "跳跳虎";
            listViewEx1.AddEmbeddedControl(rtb2, 4, 2);

            //加入唯讀之RTB
            ReadOnlyRichTextBox rtb = new ReadOnlyRichTextBox();
            rtb.ScrollBars = RichTextBoxScrollBars.None;
            rtb.BorderStyle = BorderStyle.None;
            rtb.WordWrap = false;
            rtb.BackColor = Color.White;
            rtb.Cursor = Cursors.Default;
            rtb.Text = "逗逗龍(唯讀)";
            listViewEx1.AddEmbeddedControl(rtb, 4, 4);
        }

        private void btn_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ((Button)sender).Name + "\n";

            int cnt = listViewEx1.SelectedItems.Count;
            richTextBox1.Text += cnt.ToString() + "\n";
            if (cnt > 0)
            {
                int selNdx = listViewEx1.SelectedIndices[0];
                listViewEx1.Items[selNdx].Selected = true;    //選到的項目
                richTextBox1.Text += "你選了 " + selNdx.ToString() + "\n";


            }



            //richTextBox1.Text += listViewEx1.SelectedIndices[0].ToString() + "\n";
        }
    }
}
