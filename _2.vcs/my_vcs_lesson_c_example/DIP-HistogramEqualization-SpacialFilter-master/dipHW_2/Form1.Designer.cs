namespace dipHW_2
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button6 = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.button5 = new System.Windows.Forms.Button();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.filter1 = new System.Windows.Forms.TextBox();
            this.filter2 = new System.Windows.Forms.TextBox();
            this.filter3 = new System.Windows.Forms.TextBox();
            this.filter6 = new System.Windows.Forms.TextBox();
            this.filter5 = new System.Windows.Forms.TextBox();
            this.filter4 = new System.Windows.Forms.TextBox();
            this.filter9 = new System.Windows.Forms.TextBox();
            this.filter8 = new System.Windows.Forms.TextBox();
            this.filter7 = new System.Windows.Forms.TextBox();
            this.button7 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(560, 350);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(26, 24);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "选择图像";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 376);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "图片信息";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(27, 78);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 3;
            this.button2.Text = "均衡化";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(26, 91);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 4;
            this.button3.Text = "保存图片";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(26, 57);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 5;
            this.button4.Text = "还原图片";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // saveFileDialog1
            // 
            this.saveFileDialog1.Filter = "位图|*.bmp";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.button3);
            this.groupBox1.Controls.Add(this.button4);
            this.groupBox1.Location = new System.Drawing.Point(12, 402);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(132, 130);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "图片读写";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button6);
            this.groupBox2.Controls.Add(this.button2);
            this.groupBox2.Location = new System.Drawing.Point(158, 402);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(133, 130);
            this.groupBox2.TabIndex = 7;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "直方图处理";
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(27, 35);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(75, 23);
            this.button6.TabIndex = 4;
            this.button6.Text = "显示直方图";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.button7);
            this.groupBox3.Controls.Add(this.filter9);
            this.groupBox3.Controls.Add(this.filter8);
            this.groupBox3.Controls.Add(this.filter7);
            this.groupBox3.Controls.Add(this.filter6);
            this.groupBox3.Controls.Add(this.filter5);
            this.groupBox3.Controls.Add(this.filter4);
            this.groupBox3.Controls.Add(this.filter3);
            this.groupBox3.Controls.Add(this.filter2);
            this.groupBox3.Controls.Add(this.filter1);
            this.groupBox3.Controls.Add(this.label2);
            this.groupBox3.Controls.Add(this.button5);
            this.groupBox3.Controls.Add(this.textBox3);
            this.groupBox3.Controls.Add(this.label4);
            this.groupBox3.Location = new System.Drawing.Point(297, 402);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(275, 130);
            this.groupBox3.TabIndex = 8;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "空间滤波";
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(208, 19);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(61, 23);
            this.button5.TabIndex = 2;
            this.button5.Text = "滤波";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(110, 21);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(92, 21);
            this.textBox3.TabIndex = 1;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(19, 24);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(95, 12);
            this.label4.TabIndex = 0;
            this.label4.Text = "平均滤波宽/高：";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(417, 540);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(155, 12);
            this.label5.TabIndex = 9;
            this.label5.Text = "by 14数媒 孙展博 14331242";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(19, 51);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(95, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "3x3自定义滤波：";
            // 
            // filter1
            // 
            this.filter1.Location = new System.Drawing.Point(110, 48);
            this.filter1.Name = "filter1";
            this.filter1.Size = new System.Drawing.Size(26, 21);
            this.filter1.TabIndex = 4;
            // 
            // filter2
            // 
            this.filter2.Location = new System.Drawing.Point(142, 48);
            this.filter2.Name = "filter2";
            this.filter2.Size = new System.Drawing.Size(26, 21);
            this.filter2.TabIndex = 5;
            // 
            // filter3
            // 
            this.filter3.Location = new System.Drawing.Point(174, 48);
            this.filter3.Name = "filter3";
            this.filter3.Size = new System.Drawing.Size(26, 21);
            this.filter3.TabIndex = 6;
            // 
            // filter6
            // 
            this.filter6.Location = new System.Drawing.Point(174, 75);
            this.filter6.Name = "filter6";
            this.filter6.Size = new System.Drawing.Size(26, 21);
            this.filter6.TabIndex = 9;
            // 
            // filter5
            // 
            this.filter5.Location = new System.Drawing.Point(142, 75);
            this.filter5.Name = "filter5";
            this.filter5.Size = new System.Drawing.Size(26, 21);
            this.filter5.TabIndex = 8;
            // 
            // filter4
            // 
            this.filter4.Location = new System.Drawing.Point(110, 75);
            this.filter4.Name = "filter4";
            this.filter4.Size = new System.Drawing.Size(26, 21);
            this.filter4.TabIndex = 7;
            // 
            // filter9
            // 
            this.filter9.Location = new System.Drawing.Point(174, 102);
            this.filter9.Name = "filter9";
            this.filter9.Size = new System.Drawing.Size(26, 21);
            this.filter9.TabIndex = 12;
            // 
            // filter8
            // 
            this.filter8.Location = new System.Drawing.Point(142, 102);
            this.filter8.Name = "filter8";
            this.filter8.Size = new System.Drawing.Size(26, 21);
            this.filter8.TabIndex = 11;
            // 
            // filter7
            // 
            this.filter7.Location = new System.Drawing.Point(110, 102);
            this.filter7.Name = "filter7";
            this.filter7.Size = new System.Drawing.Size(26, 21);
            this.filter7.TabIndex = 10;
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(206, 73);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(61, 23);
            this.button7.TabIndex = 13;
            this.button7.Text = "滤波";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 561);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pictureBox1);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(600, 600);
            this.MinimumSize = new System.Drawing.Size(600, 600);
            this.Name = "Form1";
            this.Text = "DIP HW 2 - 孙展博";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox filter9;
        private System.Windows.Forms.TextBox filter8;
        private System.Windows.Forms.TextBox filter7;
        private System.Windows.Forms.TextBox filter6;
        private System.Windows.Forms.TextBox filter5;
        private System.Windows.Forms.TextBox filter4;
        private System.Windows.Forms.TextBox filter3;
        private System.Windows.Forms.TextBox filter2;
        private System.Windows.Forms.TextBox filter1;
        private System.Windows.Forms.Button button7;
    }
}

