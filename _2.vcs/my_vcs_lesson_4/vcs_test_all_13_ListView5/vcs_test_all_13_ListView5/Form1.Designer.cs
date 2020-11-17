namespace vcs_test_all_13_ListView5
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
            this.radNoSort = new System.Windows.Forms.RadioButton();
            this.radSortAllColumns = new System.Windows.Forms.RadioButton();
            this.radSortClickedColumn = new System.Windows.Forms.RadioButton();
            this.listView1 = new System.Windows.Forms.ListView();
            this.SuspendLayout();
            // 
            // radNoSort
            // 
            this.radNoSort.AutoSize = true;
            this.radNoSort.Location = new System.Drawing.Point(0, 0);
            this.radNoSort.Name = "radNoSort";
            this.radNoSort.Size = new System.Drawing.Size(59, 17);
            this.radNoSort.TabIndex = 4;
            this.radNoSort.TabStop = true;
            this.radNoSort.Text = "No sort";
            this.radNoSort.UseVisualStyleBackColor = true;
            this.radNoSort.Click += new System.EventHandler(this.radNoSort_Click);
            // 
            // radSortAllColumns
            // 
            this.radSortAllColumns.AutoSize = true;
            this.radSortAllColumns.Location = new System.Drawing.Point(65, 0);
            this.radSortAllColumns.Name = "radSortAllColumns";
            this.radSortAllColumns.Size = new System.Drawing.Size(114, 17);
            this.radSortAllColumns.TabIndex = 5;
            this.radSortAllColumns.TabStop = true;
            this.radSortAllColumns.Text = "Sort on all columns";
            this.radSortAllColumns.UseVisualStyleBackColor = true;
            this.radSortAllColumns.Click += new System.EventHandler(this.radSortAllColumns_Click);
            // 
            // radSortClickedColumn
            // 
            this.radSortClickedColumn.AutoSize = true;
            this.radSortClickedColumn.Location = new System.Drawing.Point(185, 0);
            this.radSortClickedColumn.Name = "radSortClickedColumn";
            this.radSortClickedColumn.Size = new System.Drawing.Size(138, 17);
            this.radSortClickedColumn.TabIndex = 6;
            this.radSortClickedColumn.TabStop = true;
            this.radSortClickedColumn.Text = "Sort on clicked columns";
            this.radSortClickedColumn.UseVisualStyleBackColor = true;
            this.radSortClickedColumn.Click += new System.EventHandler(this.radSortClickedColumn_Click);
            // 
            // listView1
            // 
            this.listView1.AllowColumnReorder = true;
            this.listView1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.listView1.FullRowSelect = true;
            this.listView1.Location = new System.Drawing.Point(0, 23);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(577, 243);
            this.listView1.TabIndex = 7;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(577, 266);
            this.Controls.Add(this.radNoSort);
            this.Controls.Add(this.radSortAllColumns);
            this.Controls.Add(this.radSortClickedColumn);
            this.Controls.Add(this.listView1);
            this.Name = "Form1";
            this.Text = "vcs_test_all_13_ListView5";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton radNoSort;
        private System.Windows.Forms.RadioButton radSortAllColumns;
        private System.Windows.Forms.RadioButton radSortClickedColumn;
        internal System.Windows.Forms.ListView listView1;
    }
}

