namespace vcs_DrawH_StrangeAttractors
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
            this.chkDrawAxes = new System.Windows.Forms.CheckBox();
            this.cboCoefficients = new System.Windows.Forms.ComboBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.btnStart = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // chkDrawAxes
            // 
            this.chkDrawAxes.Location = new System.Drawing.Point(360, 3);
            this.chkDrawAxes.Name = "chkDrawAxes";
            this.chkDrawAxes.Size = new System.Drawing.Size(80, 15);
            this.chkDrawAxes.TabIndex = 9;
            this.chkDrawAxes.Text = "Draw Axes";
            this.chkDrawAxes.CheckedChanged += new System.EventHandler(this.chkDrawAxes_CheckedChanged);
            // 
            // cboCoefficients
            // 
            this.cboCoefficients.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboCoefficients.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cboCoefficients.Items.AddRange(new object[] {
            "AMTMNQQXUYGA -1.2 -0.1 -1.5 0.8",
            "CVQKGHQTPHTE -4 1.25 -0.75 1.75",
            "FIRCDERRPVLD -1.1 0.3 -0.75 0.75",
            "GIIETPIQRRUL -2.1 0.9 -0.8 0.85",
            "GLXOESFTTPSV -0.9 1.05 -1 0.85",
            "GXQSNSKEECTX -1.35 0.3 -1.35 0.2",
            "HGUHDPHNSGOH -0.4 0.7 -0.95 -0.15",
            "ILIBVPKJWGRR -0.7 0.4 -0.2 0.7",
            "LUFBBFISGJYS 0.1 2 -1.7 -0.2",
            "MCRBIPOPHTBN -0.8 1.1 -0.4 0.65",
            "MDVAIDOYHYEA -0.8 0.7 -1.1 0.75",
            "ODGQCNXODNYA -1.1 0.6 -0.1 1.5",
            "QFFVSLMJJGCR -1.1 0.8 -0.6 0.7",
            "UWACXDQIGKHF -0.4 1.2 -1.0 0.5",
            "VBWNBDELYHUL 0.15 1.05 -1.1 0.4",
            "WNCSLFLGIHGL -0.35 1.05 -1.25 0.5"});
            this.cboCoefficients.Location = new System.Drawing.Point(64, 0);
            this.cboCoefficients.Name = "cboCoefficients";
            this.cboCoefficients.Size = new System.Drawing.Size(264, 22);
            this.cboCoefficients.TabIndex = 8;
            this.cboCoefficients.SelectedIndexChanged += new System.EventHandler(this.cboCoefficients_SelectedIndexChanged);
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(0, 3);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(64, 15);
            this.Label1.TabIndex = 7;
            this.Label1.Text = "Coefficients";
            // 
            // timer1
            // 
            this.timer1.Interval = 10;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(0, 22);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(848, 522);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Resize += new System.EventHandler(this.pictureBox1_Resize);
            // 
            // btnStart
            // 
            this.btnStart.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnStart.Location = new System.Drawing.Point(772, 0);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(75, 21);
            this.btnStart.TabIndex = 5;
            this.btnStart.Text = "Start";
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnStart;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(848, 521);
            this.Controls.Add(this.chkDrawAxes);
            this.Controls.Add(this.cboCoefficients);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.btnStart);
            this.Name = "Form1";
            this.Text = "vcs_DrawH_StrangeAttractors";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.CheckBox chkDrawAxes;
        internal System.Windows.Forms.ComboBox cboCoefficients;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Timer timer1;
        internal System.Windows.Forms.PictureBox pictureBox1;
        internal System.Windows.Forms.Button btnStart;
    }
}

