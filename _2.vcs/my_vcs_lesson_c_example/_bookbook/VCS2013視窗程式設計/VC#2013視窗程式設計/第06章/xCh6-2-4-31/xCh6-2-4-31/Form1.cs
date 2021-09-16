using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_31
{
    public partial class Form1 : Form
    {
        ToolStripTextBox toolStripTextBox1;
        ToolStripButton toolStripButton1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripTextBox1 = new ToolStripTextBox();
            toolStripTextBox1.Size = new Size(300, 30);
            toolStripTextBox1.ToolTipText = "請輸入網址";
            toolStripTextBox1.CharacterCasing = CharacterCasing.Upper;

            toolStripButton1 = new ToolStripButton();
            toolStripButton1.Text = "上網";
            toolStripButton1.ToolTipText = "點選以開啟文字方塊所指的網址";
            toolStripButton1.Image = Image.FromFile(@"c:\frai32x32.png");
            toolStripButton1.DisplayStyle = ToolStripItemDisplayStyle.ImageAndText;
            toolStripButton1.Click += new EventHandler(toolStripButton1_Click);

            toolStrip1.Items.Add(toolStripTextBox1);
            toolStrip1.Items.Add(toolStripButton1);
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("IEXPLORE.EXE",toolStripTextBox1.Text);
        }
 
    }
}
