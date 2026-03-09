using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MDIMutilFormDemo
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }
        // 表單載入時執行此事件處理函式
        private void frmMain_Load(object sender, EventArgs e)
        {
            // 指定目前表單為MDI表單的容器
            this.IsMdiContainer = true;
        }
        // 執行功能表的 [遊戲種類/拉霸遊戲] 選項會執行此事件處理函式 
        private void 拉霸遊戲ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            frmBar f = new frmBar();
            f.MdiParent = this;
            f.Show();
        }
        // 執行功能表的 [遊戲種類/記憶大考驗] 選項會執行此事件處理函式 
        private void 記憶大考驗ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            frmMemory f = new frmMemory();
            f.MdiParent = this;
            f.Show();
        }
        // 執行功能表的 [結束] 選項會執行此事件處理函式 
        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
