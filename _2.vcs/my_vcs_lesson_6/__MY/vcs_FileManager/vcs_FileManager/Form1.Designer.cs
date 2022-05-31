namespace vcs_FileManager
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rb_sort2 = new System.Windows.Forms.RadioButton();
            this.rb_sort1 = new System.Windows.Forms.RadioButton();
            this.rb_sort0 = new System.Windows.Forms.RadioButton();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.cb_show0 = new System.Windows.Forms.CheckBox();
            this.cb_show1 = new System.Windows.Forms.CheckBox();
            this.cb_show2 = new System.Windows.Forms.CheckBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb_sort2);
            this.groupBox1.Controls.Add(this.rb_sort1);
            this.groupBox1.Controls.Add(this.rb_sort0);
            this.groupBox1.Location = new System.Drawing.Point(12, 471);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(166, 145);
            this.groupBox1.TabIndex = 11;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "排序";
            // 
            // rb_sort2
            // 
            this.rb_sort2.AutoSize = true;
            this.rb_sort2.Location = new System.Drawing.Point(16, 104);
            this.rb_sort2.Name = "rb_sort2";
            this.rb_sort2.Size = new System.Drawing.Size(107, 16);
            this.rb_sort2.TabIndex = 2;
            this.rb_sort2.Text = "依檔案日期排序";
            this.rb_sort2.UseVisualStyleBackColor = true;
            // 
            // rb_sort1
            // 
            this.rb_sort1.AutoSize = true;
            this.rb_sort1.Location = new System.Drawing.Point(16, 72);
            this.rb_sort1.Name = "rb_sort1";
            this.rb_sort1.Size = new System.Drawing.Size(107, 16);
            this.rb_sort1.TabIndex = 1;
            this.rb_sort1.Text = "依檔案大小排序";
            this.rb_sort1.UseVisualStyleBackColor = true;
            // 
            // rb_sort0
            // 
            this.rb_sort0.AutoSize = true;
            this.rb_sort0.Checked = true;
            this.rb_sort0.Location = new System.Drawing.Point(16, 33);
            this.rb_sort0.Name = "rb_sort0";
            this.rb_sort0.Size = new System.Drawing.Size(83, 16);
            this.rb_sort0.TabIndex = 0;
            this.rb_sort0.TabStop = true;
            this.rb_sort0.Text = "依檔名排序";
            this.rb_sort0.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 326);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(101, 126);
            this.button3.TabIndex = 10;
            this.button3.Text = "Info";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 169);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(101, 126);
            this.button2.TabIndex = 9;
            this.button2.Text = "從一個資料夾中撈出所有檔案 標準版 多層";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(101, 126);
            this.button1.TabIndex = 8;
            this.button1.Text = "從一個資料夾中撈出所有檔案 標準版  一層";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_clear1
            // 
            this.bt_clear1.Location = new System.Drawing.Point(1114, 591);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(75, 34);
            this.bt_clear1.TabIndex = 13;
            this.bt_clear1.Text = "Clear";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(792, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(397, 613);
            this.richTextBox1.TabIndex = 12;
            this.richTextBox1.Text = "";
            // 
            // bt_clear2
            // 
            this.bt_clear2.Location = new System.Drawing.Point(702, 591);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(75, 34);
            this.bt_clear2.TabIndex = 15;
            this.bt_clear2.Text = "Clear";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(380, 12);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(397, 613);
            this.richTextBox2.TabIndex = 14;
            this.richTextBox2.Text = "";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.cb_show2);
            this.groupBox2.Controls.Add(this.cb_show1);
            this.groupBox2.Controls.Add(this.cb_show0);
            this.groupBox2.Location = new System.Drawing.Point(184, 471);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(166, 145);
            this.groupBox2.TabIndex = 12;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "顯示";
            // 
            // cb_show0
            // 
            this.cb_show0.AutoSize = true;
            this.cb_show0.Checked = true;
            this.cb_show0.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_show0.Enabled = false;
            this.cb_show0.Location = new System.Drawing.Point(20, 33);
            this.cb_show0.Name = "cb_show0";
            this.cb_show0.Size = new System.Drawing.Size(48, 16);
            this.cb_show0.TabIndex = 0;
            this.cb_show0.Text = "檔名";
            this.cb_show0.UseVisualStyleBackColor = true;
            // 
            // cb_show1
            // 
            this.cb_show1.AutoSize = true;
            this.cb_show1.Location = new System.Drawing.Point(20, 72);
            this.cb_show1.Name = "cb_show1";
            this.cb_show1.Size = new System.Drawing.Size(72, 16);
            this.cb_show1.TabIndex = 1;
            this.cb_show1.Text = "檔案大小";
            this.cb_show1.UseVisualStyleBackColor = true;
            // 
            // cb_show2
            // 
            this.cb_show2.AutoSize = true;
            this.cb_show2.Location = new System.Drawing.Point(20, 104);
            this.cb_show2.Name = "cb_show2";
            this.cb_show2.Size = new System.Drawing.Size(72, 16);
            this.cb_show2.TabIndex = 2;
            this.cb_show2.Text = "檔案日期";
            this.cb_show2.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1205, 665);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "檔案管理員";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_sort2;
        private System.Windows.Forms.RadioButton rb_sort1;
        private System.Windows.Forms.RadioButton rb_sort0;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear2;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.CheckBox cb_show2;
        private System.Windows.Forms.CheckBox cb_show1;
        private System.Windows.Forms.CheckBox cb_show0;
    }
}

