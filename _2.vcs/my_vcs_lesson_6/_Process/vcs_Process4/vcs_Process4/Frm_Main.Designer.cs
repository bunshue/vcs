namespace vcs_Process4
{
    partial class Frm_Main
    {
        /// <summary>
        /// 必需的設計器變量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗體設計器生成的代碼

        /// <summary>
        /// 設計器支持所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.刷新ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.結束進程ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.設置優先級ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.實時ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.高ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.高于標準ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.標準ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.低于標準ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.低ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.listView1 = new System.Windows.Forms.ListView();
            this.columnHeader11 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader12 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader13 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader14 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader15 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader16 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.tsslInfo = new System.Windows.Forms.ToolStripStatusLabel();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.contextMenuStrip1.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.刷新ToolStripMenuItem,
            this.結束進程ToolStripMenuItem,
            this.設置優先級ToolStripMenuItem});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.RenderMode = System.Windows.Forms.ToolStripRenderMode.System;
            this.contextMenuStrip1.ShowImageMargin = false;
            this.contextMenuStrip1.ShowItemToolTips = false;
            this.contextMenuStrip1.Size = new System.Drawing.Size(110, 70);
            // 
            // 刷新ToolStripMenuItem
            // 
            this.刷新ToolStripMenuItem.Name = "刷新ToolStripMenuItem";
            this.刷新ToolStripMenuItem.Size = new System.Drawing.Size(109, 22);
            this.刷新ToolStripMenuItem.Text = "刷新";
            this.刷新ToolStripMenuItem.Click += new System.EventHandler(this.刷新ToolStripMenuItem_Click);
            // 
            // 結束進程ToolStripMenuItem
            // 
            this.結束進程ToolStripMenuItem.Name = "結束進程ToolStripMenuItem";
            this.結束進程ToolStripMenuItem.Size = new System.Drawing.Size(109, 22);
            this.結束進程ToolStripMenuItem.Text = "結束進程";
            this.結束進程ToolStripMenuItem.Click += new System.EventHandler(this.結束進程ToolStripMenuItem_Click);
            // 
            // 設置優先級ToolStripMenuItem
            // 
            this.設置優先級ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.實時ToolStripMenuItem,
            this.高ToolStripMenuItem,
            this.高于標準ToolStripMenuItem,
            this.標準ToolStripMenuItem,
            this.低于標準ToolStripMenuItem,
            this.低ToolStripMenuItem});
            this.設置優先級ToolStripMenuItem.Name = "設置優先級ToolStripMenuItem";
            this.設置優先級ToolStripMenuItem.Size = new System.Drawing.Size(109, 22);
            this.設置優先級ToolStripMenuItem.Text = "設置優先級";
            // 
            // 實時ToolStripMenuItem
            // 
            this.實時ToolStripMenuItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.實時ToolStripMenuItem.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.實時ToolStripMenuItem.ImageScaling = System.Windows.Forms.ToolStripItemImageScaling.None;
            this.實時ToolStripMenuItem.Name = "實時ToolStripMenuItem";
            this.實時ToolStripMenuItem.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.實時ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.實時ToolStripMenuItem.Text = "實時";
            this.實時ToolStripMenuItem.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.實時ToolStripMenuItem.Click += new System.EventHandler(this.實時ToolStripMenuItem_Click);
            // 
            // 高ToolStripMenuItem
            // 
            this.高ToolStripMenuItem.Name = "高ToolStripMenuItem";
            this.高ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.高ToolStripMenuItem.Text = "高";
            this.高ToolStripMenuItem.Click += new System.EventHandler(this.高ToolStripMenuItem_Click);
            // 
            // 高于標準ToolStripMenuItem
            // 
            this.高于標準ToolStripMenuItem.Name = "高于標準ToolStripMenuItem";
            this.高于標準ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.高于標準ToolStripMenuItem.Text = "高于標準";
            this.高于標準ToolStripMenuItem.Click += new System.EventHandler(this.高于標準ToolStripMenuItem_Click);
            // 
            // 標準ToolStripMenuItem
            // 
            this.標準ToolStripMenuItem.Name = "標準ToolStripMenuItem";
            this.標準ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.標準ToolStripMenuItem.Text = "標準";
            this.標準ToolStripMenuItem.Click += new System.EventHandler(this.標準ToolStripMenuItem_Click);
            // 
            // 低于標準ToolStripMenuItem
            // 
            this.低于標準ToolStripMenuItem.Name = "低于標準ToolStripMenuItem";
            this.低于標準ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.低于標準ToolStripMenuItem.Text = "低于標準";
            this.低于標準ToolStripMenuItem.Click += new System.EventHandler(this.低于標準ToolStripMenuItem_Click);
            // 
            // 低ToolStripMenuItem
            // 
            this.低ToolStripMenuItem.Name = "低ToolStripMenuItem";
            this.低ToolStripMenuItem.Size = new System.Drawing.Size(122, 22);
            this.低ToolStripMenuItem.Text = "低";
            this.低ToolStripMenuItem.Click += new System.EventHandler(this.低ToolStripMenuItem_Click);
            // 
            // listView1
            // 
            this.listView1.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader11,
            this.columnHeader12,
            this.columnHeader13,
            this.columnHeader14,
            this.columnHeader15,
            this.columnHeader16});
            this.listView1.ContextMenuStrip = this.contextMenuStrip1;
            this.listView1.FullRowSelect = true;
            this.listView1.GridLines = true;
            this.listView1.Location = new System.Drawing.Point(12, 12);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(608, 585);
            this.listView1.TabIndex = 0;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // columnHeader11
            // 
            this.columnHeader11.Text = "映像名稱";
            this.columnHeader11.Width = 100;
            // 
            // columnHeader12
            // 
            this.columnHeader12.Text = "進程ID";
            this.columnHeader12.Width = 70;
            // 
            // columnHeader13
            // 
            this.columnHeader13.Text = "線程數";
            this.columnHeader13.Width = 70;
            // 
            // columnHeader14
            // 
            this.columnHeader14.Text = "優先級";
            // 
            // columnHeader15
            // 
            this.columnHeader15.Text = "物理內存";
            this.columnHeader15.Width = 89;
            // 
            // columnHeader16
            // 
            this.columnHeader16.Text = "虛擬內存";
            this.columnHeader16.Width = 128;
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsslInfo});
            this.statusStrip1.Location = new System.Drawing.Point(0, 653);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(1218, 22);
            this.statusStrip1.TabIndex = 7;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // tsslInfo
            // 
            this.tsslInfo.Name = "tsslInfo";
            this.tsslInfo.Size = new System.Drawing.Size(128, 17);
            this.tsslInfo.Text = "toolStripStatusLabel1";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(626, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(580, 585);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // Frm_Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1218, 675);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.statusStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Frm_Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "進程管理器";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.contextMenuStrip1.ResumeLayout(false);
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 刷新ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 結束進程ToolStripMenuItem;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.ColumnHeader columnHeader11;
        private System.Windows.Forms.ColumnHeader columnHeader12;
        private System.Windows.Forms.ColumnHeader columnHeader13;
        private System.Windows.Forms.ColumnHeader columnHeader14;
        private System.Windows.Forms.ColumnHeader columnHeader15;
        private System.Windows.Forms.ColumnHeader columnHeader16;
        private System.Windows.Forms.ToolStripMenuItem 設置優先級ToolStripMenuItem;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel tsslInfo;
        private System.Windows.Forms.ToolStripMenuItem 實時ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 高ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 高于標準ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 標準ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 低于標準ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 低ToolStripMenuItem;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}
