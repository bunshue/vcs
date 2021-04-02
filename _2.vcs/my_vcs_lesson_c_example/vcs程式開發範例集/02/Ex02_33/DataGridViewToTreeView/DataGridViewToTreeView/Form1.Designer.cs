namespace DataGridViewToTreeView
{
    partial class Form1
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

        #region Windows 視窗設計器產生的程式碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.清空內容ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.追加節點ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.操作類型ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // 清空內容ToolStripMenuItem
            // 
            this.清空內容ToolStripMenuItem.Name = "清空內容ToolStripMenuItem";
            this.清空內容ToolStripMenuItem.Size = new System.Drawing.Size(118,22);
            this.清空內容ToolStripMenuItem.Text = "清空內容";
            this.清空內容ToolStripMenuItem.Click += new System.EventHandler(this.清空內容ToolStripMenuItem_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowDrop = true;
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.BackgroundColor = System.Drawing.SystemColors.ButtonHighlight;
            this.dataGridView1.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.EnableWithoutHeaderText;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(-4,12);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 23;
            this.dataGridView1.Size = new System.Drawing.Size(321,380);
            this.dataGridView1.TabIndex = 5;
            this.dataGridView1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.dataGridView1_MouseDown);
            // 
            // 追加節點ToolStripMenuItem
            // 
            this.追加節點ToolStripMenuItem.Name = "追加節點ToolStripMenuItem";
            this.追加節點ToolStripMenuItem.Size = new System.Drawing.Size(118,22);
            this.追加節點ToolStripMenuItem.Text = "追加節點";
            this.追加節點ToolStripMenuItem.Click += new System.EventHandler(this.追加節點ToolStripMenuItem_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.dataGridView1);
            this.groupBox1.Location = new System.Drawing.Point(0,26);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(318,392);
            this.groupBox1.TabIndex = 17;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "DataGridView控制元件";
            // 
            // 操作類型ToolStripMenuItem
            // 
            this.操作類型ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.追加節點ToolStripMenuItem,
            this.清空內容ToolStripMenuItem});
            this.操作類型ToolStripMenuItem.Name = "操作類型ToolStripMenuItem";
            this.操作類型ToolStripMenuItem.Size = new System.Drawing.Size(65,20);
            this.操作類型ToolStripMenuItem.Text = "操作類型";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.treeView1);
            this.groupBox2.Location = new System.Drawing.Point(324,26);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(315,392);
            this.groupBox2.TabIndex = 15;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "TreeView控制元件";
            // 
            // treeView1
            // 
            this.treeView1.AllowDrop = true;
            this.treeView1.Location = new System.Drawing.Point(1,12);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(312,380);
            this.treeView1.TabIndex = 4;
            this.treeView1.MouseEnter += new System.EventHandler(this.treeView1_MouseEnter);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.操作類型ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0,0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(638,24);
            this.menuStrip1.TabIndex = 16;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F,12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(638,416);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "DataGridView與TreeView間數據的轉移";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ToolStripMenuItem 清空內容ToolStripMenuItem;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.ToolStripMenuItem 追加節點ToolStripMenuItem;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ToolStripMenuItem 操作類型ToolStripMenuItem;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.MenuStrip menuStrip1;
    }
}

