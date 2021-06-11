namespace vcs_ReadWrite_TXT4
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
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(136, 48);
            this.button1.TabIndex = 0;
            this.button1.Text = "輸入資料";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 81);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(136, 48);
            this.button2.TabIndex = 1;
            this.button2.Text = "載入資料(TXT)";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 149);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(136, 48);
            this.button3.TabIndex = 2;
            this.button3.Text = "儲存資料(TXT)";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 219);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(136, 48);
            this.button4.TabIndex = 3;
            this.button4.Text = "載入資料(BIN)";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(12, 289);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(136, 48);
            this.button5.TabIndex = 4;
            this.button5.Text = "儲存資料(BIN)";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_clear1
            // 
            this.bt_clear1.Location = new System.Drawing.Point(362, 501);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(80, 36);
            this.bt_clear1.TabIndex = 5;
            this.bt_clear1.Text = "clear";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(165, 81);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(277, 481);
            this.richTextBox1.TabIndex = 6;
            this.richTextBox1.Text = "";
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(448, 12);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(320, 550);
            this.richTextBox2.TabIndex = 7;
            this.richTextBox2.Text = "";
            // 
            // bt_clear2
            // 
            this.bt_clear2.Location = new System.Drawing.Point(688, 501);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(80, 36);
            this.bt_clear2.TabIndex = 8;
            this.bt_clear2.Text = "clear";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // label1
            // 
            this.label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(165, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(277, 45);
            this.label1.TabIndex = 9;
            this.label1.Text = "label1";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(780, 574);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.Button bt_clear2;
        private System.Windows.Forms.Label label1;
    }
}

