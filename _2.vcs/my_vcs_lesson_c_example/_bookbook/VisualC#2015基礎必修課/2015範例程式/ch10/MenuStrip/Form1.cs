using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MenuStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "寬容別人, 豁達自已";
            label1.ForeColor = Color.Red;           //設前景色為紅色
            label1.Font = new Font("細明體", 16, FontStyle.Bold);
            粗體ToolStripMenuItem.Checked = true;   //預設粗體項目被勾選
        }

        private void 細明體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //設字型為細明體、大小為16、原字型樣式
            label1.Font = new Font("細明體", 16, label1.Font.Style);
        }

        private void 新細明體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label1.Font = new Font("新細明體", 16, label1.Font.Style);
        }

        private void 標楷體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label1.Font = new Font("標楷體", 16, label1.Font.Style);
        }

        private void 粗體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label1.Font = new Font(label1.Font, label1.Font.Style ^ FontStyle.Bold);
            粗體ToolStripMenuItem.Checked = !(粗體ToolStripMenuItem.Checked);
        }

        private void 斜體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label1.Font = new Font(label1.Font, label1.Font.Style ^ FontStyle.Italic);
            斜體ToolStripMenuItem.Checked = !(斜體ToolStripMenuItem.Checked);
        }

        private void 加底線ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label1.Font = new Font(label1.Font, label1.Font.Style ^ FontStyle.Underline);
            加底線ToolStripMenuItem.Checked = !(加底線ToolStripMenuItem.Checked);
        }
    }
}
