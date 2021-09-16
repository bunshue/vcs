namespace WinFontColorDialog
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.字型ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.色彩ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.前景色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.背景色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(25, 119);
            this.richTextBox1.Margin = new System.Windows.Forms.Padding(2);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(76, 78);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // menuStrip1
            // 
            this.menuStrip1.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.字型ToolStripMenuItem,
            this.色彩ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(4, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(284, 24);
            this.menuStrip1.TabIndex = 2;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 字型ToolStripMenuItem
            // 
            this.字型ToolStripMenuItem.Name = "字型ToolStripMenuItem";
            this.字型ToolStripMenuItem.Size = new System.Drawing.Size(49, 20);
            this.字型ToolStripMenuItem.Text = "字型";
            this.字型ToolStripMenuItem.Click += new System.EventHandler(this.字型ToolStripMenuItem_Click);
            // 
            // 色彩ToolStripMenuItem
            // 
            this.色彩ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.前景色ToolStripMenuItem,
            this.背景色ToolStripMenuItem});
            this.色彩ToolStripMenuItem.Name = "色彩ToolStripMenuItem";
            this.色彩ToolStripMenuItem.Size = new System.Drawing.Size(49, 20);
            this.色彩ToolStripMenuItem.Text = "色彩";
            // 
            // 前景色ToolStripMenuItem
            // 
            this.前景色ToolStripMenuItem.Name = "前景色ToolStripMenuItem";
            this.前景色ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.前景色ToolStripMenuItem.Text = "前景色";
            this.前景色ToolStripMenuItem.Click += new System.EventHandler(this.前景色ToolStripMenuItem_Click);
            // 
            // 背景色ToolStripMenuItem
            // 
            this.背景色ToolStripMenuItem.Name = "背景色ToolStripMenuItem";
            this.背景色ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.背景色ToolStripMenuItem.Text = "背景色";
            this.背景色ToolStripMenuItem.Click += new System.EventHandler(this.背景色ToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 262);
            this.Controls.Add(this.richTextBox1);
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

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 字型ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 色彩ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 前景色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 背景色ToolStripMenuItem;
        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.ColorDialog colorDialog1;
    }
}

