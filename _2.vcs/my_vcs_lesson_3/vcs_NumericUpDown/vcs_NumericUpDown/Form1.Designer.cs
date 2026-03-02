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
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            this.SuspendLayout();
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown1.Location = new System.Drawing.Point(12, 42);
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(200, 33);
            this.numericUpDown1.TabIndex = 0;
            this.numericUpDown1.ValueChanged += new System.EventHandler(this.numericUpDown1_ValueChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 165);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(653, 349);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // bt_plus
            // 
            this.bt_plus.Location = new System.Drawing.Point(228, 23);
            this.bt_plus.Name = "bt_plus";
            this.bt_plus.Size = new System.Drawing.Size(32, 32);
            this.bt_plus.TabIndex = 2;
            this.bt_plus.Text = "+";
            this.bt_plus.UseVisualStyleBackColor = true;
            this.bt_plus.Click += new System.EventHandler(this.bt_plus_Click);
            // 
            // bt_minus
            // 
            this.bt_minus.Location = new System.Drawing.Point(228, 61);
            this.bt_minus.Name = "bt_minus";
            this.bt_minus.Size = new System.Drawing.Size(32, 32);
            this.bt_minus.TabIndex = 3;
            this.bt_minus.Text = "-";
            this.bt_minus.UseVisualStyleBackColor = true;
            this.bt_minus.Click += new System.EventHandler(this.bt_minus_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(677, 526);
            this.Controls.Add(this.bt_minus);
            this.Controls.Add(this.bt_plus);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.numericUpDown1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDown1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_plus;
        private System.Windows.Forms.Button bt_minus;
    }
}

