namespace vcs_ShowFont
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
            this.bt_open_folder = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.bt_minus = new System.Windows.Forms.Button();
            this.bt_plus = new System.Windows.Forms.Button();
            this.tb_font_size = new System.Windows.Forms.TextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_x = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // bt_open_folder
            // 
            this.bt_open_folder.Location = new System.Drawing.Point(20, 20);
            this.bt_open_folder.Name = "bt_open_folder";
            this.bt_open_folder.Size = new System.Drawing.Size(60, 60);
            this.bt_open_folder.TabIndex = 0;
            this.bt_open_folder.UseVisualStyleBackColor = true;
            this.bt_open_folder.Click += new System.EventHandler(this.bt_open_folder_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(100, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 19);
            this.label1.TabIndex = 1;
            this.label1.Text = "label1";
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(100, 50);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(330, 20);
            this.comboBox1.TabIndex = 2;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.richTextBox1.Location = new System.Drawing.Point(0, 523);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(715, 147);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(20, 100);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(176, 64);
            this.label2.TabIndex = 4;
            this.label2.Text = "label2";
            // 
            // bt_minus
            // 
            this.bt_minus.Location = new System.Drawing.Point(643, 78);
            this.bt_minus.Name = "bt_minus";
            this.bt_minus.Size = new System.Drawing.Size(60, 60);
            this.bt_minus.TabIndex = 5;
            this.bt_minus.UseVisualStyleBackColor = true;
            this.bt_minus.Click += new System.EventHandler(this.bt_minus_Click);
            // 
            // bt_plus
            // 
            this.bt_plus.Location = new System.Drawing.Point(643, 12);
            this.bt_plus.Name = "bt_plus";
            this.bt_plus.Size = new System.Drawing.Size(60, 60);
            this.bt_plus.TabIndex = 6;
            this.bt_plus.UseVisualStyleBackColor = true;
            this.bt_plus.Click += new System.EventHandler(this.bt_plus_Click);
            // 
            // tb_font_size
            // 
            this.tb_font_size.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_font_size.Location = new System.Drawing.Point(557, 12);
            this.tb_font_size.Name = "tb_font_size";
            this.tb_font_size.Size = new System.Drawing.Size(80, 36);
            this.tb_font_size.TabIndex = 7;
            this.tb_font_size.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(643, 144);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 60);
            this.bt_clear.TabIndex = 8;
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_x
            // 
            this.bt_x.Location = new System.Drawing.Point(643, 210);
            this.bt_x.Name = "bt_x";
            this.bt_x.Size = new System.Drawing.Size(60, 60);
            this.bt_x.TabIndex = 9;
            this.bt_x.UseVisualStyleBackColor = true;
            this.bt_x.Click += new System.EventHandler(this.bt_x_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(715, 670);
            this.Controls.Add(this.bt_x);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.tb_font_size);
            this.Controls.Add(this.bt_plus);
            this.Controls.Add(this.bt_minus);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bt_open_folder);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_open_folder;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button bt_minus;
        private System.Windows.Forms.Button bt_plus;
        private System.Windows.Forms.TextBox tb_font_size;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_x;
    }
}

