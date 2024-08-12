namespace vcs_BarcodeScanner
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
            this.tb_wait_barcode_data = new System.Windows.Forms.TextBox();
            this.tb_barcode_data = new System.Windows.Forms.TextBox();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.label0 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer_barcode = new System.Windows.Forms.Timer(this.components);
            this.button01 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tb_wait_barcode_data
            // 
            this.tb_wait_barcode_data.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_wait_barcode_data.Location = new System.Drawing.Point(148, 117);
            this.tb_wait_barcode_data.Multiline = true;
            this.tb_wait_barcode_data.Name = "tb_wait_barcode_data";
            this.tb_wait_barcode_data.Size = new System.Drawing.Size(335, 22);
            this.tb_wait_barcode_data.TabIndex = 105;
            this.tb_wait_barcode_data.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_barcode_data
            // 
            this.tb_barcode_data.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_barcode_data.Location = new System.Drawing.Point(148, 56);
            this.tb_barcode_data.Name = "tb_barcode_data";
            this.tb_barcode_data.Size = new System.Drawing.Size(518, 32);
            this.tb_barcode_data.TabIndex = 104;
            this.tb_barcode_data.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(12, 9);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1.TabIndex = 134;
            this.lb_main_mesg1.Text = "mesg1";
            // 
            // label0
            // 
            this.label0.AutoSize = true;
            this.label0.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label0.Location = new System.Drawing.Point(12, 59);
            this.label0.Name = "label0";
            this.label0.Size = new System.Drawing.Size(106, 24);
            this.label0.TabIndex = 135;
            this.label0.Text = "取得資料";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(16, 156);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(736, 154);
            this.richTextBox1.TabIndex = 136;
            this.richTextBox1.Text = "";
            // 
            // timer_barcode
            // 
            this.timer_barcode.Enabled = true;
            this.timer_barcode.Interval = 300;
            this.timer_barcode.Tick += new System.EventHandler(this.timer_barcode_Tick);
            // 
            // button01
            // 
            this.button01.Location = new System.Drawing.Point(672, 54);
            this.button01.Name = "button01";
            this.button01.Size = new System.Drawing.Size(80, 40);
            this.button01.TabIndex = 137;
            this.button01.Text = "網頁連線";
            this.button01.UseVisualStyleBackColor = true;
            this.button01.Click += new System.EventHandler(this.button01_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 115);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(106, 24);
            this.label1.TabIndex = 138;
            this.label1.Text = "等待資料";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(681, 280);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(71, 30);
            this.bt_clear.TabIndex = 139;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(768, 342);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button01);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label0);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.tb_wait_barcode_data);
            this.Controls.Add(this.tb_barcode_data);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tb_wait_barcode_data;
        private System.Windows.Forms.TextBox tb_barcode_data;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Label label0;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer_barcode;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button bt_clear;
    }
}

