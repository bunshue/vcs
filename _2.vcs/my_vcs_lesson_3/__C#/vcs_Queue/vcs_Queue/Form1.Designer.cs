namespace vcs_Queue
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
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox_show = new System.Windows.Forms.PictureBox();
            this.button4 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.pictureBox_count = new System.Windows.Forms.PictureBox();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_show)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_count)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 65);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(120, 60);
            this.button1.TabIndex = 0;
            this.button1.Text = "+ 1 peony";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 140);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(120, 60);
            this.button2.TabIndex = 1;
            this.button2.Text = "+2 bear";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 221);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(120, 60);
            this.button3.TabIndex = 2;
            this.button3.Text = "+ 3 elephant";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(654, 263);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(295, 330);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // pictureBox_show
            // 
            this.pictureBox_show.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox_show.Location = new System.Drawing.Point(150, 263);
            this.pictureBox_show.Name = "pictureBox_show";
            this.pictureBox_show.Size = new System.Drawing.Size(485, 330);
            this.pictureBox_show.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_show.TabIndex = 4;
            this.pictureBox_show.TabStop = false;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(654, 129);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(120, 60);
            this.button4.TabIndex = 5;
            this.button4.Text = "dequeue";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(188, 42);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 19);
            this.label1.TabIndex = 6;
            this.label1.Text = "label1";
            // 
            // pictureBox_count
            // 
            this.pictureBox_count.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox_count.Location = new System.Drawing.Point(150, 101);
            this.pictureBox_count.Name = "pictureBox_count";
            this.pictureBox_count.Size = new System.Drawing.Size(485, 123);
            this.pictureBox_count.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_count.TabIndex = 7;
            this.pictureBox_count.TabStop = false;
            this.pictureBox_count.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_count_Paint);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(543, 42);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(92, 49);
            this.button5.TabIndex = 8;
            this.button5.Text = "clear";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(829, 31);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(120, 60);
            this.button6.TabIndex = 9;
            this.button6.Text = "字元隊列範例";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(829, 101);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(120, 60);
            this.button7.TabIndex = 10;
            this.button7.Text = "Queue範例";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(829, 167);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(120, 60);
            this.button8.TabIndex = 11;
            this.button8.Text = "Queue範例";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button11);
            this.groupBox1.Controls.Add(this.button10);
            this.groupBox1.Controls.Add(this.button9);
            this.groupBox1.Location = new System.Drawing.Point(12, 319);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(120, 260);
            this.groupBox1.TabIndex = 12;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Queue 測試";
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(14, 30);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(100, 50);
            this.button9.TabIndex = 13;
            this.button9.Text = "Queue訊息";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(14, 95);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(100, 50);
            this.button10.TabIndex = 14;
            this.button10.Text = "Queue加入";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(14, 160);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(100, 50);
            this.button11.TabIndex = 15;
            this.button11.Text = "Queue取出";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(961, 605);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.pictureBox_count);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.pictureBox_show);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_show)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_count)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox_show;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox_count;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button10;
    }
}

