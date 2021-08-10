namespace vcs_AForge_TexturesDemo
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb4 = new System.Windows.Forms.RadioButton();
            this.rb5 = new System.Windows.Forms.RadioButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(708, 651);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb5);
            this.groupBox1.Controls.Add(this.rb4);
            this.groupBox1.Controls.Add(this.rb3);
            this.groupBox1.Controls.Add(this.rb2);
            this.groupBox1.Controls.Add(this.rb1);
            this.groupBox1.Location = new System.Drawing.Point(726, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(183, 236);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Textures";
            // 
            // rb1
            // 
            this.rb1.AutoSize = true;
            this.rb1.Checked = true;
            this.rb1.Location = new System.Drawing.Point(30, 34);
            this.rb1.Name = "rb1";
            this.rb1.Size = new System.Drawing.Size(56, 16);
            this.rb1.TabIndex = 0;
            this.rb1.TabStop = true;
            this.rb1.Text = "Clouds";
            this.rb1.UseVisualStyleBackColor = true;
            this.rb1.CheckedChanged += new System.EventHandler(this.rb_texture_CheckedChanged);
            // 
            // rb2
            // 
            this.rb2.AutoSize = true;
            this.rb2.Location = new System.Drawing.Point(30, 66);
            this.rb2.Name = "rb2";
            this.rb2.Size = new System.Drawing.Size(56, 16);
            this.rb2.TabIndex = 1;
            this.rb2.Text = "Marble";
            this.rb2.UseVisualStyleBackColor = true;
            this.rb2.CheckedChanged += new System.EventHandler(this.rb_texture_CheckedChanged);
            // 
            // rb3
            // 
            this.rb3.AutoSize = true;
            this.rb3.Location = new System.Drawing.Point(30, 100);
            this.rb3.Name = "rb3";
            this.rb3.Size = new System.Drawing.Size(52, 16);
            this.rb3.TabIndex = 2;
            this.rb3.Text = "Wood";
            this.rb3.UseVisualStyleBackColor = true;
            this.rb3.CheckedChanged += new System.EventHandler(this.rb_texture_CheckedChanged);
            // 
            // rb4
            // 
            this.rb4.AutoSize = true;
            this.rb4.Location = new System.Drawing.Point(30, 137);
            this.rb4.Name = "rb4";
            this.rb4.Size = new System.Drawing.Size(69, 16);
            this.rb4.TabIndex = 3;
            this.rb4.Text = "Labyrinth";
            this.rb4.UseVisualStyleBackColor = true;
            this.rb4.CheckedChanged += new System.EventHandler(this.rb_texture_CheckedChanged);
            // 
            // rb5
            // 
            this.rb5.AutoSize = true;
            this.rb5.Location = new System.Drawing.Point(30, 171);
            this.rb5.Name = "rb5";
            this.rb5.Size = new System.Drawing.Size(55, 16);
            this.rb5.TabIndex = 4;
            this.rb5.Text = "Textile";
            this.rb5.UseVisualStyleBackColor = true;
            this.rb5.CheckedChanged += new System.EventHandler(this.rb_texture_CheckedChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(726, 254);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(183, 409);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1500;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(972, 675);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb5;
        private System.Windows.Forms.RadioButton rb4;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer1;
    }
}

