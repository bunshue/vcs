namespace vcs_ImageConversion
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
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 552);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(99, 42);
            this.button1.TabIndex = 0;
            this.button1.Text = "選取檔案";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(176, 57);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(72, 42);
            this.button2.TabIndex = 1;
            this.button2.Text = "轉換";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(386, 479);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // bt_clear1
            // 
            this.bt_clear1.Location = new System.Drawing.Point(330, 450);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(68, 41);
            this.bt_clear1.TabIndex = 3;
            this.bt_clear1.Text = "清除";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(415, 12);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(386, 624);
            this.richTextBox2.TabIndex = 4;
            this.richTextBox2.Text = "";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.checkBox1);
            this.groupBox1.Controls.Add(this.button2);
            this.groupBox1.Location = new System.Drawing.Point(120, 517);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(278, 119);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "影像格式轉換";
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(176, 30);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(72, 16);
            this.checkBox1.TabIndex = 2;
            this.checkBox1.Text = "覆蓋原檔";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // bt_clear2
            // 
            this.bt_clear2.Location = new System.Drawing.Point(733, 595);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(68, 41);
            this.bt_clear2.TabIndex = 6;
            this.bt_clear2.Text = "清除";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(817, 648);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.Button bt_clear2;
    }
}

