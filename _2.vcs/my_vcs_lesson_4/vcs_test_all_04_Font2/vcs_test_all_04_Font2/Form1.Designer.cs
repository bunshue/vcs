namespace vcs_test_all_04_Font2
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
            this.lstFonts = new System.Windows.Forms.ListBox();
            this.txtSample = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.chkStrikeout = new System.Windows.Forms.CheckBox();
            this.chkUnderline = new System.Windows.Forms.CheckBox();
            this.chkItalic = new System.Windows.Forms.CheckBox();
            this.chkBold = new System.Windows.Forms.CheckBox();
            this.txtSize = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // lstFonts
            // 
            this.lstFonts.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.lstFonts.FormattingEnabled = true;
            this.lstFonts.ItemHeight = 15;
            this.lstFonts.Location = new System.Drawing.Point(203, 14);
            this.lstFonts.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.lstFonts.Name = "lstFonts";
            this.lstFonts.Size = new System.Drawing.Size(189, 544);
            this.lstFonts.TabIndex = 0;
            this.lstFonts.SelectedIndexChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // txtSample
            // 
            this.txtSample.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtSample.Location = new System.Drawing.Point(401, 14);
            this.txtSample.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtSample.Multiline = true;
            this.txtSample.Name = "txtSample";
            this.txtSample.Size = new System.Drawing.Size(674, 547);
            this.txtSample.TabIndex = 1;
            this.txtSample.Text = "流水落花春去也，天上人間。ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^" +
                "&*()-=_+[]\\{}|;\':\",./<>?`~";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.groupBox1.Controls.Add(this.chkStrikeout);
            this.groupBox1.Controls.Add(this.chkUnderline);
            this.groupBox1.Controls.Add(this.chkItalic);
            this.groupBox1.Controls.Add(this.chkBold);
            this.groupBox1.Controls.Add(this.txtSize);
            this.groupBox1.Controls.Add(this.Label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 14);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.groupBox1.Size = new System.Drawing.Size(177, 548);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Properties";
            // 
            // chkStrikeout
            // 
            this.chkStrikeout.Location = new System.Drawing.Point(36, 142);
            this.chkStrikeout.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkStrikeout.Name = "chkStrikeout";
            this.chkStrikeout.Size = new System.Drawing.Size(117, 18);
            this.chkStrikeout.TabIndex = 11;
            this.chkStrikeout.Text = "Strikeout";
            this.chkStrikeout.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkUnderline
            // 
            this.chkUnderline.Location = new System.Drawing.Point(36, 114);
            this.chkUnderline.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkUnderline.Name = "chkUnderline";
            this.chkUnderline.Size = new System.Drawing.Size(117, 18);
            this.chkUnderline.TabIndex = 10;
            this.chkUnderline.Text = "Underline";
            this.chkUnderline.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkItalic
            // 
            this.chkItalic.Location = new System.Drawing.Point(36, 87);
            this.chkItalic.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkItalic.Name = "chkItalic";
            this.chkItalic.Size = new System.Drawing.Size(117, 18);
            this.chkItalic.TabIndex = 9;
            this.chkItalic.Text = "Italic";
            this.chkItalic.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkBold
            // 
            this.chkBold.Location = new System.Drawing.Point(36, 59);
            this.chkBold.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkBold.Name = "chkBold";
            this.chkBold.Size = new System.Drawing.Size(117, 18);
            this.chkBold.TabIndex = 8;
            this.chkBold.Text = "Bold";
            this.chkBold.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // txtSize
            // 
            this.txtSize.Location = new System.Drawing.Point(79, 22);
            this.txtSize.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtSize.Name = "txtSize";
            this.txtSize.Size = new System.Drawing.Size(41, 25);
            this.txtSize.TabIndex = 7;
            this.txtSize.Text = "30";
            this.txtSize.TextChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(25, 22);
            this.Label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(43, 18);
            this.Label1.TabIndex = 6;
            this.Label1.Text = "Size";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1092, 575);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.txtSample);
            this.Controls.Add(this.lstFonts);
            this.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.Name = "Form1";
            this.Text = "vcs_test_all_04_Font2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox lstFonts;
        private System.Windows.Forms.TextBox txtSample;
        private System.Windows.Forms.GroupBox groupBox1;
        internal System.Windows.Forms.CheckBox chkStrikeout;
        internal System.Windows.Forms.CheckBox chkUnderline;
        internal System.Windows.Forms.CheckBox chkItalic;
        internal System.Windows.Forms.CheckBox chkBold;
        internal System.Windows.Forms.TextBox txtSize;
        internal System.Windows.Forms.Label Label1;
    }
}

