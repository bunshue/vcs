namespace vcs_FolderInfo
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
            this.btn_test6 = new System.Windows.Forms.Button();
            this.btn_test8 = new System.Windows.Forms.Button();
            this.btn_test7 = new System.Windows.Forms.Button();
            this.btn_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.listView1 = new System.Windows.Forms.ListView();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_test6
            // 
            this.btn_test6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btn_test6.Location = new System.Drawing.Point(22, 12);
            this.btn_test6.Name = "btn_test6";
            this.btn_test6.Size = new System.Drawing.Size(222, 36);
            this.btn_test6.TabIndex = 5;
            this.btn_test6.Text = "獲得指定目錄下的所有文檔";
            this.btn_test6.UseVisualStyleBackColor = true;
            this.btn_test6.Click += new System.EventHandler(this.btn_test6_Click);
            // 
            // btn_test8
            // 
            this.btn_test8.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btn_test8.Location = new System.Drawing.Point(22, 119);
            this.btn_test8.Name = "btn_test8";
            this.btn_test8.Size = new System.Drawing.Size(222, 36);
            this.btn_test8.TabIndex = 7;
            this.btn_test8.Text = "xxx";
            this.btn_test8.UseVisualStyleBackColor = true;
            this.btn_test8.Click += new System.EventHandler(this.btn_test8_Click);
            // 
            // btn_test7
            // 
            this.btn_test7.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btn_test7.Location = new System.Drawing.Point(22, 66);
            this.btn_test7.Name = "btn_test7";
            this.btn_test7.Size = new System.Drawing.Size(222, 36);
            this.btn_test7.TabIndex = 6;
            this.btn_test7.Text = "xxx";
            this.btn_test7.UseVisualStyleBackColor = true;
            this.btn_test7.Click += new System.EventHandler(this.btn_test7_Click);
            // 
            // btn_clear
            // 
            this.btn_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btn_clear.Location = new System.Drawing.Point(12, 563);
            this.btn_clear.Name = "btn_clear";
            this.btn_clear.Size = new System.Drawing.Size(148, 36);
            this.btn_clear.TabIndex = 8;
            this.btn_clear.Text = "clear";
            this.btn_clear.UseVisualStyleBackColor = true;
            this.btn_clear.Click += new System.EventHandler(this.btn_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(267, 345);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(761, 254);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(22, 226);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(222, 36);
            this.button1.TabIndex = 11;
            this.button1.Text = "xxx";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(22, 173);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(222, 36);
            this.button2.TabIndex = 10;
            this.button2.Text = "xxx";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // listView1
            // 
            this.listView1.Location = new System.Drawing.Point(267, 12);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(761, 327);
            this.listView1.TabIndex = 12;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(8, 406);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 16);
            this.label1.TabIndex = 13;
            this.label1.Text = "路徑";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1040, 611);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btn_clear);
            this.Controls.Add(this.btn_test8);
            this.Controls.Add(this.btn_test7);
            this.Controls.Add(this.btn_test6);
            this.KeyPreview = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_test6;
        private System.Windows.Forms.Button btn_test8;
        private System.Windows.Forms.Button btn_test7;
        private System.Windows.Forms.Button btn_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Label label1;
    }
}

