namespace vcs_PictureCrop4
{
    partial class Form1
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
            this.picSource = new System.Windows.Forms.PictureBox();
            this.ofdOriginal = new System.Windows.Forms.OpenFileDialog();
            this.sfdResult = new System.Windows.Forms.SaveFileDialog();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileOpen = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileSaveArea = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileSaveWithoutArea = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.picArea = new System.Windows.Forms.PictureBox();
            this.picWithoutArea = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picSource)).BeginInit();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWithoutArea)).BeginInit();
            this.SuspendLayout();
            // 
            // picSource
            // 
            this.picSource.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSource.Location = new System.Drawing.Point(12, 25);
            this.picSource.Name = "picSource";
            this.picSource.Size = new System.Drawing.Size(100, 100);
            this.picSource.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSource.TabIndex = 10;
            this.picSource.TabStop = false;
            this.picSource.Visible = false;
            this.picSource.Paint += new System.Windows.Forms.PaintEventHandler(this.picSource_Paint);
            this.picSource.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseDown);
            this.picSource.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseMove);
            this.picSource.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseUp);
            // 
            // ofdOriginal
            // 
            this.ofdOriginal.Filter = "Image Files|*.bmp;*.jpg;*.gif;*.tif;*.png|All Files|*.*";
            // 
            // sfdResult
            // 
            this.sfdResult.Filter = "Image Files|*.bmp;*.jpg;*.gif;*.tif;*.png|All Files|*.*";
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(935, 24);
            this.menuStrip1.TabIndex = 11;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileOpen,
            this.mnuFileSaveArea,
            this.mnuFileSaveWithoutArea,
            this.toolStripMenuItem1,
            this.mnuFileExit});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(38, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileOpen
            // 
            this.mnuFileOpen.Name = "mnuFileOpen";
            this.mnuFileOpen.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
            this.mnuFileOpen.Size = new System.Drawing.Size(234, 22);
            this.mnuFileOpen.Text = "&Open...";
            this.mnuFileOpen.Click += new System.EventHandler(this.mnuFileOpen_Click);
            // 
            // mnuFileSaveArea
            // 
            this.mnuFileSaveArea.Enabled = false;
            this.mnuFileSaveArea.Name = "mnuFileSaveArea";
            this.mnuFileSaveArea.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.A)));
            this.mnuFileSaveArea.Size = new System.Drawing.Size(234, 22);
            this.mnuFileSaveArea.Text = "Save &Area...";
            this.mnuFileSaveArea.Click += new System.EventHandler(this.mnuFileSaveArea_Click);
            // 
            // mnuFileSaveWithoutArea
            // 
            this.mnuFileSaveWithoutArea.Enabled = false;
            this.mnuFileSaveWithoutArea.Name = "mnuFileSaveWithoutArea";
            this.mnuFileSaveWithoutArea.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.W)));
            this.mnuFileSaveWithoutArea.Size = new System.Drawing.Size(234, 22);
            this.mnuFileSaveWithoutArea.Text = "Save &Without Area...";
            this.mnuFileSaveWithoutArea.Click += new System.EventHandler(this.mnuFileSaveWithoutArea_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(231, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(234, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // picArea
            // 
            this.picArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picArea.Location = new System.Drawing.Point(118, 25);
            this.picArea.Name = "picArea";
            this.picArea.Size = new System.Drawing.Size(100, 100);
            this.picArea.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picArea.TabIndex = 12;
            this.picArea.TabStop = false;
            this.picArea.Visible = false;
            // 
            // picWithoutArea
            // 
            this.picWithoutArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picWithoutArea.Location = new System.Drawing.Point(224, 25);
            this.picWithoutArea.Name = "picWithoutArea";
            this.picWithoutArea.Size = new System.Drawing.Size(100, 100);
            this.picWithoutArea.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picWithoutArea.TabIndex = 13;
            this.picWithoutArea.TabStop = false;
            this.picWithoutArea.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(935, 571);
            this.Controls.Add(this.picWithoutArea);
            this.Controls.Add(this.picArea);
            this.Controls.Add(this.picSource);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "vcs_PictureCrop4";
            ((System.ComponentModel.ISupportInitialize)(this.picSource)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWithoutArea)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picSource;
        private System.Windows.Forms.OpenFileDialog ofdOriginal;
        private System.Windows.Forms.SaveFileDialog sfdResult;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileOpen;
        private System.Windows.Forms.ToolStripMenuItem mnuFileSaveWithoutArea;
        private System.Windows.Forms.ToolStripMenuItem mnuFileSaveArea;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.PictureBox picArea;
        private System.Windows.Forms.PictureBox picWithoutArea;
    }
}

