namespace vcs_PropertiesSettingsDefault
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.tb_location = new System.Windows.Forms.TextBox();
            this.tb_h = new System.Windows.Forms.TextBox();
            this.tb_w = new System.Windows.Forms.TextBox();
            this.tb_right = new System.Windows.Forms.TextBox();
            this.tb_bottom = new System.Windows.Forms.TextBox();
            this.tb_left = new System.Windows.Forms.TextBox();
            this.tb_top = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(521, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(359, 569);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            // 
            // tb_location
            // 
            this.tb_location.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_location.Location = new System.Drawing.Point(49, 406);
            this.tb_location.Name = "tb_location";
            this.tb_location.Size = new System.Drawing.Size(315, 36);
            this.tb_location.TabIndex = 14;
            // 
            // tb_h
            // 
            this.tb_h.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_h.Location = new System.Drawing.Point(213, 468);
            this.tb_h.Name = "tb_h";
            this.tb_h.Size = new System.Drawing.Size(151, 36);
            this.tb_h.TabIndex = 13;
            // 
            // tb_w
            // 
            this.tb_w.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_w.Location = new System.Drawing.Point(49, 468);
            this.tb_w.Name = "tb_w";
            this.tb_w.Size = new System.Drawing.Size(151, 36);
            this.tb_w.TabIndex = 12;
            // 
            // tb_right
            // 
            this.tb_right.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_right.Location = new System.Drawing.Point(213, 263);
            this.tb_right.Name = "tb_right";
            this.tb_right.Size = new System.Drawing.Size(151, 36);
            this.tb_right.TabIndex = 11;
            // 
            // tb_bottom
            // 
            this.tb_bottom.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_bottom.Location = new System.Drawing.Point(111, 332);
            this.tb_bottom.Name = "tb_bottom";
            this.tb_bottom.Size = new System.Drawing.Size(151, 36);
            this.tb_bottom.TabIndex = 10;
            // 
            // tb_left
            // 
            this.tb_left.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_left.Location = new System.Drawing.Point(36, 263);
            this.tb_left.Name = "tb_left";
            this.tb_left.Size = new System.Drawing.Size(151, 36);
            this.tb_left.TabIndex = 9;
            // 
            // tb_top
            // 
            this.tb_top.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_top.Location = new System.Drawing.Point(111, 190);
            this.tb_top.Name = "tb_top";
            this.tb_top.Size = new System.Drawing.Size(151, 36);
            this.tb_top.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(25, 29);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 24);
            this.label1.TabIndex = 15;
            this.label1.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(892, 593);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tb_location);
            this.Controls.Add(this.tb_h);
            this.Controls.Add(this.tb_w);
            this.Controls.Add(this.tb_right);
            this.Controls.Add(this.tb_bottom);
            this.Controls.Add(this.tb_left);
            this.Controls.Add(this.tb_top);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "儲存參數到 Properties.Settings.Default";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Move += new System.EventHandler(this.Form1_Move);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.TextBox tb_location;
        private System.Windows.Forms.TextBox tb_h;
        private System.Windows.Forms.TextBox tb_w;
        private System.Windows.Forms.TextBox tb_right;
        private System.Windows.Forms.TextBox tb_bottom;
        private System.Windows.Forms.TextBox tb_left;
        private System.Windows.Forms.TextBox tb_top;
        private System.Windows.Forms.Label label1;
    }
}

