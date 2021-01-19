namespace howto_crypto_random_numbers
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
            this.txtMax = new System.Windows.Forms.TextBox();
            this.Label3 = new System.Windows.Forms.Label();
            this.txtMin = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtNumNumbers = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.picGraphRandom = new System.Windows.Forms.PictureBox();
            this.lblRandom = new System.Windows.Forms.Label();
            this.picGraphRNG = new System.Windows.Forms.PictureBox();
            this.lblRng = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picGraphRandom)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGraphRNG)).BeginInit();
            this.SuspendLayout();
            // 
            // txtMax
            // 
            this.txtMax.Location = new System.Drawing.Point(80, 55);
            this.txtMax.Name = "txtMax";
            this.txtMax.Size = new System.Drawing.Size(56, 20);
            this.txtMax.TabIndex = 15;
            this.txtMax.Text = "100";
            this.txtMax.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Location = new System.Drawing.Point(8, 55);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(30, 13);
            this.Label3.TabIndex = 14;
            this.Label3.Text = "Max:";
            // 
            // txtMin
            // 
            this.txtMin.Location = new System.Drawing.Point(80, 31);
            this.txtMin.Name = "txtMin";
            this.txtMin.Size = new System.Drawing.Size(56, 20);
            this.txtMin.TabIndex = 13;
            this.txtMin.Text = "1";
            this.txtMin.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(8, 31);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(27, 13);
            this.Label2.TabIndex = 12;
            this.Label2.Text = "Min:";
            // 
            // txtNumNumbers
            // 
            this.txtNumNumbers.Location = new System.Drawing.Point(80, 7);
            this.txtNumNumbers.Name = "txtNumNumbers";
            this.txtNumNumbers.Size = new System.Drawing.Size(56, 20);
            this.txtNumNumbers.TabIndex = 10;
            this.txtNumNumbers.Text = "1000";
            this.txtNumNumbers.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(8, 7);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(62, 13);
            this.Label1.TabIndex = 9;
            this.Label1.Text = "# Numbers:";
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(184, 31);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(75, 23);
            this.btnGenerate.TabIndex = 8;
            this.btnGenerate.Text = "Generate";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // picGraphRandom
            // 
            this.picGraphRandom.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraphRandom.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraphRandom.Location = new System.Drawing.Point(11, 97);
            this.picGraphRandom.Name = "picGraphRandom";
            this.picGraphRandom.Size = new System.Drawing.Size(807, 162);
            this.picGraphRandom.TabIndex = 16;
            this.picGraphRandom.TabStop = false;
            // 
            // lblRandom
            // 
            this.lblRandom.AutoSize = true;
            this.lblRandom.Location = new System.Drawing.Point(12, 81);
            this.lblRandom.Name = "lblRandom";
            this.lblRandom.Size = new System.Drawing.Size(47, 13);
            this.lblRandom.TabIndex = 17;
            this.lblRandom.Text = "Random";
            // 
            // picGraphRNG
            // 
            this.picGraphRNG.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraphRNG.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraphRNG.Location = new System.Drawing.Point(11, 287);
            this.picGraphRNG.Name = "picGraphRNG";
            this.picGraphRNG.Size = new System.Drawing.Size(807, 162);
            this.picGraphRNG.TabIndex = 18;
            this.picGraphRNG.TabStop = false;
            // 
            // lblRng
            // 
            this.lblRng.AutoSize = true;
            this.lblRng.Location = new System.Drawing.Point(8, 271);
            this.lblRng.Name = "lblRng";
            this.lblRng.Size = new System.Drawing.Size(136, 13);
            this.lblRng.TabIndex = 19;
            this.lblRng.Text = "RNGCryptoServiceProvider";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGenerate;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(830, 462);
            this.Controls.Add(this.lblRng);
            this.Controls.Add(this.picGraphRNG);
            this.Controls.Add(this.lblRandom);
            this.Controls.Add(this.picGraphRandom);
            this.Controls.Add(this.txtMax);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.txtMin);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtNumNumbers);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.btnGenerate);
            this.Name = "Form1";
            this.Text = "howto_crypto_random_numbers";
            ((System.ComponentModel.ISupportInitialize)(this.picGraphRandom)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGraphRNG)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.TextBox txtMax;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.TextBox txtMin;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtNumNumbers;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Button btnGenerate;
        private System.Windows.Forms.PictureBox picGraphRandom;
        private System.Windows.Forms.Label lblRandom;
        private System.Windows.Forms.PictureBox picGraphRNG;
        private System.Windows.Forms.Label lblRng;
    }
}

