namespace vcs_Thread3
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_th3 = new System.Windows.Forms.Button();
            this.bt_th2 = new System.Windows.Forms.Button();
            this.bt_th1 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(149, 62);
            this.button1.TabIndex = 0;
            this.button1.Text = "開啟新的Thread";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(191, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(545, 566);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 91);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(149, 62);
            this.button2.TabIndex = 2;
            this.button2.Text = "開啟新的Thread";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 159);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(149, 62);
            this.button3.TabIndex = 3;
            this.button3.Text = "開啟新的Thread";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_th3);
            this.groupBox1.Controls.Add(this.bt_th2);
            this.groupBox1.Controls.Add(this.bt_th1);
            this.groupBox1.Location = new System.Drawing.Point(12, 288);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(111, 242);
            this.groupBox1.TabIndex = 4;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "groupBox1";
            // 
            // bt_th3
            // 
            this.bt_th3.Location = new System.Drawing.Point(16, 168);
            this.bt_th3.Name = "bt_th3";
            this.bt_th3.Size = new System.Drawing.Size(75, 33);
            this.bt_th3.TabIndex = 6;
            this.bt_th3.Text = "info";
            this.bt_th3.UseVisualStyleBackColor = true;
            this.bt_th3.Click += new System.EventHandler(this.bt_th3_Click);
            // 
            // bt_th2
            // 
            this.bt_th2.Location = new System.Drawing.Point(16, 97);
            this.bt_th2.Name = "bt_th2";
            this.bt_th2.Size = new System.Drawing.Size(75, 33);
            this.bt_th2.TabIndex = 5;
            this.bt_th2.Text = "停止";
            this.bt_th2.UseVisualStyleBackColor = true;
            this.bt_th2.Click += new System.EventHandler(this.bt_th2_Click);
            // 
            // bt_th1
            // 
            this.bt_th1.Location = new System.Drawing.Point(16, 34);
            this.bt_th1.Name = "bt_th1";
            this.bt_th1.Size = new System.Drawing.Size(75, 33);
            this.bt_th1.TabIndex = 4;
            this.bt_th1.Text = "啟動";
            this.bt_th1.UseVisualStyleBackColor = true;
            this.bt_th1.Click += new System.EventHandler(this.bt_th1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(748, 590);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_th3;
        private System.Windows.Forms.Button bt_th2;
        private System.Windows.Forms.Button bt_th1;
    }
}

