namespace vcs_PictureCrop9
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
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.lb_x = new System.Windows.Forms.Label();
            this.lb_y = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.lb_h = new System.Windows.Forms.Label();
            this.tb_x = new System.Windows.Forms.TextBox();
            this.tb_y = new System.Windows.Forms.TextBox();
            this.tb_w = new System.Windows.Forms.TextBox();
            this.tb_h = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(10, 10);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(210, 129);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(116, 42);
            this.button1.TabIndex = 1;
            this.button1.Text = "crop";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(226, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(120, 10);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 3;
            this.pictureBox2.TabStop = false;
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(245, 55);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 132;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // lb_x
            // 
            this.lb_x.AutoSize = true;
            this.lb_x.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_x.Location = new System.Drawing.Point(12, 132);
            this.lb_x.Name = "lb_x";
            this.lb_x.Size = new System.Drawing.Size(58, 21);
            this.lb_x.TabIndex = 133;
            this.lb_x.Text = "label1";
            // 
            // lb_y
            // 
            this.lb_y.AutoSize = true;
            this.lb_y.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y.Location = new System.Drawing.Point(10, 169);
            this.lb_y.Name = "lb_y";
            this.lb_y.Size = new System.Drawing.Size(58, 21);
            this.lb_y.TabIndex = 134;
            this.lb_y.Text = "label2";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(12, 204);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(58, 21);
            this.lb_w.TabIndex = 135;
            this.lb_w.Text = "label3";
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(12, 241);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(58, 21);
            this.lb_h.TabIndex = 136;
            this.lb_h.Text = "label4";
            // 
            // tb_x
            // 
            this.tb_x.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_x.Location = new System.Drawing.Point(73, 129);
            this.tb_x.Name = "tb_x";
            this.tb_x.Size = new System.Drawing.Size(100, 33);
            this.tb_x.TabIndex = 137;
            // 
            // tb_y
            // 
            this.tb_y.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_y.Location = new System.Drawing.Point(73, 166);
            this.tb_y.Name = "tb_y";
            this.tb_y.Size = new System.Drawing.Size(100, 33);
            this.tb_y.TabIndex = 138;
            // 
            // tb_w
            // 
            this.tb_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_w.Location = new System.Drawing.Point(73, 201);
            this.tb_w.Name = "tb_w";
            this.tb_w.Size = new System.Drawing.Size(100, 33);
            this.tb_w.TabIndex = 139;
            // 
            // tb_h
            // 
            this.tb_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_h.Location = new System.Drawing.Point(73, 238);
            this.tb_h.Name = "tb_h";
            this.tb_h.Size = new System.Drawing.Size(100, 33);
            this.tb_h.TabIndex = 140;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(483, 418);
            this.Controls.Add(this.tb_h);
            this.Controls.Add(this.tb_w);
            this.Controls.Add(this.tb_y);
            this.Controls.Add(this.tb_x);
            this.Controls.Add(this.lb_h);
            this.Controls.Add(this.lb_w);
            this.Controls.Add(this.lb_y);
            this.Controls.Add(this.lb_x);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Label lb_x;
        private System.Windows.Forms.Label lb_y;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.TextBox tb_x;
        private System.Windows.Forms.TextBox tb_y;
        private System.Windows.Forms.TextBox tb_w;
        private System.Windows.Forms.TextBox tb_h;
    }
}

