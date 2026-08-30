namespace howto_rename_files_with_regex
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
            this.label1 = new System.Windows.Forms.Label();
            this.txtDirectory = new System.Windows.Forms.TextBox();
            this.txtOldPattern = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtNewPattern = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.btnPreviewChanges = new System.Windows.Forms.Button();
            this.btnMakeChanges = new System.Windows.Forms.Button();
            this.txtFilePattern = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.lvwResults = new System.Windows.Forms.ListView();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.btnRemoveFile = new System.Windows.Forms.Button();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 12);
            this.label1.TabIndex = 7;
            this.label1.Text = "Directory:";
            // 
            // txtDirectory
            // 
            this.txtDirectory.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtDirectory.Location = new System.Drawing.Point(87, 11);
            this.txtDirectory.Name = "txtDirectory";
            this.txtDirectory.Size = new System.Drawing.Size(486, 22);
            this.txtDirectory.TabIndex = 0;
            // 
            // txtOldPattern
            // 
            this.txtOldPattern.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtOldPattern.Location = new System.Drawing.Point(87, 59);
            this.txtOldPattern.Name = "txtOldPattern";
            this.txtOldPattern.Size = new System.Drawing.Size(486, 22);
            this.txtOldPattern.TabIndex = 2;
            this.txtOldPattern.Text = "^(.*)file(.*)$";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 62);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 12);
            this.label2.TabIndex = 9;
            this.label2.Text = "Old Pattern:";
            // 
            // txtNewPattern
            // 
            this.txtNewPattern.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtNewPattern.Location = new System.Drawing.Point(87, 83);
            this.txtNewPattern.Name = "txtNewPattern";
            this.txtNewPattern.Size = new System.Drawing.Size(486, 22);
            this.txtNewPattern.TabIndex = 3;
            this.txtNewPattern.Text = "$1part($i)_$2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 86);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 12);
            this.label3.TabIndex = 10;
            this.label3.Text = "New Pattern:";
            // 
            // btnPreviewChanges
            // 
            this.btnPreviewChanges.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnPreviewChanges.Location = new System.Drawing.Point(161, 118);
            this.btnPreviewChanges.Name = "btnPreviewChanges";
            this.btnPreviewChanges.Size = new System.Drawing.Size(115, 21);
            this.btnPreviewChanges.TabIndex = 4;
            this.btnPreviewChanges.Text = "Preview Changes";
            this.btnPreviewChanges.UseVisualStyleBackColor = true;
            this.btnPreviewChanges.Click += new System.EventHandler(this.btnPreviewChanges_Click);
            // 
            // btnMakeChanges
            // 
            this.btnMakeChanges.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnMakeChanges.Enabled = false;
            this.btnMakeChanges.Location = new System.Drawing.Point(309, 118);
            this.btnMakeChanges.Name = "btnMakeChanges";
            this.btnMakeChanges.Size = new System.Drawing.Size(115, 21);
            this.btnMakeChanges.TabIndex = 5;
            this.btnMakeChanges.Text = "Make Changes";
            this.btnMakeChanges.UseVisualStyleBackColor = true;
            this.btnMakeChanges.Click += new System.EventHandler(this.btnMakeChanges_Click);
            // 
            // txtFilePattern
            // 
            this.txtFilePattern.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtFilePattern.Location = new System.Drawing.Point(87, 35);
            this.txtFilePattern.Name = "txtFilePattern";
            this.txtFilePattern.Size = new System.Drawing.Size(486, 22);
            this.txtFilePattern.TabIndex = 1;
            this.txtFilePattern.Text = "*.txt";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 38);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(60, 12);
            this.label4.TabIndex = 8;
            this.label4.Text = "File Pattern:";
            // 
            // lvwResults
            // 
            this.lvwResults.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lvwResults.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2});
            this.lvwResults.FullRowSelect = true;
            this.lvwResults.Location = new System.Drawing.Point(12, 156);
            this.lvwResults.Name = "lvwResults";
            this.lvwResults.Size = new System.Drawing.Size(561, 127);
            this.lvwResults.TabIndex = 11;
            this.lvwResults.UseCompatibleStateImageBehavior = false;
            this.lvwResults.View = System.Windows.Forms.View.Details;
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Change From:";
            this.columnHeader1.Width = 234;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "Change To:";
            this.columnHeader2.Width = 234;
            // 
            // btnRemoveFile
            // 
            this.btnRemoveFile.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRemoveFile.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnRemoveFile.Location = new System.Drawing.Point(554, 135);
            this.btnRemoveFile.Name = "btnRemoveFile";
            this.btnRemoveFile.Size = new System.Drawing.Size(20, 21);
            this.btnRemoveFile.TabIndex = 12;
            this.btnRemoveFile.Text = "x";
            this.toolTip1.SetToolTip(this.btnRemoveFile, "Remove file from list.");
            this.btnRemoveFile.UseVisualStyleBackColor = true;
            this.btnRemoveFile.Click += new System.EventHandler(this.btnRemoveFile_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(585, 294);
            this.Controls.Add(this.btnRemoveFile);
            this.Controls.Add(this.lvwResults);
            this.Controls.Add(this.txtFilePattern);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.btnMakeChanges);
            this.Controls.Add(this.btnPreviewChanges);
            this.Controls.Add(this.txtNewPattern);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtOldPattern);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtDirectory);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_rename_files_with_regex";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtDirectory;
        private System.Windows.Forms.TextBox txtOldPattern;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtNewPattern;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btnPreviewChanges;
        private System.Windows.Forms.Button btnMakeChanges;
        private System.Windows.Forms.TextBox txtFilePattern;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ListView lvwResults;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.Button btnRemoveFile;
        private System.Windows.Forms.ToolTip toolTip1;
    }
}

