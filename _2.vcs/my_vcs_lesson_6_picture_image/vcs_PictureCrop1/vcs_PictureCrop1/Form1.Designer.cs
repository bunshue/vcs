namespace vcs_PictureCrop1
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
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.button6 = new System.Windows.Forms.Button();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.Color.LightGray;
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(444, 21);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(400, 450);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.pictureBox2.TabIndex = 1;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Cursor = System.Windows.Forms.Cursors.Cross;
            this.pictureBox1.Location = new System.Drawing.Point(22, 21);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(400, 450);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(867, 21);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(310, 450);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(867, 477);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(102, 38);
            this.button1.TabIndex = 3;
            this.button1.Text = "截圖部分存檔";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(1083, 477);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(102, 38);
            this.button2.TabIndex = 4;
            this.button2.Text = "info";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(867, 521);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(102, 38);
            this.button3.TabIndex = 5;
            this.button3.Text = "Cut";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(975, 521);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(102, 38);
            this.button4.TabIndex = 6;
            this.button4.Text = "Copy to Clipboard";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(1083, 521);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(102, 38);
            this.button5.TabIndex = 7;
            this.button5.Text = "Reset";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.nud_h);
            this.groupBox1.Controls.Add(this.button6);
            this.groupBox1.Controls.Add(this.nud_w);
            this.groupBox1.Controls.Add(this.nud_y_st);
            this.groupBox1.Controls.Add(this.nud_x_st);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Location = new System.Drawing.Point(484, 490);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(241, 179);
            this.groupBox1.TabIndex = 8;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "指明部分截取";
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(146, 85);
            this.nud_h.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_h.Name = "nud_h";
            this.nud_h.Size = new System.Drawing.Size(74, 33);
            this.nud_h.TabIndex = 16;
            this.nud_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_h.ValueChanged += new System.EventHandler(this.select_crop_area);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(72, 132);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(81, 33);
            this.button6.TabIndex = 6;
            this.button6.Text = "save";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(43, 85);
            this.nud_w.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_w.Name = "nud_w";
            this.nud_w.Size = new System.Drawing.Size(74, 33);
            this.nud_w.TabIndex = 15;
            this.nud_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_w.ValueChanged += new System.EventHandler(this.select_crop_area);
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(146, 26);
            this.nud_y_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_y_st.Name = "nud_y_st";
            this.nud_y_st.Size = new System.Drawing.Size(74, 33);
            this.nud_y_st.TabIndex = 14;
            this.nud_y_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_y_st.ValueChanged += new System.EventHandler(this.select_crop_area);
            // 
            // nud_x_st
            // 
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(43, 26);
            this.nud_x_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_x_st.Name = "nud_x_st";
            this.nud_x_st.Size = new System.Drawing.Size(74, 33);
            this.nud_x_st.TabIndex = 13;
            this.nud_x_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_x_st.ValueChanged += new System.EventHandler(this.select_crop_area);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(21, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(122, 16);
            this.label1.TabIndex = 11;
            this.label1.Text = "X                       Y";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(20, 93);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(121, 16);
            this.label2.TabIndex = 12;
            this.label2.Text = "W                      H";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(12, 665);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(274, 24);
            this.label3.TabIndex = 9;
            this.label3.Text = "可將選取區域貼在空白處";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1240, 698);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "vcs_PictureCrop1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.Form1_KeyPress);
            this.MouseClick += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseClick);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label label3;
    }
}

