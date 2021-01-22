namespace vcs_ImageProcessing5
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
            this.btnDoubleWave = new System.Windows.Forms.Button();
            this.btnWiggles = new System.Windows.Forms.Button();
            this.btnSmallTop = new System.Windows.Forms.Button();
            this.btnWave = new System.Windows.Forms.Button();
            this.btnTwist = new System.Windows.Forms.Button();
            this.btnFishEye = new System.Windows.Forms.Button();
            this.btnInvert = new System.Windows.Forms.Button();
            this.btnBlue = new System.Windows.Forms.Button();
            this.btnGreen = new System.Windows.Forms.Button();
            this.btnRed = new System.Windows.Forms.Button();
            this.btnGrayscale = new System.Windows.Forms.Button();
            this.btnAverage = new System.Windows.Forms.Button();
            this.btnEdge3 = new System.Windows.Forms.Button();
            this.btnEmboss2 = new System.Windows.Forms.Button();
            this.btnEdge2 = new System.Windows.Forms.Button();
            this.btnEdge1 = new System.Windows.Forms.Button();
            this.btnHighPass2 = new System.Windows.Forms.Button();
            this.btnHighPass1 = new System.Windows.Forms.Button();
            this.btnBlur2 = new System.Windows.Forms.Button();
            this.btnBlur1 = new System.Windows.Forms.Button();
            this.btnEmboss1 = new System.Windows.Forms.Button();
            this.lblElapsed = new System.Windows.Forms.Label();
            this.btnReset = new System.Windows.Forms.Button();
            this.picHidden = new System.Windows.Forms.PictureBox();
            this.picVisible = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).BeginInit();
            this.SuspendLayout();
            // 
            // btnDoubleWave
            // 
            this.btnDoubleWave.Location = new System.Drawing.Point(184, 150);
            this.btnDoubleWave.Name = "btnDoubleWave";
            this.btnDoubleWave.Size = new System.Drawing.Size(90, 22);
            this.btnDoubleWave.TabIndex = 46;
            this.btnDoubleWave.Text = "Double Wave";
            this.btnDoubleWave.Click += new System.EventHandler(this.btnDoubleWave_Click);
            // 
            // btnWiggles
            // 
            this.btnWiggles.Location = new System.Drawing.Point(184, 122);
            this.btnWiggles.Name = "btnWiggles";
            this.btnWiggles.Size = new System.Drawing.Size(90, 22);
            this.btnWiggles.TabIndex = 45;
            this.btnWiggles.Text = "Wiggles";
            this.btnWiggles.Click += new System.EventHandler(this.btnWiggles_Click);
            // 
            // btnSmallTop
            // 
            this.btnSmallTop.Location = new System.Drawing.Point(184, 94);
            this.btnSmallTop.Name = "btnSmallTop";
            this.btnSmallTop.Size = new System.Drawing.Size(90, 22);
            this.btnSmallTop.TabIndex = 44;
            this.btnSmallTop.Text = "Small Top";
            this.btnSmallTop.Click += new System.EventHandler(this.btnSmallTop_Click);
            // 
            // btnWave
            // 
            this.btnWave.Location = new System.Drawing.Point(184, 66);
            this.btnWave.Name = "btnWave";
            this.btnWave.Size = new System.Drawing.Size(90, 22);
            this.btnWave.TabIndex = 43;
            this.btnWave.Text = "Wave";
            this.btnWave.Click += new System.EventHandler(this.btnWave_Click);
            // 
            // btnTwist
            // 
            this.btnTwist.Location = new System.Drawing.Point(184, 39);
            this.btnTwist.Name = "btnTwist";
            this.btnTwist.Size = new System.Drawing.Size(90, 22);
            this.btnTwist.TabIndex = 42;
            this.btnTwist.Text = "Twist";
            this.btnTwist.Click += new System.EventHandler(this.btnTwist_Click);
            // 
            // btnFishEye
            // 
            this.btnFishEye.Location = new System.Drawing.Point(184, 11);
            this.btnFishEye.Name = "btnFishEye";
            this.btnFishEye.Size = new System.Drawing.Size(90, 22);
            this.btnFishEye.TabIndex = 41;
            this.btnFishEye.Text = "Fish Eye";
            this.btnFishEye.Click += new System.EventHandler(this.btnFishEye_Click);
            // 
            // btnInvert
            // 
            this.btnInvert.Location = new System.Drawing.Point(98, 150);
            this.btnInvert.Name = "btnInvert";
            this.btnInvert.Size = new System.Drawing.Size(80, 22);
            this.btnInvert.TabIndex = 40;
            this.btnInvert.Text = "Invert";
            this.btnInvert.Click += new System.EventHandler(this.btnInvert_Click);
            // 
            // btnBlue
            // 
            this.btnBlue.Location = new System.Drawing.Point(98, 122);
            this.btnBlue.Name = "btnBlue";
            this.btnBlue.Size = new System.Drawing.Size(80, 22);
            this.btnBlue.TabIndex = 39;
            this.btnBlue.Text = "Blue";
            this.btnBlue.Click += new System.EventHandler(this.btnBlue_Click);
            // 
            // btnGreen
            // 
            this.btnGreen.Location = new System.Drawing.Point(98, 94);
            this.btnGreen.Name = "btnGreen";
            this.btnGreen.Size = new System.Drawing.Size(80, 22);
            this.btnGreen.TabIndex = 38;
            this.btnGreen.Text = "Green";
            this.btnGreen.Click += new System.EventHandler(this.btnGreen_Click);
            // 
            // btnRed
            // 
            this.btnRed.Location = new System.Drawing.Point(98, 66);
            this.btnRed.Name = "btnRed";
            this.btnRed.Size = new System.Drawing.Size(80, 22);
            this.btnRed.TabIndex = 37;
            this.btnRed.Text = "Red";
            this.btnRed.Click += new System.EventHandler(this.btnRed_Click);
            // 
            // btnGrayscale
            // 
            this.btnGrayscale.Location = new System.Drawing.Point(98, 39);
            this.btnGrayscale.Name = "btnGrayscale";
            this.btnGrayscale.Size = new System.Drawing.Size(80, 22);
            this.btnGrayscale.TabIndex = 36;
            this.btnGrayscale.Text = "Grayscale";
            this.btnGrayscale.Click += new System.EventHandler(this.btnGrayscale_Click);
            // 
            // btnAverage
            // 
            this.btnAverage.Location = new System.Drawing.Point(98, 11);
            this.btnAverage.Name = "btnAverage";
            this.btnAverage.Size = new System.Drawing.Size(80, 22);
            this.btnAverage.TabIndex = 35;
            this.btnAverage.Text = "Average";
            this.btnAverage.Click += new System.EventHandler(this.btnAverage_Click);
            // 
            // btnEdge3
            // 
            this.btnEdge3.Location = new System.Drawing.Point(12, 260);
            this.btnEdge3.Name = "btnEdge3";
            this.btnEdge3.Size = new System.Drawing.Size(80, 22);
            this.btnEdge3.TabIndex = 34;
            this.btnEdge3.Text = "Edge 3";
            this.btnEdge3.Click += new System.EventHandler(this.btnEdge3_Click);
            // 
            // btnEmboss2
            // 
            this.btnEmboss2.Location = new System.Drawing.Point(12, 66);
            this.btnEmboss2.Name = "btnEmboss2";
            this.btnEmboss2.Size = new System.Drawing.Size(80, 22);
            this.btnEmboss2.TabIndex = 25;
            this.btnEmboss2.Text = "Emboss 2";
            this.btnEmboss2.Click += new System.EventHandler(this.btnEmboss2_Click);
            // 
            // btnEdge2
            // 
            this.btnEdge2.Location = new System.Drawing.Point(12, 233);
            this.btnEdge2.Name = "btnEdge2";
            this.btnEdge2.Size = new System.Drawing.Size(80, 22);
            this.btnEdge2.TabIndex = 33;
            this.btnEdge2.Text = "Edge 2";
            this.btnEdge2.Click += new System.EventHandler(this.btnEdge2_Click);
            // 
            // btnEdge1
            // 
            this.btnEdge1.Location = new System.Drawing.Point(12, 205);
            this.btnEdge1.Name = "btnEdge1";
            this.btnEdge1.Size = new System.Drawing.Size(80, 22);
            this.btnEdge1.TabIndex = 32;
            this.btnEdge1.Text = "Edge 1";
            this.btnEdge1.Click += new System.EventHandler(this.btnEdge1_Click);
            // 
            // btnHighPass2
            // 
            this.btnHighPass2.Location = new System.Drawing.Point(12, 177);
            this.btnHighPass2.Name = "btnHighPass2";
            this.btnHighPass2.Size = new System.Drawing.Size(80, 22);
            this.btnHighPass2.TabIndex = 30;
            this.btnHighPass2.Text = "High Pass 2";
            this.btnHighPass2.Click += new System.EventHandler(this.btnHighPass2_Click);
            // 
            // btnHighPass1
            // 
            this.btnHighPass1.Location = new System.Drawing.Point(12, 150);
            this.btnHighPass1.Name = "btnHighPass1";
            this.btnHighPass1.Size = new System.Drawing.Size(80, 22);
            this.btnHighPass1.TabIndex = 28;
            this.btnHighPass1.Text = "High Pass 1";
            this.btnHighPass1.Click += new System.EventHandler(this.btnHighPass1_Click);
            // 
            // btnBlur2
            // 
            this.btnBlur2.Location = new System.Drawing.Point(12, 122);
            this.btnBlur2.Name = "btnBlur2";
            this.btnBlur2.Size = new System.Drawing.Size(80, 22);
            this.btnBlur2.TabIndex = 27;
            this.btnBlur2.Text = "Blur 2";
            this.btnBlur2.Click += new System.EventHandler(this.btnBlur2_Click);
            // 
            // btnBlur1
            // 
            this.btnBlur1.Location = new System.Drawing.Point(12, 94);
            this.btnBlur1.Name = "btnBlur1";
            this.btnBlur1.Size = new System.Drawing.Size(80, 22);
            this.btnBlur1.TabIndex = 26;
            this.btnBlur1.Text = "Blur 1";
            this.btnBlur1.Click += new System.EventHandler(this.btnBlur1_Click);
            // 
            // btnEmboss1
            // 
            this.btnEmboss1.Location = new System.Drawing.Point(12, 39);
            this.btnEmboss1.Name = "btnEmboss1";
            this.btnEmboss1.Size = new System.Drawing.Size(80, 22);
            this.btnEmboss1.TabIndex = 23;
            this.btnEmboss1.Text = "Emboss 1";
            this.btnEmboss1.Click += new System.EventHandler(this.btnEmboss1_Click);
            // 
            // lblElapsed
            // 
            this.lblElapsed.AutoSize = true;
            this.lblElapsed.Location = new System.Drawing.Point(12, 574);
            this.lblElapsed.Name = "lblElapsed";
            this.lblElapsed.Size = new System.Drawing.Size(0, 12);
            this.lblElapsed.TabIndex = 31;
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(12, 11);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(80, 22);
            this.btnReset.TabIndex = 22;
            this.btnReset.Text = "Reset";
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // picHidden
            // 
            this.picHidden.Image = global::vcs_ImageProcessing5.Properties.Resources.JackOLanterns;
            this.picHidden.Location = new System.Drawing.Point(358, 54);
            this.picHidden.Name = "picHidden";
            this.picHidden.Size = new System.Drawing.Size(300, 400);
            this.picHidden.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHidden.TabIndex = 24;
            this.picHidden.TabStop = false;
            this.picHidden.Visible = false;
            // 
            // picVisible
            // 
            this.picVisible.Location = new System.Drawing.Point(280, 11);
            this.picVisible.Name = "picVisible";
            this.picVisible.Size = new System.Drawing.Size(300, 400);
            this.picVisible.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picVisible.TabIndex = 29;
            this.picVisible.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(801, 571);
            this.Controls.Add(this.btnDoubleWave);
            this.Controls.Add(this.btnWiggles);
            this.Controls.Add(this.btnSmallTop);
            this.Controls.Add(this.btnWave);
            this.Controls.Add(this.btnTwist);
            this.Controls.Add(this.btnFishEye);
            this.Controls.Add(this.btnInvert);
            this.Controls.Add(this.btnBlue);
            this.Controls.Add(this.btnGreen);
            this.Controls.Add(this.btnRed);
            this.Controls.Add(this.btnGrayscale);
            this.Controls.Add(this.btnAverage);
            this.Controls.Add(this.btnEdge3);
            this.Controls.Add(this.btnEmboss2);
            this.Controls.Add(this.btnEdge2);
            this.Controls.Add(this.btnEdge1);
            this.Controls.Add(this.btnHighPass2);
            this.Controls.Add(this.btnHighPass1);
            this.Controls.Add(this.btnBlur2);
            this.Controls.Add(this.btnBlur1);
            this.Controls.Add(this.btnEmboss1);
            this.Controls.Add(this.lblElapsed);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.picHidden);
            this.Controls.Add(this.picVisible);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing5";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Button btnDoubleWave;
        internal System.Windows.Forms.Button btnWiggles;
        internal System.Windows.Forms.Button btnSmallTop;
        internal System.Windows.Forms.Button btnWave;
        internal System.Windows.Forms.Button btnTwist;
        internal System.Windows.Forms.Button btnFishEye;
        internal System.Windows.Forms.Button btnInvert;
        internal System.Windows.Forms.Button btnBlue;
        internal System.Windows.Forms.Button btnGreen;
        internal System.Windows.Forms.Button btnRed;
        internal System.Windows.Forms.Button btnGrayscale;
        internal System.Windows.Forms.Button btnAverage;
        internal System.Windows.Forms.Button btnEdge3;
        internal System.Windows.Forms.Button btnEmboss2;
        internal System.Windows.Forms.Button btnEdge2;
        internal System.Windows.Forms.Button btnEdge1;
        internal System.Windows.Forms.Button btnHighPass2;
        internal System.Windows.Forms.Button btnHighPass1;
        internal System.Windows.Forms.Button btnBlur2;
        internal System.Windows.Forms.Button btnBlur1;
        internal System.Windows.Forms.Button btnEmboss1;
        private System.Windows.Forms.Label lblElapsed;
        internal System.Windows.Forms.Button btnReset;
        internal System.Windows.Forms.PictureBox picHidden;
        internal System.Windows.Forms.PictureBox picVisible;
    }
}

