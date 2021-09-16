namespace WinMultiForm
{
    partial class frmCal
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
            this.rdbMonth = new System.Windows.Forms.RadioButton();
            this.rdbYear = new System.Windows.Forms.RadioButton();
            this.SuspendLayout();
            // 
            // rdbMonth
            // 
            this.rdbMonth.AutoSize = true;
            this.rdbMonth.Location = new System.Drawing.Point(55, 80);
            this.rdbMonth.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbMonth.Name = "rdbMonth";
            this.rdbMonth.Size = new System.Drawing.Size(85, 19);
            this.rdbMonth.TabIndex = 3;
            this.rdbMonth.TabStop = true;
            this.rdbMonth.Text = "每月計息";
            this.rdbMonth.UseVisualStyleBackColor = true;
            // 
            // rdbYear
            // 
            this.rdbYear.AutoSize = true;
            this.rdbYear.Checked = true;
            this.rdbYear.Location = new System.Drawing.Point(55, 36);
            this.rdbYear.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbYear.Name = "rdbYear";
            this.rdbYear.Size = new System.Drawing.Size(85, 19);
            this.rdbYear.TabIndex = 2;
            this.rdbYear.TabStop = true;
            this.rdbYear.Text = "每年計息";
            this.rdbYear.UseVisualStyleBackColor = true;
            // 
            // frmCal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(240, 194);
            this.Controls.Add(this.rdbMonth);
            this.Controls.Add(this.rdbYear);
            this.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "frmCal";
            this.Text = "選擇計息";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton rdbMonth;
        private System.Windows.Forms.RadioButton rdbYear;
    }
}