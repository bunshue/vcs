namespace howto_401k_graph
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
            this.txtRothSurrendered = new System.Windows.Forms.TextBox();
            this.label13 = new System.Windows.Forms.Label();
            this.nudYears = new System.Windows.Forms.NumericUpDown();
            this.txtFinalRoth = new System.Windows.Forms.TextBox();
            this.label12 = new System.Windows.Forms.Label();
            this.txt401kSurrendered = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.txtTaxAtEnd = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.txtPenalty = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.txtFinal401k = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.txtFinalSavings = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.picGraph = new System.Windows.Forms.PictureBox();
            this.Label5 = new System.Windows.Forms.Label();
            this.btnGo = new System.Windows.Forms.Button();
            this.txtInterestRate = new System.Windows.Forms.TextBox();
            this.Label4 = new System.Windows.Forms.Label();
            this.GroupBox1 = new System.Windows.Forms.GroupBox();
            this.Label3 = new System.Windows.Forms.Label();
            this.txtTaxRate = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtAnnualContribution = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.nudYears)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).BeginInit();
            this.GroupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // txtRothSurrendered
            // 
            this.txtRothSurrendered.Location = new System.Drawing.Point(447, 187);
            this.txtRothSurrendered.Name = "txtRothSurrendered";
            this.txtRothSurrendered.ReadOnly = true;
            this.txtRothSurrendered.Size = new System.Drawing.Size(76, 22);
            this.txtRothSurrendered.TabIndex = 85;
            this.txtRothSurrendered.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.ForeColor = System.Drawing.Color.Green;
            this.label13.Location = new System.Drawing.Point(339, 187);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(97, 12);
            this.label13.TabIndex = 86;
            this.label13.Text = "Roth (surrendered):";
            // 
            // nudYears
            // 
            this.nudYears.Location = new System.Drawing.Point(146, 141);
            this.nudYears.Minimum = new decimal(new int[] {
            2,
            0,
            0,
            0});
            this.nudYears.Name = "nudYears";
            this.nudYears.Size = new System.Drawing.Size(76, 22);
            this.nudYears.TabIndex = 84;
            this.nudYears.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.nudYears.Value = new decimal(new int[] {
            35,
            0,
            0,
            0});
            // 
            // txtFinalRoth
            // 
            this.txtFinalRoth.Location = new System.Drawing.Point(447, 163);
            this.txtFinalRoth.Name = "txtFinalRoth";
            this.txtFinalRoth.ReadOnly = true;
            this.txtFinalRoth.Size = new System.Drawing.Size(76, 22);
            this.txtFinalRoth.TabIndex = 82;
            this.txtFinalRoth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.ForeColor = System.Drawing.Color.Green;
            this.label12.Location = new System.Drawing.Point(339, 163);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(31, 12);
            this.label12.TabIndex = 83;
            this.label12.Text = "Roth:";
            // 
            // txt401kSurrendered
            // 
            this.txt401kSurrendered.Location = new System.Drawing.Point(447, 139);
            this.txt401kSurrendered.Name = "txt401kSurrendered";
            this.txt401kSurrendered.ReadOnly = true;
            this.txt401kSurrendered.Size = new System.Drawing.Size(76, 22);
            this.txt401kSurrendered.TabIndex = 69;
            this.txt401kSurrendered.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.ForeColor = System.Drawing.Color.Blue;
            this.label11.Location = new System.Drawing.Point(339, 139);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(101, 12);
            this.label11.TabIndex = 81;
            this.label11.Text = "401 (k) surrendered:";
            // 
            // txtTaxAtEnd
            // 
            this.txtTaxAtEnd.Location = new System.Drawing.Point(146, 187);
            this.txtTaxAtEnd.Name = "txtTaxAtEnd";
            this.txtTaxAtEnd.Size = new System.Drawing.Size(76, 22);
            this.txtTaxAtEnd.TabIndex = 65;
            this.txtTaxAtEnd.Text = "15%";
            this.txtTaxAtEnd.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label9
            // 
            this.label9.Location = new System.Drawing.Point(26, 187);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(104, 15);
            this.label9.TabIndex = 80;
            this.label9.Text = "Tax at withdrawl:";
            // 
            // txtPenalty
            // 
            this.txtPenalty.Location = new System.Drawing.Point(146, 165);
            this.txtPenalty.Name = "txtPenalty";
            this.txtPenalty.Size = new System.Drawing.Size(76, 22);
            this.txtPenalty.TabIndex = 64;
            this.txtPenalty.Text = "0%";
            this.txtPenalty.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label10
            // 
            this.label10.Location = new System.Drawing.Point(26, 165);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(104, 15);
            this.label10.TabIndex = 79;
            this.label10.Text = "Penalty:";
            // 
            // txtFinal401k
            // 
            this.txtFinal401k.Location = new System.Drawing.Point(447, 115);
            this.txtFinal401k.Name = "txtFinal401k";
            this.txtFinal401k.ReadOnly = true;
            this.txtFinal401k.Size = new System.Drawing.Size(76, 22);
            this.txtFinal401k.TabIndex = 68;
            this.txtFinal401k.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.ForeColor = System.Drawing.Color.Blue;
            this.label8.Location = new System.Drawing.Point(339, 115);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(43, 12);
            this.label8.TabIndex = 78;
            this.label8.Text = "401 (k):";
            // 
            // txtFinalSavings
            // 
            this.txtFinalSavings.Location = new System.Drawing.Point(447, 91);
            this.txtFinalSavings.Name = "txtFinalSavings";
            this.txtFinalSavings.ReadOnly = true;
            this.txtFinalSavings.Size = new System.Drawing.Size(76, 22);
            this.txtFinalSavings.TabIndex = 67;
            this.txtFinalSavings.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.ForeColor = System.Drawing.Color.Red;
            this.label7.Location = new System.Drawing.Point(339, 91);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(44, 12);
            this.label7.TabIndex = 77;
            this.label7.Text = "Savings:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(322, 75);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(63, 12);
            this.label6.TabIndex = 76;
            this.label6.Text = "Final results:";
            // 
            // picGraph
            // 
            this.picGraph.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraph.BackColor = System.Drawing.Color.White;
            this.picGraph.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraph.Location = new System.Drawing.Point(12, 211);
            this.picGraph.Name = "picGraph";
            this.picGraph.Size = new System.Drawing.Size(511, 425);
            this.picGraph.TabIndex = 75;
            this.picGraph.TabStop = false;
            // 
            // Label5
            // 
            this.Label5.Location = new System.Drawing.Point(26, 141);
            this.Label5.Name = "Label5";
            this.Label5.Size = new System.Drawing.Size(104, 15);
            this.Label5.TabIndex = 74;
            this.Label5.Text = "Years:";
            // 
            // btnGo
            // 
            this.btnGo.Location = new System.Drawing.Point(237, 139);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(75, 21);
            this.btnGo.TabIndex = 66;
            this.btnGo.Text = "Go";
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // txtInterestRate
            // 
            this.txtInterestRate.Location = new System.Drawing.Point(146, 119);
            this.txtInterestRate.Name = "txtInterestRate";
            this.txtInterestRate.Size = new System.Drawing.Size(76, 22);
            this.txtInterestRate.TabIndex = 63;
            this.txtInterestRate.Text = "9%";
            this.txtInterestRate.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label4
            // 
            this.Label4.Location = new System.Drawing.Point(26, 119);
            this.Label4.Name = "Label4";
            this.Label4.Size = new System.Drawing.Size(104, 15);
            this.Label4.TabIndex = 73;
            this.Label4.Text = "Annual interest rate:";
            // 
            // GroupBox1
            // 
            this.GroupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.GroupBox1.Controls.Add(this.Label3);
            this.GroupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GroupBox1.ForeColor = System.Drawing.Color.Red;
            this.GroupBox1.Location = new System.Drawing.Point(12, 11);
            this.GroupBox1.Name = "GroupBox1";
            this.GroupBox1.Size = new System.Drawing.Size(785, 58);
            this.GroupBox1.TabIndex = 72;
            this.GroupBox1.TabStop = false;
            this.GroupBox1.Text = "WARNING";
            // 
            // Label3
            // 
            this.Label3.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.Label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Label3.Location = new System.Drawing.Point(8, 15);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(769, 36);
            this.Label3.TabIndex = 0;
            this.Label3.Text = resources.GetString("Label3.Text");
            this.Label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // txtTaxRate
            // 
            this.txtTaxRate.Location = new System.Drawing.Point(146, 97);
            this.txtTaxRate.Name = "txtTaxRate";
            this.txtTaxRate.Size = new System.Drawing.Size(76, 22);
            this.txtTaxRate.TabIndex = 62;
            this.txtTaxRate.Text = "20%";
            this.txtTaxRate.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label2
            // 
            this.Label2.Location = new System.Drawing.Point(26, 97);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(104, 15);
            this.Label2.TabIndex = 71;
            this.Label2.Text = "Income tax rate:";
            // 
            // txtAnnualContribution
            // 
            this.txtAnnualContribution.Location = new System.Drawing.Point(146, 75);
            this.txtAnnualContribution.Name = "txtAnnualContribution";
            this.txtAnnualContribution.Size = new System.Drawing.Size(76, 22);
            this.txtAnnualContribution.TabIndex = 61;
            this.txtAnnualContribution.Text = "4000";
            this.txtAnnualContribution.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(26, 75);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(104, 15);
            this.Label1.TabIndex = 70;
            this.Label1.Text = "Annual contribution:";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(539, 211);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(258, 425);
            this.richTextBox1.TabIndex = 87;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGo;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(809, 647);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.txtRothSurrendered);
            this.Controls.Add(this.label13);
            this.Controls.Add(this.nudYears);
            this.Controls.Add(this.txtFinalRoth);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.txt401kSurrendered);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.txtTaxAtEnd);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.txtPenalty);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.txtFinal401k);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.txtFinalSavings);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.picGraph);
            this.Controls.Add(this.Label5);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.txtInterestRate);
            this.Controls.Add(this.Label4);
            this.Controls.Add(this.GroupBox1);
            this.Controls.Add(this.txtTaxRate);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtAnnualContribution);
            this.Controls.Add(this.Label1);
            this.Name = "Form1";
            this.Text = "howto_401k_graph";
            ((System.ComponentModel.ISupportInitialize)(this.nudYears)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).EndInit();
            this.GroupBox1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtRothSurrendered;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.NumericUpDown nudYears;
        private System.Windows.Forms.TextBox txtFinalRoth;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox txt401kSurrendered;
        private System.Windows.Forms.Label label11;
        internal System.Windows.Forms.TextBox txtTaxAtEnd;
        internal System.Windows.Forms.Label label9;
        internal System.Windows.Forms.TextBox txtPenalty;
        internal System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox txtFinal401k;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox txtFinalSavings;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.PictureBox picGraph;
        internal System.Windows.Forms.Label Label5;
        internal System.Windows.Forms.Button btnGo;
        internal System.Windows.Forms.TextBox txtInterestRate;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.GroupBox GroupBox1;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.TextBox txtTaxRate;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtAnnualContribution;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

