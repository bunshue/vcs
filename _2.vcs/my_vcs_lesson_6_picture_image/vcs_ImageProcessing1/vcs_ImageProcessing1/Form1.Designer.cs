namespace vcs_ImageProcessing1
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
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.trackBar_R = new System.Windows.Forms.TrackBar();
            this.trackBar_G = new System.Windows.Forms.TrackBar();
            this.trackBar_B = new System.Windows.Forms.TrackBar();
            this.button1 = new System.Windows.Forms.Button();
            this.tb_R = new System.Windows.Forms.TextBox();
            this.tb_G = new System.Windows.Forms.TextBox();
            this.tb_B = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            this.button20 = new System.Windows.Forms.Button();
            this.button21 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_R)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_G)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_B)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(12, 498);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(640, 480);
            this.pictureBox2.TabIndex = 1;
            this.pictureBox2.TabStop = false;
            // 
            // trackBar_R
            // 
            this.trackBar_R.Location = new System.Drawing.Point(671, 51);
            this.trackBar_R.Maximum = 200;
            this.trackBar_R.Name = "trackBar_R";
            this.trackBar_R.Size = new System.Drawing.Size(436, 45);
            this.trackBar_R.TabIndex = 2;
            this.trackBar_R.Value = 100;
            this.trackBar_R.Scroll += new System.EventHandler(this.trackBar_R_Scroll);
            // 
            // trackBar_G
            // 
            this.trackBar_G.Location = new System.Drawing.Point(671, 118);
            this.trackBar_G.Maximum = 200;
            this.trackBar_G.Name = "trackBar_G";
            this.trackBar_G.Size = new System.Drawing.Size(436, 45);
            this.trackBar_G.TabIndex = 3;
            this.trackBar_G.Value = 100;
            this.trackBar_G.Scroll += new System.EventHandler(this.trackBar_G_Scroll);
            // 
            // trackBar_B
            // 
            this.trackBar_B.Location = new System.Drawing.Point(671, 178);
            this.trackBar_B.Maximum = 200;
            this.trackBar_B.Name = "trackBar_B";
            this.trackBar_B.Size = new System.Drawing.Size(436, 45);
            this.trackBar_B.TabIndex = 4;
            this.trackBar_B.Value = 100;
            this.trackBar_B.Scroll += new System.EventHandler(this.trackBar_B_Scroll);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1113, 230);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(71, 37);
            this.button1.TabIndex = 5;
            this.button1.Text = "OK";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // tb_R
            // 
            this.tb_R.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_R.Location = new System.Drawing.Point(1113, 51);
            this.tb_R.Name = "tb_R";
            this.tb_R.Size = new System.Drawing.Size(71, 36);
            this.tb_R.TabIndex = 6;
            this.tb_R.Text = "100";
            this.tb_R.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_G
            // 
            this.tb_G.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_G.Location = new System.Drawing.Point(1113, 118);
            this.tb_G.Name = "tb_G";
            this.tb_G.Size = new System.Drawing.Size(71, 36);
            this.tb_G.TabIndex = 7;
            this.tb_G.Text = "100";
            this.tb_G.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_B
            // 
            this.tb_B.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_B.Location = new System.Drawing.Point(1113, 178);
            this.tb_B.Name = "tb_B";
            this.tb_B.Size = new System.Drawing.Size(71, 36);
            this.tb_B.TabIndex = 8;
            this.tb_B.Text = "100";
            this.tb_B.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(671, 498);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(509, 480);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(748, 229);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(71, 37);
            this.button2.TabIndex = 10;
            this.button2.Text = "+ 10%";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(748, 283);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(71, 37);
            this.button3.TabIndex = 11;
            this.button3.Text = "- 10%";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(671, 229);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(71, 37);
            this.button4.TabIndex = 12;
            this.button4.Text = "R";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(671, 283);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(71, 37);
            this.button5.TabIndex = 13;
            this.button5.Text = "G";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(671, 338);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(71, 37);
            this.button6.TabIndex = 14;
            this.button6.Text = "B";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(1113, 283);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(71, 37);
            this.button7.TabIndex = 15;
            this.button7.Text = "clear";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(671, 392);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(71, 37);
            this.button8.TabIndex = 16;
            this.button8.Text = "水平Mirror";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(671, 445);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(71, 37);
            this.button9.TabIndex = 17;
            this.button9.Text = "垂直Mirror";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(748, 392);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(71, 37);
            this.button10.TabIndex = 18;
            this.button10.Text = "擷取其中一塊";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(748, 445);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(71, 37);
            this.button11.TabIndex = 19;
            this.button11.Text = "摺頁效果";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(825, 445);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(71, 37);
            this.button13.TabIndex = 21;
            this.button13.Text = "縮圖成一半";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(825, 392);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(71, 37);
            this.button14.TabIndex = 22;
            this.button14.Text = "轉成藍色系";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(825, 229);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(100, 37);
            this.button16.TabIndex = 24;
            this.button16.Text = "對圖片做Marshal處理1";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(919, 457);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(75, 23);
            this.button17.TabIndex = 27;
            this.button17.Text = "降亮度";
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(919, 419);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(75, 23);
            this.button18.TabIndex = 26;
            this.button18.Text = "找過亮";
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // button19
            // 
            this.button19.Location = new System.Drawing.Point(919, 390);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(75, 23);
            this.button19.TabIndex = 25;
            this.button19.Text = "開啟圖片";
            this.button19.UseVisualStyleBackColor = true;
            this.button19.Click += new System.EventHandler(this.button19_Click);
            // 
            // button20
            // 
            this.button20.Location = new System.Drawing.Point(1000, 433);
            this.button20.Name = "button20";
            this.button20.Size = new System.Drawing.Size(48, 23);
            this.button20.TabIndex = 28;
            this.button20.Text = "存圖";
            this.button20.UseVisualStyleBackColor = true;
            this.button20.Click += new System.EventHandler(this.button20_Click);
            // 
            // button21
            // 
            this.button21.Location = new System.Drawing.Point(825, 283);
            this.button21.Name = "button21";
            this.button21.Size = new System.Drawing.Size(100, 37);
            this.button21.TabIndex = 29;
            this.button21.Text = "對圖片做Marshal處理2";
            this.button21.UseVisualStyleBackColor = true;
            this.button21.Click += new System.EventHandler(this.button21_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1192, 987);
            this.Controls.Add(this.button21);
            this.Controls.Add(this.button20);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button18);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.button16);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.tb_B);
            this.Controls.Add(this.tb_G);
            this.Controls.Add(this.tb_R);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.trackBar_B);
            this.Controls.Add(this.trackBar_G);
            this.Controls.Add(this.trackBar_R);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "ImageProcessing";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_R)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_G)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_B)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.TrackBar trackBar_R;
        private System.Windows.Forms.TrackBar trackBar_G;
        private System.Windows.Forms.TrackBar trackBar_B;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox tb_R;
        private System.Windows.Forms.TextBox tb_G;
        private System.Windows.Forms.TextBox tb_B;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Button button19;
        private System.Windows.Forms.Button button20;
        private System.Windows.Forms.Button button21;
    }
}

