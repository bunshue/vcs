namespace howto_draw_ngon_stars
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
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.btnGo = new System.Windows.Forms.Button();
            this.Label1 = new System.Windows.Forms.Label();
            this.txtNumPoints = new System.Windows.Forms.TextBox();
            this.chkRelPrimeOnly = new System.Windows.Forms.CheckBox();
            this.chkHalfOnly = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(12, 39);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(466, 466);
            this.picCanvas.TabIndex = 7;
            this.picCanvas.TabStop = false;
            this.picCanvas.Resize += new System.EventHandler(this.picCanvas_Resize);
            this.picCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            // 
            // btnGo
            // 
            this.btnGo.Location = new System.Drawing.Point(104, 10);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(48, 23);
            this.btnGo.TabIndex = 6;
            this.btnGo.Text = "Go";
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(12, 15);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(48, 16);
            this.Label1.TabIndex = 5;
            this.Label1.Text = "# Points";
            // 
            // txtNumPoints
            // 
            this.txtNumPoints.Location = new System.Drawing.Point(66, 12);
            this.txtNumPoints.Name = "txtNumPoints";
            this.txtNumPoints.Size = new System.Drawing.Size(32, 20);
            this.txtNumPoints.TabIndex = 4;
            this.txtNumPoints.Text = "7";
            // 
            // chkRelPrimeOnly
            // 
            this.chkRelPrimeOnly.AutoSize = true;
            this.chkRelPrimeOnly.Location = new System.Drawing.Point(192, 14);
            this.chkRelPrimeOnly.Name = "chkRelPrimeOnly";
            this.chkRelPrimeOnly.Size = new System.Drawing.Size(122, 17);
            this.chkRelPrimeOnly.TabIndex = 8;
            this.chkRelPrimeOnly.Text = "Relatively prime only";
            this.chkRelPrimeOnly.UseVisualStyleBackColor = true;
            // 
            // chkHalfOnly
            // 
            this.chkHalfOnly.AutoSize = true;
            this.chkHalfOnly.Location = new System.Drawing.Point(320, 14);
            this.chkHalfOnly.Name = "chkHalfOnly";
            this.chkHalfOnly.Size = new System.Drawing.Size(67, 17);
            this.chkHalfOnly.TabIndex = 9;
            this.chkHalfOnly.Text = "Half only";
            this.chkHalfOnly.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGo;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(490, 517);
            this.Controls.Add(this.chkHalfOnly);
            this.Controls.Add(this.chkRelPrimeOnly);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.txtNumPoints);
            this.Name = "Form1";
            this.Text = "howto_draw_ngon_stars";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.PictureBox picCanvas;
        internal System.Windows.Forms.Button btnGo;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.TextBox txtNumPoints;
        private System.Windows.Forms.CheckBox chkRelPrimeOnly;
        private System.Windows.Forms.CheckBox chkHalfOnly;
    }
}

