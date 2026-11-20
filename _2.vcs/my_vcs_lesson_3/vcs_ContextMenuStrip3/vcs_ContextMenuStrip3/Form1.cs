using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//在RichTextBox做右鍵選單, 可以全選複製貼上

namespace vcs_ContextMenuStrip3
{
    public partial class Form1 : Form
    {
        private ContextMenuStrip menu;
        private ToolStripMenuItem miUndo;
        private ToolStripMenuItem miRedo;
        private ToolStripMenuItem miCut;
        private ToolStripMenuItem miCopy;
        private ToolStripMenuItem miPaste;
        private ToolStripMenuItem miSelectAll;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            CreateContextMenu();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void show_item_location()
        {
            richTextBox1.Dock = DockStyle.Fill;
            //richTextBox1.Size = new Size(600, 600);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(600, 600);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void CreateContextMenu()
        {
            menu = new ContextMenuStrip();

            miUndo = new ToolStripMenuItem("復原");
            miRedo = new ToolStripMenuItem("重做");

            miCut = new ToolStripMenuItem("剪下");
            miCopy = new ToolStripMenuItem("複製");
            miPaste = new ToolStripMenuItem("貼上");

            miSelectAll = new ToolStripMenuItem("全選");

            menu.Items.Add(miUndo);
            menu.Items.Add(miRedo);

            menu.Items.Add(new ToolStripSeparator());

            menu.Items.Add(miCut);
            menu.Items.Add(miCopy);
            menu.Items.Add(miPaste);

            menu.Items.Add(new ToolStripSeparator());

            menu.Items.Add(miSelectAll);

            richTextBox1.ContextMenuStrip = menu;  // 直接指定 ContextMenuStrip

            menu.Opening += Menu_Opening;

            miUndo.Click += MiUndo_Click;
            miRedo.Click += MiRedo_Click;

            miCut.Click += MiCut_Click;
            miCopy.Click += MiCopy_Click;
            miPaste.Click += MiPaste_Click;

            miSelectAll.Click += MiSelectAll_Click;
        }

        //Opening 事件
        private void Menu_Opening(object sender, CancelEventArgs e)
        {
            miUndo.Enabled = richTextBox1.CanUndo;
            miRedo.Enabled = richTextBox1.CanRedo;

            bool hasSelection = richTextBox1.SelectionLength > 0;

            miCut.Enabled = hasSelection;
            miCopy.Enabled = hasSelection;

            miPaste.Enabled = Clipboard.ContainsText();
        }

        private void MiUndo_Click(object sender, EventArgs e)
        {
            if (richTextBox1.CanUndo)
            {
                richTextBox1.Undo();
            }
        }

        private void MiRedo_Click(object sender, EventArgs e)
        {
            if (richTextBox1.CanRedo)
            {
                richTextBox1.Redo();
            }
        }

        private void MiCut_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void MiCopy_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void MiPaste_Click(object sender, EventArgs e)
        {
            //richTextBox1.Paste();
            richTextBox1.SelectedText = Clipboard.GetText();  // 強制只取 Unicode 文字

            if (Clipboard.ContainsText())
            {
                //richTextBox1.SelectedText = Clipboard.GetText(TextDataFormat.UnicodeText);  // 強制只取 Unicode 文字
            }
        }

        private void MiSelectAll_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

