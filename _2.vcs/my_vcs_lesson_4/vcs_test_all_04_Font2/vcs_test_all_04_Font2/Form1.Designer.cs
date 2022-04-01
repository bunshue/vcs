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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.chkStrikeout = new System.Windows.Forms.CheckBox();
            this.chkUnderline = new System.Windows.Forms.CheckBox();
            this.chkItalic = new System.Windows.Forms.CheckBox();
            this.chkBold = new System.Windows.Forms.CheckBox();
            this.txtSize = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // lstFonts
            // 
            this.lstFonts.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.lstFonts.FormattingEnabled = true;
            this.lstFonts.ItemHeight = 12;
            this.lstFonts.Location = new System.Drawing.Point(152, 11);
            this.lstFonts.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.lstFonts.Name = "lstFonts";
            this.lstFonts.Size = new System.Drawing.Size(143, 544);
            this.lstFonts.TabIndex = 0;
            this.lstFonts.SelectedIndexChanged += new System.EventHandler(this.SomethingChanged);
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
            this.groupBox1.Location = new System.Drawing.Point(9, 11);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox1.Size = new System.Drawing.Size(133, 292);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Properties";
            // 
            // chkStrikeout
            // 
            this.chkStrikeout.Location = new System.Drawing.Point(27, 114);
            this.chkStrikeout.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.chkStrikeout.Name = "chkStrikeout";
            this.chkStrikeout.Size = new System.Drawing.Size(88, 14);
            this.chkStrikeout.TabIndex = 11;
            this.chkStrikeout.Text = "Strikeout";
            this.chkStrikeout.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkUnderline
            // 
            this.chkUnderline.Location = new System.Drawing.Point(27, 91);
            this.chkUnderline.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.chkUnderline.Name = "chkUnderline";
            this.chkUnderline.Size = new System.Drawing.Size(88, 14);
            this.chkUnderline.TabIndex = 10;
            this.chkUnderline.Text = "Underline";
            this.chkUnderline.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkItalic
            // 
            this.chkItalic.Location = new System.Drawing.Point(27, 70);
            this.chkItalic.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.chkItalic.Name = "chkItalic";
            this.chkItalic.Size = new System.Drawing.Size(88, 14);
            this.chkItalic.TabIndex = 9;
            this.chkItalic.Text = "Italic";
            this.chkItalic.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // chkBold
            // 
            this.chkBold.Location = new System.Drawing.Point(27, 47);
            this.chkBold.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.chkBold.Name = "chkBold";
            this.chkBold.Size = new System.Drawing.Size(88, 14);
            this.chkBold.TabIndex = 8;
            this.chkBold.Text = "Bold";
            this.chkBold.CheckedChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // txtSize
            // 
            this.txtSize.Location = new System.Drawing.Point(59, 18);
            this.txtSize.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.txtSize.Name = "txtSize";
            this.txtSize.Size = new System.Drawing.Size(32, 22);
            this.txtSize.TabIndex = 7;
            this.txtSize.Text = "30";
            this.txtSize.TextChanged += new System.EventHandler(this.SomethingChanged);
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(19, 18);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(32, 14);
            this.Label1.TabIndex = 6;
            this.Label1.Text = "Size";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(9, 349);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(133, 65);
            this.button1.TabIndex = 3;
            this.button1.Text = "指明使用特定字型檔";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(301, 11);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(582, 544);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "流水落花春去也，天上人間。ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^" +
                "&*()-=_+[]\\{}|;\':\",./<>?`~\n";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(895, 573);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.lstFonts);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Form1";
            this.Text = "vcs_test_all_04_Font2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lstFonts;
        private System.Windows.Forms.GroupBox groupBox1;
        internal System.Windows.Forms.CheckBox chkStrikeout;
        internal System.Windows.Forms.CheckBox chkUnderline;
        internal System.Windows.Forms.CheckBox chkItalic;
        internal System.Windows.Forms.CheckBox chkBold;
        internal System.Windows.Forms.TextBox txtSize;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

