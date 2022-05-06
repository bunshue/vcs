namespace vcs_Draw_LinearGradientBrush
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox_gradient_color_sp = new System.Windows.Forms.PictureBox();
            this.pictureBox_gradient_color_st = new System.Windows.Forms.PictureBox();
            this.pictureBox_gradient_color = new System.Windows.Forms.PictureBox();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.panel1 = new System.Windows.Forms.Panel();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color_sp)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(149, 54);
            this.button1.TabIndex = 0;
            this.button1.Text = "使用 LinearGradientBrush";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(405, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(600, 600);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 90);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(149, 54);
            this.button2.TabIndex = 2;
            this.button2.Text = "使用 LinearGradientBrush";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 165);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(149, 54);
            this.button3.TabIndex = 3;
            this.button3.Text = "漸層色";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 243);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(149, 54);
            this.button4.TabIndex = 4;
            this.button4.Text = "漸層色 3種";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.pictureBox_gradient_color_sp);
            this.groupBox1.Controls.Add(this.pictureBox_gradient_color_st);
            this.groupBox1.Controls.Add(this.pictureBox_gradient_color);
            this.groupBox1.Location = new System.Drawing.Point(12, 303);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(387, 172);
            this.groupBox1.TabIndex = 79;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "漸層色";
            // 
            // pictureBox_gradient_color_sp
            // 
            this.pictureBox_gradient_color_sp.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox_gradient_color_sp.BackColor = System.Drawing.Color.Lime;
            this.pictureBox_gradient_color_sp.Location = new System.Drawing.Point(351, 94);
            this.pictureBox_gradient_color_sp.Name = "pictureBox_gradient_color_sp";
            this.pictureBox_gradient_color_sp.Size = new System.Drawing.Size(30, 67);
            this.pictureBox_gradient_color_sp.TabIndex = 2;
            this.pictureBox_gradient_color_sp.TabStop = false;
            this.pictureBox_gradient_color_sp.Click += new System.EventHandler(this.pictureBox_gradient_color_sp_Click);
            // 
            // pictureBox_gradient_color_st
            // 
            this.pictureBox_gradient_color_st.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox_gradient_color_st.BackColor = System.Drawing.Color.Red;
            this.pictureBox_gradient_color_st.Location = new System.Drawing.Point(6, 94);
            this.pictureBox_gradient_color_st.Name = "pictureBox_gradient_color_st";
            this.pictureBox_gradient_color_st.Size = new System.Drawing.Size(30, 67);
            this.pictureBox_gradient_color_st.TabIndex = 1;
            this.pictureBox_gradient_color_st.TabStop = false;
            this.pictureBox_gradient_color_st.Click += new System.EventHandler(this.pictureBox_gradient_color_st_Click);
            // 
            // pictureBox_gradient_color
            // 
            this.pictureBox_gradient_color.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox_gradient_color.BackColor = System.Drawing.Color.White;
            this.pictureBox_gradient_color.Location = new System.Drawing.Point(6, 21);
            this.pictureBox_gradient_color.Name = "pictureBox_gradient_color";
            this.pictureBox_gradient_color.Size = new System.Drawing.Size(375, 67);
            this.pictureBox_gradient_color.TabIndex = 0;
            this.pictureBox_gradient_color.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(12, 481);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(387, 84);
            this.panel1.TabIndex = 80;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(176, 12);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(149, 54);
            this.button5.TabIndex = 81;
            this.button5.Text = "漸層色1";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(176, 90);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(149, 54);
            this.button6.TabIndex = 82;
            this.button6.Text = "漸層色2";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(176, 165);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(149, 54);
            this.button7.TabIndex = 83;
            this.button7.Text = "使用 LinearGradientBrush";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(176, 243);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(149, 54);
            this.button8.TabIndex = 84;
            this.button8.Text = "使用 LinearGradientBrush";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1019, 626);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color_sp)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gradient_color)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.PictureBox pictureBox_gradient_color_sp;
        private System.Windows.Forms.PictureBox pictureBox_gradient_color_st;
        private System.Windows.Forms.PictureBox pictureBox_gradient_color;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
    }
}

