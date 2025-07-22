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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.btnReset = new System.Windows.Forms.Button();
            this.lb_elapsed = new System.Windows.Forms.Label();
            this.btnEmboss1 = new System.Windows.Forms.Button();
            this.btnBlur1 = new System.Windows.Forms.Button();
            this.btnBlur2 = new System.Windows.Forms.Button();
            this.btnHighPass1 = new System.Windows.Forms.Button();
            this.btnHighPass2 = new System.Windows.Forms.Button();
            this.btnEdge1 = new System.Windows.Forms.Button();
            this.btnEdge2 = new System.Windows.Forms.Button();
            this.btnEmboss2 = new System.Windows.Forms.Button();
            this.btnEdge3 = new System.Windows.Forms.Button();
            this.btnAverage = new System.Windows.Forms.Button();
            this.btnGrayscale = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.btnGreen = new System.Windows.Forms.Button();
            this.btnRed = new System.Windows.Forms.Button();
            this.btnBlue = new System.Windows.Forms.Button();
            this.btnInvert = new System.Windows.Forms.Button();
            this.btnMaximum = new System.Windows.Forms.Button();
            this.btnMinimum = new System.Windows.Forms.Button();
            this.btnPixellate = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txtRank = new System.Windows.Forms.TextBox();
            this.ofdImage = new System.Windows.Forms.OpenFileDialog();
            this.btnPointellate = new System.Windows.Forms.Button();
            this.btnEmboss3 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_open = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(12, 25);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(100, 40);
            this.btnReset.TabIndex = 0;
            this.btnReset.Text = "Reset";
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // lb_elapsed
            // 
            this.lb_elapsed.AutoSize = true;
            this.lb_elapsed.Location = new System.Drawing.Point(12, 574);
            this.lb_elapsed.Name = "lb_elapsed";
            this.lb_elapsed.Size = new System.Drawing.Size(53, 12);
            this.lb_elapsed.TabIndex = 7;
            this.lb_elapsed.Text = "處理時間";
            // 
            // btnEmboss1
            // 
            this.btnEmboss1.Location = new System.Drawing.Point(12, 74);
            this.btnEmboss1.Name = "btnEmboss1";
            this.btnEmboss1.Size = new System.Drawing.Size(100, 40);
            this.btnEmboss1.TabIndex = 1;
            this.btnEmboss1.Text = "Emboss 1";
            this.btnEmboss1.Click += new System.EventHandler(this.btnEmboss1_Click);
            // 
            // btnBlur1
            // 
            this.btnBlur1.Location = new System.Drawing.Point(12, 205);
            this.btnBlur1.Name = "btnBlur1";
            this.btnBlur1.Size = new System.Drawing.Size(100, 40);
            this.btnBlur1.TabIndex = 4;
            this.btnBlur1.Text = "Blur 1";
            this.btnBlur1.Click += new System.EventHandler(this.btnBlur1_Click);
            // 
            // btnBlur2
            // 
            this.btnBlur2.Location = new System.Drawing.Point(12, 249);
            this.btnBlur2.Name = "btnBlur2";
            this.btnBlur2.Size = new System.Drawing.Size(100, 40);
            this.btnBlur2.TabIndex = 5;
            this.btnBlur2.Text = "Blur 2";
            this.btnBlur2.Click += new System.EventHandler(this.btnBlur2_Click);
            // 
            // btnHighPass1
            // 
            this.btnHighPass1.Location = new System.Drawing.Point(12, 295);
            this.btnHighPass1.Name = "btnHighPass1";
            this.btnHighPass1.Size = new System.Drawing.Size(100, 40);
            this.btnHighPass1.TabIndex = 6;
            this.btnHighPass1.Text = "High Pass 1";
            this.btnHighPass1.Click += new System.EventHandler(this.btnHighPass1_Click);
            // 
            // btnHighPass2
            // 
            this.btnHighPass2.Location = new System.Drawing.Point(12, 345);
            this.btnHighPass2.Name = "btnHighPass2";
            this.btnHighPass2.Size = new System.Drawing.Size(100, 40);
            this.btnHighPass2.TabIndex = 7;
            this.btnHighPass2.Text = "High Pass 2";
            this.btnHighPass2.Click += new System.EventHandler(this.btnHighPass2_Click);
            // 
            // btnEdge1
            // 
            this.btnEdge1.Location = new System.Drawing.Point(12, 390);
            this.btnEdge1.Name = "btnEdge1";
            this.btnEdge1.Size = new System.Drawing.Size(100, 40);
            this.btnEdge1.TabIndex = 8;
            this.btnEdge1.Text = "Edge 1";
            this.btnEdge1.Click += new System.EventHandler(this.btnEdge1_Click);
            // 
            // btnEdge2
            // 
            this.btnEdge2.Location = new System.Drawing.Point(12, 434);
            this.btnEdge2.Name = "btnEdge2";
            this.btnEdge2.Size = new System.Drawing.Size(100, 40);
            this.btnEdge2.TabIndex = 9;
            this.btnEdge2.Text = "Edge 2";
            this.btnEdge2.Click += new System.EventHandler(this.btnEdge2_Click);
            // 
            // btnEmboss2
            // 
            this.btnEmboss2.Location = new System.Drawing.Point(12, 116);
            this.btnEmboss2.Name = "btnEmboss2";
            this.btnEmboss2.Size = new System.Drawing.Size(100, 40);
            this.btnEmboss2.TabIndex = 2;
            this.btnEmboss2.Text = "Emboss 2";
            this.btnEmboss2.Click += new System.EventHandler(this.btnEmboss2_Click);
            // 
            // btnEdge3
            // 
            this.btnEdge3.Location = new System.Drawing.Point(12, 481);
            this.btnEdge3.Name = "btnEdge3";
            this.btnEdge3.Size = new System.Drawing.Size(100, 40);
            this.btnEdge3.TabIndex = 10;
            this.btnEdge3.Text = "Edge 3";
            this.btnEdge3.Click += new System.EventHandler(this.btnEdge3_Click);
            // 
            // btnAverage
            // 
            this.btnAverage.Location = new System.Drawing.Point(123, 25);
            this.btnAverage.Name = "btnAverage";
            this.btnAverage.Size = new System.Drawing.Size(100, 40);
            this.btnAverage.TabIndex = 16;
            this.btnAverage.Text = "Average";
            this.btnAverage.Click += new System.EventHandler(this.btnAverage_Click);
            // 
            // btnGrayscale
            // 
            this.btnGrayscale.Location = new System.Drawing.Point(123, 74);
            this.btnGrayscale.Name = "btnGrayscale";
            this.btnGrayscale.Size = new System.Drawing.Size(100, 40);
            this.btnGrayscale.TabIndex = 17;
            this.btnGrayscale.Text = "Grayscale";
            this.btnGrayscale.Click += new System.EventHandler(this.btnGrayscale_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(373, 61);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(305, 400);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Visible = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(304, 25);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(300, 400);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 6;
            this.pictureBox2.TabStop = false;
            // 
            // btnGreen
            // 
            this.btnGreen.Location = new System.Drawing.Point(123, 160);
            this.btnGreen.Name = "btnGreen";
            this.btnGreen.Size = new System.Drawing.Size(100, 40);
            this.btnGreen.TabIndex = 19;
            this.btnGreen.Text = "Green";
            this.btnGreen.Click += new System.EventHandler(this.btnGreen_Click);
            // 
            // btnRed
            // 
            this.btnRed.Location = new System.Drawing.Point(123, 116);
            this.btnRed.Name = "btnRed";
            this.btnRed.Size = new System.Drawing.Size(100, 40);
            this.btnRed.TabIndex = 18;
            this.btnRed.Text = "Red";
            this.btnRed.Click += new System.EventHandler(this.btnRed_Click);
            // 
            // btnBlue
            // 
            this.btnBlue.Location = new System.Drawing.Point(123, 205);
            this.btnBlue.Name = "btnBlue";
            this.btnBlue.Size = new System.Drawing.Size(100, 40);
            this.btnBlue.TabIndex = 20;
            this.btnBlue.Text = "Blue";
            this.btnBlue.Click += new System.EventHandler(this.btnBlue_Click);
            // 
            // btnInvert
            // 
            this.btnInvert.Location = new System.Drawing.Point(123, 249);
            this.btnInvert.Name = "btnInvert";
            this.btnInvert.Size = new System.Drawing.Size(100, 40);
            this.btnInvert.TabIndex = 21;
            this.btnInvert.Text = "Invert";
            this.btnInvert.Click += new System.EventHandler(this.btnInvert_Click);
            // 
            // btnMaximum
            // 
            this.btnMaximum.Location = new System.Drawing.Point(141, 348);
            this.btnMaximum.Name = "btnMaximum";
            this.btnMaximum.Size = new System.Drawing.Size(100, 40);
            this.btnMaximum.TabIndex = 12;
            this.btnMaximum.Text = "Maximum";
            this.btnMaximum.Click += new System.EventHandler(this.btnMaximum_Click);
            // 
            // btnMinimum
            // 
            this.btnMinimum.Location = new System.Drawing.Point(141, 392);
            this.btnMinimum.Name = "btnMinimum";
            this.btnMinimum.Size = new System.Drawing.Size(100, 40);
            this.btnMinimum.TabIndex = 13;
            this.btnMinimum.Text = "Minimum";
            this.btnMinimum.Click += new System.EventHandler(this.btnMinimum_Click);
            // 
            // btnPixellate
            // 
            this.btnPixellate.Location = new System.Drawing.Point(141, 432);
            this.btnPixellate.Name = "btnPixellate";
            this.btnPixellate.Size = new System.Drawing.Size(100, 40);
            this.btnPixellate.TabIndex = 14;
            this.btnPixellate.Text = "Pixellate";
            this.btnPixellate.Click += new System.EventHandler(this.btnPixellate_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(138, 320);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 19;
            this.label1.Text = "Rank:";
            // 
            // txtRank
            // 
            this.txtRank.Location = new System.Drawing.Point(180, 317);
            this.txtRank.Name = "txtRank";
            this.txtRank.Size = new System.Drawing.Size(38, 22);
            this.txtRank.TabIndex = 11;
            this.txtRank.Text = "9";
            this.txtRank.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // ofdImage
            // 
            this.ofdImage.FileName = "openFileDialog1";
            this.ofdImage.Filter = "Image Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // btnPointellate
            // 
            this.btnPointellate.Location = new System.Drawing.Point(141, 478);
            this.btnPointellate.Name = "btnPointellate";
            this.btnPointellate.Size = new System.Drawing.Size(100, 40);
            this.btnPointellate.TabIndex = 15;
            this.btnPointellate.Text = "Pointellate";
            this.btnPointellate.Click += new System.EventHandler(this.btnPointellate_Click);
            // 
            // btnEmboss3
            // 
            this.btnEmboss3.Location = new System.Drawing.Point(12, 160);
            this.btnEmboss3.Name = "btnEmboss3";
            this.btnEmboss3.Size = new System.Drawing.Size(100, 40);
            this.btnEmboss3.TabIndex = 3;
            this.btnEmboss3.Text = "Emboss 3";
            this.btnEmboss3.Click += new System.EventHandler(this.btnEmboss3_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(726, 27);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(319, 550);
            this.richTextBox1.TabIndex = 22;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(985, 547);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 30);
            this.bt_clear.TabIndex = 23;
            this.bt_clear.Text = "Clear";
            // 
            // bt_open
            // 
            this.bt_open.Location = new System.Drawing.Point(229, 25);
            this.bt_open.Name = "bt_open";
            this.bt_open.Size = new System.Drawing.Size(100, 40);
            this.bt_open.TabIndex = 24;
            this.bt_open.Text = "Open";
            this.bt_open.Click += new System.EventHandler(this.bt_open_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1057, 655);
            this.Controls.Add(this.bt_open);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnEmboss3);
            this.Controls.Add(this.btnPointellate);
            this.Controls.Add(this.txtRank);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnPixellate);
            this.Controls.Add(this.btnMinimum);
            this.Controls.Add(this.btnMaximum);
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
            this.Controls.Add(this.lb_elapsed);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.pictureBox2);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing5";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.PictureBox pictureBox1;
        internal System.Windows.Forms.Button btnReset;
        internal System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Label lb_elapsed;
        internal System.Windows.Forms.Button btnEmboss1;
        internal System.Windows.Forms.Button btnBlur1;
        internal System.Windows.Forms.Button btnBlur2;
        internal System.Windows.Forms.Button btnHighPass1;
        internal System.Windows.Forms.Button btnHighPass2;
        internal System.Windows.Forms.Button btnEdge1;
        internal System.Windows.Forms.Button btnEdge2;
        internal System.Windows.Forms.Button btnEmboss2;
        internal System.Windows.Forms.Button btnEdge3;
        internal System.Windows.Forms.Button btnAverage;
        internal System.Windows.Forms.Button btnGrayscale;
        internal System.Windows.Forms.Button btnGreen;
        internal System.Windows.Forms.Button btnRed;
        internal System.Windows.Forms.Button btnBlue;
        internal System.Windows.Forms.Button btnInvert;
        internal System.Windows.Forms.Button btnMaximum;
        internal System.Windows.Forms.Button btnMinimum;
        internal System.Windows.Forms.Button btnPixellate;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtRank;
        private System.Windows.Forms.OpenFileDialog ofdImage;
        internal System.Windows.Forms.Button btnPointellate;
        internal System.Windows.Forms.Button btnEmboss3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        internal System.Windows.Forms.Button bt_clear;
        internal System.Windows.Forms.Button bt_open;
    }
}

