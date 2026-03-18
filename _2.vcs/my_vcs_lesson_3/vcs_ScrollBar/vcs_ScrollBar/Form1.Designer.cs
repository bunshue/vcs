namespace vcs_ScrollBar
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
            this.label1 = new System.Windows.Forms.Label();
            this.hScrollBar1 = new System.Windows.Forms.HScrollBar();
            this.vScrollBar1 = new System.Windows.Forms.VScrollBar();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.panel_b = new System.Windows.Forms.Panel();
            this.panel_g = new System.Windows.Forms.Panel();
            this.panel_r = new System.Windows.Forms.Panel();
            this.tb_b = new System.Windows.Forms.TextBox();
            this.tb_g = new System.Windows.Forms.TextBox();
            this.tb_r = new System.Windows.Forms.TextBox();
            this.lb_b = new System.Windows.Forms.Label();
            this.lb_g = new System.Windows.Forms.Label();
            this.lb_r = new System.Windows.Forms.Label();
            this.hScrollBar_b = new System.Windows.Forms.HScrollBar();
            this.hScrollBar_g = new System.Windows.Forms.HScrollBar();
            this.hScrollBar_r = new System.Windows.Forms.HScrollBar();
            this.panel_rgb = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 286);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 11;
            this.label1.Text = "label1";
            // 
            // hScrollBar1
            // 
            this.hScrollBar1.Location = new System.Drawing.Point(11, 253);
            this.hScrollBar1.Name = "hScrollBar1";
            this.hScrollBar1.Size = new System.Drawing.Size(300, 21);
            this.hScrollBar1.TabIndex = 10;
            this.hScrollBar1.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar1_Scroll);
            // 
            // vScrollBar1
            // 
            this.vScrollBar1.Location = new System.Drawing.Point(313, 11);
            this.vScrollBar1.Name = "vScrollBar1";
            this.vScrollBar1.Size = new System.Drawing.Size(21, 240);
            this.vScrollBar1.TabIndex = 9;
            this.vScrollBar1.Scroll += new System.Windows.Forms.ScrollEventHandler(this.vScrollBar1_Scroll);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(11, 11);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(2);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(300, 240);
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(655, 52);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 13;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(639, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 12;
            this.richTextBox1.Text = "";
            // 
            // panel_b
            // 
            this.panel_b.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel_b.Location = new System.Drawing.Point(441, 471);
            this.panel_b.Name = "panel_b";
            this.panel_b.Size = new System.Drawing.Size(100, 50);
            this.panel_b.TabIndex = 24;
            // 
            // panel_g
            // 
            this.panel_g.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel_g.Location = new System.Drawing.Point(441, 408);
            this.panel_g.Name = "panel_g";
            this.panel_g.Size = new System.Drawing.Size(100, 50);
            this.panel_g.TabIndex = 25;
            // 
            // panel_r
            // 
            this.panel_r.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel_r.Location = new System.Drawing.Point(441, 341);
            this.panel_r.Name = "panel_r";
            this.panel_r.Size = new System.Drawing.Size(100, 50);
            this.panel_r.TabIndex = 23;
            // 
            // tb_b
            // 
            this.tb_b.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_b.Location = new System.Drawing.Point(335, 485);
            this.tb_b.Name = "tb_b";
            this.tb_b.Size = new System.Drawing.Size(75, 32);
            this.tb_b.TabIndex = 22;
            this.tb_b.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_g
            // 
            this.tb_g.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_g.Location = new System.Drawing.Point(335, 413);
            this.tb_g.Name = "tb_g";
            this.tb_g.Size = new System.Drawing.Size(75, 32);
            this.tb_g.TabIndex = 21;
            this.tb_g.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_r
            // 
            this.tb_r.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_r.Location = new System.Drawing.Point(335, 350);
            this.tb_r.Name = "tb_r";
            this.tb_r.Size = new System.Drawing.Size(75, 32);
            this.tb_r.TabIndex = 20;
            this.tb_r.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_b
            // 
            this.lb_b.AutoSize = true;
            this.lb_b.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_b.Location = new System.Drawing.Point(13, 488);
            this.lb_b.Name = "lb_b";
            this.lb_b.Size = new System.Drawing.Size(22, 24);
            this.lb_b.TabIndex = 19;
            this.lb_b.Text = "B";
            // 
            // lb_g
            // 
            this.lb_g.AutoSize = true;
            this.lb_g.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_g.Location = new System.Drawing.Point(13, 415);
            this.lb_g.Name = "lb_g";
            this.lb_g.Size = new System.Drawing.Size(22, 24);
            this.lb_g.TabIndex = 18;
            this.lb_g.Text = "G";
            // 
            // lb_r
            // 
            this.lb_r.AutoSize = true;
            this.lb_r.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_r.Location = new System.Drawing.Point(13, 353);
            this.lb_r.Name = "lb_r";
            this.lb_r.Size = new System.Drawing.Size(22, 24);
            this.lb_r.TabIndex = 17;
            this.lb_r.Text = "R";
            // 
            // hScrollBar_b
            // 
            this.hScrollBar_b.LargeChange = 1;
            this.hScrollBar_b.Location = new System.Drawing.Point(48, 488);
            this.hScrollBar_b.Maximum = 255;
            this.hScrollBar_b.Name = "hScrollBar_b";
            this.hScrollBar_b.Size = new System.Drawing.Size(263, 21);
            this.hScrollBar_b.TabIndex = 16;
            this.hScrollBar_b.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar_rgb_Scroll);
            // 
            // hScrollBar_g
            // 
            this.hScrollBar_g.LargeChange = 1;
            this.hScrollBar_g.Location = new System.Drawing.Point(48, 415);
            this.hScrollBar_g.Maximum = 255;
            this.hScrollBar_g.Name = "hScrollBar_g";
            this.hScrollBar_g.Size = new System.Drawing.Size(263, 21);
            this.hScrollBar_g.TabIndex = 15;
            this.hScrollBar_g.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar_rgb_Scroll);
            // 
            // hScrollBar_r
            // 
            this.hScrollBar_r.LargeChange = 1;
            this.hScrollBar_r.Location = new System.Drawing.Point(48, 353);
            this.hScrollBar_r.Maximum = 255;
            this.hScrollBar_r.Name = "hScrollBar_r";
            this.hScrollBar_r.Size = new System.Drawing.Size(263, 21);
            this.hScrollBar_r.TabIndex = 14;
            this.hScrollBar_r.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar_rgb_Scroll);
            // 
            // panel_rgb
            // 
            this.panel_rgb.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel_rgb.Location = new System.Drawing.Point(416, 326);
            this.panel_rgb.Name = "panel_rgb";
            this.panel_rgb.Size = new System.Drawing.Size(159, 210);
            this.panel_rgb.TabIndex = 24;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(772, 684);
            this.Controls.Add(this.panel_b);
            this.Controls.Add(this.panel_g);
            this.Controls.Add(this.panel_r);
            this.Controls.Add(this.tb_b);
            this.Controls.Add(this.tb_g);
            this.Controls.Add(this.tb_r);
            this.Controls.Add(this.lb_b);
            this.Controls.Add(this.lb_g);
            this.Controls.Add(this.lb_r);
            this.Controls.Add(this.hScrollBar_b);
            this.Controls.Add(this.hScrollBar_g);
            this.Controls.Add(this.hScrollBar_r);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.hScrollBar1);
            this.Controls.Add(this.vScrollBar1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.panel_rgb);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.HScrollBar hScrollBar1;
        private System.Windows.Forms.VScrollBar vScrollBar1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Panel panel_b;
        private System.Windows.Forms.Panel panel_g;
        private System.Windows.Forms.Panel panel_r;
        private System.Windows.Forms.TextBox tb_b;
        private System.Windows.Forms.TextBox tb_g;
        private System.Windows.Forms.TextBox tb_r;
        private System.Windows.Forms.Label lb_b;
        private System.Windows.Forms.Label lb_g;
        private System.Windows.Forms.Label lb_r;
        private System.Windows.Forms.HScrollBar hScrollBar_b;
        private System.Windows.Forms.HScrollBar hScrollBar_g;
        private System.Windows.Forms.HScrollBar hScrollBar_r;
        private System.Windows.Forms.Panel panel_rgb;
    }
}

