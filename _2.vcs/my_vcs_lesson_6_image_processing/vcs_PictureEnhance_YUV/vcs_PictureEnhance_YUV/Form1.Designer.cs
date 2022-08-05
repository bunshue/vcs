namespace vcs_PictureEnhance_YUV
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
            this.components = new System.ComponentModel.Container();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.pictureBox3a = new System.Windows.Forms.PictureBox();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.button6 = new System.Windows.Forms.Button();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.button7 = new System.Windows.Forms.Button();
            this.pictureBox3b = new System.Windows.Forms.PictureBox();
            this.button8 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.cb_magnify = new System.Windows.Forms.CheckBox();
            this.timer_rgb = new System.Windows.Forms.Timer(this.components);
            this.lb_brightness = new System.Windows.Forms.Label();
            this.button11 = new System.Windows.Forms.Button();
            this.cb_modify = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3a)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3b)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(10, 120);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 7;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(10, 10);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(472, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(200, 200);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(239, 100);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(80, 40);
            this.button1.TabIndex = 8;
            this.button1.Text = "影像加強1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(239, 145);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(80, 40);
            this.button2.TabIndex = 9;
            this.button2.Text = "影像加強2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(240, 191);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(80, 40);
            this.button3.TabIndex = 10;
            this.button3.Text = "影像加強3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(240, 237);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(80, 40);
            this.button4.TabIndex = 11;
            this.button4.Text = "影像加強4";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // pictureBox3a
            // 
            this.pictureBox3a.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3a.Location = new System.Drawing.Point(120, 10);
            this.pictureBox3a.Name = "pictureBox3a";
            this.pictureBox3a.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3a.TabIndex = 12;
            this.pictureBox3a.TabStop = false;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(240, 283);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(80, 40);
            this.button5.TabIndex = 13;
            this.button5.Text = "全圖";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(600, 165);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 14;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox4
            // 
            this.pictureBox4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox4.Location = new System.Drawing.Point(120, 230);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 100);
            this.pictureBox4.TabIndex = 15;
            this.pictureBox4.TabStop = false;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(240, 329);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(80, 40);
            this.button6.TabIndex = 16;
            this.button6.Text = "影像加強 + 亮度分布";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // pictureBox5
            // 
            this.pictureBox5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox5.Location = new System.Drawing.Point(120, 340);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(100, 100);
            this.pictureBox5.TabIndex = 17;
            this.pictureBox5.TabStop = false;
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(240, 375);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(80, 40);
            this.button7.TabIndex = 18;
            this.button7.Text = "影像加強 + 亮度分布";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // pictureBox3b
            // 
            this.pictureBox3b.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3b.Location = new System.Drawing.Point(120, 120);
            this.pictureBox3b.Name = "pictureBox3b";
            this.pictureBox3b.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3b.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox3b.TabIndex = 19;
            this.pictureBox3b.TabStop = false;
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(341, 56);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(80, 40);
            this.button8.TabIndex = 20;
            this.button8.Text = "info";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(240, 56);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(80, 40);
            this.button0.TabIndex = 21;
            this.button0.Text = "Reset";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(341, 100);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(80, 40);
            this.button9.TabIndex = 22;
            this.button9.Text = "2D plot 黑白";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(341, 145);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(80, 40);
            this.button10.TabIndex = 23;
            this.button10.Text = "2D plot 彩色";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // cb_magnify
            // 
            this.cb_magnify.AutoSize = true;
            this.cb_magnify.Location = new System.Drawing.Point(351, 22);
            this.cb_magnify.Name = "cb_magnify";
            this.cb_magnify.Size = new System.Drawing.Size(60, 16);
            this.cb_magnify.TabIndex = 24;
            this.cb_magnify.Text = "放大鏡";
            this.cb_magnify.UseVisualStyleBackColor = true;
            // 
            // timer_rgb
            // 
            this.timer_rgb.Enabled = true;
            this.timer_rgb.Tick += new System.EventHandler(this.timer_rgb_Tick);
            // 
            // lb_brightness
            // 
            this.lb_brightness.AutoSize = true;
            this.lb_brightness.Font = new System.Drawing.Font("Consolas", 27.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_brightness.ForeColor = System.Drawing.Color.Gold;
            this.lb_brightness.Location = new System.Drawing.Point(242, 10);
            this.lb_brightness.Name = "lb_brightness";
            this.lb_brightness.Size = new System.Drawing.Size(39, 43);
            this.lb_brightness.TabIndex = 203;
            this.lb_brightness.Text = "Y";
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(341, 191);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(80, 40);
            this.button11.TabIndex = 204;
            this.button11.Text = "2D plot test";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // cb_modify
            // 
            this.cb_modify.AutoSize = true;
            this.cb_modify.Checked = true;
            this.cb_modify.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_modify.Location = new System.Drawing.Point(351, 37);
            this.cb_modify.Name = "cb_modify";
            this.cb_modify.Size = new System.Drawing.Size(48, 16);
            this.cb_modify.TabIndex = 205;
            this.cb_modify.Text = "調整";
            this.cb_modify.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 461);
            this.Controls.Add(this.cb_modify);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.lb_brightness);
            this.Controls.Add(this.cb_magnify);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.pictureBox3b);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.pictureBox5);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.pictureBox3a);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3a)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3b)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.PictureBox pictureBox3a;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.PictureBox pictureBox5;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.PictureBox pictureBox3b;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.CheckBox cb_magnify;
        private System.Windows.Forms.Timer timer_rgb;
        private System.Windows.Forms.Label lb_brightness;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.CheckBox cb_modify;
    }
}

