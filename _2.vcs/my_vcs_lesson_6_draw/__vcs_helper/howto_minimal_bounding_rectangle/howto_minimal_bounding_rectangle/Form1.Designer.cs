namespace howto_minimal_bounding_rectangle
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
            this.lblBestArea = new System.Windows.Forms.Label();
            this.Label3 = new System.Windows.Forms.Label();
            this.lblCurrentArea = new System.Windows.Forms.Label();
            this.Label1 = new System.Windows.Forms.Label();
            this.btnStep = new System.Windows.Forms.Button();
            this.btnReset = new System.Windows.Forms.Button();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // lblBestArea
            // 
            this.lblBestArea.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.lblBestArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblBestArea.Location = new System.Drawing.Point(704, 155);
            this.lblBestArea.Name = "lblBestArea";
            this.lblBestArea.Size = new System.Drawing.Size(72, 15);
            this.lblBestArea.TabIndex = 13;
            this.lblBestArea.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Label3
            // 
            this.Label3.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Label3.Location = new System.Drawing.Point(704, 140);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(72, 15);
            this.Label3.TabIndex = 12;
            this.Label3.Text = "Best Area";
            this.Label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblCurrentArea
            // 
            this.lblCurrentArea.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.lblCurrentArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCurrentArea.Location = new System.Drawing.Point(704, 103);
            this.lblCurrentArea.Name = "lblCurrentArea";
            this.lblCurrentArea.Size = new System.Drawing.Size(72, 15);
            this.lblCurrentArea.TabIndex = 11;
            this.lblCurrentArea.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Label1
            // 
            this.Label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Label1.Location = new System.Drawing.Point(704, 89);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(72, 15);
            this.Label1.TabIndex = 10;
            this.Label1.Text = "Current Area";
            this.Label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // btnStep
            // 
            this.btnStep.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnStep.Location = new System.Drawing.Point(704, 44);
            this.btnStep.Name = "btnStep";
            this.btnStep.Size = new System.Drawing.Size(72, 30);
            this.btnStep.TabIndex = 9;
            this.btnStep.Text = "Step";
            this.btnStep.Click += new System.EventHandler(this.btnStep_Click);
            // 
            // btnReset
            // 
            this.btnReset.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnReset.Location = new System.Drawing.Point(704, 7);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(72, 30);
            this.btnReset.TabIndex = 8;
            this.btnReset.Text = "Reset";
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BackColor = System.Drawing.Color.White;
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(12, 11);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(686, 529);
            this.picCanvas.TabIndex = 7;
            this.picCanvas.TabStop = false;
            this.picCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 551);
            this.Controls.Add(this.lblBestArea);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.lblCurrentArea);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.btnStep);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.picCanvas);
            this.Name = "Form1";
            this.Text = "howto_minimal_bounding_rectangle";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.Label lblBestArea;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.Label lblCurrentArea;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Button btnStep;
        internal System.Windows.Forms.Button btnReset;
        internal System.Windows.Forms.PictureBox picCanvas;
    }
}

