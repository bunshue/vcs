namespace vcs_RadioButton
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.rb_color1 = new System.Windows.Forms.RadioButton();
            this.rb_color3 = new System.Windows.Forms.RadioButton();
            this.rb_color2 = new System.Windows.Forms.RadioButton();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.rb_style1 = new System.Windows.Forms.RadioButton();
            this.rb_style2 = new System.Windows.Forms.RadioButton();
            this.rb_style3 = new System.Windows.Forms.RadioButton();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(253, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.rb_color1);
            this.groupBox3.Controls.Add(this.rb_color3);
            this.groupBox3.Controls.Add(this.rb_color2);
            this.groupBox3.Location = new System.Drawing.Point(12, 12);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(226, 107);
            this.groupBox3.TabIndex = 64;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "顏色(RB共用函數)";
            // 
            // rb_color1
            // 
            this.rb_color1.AutoSize = true;
            this.rb_color1.Checked = true;
            this.rb_color1.ForeColor = System.Drawing.Color.Red;
            this.rb_color1.Location = new System.Drawing.Point(16, 24);
            this.rb_color1.Name = "rb_color1";
            this.rb_color1.Size = new System.Drawing.Size(47, 16);
            this.rb_color1.TabIndex = 12;
            this.rb_color1.TabStop = true;
            this.rb_color1.Text = "紅色";
            this.rb_color1.UseVisualStyleBackColor = true;
            this.rb_color1.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // rb_color3
            // 
            this.rb_color3.AutoSize = true;
            this.rb_color3.ForeColor = System.Drawing.Color.Blue;
            this.rb_color3.Location = new System.Drawing.Point(16, 70);
            this.rb_color3.Name = "rb_color3";
            this.rb_color3.Size = new System.Drawing.Size(47, 16);
            this.rb_color3.TabIndex = 14;
            this.rb_color3.Text = "藍色";
            this.rb_color3.UseVisualStyleBackColor = true;
            this.rb_color3.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // rb_color2
            // 
            this.rb_color2.AutoSize = true;
            this.rb_color2.ForeColor = System.Drawing.Color.Lime;
            this.rb_color2.Location = new System.Drawing.Point(16, 47);
            this.rb_color2.Name = "rb_color2";
            this.rb_color2.Size = new System.Drawing.Size(47, 16);
            this.rb_color2.TabIndex = 13;
            this.rb_color2.Text = "綠色";
            this.rb_color2.UseVisualStyleBackColor = true;
            this.rb_color2.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.rb_style1);
            this.groupBox4.Controls.Add(this.rb_style2);
            this.groupBox4.Controls.Add(this.rb_style3);
            this.groupBox4.Location = new System.Drawing.Point(12, 125);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(226, 99);
            this.groupBox4.TabIndex = 66;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "樣式(RB共用函數)";
            // 
            // rb_style1
            // 
            this.rb_style1.AutoSize = true;
            this.rb_style1.Checked = true;
            this.rb_style1.Location = new System.Drawing.Point(15, 23);
            this.rb_style1.Name = "rb_style1";
            this.rb_style1.Size = new System.Drawing.Size(47, 16);
            this.rb_style1.TabIndex = 2;
            this.rb_style1.TabStop = true;
            this.rb_style1.Text = "Solid";
            this.rb_style1.UseVisualStyleBackColor = true;
            this.rb_style1.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // rb_style2
            // 
            this.rb_style2.AutoSize = true;
            this.rb_style2.Location = new System.Drawing.Point(14, 45);
            this.rb_style2.Name = "rb_style2";
            this.rb_style2.Size = new System.Drawing.Size(46, 16);
            this.rb_style2.TabIndex = 1;
            this.rb_style2.Text = "Dash";
            this.rb_style2.UseVisualStyleBackColor = true;
            this.rb_style2.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // rb_style3
            // 
            this.rb_style3.AutoSize = true;
            this.rb_style3.Location = new System.Drawing.Point(15, 67);
            this.rb_style3.Name = "rb_style3";
            this.rb_style3.Size = new System.Drawing.Size(40, 16);
            this.rb_style3.TabIndex = 0;
            this.rb_style3.Text = "Dot";
            this.rb_style3.UseVisualStyleBackColor = true;
            this.rb_style3.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(263, 18);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(80, 40);
            this.bt_clear.TabIndex = 67;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(484, 461);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "vcs_RadioButton";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton rb_color1;
        private System.Windows.Forms.RadioButton rb_color3;
        private System.Windows.Forms.RadioButton rb_color2;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.RadioButton rb_style1;
        private System.Windows.Forms.RadioButton rb_style2;
        private System.Windows.Forms.RadioButton rb_style3;
        private System.Windows.Forms.Button bt_clear;
    }
}

