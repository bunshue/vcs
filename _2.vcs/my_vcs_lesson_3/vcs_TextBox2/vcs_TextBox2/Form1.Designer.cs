namespace vcs_TextBox2
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
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.tb_auto_complete2 = new System.Windows.Forms.TextBox();
            this.tb_auto_complete1 = new System.Windows.Forms.TextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.textBox0 = new System.Windows.Forms.TextBox();
            this.label3a = new System.Windows.Forms.Label();
            this.label2a = new System.Windows.Forms.Label();
            this.label1a = new System.Windows.Forms.Label();
            this.label0a = new System.Windows.Forms.Label();
            this.label3b = new System.Windows.Forms.Label();
            this.label2b = new System.Windows.Forms.Label();
            this.label1b = new System.Windows.Forms.Label();
            this.label0b = new System.Windows.Forms.Label();
            this.groupBox0.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.tb_auto_complete2);
            this.groupBox0.Controls.Add(this.tb_auto_complete1);
            this.groupBox0.Location = new System.Drawing.Point(12, 12);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(286, 136);
            this.groupBox0.TabIndex = 0;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "自動完成";
            // 
            // tb_auto_complete2
            // 
            this.tb_auto_complete2.Location = new System.Drawing.Point(19, 88);
            this.tb_auto_complete2.Name = "tb_auto_complete2";
            this.tb_auto_complete2.Size = new System.Drawing.Size(244, 22);
            this.tb_auto_complete2.TabIndex = 12;
            // 
            // tb_auto_complete1
            // 
            this.tb_auto_complete1.Location = new System.Drawing.Point(19, 34);
            this.tb_auto_complete1.Name = "tb_auto_complete1";
            this.tb_auto_complete1.Size = new System.Drawing.Size(244, 22);
            this.tb_auto_complete1.TabIndex = 11;
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(850, 42);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 39;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(823, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 38;
            this.richTextBox1.Text = "";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label3b);
            this.groupBox1.Controls.Add(this.label2b);
            this.groupBox1.Controls.Add(this.label1b);
            this.groupBox1.Controls.Add(this.label0b);
            this.groupBox1.Controls.Add(this.label3a);
            this.groupBox1.Controls.Add(this.label2a);
            this.groupBox1.Controls.Add(this.label1a);
            this.groupBox1.Controls.Add(this.label0a);
            this.groupBox1.Controls.Add(this.textBox0);
            this.groupBox1.Controls.Add(this.textBox3);
            this.groupBox1.Controls.Add(this.textBox1);
            this.groupBox1.Controls.Add(this.textBox2);
            this.groupBox1.Location = new System.Drawing.Point(317, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(286, 136);
            this.groupBox1.TabIndex = 13;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "限制輸入";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(90, 41);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(110, 22);
            this.textBox1.TabIndex = 12;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(90, 68);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(110, 22);
            this.textBox2.TabIndex = 11;
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(90, 96);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(110, 22);
            this.textBox3.TabIndex = 13;
            // 
            // textBox0
            // 
            this.textBox0.Location = new System.Drawing.Point(90, 15);
            this.textBox0.Name = "textBox0";
            this.textBox0.Size = new System.Drawing.Size(110, 22);
            this.textBox0.TabIndex = 14;
            // 
            // label3a
            // 
            this.label3a.AutoSize = true;
            this.label3a.Location = new System.Drawing.Point(49, 106);
            this.label3a.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3a.Name = "label3a";
            this.label3a.Size = new System.Drawing.Size(29, 12);
            this.label3a.TabIndex = 15;
            this.label3a.Text = "金額";
            // 
            // label2a
            // 
            this.label2a.AutoSize = true;
            this.label2a.Location = new System.Drawing.Point(49, 71);
            this.label2a.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2a.Name = "label2a";
            this.label2a.Size = new System.Drawing.Size(29, 12);
            this.label2a.TabIndex = 16;
            this.label2a.Text = "數量";
            // 
            // label1a
            // 
            this.label1a.AutoSize = true;
            this.label1a.Location = new System.Drawing.Point(49, 48);
            this.label1a.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1a.Name = "label1a";
            this.label1a.Size = new System.Drawing.Size(29, 12);
            this.label1a.TabIndex = 17;
            this.label1a.Text = "單價";
            // 
            // label0a
            // 
            this.label0a.AutoSize = true;
            this.label0a.Location = new System.Drawing.Point(17, 25);
            this.label0a.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label0a.Name = "label0a";
            this.label0a.Size = new System.Drawing.Size(53, 12);
            this.label0a.TabIndex = 18;
            this.label0a.Text = "產品編號";
            // 
            // label3b
            // 
            this.label3b.AutoSize = true;
            this.label3b.Location = new System.Drawing.Point(210, 99);
            this.label3b.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3b.Name = "label3b";
            this.label3b.Size = new System.Drawing.Size(29, 12);
            this.label3b.TabIndex = 19;
            this.label3b.Text = "金額";
            // 
            // label2b
            // 
            this.label2b.AutoSize = true;
            this.label2b.Location = new System.Drawing.Point(210, 64);
            this.label2b.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2b.Name = "label2b";
            this.label2b.Size = new System.Drawing.Size(29, 12);
            this.label2b.TabIndex = 20;
            this.label2b.Text = "數量";
            // 
            // label1b
            // 
            this.label1b.AutoSize = true;
            this.label1b.Location = new System.Drawing.Point(207, 44);
            this.label1b.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1b.Name = "label1b";
            this.label1b.Size = new System.Drawing.Size(29, 12);
            this.label1b.TabIndex = 21;
            this.label1b.Text = "單價";
            // 
            // label0b
            // 
            this.label0b.AutoSize = true;
            this.label0b.Location = new System.Drawing.Point(210, 18);
            this.label0b.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label0b.Name = "label0b";
            this.label0b.Size = new System.Drawing.Size(53, 12);
            this.label0b.TabIndex = 22;
            this.label0b.Text = "產品編號";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(935, 591);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.TextBox tb_auto_complete2;
        private System.Windows.Forms.TextBox tb_auto_complete1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label3a;
        private System.Windows.Forms.Label label2a;
        private System.Windows.Forms.Label label1a;
        private System.Windows.Forms.Label label0a;
        private System.Windows.Forms.TextBox textBox0;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label3b;
        private System.Windows.Forms.Label label2b;
        private System.Windows.Forms.Label label1b;
        private System.Windows.Forms.Label label0b;
    }
}

