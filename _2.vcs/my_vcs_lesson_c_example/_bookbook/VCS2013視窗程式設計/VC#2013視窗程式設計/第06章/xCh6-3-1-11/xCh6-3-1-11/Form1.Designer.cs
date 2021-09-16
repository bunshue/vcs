namespace xCh6_3_1_11
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.檔案FToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.開新檔案ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.開啟舊檔ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.關閉檔案ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.結束XToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.格式OToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.樣式ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.粗體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.斜體ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.底線ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.顏色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.大小ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripTextBox1 = new System.Windows.Forms.ToolStripTextBox();
            this.toolStripComboBox1 = new System.Windows.Forms.ToolStripComboBox();
            this.toolStripComboBox2 = new System.Windows.Forms.ToolStripComboBox();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Visible;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.檔案FToolStripMenuItem,
            this.格式OToolStripMenuItem,
            this.toolStripTextBox1});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(425, 29);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 檔案FToolStripMenuItem
            // 
            this.檔案FToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.開新檔案ToolStripMenuItem,
            this.開啟舊檔ToolStripMenuItem,
            this.關閉檔案ToolStripMenuItem,
            this.toolStripMenuItem1,
            this.結束XToolStripMenuItem});
            this.檔案FToolStripMenuItem.Name = "檔案FToolStripMenuItem";
            this.檔案FToolStripMenuItem.Size = new System.Drawing.Size(63, 25);
            this.檔案FToolStripMenuItem.Text = "檔案(&F)";
            // 
            // 開新檔案ToolStripMenuItem
            // 
            this.開新檔案ToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("開新檔案ToolStripMenuItem.Image")));
            this.開新檔案ToolStripMenuItem.Name = "開新檔案ToolStripMenuItem";
            this.開新檔案ToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.開新檔案ToolStripMenuItem.Size = new System.Drawing.Size(193, 22);
            this.開新檔案ToolStripMenuItem.Text = "開新檔案...";
            this.開新檔案ToolStripMenuItem.Click += new System.EventHandler(this.開新檔案ToolStripMenuItem_Click);
            // 
            // 開啟舊檔ToolStripMenuItem
            // 
            this.開啟舊檔ToolStripMenuItem.Name = "開啟舊檔ToolStripMenuItem";
            this.開啟舊檔ToolStripMenuItem.Size = new System.Drawing.Size(193, 22);
            this.開啟舊檔ToolStripMenuItem.Text = "開啟舊檔";
            // 
            // 關閉檔案ToolStripMenuItem
            // 
            this.關閉檔案ToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("關閉檔案ToolStripMenuItem.Image")));
            this.關閉檔案ToolStripMenuItem.Name = "關閉檔案ToolStripMenuItem";
            this.關閉檔案ToolStripMenuItem.Size = new System.Drawing.Size(193, 22);
            this.關閉檔案ToolStripMenuItem.Text = "關閉檔案";
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(190, 6);
            // 
            // 結束XToolStripMenuItem
            // 
            this.結束XToolStripMenuItem.Name = "結束XToolStripMenuItem";
            this.結束XToolStripMenuItem.Size = new System.Drawing.Size(193, 22);
            this.結束XToolStripMenuItem.Text = "結束(&X)";
            // 
            // 格式OToolStripMenuItem
            // 
            this.格式OToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.樣式ToolStripMenuItem,
            this.顏色ToolStripMenuItem,
            this.大小ToolStripMenuItem});
            this.格式OToolStripMenuItem.Name = "格式OToolStripMenuItem";
            this.格式OToolStripMenuItem.Size = new System.Drawing.Size(67, 25);
            this.格式OToolStripMenuItem.Text = "格式(&O)";
            // 
            // 樣式ToolStripMenuItem
            // 
            this.樣式ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.粗體ToolStripMenuItem,
            this.斜體ToolStripMenuItem,
            this.底線ToolStripMenuItem});
            this.樣式ToolStripMenuItem.Name = "樣式ToolStripMenuItem";
            this.樣式ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.樣式ToolStripMenuItem.Text = "樣式";
            // 
            // 粗體ToolStripMenuItem
            // 
            this.粗體ToolStripMenuItem.CheckOnClick = true;
            this.粗體ToolStripMenuItem.Name = "粗體ToolStripMenuItem";
            this.粗體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.粗體ToolStripMenuItem.Text = "粗體";
            // 
            // 斜體ToolStripMenuItem
            // 
            this.斜體ToolStripMenuItem.CheckOnClick = true;
            this.斜體ToolStripMenuItem.Name = "斜體ToolStripMenuItem";
            this.斜體ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.斜體ToolStripMenuItem.Text = "斜體";
            // 
            // 底線ToolStripMenuItem
            // 
            this.底線ToolStripMenuItem.CheckOnClick = true;
            this.底線ToolStripMenuItem.Name = "底線ToolStripMenuItem";
            this.底線ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.底線ToolStripMenuItem.Text = "底線";
            // 
            // 顏色ToolStripMenuItem
            // 
            this.顏色ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripComboBox1});
            this.顏色ToolStripMenuItem.Name = "顏色ToolStripMenuItem";
            this.顏色ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.顏色ToolStripMenuItem.Text = "顏色";
            // 
            // 大小ToolStripMenuItem
            // 
            this.大小ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripComboBox2});
            this.大小ToolStripMenuItem.Name = "大小ToolStripMenuItem";
            this.大小ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.大小ToolStripMenuItem.Text = "大小";
            // 
            // toolStripTextBox1
            // 
            this.toolStripTextBox1.Name = "toolStripTextBox1";
            this.toolStripTextBox1.Size = new System.Drawing.Size(100, 25);
            // 
            // toolStripComboBox1
            // 
            this.toolStripComboBox1.Name = "toolStripComboBox1";
            this.toolStripComboBox1.Size = new System.Drawing.Size(121, 26);
            // 
            // toolStripComboBox2
            // 
            this.toolStripComboBox2.Name = "toolStripComboBox2";
            this.toolStripComboBox2.Size = new System.Drawing.Size(121, 26);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(425, 166);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "MenuStrip範例";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 檔案FToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 開新檔案ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 開啟舊檔ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 關閉檔案ToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem 結束XToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 格式OToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 樣式ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 粗體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 斜體ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 底線ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 顏色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 大小ToolStripMenuItem;
        private System.Windows.Forms.ToolStripTextBox toolStripTextBox1;
        private System.Windows.Forms.ToolStripComboBox toolStripComboBox1;
        private System.Windows.Forms.ToolStripComboBox toolStripComboBox2;
    }
}

