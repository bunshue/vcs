namespace xCh6_3_2_11
{
    partial class Form1
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
            this.components = new System.ComponentModel.Container();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.剪下ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.複製ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.貼上ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.contextMenuStrip2 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.還原ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.移動ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.大小ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.最小化ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.最大化ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.關閉ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.contextMenuStrip1.SuspendLayout();
            this.contextMenuStrip2.SuspendLayout();
            this.SuspendLayout();
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.剪下ToolStripMenuItem,
            this.複製ToolStripMenuItem,
            this.貼上ToolStripMenuItem});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.ShowImageMargin = false;
            this.contextMenuStrip1.Size = new System.Drawing.Size(131, 70);
            // 
            // 剪下ToolStripMenuItem
            // 
            this.剪下ToolStripMenuItem.Name = "剪下ToolStripMenuItem";
            this.剪下ToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.U)));
            this.剪下ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.剪下ToolStripMenuItem.Text = "剪下";
            // 
            // 複製ToolStripMenuItem
            // 
            this.複製ToolStripMenuItem.Name = "複製ToolStripMenuItem";
            this.複製ToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
            this.複製ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.複製ToolStripMenuItem.Text = "複製";
            // 
            // 貼上ToolStripMenuItem
            // 
            this.貼上ToolStripMenuItem.Name = "貼上ToolStripMenuItem";
            this.貼上ToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
            this.貼上ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.貼上ToolStripMenuItem.Text = "貼上";
            // 
            // contextMenuStrip2
            // 
            this.contextMenuStrip2.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.還原ToolStripMenuItem,
            this.移動ToolStripMenuItem,
            this.大小ToolStripMenuItem,
            this.最小化ToolStripMenuItem,
            this.最大化ToolStripMenuItem,
            this.toolStripMenuItem1,
            this.關閉ToolStripMenuItem});
            this.contextMenuStrip2.Name = "contextMenuStrip2";
            this.contextMenuStrip2.Size = new System.Drawing.Size(119, 142);
            // 
            // 還原ToolStripMenuItem
            // 
            this.還原ToolStripMenuItem.Image = global::xCh6_3_2_11.Properties.Resources.user32x32;
            this.還原ToolStripMenuItem.Name = "還原ToolStripMenuItem";
            this.還原ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.還原ToolStripMenuItem.Text = "還原";
            // 
            // 移動ToolStripMenuItem
            // 
            this.移動ToolStripMenuItem.Name = "移動ToolStripMenuItem";
            this.移動ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.移動ToolStripMenuItem.Text = "移動";
            // 
            // 大小ToolStripMenuItem
            // 
            this.大小ToolStripMenuItem.Name = "大小ToolStripMenuItem";
            this.大小ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.大小ToolStripMenuItem.Text = "大小";
            // 
            // 最小化ToolStripMenuItem
            // 
            this.最小化ToolStripMenuItem.Image = global::xCh6_3_2_11.Properties.Resources.frai32x32;
            this.最小化ToolStripMenuItem.Name = "最小化ToolStripMenuItem";
            this.最小化ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.最小化ToolStripMenuItem.Text = "最小化";
            // 
            // 最大化ToolStripMenuItem
            // 
            this.最大化ToolStripMenuItem.Name = "最大化ToolStripMenuItem";
            this.最大化ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.最大化ToolStripMenuItem.Text = "最大化";
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(149, 6);
            // 
            // 關閉ToolStripMenuItem
            // 
            this.關閉ToolStripMenuItem.Name = "關閉ToolStripMenuItem";
            this.關閉ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.關閉ToolStripMenuItem.Text = "關閉";
            // 
            // textBox1
            // 
            this.textBox1.ContextMenuStrip = this.contextMenuStrip1;
            this.textBox1.Location = new System.Drawing.Point(12, 12);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(254, 23);
            this.textBox1.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(278, 222);
            this.ContextMenuStrip = this.contextMenuStrip2;
            this.Controls.Add(this.textBox1);
            this.Name = "Form1";
            this.Text = "ContextMenuStrip範例";
            this.contextMenuStrip1.ResumeLayout(false);
            this.contextMenuStrip2.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 剪下ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 複製ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 貼上ToolStripMenuItem;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip2;
        private System.Windows.Forms.ToolStripMenuItem 還原ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 移動ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 大小ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 最小化ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 最大化ToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem 關閉ToolStripMenuItem;
        private System.Windows.Forms.TextBox textBox1;
    }
}

