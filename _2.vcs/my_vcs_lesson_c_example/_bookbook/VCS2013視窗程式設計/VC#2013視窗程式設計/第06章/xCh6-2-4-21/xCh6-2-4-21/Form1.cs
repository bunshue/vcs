using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_21
{
    public partial class Form1 : Form
    {
        ToolStripLabel toolStripLabel1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripLabel1 = new ToolStripLabel();
            toolStripLabel1.Text = "MSDN文件庫";
            toolStripLabel1.IsLink = true;
            toolStripLabel1.ToolTipText = "點選以開啟線上MSDN文件庫";
            toolStripLabel1.Tag = "http://msdn.microsoft.com/zh-TW/";
            toolStripLabel1.Click += new EventHandler(toolStripLabel1_Click);

            toolStrip1.Items.Add(toolStripLabel1);
        }

        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            ToolStripLabel toolStripLabel1 = (ToolStripLabel)sender;

            // 從tag屬性中取出網址
            System.Diagnostics.Process.Start(
                "IEXPLORE.EXE",
                toolStripLabel1.Tag.ToString()
             );

            // 設定已瀏覽
            toolStripLabel1.LinkVisited = true;
        }
    }
}
