namespace vcs_SendTo_All
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_copy = new System.Windows.Forms.Button();
            this.bt_save = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.bt_setup = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.richTextBox1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(0, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(622, 535);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            // 
            // bt_copy
            // 
            this.bt_copy.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_copy.BackgroundImage")));
            this.bt_copy.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bt_copy.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy.ForeColor = System.Drawing.Color.Black;
            this.bt_copy.Location = new System.Drawing.Point(570, 12);
            this.bt_copy.Name = "bt_copy";
            this.bt_copy.Size = new System.Drawing.Size(40, 40);
            this.bt_copy.TabIndex = 44;
            this.bt_copy.UseVisualStyleBackColor = true;
            this.bt_copy.Click += new System.EventHandler(this.bt_copy_Click);
            // 
            // bt_save
            // 
            this.bt_save.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_save.BackgroundImage")));
            this.bt_save.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bt_save.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.ForeColor = System.Drawing.Color.Black;
            this.bt_save.Location = new System.Drawing.Point(524, 12);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(40, 40);
            this.bt_save.TabIndex = 45;
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // bt_setup
            // 
            this.bt_setup.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_setup.BackgroundImage")));
            this.bt_setup.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bt_setup.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup.ForeColor = System.Drawing.Color.Black;
            this.bt_setup.Location = new System.Drawing.Point(570, 58);
            this.bt_setup.Name = "bt_setup";
            this.bt_setup.Size = new System.Drawing.Size(40, 40);
            this.bt_setup.TabIndex = 46;
            this.bt_setup.UseVisualStyleBackColor = true;
            this.bt_setup.Click += new System.EventHandler(this.bt_setup_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(622, 535);
            this.Controls.Add(this.bt_setup);
            this.Controls.Add(this.bt_save);
            this.Controls.Add(this.bt_copy);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "檢視檔案內容";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_copy;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.Button bt_setup;
    }
}

