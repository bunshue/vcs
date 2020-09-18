namespace vcs_MouseKety_Form
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.lb_shift = new System.Windows.Forms.Label();
            this.lb_ctrl = new System.Windows.Forms.Label();
            this.lb_alt = new System.Windows.Forms.Label();
            this.lb_key = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(12, 84);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(240, 32);
            this.label1.TabIndex = 0;
            this.label1.Text = "Form抓各種按鍵";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(12, 18);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(87, 32);
            this.label2.TabIndex = 1;
            this.label2.Text = "label2";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(237, 150);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(305, 400);
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // lb_shift
            // 
            this.lb_shift.AutoSize = true;
            this.lb_shift.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_shift.Location = new System.Drawing.Point(26, 458);
            this.lb_shift.Name = "lb_shift";
            this.lb_shift.Size = new System.Drawing.Size(73, 32);
            this.lb_shift.TabIndex = 6;
            this.lb_shift.Text = "Shift";
            // 
            // lb_ctrl
            // 
            this.lb_ctrl.AutoSize = true;
            this.lb_ctrl.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_ctrl.Location = new System.Drawing.Point(12, 503);
            this.lb_ctrl.Name = "lb_ctrl";
            this.lb_ctrl.Size = new System.Drawing.Size(61, 32);
            this.lb_ctrl.TabIndex = 7;
            this.lb_ctrl.Text = "Ctrl";
            // 
            // lb_alt
            // 
            this.lb_alt.AutoSize = true;
            this.lb_alt.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_alt.Location = new System.Drawing.Point(79, 503);
            this.lb_alt.Name = "lb_alt";
            this.lb_alt.Size = new System.Drawing.Size(53, 32);
            this.lb_alt.TabIndex = 8;
            this.lb_alt.Text = "Alt";
            // 
            // lb_key
            // 
            this.lb_key.AutoSize = true;
            this.lb_key.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_key.Location = new System.Drawing.Point(142, 480);
            this.lb_key.Name = "lb_key";
            this.lb_key.Size = new System.Drawing.Size(65, 32);
            this.lb_key.TabIndex = 9;
            this.lb_key.Text = "Key";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(810, 630);
            this.Controls.Add(this.lb_key);
            this.Controls.Add(this.lb_alt);
            this.Controls.Add(this.lb_ctrl);
            this.Controls.Add(this.lb_shift);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.Form1_KeyPress);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lb_shift;
        private System.Windows.Forms.Label lb_ctrl;
        private System.Windows.Forms.Label lb_alt;
        private System.Windows.Forms.Label lb_key;
    }
}

