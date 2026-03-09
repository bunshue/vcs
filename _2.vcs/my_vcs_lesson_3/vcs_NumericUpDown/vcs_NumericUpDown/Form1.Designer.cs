namespace vcs_NumericUpDown
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
            this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_plus = new System.Windows.Forms.Button();
            this.bt_minus = new System.Windows.Forms.Button();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.domainUpDown1 = new System.Windows.Forms.DomainUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            this.groupBox0.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown1.Location = new System.Drawing.Point(22, 59);
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(200, 33);
            this.numericUpDown1.TabIndex = 0;
            this.numericUpDown1.ValueChanged += new System.EventHandler(this.numericUpDown1_ValueChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(20, 185);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // bt_plus
            // 
            this.bt_plus.Location = new System.Drawing.Point(238, 40);
            this.bt_plus.Name = "bt_plus";
            this.bt_plus.Size = new System.Drawing.Size(32, 32);
            this.bt_plus.TabIndex = 2;
            this.bt_plus.Text = "+";
            this.bt_plus.UseVisualStyleBackColor = true;
            this.bt_plus.Click += new System.EventHandler(this.bt_plus_Click);
            // 
            // bt_minus
            // 
            this.bt_minus.Location = new System.Drawing.Point(238, 78);
            this.bt_minus.Name = "bt_minus";
            this.bt_minus.Size = new System.Drawing.Size(32, 32);
            this.bt_minus.TabIndex = 3;
            this.bt_minus.Text = "-";
            this.bt_minus.UseVisualStyleBackColor = true;
            this.bt_minus.Click += new System.EventHandler(this.bt_minus_Click);
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.numericUpDown1);
            this.groupBox0.Controls.Add(this.bt_plus);
            this.groupBox0.Controls.Add(this.bt_minus);
            this.groupBox0.Location = new System.Drawing.Point(20, 20);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(300, 150);
            this.groupBox0.TabIndex = 4;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "NumericUpDown";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.domainUpDown1);
            this.groupBox1.Location = new System.Drawing.Point(339, 20);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(300, 150);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "DomainUpDown";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(42, 226);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 9;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // domainUpDown1
            // 
            this.domainUpDown1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.domainUpDown1.Location = new System.Drawing.Point(26, 59);
            this.domainUpDown1.Name = "domainUpDown1";
            this.domainUpDown1.Size = new System.Drawing.Size(226, 33);
            this.domainUpDown1.TabIndex = 0;
            this.domainUpDown1.Text = "domainUpDown1";
            this.domainUpDown1.SelectedItemChanged += new System.EventHandler(this.domainUpDown1_SelectedItemChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(661, 384);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            this.groupBox0.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDown1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_plus;
        private System.Windows.Forms.Button bt_minus;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.DomainUpDown domainUpDown1;
    }
}

