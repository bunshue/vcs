namespace vcs_DrawA_Radar
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
            this.picPlot = new System.Windows.Forms.PictureBox();
            this.tipPoint = new System.Windows.Forms.ToolTip(this.components);
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.chkFillAreas = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.picPlot)).BeginInit();
            this.SuspendLayout();
            // 
            // picPlot
            // 
            this.picPlot.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picPlot.BackColor = System.Drawing.Color.White;
            this.picPlot.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picPlot.Location = new System.Drawing.Point(94, 12);
            this.picPlot.Name = "picPlot";
            this.picPlot.Size = new System.Drawing.Size(310, 310);
            this.picPlot.TabIndex = 0;
            this.picPlot.TabStop = false;
            this.picPlot.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picPlot_MouseMove);
            this.picPlot.Resize += new System.EventHandler(this.picPlot_Resize);
            this.picPlot.Paint += new System.Windows.Forms.PaintEventHandler(this.picPlot_Paint);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.ForeColor = System.Drawing.Color.Red;
            this.label1.Location = new System.Drawing.Point(12, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Audi e-tron";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.ForeColor = System.Drawing.Color.Green;
            this.label2.Location = new System.Drawing.Point(12, 33);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(76, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Jaguar I-PACE";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.Color.Blue;
            this.label3.Location = new System.Drawing.Point(12, 54);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(54, 13);
            this.label3.TabIndex = 2;
            this.label3.Text = "Polestar 2";
            // 
            // chkFillAreas
            // 
            this.chkFillAreas.AutoSize = true;
            this.chkFillAreas.Location = new System.Drawing.Point(12, 98);
            this.chkFillAreas.Name = "chkFillAreas";
            this.chkFillAreas.Size = new System.Drawing.Size(68, 17);
            this.chkFillAreas.TabIndex = 3;
            this.chkFillAreas.Text = "Fill Areas";
            this.chkFillAreas.UseVisualStyleBackColor = true;
            this.chkFillAreas.CheckedChanged += new System.EventHandler(this.chkFillAreas_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(416, 334);
            this.Controls.Add(this.chkFillAreas);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picPlot);
            this.Name = "Form1";
            this.Text = "vcs_DrawA_Radar";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picPlot)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picPlot;
        private System.Windows.Forms.ToolTip tipPoint;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.CheckBox chkFillAreas;
    }
}

