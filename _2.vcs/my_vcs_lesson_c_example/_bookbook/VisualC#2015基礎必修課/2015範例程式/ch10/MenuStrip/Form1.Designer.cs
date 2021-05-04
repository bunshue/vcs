namespace MenuStrip
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.字型ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.細明體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.新細明體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.標楷體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.樣式ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.粗體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.斜體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.加底線ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.字型ToolStripMenuItem,
            this.樣式ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(245, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 字型ToolStripMenuItem
            // 
            this.字型ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.細明體ToolStripMenuItem,
            this.新細明體ToolStripMenuItem,
            this.標楷體ToolStripMenuItem});
            this.字型ToolStripMenuItem.Name = "字型ToolStripMenuItem";
            this.字型ToolStripMenuItem.Size = new System.Drawing.Size(43, 20);
            this.字型ToolStripMenuItem.Text = "字型";
            // 
            // 細明體ToolStripMenuItem
            // 
            this.細明體ToolStripMenuItem.Name = "細明體ToolStripMenuItem";
            this.細明體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.細明體ToolStripMenuItem.Text = "細明體";
            this.細明體ToolStripMenuItem.Click += new System.EventHandler(this.細明體ToolStripMenuItem_Click);
            // 
            // 新細明體ToolStripMenuItem
            // 
            this.新細明體ToolStripMenuItem.Name = "新細明體ToolStripMenuItem";
            this.新細明體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.新細明體ToolStripMenuItem.Text = "新細明體";
            this.新細明體ToolStripMenuItem.Click += new System.EventHandler(this.新細明體ToolStripMenuItem_Click);
            // 
            // 標楷體ToolStripMenuItem
            // 
            this.標楷體ToolStripMenuItem.Name = "標楷體ToolStripMenuItem";
            this.標楷體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.標楷體ToolStripMenuItem.Text = "標楷體";
            this.標楷體ToolStripMenuItem.Click += new System.EventHandler(this.標楷體ToolStripMenuItem_Click);
            // 
            // 樣式ToolStripMenuItem
            // 
            this.樣式ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.粗體ToolStripMenuItem,
            this.斜體ToolStripMenuItem,
            this.加底線ToolStripMenuItem});
            this.樣式ToolStripMenuItem.Name = "樣式ToolStripMenuItem";
            this.樣式ToolStripMenuItem.Size = new System.Drawing.Size(43, 20);
            this.樣式ToolStripMenuItem.Text = "樣式";
            // 
            // 粗體ToolStripMenuItem
            // 
            this.粗體ToolStripMenuItem.Name = "粗體ToolStripMenuItem";
            this.粗體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.粗體ToolStripMenuItem.Text = "粗體";
            this.粗體ToolStripMenuItem.Click += new System.EventHandler(this.粗體ToolStripMenuItem_Click);
            // 
            // 斜體ToolStripMenuItem
            // 
            this.斜體ToolStripMenuItem.Name = "斜體ToolStripMenuItem";
            this.斜體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.斜體ToolStripMenuItem.Text = "斜體";
            this.斜體ToolStripMenuItem.Click += new System.EventHandler(this.斜體ToolStripMenuItem_Click);
            // 
            // 加底線ToolStripMenuItem
            // 
            this.加底線ToolStripMenuItem.Name = "加底線ToolStripMenuItem";
            this.加底線ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.加底線ToolStripMenuItem.Text = "加底線";
            this.加底線ToolStripMenuItem.Click += new System.EventHandler(this.加底線ToolStripMenuItem_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 107);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(245, 140);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 字型ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 細明體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 新細明體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 標楷體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 樣式ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 粗體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 斜體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 加底線ToolStripMenuItem;
        private System.Windows.Forms.Label label1;
    }
}

