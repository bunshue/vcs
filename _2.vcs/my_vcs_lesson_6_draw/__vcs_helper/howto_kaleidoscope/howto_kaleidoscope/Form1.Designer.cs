namespace howto_kaleidoscope
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
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileNew = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyle = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleReflectX = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleReflectY = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleReflectXY = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleRotate2 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleRotate4 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuStyleRotate8 = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(12, 25);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(498, 381);
            this.picCanvas.TabIndex = 0;
            this.picCanvas.TabStop = false;
            this.picCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            this.picCanvas.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseDown);
            this.picCanvas.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseMove);
            this.picCanvas.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseUp);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.mnuStyle});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(522, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileNew,
            this.toolStripMenuItem1,
            this.mnuFileExit});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(39, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileNew
            // 
            this.mnuFileNew.Name = "mnuFileNew";
            this.mnuFileNew.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.mnuFileNew.Size = new System.Drawing.Size(148, 22);
            this.mnuFileNew.Text = "&New";
            this.mnuFileNew.Click += new System.EventHandler(this.mnuFileNew_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(145, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(148, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // mnuStyle
            // 
            this.mnuStyle.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuStyleReflectX,
            this.mnuStyleReflectY,
            this.mnuStyleReflectXY,
            this.mnuStyleRotate2,
            this.mnuStyleRotate4,
            this.mnuStyleRotate8});
            this.mnuStyle.Name = "mnuStyle";
            this.mnuStyle.Size = new System.Drawing.Size(47, 20);
            this.mnuStyle.Text = "&Style";
            // 
            // mnuStyleReflectX
            // 
            this.mnuStyleReflectX.Checked = true;
            this.mnuStyleReflectX.CheckState = System.Windows.Forms.CheckState.Checked;
            this.mnuStyleReflectX.Name = "mnuStyleReflectX";
            this.mnuStyleReflectX.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleReflectX.Text = "Reflect &X";
            this.mnuStyleReflectX.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // mnuStyleReflectY
            // 
            this.mnuStyleReflectY.Name = "mnuStyleReflectY";
            this.mnuStyleReflectY.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleReflectY.Text = "Reflect &Y";
            this.mnuStyleReflectY.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // mnuStyleReflectXY
            // 
            this.mnuStyleReflectXY.Name = "mnuStyleReflectXY";
            this.mnuStyleReflectXY.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleReflectXY.Text = "Reflect XY";
            this.mnuStyleReflectXY.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // mnuStyleRotate2
            // 
            this.mnuStyleRotate2.Name = "mnuStyleRotate2";
            this.mnuStyleRotate2.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleRotate2.Text = "Rotate &2";
            this.mnuStyleRotate2.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // mnuStyleRotate4
            // 
            this.mnuStyleRotate4.Name = "mnuStyleRotate4";
            this.mnuStyleRotate4.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleRotate4.Text = "Rotate &4";
            this.mnuStyleRotate4.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // mnuStyleRotate8
            // 
            this.mnuStyleRotate8.Name = "mnuStyleRotate8";
            this.mnuStyleRotate8.Size = new System.Drawing.Size(133, 22);
            this.mnuStyleRotate8.Text = "Rotate &8";
            this.mnuStyleRotate8.Click += new System.EventHandler(this.mnuStyle_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(522, 417);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "howto_kaleidoscope";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picCanvas;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileNew;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.ToolStripMenuItem mnuStyle;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleReflectX;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleReflectY;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleReflectXY;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleRotate2;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleRotate4;
        private System.Windows.Forms.ToolStripMenuItem mnuStyleRotate8;
    }
}

