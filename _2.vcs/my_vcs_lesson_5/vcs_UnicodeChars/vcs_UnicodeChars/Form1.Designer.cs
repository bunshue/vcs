namespace vcs_UnicodeChars
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
            this.txtChars = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.txtMin = new System.Windows.Forms.TextBox();
            this.txtMax = new System.Windows.Forms.TextBox();
            this.btnList = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.txtFontSize = new System.Windows.Forms.TextBox();
            this.txtCharCode = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.lblSample = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtChars
            // 
            this.txtChars.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtChars.BackColor = System.Drawing.Color.White;
            this.txtChars.Cursor = System.Windows.Forms.Cursors.Cross;
            this.txtChars.Font = new System.Drawing.Font("Times New Roman", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtChars.Location = new System.Drawing.Point(16, 47);
            this.txtChars.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtChars.Multiline = true;
            this.txtChars.Name = "txtChars";
            this.txtChars.ReadOnly = true;
            this.txtChars.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtChars.Size = new System.Drawing.Size(932, 469);
            this.txtChars.TabIndex = 4;
            this.txtChars.MouseMove += new System.Windows.Forms.MouseEventHandler(this.txtChars_MouseMove);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(136, 20);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(18, 15);
            this.label1.TabIndex = 1;
            this.label1.Text = "to";
            // 
            // txtMin
            // 
            this.txtMin.Location = new System.Drawing.Point(73, 16);
            this.txtMin.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtMin.Name = "txtMin";
            this.txtMin.Size = new System.Drawing.Size(59, 25);
            this.txtMin.TabIndex = 0;
            this.txtMin.Text = "10000";
            this.txtMin.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtMax
            // 
            this.txtMax.Location = new System.Drawing.Point(156, 16);
            this.txtMax.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtMax.Name = "txtMax";
            this.txtMax.Size = new System.Drawing.Size(59, 25);
            this.txtMax.TabIndex = 1;
            this.txtMax.Text = "20000";
            this.txtMax.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnList
            // 
            this.btnList.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnList.Location = new System.Drawing.Point(850, 14);
            this.btnList.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnList.Name = "btnList";
            this.btnList.Size = new System.Drawing.Size(100, 27);
            this.btnList.TabIndex = 3;
            this.btnList.Text = "List";
            this.btnList.UseVisualStyleBackColor = true;
            this.btnList.Click += new System.EventHandler(this.btnList_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(16, 20);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(43, 15);
            this.label2.TabIndex = 5;
            this.label2.Text = "Chars:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(251, 20);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 15);
            this.label3.TabIndex = 7;
            this.label3.Text = "Font Size:";
            // 
            // txtFontSize
            // 
            this.txtFontSize.Location = new System.Drawing.Point(331, 16);
            this.txtFontSize.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtFontSize.Name = "txtFontSize";
            this.txtFontSize.Size = new System.Drawing.Size(39, 25);
            this.txtFontSize.TabIndex = 2;
            this.txtFontSize.Text = "20";
            this.txtFontSize.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtCharCode
            // 
            this.txtCharCode.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txtCharCode.Location = new System.Drawing.Point(136, 524);
            this.txtCharCode.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtCharCode.Name = "txtCharCode";
            this.txtCharCode.ReadOnly = true;
            this.txtCharCode.Size = new System.Drawing.Size(59, 25);
            this.txtCharCode.TabIndex = 5;
            this.txtCharCode.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(16, 528);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(98, 15);
            this.label4.TabIndex = 9;
            this.label4.Text = "Character Code:";
            // 
            // lblSample
            // 
            this.lblSample.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.lblSample.AutoSize = true;
            this.lblSample.Location = new System.Drawing.Point(204, 521);
            this.lblSample.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblSample.Name = "lblSample";
            this.lblSample.Size = new System.Drawing.Size(0, 15);
            this.lblSample.TabIndex = 10;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnList;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(966, 561);
            this.Controls.Add(this.lblSample);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txtCharCode);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtFontSize);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnList);
            this.Controls.Add(this.txtMax);
            this.Controls.Add(this.txtMin);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtChars);
            this.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.MinimumSize = new System.Drawing.Size(527, 224);
            this.Name = "Form1";
            this.Text = "vcs_UnicodeChars";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtChars;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtMin;
        private System.Windows.Forms.TextBox txtMax;
        private System.Windows.Forms.Button btnList;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtFontSize;
        private System.Windows.Forms.TextBox txtCharCode;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label lblSample;
    }
}

