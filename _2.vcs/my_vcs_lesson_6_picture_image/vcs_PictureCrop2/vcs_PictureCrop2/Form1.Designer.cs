﻿namespace vcs_PictureCrop2
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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.mnuScale = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale100 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale75 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale66 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale50 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale25 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuScale15 = new System.Windows.Forms.ToolStripMenuItem();
            this.sfdImage = new System.Windows.Forms.SaveFileDialog();
            this.ofdImage = new System.Windows.Forms.OpenFileDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.txtWidth = new System.Windows.Forms.TextBox();
            this.txtHeight = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.picImage = new System.Windows.Forms.PictureBox();
            this.txtAspectRatio = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).BeginInit();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuScale});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1309, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // mnuScale
            // 
            this.mnuScale.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuScale100,
            this.mnuScale75,
            this.mnuScale66,
            this.mnuScale50,
            this.mnuScale25,
            this.mnuScale15});
            this.mnuScale.Name = "mnuScale";
            this.mnuScale.Size = new System.Drawing.Size(92, 20);
            this.mnuScale.Text = "&Scale (100%)";
            // 
            // mnuScale100
            // 
            this.mnuScale100.Checked = true;
            this.mnuScale100.CheckState = System.Windows.Forms.CheckState.Checked;
            this.mnuScale100.Name = "mnuScale100";
            this.mnuScale100.Size = new System.Drawing.Size(106, 22);
            this.mnuScale100.Text = "1&00%";
            this.mnuScale100.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale75
            // 
            this.mnuScale75.Name = "mnuScale75";
            this.mnuScale75.Size = new System.Drawing.Size(106, 22);
            this.mnuScale75.Text = "&75%";
            this.mnuScale75.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale66
            // 
            this.mnuScale66.Name = "mnuScale66";
            this.mnuScale66.Size = new System.Drawing.Size(106, 22);
            this.mnuScale66.Text = "&66%";
            this.mnuScale66.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale50
            // 
            this.mnuScale50.Name = "mnuScale50";
            this.mnuScale50.Size = new System.Drawing.Size(106, 22);
            this.mnuScale50.Text = "&50%";
            this.mnuScale50.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale25
            // 
            this.mnuScale25.Name = "mnuScale25";
            this.mnuScale25.Size = new System.Drawing.Size(106, 22);
            this.mnuScale25.Text = "&25%";
            this.mnuScale25.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale15
            // 
            this.mnuScale15.Name = "mnuScale15";
            this.mnuScale15.Size = new System.Drawing.Size(106, 22);
            this.mnuScale15.Text = "&15%";
            this.mnuScale15.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // sfdImage
            // 
            this.sfdImage.DefaultExt = "png";
            this.sfdImage.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // ofdImage
            // 
            this.ofdImage.DefaultExt = "png";
            this.ofdImage.Filter = "Picture Files|*.bmp;*.jpg;*.gif;*.png;*.tif|All Files|*.*";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "Aspect Ratio:";
            // 
            // txtWidth
            // 
            this.txtWidth.Location = new System.Drawing.Point(156, 25);
            this.txtWidth.Name = "txtWidth";
            this.txtWidth.Size = new System.Drawing.Size(46, 22);
            this.txtWidth.TabIndex = 1;
            this.txtWidth.Text = "400";
            this.txtWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtWidth.TextChanged += new System.EventHandler(this.txtWidth_TextChanged);
            // 
            // txtHeight
            // 
            this.txtHeight.Location = new System.Drawing.Point(226, 25);
            this.txtHeight.Name = "txtHeight";
            this.txtHeight.Size = new System.Drawing.Size(46, 22);
            this.txtHeight.TabIndex = 2;
            this.txtHeight.Text = "300";
            this.txtHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtHeight.TextChanged += new System.EventHandler(this.txtHeight_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(208, 28);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(11, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "x";
            // 
            // picImage
            // 
            this.picImage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picImage.Location = new System.Drawing.Point(12, 49);
            this.picImage.Name = "picImage";
            this.picImage.Size = new System.Drawing.Size(260, 196);
            this.picImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picImage.TabIndex = 5;
            this.picImage.TabStop = false;
            this.picImage.Visible = false;
            this.picImage.Paint += new System.Windows.Forms.PaintEventHandler(this.picImage_Paint);
            this.picImage.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseDown);
            this.picImage.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseMove);
            this.picImage.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseUp);
            // 
            // txtAspectRatio
            // 
            this.txtAspectRatio.Location = new System.Drawing.Point(88, 25);
            this.txtAspectRatio.Name = "txtAspectRatio";
            this.txtAspectRatio.Size = new System.Drawing.Size(46, 22);
            this.txtAspectRatio.TabIndex = 0;
            this.txtAspectRatio.Text = "4:3";
            this.txtAspectRatio.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtAspectRatio.TextChanged += new System.EventHandler(this.txtAspectRatio_TextChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(1102, 24);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(207, 671);
            this.richTextBox1.TabIndex = 6;
            this.richTextBox1.Text = "";
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Location = new System.Drawing.Point(866, 28);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(230, 192);
            this.groupBox_selection.TabIndex = 15;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // lb_x_st
            // 
            this.lb_x_st.AutoSize = true;
            this.lb_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_x_st.Location = new System.Drawing.Point(47, 18);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(47, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x_st";
            // 
            // nud_x_st
            // 
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(97, 16);
            this.nud_x_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_x_st.Name = "nud_x_st";
            this.nud_x_st.Size = new System.Drawing.Size(89, 36);
            this.nud_x_st.TabIndex = 5;
            this.nud_x_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(59, 144);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(97, 58);
            this.nud_y_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_y_st.Name = "nud_y_st";
            this.nud_y_st.Size = new System.Drawing.Size(89, 36);
            this.nud_y_st.TabIndex = 7;
            this.nud_y_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(97, 142);
            this.nud_h.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_h.Name = "nud_h";
            this.nud_h.Size = new System.Drawing.Size(89, 36);
            this.nud_h.TabIndex = 11;
            this.nud_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_y_st
            // 
            this.lb_y_st.AutoSize = true;
            this.lb_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y_st.Location = new System.Drawing.Point(47, 60);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(47, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y_st";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(59, 102);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(97, 100);
            this.nud_w.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_w.Name = "nud_w";
            this.nud_w.Size = new System.Drawing.Size(89, 36);
            this.nud_w.TabIndex = 9;
            this.nud_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(866, 252);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(85, 54);
            this.button1.TabIndex = 16;
            this.button1.Text = "開啟檔案";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(866, 323);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(85, 54);
            this.button2.TabIndex = 17;
            this.button2.Text = "選取部分存檔";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(976, 252);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(85, 54);
            this.button3.TabIndex = 18;
            this.button3.Text = "100%";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(976, 323);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(85, 54);
            this.button4.TabIndex = 19;
            this.button4.Text = "75%";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(976, 393);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(85, 54);
            this.button5.TabIndex = 20;
            this.button5.Text = "66%";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(976, 468);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(85, 54);
            this.button6.TabIndex = 21;
            this.button6.Text = "50%";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(976, 528);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(85, 54);
            this.button7.TabIndex = 22;
            this.button7.Text = "25%";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(976, 598);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(85, 54);
            this.button8.TabIndex = 23;
            this.button8.Text = "15%";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1309, 695);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.txtAspectRatio);
            this.Controls.Add(this.picImage);
            this.Controls.Add(this.txtHeight);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtWidth);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "vcs_PictureCrop2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).EndInit();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.SaveFileDialog sfdImage;
        private System.Windows.Forms.OpenFileDialog ofdImage;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtWidth;
        private System.Windows.Forms.TextBox txtHeight;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox picImage;
        private System.Windows.Forms.ToolStripMenuItem mnuScale;
        private System.Windows.Forms.ToolStripMenuItem mnuScale75;
        private System.Windows.Forms.ToolStripMenuItem mnuScale66;
        private System.Windows.Forms.ToolStripMenuItem mnuScale50;
        private System.Windows.Forms.ToolStripMenuItem mnuScale25;
        private System.Windows.Forms.ToolStripMenuItem mnuScale15;
        private System.Windows.Forms.ToolStripMenuItem mnuScale100;
        private System.Windows.Forms.TextBox txtAspectRatio;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
    }
}

