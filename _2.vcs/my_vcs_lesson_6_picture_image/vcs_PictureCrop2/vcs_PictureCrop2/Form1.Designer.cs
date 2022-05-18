namespace vcs_PictureCrop2
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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileOpen = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileSaveAs = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale100 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale75 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale66 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale50 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale25 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale15 = new System.Windows.Forms.ToolStripMenuItem();
            this.rectangleToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRectangleReset = new System.Windows.Forms.ToolStripMenuItem();
            this.sfdImage = new System.Windows.Forms.SaveFileDialog();
            this.ofdImage = new System.Windows.Forms.OpenFileDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.txtWidth = new System.Windows.Forms.TextBox();
            this.txtHeight = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.picImage = new System.Windows.Forms.PictureBox();
            this.txtAspectRatio = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.mnuScale,
            this.rectangleToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1142, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileOpen,
            this.mnuFileSaveAs,
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
            this.mnuFileOpen.Size = new System.Drawing.Size(168, 22);
            this.mnuFileOpen.Text = "&Open...";
            this.mnuFileOpen.Click += new System.EventHandler(this.mnuFileOpen_Click);
            // 
            // mnuFileSaveAs
            // 
            this.mnuFileSaveAs.Enabled = false;
            this.mnuFileSaveAs.Name = "mnuFileSaveAs";
            this.mnuFileSaveAs.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.mnuFileSaveAs.Size = new System.Drawing.Size(168, 22);
            this.mnuFileSaveAs.Text = "&Save As...";
            this.mnuFileSaveAs.Click += new System.EventHandler(this.mnuFileSaveAs_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(165, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(168, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // mnuScale
            // 
            this.mnuScale.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuScale100,
            this.mnuScale75,
            this.mnuScale66,
            this.mnuScale50,
            this.mnuScale25,
            this.mnuScale15});
            this.mnuScale.Name = "mnuScale";
            this.mnuScale.Size = new System.Drawing.Size(92, 20);
            this.mnuScale.Text = "&Scale (100%)";
            // 
            // mnuScale100
            // 
            this.mnuScale100.Checked = true;
            this.mnuScale100.CheckState = System.Windows.Forms.CheckState.Checked;
            this.mnuScale100.Name = "mnuScale100";
            this.mnuScale100.Size = new System.Drawing.Size(106, 22);
            this.mnuScale100.Text = "1&00%";
            this.mnuScale100.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale75
            // 
            this.mnuScale75.Name = "mnuScale75";
            this.mnuScale75.Size = new System.Drawing.Size(106, 22);
            this.mnuScale75.Text = "&75%";
            this.mnuScale75.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale66
            // 
            this.mnuScale66.Name = "mnuScale66";
            this.mnuScale66.Size = new System.Drawing.Size(106, 22);
            this.mnuScale66.Text = "&66%";
            this.mnuScale66.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale50
            // 
            this.mnuScale50.Name = "mnuScale50";
            this.mnuScale50.Size = new System.Drawing.Size(106, 22);
            this.mnuScale50.Text = "&50%";
            this.mnuScale50.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale25
            // 
            this.mnuScale25.Name = "mnuScale25";
            this.mnuScale25.Size = new System.Drawing.Size(106, 22);
            this.mnuScale25.Text = "&25%";
            this.mnuScale25.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale15
            // 
            this.mnuScale15.Name = "mnuScale15";
            this.mnuScale15.Size = new System.Drawing.Size(106, 22);
            this.mnuScale15.Text = "&15%";
            this.mnuScale15.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // rectangleToolStripMenuItem
            // 
            this.rectangleToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuRectangleReset});
            this.rectangleToolStripMenuItem.Name = "rectangleToolStripMenuItem";
            this.rectangleToolStripMenuItem.Size = new System.Drawing.Size(76, 20);
            this.rectangleToolStripMenuItem.Text = "&Rectangle";
            // 
            // mnuRectangleReset
            // 
            this.mnuRectangleReset.Name = "mnuRectangleReset";
            this.mnuRectangleReset.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.R)));
            this.mnuRectangleReset.Size = new System.Drawing.Size(148, 22);
            this.mnuRectangleReset.Text = "&Reset";
            this.mnuRectangleReset.Click += new System.EventHandler(this.mnuRectangleReset_Click);
            // 
            // sfdImage
            // 
            this.sfdImage.DefaultExt = "png";
            this.sfdImage.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // ofdImage
            // 
            this.ofdImage.DefaultExt = "png";
            this.ofdImage.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "Aspect Ratio:";
            // 
            // txtWidth
            // 
            this.txtWidth.Location = new System.Drawing.Point(156, 25);
            this.txtWidth.Name = "txtWidth";
            this.txtWidth.Size = new System.Drawing.Size(46, 22);
            this.txtWidth.TabIndex = 1;
            this.txtWidth.Text = "400";
            this.txtWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtWidth.TextChanged += new System.EventHandler(this.txtWidth_TextChanged);
            // 
            // txtHeight
            // 
            this.txtHeight.Location = new System.Drawing.Point(226, 25);
            this.txtHeight.Name = "txtHeight";
            this.txtHeight.Size = new System.Drawing.Size(46, 22);
            this.txtHeight.TabIndex = 2;
            this.txtHeight.Text = "300";
            this.txtHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtHeight.TextChanged += new System.EventHandler(this.txtHeight_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(208, 28);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(11, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "x";
            // 
            // picImage
            // 
            this.picImage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picImage.Location = new System.Drawing.Point(12, 49);
            this.picImage.Name = "picImage";
            this.picImage.Size = new System.Drawing.Size(260, 196);
            this.picImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picImage.TabIndex = 5;
            this.picImage.TabStop = false;
            this.picImage.Visible = false;
            this.picImage.Paint += new System.Windows.Forms.PaintEventHandler(this.picImage_Paint);
            this.picImage.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseDown);
            this.picImage.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseMove);
            this.picImage.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseUp);
            // 
            // txtAspectRatio
            // 
            this.txtAspectRatio.Location = new System.Drawing.Point(88, 25);
            this.txtAspectRatio.Name = "txtAspectRatio";
            this.txtAspectRatio.Size = new System.Drawing.Size(46, 22);
            this.txtAspectRatio.TabIndex = 0;
            this.txtAspectRatio.Text = "4:3";
            this.txtAspectRatio.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtAspectRatio.TextChanged += new System.EventHandler(this.txtAspectRatio_TextChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(935, 24);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(207, 575);
            this.richTextBox1.TabIndex = 6;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1142, 599);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.txtAspectRatio);
            this.Controls.Add(this.picImage);
            this.Controls.Add(this.txtHeight);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtWidth);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "vcs_PictureCrop2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileOpen;
        private System.Windows.Forms.ToolStripMenuItem mnuFileSaveAs;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.SaveFileDialog sfdImage;
        private System.Windows.Forms.OpenFileDialog ofdImage;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtWidth;
        private System.Windows.Forms.TextBox txtHeight;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox picImage;
        private System.Windows.Forms.ToolStripMenuItem mnuScale;
        private System.Windows.Forms.ToolStripMenuItem mnuScale75;
        private System.Windows.Forms.ToolStripMenuItem mnuScale66;
        private System.Windows.Forms.ToolStripMenuItem mnuScale50;
        private System.Windows.Forms.ToolStripMenuItem mnuScale25;
        private System.Windows.Forms.ToolStripMenuItem mnuScale15;
        private System.Windows.Forms.ToolStripMenuItem mnuScale100;
        private System.Windows.Forms.TextBox txtAspectRatio;
        private System.Windows.Forms.ToolStripMenuItem rectangleToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuRectangleReset;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

