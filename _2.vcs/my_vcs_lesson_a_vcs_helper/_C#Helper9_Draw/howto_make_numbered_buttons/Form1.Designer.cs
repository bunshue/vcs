namespace howto_make_numbered_buttons
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
            this.nudWidth = new System.Windows.Forms.NumericUpDown();
            this.fdFont = new System.Windows.Forms.FontDialog();
            this.label8 = new System.Windows.Forms.Label();
            this.cdColor = new System.Windows.Forms.ColorDialog();
            this.label5 = new System.Windows.Forms.Label();
            this.btnMakeFiles = new System.Windows.Forms.Button();
            this.picBackground = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            this.picForeground = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.lblFontSample = new System.Windows.Forms.Label();
            this.picSample = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.nudBorderThickness = new System.Windows.Forms.NumericUpDown();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.nudWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBackground)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picForeground)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudBorderThickness)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            this.SuspendLayout();
            // 
            // nudWidth
            // 
            this.nudWidth.Location = new System.Drawing.Point(164, 25);
            this.nudWidth.Minimum = new decimal(new int[] {
            5,
            0,
            0,
            0});
            this.nudWidth.Name = "nudWidth";
            this.nudWidth.Size = new System.Drawing.Size(71, 22);
            this.nudWidth.TabIndex = 0;
            this.nudWidth.Value = new decimal(new int[] {
            60,
            0,
            0,
            0});
            this.nudWidth.ValueChanged += new System.EventHandler(this.nud_ValueChanged);
            this.nudWidth.Scroll += new System.Windows.Forms.ScrollEventHandler(this.nud_Scroll);
            this.nudWidth.KeyUp += new System.Windows.Forms.KeyEventHandler(this.nud_KeyUp);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 78);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(90, 12);
            this.label8.TabIndex = 34;
            this.label8.Text = "Border Thickness:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(164, 8);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(68, 12);
            this.label5.TabIndex = 31;
            this.label5.Text = "Width/Height";
            // 
            // btnMakeFiles
            // 
            this.btnMakeFiles.Location = new System.Drawing.Point(310, 87);
            this.btnMakeFiles.Name = "btnMakeFiles";
            this.btnMakeFiles.Size = new System.Drawing.Size(60, 60);
            this.btnMakeFiles.TabIndex = 4;
            this.btnMakeFiles.Text = "建立數字球";
            this.btnMakeFiles.UseVisualStyleBackColor = true;
            this.btnMakeFiles.Click += new System.EventHandler(this.btnMakeFiles_Click);
            // 
            // picBackground
            // 
            this.picBackground.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picBackground.Location = new System.Drawing.Point(12, 25);
            this.picBackground.Name = "picBackground";
            this.picBackground.Size = new System.Drawing.Size(70, 37);
            this.picBackground.TabIndex = 29;
            this.picBackground.TabStop = false;
            this.picBackground.Click += new System.EventHandler(this.picBackground_Click);
            // 
            // label3
            // 
            this.label3.Location = new System.Drawing.Point(12, 8);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(70, 17);
            this.label3.TabIndex = 27;
            this.label3.Text = "Background";
            this.label3.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // picForeground
            // 
            this.picForeground.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picForeground.Location = new System.Drawing.Point(88, 25);
            this.picForeground.Name = "picForeground";
            this.picForeground.Size = new System.Drawing.Size(70, 37);
            this.picForeground.TabIndex = 25;
            this.picForeground.TabStop = false;
            this.picForeground.Click += new System.EventHandler(this.picForeground_Click);
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(88, 8);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(70, 17);
            this.label2.TabIndex = 23;
            this.label2.Text = "Foreground";
            // 
            // lblFontSample
            // 
            this.lblFontSample.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.lblFontSample.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblFontSample.Font = new System.Drawing.Font("Times New Roman", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblFontSample.Location = new System.Drawing.Point(241, 25);
            this.lblFontSample.Name = "lblFontSample";
            this.lblFontSample.Size = new System.Drawing.Size(692, 37);
            this.lblFontSample.TabIndex = 22;
            this.lblFontSample.Text = "Times New Roman, 24pt, style=Bold";
            this.lblFontSample.Click += new System.EventHandler(this.lblFontSample_Click);
            // 
            // picSample
            // 
            this.picSample.Location = new System.Drawing.Point(180, 77);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(100, 100);
            this.picSample.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSample.TabIndex = 21;
            this.picSample.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(241, 8);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(26, 12);
            this.label1.TabIndex = 20;
            this.label1.Text = "Font";
            // 
            // nudBorderThickness
            // 
            this.nudBorderThickness.Location = new System.Drawing.Point(111, 77);
            this.nudBorderThickness.Name = "nudBorderThickness";
            this.nudBorderThickness.Size = new System.Drawing.Size(46, 22);
            this.nudBorderThickness.TabIndex = 1;
            this.nudBorderThickness.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            this.nudBorderThickness.ValueChanged += new System.EventHandler(this.nud_ValueChanged);
            this.nudBorderThickness.Scroll += new System.Windows.Forms.ScrollEventHandler(this.nud_Scroll);
            this.nudBorderThickness.KeyUp += new System.Windows.Forms.KeyEventHandler(this.nud_KeyUp);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 197);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(921, 377);
            this.richTextBox1.TabIndex = 35;
            this.richTextBox1.Text = "";
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown1.Location = new System.Drawing.Point(70, 121);
            this.numericUpDown1.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDown1.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown1.TabIndex = 36;
            this.numericUpDown1.Value = new decimal(new int[] {
            15,
            0,
            0,
            0});
            this.numericUpDown1.ValueChanged += new System.EventHandler(this.numericUpDown1_ValueChanged);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnMakeFiles;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(945, 586);
            this.Controls.Add(this.numericUpDown1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.nudBorderThickness);
            this.Controls.Add(this.nudWidth);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.btnMakeFiles);
            this.Controls.Add(this.picBackground);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.picForeground);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.lblFontSample);
            this.Controls.Add(this.picSample);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "建立數字球";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.nudWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBackground)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picForeground)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudBorderThickness)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown nudWidth;
        private System.Windows.Forms.FontDialog fdFont;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ColorDialog cdColor;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button btnMakeFiles;
        private System.Windows.Forms.PictureBox picBackground;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox picForeground;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label lblFontSample;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown nudBorderThickness;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.NumericUpDown numericUpDown1;
    }
}

