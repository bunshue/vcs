namespace vcs_Process6_TabTip
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
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.richTextBox3 = new System.Windows.Forms.RichTextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.richTextBox4 = new System.Windows.Forms.RichTextBox();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // richTextBox3
            // 
            this.richTextBox3.Location = new System.Drawing.Point(125, 151);
            this.richTextBox3.Name = "richTextBox3";
            this.richTextBox3.Size = new System.Drawing.Size(942, 52);
            this.richTextBox3.TabIndex = 11;
            this.richTextBox3.Text = "";
            this.richTextBox3.MouseDown += new System.Windows.Forms.MouseEventHandler(this.richTextBox3_MouseDown);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 151);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(107, 52);
            this.button3.TabIndex = 10;
            this.button3.Text = "輸入資料";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(125, 84);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(942, 52);
            this.richTextBox2.TabIndex = 9;
            this.richTextBox2.Text = "";
            this.richTextBox2.MouseDown += new System.Windows.Forms.MouseEventHandler(this.richTextBox2_MouseDown);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 84);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(107, 52);
            this.button2.TabIndex = 8;
            this.button2.Text = "輸入資料";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(125, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(942, 52);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            this.richTextBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.richTextBox1_MouseDown);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(107, 52);
            this.button1.TabIndex = 6;
            this.button1.Text = "輸入資料";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 295);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(107, 52);
            this.button4.TabIndex = 12;
            this.button4.Text = "關閉螢幕鍵盤";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // richTextBox4
            // 
            this.richTextBox4.Location = new System.Drawing.Point(125, 295);
            this.richTextBox4.Name = "richTextBox4";
            this.richTextBox4.Size = new System.Drawing.Size(942, 211);
            this.richTextBox4.TabIndex = 13;
            this.richTextBox4.Text = "";
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(12, 369);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(107, 52);
            this.button5.TabIndex = 14;
            this.button5.Text = "螢幕鍵盤Info";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1006, 476);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 30);
            this.bt_clear.TabIndex = 50;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1078, 515);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.richTextBox4);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.richTextBox3);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.RichTextBox richTextBox3;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.RichTextBox richTextBox4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_clear;
    }
}

