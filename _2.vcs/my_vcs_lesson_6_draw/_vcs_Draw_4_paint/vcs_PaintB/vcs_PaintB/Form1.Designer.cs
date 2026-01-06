namespace vcs_PaintB
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_new = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_open = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 54);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            // 
            // bt_new
            // 
            this.bt_new.Location = new System.Drawing.Point(12, 10);
            this.bt_new.Name = "bt_new";
            this.bt_new.Size = new System.Drawing.Size(75, 36);
            this.bt_new.TabIndex = 5;
            this.bt_new.Text = "New";
            this.bt_new.UseVisualStyleBackColor = true;
            this.bt_new.Click += new System.EventHandler(this.bt_new_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(133, 54);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(153, 90);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 108;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_open
            // 
            this.bt_open.Location = new System.Drawing.Point(93, 10);
            this.bt_open.Name = "bt_open";
            this.bt_open.Size = new System.Drawing.Size(75, 36);
            this.bt_open.TabIndex = 109;
            this.bt_open.Text = "Open";
            this.bt_open.UseVisualStyleBackColor = true;
            this.bt_open.Click += new System.EventHandler(this.bt_open_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(417, 359);
            this.Controls.Add(this.bt_open);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_new);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_new;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_open;
    }
}

