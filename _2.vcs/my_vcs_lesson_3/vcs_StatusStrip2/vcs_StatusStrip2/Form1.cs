using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StatusStrip2
{
    public partial class Form1 : Form
    {
        StatusStrip statusStrip1 = new StatusStrip();
        ToolStripStatusLabel toolStripStatusLabel1 = new ToolStripStatusLabel();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            #region AddStatusStrip
            //1. 定義要增加的StatusStrip
            //StatusStrip statusStrip1 = new StatusStrip();

            //2. 定義StatusStrip項目中的控件，其中ToolStripLabel是一個相似於label的控件，現在用於顯示文字
            ToolStripLabel toolStripLabel1 = new ToolStripLabel();
            toolStripLabel1.Text = "VCS";   //要顯示的文字內容

            //2. 定義StatusStrip項目中的控件，其中ToolStripStatusLabel是一個相似於label的控件，現在用於顯示文字
            //ToolStripStatusLabel toolStripStatusLabel1 = new ToolStripStatusLabel();

            //3. 定義StatusStrip中要項目
            ToolStripItem[] tsi = new ToolStripItem[2];
            tsi[0] = toolStripLabel1;
            tsi[1] = toolStripStatusLabel1;

            //4. 將項目加入到StatusStrip中
            statusStrip1.Items.AddRange(tsi);

            //5. 將StatusStrip加入到窗體中
            this.Controls.Add(statusStrip1);
            #endregion
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
        }
    }
}
