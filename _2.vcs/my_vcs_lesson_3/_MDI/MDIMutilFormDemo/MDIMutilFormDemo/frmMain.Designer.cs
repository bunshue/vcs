namespace MDIMutilFormDemo
{
    partial class frmMain
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.遊戲種類ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.拉霸ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.記憶大考驗ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.結束ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.遊戲種類ToolStripMenuItem,
            this.結束ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(300, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 遊戲種類ToolStripMenuItem
            // 
            this.遊戲種類ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.拉霸ToolStripMenuItem,
            this.記憶大考驗ToolStripMenuItem});
            this.遊戲種類ToolStripMenuItem.Name = "遊戲種類ToolStripMenuItem";
            this.遊戲種類ToolStripMenuItem.Size = new System.Drawing.Size(68, 20);
            this.遊戲種類ToolStripMenuItem.Text = "遊戲種類";
            // 
            // 拉霸ToolStripMenuItem
            // 
            this.拉霸ToolStripMenuItem.Name = "拉霸ToolStripMenuItem";
            this.拉霸ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.拉霸ToolStripMenuItem.Text = "拉霸遊戲";
            this.拉霸ToolStripMenuItem.Click += new System.EventHandler(this.拉霸遊戲ToolStripMenuItem_Click);
            // 
            // 記憶大考驗ToolStripMenuItem
            // 
            this.記憶大考驗ToolStripMenuItem.Name = "記憶大考驗ToolStripMenuItem";
            this.記憶大考驗ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.記憶大考驗ToolStripMenuItem.Text = "記憶大考驗";
            this.記憶大考驗ToolStripMenuItem.Click += new System.EventHandler(this.記憶大考驗ToolStripMenuItem_Click);
            // 
            // 結束ToolStripMenuItem
            // 
            this.結束ToolStripMenuItem.Name = "結束ToolStripMenuItem";
            this.結束ToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.結束ToolStripMenuItem.Text = "結束";
            this.結束ToolStripMenuItem.Click += new System.EventHandler(this.結束ToolStripMenuItem_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(300, 272);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "frmMain";
            this.Text = "遊戲大進擊";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 遊戲種類ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 拉霸ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 記憶大考驗ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 結束ToolStripMenuItem;

    }
}

