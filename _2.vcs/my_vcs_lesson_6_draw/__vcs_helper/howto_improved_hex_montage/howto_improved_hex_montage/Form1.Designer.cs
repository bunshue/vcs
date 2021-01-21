namespace howto_improved_hex_montage
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileOpenDirectoryFiles = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileSaveAs = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.sfdSave = new System.Windows.Forms.SaveFileDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.txtHexHeight = new System.Windows.Forms.TextBox();
            this.ofdFile = new System.Windows.Forms.OpenFileDialog();
            this.txtBorderThickness = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.picBorderColor = new System.Windows.Forms.PictureBox();
            this.cdBorderColor = new System.Windows.Forms.ColorDialog();
            this.picBackgroundColor = new System.Windows.Forms.PictureBox();
            this.label4 = new System.Windows.Forms.Label();
            this.ofdDirectoryFiles = new System.Windows.Forms.OpenFileDialog();
            this.panel1 = new System.Windows.Forms.Panel();
            this.txtNumCols = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.txtNumRows = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.btnCreateGrid = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBorderColor)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBackgroundColor)).BeginInit();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.Location = new System.Drawing.Point(0, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(190, 163);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Visible = false;
            this.pictureBox1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseClick);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1188, 24);
            this.menuStrip1.TabIndex = 2;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileOpenDirectoryFiles,
            this.mnuFileSaveAs,
            this.toolStripMenuItem1,
            this.mnuFileExit});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(39, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileOpenDirectoryFiles
            // 
            this.mnuFileOpenDirectoryFiles.Name = "mnuFileOpenDirectoryFiles";
            this.mnuFileOpenDirectoryFiles.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
            this.mnuFileOpenDirectoryFiles.Size = new System.Drawing.Size(257, 22);
            this.mnuFileOpenDirectoryFiles.Text = "&Open Files in Directory...";
            this.mnuFileOpenDirectoryFiles.Click += new System.EventHandler(this.mnuFileOpenDirectoryFiles_Click);
            // 
            // mnuFileSaveAs
            // 
            this.mnuFileSaveAs.Enabled = false;
            this.mnuFileSaveAs.Name = "mnuFileSaveAs";
            this.mnuFileSaveAs.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.mnuFileSaveAs.Size = new System.Drawing.Size(257, 22);
            this.mnuFileSaveAs.Text = "&Save As...";
            this.mnuFileSaveAs.Click += new System.EventHandler(this.mnuFileSaveAs_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(254, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(257, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // sfdSave
            // 
            this.sfdSave.DefaultExt = "png";
            this.sfdSave.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 12);
            this.label1.TabIndex = 3;
            this.label1.Text = "Hex Height:";
            // 
            // txtHexHeight
            // 
            this.txtHexHeight.Location = new System.Drawing.Point(111, 25);
            this.txtHexHeight.Name = "txtHexHeight";
            this.txtHexHeight.Size = new System.Drawing.Size(43, 22);
            this.txtHexHeight.TabIndex = 4;
            this.txtHexHeight.Text = "200";
            this.txtHexHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtHexHeight.TextChanged += new System.EventHandler(this.txt_TextChanged);
            // 
            // ofdFile
            // 
            this.ofdFile.DefaultExt = "png";
            this.ofdFile.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // txtBorderThickness
            // 
            this.txtBorderThickness.Location = new System.Drawing.Point(111, 49);
            this.txtBorderThickness.Name = "txtBorderThickness";
            this.txtBorderThickness.Size = new System.Drawing.Size(43, 22);
            this.txtBorderThickness.TabIndex = 6;
            this.txtBorderThickness.Text = "5";
            this.txtBorderThickness.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtBorderThickness.TextChanged += new System.EventHandler(this.txt_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 52);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(90, 12);
            this.label2.TabIndex = 5;
            this.label2.Text = "Border Thickness:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(300, 28);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(71, 12);
            this.label3.TabIndex = 7;
            this.label3.Text = "Border Color:";
            // 
            // picBorderColor
            // 
            this.picBorderColor.BackColor = System.Drawing.Color.Red;
            this.picBorderColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picBorderColor.Location = new System.Drawing.Point(374, 25);
            this.picBorderColor.Name = "picBorderColor";
            this.picBorderColor.Size = new System.Drawing.Size(43, 19);
            this.picBorderColor.TabIndex = 8;
            this.picBorderColor.TabStop = false;
            this.picBorderColor.Click += new System.EventHandler(this.picBorderColor_Click);
            // 
            // picBackgroundColor
            // 
            this.picBackgroundColor.BackColor = System.Drawing.Color.LightGreen;
            this.picBackgroundColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picBackgroundColor.Location = new System.Drawing.Point(374, 49);
            this.picBackgroundColor.Name = "picBackgroundColor";
            this.picBackgroundColor.Size = new System.Drawing.Size(43, 19);
            this.picBackgroundColor.TabIndex = 10;
            this.picBackgroundColor.TabStop = false;
            this.picBackgroundColor.Click += new System.EventHandler(this.picBackgroundColor_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(300, 52);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(54, 12);
            this.label4.TabIndex = 9;
            this.label4.Text = "BG Color:";
            // 
            // ofdDirectoryFiles
            // 
            this.ofdDirectoryFiles.DefaultExt = "png";
            this.ofdDirectoryFiles.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // panel1
            // 
            this.panel1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.panel1.AutoScroll = true;
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Location = new System.Drawing.Point(12, 73);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(963, 730);
            this.panel1.TabIndex = 11;
            // 
            // txtNumCols
            // 
            this.txtNumCols.Location = new System.Drawing.Point(239, 49);
            this.txtNumCols.Name = "txtNumCols";
            this.txtNumCols.Size = new System.Drawing.Size(43, 22);
            this.txtNumCols.TabIndex = 15;
            this.txtNumCols.Text = "5";
            this.txtNumCols.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(173, 52);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(59, 12);
            this.label5.TabIndex = 14;
            this.label5.Text = "# Columns:";
            // 
            // txtNumRows
            // 
            this.txtNumRows.Location = new System.Drawing.Point(239, 25);
            this.txtNumRows.Name = "txtNumRows";
            this.txtNumRows.Size = new System.Drawing.Size(43, 22);
            this.txtNumRows.TabIndex = 13;
            this.txtNumRows.Text = "4";
            this.txtNumRows.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(173, 28);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(43, 12);
            this.label6.TabIndex = 12;
            this.label6.Text = "# Rows:";
            // 
            // btnCreateGrid
            // 
            this.btnCreateGrid.Location = new System.Drawing.Point(436, 34);
            this.btnCreateGrid.Name = "btnCreateGrid";
            this.btnCreateGrid.Size = new System.Drawing.Size(75, 21);
            this.btnCreateGrid.TabIndex = 16;
            this.btnCreateGrid.Text = "Create Grid";
            this.btnCreateGrid.UseVisualStyleBackColor = true;
            this.btnCreateGrid.Click += new System.EventHandler(this.btnCreateGrid_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(981, 73);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(195, 730);
            this.richTextBox1.TabIndex = 17;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(529, 34);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 21);
            this.button1.TabIndex = 18;
            this.button1.Text = "Setup Folder";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnCreateGrid;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1188, 814);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnCreateGrid);
            this.Controls.Add(this.txtNumCols);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.txtNumRows);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.picBackgroundColor);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.picBorderColor);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtBorderThickness);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtHexHeight);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "howto_improved_hex_montage";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBorderColor)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBackgroundColor)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mnuFileSaveAs;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.SaveFileDialog sfdSave;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtHexHeight;
        private System.Windows.Forms.OpenFileDialog ofdFile;
        private System.Windows.Forms.TextBox txtBorderThickness;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox picBorderColor;
        private System.Windows.Forms.ColorDialog cdBorderColor;
        private System.Windows.Forms.PictureBox picBackgroundColor;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ToolStripMenuItem mnuFileOpenDirectoryFiles;
        private System.Windows.Forms.OpenFileDialog ofdDirectoryFiles;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.TextBox txtNumCols;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtNumRows;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button btnCreateGrid;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}

