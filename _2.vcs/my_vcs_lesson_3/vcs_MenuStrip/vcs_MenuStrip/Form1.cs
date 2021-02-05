using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MenuStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Exit.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Create some tool menu items.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Tool 1 displays a string.
            ToolStripMenuItem tool1 = new ToolStripMenuItem("Tool 1");
            tool1.Name = "mnuToolsTool1";
            tool1.ShortcutKeys = (Keys.D1 | Keys.Control); // Ctrl+1
            tool1.Click += mnuTool1_Click;
            mnuTools.DropDownItems.Add(tool1);

            // Tool 2 displays a string and image.
            ToolStripMenuItem tool2 = new ToolStripMenuItem("Tool 2", Properties.Resources.happy);
            tool2.Name = "mnuToolsTool2";
            tool2.ShortcutKeys = (Keys.D2 | Keys.Control); // Ctrl+2
            tool2.Click += mnuTool2_Click;
            mnuTools.DropDownItems.Add(tool2);

            richTextBox1.Text += "程式啟動時 動態增加MenuStrip內容\n";
        }

        // Execute tool 1.
        private void mnuTool1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 Tool 1\n";
        }

        // Execute tool 2.
        private void mnuTool2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你點選了 Tool 2\n";
        }
    }
}
