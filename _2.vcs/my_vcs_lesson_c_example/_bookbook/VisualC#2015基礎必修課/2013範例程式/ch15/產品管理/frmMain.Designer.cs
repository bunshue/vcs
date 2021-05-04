namespace 產品管理
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.系統功能ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.產品類別管理ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.產品資料管理ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.產品關聯查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.系統功能ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(284, 24);
            this.menuStrip1.TabIndex = 2;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 系統功能ToolStripMenuItem
            // 
            this.系統功能ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.產品類別管理ToolStripMenuItem,
            this.產品資料管理ToolStripMenuItem,
            this.產品關聯查詢ToolStripMenuItem});
            this.系統功能ToolStripMenuItem.Name = "系統功能ToolStripMenuItem";
            this.系統功能ToolStripMenuItem.Size = new System.Drawing.Size(67, 20);
            this.系統功能ToolStripMenuItem.Text = "系統功能";
            // 
            // 產品類別管理ToolStripMenuItem
            // 
            this.產品類別管理ToolStripMenuItem.Name = "產品類別管理ToolStripMenuItem";
            this.產品類別管理ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.產品類別管理ToolStripMenuItem.Text = "產品類別管理";
            this.產品類別管理ToolStripMenuItem.Click += new System.EventHandler(this.產品類別管理ToolStripMenuItem_Click);
            // 
            // 產品資料管理ToolStripMenuItem
            // 
            this.產品資料管理ToolStripMenuItem.Name = "產品資料管理ToolStripMenuItem";
            this.產品資料管理ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.產品資料管理ToolStripMenuItem.Text = "產品資料管理";
            this.產品資料管理ToolStripMenuItem.Click += new System.EventHandler(this.產品資料管理ToolStripMenuItem_Click);
            // 
            // 產品關聯查詢ToolStripMenuItem
            // 
            this.產品關聯查詢ToolStripMenuItem.Name = "產品關聯查詢ToolStripMenuItem";
            this.產品關聯查詢ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.產品關聯查詢ToolStripMenuItem.Text = "產品關聯查詢";
            this.產品關聯查詢ToolStripMenuItem.Click += new System.EventHandler(this.產品關聯查詢ToolStripMenuItem_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.menuStrip1);
            this.IsMdiContainer = true;
            this.Name = "frmMain";
            this.Text = "產品管理系統";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 系統功能ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 產品類別管理ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 產品資料管理ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 產品關聯查詢ToolStripMenuItem;
    }
}