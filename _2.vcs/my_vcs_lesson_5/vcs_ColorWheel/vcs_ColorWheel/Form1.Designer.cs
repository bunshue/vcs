namespace vcs_ColorWheel
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
            this.picWheel = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.hscrSaturation = new System.Windows.Forms.HScrollBar();
            this.hscrAlpha = new System.Windows.Forms.HScrollBar();
            this.txtAlpha = new System.Windows.Forms.TextBox();
            this.txtSaturation = new System.Windows.Forms.TextBox();
            this.picSample = new System.Windows.Forms.PictureBox();
            this.btnColor2 = new System.Windows.Forms.Button();
            this.btnColor1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picWheel)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            this.SuspendLayout();
            // 
            // picWheel
            // 
            this.picWheel.Location = new System.Drawing.Point(25, 25);
            this.picWheel.Name = "picWheel";
            this.picWheel.Size = new System.Drawing.Size(200, 200);
            this.picWheel.TabIndex = 18;
            this.picWheel.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(29, 267);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 12);
            this.label2.TabIndex = 17;
            this.label2.Text = "Saturation:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 243);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(36, 12);
            this.label1.TabIndex = 16;
            this.label1.Text = "Alpha:";
            // 
            // hscrSaturation
            // 
            this.hscrSaturation.Location = new System.Drawing.Point(90, 266);
            this.hscrSaturation.Maximum = 264;
            this.hscrSaturation.Name = "hscrSaturation";
            this.hscrSaturation.Size = new System.Drawing.Size(105, 16);
            this.hscrSaturation.TabIndex = 15;
            this.hscrSaturation.Value = 255;
            this.hscrSaturation.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hscrSaturation_Scroll);
            // 
            // hscrAlpha
            // 
            this.hscrAlpha.Location = new System.Drawing.Point(90, 242);
            this.hscrAlpha.Maximum = 264;
            this.hscrAlpha.Name = "hscrAlpha";
            this.hscrAlpha.Size = new System.Drawing.Size(105, 16);
            this.hscrAlpha.TabIndex = 14;
            this.hscrAlpha.Value = 255;
            this.hscrAlpha.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hscrAlpha_Scroll);
            // 
            // txtAlpha
            // 
            this.txtAlpha.Location = new System.Drawing.Point(198, 240);
            this.txtAlpha.Name = "txtAlpha";
            this.txtAlpha.ReadOnly = true;
            this.txtAlpha.Size = new System.Drawing.Size(30, 22);
            this.txtAlpha.TabIndex = 19;
            this.txtAlpha.TabStop = false;
            this.txtAlpha.Text = "255";
            this.txtAlpha.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtSaturation
            // 
            this.txtSaturation.Location = new System.Drawing.Point(198, 264);
            this.txtSaturation.Name = "txtSaturation";
            this.txtSaturation.ReadOnly = true;
            this.txtSaturation.Size = new System.Drawing.Size(30, 22);
            this.txtSaturation.TabIndex = 20;
            this.txtSaturation.TabStop = false;
            this.txtSaturation.Text = "255";
            this.txtSaturation.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // picSample
            // 
            this.picSample.Location = new System.Drawing.Point(300, 25);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(300, 200);
            this.picSample.TabIndex = 23;
            this.picSample.TabStop = false;
            this.picSample.Paint += new System.Windows.Forms.PaintEventHandler(this.picSample_Paint);
            this.picSample.Resize += new System.EventHandler(this.picSample_Resize);
            // 
            // btnColor2
            // 
            this.btnColor2.ForeColor = System.Drawing.Color.Black;
            this.btnColor2.Location = new System.Drawing.Point(466, 245);
            this.btnColor2.Name = "btnColor2";
            this.btnColor2.Size = new System.Drawing.Size(91, 34);
            this.btnColor2.TabIndex = 22;
            this.btnColor2.Text = "Select Color 2";
            this.btnColor2.UseVisualStyleBackColor = true;
            this.btnColor2.Click += new System.EventHandler(this.btnColor2_Click);
            // 
            // btnColor1
            // 
            this.btnColor1.ForeColor = System.Drawing.Color.Black;
            this.btnColor1.Location = new System.Drawing.Point(336, 245);
            this.btnColor1.Name = "btnColor1";
            this.btnColor1.Size = new System.Drawing.Size(91, 34);
            this.btnColor1.TabIndex = 21;
            this.btnColor1.Text = "Select Color 1";
            this.btnColor1.UseVisualStyleBackColor = true;
            this.btnColor1.Click += new System.EventHandler(this.btnColor1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(632, 308);
            this.Controls.Add(this.picSample);
            this.Controls.Add(this.btnColor2);
            this.Controls.Add(this.btnColor1);
            this.Controls.Add(this.txtSaturation);
            this.Controls.Add(this.txtAlpha);
            this.Controls.Add(this.picWheel);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.hscrSaturation);
            this.Controls.Add(this.hscrAlpha);
            this.Name = "Form1";
            this.Text = "vcs_ColorWheel";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picWheel)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picWheel;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.HScrollBar hscrSaturation;
        private System.Windows.Forms.HScrollBar hscrAlpha;
        private System.Windows.Forms.TextBox txtAlpha;
        private System.Windows.Forms.TextBox txtSaturation;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.Button btnColor2;
        private System.Windows.Forms.Button btnColor1;
    }
}

