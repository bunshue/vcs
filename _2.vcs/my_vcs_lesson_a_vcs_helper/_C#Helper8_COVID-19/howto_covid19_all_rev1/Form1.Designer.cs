namespace howto_covid19_all_rev1
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
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.radSortByName = new System.Windows.Forms.RadioButton();
            this.radSortByMaxCases = new System.Windows.Forms.RadioButton();
            this.txtAlignCases = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.radDeathsPerResolution = new System.Windows.Forms.RadioButton();
            this.radRecoveriesPerMillion = new System.Windows.Forms.RadioButton();
            this.radRecoveries = new System.Windows.Forms.RadioButton();
            this.radDeathsPerMillion = new System.Windows.Forms.RadioButton();
            this.radDeaths = new System.Windows.Forms.RadioButton();
            this.radCasesPerMillion = new System.Windows.Forms.RadioButton();
            this.radCases = new System.Windows.Forms.RadioButton();
            this.lblLoading = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // picGraph
            // 
            this.picGraph.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraph.BackColor = System.Drawing.SystemColors.Control;
            this.picGraph.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraph.Location = new System.Drawing.Point(184, 120);
            this.picGraph.Name = "picGraph";
            this.picGraph.Size = new System.Drawing.Size(755, 454);
            this.picGraph.TabIndex = 3;
            this.picGraph.TabStop = false;
            this.picGraph.Paint += new System.Windows.Forms.PaintEventHandler(this.picGraph_Paint);
            this.picGraph.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picGraph_MouseMove);
            // 
            // clbCountries
            // 
            this.clbCountries.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.clbCountries.CheckOnClick = true;
            this.clbCountries.FormattingEnabled = true;
            this.clbCountries.IntegralHeight = false;
            this.clbCountries.Location = new System.Drawing.Point(12, 120);
            this.clbCountries.Name = "clbCountries";
            this.clbCountries.Size = new System.Drawing.Size(166, 427);
            this.clbCountries.TabIndex = 4;
            this.clbCountries.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.clbCountries_ItemCheck);
            // 
            // btnAll
            // 
            this.btnAll.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnAll.Location = new System.Drawing.Point(12, 552);
            this.btnAll.Name = "btnAll";
            this.btnAll.Size = new System.Drawing.Size(75, 21);
            this.btnAll.TabIndex = 5;
            this.btnAll.Text = "All";
            this.btnAll.UseVisualStyleBackColor = true;
            this.btnAll.Click += new System.EventHandler(this.btnAll_Click);
            // 
            // btnNone
            // 
            this.btnNone.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnNone.Location = new System.Drawing.Point(103, 552);
            this.btnNone.Name = "btnNone";
            this.btnNone.Size = new System.Drawing.Size(75, 21);
            this.btnNone.TabIndex = 6;
            this.btnNone.Text = "None";
            this.btnNone.UseVisualStyleBackColor = true;
            this.btnNone.Click += new System.EventHandler(this.btnNone_Click);
            // 
            // radSortByName
            // 
            this.radSortByName.AutoSize = true;
            this.radSortByName.Location = new System.Drawing.Point(20, 18);
            this.radSortByName.Name = "radSortByName";
            this.radSortByName.Size = new System.Drawing.Size(50, 16);
            this.radSortByName.TabIndex = 8;
            this.radSortByName.TabStop = true;
            this.radSortByName.Text = "Name";
            this.radSortByName.UseVisualStyleBackColor = true;
            this.radSortByName.Click += new System.EventHandler(this.radSort_Click);
            // 
            // radSortByMaxCases
            // 
            this.radSortByMaxCases.AutoSize = true;
            this.radSortByMaxCases.Checked = true;
            this.radSortByMaxCases.Location = new System.Drawing.Point(79, 18);
            this.radSortByMaxCases.Name = "radSortByMaxCases";
            this.radSortByMaxCases.Size = new System.Drawing.Size(73, 16);
            this.radSortByMaxCases.TabIndex = 9;
            this.radSortByMaxCases.TabStop = true;
            this.radSortByMaxCases.Text = "Max Cases";
            this.radSortByMaxCases.UseVisualStyleBackColor = true;
            this.radSortByMaxCases.Click += new System.EventHandler(this.radSort_Click);
            // 
            // txtAlignCases
            // 
            this.txtAlignCases.Location = new System.Drawing.Point(20, 17);
            this.txtAlignCases.Name = "txtAlignCases";
            this.txtAlignCases.Size = new System.Drawing.Size(53, 22);
            this.txtAlignCases.TabIndex = 11;
            this.txtAlignCases.Text = "0";
            this.txtAlignCases.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtAlignCases.TextChanged += new System.EventHandler(this.txtAlignCases_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(79, 19);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(28, 12);
            this.label3.TabIndex = 13;
            this.label3.Text = "cases";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radSortByName);
            this.groupBox1.Controls.Add(this.radSortByMaxCases);
            this.groupBox1.Location = new System.Drawing.Point(12, 11);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(166, 43);
            this.groupBox1.TabIndex = 14;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Sort By";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.txtAlignCases);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Location = new System.Drawing.Point(184, 11);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(125, 43);
            this.groupBox2.TabIndex = 10;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Align At";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.radDeathsPerResolution);
            this.groupBox3.Controls.Add(this.radRecoveriesPerMillion);
            this.groupBox3.Controls.Add(this.radRecoveries);
            this.groupBox3.Controls.Add(this.radDeathsPerMillion);
            this.groupBox3.Controls.Add(this.radDeaths);
            this.groupBox3.Controls.Add(this.radCasesPerMillion);
            this.groupBox3.Controls.Add(this.radCases);
            this.groupBox3.Location = new System.Drawing.Point(315, 11);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(247, 103);
            this.groupBox3.TabIndex = 14;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Display";
            // 
            // radDeathsPerResolution
            // 
            this.radDeathsPerResolution.AutoSize = true;
            this.radDeathsPerResolution.Location = new System.Drawing.Point(20, 81);
            this.radDeathsPerResolution.Name = "radDeathsPerResolution";
            this.radDeathsPerResolution.Size = new System.Drawing.Size(125, 16);
            this.radDeathsPerResolution.TabIndex = 6;
            this.radDeathsPerResolution.Text = "Deaths Per Resolution";
            this.radDeathsPerResolution.UseVisualStyleBackColor = true;
            this.radDeathsPerResolution.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radRecoveriesPerMillion
            // 
            this.radRecoveriesPerMillion.AutoSize = true;
            this.radRecoveriesPerMillion.Location = new System.Drawing.Point(105, 60);
            this.radRecoveriesPerMillion.Name = "radRecoveriesPerMillion";
            this.radRecoveriesPerMillion.Size = new System.Drawing.Size(129, 16);
            this.radRecoveriesPerMillion.TabIndex = 5;
            this.radRecoveriesPerMillion.Text = "Recoveries Per Million";
            this.radRecoveriesPerMillion.UseVisualStyleBackColor = true;
            this.radRecoveriesPerMillion.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radRecoveries
            // 
            this.radRecoveries.AutoSize = true;
            this.radRecoveries.Location = new System.Drawing.Point(20, 60);
            this.radRecoveries.Name = "radRecoveries";
            this.radRecoveries.Size = new System.Drawing.Size(74, 16);
            this.radRecoveries.TabIndex = 4;
            this.radRecoveries.Text = "Recoveries";
            this.radRecoveries.UseVisualStyleBackColor = true;
            this.radRecoveries.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radDeathsPerMillion
            // 
            this.radDeathsPerMillion.AutoSize = true;
            this.radDeathsPerMillion.Location = new System.Drawing.Point(105, 39);
            this.radDeathsPerMillion.Name = "radDeathsPerMillion";
            this.radDeathsPerMillion.Size = new System.Drawing.Size(109, 16);
            this.radDeathsPerMillion.TabIndex = 3;
            this.radDeathsPerMillion.Text = "Deaths Per Million";
            this.radDeathsPerMillion.UseVisualStyleBackColor = true;
            this.radDeathsPerMillion.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radDeaths
            // 
            this.radDeaths.AutoSize = true;
            this.radDeaths.Location = new System.Drawing.Point(20, 39);
            this.radDeaths.Name = "radDeaths";
            this.radDeaths.Size = new System.Drawing.Size(54, 16);
            this.radDeaths.TabIndex = 2;
            this.radDeaths.Text = "Deaths";
            this.radDeaths.UseVisualStyleBackColor = true;
            this.radDeaths.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radCasesPerMillion
            // 
            this.radCasesPerMillion.AutoSize = true;
            this.radCasesPerMillion.Location = new System.Drawing.Point(105, 18);
            this.radCasesPerMillion.Name = "radCasesPerMillion";
            this.radCasesPerMillion.Size = new System.Drawing.Size(104, 16);
            this.radCasesPerMillion.TabIndex = 1;
            this.radCasesPerMillion.Text = "Cases Per Million";
            this.radCasesPerMillion.UseVisualStyleBackColor = true;
            this.radCasesPerMillion.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // radCases
            // 
            this.radCases.AutoSize = true;
            this.radCases.Checked = true;
            this.radCases.Location = new System.Drawing.Point(20, 18);
            this.radCases.Name = "radCases";
            this.radCases.Size = new System.Drawing.Size(49, 16);
            this.radCases.TabIndex = 0;
            this.radCases.TabStop = true;
            this.radCases.Text = "Cases";
            this.radCases.UseVisualStyleBackColor = true;
            this.radCases.Click += new System.EventHandler(this.radDataSet_Click);
            // 
            // lblLoading
            // 
            this.lblLoading.AutoSize = true;
            this.lblLoading.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLoading.ForeColor = System.Drawing.Color.Red;
            this.lblLoading.Location = new System.Drawing.Point(12, 73);
            this.lblLoading.Name = "lblLoading";
            this.lblLoading.Size = new System.Drawing.Size(70, 20);
            this.lblLoading.TabIndex = 15;
            this.lblLoading.Text = "Loading:";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(943, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(267, 562);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1222, 584);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lblLoading);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.btnNone);
            this.Controls.Add(this.btnAll);
            this.Controls.Add(this.clbCountries);
            this.Controls.Add(this.picGraph);
            this.Name = "Form1";
            this.Text = "howto_covid19_all_rev1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picGraph;
        private System.Windows.Forms.CheckedListBox clbCountries;
        private System.Windows.Forms.Button btnAll;
        private System.Windows.Forms.Button btnNone;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.RadioButton radSortByName;
        private System.Windows.Forms.RadioButton radSortByMaxCases;
        private System.Windows.Forms.TextBox txtAlignCases;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton radCasesPerMillion;
        private System.Windows.Forms.RadioButton radCases;
        private System.Windows.Forms.RadioButton radDeathsPerMillion;
        private System.Windows.Forms.RadioButton radDeaths;
        private System.Windows.Forms.RadioButton radDeathsPerResolution;
        private System.Windows.Forms.RadioButton radRecoveriesPerMillion;
        private System.Windows.Forms.RadioButton radRecoveries;
        private System.Windows.Forms.Label lblLoading;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

