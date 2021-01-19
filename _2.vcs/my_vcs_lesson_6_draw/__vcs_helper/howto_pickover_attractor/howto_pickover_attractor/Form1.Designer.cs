namespace howto_pickover_attractor
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
            this.btnStart = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.lblForeColor = new System.Windows.Forms.Label();
            this.lblBackColor = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.cboPlane = new System.Windows.Forms.ComboBox();
            this.cdColor = new System.Windows.Forms.ColorDialog();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.txtA = new System.Windows.Forms.TextBox();
            this.txtB = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.txtC = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtD = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.txtE = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.txtZ0 = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.txtY0 = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.txtX0 = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(266, 78);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(75, 23);
            this.btnStart.TabIndex = 9;
            this.btnStart.Text = "Start";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(14, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Foreground";
            // 
            // lblForeColor
            // 
            this.lblForeColor.BackColor = System.Drawing.Color.Blue;
            this.lblForeColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblForeColor.Location = new System.Drawing.Point(81, 25);
            this.lblForeColor.Name = "lblForeColor";
            this.lblForeColor.Size = new System.Drawing.Size(20, 20);
            this.lblForeColor.TabIndex = 3;
            this.lblForeColor.Click += new System.EventHandler(this.ColorSample_Click);
            // 
            // lblBackColor
            // 
            this.lblBackColor.BackColor = System.Drawing.Color.Black;
            this.lblBackColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblBackColor.Location = new System.Drawing.Point(81, 51);
            this.lblBackColor.Name = "lblBackColor";
            this.lblBackColor.Size = new System.Drawing.Size(20, 20);
            this.lblBackColor.TabIndex = 5;
            this.lblBackColor.Click += new System.EventHandler(this.ColorSample_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(14, 52);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "Background";
            // 
            // cboPlane
            // 
            this.cboPlane.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboPlane.FormattingEnabled = true;
            this.cboPlane.Items.AddRange(new object[] {
            "XY",
            "YZ",
            "XZ"});
            this.cboPlane.Location = new System.Drawing.Point(81, 75);
            this.cboPlane.Name = "cboPlane";
            this.cboPlane.Size = new System.Drawing.Size(41, 21);
            this.cboPlane.TabIndex = 0;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(14, 78);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(34, 13);
            this.label2.TabIndex = 7;
            this.label2.Text = "Plane";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.txtZ0);
            this.groupBox1.Controls.Add(this.btnStart);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.txtY0);
            this.groupBox1.Controls.Add(this.label10);
            this.groupBox1.Controls.Add(this.txtX0);
            this.groupBox1.Controls.Add(this.label11);
            this.groupBox1.Controls.Add(this.txtE);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.txtD);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.txtC);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.txtB);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.txtA);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.lblForeColor);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.cboPlane);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.lblBackColor);
            this.groupBox1.Location = new System.Drawing.Point(12, 9);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(506, 110);
            this.groupBox1.TabIndex = 8;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Parameters";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(162, 26);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(14, 13);
            this.label4.TabIndex = 9;
            this.label4.Text = "A";
            // 
            // txtA
            // 
            this.txtA.Location = new System.Drawing.Point(182, 23);
            this.txtA.Name = "txtA";
            this.txtA.Size = new System.Drawing.Size(33, 20);
            this.txtA.TabIndex = 1;
            this.txtA.Text = "2.0";
            this.txtA.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtB
            // 
            this.txtB.Location = new System.Drawing.Point(252, 23);
            this.txtB.Name = "txtB";
            this.txtB.Size = new System.Drawing.Size(33, 20);
            this.txtB.TabIndex = 2;
            this.txtB.Text = "0.5";
            this.txtB.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(232, 26);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(14, 13);
            this.label5.TabIndex = 11;
            this.label5.Text = "B";
            // 
            // txtC
            // 
            this.txtC.Location = new System.Drawing.Point(322, 23);
            this.txtC.Name = "txtC";
            this.txtC.Size = new System.Drawing.Size(33, 20);
            this.txtC.TabIndex = 3;
            this.txtC.Text = "-0.6";
            this.txtC.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(301, 26);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(14, 13);
            this.label6.TabIndex = 13;
            this.label6.Text = "C";
            // 
            // txtD
            // 
            this.txtD.Location = new System.Drawing.Point(392, 23);
            this.txtD.Name = "txtD";
            this.txtD.Size = new System.Drawing.Size(33, 20);
            this.txtD.TabIndex = 4;
            this.txtD.Text = "-2.5";
            this.txtD.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(371, 26);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(15, 13);
            this.label7.TabIndex = 15;
            this.label7.Text = "D";
            // 
            // txtE
            // 
            this.txtE.Location = new System.Drawing.Point(462, 23);
            this.txtE.Name = "txtE";
            this.txtE.Size = new System.Drawing.Size(33, 20);
            this.txtE.TabIndex = 5;
            this.txtE.Text = "1.0";
            this.txtE.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(441, 26);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(14, 13);
            this.label8.TabIndex = 17;
            this.label8.Text = "E";
            // 
            // txtZ0
            // 
            this.txtZ0.Location = new System.Drawing.Point(322, 49);
            this.txtZ0.Name = "txtZ0";
            this.txtZ0.Size = new System.Drawing.Size(33, 20);
            this.txtZ0.TabIndex = 8;
            this.txtZ0.Text = "0";
            this.txtZ0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(301, 52);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(20, 13);
            this.label9.TabIndex = 24;
            this.label9.Text = "Z0";
            // 
            // txtY0
            // 
            this.txtY0.Location = new System.Drawing.Point(252, 49);
            this.txtY0.Name = "txtY0";
            this.txtY0.Size = new System.Drawing.Size(33, 20);
            this.txtY0.TabIndex = 7;
            this.txtY0.Text = "0";
            this.txtY0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(232, 52);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(20, 13);
            this.label10.TabIndex = 22;
            this.label10.Text = "Y0";
            // 
            // txtX0
            // 
            this.txtX0.Location = new System.Drawing.Point(182, 49);
            this.txtX0.Name = "txtX0";
            this.txtX0.Size = new System.Drawing.Size(33, 20);
            this.txtX0.TabIndex = 6;
            this.txtX0.Text = "0";
            this.txtX0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(162, 52);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(20, 13);
            this.label11.TabIndex = 20;
            this.label11.Text = "X0";
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(12, 125);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(506, 506);
            this.picCanvas.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.picCanvas.TabIndex = 9;
            this.picCanvas.TabStop = false;
            this.picCanvas.Resize += new System.EventHandler(this.picCanvas_Resize);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnStart;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(530, 643);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "howto_pickover_attractor";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblForeColor;
        private System.Windows.Forms.Label lblBackColor;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox cboPlane;
        private System.Windows.Forms.ColorDialog cdColor;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtE;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox txtD;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox txtC;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtB;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtA;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtZ0;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox txtY0;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox txtX0;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.PictureBox picCanvas;
    }
}

