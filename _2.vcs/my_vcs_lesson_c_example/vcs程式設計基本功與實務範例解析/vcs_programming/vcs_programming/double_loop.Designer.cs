namespace vcs_programming
{
    partial class double_loop
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
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.txtRows = new System.Windows.Forms.TextBox();
            this.btnDigitRow = new System.Windows.Forms.Button();
            this.btn99 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(12, 12);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(307, 186);
            this.txtOutput.TabIndex = 0;
            this.txtOutput.WordWrap = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(14, 224);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(71, 16);
            this.label1.TabIndex = 1;
            this.label1.Text = "列數(1-9)";
            // 
            // txtRows
            // 
            this.txtRows.Location = new System.Drawing.Point(91, 213);
            this.txtRows.Name = "txtRows";
            this.txtRows.Size = new System.Drawing.Size(100, 27);
            this.txtRows.TabIndex = 2;
            // 
            // btnDigitRow
            // 
            this.btnDigitRow.Location = new System.Drawing.Point(197, 213);
            this.btnDigitRow.Name = "btnDigitRow";
            this.btnDigitRow.Size = new System.Drawing.Size(122, 27);
            this.btnDigitRow.TabIndex = 3;
            this.btnDigitRow.Text = "顯示";
            this.btnDigitRow.UseVisualStyleBackColor = true;
            this.btnDigitRow.Click += new System.EventHandler(this.btnDigitRow_Click);
            // 
            // btn99
            // 
            this.btn99.Location = new System.Drawing.Point(17, 257);
            this.btn99.Name = "btn99";
            this.btn99.Size = new System.Drawing.Size(302, 30);
            this.btn99.TabIndex = 4;
            this.btn99.Text = "九九乘法表";
            this.btn99.UseVisualStyleBackColor = true;
            this.btn99.Click += new System.EventHandler(this.btn99_Click);
            // 
            // double_loop
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(336, 303);
            this.Controls.Add(this.btn99);
            this.Controls.Add(this.btnDigitRow);
            this.Controls.Add(this.txtRows);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtOutput);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "double_loop";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "雙迴圈";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtRows;
        private System.Windows.Forms.Button btnDigitRow;
        private System.Windows.Forms.Button btn99;
    }
}