namespace CH1301
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
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
            this.components = new System.ComponentModel.Container();
            this.Main_menuStrip = new System.Windows.Forms.MenuStrip();
            this.File_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.NewFile_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.OpenFile_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.SaveFile_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.EndFile_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Edit_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Upper_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Lower_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.Std_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.Style_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.StyleStd_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.StyleBold_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.StyleItalic_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font_menuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font8MenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font10MenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font12MenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font14MenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Font16MenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.ctmsColor = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.綠色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.黑色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.黃色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.紅色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Main_menuStrip.SuspendLayout();
            this.ctmsColor.SuspendLayout();
            this.SuspendLayout();
            // 
            // Main_menuStrip
            // 
            this.Main_menuStrip.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.Main_menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.File_menuItem,
            this.Edit_menuItem,
            this.Font_menuItem});
            this.Main_menuStrip.Location = new System.Drawing.Point(0, 0);
            this.Main_menuStrip.Name = "Main_menuStrip";
            this.Main_menuStrip.Size = new System.Drawing.Size(375, 24);
            this.Main_menuStrip.TabIndex = 2;
            this.Main_menuStrip.Text = "設定檔案";
            // 
            // File_menuItem
            // 
            this.File_menuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.NewFile_menuItem,
            this.OpenFile_menuItem,
            this.SaveFile_menuItem,
            this.toolStripSeparator1,
            this.EndFile_menuItem});
            this.File_menuItem.Name = "File_menuItem";
            this.File_menuItem.Size = new System.Drawing.Size(57, 20);
            this.File_menuItem.Text = "檔案(&F)";
            // 
            // NewFile_menuItem
            // 
            this.NewFile_menuItem.Name = "NewFile_menuItem";
            this.NewFile_menuItem.ShortcutKeyDisplayString = "";
            this.NewFile_menuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.NewFile_menuItem.Size = new System.Drawing.Size(167, 22);
            this.NewFile_menuItem.Text = "新增檔案";
            this.NewFile_menuItem.Click += new System.EventHandler(this.NewFile_menuItem_Click);
            // 
            // OpenFile_menuItem
            // 
            this.OpenFile_menuItem.Name = "OpenFile_menuItem";
            this.OpenFile_menuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Q)));
            this.OpenFile_menuItem.Size = new System.Drawing.Size(167, 22);
            this.OpenFile_menuItem.Text = "開啟檔案";
            this.OpenFile_menuItem.Click += new System.EventHandler(this.OpenFile_menuItem_Click);
            // 
            // SaveFile_menuItem
            // 
            this.SaveFile_menuItem.Name = "SaveFile_menuItem";
            this.SaveFile_menuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.SaveFile_menuItem.Size = new System.Drawing.Size(167, 22);
            this.SaveFile_menuItem.Text = "儲存檔案";
            this.SaveFile_menuItem.Click += new System.EventHandler(this.SaveFile_menuItem_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(164, 6);
            // 
            // EndFile_menuItem
            // 
            this.EndFile_menuItem.Name = "EndFile_menuItem";
            this.EndFile_menuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Q)));
            this.EndFile_menuItem.Size = new System.Drawing.Size(167, 22);
            this.EndFile_menuItem.Text = "結束";
            this.EndFile_menuItem.Click += new System.EventHandler(this.EndFile_menuItem_Click);
            // 
            // Edit_menuItem
            // 
            this.Edit_menuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.Upper_menuItem,
            this.Lower_menuItem,
            this.toolStripMenuItem1,
            this.Std_menuItem,
            this.toolStripSeparator2,
            this.Style_menuItem});
            this.Edit_menuItem.Name = "Edit_menuItem";
            this.Edit_menuItem.Size = new System.Drawing.Size(58, 20);
            this.Edit_menuItem.Text = "文字(&T)";
            // 
            // Upper_menuItem
            // 
            this.Upper_menuItem.Name = "Upper_menuItem";
            this.Upper_menuItem.Size = new System.Drawing.Size(137, 22);
            this.Upper_menuItem.Text = " \t轉換大寫";
            this.Upper_menuItem.Click += new System.EventHandler(this.Upper_menuItem_Click);
            // 
            // Lower_menuItem
            // 
            this.Lower_menuItem.Name = "Lower_menuItem";
            this.Lower_menuItem.Size = new System.Drawing.Size(137, 22);
            this.Lower_menuItem.Text = " \t轉換小寫";
            this.Lower_menuItem.Click += new System.EventHandler(this.Lower_menuItem_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(134, 6);
            // 
            // Std_menuItem
            // 
            this.Std_menuItem.Name = "Std_menuItem";
            this.Std_menuItem.Size = new System.Drawing.Size(137, 22);
            this.Std_menuItem.Text = " \t標楷體字型";
            this.Std_menuItem.Click += new System.EventHandler(this.Std_menuItem_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(134, 6);
            // 
            // Style_menuItem
            // 
            this.Style_menuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.StyleStd_menuItem,
            this.StyleBold_menuItem,
            this.StyleItalic_menuItem});
            this.Style_menuItem.Name = "Style_menuItem";
            this.Style_menuItem.Size = new System.Drawing.Size(137, 22);
            this.Style_menuItem.Text = " \t字體";
            // 
            // StyleStd_menuItem
            // 
            this.StyleStd_menuItem.Name = "StyleStd_menuItem";
            this.StyleStd_menuItem.Size = new System.Drawing.Size(98, 22);
            this.StyleStd_menuItem.Text = "標準";
            this.StyleStd_menuItem.Click += new System.EventHandler(this.StyleStd_menuItem_Click);
            // 
            // StyleBold_menuItem
            // 
            this.StyleBold_menuItem.Name = "StyleBold_menuItem";
            this.StyleBold_menuItem.Size = new System.Drawing.Size(98, 22);
            this.StyleBold_menuItem.Text = "粗體";
            this.StyleBold_menuItem.Click += new System.EventHandler(this.StyleBold_menuItem_Click);
            // 
            // StyleItalic_menuItem
            // 
            this.StyleItalic_menuItem.Name = "StyleItalic_menuItem";
            this.StyleItalic_menuItem.Size = new System.Drawing.Size(98, 22);
            this.StyleItalic_menuItem.Text = "斜體";
            this.StyleItalic_menuItem.Click += new System.EventHandler(this.StyleItalic_menuItem_Click);
            // 
            // Font_menuItem
            // 
            this.Font_menuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.Font8MenuItem,
            this.Font10MenuItem,
            this.Font12MenuItem,
            this.Font14MenuItem,
            this.Font16MenuItem});
            this.Font_menuItem.Name = "Font_menuItem";
            this.Font_menuItem.Size = new System.Drawing.Size(82, 20);
            this.Font_menuItem.Text = "字型大小(&S)";
            // 
            // Font8MenuItem
            // 
            this.Font8MenuItem.Name = "Font8MenuItem";
            this.Font8MenuItem.Size = new System.Drawing.Size(180, 22);
            this.Font8MenuItem.Text = "8";
            this.Font8MenuItem.Click += new System.EventHandler(this.Font8MenuItem_Click);
            // 
            // Font10MenuItem
            // 
            this.Font10MenuItem.Name = "Font10MenuItem";
            this.Font10MenuItem.Size = new System.Drawing.Size(180, 22);
            this.Font10MenuItem.Text = "10";
            this.Font10MenuItem.Click += new System.EventHandler(this.Font10MenuItem_Click);
            // 
            // Font12MenuItem
            // 
            this.Font12MenuItem.Name = "Font12MenuItem";
            this.Font12MenuItem.Size = new System.Drawing.Size(180, 22);
            this.Font12MenuItem.Text = "12";
            this.Font12MenuItem.Click += new System.EventHandler(this.Font12MenuItem_Click);
            // 
            // Font14MenuItem
            // 
            this.Font14MenuItem.Name = "Font14MenuItem";
            this.Font14MenuItem.Size = new System.Drawing.Size(180, 22);
            this.Font14MenuItem.Text = "14";
            this.Font14MenuItem.Click += new System.EventHandler(this.Font14MenuItem_Click);
            // 
            // Font16MenuItem
            // 
            this.Font16MenuItem.Name = "Font16MenuItem";
            this.Font16MenuItem.Size = new System.Drawing.Size(180, 22);
            this.Font16MenuItem.Text = "16";
            this.Font16MenuItem.Click += new System.EventHandler(this.Font16MenuItem_Click);
            // 
            // rtxtShow
            // 
            this.rtxtShow.ContextMenuStrip = this.ctmsColor;
            this.rtxtShow.Dock = System.Windows.Forms.DockStyle.Fill;
            this.rtxtShow.Location = new System.Drawing.Point(0, 0);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(375, 210);
            this.rtxtShow.TabIndex = 3;
            this.rtxtShow.Text = "";
            // 
            // ctmsColor
            // 
            this.ctmsColor.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.ctmsColor.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.綠色ToolStripMenuItem,
            this.黑色ToolStripMenuItem,
            this.黃色ToolStripMenuItem,
            this.紅色ToolStripMenuItem});
            this.ctmsColor.Name = "ctmsColor";
            this.ctmsColor.Size = new System.Drawing.Size(181, 114);
            // 
            // 綠色ToolStripMenuItem
            // 
            this.綠色ToolStripMenuItem.Name = "綠色ToolStripMenuItem";
            this.綠色ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.綠色ToolStripMenuItem.Text = "綠色";
            this.綠色ToolStripMenuItem.Click += new System.EventHandler(this.綠色ToolStripMenuItem_Click);
            // 
            // 黑色ToolStripMenuItem
            // 
            this.黑色ToolStripMenuItem.Name = "黑色ToolStripMenuItem";
            this.黑色ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.黑色ToolStripMenuItem.Text = "黑色";
            this.黑色ToolStripMenuItem.Click += new System.EventHandler(this.黑色ToolStripMenuItem_Click);
            // 
            // 黃色ToolStripMenuItem
            // 
            this.黃色ToolStripMenuItem.Name = "黃色ToolStripMenuItem";
            this.黃色ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.黃色ToolStripMenuItem.Text = "黃色";
            this.黃色ToolStripMenuItem.Click += new System.EventHandler(this.黃色ToolStripMenuItem_Click);
            // 
            // 紅色ToolStripMenuItem
            // 
            this.紅色ToolStripMenuItem.Name = "紅色ToolStripMenuItem";
            this.紅色ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.紅色ToolStripMenuItem.Text = "紅色";
            this.紅色ToolStripMenuItem.Click += new System.EventHandler(this.紅色ToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(375, 210);
            this.Controls.Add(this.Main_menuStrip);
            this.Controls.Add(this.rtxtShow);
            this.Name = "Form1";
            this.Text = "CH1301";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Main_menuStrip.ResumeLayout(false);
            this.Main_menuStrip.PerformLayout();
            this.ctmsColor.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip Main_menuStrip;
        private System.Windows.Forms.ToolStripMenuItem File_menuItem;
        private System.Windows.Forms.ToolStripMenuItem NewFile_menuItem;
        private System.Windows.Forms.ToolStripMenuItem OpenFile_menuItem;
        private System.Windows.Forms.ToolStripMenuItem SaveFile_menuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem EndFile_menuItem;
        private System.Windows.Forms.ToolStripMenuItem Edit_menuItem;
        private System.Windows.Forms.ToolStripMenuItem Upper_menuItem;
        private System.Windows.Forms.ToolStripMenuItem Lower_menuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem Std_menuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripMenuItem Style_menuItem;
        private System.Windows.Forms.ToolStripMenuItem StyleStd_menuItem;
        private System.Windows.Forms.ToolStripMenuItem StyleBold_menuItem;
        private System.Windows.Forms.ToolStripMenuItem StyleItalic_menuItem;
        private System.Windows.Forms.ToolStripMenuItem Font_menuItem;
        private System.Windows.Forms.ToolStripMenuItem Font8MenuItem;
        private System.Windows.Forms.ToolStripMenuItem Font10MenuItem;
        private System.Windows.Forms.ToolStripMenuItem Font12MenuItem;
        private System.Windows.Forms.ToolStripMenuItem Font14MenuItem;
        private System.Windows.Forms.ToolStripMenuItem Font16MenuItem;
        private System.Windows.Forms.RichTextBox rtxtShow;
        private System.Windows.Forms.ContextMenuStrip ctmsColor;
        private System.Windows.Forms.ToolStripMenuItem 綠色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 黑色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 黃色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 紅色ToolStripMenuItem;
    }
}

