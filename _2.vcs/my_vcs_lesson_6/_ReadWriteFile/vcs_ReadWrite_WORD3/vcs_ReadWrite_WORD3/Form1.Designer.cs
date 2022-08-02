namespace vcs_ReadWrite_WORD3
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
            this.label1 = new System.Windows.Forms.Label();
            this.cboTimeZone1 = new System.Windows.Forms.ComboBox();
            this.cboTimeZone2 = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnMakeChart = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.dtpDate = new System.Windows.Forms.DateTimePicker();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 38);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Time Zone 1:";
            // 
            // cboTimeZone1
            // 
            this.cboTimeZone1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.cboTimeZone1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboTimeZone1.FormattingEnabled = true;
            this.cboTimeZone1.Location = new System.Drawing.Point(88, 35);
            this.cboTimeZone1.Name = "cboTimeZone1";
            this.cboTimeZone1.Size = new System.Drawing.Size(520, 20);
            this.cboTimeZone1.Sorted = true;
            this.cboTimeZone1.TabIndex = 1;
            // 
            // cboTimeZone2
            // 
            this.cboTimeZone2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.cboTimeZone2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboTimeZone2.FormattingEnabled = true;
            this.cboTimeZone2.Location = new System.Drawing.Point(88, 60);
            this.cboTimeZone2.Name = "cboTimeZone2";
            this.cboTimeZone2.Size = new System.Drawing.Size(520, 20);
            this.cboTimeZone2.Sorted = true;
            this.cboTimeZone2.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 63);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(68, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Time Zone 2:";
            // 
            // btnMakeChart
            // 
            this.btnMakeChart.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnMakeChart.Location = new System.Drawing.Point(14, 110);
            this.btnMakeChart.Name = "btnMakeChart";
            this.btnMakeChart.Size = new System.Drawing.Size(108, 52);
            this.btnMakeChart.TabIndex = 4;
            this.btnMakeChart.Text = "製作一個docx檔案 使用表格";
            this.btnMakeChart.UseVisualStyleBackColor = true;
            this.btnMakeChart.Click += new System.EventHandler(this.btnMakeChart_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 17);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(29, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "Date:";
            // 
            // dtpDate
            // 
            this.dtpDate.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.dtpDate.Location = new System.Drawing.Point(88, 11);
            this.dtpDate.Name = "dtpDate";
            this.dtpDate.Size = new System.Drawing.Size(520, 22);
            this.dtpDate.TabIndex = 6;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(14, 186);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(594, 275);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnMakeChart;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(620, 473);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.dtpDate);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.btnMakeChart);
            this.Controls.Add(this.cboTimeZone2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.cboTimeZone1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_hour_conversion_chart";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cboTimeZone1;
        private System.Windows.Forms.ComboBox cboTimeZone2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnMakeChart;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.DateTimePicker dtpDate;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

