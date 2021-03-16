using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyNotepad1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup_menu_strip();
        }

        void setup_menu_strip()
        {
            richTextBox1.Text += "程式啟動時 動態增加MenuStrip內容\n";

            //檔案(F)
            ToolStripMenuItem item1_1 = new ToolStripMenuItem("新增檔案");
            //ToolStripMenuItem item1_1 = new ToolStripMenuItem("新增檔案", Properties.Resources.new);	若有圖示
            item1_1.Name = "menuFileItem1_1";
            item1_1.ShortcutKeys = (Keys.D1 | Keys.Control); // Ctrl+1
            item1_1.Click += menuFileItem1_1_Click;
            toolStripMenuItem_File.DropDownItems.Add(item1_1);

            ToolStripMenuItem item1_2 = new ToolStripMenuItem("開啟檔案");
            item1_2.Name = "menuFileItem1_2";
            item1_2.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+2
            item1_2.Click += menuFileItem1_2_Click;
            toolStripMenuItem_File.DropDownItems.Add(item1_2);

            ToolStripMenuItem item1_3 = new ToolStripMenuItem("儲存檔案");
            item1_3.Name = "menuFileItem1_3";
            item1_3.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+3
            item1_3.Click += menuFileItem1_3_Click;
            toolStripMenuItem_File.DropDownItems.Add(item1_3);

            ToolStripMenuItem item1_4 = new ToolStripMenuItem("另存新檔");
            item1_4.Name = "menuFileItem1_4";
            item1_4.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+4
            item1_4.Click += menuFileItem1_4_Click;
            toolStripMenuItem_File.DropDownItems.Add(item1_4);

            ToolStripMenuItem item1_5 = new ToolStripMenuItem("結束");
            item1_5.Name = "menuFileItem1_5";
            item1_5.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+X
            item1_5.Click += menuFileItem1_5_Click;
            toolStripMenuItem_File.DropDownItems.Add(item1_5);

            //編輯(E)
            ToolStripMenuItem item2_1 = new ToolStripMenuItem("復原");
            item2_1.Name = "menuFileItem2_1";
            item2_1.ShortcutKeys = (Keys.D1 | Keys.Control); // Ctrl+1
            item2_1.Click += menuFileItem2_1_Click;
            toolStripMenuItem_Edit.DropDownItems.Add(item2_1);

            ToolStripMenuItem item2_2 = new ToolStripMenuItem("複製");
            item2_2.Name = "menuFileItem2_2";
            item2_2.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+2
            item2_2.Click += menuFileItem2_2_Click;
            toolStripMenuItem_Edit.DropDownItems.Add(item2_2);

            ToolStripMenuItem item2_3 = new ToolStripMenuItem("剪下");
            item2_3.Name = "menuFileItem2_3";
            item2_3.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+3
            item2_3.Click += menuFileItem2_3_Click;
            toolStripMenuItem_Edit.DropDownItems.Add(item2_3);

            ToolStripMenuItem item2_4 = new ToolStripMenuItem("貼上");
            item2_4.Name = "menuFileItem2_4";
            item2_4.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+4
            item2_4.Click += menuFileItem2_4_Click;
            toolStripMenuItem_Edit.DropDownItems.Add(item2_4);

            ToolStripMenuItem item2_5 = new ToolStripMenuItem("全選");
            item2_5.Name = "menuFileItem2_5";
            item2_5.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+X
            item2_5.Click += menuFileItem2_5_Click;
            toolStripMenuItem_Edit.DropDownItems.Add(item2_5);

            //設定(T)
            ToolStripMenuItem item3_1 = new ToolStripMenuItem("字型");
            item3_1.Name = "menuFileItem3_1";
            item3_1.ShortcutKeys = (Keys.D1 | Keys.Control); // Ctrl+1
            item3_1.Click += menuFileItem3_1_Click;
            toolStripMenuItem_Option.DropDownItems.Add(item3_1);

            ToolStripMenuItem item3_2 = new ToolStripMenuItem("顏色");
            item3_2.Name = "menuFileItem3_2";
            item3_2.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+2
            item3_2.Click += menuFileItem3_2_Click;
            toolStripMenuItem_Option.DropDownItems.Add(item3_2);

            //關於(A)
            ToolStripMenuItem item4_1 = new ToolStripMenuItem("關於");
            item4_1.Name = "menuFileItem4_1";
            item4_1.ShortcutKeys = (Keys.D1 | Keys.Control); // Ctrl+1
            item4_1.Click += menuFileItem4_1_Click;
            toolStripMenuItem_About.DropDownItems.Add(item4_1);
        }

        private void menuFileItem1_1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem1_1 檔案/新增檔案\n";
        }

        private void menuFileItem1_2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem1_2 檔案/開啟檔案\n";
        }

        private void menuFileItem1_3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem1_3 檔案/儲存檔案\n";
        }

        private void menuFileItem1_4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem1_4 檔案/另存新檔\n";
        }

        private void menuFileItem1_5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem1_5 檔案/結束\n";
        }

        private void menuFileItem2_1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem2_1 編輯/還原\n";
        }

        private void menuFileItem2_2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem2_2 編輯/複製\n";
        }

        private void menuFileItem2_3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem2_3 編輯/剪下\n";
        }

        private void menuFileItem2_4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem2_4 編輯/貼上\n";
        }

        private void menuFileItem2_5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem2_5 編輯/全選\n";
        }

        private void menuFileItem3_1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem3_1 設定/字型\n";
        }

        private void menuFileItem3_2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem3_2 設定/顏色\n";
        }

        private void menuFileItem4_1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 menuFileItem4_1 關於/關於\n";
        }
    }
}
