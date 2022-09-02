namespace howto_password_tracker
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
            this.components = new System.ComponentModel.Container();
            this.ToolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.dgvPasswords = new System.Windows.Forms.DataGridView();
            this.colName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colUsername = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colPassword = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colChangedDate = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colCopy = new System.Windows.Forms.DataGridViewButtonColumn();
            this.colNew = new System.Windows.Forms.DataGridViewButtonColumn();
            this.MenuStrip1 = new System.Windows.Forms.MenuStrip();
            this.FileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuFileChangeMasterPassword = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuFileExit = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.dgvPasswords)).BeginInit();
            this.MenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // dgvPasswords
            // 
            this.dgvPasswords.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dgvPasswords.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvPasswords.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.colName,
            this.colUsername,
            this.colPassword,
            this.colChangedDate,
            this.colCopy,
            this.colNew});
            this.dgvPasswords.Location = new System.Drawing.Point(1, 25);
            this.dgvPasswords.Name = "dgvPasswords";
            this.dgvPasswords.Size = new System.Drawing.Size(479, 321);
            this.dgvPasswords.TabIndex = 14;
            this.dgvPasswords.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvPasswords_CellContentClick);
            this.dgvPasswords.CellEndEdit += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvPasswords_CellEndEdit);
            // 
            // colName
            // 
            this.colName.HeaderText = "Name";
            this.colName.Name = "colName";
            this.colName.Width = 150;
            // 
            // colUsername
            // 
            this.colUsername.HeaderText = "Username";
            this.colUsername.Name = "colUsername";
            // 
            // colPassword
            // 
            this.colPassword.HeaderText = "Password";
            this.colPassword.Name = "colPassword";
            this.colPassword.Width = 150;
            // 
            // colChangedDate
            // 
            this.colChangedDate.HeaderText = "Changed Date";
            this.colChangedDate.Name = "colChangedDate";
            this.colChangedDate.ReadOnly = true;
            this.colChangedDate.Width = 150;
            // 
            // colCopy
            // 
            this.colCopy.HeaderText = "Copy";
            this.colCopy.Name = "colCopy";
            this.colCopy.Resizable = System.Windows.Forms.DataGridViewTriState.False;
            this.colCopy.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.Automatic;
            this.colCopy.Width = 40;
            // 
            // colNew
            // 
            this.colNew.HeaderText = "New";
            this.colNew.Name = "colNew";
            this.colNew.Resizable = System.Windows.Forms.DataGridViewTriState.False;
            this.colNew.Width = 40;
            // 
            // MenuStrip1
            // 
            this.MenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.FileToolStripMenuItem});
            this.MenuStrip1.Location = new System.Drawing.Point(0, 0);
            this.MenuStrip1.Name = "MenuStrip1";
            this.MenuStrip1.Size = new System.Drawing.Size(481, 24);
            this.MenuStrip1.TabIndex = 13;
            this.MenuStrip1.Text = "MenuStrip1";
            // 
            // FileToolStripMenuItem
            // 
            this.FileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuFileChangeMasterPassword,
            this.ToolStripMenuItem1,
            this.mnuFileExit});
            this.FileToolStripMenuItem.Name = "FileToolStripMenuItem";
            this.FileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.FileToolStripMenuItem.Text = "&File";
            // 
            // mnuFileChangeMasterPassword
            // 
            this.mnuFileChangeMasterPassword.Name = "mnuFileChangeMasterPassword";
            this.mnuFileChangeMasterPassword.Size = new System.Drawing.Size(207, 22);
            this.mnuFileChangeMasterPassword.Text = "Change Master Password";
            this.mnuFileChangeMasterPassword.Click += new System.EventHandler(this.mnuFileChangeMasterPassword_Click);
            // 
            // ToolStripMenuItem1
            // 
            this.ToolStripMenuItem1.Name = "ToolStripMenuItem1";
            this.ToolStripMenuItem1.Size = new System.Drawing.Size(204, 6);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Name = "mnuFileExit";
            this.mnuFileExit.Size = new System.Drawing.Size(207, 22);
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(481, 347);
            this.Controls.Add(this.dgvPasswords);
            this.Controls.Add(this.MenuStrip1);
            this.KeyPreview = true;
            this.Name = "Form1";
            this.Text = "PasswordTracker";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.dgvPasswords)).EndInit();
            this.MenuStrip1.ResumeLayout(false);
            this.MenuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.ToolTip ToolTip1;
        internal System.Windows.Forms.DataGridView dgvPasswords;
        internal System.Windows.Forms.MenuStrip MenuStrip1;
        internal System.Windows.Forms.ToolStripMenuItem FileToolStripMenuItem;
        internal System.Windows.Forms.ToolStripMenuItem mnuFileChangeMasterPassword;
        internal System.Windows.Forms.ToolStripSeparator ToolStripMenuItem1;
        internal System.Windows.Forms.ToolStripMenuItem mnuFileExit;
        private System.Windows.Forms.DataGridViewTextBoxColumn colName;
        private System.Windows.Forms.DataGridViewTextBoxColumn colUsername;
        private System.Windows.Forms.DataGridViewTextBoxColumn colPassword;
        private System.Windows.Forms.DataGridViewTextBoxColumn colChangedDate;
        private System.Windows.Forms.DataGridViewButtonColumn colCopy;
        private System.Windows.Forms.DataGridViewButtonColumn colNew;
    }
}

