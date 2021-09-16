using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_1_11
{
    public partial class Form1 : Form
    {
        private TextBox textBox1;
        private Button button1;
        private ToolStrip toolStrip1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 為ToolStrip物件新增內容
            toolStrip1 = new ToolStrip();
            toolStrip1.Items.Add("複製");
            toolStrip1.Items.Add("剪下");
            toolStrip1.Items.Add("貼上");

            textBox1 = new TextBox();
            textBox1.Location = new Point(10, 20);
            textBox1.Size = new Size(200, 20);
            textBox1.Text = "動態建構的TextBox";

            button1 = new Button();
            button1.Text = "隱藏TopToolStripPanel";
            button1.Location = new Point(210, 20);
            button1.Click += new EventHandler(button1_Click);
            toolStripContainer1.ContentPanel.Controls.Add(textBox1);
            toolStripContainer1.ContentPanel.Controls.Add(button1);

            // 將ToolStrip加入ToolStripContainer物件
            toolStripContainer1.TopToolStripPanel.Controls.Add(toolStrip1);
            toolStripContainer1.Dock = DockStyle.Fill;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (toolStripContainer1.TopToolStripPanel.Visible == true)
            {
                toolStripContainer1.TopToolStripPanel.Visible = false;
                button1.Text = "顯現TopToolStripPanel";
            }
            else
            {
                toolStripContainer1.TopToolStripPanel.Visible = true;
                button1.Text = "隱藏TopToolStripPanel";
            }
        }
    }
}
