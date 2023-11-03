namespace CH1502
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
            this.msMain = new System.Windows.Forms.MenuStrip();
            this.msEdit = new System.Windows.Forms.ToolStripMenuItem();
            this.msView = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.msCreate = new System.Windows.Forms.ToolStripMenuItem();
            this.msCopy = new System.Windows.Forms.ToolStripMenuItem();
            this.msDelete = new System.Windows.Forms.ToolStripMenuItem();
            this.txtShow = new System.Windows.Forms.TextBox();
            this.msMain.SuspendLayout();
            this.SuspendLayout();
            // 
            // msMain
            // 
            this.msMain.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.msMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.msEdit});
            this.msMain.Location = new System.Drawing.Point(0, 0);
            this.msMain.Name = "msMain";
            this.msMain.Padding = new System.Windows.Forms.Padding(8, 3, 0, 3);
            this.msMain.Size = new System.Drawing.Size(303, 25);
            this.msMain.TabIndex = 2;
            this.msMain.Text = "menuStrip1";
            // 
            // msEdit
            // 
            this.msEdit.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.msView,
            this.toolStripSeparator1,
            this.msCreate,
            this.msCopy,
            this.msDelete});
            this.msEdit.Name = "msEdit";
            this.msEdit.Size = new System.Drawing.Size(43, 19);
            this.msEdit.Text = "編輯";
            // 
            // msView
            // 
            this.msView.Name = "msView";
            this.msView.Size = new System.Drawing.Size(180, 22);
            this.msView.Text = "檢視";
            this.msView.Click += new System.EventHandler(this.msView_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(95, 6);
            // 
            // msCreate
            // 
            this.msCreate.Name = "msCreate";
            this.msCreate.Size = new System.Drawing.Size(180, 22);
            this.msCreate.Text = "新增";
            this.msCreate.Click += new System.EventHandler(this.msCreate_Click);
            // 
            // msCopy
            // 
            this.msCopy.Name = "msCopy";
            this.msCopy.Size = new System.Drawing.Size(180, 22);
            this.msCopy.Text = "複製";
            this.msCopy.Click += new System.EventHandler(this.msCopy_Click);
            // 
            // msDelete
            // 
            this.msDelete.Name = "msDelete";
            this.msDelete.Size = new System.Drawing.Size(180, 22);
            this.msDelete.Text = "刪除";
            this.msDelete.Click += new System.EventHandler(this.msDelete_Click);
            // 
            // txtShow
            // 
            this.txtShow.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.txtShow.Location = new System.Drawing.Point(0, 76);
            this.txtShow.Multiline = true;
            this.txtShow.Name = "txtShow";
            this.txtShow.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtShow.Size = new System.Drawing.Size(303, 111);
            this.txtShow.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(303, 187);
            this.Controls.Add(this.msMain);
            this.Controls.Add(this.txtShow);
            this.Name = "Form1";
            this.Text = "CH1502";
            this.msMain.ResumeLayout(false);
            this.msMain.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip msMain;
        private System.Windows.Forms.ToolStripMenuItem msEdit;
        private System.Windows.Forms.ToolStripMenuItem msView;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem msCreate;
        private System.Windows.Forms.ToolStripMenuItem msCopy;
        private System.Windows.Forms.ToolStripMenuItem msDelete;
        private System.Windows.Forms.TextBox txtShow;
    }
}

