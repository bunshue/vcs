using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_11
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
            newToolStripButton = new ToolStripButton();
            openToolStripButton = new ToolStripButton();
            saveToolStripButton = new ToolStripButton();

            newToolStripButton.Text = "新增C#檔";
            openToolStripButton.Text = "開啟舊檔";
            saveToolStripButton.Text = "儲存檔案";

            toolStrip1.Items.AddRange(
                 new System.Windows.Forms.ToolStripItem[] 
            {
               newToolStripButton,
               openToolStripButton,
               saveToolStripButton,
             }
            );
        }
    }
}
