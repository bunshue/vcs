namespace howto_stego_images_tiled
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
            this.btnGo = new System.Windows.Forms.Button();
            this.nudHiddenBits = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.picMainOriginal = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.picHiddenRecovered1 = new System.Windows.Forms.PictureBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.picHiddenOriginal1 = new System.Windows.Forms.PictureBox();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.picHiddenRecovered2 = new System.Windows.Forms.PictureBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.picHiddenOriginal2 = new System.Windows.Forms.PictureBox();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.picHiddenRecovered3 = new System.Windows.Forms.PictureBox();
            this.label9 = new System.Windows.Forms.Label();
            this.picHiddenOriginal3 = new System.Windows.Forms.PictureBox();
            this.label10 = new System.Windows.Forms.Label();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.picHiddenRecovered4 = new System.Windows.Forms.PictureBox();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.picHiddenOriginal4 = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.picCombined = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.nudHiddenBits)).BeginInit();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picMainOriginal)).BeginInit();
            this.tabPage2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal1)).BeginInit();
            this.tabPage3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal2)).BeginInit();
            this.tabPage4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal3)).BeginInit();
            this.tabPage5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picCombined)).BeginInit();
            this.SuspendLayout();
            // 
            // btnGo
            // 
            this.btnGo.Location = new System.Drawing.Point(180, 11);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(75, 23);
            this.btnGo.TabIndex = 17;
            this.btnGo.Text = "Go";
            this.btnGo.UseVisualStyleBackColor = true;
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // nudHiddenBits
            // 
            this.nudHiddenBits.Location = new System.Drawing.Point(114, 11);
            this.nudHiddenBits.Maximum = new decimal(new int[] {
            8,
            0,
            0,
            0});
            this.nudHiddenBits.Name = "nudHiddenBits";
            this.nudHiddenBits.Size = new System.Drawing.Size(48, 20);
            this.nudHiddenBits.TabIndex = 16;
            this.nudHiddenBits.Value = new decimal(new int[] {
            2,
            0,
            0,
            0});
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(96, 13);
            this.label1.TabIndex = 15;
            this.label1.Text = "Hidden Image Bits:";
            // 
            // tabControl1
            // 
            this.tabControl1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Location = new System.Drawing.Point(381, 40);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(387, 320);
            this.tabControl1.TabIndex = 18;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.picMainOriginal);
            this.tabPage1.Controls.Add(this.label3);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(379, 294);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "Main";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // picMainOriginal
            // 
            this.picMainOriginal.Image = global::howto_stego_images_tiled.Properties.Resources.usmapsmall;
            this.picMainOriginal.Location = new System.Drawing.Point(6, 19);
            this.picMainOriginal.Name = "picMainOriginal";
            this.picMainOriginal.Size = new System.Drawing.Size(363, 233);
            this.picMainOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picMainOriginal.TabIndex = 3;
            this.picMainOriginal.TabStop = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 3);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(42, 13);
            this.label3.TabIndex = 2;
            this.label3.Text = "Original";
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.picHiddenRecovered1);
            this.tabPage2.Controls.Add(this.label5);
            this.tabPage2.Controls.Add(this.label6);
            this.tabPage2.Controls.Add(this.picHiddenOriginal1);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(379, 385);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "Hidden 1";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // picHiddenRecovered1
            // 
            this.picHiddenRecovered1.Location = new System.Drawing.Point(6, 159);
            this.picHiddenRecovered1.Name = "picHiddenRecovered1";
            this.picHiddenRecovered1.Size = new System.Drawing.Size(181, 116);
            this.picHiddenRecovered1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenRecovered1.TabIndex = 9;
            this.picHiddenRecovered1.TabStop = false;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(9, 143);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(60, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Recovered";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(9, 3);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(42, 13);
            this.label6.TabIndex = 6;
            this.label6.Text = "Original";
            // 
            // picHiddenOriginal1
            // 
            this.picHiddenOriginal1.Image = ((System.Drawing.Image)(resources.GetObject("picHiddenOriginal1.Image")));
            this.picHiddenOriginal1.Location = new System.Drawing.Point(6, 19);
            this.picHiddenOriginal1.Name = "picHiddenOriginal1";
            this.picHiddenOriginal1.Size = new System.Drawing.Size(181, 116);
            this.picHiddenOriginal1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenOriginal1.TabIndex = 7;
            this.picHiddenOriginal1.TabStop = false;
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.picHiddenRecovered2);
            this.tabPage3.Controls.Add(this.label7);
            this.tabPage3.Controls.Add(this.label8);
            this.tabPage3.Controls.Add(this.picHiddenOriginal2);
            this.tabPage3.Location = new System.Drawing.Point(4, 22);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Size = new System.Drawing.Size(379, 294);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "Hidden 2";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // picHiddenRecovered2
            // 
            this.picHiddenRecovered2.Location = new System.Drawing.Point(6, 159);
            this.picHiddenRecovered2.Name = "picHiddenRecovered2";
            this.picHiddenRecovered2.Size = new System.Drawing.Size(181, 116);
            this.picHiddenRecovered2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenRecovered2.TabIndex = 9;
            this.picHiddenRecovered2.TabStop = false;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(9, 143);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(60, 13);
            this.label7.TabIndex = 8;
            this.label7.Text = "Recovered";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(9, 3);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(42, 13);
            this.label8.TabIndex = 6;
            this.label8.Text = "Original";
            // 
            // picHiddenOriginal2
            // 
            this.picHiddenOriginal2.Image = ((System.Drawing.Image)(resources.GetObject("picHiddenOriginal2.Image")));
            this.picHiddenOriginal2.Location = new System.Drawing.Point(6, 19);
            this.picHiddenOriginal2.Name = "picHiddenOriginal2";
            this.picHiddenOriginal2.Size = new System.Drawing.Size(181, 116);
            this.picHiddenOriginal2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenOriginal2.TabIndex = 7;
            this.picHiddenOriginal2.TabStop = false;
            // 
            // tabPage4
            // 
            this.tabPage4.Controls.Add(this.picHiddenRecovered3);
            this.tabPage4.Controls.Add(this.label9);
            this.tabPage4.Controls.Add(this.picHiddenOriginal3);
            this.tabPage4.Controls.Add(this.label10);
            this.tabPage4.Location = new System.Drawing.Point(4, 22);
            this.tabPage4.Name = "tabPage4";
            this.tabPage4.Size = new System.Drawing.Size(379, 294);
            this.tabPage4.TabIndex = 3;
            this.tabPage4.Text = "Hidden 3";
            this.tabPage4.UseVisualStyleBackColor = true;
            // 
            // picHiddenRecovered3
            // 
            this.picHiddenRecovered3.Location = new System.Drawing.Point(6, 159);
            this.picHiddenRecovered3.Name = "picHiddenRecovered3";
            this.picHiddenRecovered3.Size = new System.Drawing.Size(181, 116);
            this.picHiddenRecovered3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenRecovered3.TabIndex = 9;
            this.picHiddenRecovered3.TabStop = false;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(9, 143);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(60, 13);
            this.label9.TabIndex = 8;
            this.label9.Text = "Recovered";
            // 
            // picHiddenOriginal3
            // 
            this.picHiddenOriginal3.Image = ((System.Drawing.Image)(resources.GetObject("picHiddenOriginal3.Image")));
            this.picHiddenOriginal3.Location = new System.Drawing.Point(6, 19);
            this.picHiddenOriginal3.Name = "picHiddenOriginal3";
            this.picHiddenOriginal3.Size = new System.Drawing.Size(181, 116);
            this.picHiddenOriginal3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenOriginal3.TabIndex = 7;
            this.picHiddenOriginal3.TabStop = false;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(9, 3);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(42, 13);
            this.label10.TabIndex = 6;
            this.label10.Text = "Original";
            // 
            // tabPage5
            // 
            this.tabPage5.Controls.Add(this.picHiddenRecovered4);
            this.tabPage5.Controls.Add(this.label11);
            this.tabPage5.Controls.Add(this.label12);
            this.tabPage5.Controls.Add(this.picHiddenOriginal4);
            this.tabPage5.Location = new System.Drawing.Point(4, 22);
            this.tabPage5.Name = "tabPage5";
            this.tabPage5.Size = new System.Drawing.Size(379, 294);
            this.tabPage5.TabIndex = 4;
            this.tabPage5.Text = "Hidden 4";
            this.tabPage5.UseVisualStyleBackColor = true;
            // 
            // picHiddenRecovered4
            // 
            this.picHiddenRecovered4.Location = new System.Drawing.Point(6, 159);
            this.picHiddenRecovered4.Name = "picHiddenRecovered4";
            this.picHiddenRecovered4.Size = new System.Drawing.Size(181, 116);
            this.picHiddenRecovered4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenRecovered4.TabIndex = 9;
            this.picHiddenRecovered4.TabStop = false;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(9, 143);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(60, 13);
            this.label11.TabIndex = 8;
            this.label11.Text = "Recovered";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(9, 3);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(42, 13);
            this.label12.TabIndex = 6;
            this.label12.Text = "Original";
            // 
            // picHiddenOriginal4
            // 
            this.picHiddenOriginal4.Image = ((System.Drawing.Image)(resources.GetObject("picHiddenOriginal4.Image")));
            this.picHiddenOriginal4.Location = new System.Drawing.Point(6, 19);
            this.picHiddenOriginal4.Name = "picHiddenOriginal4";
            this.picHiddenOriginal4.Size = new System.Drawing.Size(181, 116);
            this.picHiddenOriginal4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHiddenOriginal4.TabIndex = 7;
            this.picHiddenOriginal4.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(15, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(54, 13);
            this.label2.TabIndex = 0;
            this.label2.Text = "Combined";
            // 
            // picCombined
            // 
            this.picCombined.Location = new System.Drawing.Point(12, 81);
            this.picCombined.Name = "picCombined";
            this.picCombined.Size = new System.Drawing.Size(363, 233);
            this.picCombined.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picCombined.TabIndex = 1;
            this.picCombined.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(780, 372);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.picCombined);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.nudHiddenBits);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_stego_images_tiled";
            ((System.ComponentModel.ISupportInitialize)(this.nudHiddenBits)).EndInit();
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picMainOriginal)).EndInit();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal1)).EndInit();
            this.tabPage3.ResumeLayout(false);
            this.tabPage3.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal2)).EndInit();
            this.tabPage4.ResumeLayout(false);
            this.tabPage4.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal3)).EndInit();
            this.tabPage5.ResumeLayout(false);
            this.tabPage5.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenRecovered4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHiddenOriginal4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picCombined)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnGo;
        private System.Windows.Forms.NumericUpDown nudHiddenBits;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.PictureBox picMainOriginal;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox picCombined;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TabPage tabPage4;
        private System.Windows.Forms.TabPage tabPage5;
        private System.Windows.Forms.PictureBox picHiddenRecovered1;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.PictureBox picHiddenOriginal1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.PictureBox picHiddenRecovered2;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.PictureBox picHiddenOriginal2;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.PictureBox picHiddenRecovered3;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.PictureBox picHiddenOriginal3;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.PictureBox picHiddenRecovered4;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.PictureBox picHiddenOriginal4;
        private System.Windows.Forms.Label label12;
    }
}

