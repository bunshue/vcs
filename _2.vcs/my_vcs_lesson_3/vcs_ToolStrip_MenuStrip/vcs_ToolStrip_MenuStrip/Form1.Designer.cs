namespace vcs_ToolStrip_MenuStrip
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
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.toolColor = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolBlack = new System.Windows.Forms.ToolStripMenuItem();
            this.toolRed = new System.Windows.Forms.ToolStripMenuItem();
            this.toolGreen = new System.Windows.Forms.ToolStripMenuItem();
            this.toolBlue = new System.Windows.Forms.ToolStripMenuItem();
            this.toolOrange = new System.Windows.Forms.ToolStripMenuItem();
            this.toolYellow = new System.Windows.Forms.ToolStripMenuItem();
            this.toolLime = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolThick1 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick2 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick3 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick4 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolThick5 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStyle = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolSolid = new System.Windows.Forms.ToolStripMenuItem();
            this.toolDash = new System.Windows.Forms.ToolStripMenuItem();
            this.toolDot = new System.Windows.Forms.ToolStripMenuItem();
            this.toolCustom = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileNew = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.toolStrip1.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolColor,
            this.toolThick,
            this.toolStyle});
            this.toolStrip1.Location = new System.Drawing.Point(0, 24);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(731, 25);
            this.toolStrip1.TabIndex = 2;
            this.toolStrip1.Text = "toolStrip1";
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
            // toolBlack
            // 
            this.toolBlack.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolBlack.ForeColor = System.Drawing.Color.Black;
            this.toolBlack.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.black;
            this.toolBlack.Name = "toolBlack";
            this.toolBlack.Size = new System.Drawing.Size(117, 22);
            this.toolBlack.Text = "Black";
            this.toolBlack.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolRed
            // 
            this.toolRed.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolRed.ForeColor = System.Drawing.Color.Red;
            this.toolRed.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.red;
            this.toolRed.Name = "toolRed";
            this.toolRed.Size = new System.Drawing.Size(117, 22);
            this.toolRed.Text = "Red";
            this.toolRed.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolGreen
            // 
            this.toolGreen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolGreen.ForeColor = System.Drawing.Color.Green;
            this.toolGreen.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.green;
            this.toolGreen.Name = "toolGreen";
            this.toolGreen.Size = new System.Drawing.Size(117, 22);
            this.toolGreen.Text = "Green";
            this.toolGreen.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolBlue
            // 
            this.toolBlue.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolBlue.ForeColor = System.Drawing.Color.Blue;
            this.toolBlue.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.blue;
            this.toolBlue.Name = "toolBlue";
            this.toolBlue.Size = new System.Drawing.Size(117, 22);
            this.toolBlue.Text = "Blue";
            this.toolBlue.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolOrange
            // 
            this.toolOrange.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolOrange.ForeColor = System.Drawing.Color.Orange;
            this.toolOrange.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.orange;
            this.toolOrange.Name = "toolOrange";
            this.toolOrange.Size = new System.Drawing.Size(117, 22);
            this.toolOrange.Text = "Orange";
            this.toolOrange.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolYellow
            // 
            this.toolYellow.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolYellow.ForeColor = System.Drawing.Color.Yellow;
            this.toolYellow.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.yellow;
            this.toolYellow.Name = "toolYellow";
            this.toolYellow.Size = new System.Drawing.Size(117, 22);
            this.toolYellow.Text = "Yellow";
            this.toolYellow.Click += new System.EventHandler(this.ColorTool_Click);
            // 
            // toolLime
            // 
            this.toolLime.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolLime.ForeColor = System.Drawing.Color.Lime;
            this.toolLime.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.lime;
            this.toolLime.Name = "toolLime";
            this.toolLime.Size = new System.Drawing.Size(117, 22);
            this.toolLime.Text = "Lime";
            this.toolLime.Click += new System.EventHandler(this.ColorTool_Click);
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
            this.toolThick1.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.line1;
            this.toolThick1.Name = "toolThick1";
            this.toolThick1.Size = new System.Drawing.Size(81, 22);
            this.toolThick1.Text = "1";
            this.toolThick1.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick2
            // 
            this.toolThick2.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick2.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.line2;
            this.toolThick2.Name = "toolThick2";
            this.toolThick2.Size = new System.Drawing.Size(81, 22);
            this.toolThick2.Text = "2";
            this.toolThick2.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick3
            // 
            this.toolThick3.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick3.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.line3;
            this.toolThick3.Name = "toolThick3";
            this.toolThick3.Size = new System.Drawing.Size(81, 22);
            this.toolThick3.Text = "3";
            this.toolThick3.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick4
            // 
            this.toolThick4.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick4.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.line4;
            this.toolThick4.Name = "toolThick4";
            this.toolThick4.Size = new System.Drawing.Size(81, 22);
            this.toolThick4.Text = "4";
            this.toolThick4.Click += new System.EventHandler(this.ThicknessTool_Click);
            // 
            // toolThick5
            // 
            this.toolThick5.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolThick5.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.line5;
            this.toolThick5.Name = "toolThick5";
            this.toolThick5.Size = new System.Drawing.Size(81, 22);
            this.toolThick5.Text = "5";
            this.toolThick5.Click += new System.EventHandler(this.ThicknessTool_Click);
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
            // toolSolid
            // 
            this.toolSolid.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolSolid.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.solid;
            this.toolSolid.Name = "toolSolid";
            this.toolSolid.Size = new System.Drawing.Size(117, 22);
            this.toolSolid.Text = "Solid";
            this.toolSolid.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolDash
            // 
            this.toolDash.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolDash.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.dash;
            this.toolDash.Name = "toolDash";
            this.toolDash.Size = new System.Drawing.Size(117, 22);
            this.toolDash.Text = "Dash";
            this.toolDash.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolDot
            // 
            this.toolDot.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolDot.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.dot;
            this.toolDot.Name = "toolDot";
            this.toolDot.Size = new System.Drawing.Size(117, 22);
            this.toolDot.Text = "Dot";
            this.toolDot.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // toolCustom
            // 
            this.toolCustom.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolCustom.Image = global::vcs_ToolStrip_MenuStrip.Properties.Resources.custom_dash;
            this.toolCustom.Name = "toolCustom";
            this.toolCustom.Size = new System.Drawing.Size(117, 22);
            this.toolCustom.Text = "Custom";
            this.toolCustom.Click += new System.EventHandler(this.StyleTool_Click);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(731, 24);
            this.menuStrip1.TabIndex = 4;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileNew,
            this.toolStripMenuItem1,
            this.mnuFileExit});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(38, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileNew
            // 
            this.mnuFileNew.Name = "mnuFileNew";
            this.mnuFileNew.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.mnuFileNew.Size = new System.Drawing.Size(152, 22);
            this.mnuFileNew.Text = "&New";
            this.mnuFileNew.Click += new System.EventHandler(this.mnuFileNew_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(149, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(152, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 333);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(707, 241);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(731, 586);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "vcs_ToolStrip_MenuStrip";
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripDropDownButton toolColor;
        private System.Windows.Forms.ToolStripMenuItem toolBlack;
        private System.Windows.Forms.ToolStripMenuItem toolRed;
        private System.Windows.Forms.ToolStripMenuItem toolGreen;
        private System.Windows.Forms.ToolStripMenuItem toolBlue;
        private System.Windows.Forms.ToolStripMenuItem toolOrange;
        private System.Windows.Forms.ToolStripMenuItem toolYellow;
        private System.Windows.Forms.ToolStripDropDownButton toolThick;
        private System.Windows.Forms.ToolStripMenuItem toolThick1;
        private System.Windows.Forms.ToolStripMenuItem toolThick2;
        private System.Windows.Forms.ToolStripMenuItem toolThick3;
        private System.Windows.Forms.ToolStripMenuItem toolThick4;
        private System.Windows.Forms.ToolStripMenuItem toolThick5;
        private System.Windows.Forms.ToolStripMenuItem toolLime;
        private System.Windows.Forms.ToolStripDropDownButton toolStyle;
        private System.Windows.Forms.ToolStripMenuItem toolSolid;
        private System.Windows.Forms.ToolStripMenuItem toolDash;
        private System.Windows.Forms.ToolStripMenuItem toolDot;
        private System.Windows.Forms.ToolStripMenuItem toolCustom;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileNew;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.RichTextBox richTextBox1;

    }
}

