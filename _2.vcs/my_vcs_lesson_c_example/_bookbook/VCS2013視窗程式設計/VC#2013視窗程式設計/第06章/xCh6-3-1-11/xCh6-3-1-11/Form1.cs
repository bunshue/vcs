using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_3_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 設定Form為MDI容器
            this.IsMdiContainer = true;

            // 動態建構「視窗」功能選項，會列出目前已開啟的表單數
            ToolStripMenuItem windowsMenu = new ToolStripMenuItem("視窗");

            // 取消ToolStripMenuItem 的左邊緣顯示影像的空間
            // 留下左邊緣顯示核取記號的空間，以供辨識目前有焦點的新Form為何
            ((ToolStripDropDownMenu)(windowsMenu.DropDown)).ShowImageMargin = false;
            ((ToolStripDropDownMenu)(windowsMenu.DropDown)).ShowCheckMargin = true;

            // 設定顯示多重文件介面 (MDI) 子表單的清單
            menuStrip1.MdiWindowListItem = windowsMenu;

            // 將動態建構的ToolStripMenuItem加入到MenuStrip
            menuStrip1.Items.Add(windowsMenu);

            toolStripComboBox1.Items.AddRange(new object[] { "紅色", "藍色", "綠色" });
            toolStripComboBox2.Items.AddRange(new object[] { "9", "10", "12", "14" });
            toolStripComboBox1.Text = toolStripComboBox1.Items[0].ToString();
            toolStripComboBox2.Text = toolStripComboBox2.Items[0].ToString();

            // 重設功能表單TextBox的尺寸與文字內容
            toolStripTextBox1.Size = new Size(125, 20);
            toolStripTextBox1.BackColor = Color.DarkGray;
            toolStripTextBox1.Text = "目前已開啟 " + this.MdiChildren.Length.ToString() + " 個表單";
        }

        private void 開新檔案ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form frm = new Form();
            frm.MdiParent = this;
            frm.Text = "Form - " + this.MdiChildren.Length.ToString();
            frm.Show();

            // 重設功能表單TextBox的文字內容
            toolStripTextBox1.Size = new Size(125, 20);
            toolStripTextBox1.Text = "目前已開啟 " +
                this.MdiChildren.Length.ToString() + 
                " 個表單";
        }
    }
}
