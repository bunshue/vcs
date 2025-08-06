namespace vcs_Scribble2
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.ofdFile = new System.Windows.Forms.OpenFileDialog();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileNew = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileOpen = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileSaveAs = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.editToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuEditCopy = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuEditCut = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuEditPaste = new System.Windows.Forms.ToolStripMenuItem();
            this.toolCustom = new System.Windows.Forms.ToolStripMenuItem();
            this.toolSolid = new System.Windows.Forms.ToolStripMenuItem();
            this.toolDot = new System.Windows.Forms.ToolStripMenuItem();
            this.toolDash = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStyle = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolRed = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick5 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolBlack = new System.Windows.Forms.ToolStripMenuItem();
            this.toolGreen = new System.Windows.Forms.ToolStripMenuItem();
            this.sfdFile = new System.Windows.Forms.SaveFileDialog();
            this.toolColor = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolBlue = new System.Windows.Forms.ToolStripMenuItem();
            this.toolOrange = new System.Windows.Forms.ToolStripMenuItem();
            this.toolYellow = new System.Windows.Forms.ToolStripMenuItem();
            this.toolLime = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.toolThick = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolThick1 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick2 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick3 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick4 = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.menuStrip1.SuspendLayout();
            this.toolStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // ofdFile
            // 
            this.ofdFile.FileName = "openFileDialog1";
            this.ofdFile.Filter = "Polyline Files|*.pln|All Files|*.*";
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(12, 52);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(260, 200);
            this.picCanvas.TabIndex = 12;
            this.picCanvas.TabStop = false;
            this.picCanvas.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseMove);
            this.picCanvas.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseDown);
            this.picCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            this.picCanvas.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseUp);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.editToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(284, 24);
            this.menuStrip1.TabIndex = 13;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileNew,
            this.mnuFileOpen,
            this.mnuFileSaveAs,
            this.toolStripMenuItem1,
            this.mnuFileExit});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileNew
            // 
            this.mnuFileNew.Name = "mnuFileNew";
            this.mnuFileNew.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.mnuFileNew.Size = new System.Drawing.Size(163, 22);
            this.mnuFileNew.Text = "&New";
            this.mnuFileNew.Click += new System.EventHandler(this.mnuFileNew_Click);
            // 
            // mnuFileOpen
            // 
            this.mnuFileOpen.Name = "mnuFileOpen";
            this.mnuFileOpen.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
            this.mnuFileOpen.Size = new System.Drawing.Size(163, 22);
            this.mnuFileOpen.Text = "&Open...";
            this.mnuFileOpen.Click += new System.EventHandler(this.mnuFileOpen_Click);
            // 
            // mnuFileSaveAs
            // 
            this.mnuFileSaveAs.Name = "mnuFileSaveAs";
            this.mnuFileSaveAs.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.mnuFileSaveAs.Size = new System.Drawing.Size(163, 22);
            this.mnuFileSaveAs.Text = "Save &As...";
            this.mnuFileSaveAs.Click += new System.EventHandler(this.mnuFileSaveAs_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(160, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(163, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // editToolStripMenuItem
            // 
            this.editToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuEditCopy,
            this.mnuEditCut,
            this.mnuEditPaste});
            this.editToolStripMenuItem.Name = "editToolStripMenuItem";
            this.editToolStripMenuItem.Size = new System.Drawing.Size(39, 20);
            this.editToolStripMenuItem.Text = "&Edit";
            // 
            // mnuEditCopy
            // 
            this.mnuEditCopy.Name = "mnuEditCopy";
            this.mnuEditCopy.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
            this.mnuEditCopy.Size = new System.Drawing.Size(152, 22);
            this.mnuEditCopy.Text = "&Copy";
            this.mnuEditCopy.Click += new System.EventHandler(this.mnuEditCopy_Click);
            // 
            // mnuEditCut
            // 
            this.mnuEditCut.Name = "mnuEditCut";
            this.mnuEditCut.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.X)));
            this.mnuEditCut.Size = new System.Drawing.Size(152, 22);
            this.mnuEditCut.Text = "C&ut";
            this.mnuEditCut.Click += new System.EventHandler(this.mnuEditCut_Click);
            // 
            // mnuEditPaste
            // 
            this.mnuEditPaste.Name = "mnuEditPaste";
            this.mnuEditPaste.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
            this.mnuEditPaste.Size = new System.Drawing.Size(152, 22);
            this.mnuEditPaste.Text = "&Paste";
            this.mnuEditPaste.Click += new System.EventHandler(this.mnuEditPaste_Click);
            // 
            // toolCustom
            // 
            this.toolCustom.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolCustom.Image = global::vcs_Scribble2.Properties.Resources.custom_dash;
            this.toolCustom.Name = "toolCustom";
            this.toolCustom.Size = new System.Drawing.Size(152, 22);
            this.toolCustom.Text = "Custom";
            this.toolCustom.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolSolid
            // 
            this.toolSolid.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolSolid.Image = global::vcs_Scribble2.Properties.Resources.solid;
            this.toolSolid.Name = "toolSolid";
            this.toolSolid.Size = new System.Drawing.Size(152, 22);
            this.toolSolid.Text = "Solid";
            this.toolSolid.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolDot
            // 
            this.toolDot.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolDot.Image = global::vcs_Scribble2.Properties.Resources.dot;
            this.toolDot.Name = "toolDot";
            this.toolDot.Size = new System.Drawing.Size(152, 22);
            this.toolDot.Text = "Dot";
            this.toolDot.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolDash
            // 
            this.toolDash.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolDash.Image = global::vcs_Scribble2.Properties.Resources.dash;
            this.toolDash.Name = "toolDash";
            this.toolDash.Size = new System.Drawing.Size(152, 22);
            this.toolDash.Text = "Dash";
            this.toolDash.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolStyle
            // 
            this.toolStyle.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStyle.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolSolid,
            this.toolDash,
            this.toolDot,
            this.toolCustom});
            this.toolStyle.Image = ((System.Drawing.Image)(resources.GetObject("toolStyle.Image")));
            this.toolStyle.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStyle.Name = "toolStyle";
            this.toolStyle.Size = new System.Drawing.Size(29, 22);
            this.toolStyle.Text = "toolStripDropDownButton1";
            // 
            // toolRed
            // 
            this.toolRed.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolRed.ForeColor = System.Drawing.Color.Red;
            this.toolRed.Image = global::vcs_Scribble2.Properties.Resources.red;
            this.toolRed.Name = "toolRed";
            this.toolRed.Size = new System.Drawing.Size(152, 22);
            this.toolRed.Text = "Red";
            this.toolRed.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolThick5
            // 
            this.toolThick5.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick5.Image = global::vcs_Scribble2.Properties.Resources.line5;
            this.toolThick5.Name = "toolThick5";
            this.toolThick5.Size = new System.Drawing.Size(152, 22);
            this.toolThick5.Text = "5";
            this.toolThick5.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolBlack
            // 
            this.toolBlack.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolBlack.ForeColor = System.Drawing.Color.Black;
            this.toolBlack.Image = global::vcs_Scribble2.Properties.Resources.black;
            this.toolBlack.Name = "toolBlack";
            this.toolBlack.Size = new System.Drawing.Size(152, 22);
            this.toolBlack.Text = "Black";
            this.toolBlack.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolGreen
            // 
            this.toolGreen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolGreen.ForeColor = System.Drawing.Color.Green;
            this.toolGreen.Image = global::vcs_Scribble2.Properties.Resources.green;
            this.toolGreen.Name = "toolGreen";
            this.toolGreen.Size = new System.Drawing.Size(152, 22);
            this.toolGreen.Text = "Green";
            this.toolGreen.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // sfdFile
            // 
            this.sfdFile.Filter = "Polyline Files|*.pln|All Files|*.*";
            // 
            // toolColor
            // 
            this.toolColor.BackColor = System.Drawing.SystemColors.ControlDark;
            this.toolColor.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolColor.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolBlack,
            this.toolRed,
            this.toolGreen,
            this.toolBlue,
            this.toolOrange,
            this.toolYellow,
            this.toolLime});
            this.toolColor.ForeColor = System.Drawing.Color.Black;
            this.toolColor.Image = ((System.Drawing.Image)(resources.GetObject("toolColor.Image")));
            this.toolColor.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolColor.Name = "toolColor";
            this.toolColor.Size = new System.Drawing.Size(29, 22);
            this.toolColor.Text = "toolStripDropDownButton1";
            // 
            // toolBlue
            // 
            this.toolBlue.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolBlue.ForeColor = System.Drawing.Color.Blue;
            this.toolBlue.Image = global::vcs_Scribble2.Properties.Resources.blue;
            this.toolBlue.Name = "toolBlue";
            this.toolBlue.Size = new System.Drawing.Size(152, 22);
            this.toolBlue.Text = "Blue";
            this.toolBlue.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolOrange
            // 
            this.toolOrange.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolOrange.ForeColor = System.Drawing.Color.Orange;
            this.toolOrange.Image = global::vcs_Scribble2.Properties.Resources.orange;
            this.toolOrange.Name = "toolOrange";
            this.toolOrange.Size = new System.Drawing.Size(152, 22);
            this.toolOrange.Text = "Orange";
            this.toolOrange.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolYellow
            // 
            this.toolYellow.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolYellow.ForeColor = System.Drawing.Color.Yellow;
            this.toolYellow.Image = global::vcs_Scribble2.Properties.Resources.yellow;
            this.toolYellow.Name = "toolYellow";
            this.toolYellow.Size = new System.Drawing.Size(152, 22);
            this.toolYellow.Text = "Yellow";
            this.toolYellow.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolLime
            // 
            this.toolLime.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolLime.ForeColor = System.Drawing.Color.Lime;
            this.toolLime.Image = global::vcs_Scribble2.Properties.Resources.lime;
            this.toolLime.Name = "toolLime";
            this.toolLime.Size = new System.Drawing.Size(152, 22);
            this.toolLime.Text = "Lime";
            this.toolLime.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolColor,
            this.toolThick,
            this.toolStyle});
            this.toolStrip1.Location = new System.Drawing.Point(0, 24);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(284, 25);
            this.toolStrip1.TabIndex = 11;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // toolThick
            // 
            this.toolThick.BackColor = System.Drawing.SystemColors.ControlDark;
            this.toolThick.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolThick1,
            this.toolThick2,
            this.toolThick3,
            this.toolThick4,
            this.toolThick5});
            this.toolThick.Image = ((System.Drawing.Image)(resources.GetObject("toolThick.Image")));
            this.toolThick.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolThick.Name = "toolThick";
            this.toolThick.Size = new System.Drawing.Size(29, 22);
            this.toolThick.Text = "toolStripDropDownButton1";
            // 
            // toolThick1
            // 
            this.toolThick1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick1.Image = global::vcs_Scribble2.Properties.Resources.line1;
            this.toolThick1.Name = "toolThick1";
            this.toolThick1.Size = new System.Drawing.Size(152, 22);
            this.toolThick1.Text = "1";
            this.toolThick1.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick2
            // 
            this.toolThick2.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick2.Image = global::vcs_Scribble2.Properties.Resources.line2;
            this.toolThick2.Name = "toolThick2";
            this.toolThick2.Size = new System.Drawing.Size(152, 22);
            this.toolThick2.Text = "2";
            this.toolThick2.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick3
            // 
            this.toolThick3.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick3.Image = global::vcs_Scribble2.Properties.Resources.line3;
            this.toolThick3.Name = "toolThick3";
            this.toolThick3.Size = new System.Drawing.Size(152, 22);
            this.toolThick3.Text = "3";
            this.toolThick3.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick4
            // 
            this.toolThick4.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick4.Image = global::vcs_Scribble2.Properties.Resources.line4;
            this.toolThick4.Name = "toolThick4";
            this.toolThick4.Size = new System.Drawing.Size(152, 22);
            this.toolThick4.Text = "4";
            this.toolThick4.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 264);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.menuStrip1);
            this.Name = "Form1";
            this.Text = "vcs_Scribble2";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.OpenFileDialog ofdFile;
        private System.Windows.Forms.PictureBox picCanvas;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileNew;
        private System.Windows.Forms.ToolStripMenuItem mnuFileOpen;
        private System.Windows.Forms.ToolStripMenuItem mnuFileSaveAs;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.ToolStripMenuItem editToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuEditCopy;
        private System.Windows.Forms.ToolStripMenuItem mnuEditCut;
        private System.Windows.Forms.ToolStripMenuItem mnuEditPaste;
        private System.Windows.Forms.ToolStripMenuItem toolCustom;
        private System.Windows.Forms.ToolStripMenuItem toolSolid;
        private System.Windows.Forms.ToolStripMenuItem toolDot;
        private System.Windows.Forms.ToolStripMenuItem toolDash;
        private System.Windows.Forms.ToolStripDropDownButton toolStyle;
        private System.Windows.Forms.ToolStripMenuItem toolRed;
        private System.Windows.Forms.ToolStripMenuItem toolThick5;
        private System.Windows.Forms.ToolStripMenuItem toolBlack;
        private System.Windows.Forms.ToolStripMenuItem toolGreen;
        private System.Windows.Forms.SaveFileDialog sfdFile;
        private System.Windows.Forms.ToolStripDropDownButton toolColor;
        private System.Windows.Forms.ToolStripMenuItem toolBlue;
        private System.Windows.Forms.ToolStripMenuItem toolOrange;
        private System.Windows.Forms.ToolStripMenuItem toolYellow;
        private System.Windows.Forms.ToolStripMenuItem toolLime;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripDropDownButton toolThick;
        private System.Windows.Forms.ToolStripMenuItem toolThick1;
        private System.Windows.Forms.ToolStripMenuItem toolThick2;
        private System.Windows.Forms.ToolStripMenuItem toolThick3;
        private System.Windows.Forms.ToolStripMenuItem toolThick4;
    }
}

