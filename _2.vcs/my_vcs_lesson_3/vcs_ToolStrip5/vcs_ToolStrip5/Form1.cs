using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolStrip5
{
    public partial class Form1 : Form
    {
        ToolStripButton newToolStripButton;
        ToolStripButton openToolStripButton;
        ToolStripButton saveToolStripButton;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "動態加入 ToolStrip\n";
            richTextBox1.Text += "動態加入 ToolStripItem\n";

            newToolStripButton = new ToolStripButton();
            openToolStripButton = new ToolStripButton();
            saveToolStripButton = new ToolStripButton();

            newToolStripButton.Text = "新增C#檔";
            openToolStripButton.Text = "開啟舊檔";
            saveToolStripButton.Text = "儲存檔案";

            toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] 
            {
               newToolStripButton,
               openToolStripButton,
               saveToolStripButton,
             }
            );

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
