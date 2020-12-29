namespace howto_covid19_state_increases
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
            this.clbStates = new System.Windows.Forms.CheckedListBox();
            this.btnAll = new System.Windows.Forms.Button();
            this.btnNone = new System.Windows.Forms.Button();
            this.tipGraph = new System.Windows.Forms.ToolTip(this.components);
            this.radSortByName = new System.Windows.Forms.RadioButton();
            this.radSortByMaxCases = new System.Windows.Forms.RadioButton();
            this.txtAlignCases = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.chkDeathsIncrease = new System.Windows.Forms.CheckBox();
            this.chkHospitalizedIncrease = new System.Windows.Forms.CheckBox();
            this.chkPositiveIncrease = new System.Windows.Forms.CheckBox();
            this.btnNoDataSets = new System.Windows.Forms.Button();
            this.btnAllDataSets = new System.Windows.Forms.Button();
            this.chkDeathsPerResolution = new System.Windows.Forms.CheckBox();
            this.chkDeaths = new System.Windows.Forms.CheckBox();
            this.chkRecovered = new System.Windows.Forms.CheckBox();
            this.chkVentTotal = new System.Windows.Forms.CheckBox();
            this.chkVentNow = new System.Windows.Forms.CheckBox();
            this.chkIcuTotal = new System.Windows.Forms.CheckBox();
            this.chkIcuNow = new System.Windows.Forms.CheckBox();
            this.chkHospitalizedTotal = new System.Windows.Forms.CheckBox();
            this.chkPerMillion = new System.Windows.Forms.CheckBox();
            this.chkHospitalizedNow = new System.Windows.Forms.CheckBox();
            this.chkPending = new System.Windows.Forms.CheckBox();
            this.chkTotalNegative = new System.Windows.Forms.CheckBox();
            this.chkTotalPositive = new System.Windows.Forms.CheckBox();
            this.lblLoading = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
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
            this.picGraph.Location = new System.Drawing.Point(355, 60);
            this.picGraph.Name = "picGraph";
            this.picGraph.Size = new System.Drawing.Size(491, 406);
            this.picGraph.TabIndex = 3;
            this.picGraph.TabStop = false;
            this.picGraph.Paint += new System.Windows.Forms.PaintEventHandler(this.picGraph_Paint);
            this.picGraph.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picGraph_MouseMove);
            // 
            // clbStates
            // 
            this.clbStates.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.clbStates.CheckOnClick = true;
            this.clbStates.FormattingEnabled = true;
            this.clbStates.IntegralHeight = false;
            this.clbStates.Location = new System.Drawing.Point(266, 60);
            this.clbStates.Name = "clbStates";
            this.clbStates.Size = new System.Drawing.Size(83, 353);
            this.clbStates.TabIndex = 4;
            this.clbStates.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.clbCountries_ItemCheck);
            // 
            // btnAll
            // 
            this.btnAll.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnAll.Location = new System.Drawing.Point(266, 418);
            this.btnAll.Name = "btnAll";
            this.btnAll.Size = new System.Drawing.Size(83, 21);
            this.btnAll.TabIndex = 5;
            this.btnAll.Text = "All";
            this.btnAll.UseVisualStyleBackColor = true;
            this.btnAll.Click += new System.EventHandler(this.btnAll_Click);
            // 
            // btnNone
            // 
            this.btnNone.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnNone.Location = new System.Drawing.Point(266, 445);
            this.btnNone.Name = "btnNone";
            this.btnNone.Size = new System.Drawing.Size(83, 21);
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
            this.groupBox3.Controls.Add(this.chkDeathsIncrease);
            this.groupBox3.Controls.Add(this.chkHospitalizedIncrease);
            this.groupBox3.Controls.Add(this.chkPositiveIncrease);
            this.groupBox3.Controls.Add(this.btnNoDataSets);
            this.groupBox3.Controls.Add(this.btnAllDataSets);
            this.groupBox3.Controls.Add(this.chkDeathsPerResolution);
            this.groupBox3.Controls.Add(this.chkDeaths);
            this.groupBox3.Controls.Add(this.chkRecovered);
            this.groupBox3.Controls.Add(this.chkVentTotal);
            this.groupBox3.Controls.Add(this.chkVentNow);
            this.groupBox3.Controls.Add(this.chkIcuTotal);
            this.groupBox3.Controls.Add(this.chkIcuNow);
            this.groupBox3.Controls.Add(this.chkHospitalizedTotal);
            this.groupBox3.Controls.Add(this.chkPerMillion);
            this.groupBox3.Controls.Add(this.chkHospitalizedNow);
            this.groupBox3.Controls.Add(this.chkPending);
            this.groupBox3.Controls.Add(this.chkTotalNegative);
            this.groupBox3.Controls.Add(this.chkTotalPositive);
            this.groupBox3.Location = new System.Drawing.Point(13, 60);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(247, 406);
            this.groupBox3.TabIndex = 14;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Display";
            // 
            // chkDeathsIncrease
            // 
            this.chkDeathsIncrease.AutoSize = true;
            this.chkDeathsIncrease.Location = new System.Drawing.Point(19, 379);
            this.chkDeathsIncrease.Name = "chkDeathsIncrease";
            this.chkDeathsIncrease.Size = new System.Drawing.Size(96, 16);
            this.chkDeathsIncrease.TabIndex = 24;
            this.chkDeathsIncrease.Text = "Deaths Increase";
            this.chkDeathsIncrease.UseVisualStyleBackColor = true;
            this.chkDeathsIncrease.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkHospitalizedIncrease
            // 
            this.chkHospitalizedIncrease.AutoSize = true;
            this.chkHospitalizedIncrease.Location = new System.Drawing.Point(19, 358);
            this.chkHospitalizedIncrease.Name = "chkHospitalizedIncrease";
            this.chkHospitalizedIncrease.Size = new System.Drawing.Size(122, 16);
            this.chkHospitalizedIncrease.TabIndex = 23;
            this.chkHospitalizedIncrease.Text = "Hospitalized Increase";
            this.chkHospitalizedIncrease.UseVisualStyleBackColor = true;
            this.chkHospitalizedIncrease.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkPositiveIncrease
            // 
            this.chkPositiveIncrease.AutoSize = true;
            this.chkPositiveIncrease.Location = new System.Drawing.Point(19, 337);
            this.chkPositiveIncrease.Name = "chkPositiveIncrease";
            this.chkPositiveIncrease.Size = new System.Drawing.Size(101, 16);
            this.chkPositiveIncrease.TabIndex = 22;
            this.chkPositiveIncrease.Text = "Positive Increase";
            this.chkPositiveIncrease.UseVisualStyleBackColor = true;
            this.chkPositiveIncrease.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // btnNoDataSets
            // 
            this.btnNoDataSets.Location = new System.Drawing.Point(166, 83);
            this.btnNoDataSets.Name = "btnNoDataSets";
            this.btnNoDataSets.Size = new System.Drawing.Size(75, 21);
            this.btnNoDataSets.TabIndex = 16;
            this.btnNoDataSets.Text = "None";
            this.btnNoDataSets.UseVisualStyleBackColor = true;
            this.btnNoDataSets.Click += new System.EventHandler(this.btnNoDataSets_Click);
            // 
            // btnAllDataSets
            // 
            this.btnAllDataSets.Location = new System.Drawing.Point(166, 56);
            this.btnAllDataSets.Name = "btnAllDataSets";
            this.btnAllDataSets.Size = new System.Drawing.Size(75, 21);
            this.btnAllDataSets.TabIndex = 16;
            this.btnAllDataSets.Text = "All";
            this.btnAllDataSets.UseVisualStyleBackColor = true;
            this.btnAllDataSets.Click += new System.EventHandler(this.btnAllDataSets_Click);
            // 
            // chkDeathsPerResolution
            // 
            this.chkDeathsPerResolution.AutoSize = true;
            this.chkDeathsPerResolution.Location = new System.Drawing.Point(19, 304);
            this.chkDeathsPerResolution.Name = "chkDeathsPerResolution";
            this.chkDeathsPerResolution.Size = new System.Drawing.Size(126, 16);
            this.chkDeathsPerResolution.TabIndex = 21;
            this.chkDeathsPerResolution.Text = "Deaths Per Resolution";
            this.chkDeathsPerResolution.UseVisualStyleBackColor = true;
            this.chkDeathsPerResolution.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkDeaths
            // 
            this.chkDeaths.AutoSize = true;
            this.chkDeaths.Location = new System.Drawing.Point(20, 272);
            this.chkDeaths.Name = "chkDeaths";
            this.chkDeaths.Size = new System.Drawing.Size(55, 16);
            this.chkDeaths.TabIndex = 18;
            this.chkDeaths.Text = "Deaths";
            this.chkDeaths.UseVisualStyleBackColor = true;
            this.chkDeaths.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkRecovered
            // 
            this.chkRecovered.AutoSize = true;
            this.chkRecovered.Location = new System.Drawing.Point(20, 251);
            this.chkRecovered.Name = "chkRecovered";
            this.chkRecovered.Size = new System.Drawing.Size(74, 16);
            this.chkRecovered.TabIndex = 17;
            this.chkRecovered.Text = "Recovered";
            this.chkRecovered.UseVisualStyleBackColor = true;
            this.chkRecovered.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkVentTotal
            // 
            this.chkVentTotal.AutoSize = true;
            this.chkVentTotal.Location = new System.Drawing.Point(20, 230);
            this.chkVentTotal.Name = "chkVentTotal";
            this.chkVentTotal.Size = new System.Drawing.Size(73, 16);
            this.chkVentTotal.TabIndex = 16;
            this.chkVentTotal.Text = "Vent Total";
            this.chkVentTotal.UseVisualStyleBackColor = true;
            this.chkVentTotal.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkVentNow
            // 
            this.chkVentNow.AutoSize = true;
            this.chkVentNow.Location = new System.Drawing.Point(20, 209);
            this.chkVentNow.Name = "chkVentNow";
            this.chkVentNow.Size = new System.Drawing.Size(71, 16);
            this.chkVentNow.TabIndex = 15;
            this.chkVentNow.Text = "Vent Now";
            this.chkVentNow.UseVisualStyleBackColor = true;
            this.chkVentNow.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkIcuTotal
            // 
            this.chkIcuTotal.AutoSize = true;
            this.chkIcuTotal.Location = new System.Drawing.Point(20, 187);
            this.chkIcuTotal.Name = "chkIcuTotal";
            this.chkIcuTotal.Size = new System.Drawing.Size(71, 16);
            this.chkIcuTotal.TabIndex = 14;
            this.chkIcuTotal.Text = "ICU Total";
            this.chkIcuTotal.UseVisualStyleBackColor = true;
            this.chkIcuTotal.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkIcuNow
            // 
            this.chkIcuNow.AutoSize = true;
            this.chkIcuNow.Location = new System.Drawing.Point(20, 166);
            this.chkIcuNow.Name = "chkIcuNow";
            this.chkIcuNow.Size = new System.Drawing.Size(69, 16);
            this.chkIcuNow.TabIndex = 13;
            this.chkIcuNow.Text = "ICU Now";
            this.chkIcuNow.UseVisualStyleBackColor = true;
            this.chkIcuNow.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkHospitalizedTotal
            // 
            this.chkHospitalizedTotal.AutoSize = true;
            this.chkHospitalizedTotal.Location = new System.Drawing.Point(20, 145);
            this.chkHospitalizedTotal.Name = "chkHospitalizedTotal";
            this.chkHospitalizedTotal.Size = new System.Drawing.Size(108, 16);
            this.chkHospitalizedTotal.TabIndex = 12;
            this.chkHospitalizedTotal.Text = "Hospitalized Total";
            this.chkHospitalizedTotal.UseVisualStyleBackColor = true;
            this.chkHospitalizedTotal.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkPerMillion
            // 
            this.chkPerMillion.AutoSize = true;
            this.chkPerMillion.Location = new System.Drawing.Point(20, 18);
            this.chkPerMillion.Name = "chkPerMillion";
            this.chkPerMillion.Size = new System.Drawing.Size(76, 16);
            this.chkPerMillion.TabIndex = 11;
            this.chkPerMillion.Text = "Per Million";
            this.chkPerMillion.UseVisualStyleBackColor = true;
            this.chkPerMillion.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkHospitalizedNow
            // 
            this.chkHospitalizedNow.AutoSize = true;
            this.chkHospitalizedNow.Location = new System.Drawing.Point(20, 124);
            this.chkHospitalizedNow.Name = "chkHospitalizedNow";
            this.chkHospitalizedNow.Size = new System.Drawing.Size(106, 16);
            this.chkHospitalizedNow.TabIndex = 10;
            this.chkHospitalizedNow.Text = "Hospitalized Now";
            this.chkHospitalizedNow.UseVisualStyleBackColor = true;
            this.chkHospitalizedNow.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkPending
            // 
            this.chkPending.AutoSize = true;
            this.chkPending.Location = new System.Drawing.Point(20, 102);
            this.chkPending.Name = "chkPending";
            this.chkPending.Size = new System.Drawing.Size(62, 16);
            this.chkPending.TabIndex = 9;
            this.chkPending.Text = "Pending";
            this.chkPending.UseVisualStyleBackColor = true;
            this.chkPending.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkTotalNegative
            // 
            this.chkTotalNegative.AutoSize = true;
            this.chkTotalNegative.Location = new System.Drawing.Point(20, 81);
            this.chkTotalNegative.Name = "chkTotalNegative";
            this.chkTotalNegative.Size = new System.Drawing.Size(92, 16);
            this.chkTotalNegative.TabIndex = 8;
            this.chkTotalNegative.Text = "Total Negative";
            this.chkTotalNegative.UseVisualStyleBackColor = true;
            this.chkTotalNegative.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // chkTotalPositive
            // 
            this.chkTotalPositive.AutoSize = true;
            this.chkTotalPositive.Checked = true;
            this.chkTotalPositive.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkTotalPositive.Location = new System.Drawing.Point(20, 60);
            this.chkTotalPositive.Name = "chkTotalPositive";
            this.chkTotalPositive.Size = new System.Drawing.Size(87, 16);
            this.chkTotalPositive.TabIndex = 7;
            this.chkTotalPositive.Text = "Total Positive";
            this.chkTotalPositive.UseVisualStyleBackColor = true;
            this.chkTotalPositive.CheckedChanged += new System.EventHandler(this.chkDataSet_CheckedChanged);
            // 
            // lblLoading
            // 
            this.lblLoading.AutoSize = true;
            this.lblLoading.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLoading.ForeColor = System.Drawing.Color.Red;
            this.lblLoading.Location = new System.Drawing.Point(324, 26);
            this.lblLoading.Name = "lblLoading";
            this.lblLoading.Size = new System.Drawing.Size(70, 20);
            this.lblLoading.TabIndex = 15;
            this.lblLoading.Text = "Loading:";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(852, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(359, 454);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(650, 21);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 21);
            this.button1.TabIndex = 25;
            this.button1.Text = "test";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(559, 21);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 21);
            this.button2.TabIndex = 26;
            this.button2.Text = "clear";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(749, 21);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 21);
            this.button3.TabIndex = 27;
            this.button3.Text = "test";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1223, 477);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lblLoading);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.btnNone);
            this.Controls.Add(this.btnAll);
            this.Controls.Add(this.clbStates);
            this.Controls.Add(this.picGraph);
            this.Name = "Form1";
            this.Text = "howto_covid19_state_increases";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
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
        private System.Windows.Forms.CheckedListBox clbStates;
        private System.Windows.Forms.Button btnAll;
        private System.Windows.Forms.Button btnNone;
        private System.Windows.Forms.ToolTip tipGraph;
        private System.Windows.Forms.RadioButton radSortByName;
        private System.Windows.Forms.RadioButton radSortByMaxCases;
        private System.Windows.Forms.TextBox txtAlignCases;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label lblLoading;
        public System.Windows.Forms.CheckBox chkDeathsPerResolution;
        public System.Windows.Forms.CheckBox chkDeaths;
        public System.Windows.Forms.CheckBox chkRecovered;
        public System.Windows.Forms.CheckBox chkVentTotal;
        public System.Windows.Forms.CheckBox chkVentNow;
        public System.Windows.Forms.CheckBox chkIcuTotal;
        public System.Windows.Forms.CheckBox chkIcuNow;
        public System.Windows.Forms.CheckBox chkHospitalizedTotal;
        public System.Windows.Forms.CheckBox chkPerMillion;
        public System.Windows.Forms.CheckBox chkHospitalizedNow;
        public System.Windows.Forms.CheckBox chkPending;
        public System.Windows.Forms.CheckBox chkTotalNegative;
        public System.Windows.Forms.CheckBox chkTotalPositive;
        private System.Windows.Forms.Button btnNoDataSets;
        private System.Windows.Forms.Button btnAllDataSets;
        public System.Windows.Forms.CheckBox chkDeathsIncrease;
        public System.Windows.Forms.CheckBox chkHospitalizedIncrease;
        public System.Windows.Forms.CheckBox chkPositiveIncrease;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
    }
}

