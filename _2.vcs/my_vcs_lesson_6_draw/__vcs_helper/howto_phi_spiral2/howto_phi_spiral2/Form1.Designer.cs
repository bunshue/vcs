namespace howto_phi_spiral2
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
            this.chkTrueSpiral = new System.Windows.Forms.CheckBox();
            this.chkCircularSpiral = new System.Windows.Forms.CheckBox();
            this.chkSquareSpiral = new System.Windows.Forms.CheckBox();
            this.chkRectangles = new System.Windows.Forms.CheckBox();
            this.picRectangles = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picRectangles)).BeginInit();
            this.SuspendLayout();
            // 
            // chkTrueSpiral
            // 
            this.chkTrueSpiral.AutoSize = true;
            this.chkTrueSpiral.Checked = true;
            this.chkTrueSpiral.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkTrueSpiral.ForeColor = System.Drawing.Color.Blue;
            this.chkTrueSpiral.Location = new System.Drawing.Point(301, 11);
            this.chkTrueSpiral.Name = "chkTrueSpiral";
            this.chkTrueSpiral.Size = new System.Drawing.Size(76, 16);
            this.chkTrueSpiral.TabIndex = 9;
            this.chkTrueSpiral.Text = "True Spiral";
            this.chkTrueSpiral.UseVisualStyleBackColor = true;
            this.chkTrueSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkCircularSpiral
            // 
            this.chkCircularSpiral.AutoSize = true;
            this.chkCircularSpiral.ForeColor = System.Drawing.Color.Red;
            this.chkCircularSpiral.Location = new System.Drawing.Point(201, 11);
            this.chkCircularSpiral.Name = "chkCircularSpiral";
            this.chkCircularSpiral.Size = new System.Drawing.Size(92, 16);
            this.chkCircularSpiral.TabIndex = 8;
            this.chkCircularSpiral.Text = "Circular Spiral";
            this.chkCircularSpiral.UseVisualStyleBackColor = true;
            this.chkCircularSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkSquareSpiral
            // 
            this.chkSquareSpiral.AutoSize = true;
            this.chkSquareSpiral.ForeColor = System.Drawing.Color.Green;
            this.chkSquareSpiral.Location = new System.Drawing.Point(102, 11);
            this.chkSquareSpiral.Name = "chkSquareSpiral";
            this.chkSquareSpiral.Size = new System.Drawing.Size(86, 16);
            this.chkSquareSpiral.TabIndex = 7;
            this.chkSquareSpiral.Text = "Square Spiral";
            this.chkSquareSpiral.UseVisualStyleBackColor = true;
            this.chkSquareSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkRectangles
            // 
            this.chkRectangles.AutoSize = true;
            this.chkRectangles.Checked = true;
            this.chkRectangles.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkRectangles.Location = new System.Drawing.Point(12, 11);
            this.chkRectangles.Name = "chkRectangles";
            this.chkRectangles.Size = new System.Drawing.Size(74, 16);
            this.chkRectangles.TabIndex = 6;
            this.chkRectangles.Text = "Rectangles";
            this.chkRectangles.UseVisualStyleBackColor = true;
            this.chkRectangles.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // picRectangles
            // 
            this.picRectangles.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picRectangles.BackColor = System.Drawing.Color.White;
            this.picRectangles.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picRectangles.Location = new System.Drawing.Point(12, 32);
            this.picRectangles.Name = "picRectangles";
            this.picRectangles.Size = new System.Drawing.Size(600, 398);
            this.picRectangles.TabIndex = 5;
            this.picRectangles.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(624, 442);
            this.Controls.Add(this.chkTrueSpiral);
            this.Controls.Add(this.chkCircularSpiral);
            this.Controls.Add(this.chkSquareSpiral);
            this.Controls.Add(this.chkRectangles);
            this.Controls.Add(this.picRectangles);
            this.Name = "Form1";
            this.Text = "howto_phi_spiral";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.picRectangles)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkTrueSpiral;
        private System.Windows.Forms.CheckBox chkCircularSpiral;
        private System.Windows.Forms.CheckBox chkSquareSpiral;
        private System.Windows.Forms.CheckBox chkRectangles;
        private System.Windows.Forms.PictureBox picRectangles;
    }
}

