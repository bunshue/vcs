namespace vcs_MyCalculator
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
            this.textBox0 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.groupBox_type1 = new System.Windows.Forms.GroupBox();
            this.rb_type1b = new System.Windows.Forms.RadioButton();
            this.rb_type1a = new System.Windows.Forms.RadioButton();
            this.groupBox_type2 = new System.Windows.Forms.GroupBox();
            this.rb_type2b = new System.Windows.Forms.RadioButton();
            this.rb_type2a = new System.Windows.Forms.RadioButton();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_calculate0 = new System.Windows.Forms.Button();
            this.bt_calculate1 = new System.Windows.Forms.Button();
            this.label0 = new System.Windows.Forms.Label();
            this.groupBox_type1.SuspendLayout();
            this.groupBox_type2.SuspendLayout();
            this.SuspendLayout();
            // 
            // textBox0
            // 
            this.textBox0.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox0.Location = new System.Drawing.Point(22, 33);
            this.textBox0.Name = "textBox0";
            this.textBox0.Size = new System.Drawing.Size(120, 46);
            this.textBox0.TabIndex = 0;
            this.textBox0.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textBox0.Click += new System.EventHandler(this.textBox0_Click);
            this.textBox0.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox0_KeyPress);
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox2.Location = new System.Drawing.Point(612, 33);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(120, 46);
            this.textBox2.TabIndex = 1;
            this.textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(323, 33);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(120, 46);
            this.textBox1.TabIndex = 2;
            this.textBox1.Text = "1";
            this.textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textBox1.Click += new System.EventHandler(this.textBox1_Click);
            this.textBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
            // 
            // groupBox_type1
            // 
            this.groupBox_type1.Controls.Add(this.rb_type1b);
            this.groupBox_type1.Controls.Add(this.rb_type1a);
            this.groupBox_type1.Location = new System.Drawing.Point(177, 25);
            this.groupBox_type1.Name = "groupBox_type1";
            this.groupBox_type1.Size = new System.Drawing.Size(80, 70);
            this.groupBox_type1.TabIndex = 3;
            this.groupBox_type1.TabStop = false;
            // 
            // rb_type1b
            // 
            this.rb_type1b.AutoSize = true;
            this.rb_type1b.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_type1b.Location = new System.Drawing.Point(10, 35);
            this.rb_type1b.Name = "rb_type1b";
            this.rb_type1b.Size = new System.Drawing.Size(64, 23);
            this.rb_type1b.TabIndex = 1;
            this.rb_type1b.TabStop = true;
            this.rb_type1b.Text = "KB/s";
            this.rb_type1b.UseVisualStyleBackColor = true;
            // 
            // rb_type1a
            // 
            this.rb_type1a.AutoSize = true;
            this.rb_type1a.Checked = true;
            this.rb_type1a.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_type1a.Location = new System.Drawing.Point(10, 15);
            this.rb_type1a.Name = "rb_type1a";
            this.rb_type1a.Size = new System.Drawing.Size(67, 23);
            this.rb_type1a.TabIndex = 0;
            this.rb_type1a.TabStop = true;
            this.rb_type1a.Text = "MB/s";
            this.rb_type1a.UseVisualStyleBackColor = true;
            // 
            // groupBox_type2
            // 
            this.groupBox_type2.Controls.Add(this.rb_type2b);
            this.groupBox_type2.Controls.Add(this.rb_type2a);
            this.groupBox_type2.Location = new System.Drawing.Point(12, 178);
            this.groupBox_type2.Name = "groupBox_type2";
            this.groupBox_type2.Size = new System.Drawing.Size(80, 70);
            this.groupBox_type2.TabIndex = 4;
            this.groupBox_type2.TabStop = false;
            // 
            // rb_type2b
            // 
            this.rb_type2b.AutoSize = true;
            this.rb_type2b.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_type2b.Location = new System.Drawing.Point(10, 35);
            this.rb_type2b.Name = "rb_type2b";
            this.rb_type2b.Size = new System.Drawing.Size(64, 23);
            this.rb_type2b.TabIndex = 1;
            this.rb_type2b.TabStop = true;
            this.rb_type2b.Text = "KB/s";
            this.rb_type2b.UseVisualStyleBackColor = true;
            // 
            // rb_type2a
            // 
            this.rb_type2a.AutoSize = true;
            this.rb_type2a.Checked = true;
            this.rb_type2a.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_type2a.Location = new System.Drawing.Point(10, 15);
            this.rb_type2a.Name = "rb_type2a";
            this.rb_type2a.Size = new System.Drawing.Size(67, 23);
            this.rb_type2a.TabIndex = 0;
            this.rb_type2a.TabStop = true;
            this.rb_type2a.Text = "MB/s";
            this.rb_type2a.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(489, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 19);
            this.label1.TabIndex = 5;
            this.label1.Text = "小時";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(297, 202);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(28, 19);
            this.label2.TabIndex = 6;
            this.label2.Text = "傳";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 515);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(28, 552);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(62, 36);
            this.bt_clear.TabIndex = 8;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_calculate0
            // 
            this.bt_calculate0.Location = new System.Drawing.Point(542, 25);
            this.bt_calculate0.Name = "bt_calculate0";
            this.bt_calculate0.Size = new System.Drawing.Size(45, 45);
            this.bt_calculate0.TabIndex = 9;
            this.bt_calculate0.Text = "計算";
            this.bt_calculate0.UseVisualStyleBackColor = true;
            this.bt_calculate0.Click += new System.EventHandler(this.bt_calculate0_Click);
            // 
            // bt_calculate1
            // 
            this.bt_calculate1.Location = new System.Drawing.Point(98, 191);
            this.bt_calculate1.Name = "bt_calculate1";
            this.bt_calculate1.Size = new System.Drawing.Size(45, 45);
            this.bt_calculate1.TabIndex = 10;
            this.bt_calculate1.Text = "計算";
            this.bt_calculate1.UseVisualStyleBackColor = true;
            this.bt_calculate1.Click += new System.EventHandler(this.bt_calculate1_Click);
            // 
            // label0
            // 
            this.label0.AutoSize = true;
            this.label0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label0.Location = new System.Drawing.Point(280, 33);
            this.label0.Name = "label0";
            this.label0.Size = new System.Drawing.Size(28, 19);
            this.label0.TabIndex = 11;
            this.label0.Text = "傳";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(896, 627);
            this.Controls.Add(this.label0);
            this.Controls.Add(this.bt_calculate1);
            this.Controls.Add(this.bt_calculate0);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.groupBox_type2);
            this.Controls.Add(this.groupBox_type1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_type1.ResumeLayout(false);
            this.groupBox_type1.PerformLayout();
            this.groupBox_type2.ResumeLayout(false);
            this.groupBox_type2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox0;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.GroupBox groupBox_type1;
        private System.Windows.Forms.RadioButton rb_type1b;
        private System.Windows.Forms.RadioButton rb_type1a;
        private System.Windows.Forms.GroupBox groupBox_type2;
        private System.Windows.Forms.RadioButton rb_type2b;
        private System.Windows.Forms.RadioButton rb_type2a;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_calculate0;
        private System.Windows.Forms.Button bt_calculate1;
        private System.Windows.Forms.Label label0;
    }
}

