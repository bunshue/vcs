namespace vcs_DriveInfo2
{
    partial class Form_Setup
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
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.bt_setup6 = new System.Windows.Forms.Button();
            this.bt_setup5 = new System.Windows.Forms.Button();
            this.tb_setup0 = new System.Windows.Forms.TextBox();
            this.lb_setup0 = new System.Windows.Forms.Label();
            this.tb_setup1 = new System.Windows.Forms.TextBox();
            this.lb_setup1 = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(40, 330);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(123, 24);
            this.lb_main_mesg.TabIndex = 39;
            this.lb_main_mesg.Text = "main_mesg";
            // 
            // bt_setup6
            // 
            this.bt_setup6.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup6.Location = new System.Drawing.Point(499, 349);
            this.bt_setup6.Name = "bt_setup6";
            this.bt_setup6.Size = new System.Drawing.Size(94, 32);
            this.bt_setup6.TabIndex = 38;
            this.bt_setup6.Text = "儲存";
            this.bt_setup6.UseVisualStyleBackColor = true;
            this.bt_setup6.Click += new System.EventHandler(this.bt_setup6_Click);
            // 
            // bt_setup5
            // 
            this.bt_setup5.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup5.Location = new System.Drawing.Point(499, 297);
            this.bt_setup5.Name = "bt_setup5";
            this.bt_setup5.Size = new System.Drawing.Size(94, 32);
            this.bt_setup5.TabIndex = 36;
            this.bt_setup5.Text = "取消";
            this.bt_setup5.UseVisualStyleBackColor = true;
            this.bt_setup5.Click += new System.EventHandler(this.bt_setup5_Click);
            // 
            // tb_setup0
            // 
            this.tb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_setup0.Location = new System.Drawing.Point(133, 22);
            this.tb_setup0.Name = "tb_setup0";
            this.tb_setup0.Size = new System.Drawing.Size(350, 30);
            this.tb_setup0.TabIndex = 21;
            this.tb_setup0.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_setup0
            // 
            this.lb_setup0.AutoSize = true;
            this.lb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_setup0.Location = new System.Drawing.Point(31, 25);
            this.lb_setup0.Name = "lb_setup0";
            this.lb_setup0.Size = new System.Drawing.Size(99, 19);
            this.lb_setup0.TabIndex = 32;
            this.lb_setup0.Text = "lb_setup0";
            // 
            // tb_setup1
            // 
            this.tb_setup1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_setup1.Location = new System.Drawing.Point(133, 61);
            this.tb_setup1.Name = "tb_setup1";
            this.tb_setup1.Size = new System.Drawing.Size(350, 30);
            this.tb_setup1.TabIndex = 23;
            this.tb_setup1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_setup1
            // 
            this.lb_setup1.AutoSize = true;
            this.lb_setup1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_setup1.Location = new System.Drawing.Point(31, 69);
            this.lb_setup1.Name = "lb_setup1";
            this.lb_setup1.Size = new System.Drawing.Size(99, 19);
            this.lb_setup1.TabIndex = 20;
            this.lb_setup1.Text = "lb_setup1";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(644, 421);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.bt_setup6);
            this.Controls.Add(this.bt_setup5);
            this.Controls.Add(this.tb_setup0);
            this.Controls.Add(this.lb_setup0);
            this.Controls.Add(this.tb_setup1);
            this.Controls.Add(this.lb_setup1);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Button bt_setup6;
        private System.Windows.Forms.Button bt_setup5;
        private System.Windows.Forms.TextBox tb_setup0;
        private System.Windows.Forms.Label lb_setup0;
        private System.Windows.Forms.TextBox tb_setup1;
        private System.Windows.Forms.Label lb_setup1;
        private System.Windows.Forms.Timer timer_display;
    }
}