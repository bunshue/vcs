namespace vcs_Remove_Bin_Obj
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
            this.lb_setup0 = new System.Windows.Forms.Label();
            this.tb_setup0 = new System.Windows.Forms.TextBox();
            this.bt_setup0 = new System.Windows.Forms.Button();
            this.bt_setup_save = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // lb_setup0
            // 
            this.lb_setup0.AutoSize = true;
            this.lb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_setup0.Location = new System.Drawing.Point(25, 22);
            this.lb_setup0.Name = "lb_setup0";
            this.lb_setup0.Size = new System.Drawing.Size(99, 19);
            this.lb_setup0.TabIndex = 7;
            this.lb_setup0.Text = "lb_setup0";
            // 
            // tb_setup0
            // 
            this.tb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_setup0.Location = new System.Drawing.Point(127, 19);
            this.tb_setup0.Name = "tb_setup0";
            this.tb_setup0.Size = new System.Drawing.Size(574, 30);
            this.tb_setup0.TabIndex = 1;
            // 
            // bt_setup0
            // 
            this.bt_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup0.Location = new System.Drawing.Point(689, 21);
            this.bt_setup0.Name = "bt_setup0";
            this.bt_setup0.Size = new System.Drawing.Size(94, 32);
            this.bt_setup0.TabIndex = 17;
            this.bt_setup0.Text = "修改";
            this.bt_setup0.UseVisualStyleBackColor = true;
            this.bt_setup0.Click += new System.EventHandler(this.bt_setup0_Click);
            // 
            // bt_setup_save
            // 
            this.bt_setup_save.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup_save.Location = new System.Drawing.Point(689, 385);
            this.bt_setup_save.Name = "bt_setup_save";
            this.bt_setup_save.Size = new System.Drawing.Size(94, 32);
            this.bt_setup_save.TabIndex = 18;
            this.bt_setup_save.Text = "儲存";
            this.bt_setup_save.UseVisualStyleBackColor = true;
            this.bt_setup_save.Click += new System.EventHandler(this.bt_setup_save_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(25, 403);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(123, 24);
            this.lb_main_mesg.TabIndex = 19;
            this.lb_main_mesg.Text = "main_mesg";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(903, 515);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.bt_setup_save);
            this.Controls.Add(this.bt_setup0);
            this.Controls.Add(this.tb_setup0);
            this.Controls.Add(this.lb_setup0);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_setup0;
        private System.Windows.Forms.TextBox tb_setup0;
        private System.Windows.Forms.Button bt_setup0;
        private System.Windows.Forms.Button bt_setup_save;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Timer timer_display;
    }
}