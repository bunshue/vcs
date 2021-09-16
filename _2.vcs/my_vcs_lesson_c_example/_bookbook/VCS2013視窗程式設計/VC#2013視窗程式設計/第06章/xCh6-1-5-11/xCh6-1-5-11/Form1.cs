using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_1_5_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ImageList myImages = new ImageList();
            myImages.Images.Add(new Bitmap(@"c:\user_red32x32.png", true));
            tabControl1.ImageList = myImages;

            tabControl1.TabPages[0].ImageIndex = 0;
            tabControl1.Appearance = TabAppearance.Normal;
            tabControl1.Multiline = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 新增Tab Page
            string title = "興趣 " + (tabControl1.TabCount + 1).ToString();
            TabPage myTabPage = new TabPage(title);

            // 新增3個Check Box
            CheckBox myTabPageCheckBox1 = new CheckBox();
            CheckBox myTabPageCheckBox2 = new CheckBox();
            CheckBox myTabPageCheckBox3 = new CheckBox();

            myTabPageCheckBox1.Location = new Point(32, 20);
            myTabPageCheckBox1.Text = "閱讀";
            myTabPageCheckBox1.Size = new System.Drawing.Size(176, 32);
            myTabPageCheckBox1.TabIndex = 0;
            myTabPageCheckBox1.Checked = true;

            myTabPageCheckBox2.Location = new Point(32, 50);
            myTabPageCheckBox2.Text = "思考";
            myTabPageCheckBox2.Size = new System.Drawing.Size(176, 32);
            myTabPageCheckBox2.TabIndex = 1;
            myTabPageCheckBox2.Visible = true;

            myTabPageCheckBox3.Location = new Point(32, 80);
            myTabPageCheckBox3.Text = "色彩";
            myTabPageCheckBox3.Size = new System.Drawing.Size(176, 32);
            myTabPageCheckBox3.TabIndex = 1;
            myTabPageCheckBox3.Visible = true;

            // 將3個Check Box加入新增的Tab Page
            myTabPage.Controls.Add(myTabPageCheckBox1);
            myTabPage.Controls.Add(myTabPageCheckBox2);
            myTabPage.Controls.Add(myTabPageCheckBox3);

            // 將新增的Tab Page加入TabControl
            tabControl1.TabPages.Add(myTabPage);

            int rows = tabControl1.RowCount;
            label1.Text = "共有  " + rows.ToString() + " 列的Tabs在TabControl1中";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Button tab1Button1 = new Button();
            tab1Button1.Text = "打招呼";
            tab1Button1.Location = new System.Drawing.Point(20, 10);
            tab1Button1.Size = new System.Drawing.Size(60, 20);
            tab1Button1.TabIndex = 0;
            tab1Button1.Click += new
               System.EventHandler(tab1Button1_Click);

            tabControl1.TabPages[0].Controls.Add(tab1Button1);
        }
        private void tab1Button1_Click(Object sender, EventArgs e)
        {
            MessageBox.Show("Hello, Moto");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            tabPage1 = new TabPage("訂單");
            tabPage2 = new TabPage("明細");
            TabPage[] myPages = new TabPage[] { tabPage1, tabPage2 };
            tabControl1.TabPages.AddRange(myPages);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            tabPage1 = new TabPage("庫存");
            tabPage2 = new TabPage("缺貨");
            tabControl1.Controls.AddRange(
              new Control[] {
                tabPage1,
                tabPage2
                }
            );
        }

        private void tabControl1_Selected(object sender, TabControlEventArgs e)
        {
            StringBuilder msg = new System.Text.StringBuilder();
            msg.AppendFormat("{0} 是 {1}", "TabPage", e.TabPage);
            msg.AppendLine();
            msg.AppendFormat("{0} 是 {1}", "TabPageIndex", e.TabPageIndex);
            msg.AppendLine();
            msg.AppendFormat("{0} 是 {1}", "Action", e.Action);
            msg.AppendLine();
            MessageBox.Show(msg.ToString(), "發生了Selected事件");
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            StringBuilder msg = new System.Text.StringBuilder();
            msg.AppendFormat("{0} 是 {1}", "SelectedIndex", tabControl1.SelectedIndex.ToString());
            msg.AppendLine();
            msg.AppendFormat("{0} 是 {1}", "SelectedTab", tabControl1.SelectedTab.ToString());
            msg.AppendLine();
            MessageBox.Show(msg.ToString(), "發生了SelectedIndexChanged事件");
        }
    }
}
