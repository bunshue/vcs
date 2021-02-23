namespace howto_rotating_arms
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
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.txtD = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.txtRadius = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.txtL3 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tmrTurnWheel = new System.Windows.Forms.Timer(this.components);
            this.txtL2 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtL1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnStartStop = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(99, 12);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(273, 240);
            this.picCanvas.TabIndex = 22;
            this.picCanvas.TabStop = false;
            // 
            // txtD
            // 
            this.txtD.Location = new System.Drawing.Point(43, 12);
            this.txtD.Name = "txtD";
            this.txtD.Size = new System.Drawing.Size(50, 20);
            this.txtD.TabIndex = 11;
            this.txtD.Text = "100";
            this.txtD.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 15);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(18, 13);
            this.label5.TabIndex = 21;
            this.label5.Text = "D:";
            // 
            // txtRadius
            // 
            this.txtRadius.Location = new System.Drawing.Point(43, 116);
            this.txtRadius.Name = "txtRadius";
            this.txtRadius.Size = new System.Drawing.Size(50, 20);
            this.txtRadius.TabIndex = 17;
            this.txtRadius.Text = "30";
            this.txtRadius.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 119);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(18, 13);
            this.label4.TabIndex = 20;
            this.label4.Text = "R:";
            // 
            // txtL3
            // 
            this.txtL3.Location = new System.Drawing.Point(43, 90);
            this.txtL3.Name = "txtL3";
            this.txtL3.Size = new System.Drawing.Size(50, 20);
            this.txtL3.TabIndex = 15;
            this.txtL3.Text = "60";
            this.txtL3.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 93);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(22, 13);
            this.label3.TabIndex = 18;
            this.label3.Text = "L3:";
            // 
            // tmrTurnWheel
            // 
            this.tmrTurnWheel.Tick += new System.EventHandler(this.tmrTurnWheel_Tick);
            // 
            // txtL2
            // 
            this.txtL2.Location = new System.Drawing.Point(43, 64);
            this.txtL2.Name = "txtL2";
            this.txtL2.Size = new System.Drawing.Size(50, 20);
            this.txtL2.TabIndex = 14;
            this.txtL2.Text = "110";
            this.txtL2.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 67);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 13);
            this.label2.TabIndex = 16;
            this.label2.Text = "L2:";
            // 
            // txtL1
            // 
            this.txtL1.Location = new System.Drawing.Point(43, 38);
            this.txtL1.Name = "txtL1";
            this.txtL1.Size = new System.Drawing.Size(50, 20);
            this.txtL1.TabIndex = 13;
            this.txtL1.Text = "100";
            this.txtL1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(22, 13);
            this.label1.TabIndex = 12;
            this.label1.Text = "L1:";
            // 
            // btnStartStop
            // 
            this.btnStartStop.Location = new System.Drawing.Point(15, 142);
            this.btnStartStop.Name = "btnStartStop";
            this.btnStartStop.Size = new System.Drawing.Size(78, 23);
            this.btnStartStop.TabIndex = 19;
            this.btnStartStop.Text = "Start";
            this.btnStartStop.UseVisualStyleBackColor = true;
            this.btnStartStop.Click += new System.EventHandler(this.btnStartStop_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnStartStop;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(384, 264);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.txtD);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.txtRadius);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txtL3);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtL2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtL1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnStartStop);
            this.Name = "Form1";
            this.Text = "howto_rotating_arms";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picCanvas;
        private System.Windows.Forms.TextBox txtD;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtRadius;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtL3;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Timer tmrTurnWheel;
        private System.Windows.Forms.TextBox txtL2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtL1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnStartStop;
    }
}

