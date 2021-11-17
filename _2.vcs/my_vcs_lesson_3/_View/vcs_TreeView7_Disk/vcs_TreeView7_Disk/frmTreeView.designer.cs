namespace vcs_TreeView7_Disk
{
    partial class frmTreeView
    {
        /// <summary>
        /// 必需的設計器變數。
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

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.TreeViewFile = new System.Windows.Forms.TreeView();
            this.ListViewFile = new System.Windows.Forms.ListView();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.SuspendLayout();
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.TreeViewFile);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.ListViewFile);
            this.splitContainer1.Size = new System.Drawing.Size(636, 550);
            this.splitContainer1.SplitterDistance = 212;
            this.splitContainer1.TabIndex = 0;
            // 
            // TreeViewFile
            // 
            this.TreeViewFile.Location = new System.Drawing.Point(3, 3);
            this.TreeViewFile.Name = "TreeViewFile";
            this.TreeViewFile.Size = new System.Drawing.Size(207, 544);
            this.TreeViewFile.TabIndex = 0;
            this.TreeViewFile.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.TreeViewFile_AfterSelect);
            // 
            // ListViewFile
            // 
            this.ListViewFile.Dock = System.Windows.Forms.DockStyle.Fill;
            this.ListViewFile.Location = new System.Drawing.Point(0, 0);
            this.ListViewFile.MultiSelect = false;
            this.ListViewFile.Name = "ListViewFile";
            this.ListViewFile.Size = new System.Drawing.Size(420, 550);
            this.ListViewFile.TabIndex = 0;
            this.ListViewFile.UseCompatibleStateImageBehavior = false;
            this.ListViewFile.View = System.Windows.Forms.View.List;
            this.ListViewFile.SelectedIndexChanged += new System.EventHandler(this.ListViewFile_SelectedIndexChanged);
            this.ListViewFile.DoubleClick += new System.EventHandler(this.ListViewFile_DoubleClick);
            // 
            // frmTreeView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(636, 550);
            this.Controls.Add(this.splitContainer1);
            this.Name = "frmTreeView";
            this.Text = "TreeView組件搜尋磁碟目錄";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.TreeView TreeViewFile;
        private System.Windows.Forms.ListView ListViewFile;
    }
}

