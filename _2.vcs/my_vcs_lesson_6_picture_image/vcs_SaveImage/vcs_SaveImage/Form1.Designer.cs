namespace vcs_SaveImage
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button1 = new System.Windows.Forms.Button();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.rb_filetype2 = new System.Windows.Forms.RadioButton();
            this.rb_filetype1 = new System.Windows.Forms.RadioButton();
            this.bt_open_folder = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 15);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(123, 74);
            this.button1.TabIndex = 0;
            this.button1.Text = "網頁 / Office / PrintScreen 存圖";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(12, 102);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(123, 24);
            this.lb_main_mesg.TabIndex = 2;
            this.lb_main_mesg.Text = "main_mesg";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // rb_filetype2
            // 
            this.rb_filetype2.AutoSize = true;
            this.rb_filetype2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype2.Location = new System.Drawing.Point(143, 80);
            this.rb_filetype2.Name = "rb_filetype2";
            this.rb_filetype2.Size = new System.Drawing.Size(54, 20);
            this.rb_filetype2.TabIndex = 13;
            this.rb_filetype2.Text = "bmp";
            this.rb_filetype2.UseVisualStyleBackColor = true;
            // 
            // rb_filetype1
            // 
            this.rb_filetype1.AutoSize = true;
            this.rb_filetype1.Checked = true;
            this.rb_filetype1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype1.Location = new System.Drawing.Point(143, 58);
            this.rb_filetype1.Name = "rb_filetype1";
            this.rb_filetype1.Size = new System.Drawing.Size(46, 20);
            this.rb_filetype1.TabIndex = 12;
            this.rb_filetype1.TabStop = true;
            this.rb_filetype1.Text = "jpg";
            this.rb_filetype1.UseVisualStyleBackColor = true;
            // 
            // bt_open_folder
            // 
            this.bt_open_folder.Location = new System.Drawing.Point(150, 12);
            this.bt_open_folder.Name = "bt_open_folder";
            this.bt_open_folder.Size = new System.Drawing.Size(40, 40);
            this.bt_open_folder.TabIndex = 11;
            this.bt_open_folder.UseVisualStyleBackColor = true;
            this.bt_open_folder.Click += new System.EventHandler(this.bt_open_folder_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(201, 139);
            this.Controls.Add(this.rb_filetype2);
            this.Controls.Add(this.rb_filetype1);
            this.Controls.Add(this.bt_open_folder);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.button1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Form1";
            this.Text = "存圖";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.RadioButton rb_filetype2;
        private System.Windows.Forms.RadioButton rb_filetype1;
        private System.Windows.Forms.Button bt_open_folder;
    }
}

