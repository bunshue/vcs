namespace vcs_ListView2
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
            this.bt_clear = new System.Windows.Forms.Button();
            this.lb_main_mesg0 = new System.Windows.Forms.Label();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.lb_main_mesg3 = new System.Windows.Forms.Label();
            this.lb_main_mesg2 = new System.Windows.Forms.Label();
            this.lb_main_mesg4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(12, 12);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 116;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // lb_main_mesg0
            // 
            this.lb_main_mesg0.AutoSize = true;
            this.lb_main_mesg0.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg0.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg0.Location = new System.Drawing.Point(12, 55);
            this.lb_main_mesg0.Name = "lb_main_mesg0";
            this.lb_main_mesg0.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg0.TabIndex = 134;
            this.lb_main_mesg0.Text = "mesg1";
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(12, 88);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1.TabIndex = 135;
            this.lb_main_mesg1.Text = "mesg1";
            // 
            // lb_main_mesg3
            // 
            this.lb_main_mesg3.AutoSize = true;
            this.lb_main_mesg3.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg3.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg3.Location = new System.Drawing.Point(12, 161);
            this.lb_main_mesg3.Name = "lb_main_mesg3";
            this.lb_main_mesg3.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg3.TabIndex = 136;
            this.lb_main_mesg3.Text = "mesg1";
            // 
            // lb_main_mesg2
            // 
            this.lb_main_mesg2.AutoSize = true;
            this.lb_main_mesg2.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2.Location = new System.Drawing.Point(12, 124);
            this.lb_main_mesg2.Name = "lb_main_mesg2";
            this.lb_main_mesg2.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg2.TabIndex = 136;
            this.lb_main_mesg2.Text = "mesg1";
            // 
            // lb_main_mesg4
            // 
            this.lb_main_mesg4.AutoSize = true;
            this.lb_main_mesg4.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg4.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg4.Location = new System.Drawing.Point(12, 185);
            this.lb_main_mesg4.Name = "lb_main_mesg4";
            this.lb_main_mesg4.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg4.TabIndex = 137;
            this.lb_main_mesg4.Text = "mesg1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 284);
            this.Controls.Add(this.lb_main_mesg4);
            this.Controls.Add(this.lb_main_mesg2);
            this.Controls.Add(this.lb_main_mesg3);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.lb_main_mesg0);
            this.Controls.Add(this.bt_clear);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Label lb_main_mesg0;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Label lb_main_mesg3;
        private System.Windows.Forms.Label lb_main_mesg2;
        private System.Windows.Forms.Label lb_main_mesg4;
    }
}

