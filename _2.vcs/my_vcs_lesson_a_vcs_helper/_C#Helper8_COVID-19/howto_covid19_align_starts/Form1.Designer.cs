namespace howto_covid19_align_starts
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
            this.picGraph = new System.Windows.Forms.PictureBox();
            this.clbCountries = new System.Windows.Forms.CheckedListBox();
            this.btnAll = new System.Windows.Forms.Button();
            this.btnNone = new System.Windows.Forms.Button();
            this.tipGraph = new System.Windows.Forms.ToolTip(this.components);
            this.label1 = new System.Windows.Forms.Label();
            this.radSortByName = new System.Windows.Forms.RadioButton();
            this.radSortByMaxCases = new System.Windows.Forms.RadioButton();
            this.txtAlignCases = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).BeginInit();
            this.SuspendLayout();
            // 
            // picGraph
            // 
            this.picGraph.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraph.BackColor = System.Drawing.SystemColors.Control;
            this.picGraph.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraph.Location = new System.Drawing.Point(184, 38);
            this.picGraph.Name = "picGraph";
            this.picGraph.Size = new System.Drawing.Size(365, 344);
            this.picGraph.TabIndex = 3;
            this.picGraph.TabStop = false;
            this.picGraph.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picGraph_MouseMove);
            this.picGraph.Paint += new System.Windows.Forms.PaintEventHandler(this.picGraph_Paint);
            // 
            // clbCountries
            // 
            this.clbCountries.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.clbCountries.FormattingEnabled = true;
            this.clbCountries.IntegralHeight = false;
            this.clbCountries.Location = new System.Drawing.Point(12, 38);
            this.clbCountries.Name = "clbCountries";
            this.clbCountries.Size = new System.Drawing.Size(166, 315);
            this.clbCountries.TabIndex = 4;
            this.clbCountries.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.clbCountries_ItemCheck);
            // 
            // btnAll
            // 
            this.btnAll.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnAll.Location = new System.Drawing.Point(12, 359);
            this.btnAll.Name = "btnAll";
            this.btnAll.Size = new System.Drawing.Size(75, 23);
            this.btnAll.TabIndex = 5;
            this.btnAll.Text = "All";
            this.btnAll.UseVisualStyleBackColor = true;
            this.btnAll.Click += new System.EventHandler(this.btnAll_Click);
            // 
            // btnNone
            // 
            this.btnNone.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnNone.Location = new System.Drawing.Point(103, 359);
            this.btnNone.Name = "btnNone";
            this.btnNone.Size = new System.Drawing.Size(75, 23);
            this.btnNone.TabIndex = 6;
            this.btnNone.Text = "None";
            this.btnNone.UseVisualStyleBackColor = true;
            this.btnNone.Click += new System.EventHandler(this.btnNone_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 13);
            this.label1.TabIndex = 7;
            this.label1.Text = "Sort By:";
            // 
            // radSortByName
            // 
            this.radSortByName.AutoSize = true;
            this.radSortByName.Location = new System.Drawing.Point(62, 13);
            this.radSortByName.Name = "radSortByName";
            this.radSortByName.Size = new System.Drawing.Size(53, 17);
            this.radSortByName.TabIndex = 8;
            this.radSortByName.TabStop = true;
            this.radSortByName.Text = "Name";
            this.radSortByName.UseVisualStyleBackColor = true;
            this.radSortByName.Click += new System.EventHandler(this.radSortByName_Click);
            // 
            // radSortByMaxCases
            // 
            this.radSortByMaxCases.AutoSize = true;
            this.radSortByMaxCases.Checked = true;
            this.radSortByMaxCases.Location = new System.Drawing.Point(121, 13);
            this.radSortByMaxCases.Name = "radSortByMaxCases";
            this.radSortByMaxCases.Size = new System.Drawing.Size(77, 17);
            this.radSortByMaxCases.TabIndex = 9;
            this.radSortByMaxCases.TabStop = true;
            this.radSortByMaxCases.Text = "Max Cases";
            this.radSortByMaxCases.UseVisualStyleBackColor = true;
            this.radSortByMaxCases.Click += new System.EventHandler(this.radSortByMaxCases_Click);
            // 
            // txtAlignCases
            // 
            this.txtAlignCases.Location = new System.Drawing.Point(268, 12);
            this.txtAlignCases.Name = "txtAlignCases";
            this.txtAlignCases.Size = new System.Drawing.Size(53, 20);
            this.txtAlignCases.TabIndex = 11;
            this.txtAlignCases.Text = "0";
            this.txtAlignCases.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtAlignCases.TextChanged += new System.EventHandler(this.txtAlignCases_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(224, 15);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(42, 13);
            this.label2.TabIndex = 12;
            this.label2.Text = "Align at";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(325, 15);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(35, 13);
            this.label3.TabIndex = 13;
            this.label3.Text = "cases";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(561, 394);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtAlignCases);
            this.Controls.Add(this.radSortByMaxCases);
            this.Controls.Add(this.radSortByName);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnNone);
            this.Controls.Add(this.btnAll);
            this.Controls.Add(this.clbCountries);
            this.Controls.Add(this.picGraph);
            this.Name = "Form1";
            this.Text = "howto_covid19_align_starts";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picGraph;
        private System.Windows.Forms.CheckedListBox clbCountries;
        private System.Windows.Forms.Button btnAll;
        private System.Windows.Forms.Button btnNone;
        private System.Windows.Forms.ToolTip tipGraph;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RadioButton radSortByName;
        private System.Windows.Forms.RadioButton radSortByMaxCases;
        private System.Windows.Forms.TextBox txtAlignCases;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
    }
}

