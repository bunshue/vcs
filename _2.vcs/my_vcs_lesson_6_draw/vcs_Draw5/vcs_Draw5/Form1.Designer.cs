namespace vcs_Draw5
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button14 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button7);
            this.groupBox1.Controls.Add(this.button8);
            this.groupBox1.Controls.Add(this.button9);
            this.groupBox1.Controls.Add(this.button5);
            this.groupBox1.Location = new System.Drawing.Point(658, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(173, 313);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Draw";
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(7, 251);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(160, 23);
            this.button7.TabIndex = 8;
            this.button7.Text = "Curve";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(7, 222);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(160, 23);
            this.button8.TabIndex = 7;
            this.button8.Text = "Bezier";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(7, 193);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(160, 23);
            this.button9.TabIndex = 6;
            this.button9.Text = "Arc deg(90~270)";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(7, 135);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(160, 23);
            this.button5.TabIndex = 4;
            this.button5.Text = "Path";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button14);
            this.groupBox2.Location = new System.Drawing.Point(837, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(173, 173);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Fill";
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(7, 135);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(160, 23);
            this.button14.TabIndex = 4;
            this.button14.Text = "Path";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button19
            // 
            this.button19.Location = new System.Drawing.Point(957, 469);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(53, 23);
            this.button19.TabIndex = 9;
            this.button19.Text = "clear";
            this.button19.UseVisualStyleBackColor = true;
            this.button19.Click += new System.EventHandler(this.button19_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1022, 502);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Draw";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button19;
    }
}

