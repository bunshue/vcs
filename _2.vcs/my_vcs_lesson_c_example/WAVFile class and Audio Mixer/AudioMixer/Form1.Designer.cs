namespace AudioMerger
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
            this.MixAudioButton = new System.Windows.Forms.Button();
            this.FilenameGrid = new System.Windows.Forms.DataGridView();
            this.FilenameColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.DeleteBtnColumn = new System.Windows.Forms.DataGridViewButtonColumn();
            this.ClearListButton = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.FilenameGrid)).BeginInit();
            this.SuspendLayout();
            // 
            // MixAudioButton
            // 
            this.MixAudioButton.AutoSize = true;
            this.MixAudioButton.Location = new System.Drawing.Point(12, 16);
            this.MixAudioButton.Name = "MixAudioButton";
            this.MixAudioButton.Size = new System.Drawing.Size(80, 40);
            this.MixAudioButton.TabIndex = 1;
            this.MixAudioButton.Text = "Perform mix";
            this.MixAudioButton.UseVisualStyleBackColor = true;
            this.MixAudioButton.Click += new System.EventHandler(this.MergeAudioButton_Click);
            // 
            // FilenameGrid
            // 
            this.FilenameGrid.AllowDrop = true;
            this.FilenameGrid.AllowUserToAddRows = false;
            this.FilenameGrid.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.FilenameGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.DisableResizing;
            this.FilenameGrid.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.FilenameColumn,
            this.DeleteBtnColumn});
            this.FilenameGrid.Location = new System.Drawing.Point(12, 71);
            this.FilenameGrid.Name = "FilenameGrid";
            this.FilenameGrid.ReadOnly = true;
            this.FilenameGrid.RowHeadersVisible = false;
            this.FilenameGrid.ShowCellErrors = false;
            this.FilenameGrid.Size = new System.Drawing.Size(622, 391);
            this.FilenameGrid.TabIndex = 3;
            this.FilenameGrid.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.FilenameGrid_CellContentClick);
            this.FilenameGrid.DragDrop += new System.Windows.Forms.DragEventHandler(this.FilenameGrid_DragDrop);
            this.FilenameGrid.DragEnter += new System.Windows.Forms.DragEventHandler(this.FilenameGrid_DragEnter);
            // 
            // FilenameColumn
            // 
            this.FilenameColumn.FillWeight = 300F;
            this.FilenameColumn.HeaderText = "Filename";
            this.FilenameColumn.Name = "FilenameColumn";
            this.FilenameColumn.ReadOnly = true;
            this.FilenameColumn.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.NotSortable;
            // 
            // DeleteBtnColumn
            // 
            this.DeleteBtnColumn.FillWeight = 50F;
            this.DeleteBtnColumn.HeaderText = "";
            this.DeleteBtnColumn.Name = "DeleteBtnColumn";
            this.DeleteBtnColumn.ReadOnly = true;
            this.DeleteBtnColumn.Text = "Remove";
            this.DeleteBtnColumn.ToolTipText = "Click to remove this audio file";
            // 
            // ClearListButton
            // 
            this.ClearListButton.Location = new System.Drawing.Point(115, 16);
            this.ClearListButton.Name = "ClearListButton";
            this.ClearListButton.Size = new System.Drawing.Size(80, 40);
            this.ClearListButton.TabIndex = 4;
            this.ClearListButton.Text = "Clear list";
            this.ClearListButton.UseVisualStyleBackColor = true;
            this.ClearListButton.Click += new System.EventHandler(this.ClearListButton_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(640, 16);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(548, 446);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1200, 474);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.ClearListButton);
            this.Controls.Add(this.FilenameGrid);
            this.Controls.Add(this.MixAudioButton);
            this.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Text = "Audio File Mixer";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.FilenameGrid)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button MixAudioButton;
        private System.Windows.Forms.DataGridView FilenameGrid;
        private System.Windows.Forms.Button ClearListButton;
        private System.Windows.Forms.DataGridViewTextBoxColumn FilenameColumn;
        private System.Windows.Forms.DataGridViewButtonColumn DeleteBtnColumn;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

