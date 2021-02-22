namespace vcs_programming
{
    partial class order
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該公開 Managed 資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.chkBPizza = new System.Windows.Forms.CheckBox();
            this.chkSPizza = new System.Windows.Forms.CheckBox();
            this.chkChicken = new System.Windows.Forms.CheckBox();
            this.chkFish = new System.Windows.Forms.CheckBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rdbBig = new System.Windows.Forms.RadioButton();
            this.rdbSmall = new System.Windows.Forms.RadioButton();
            this.chkFries = new System.Windows.Forms.CheckBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.rdbBlackTea = new System.Windows.Forms.RadioButton();
            this.rdbCoffee = new System.Windows.Forms.RadioButton();
            this.rdbCoke = new System.Windows.Forms.RadioButton();
            this.chkDrink = new System.Windows.Forms.CheckBox();
            this.btnOrder = new System.Windows.Forms.Button();
            this.lblOutput = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.chkBPizza);
            this.groupBox1.Controls.Add(this.chkSPizza);
            this.groupBox1.Controls.Add(this.chkChicken);
            this.groupBox1.Controls.Add(this.chkFish);
            this.groupBox1.Location = new System.Drawing.Point(22, 20);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(4);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(4);
            this.groupBox1.Size = new System.Drawing.Size(200, 191);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "漢堡/披薩";
            // 
            // chkBPizza
            // 
            this.chkBPizza.AutoSize = true;
            this.chkBPizza.Location = new System.Drawing.Point(26, 149);
            this.chkBPizza.Margin = new System.Windows.Forms.Padding(4);
            this.chkBPizza.Name = "chkBPizza";
            this.chkBPizza.Size = new System.Drawing.Size(111, 20);
            this.chkBPizza.TabIndex = 1;
            this.chkBPizza.Text = "大披薩 $429";
            this.chkBPizza.UseVisualStyleBackColor = true;
            // 
            // chkSPizza
            // 
            this.chkSPizza.AutoSize = true;
            this.chkSPizza.Location = new System.Drawing.Point(26, 109);
            this.chkSPizza.Margin = new System.Windows.Forms.Padding(4);
            this.chkSPizza.Name = "chkSPizza";
            this.chkSPizza.Size = new System.Drawing.Size(111, 20);
            this.chkSPizza.TabIndex = 1;
            this.chkSPizza.Text = "小披薩 $259";
            this.chkSPizza.UseVisualStyleBackColor = true;
            // 
            // chkChicken
            // 
            this.chkChicken.AutoSize = true;
            this.chkChicken.Location = new System.Drawing.Point(26, 68);
            this.chkChicken.Margin = new System.Windows.Forms.Padding(4);
            this.chkChicken.Name = "chkChicken";
            this.chkChicken.Size = new System.Drawing.Size(135, 20);
            this.chkChicken.TabIndex = 1;
            this.chkChicken.Text = "勁辣雞腿堡 $69";
            this.chkChicken.UseVisualStyleBackColor = true;
            // 
            // chkFish
            // 
            this.chkFish.AutoSize = true;
            this.chkFish.Location = new System.Drawing.Point(26, 28);
            this.chkFish.Margin = new System.Windows.Forms.Padding(4);
            this.chkFish.Name = "chkFish";
            this.chkFish.Size = new System.Drawing.Size(127, 20);
            this.chkFish.TabIndex = 1;
            this.chkFish.Text = "麥香魚堡 ＄59";
            this.chkFish.UseVisualStyleBackColor = true;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rdbBig);
            this.groupBox2.Controls.Add(this.rdbSmall);
            this.groupBox2.Controls.Add(this.chkFries);
            this.groupBox2.Location = new System.Drawing.Point(249, 20);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(4);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(4);
            this.groupBox2.Size = new System.Drawing.Size(243, 73);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            // 
            // rdbBig
            // 
            this.rdbBig.AutoSize = true;
            this.rdbBig.Location = new System.Drawing.Point(120, 29);
            this.rdbBig.Margin = new System.Windows.Forms.Padding(4);
            this.rdbBig.Name = "rdbBig";
            this.rdbBig.Size = new System.Drawing.Size(86, 20);
            this.rdbBig.TabIndex = 2;
            this.rdbBig.Text = "大薯 $35";
            this.rdbBig.UseVisualStyleBackColor = true;
            // 
            // rdbSmall
            // 
            this.rdbSmall.AutoSize = true;
            this.rdbSmall.Checked = true;
            this.rdbSmall.Location = new System.Drawing.Point(9, 29);
            this.rdbSmall.Margin = new System.Windows.Forms.Padding(4);
            this.rdbSmall.Name = "rdbSmall";
            this.rdbSmall.Size = new System.Drawing.Size(86, 20);
            this.rdbSmall.TabIndex = 1;
            this.rdbSmall.TabStop = true;
            this.rdbSmall.Text = "小薯 $25";
            this.rdbSmall.UseVisualStyleBackColor = true;
            // 
            // chkFries
            // 
            this.chkFries.AutoSize = true;
            this.chkFries.Location = new System.Drawing.Point(30, 0);
            this.chkFries.Margin = new System.Windows.Forms.Padding(4);
            this.chkFries.Name = "chkFries";
            this.chkFries.Size = new System.Drawing.Size(59, 20);
            this.chkFries.TabIndex = 0;
            this.chkFries.Text = "薯條";
            this.chkFries.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.rdbBlackTea);
            this.groupBox3.Controls.Add(this.rdbCoffee);
            this.groupBox3.Controls.Add(this.rdbCoke);
            this.groupBox3.Controls.Add(this.chkDrink);
            this.groupBox3.Location = new System.Drawing.Point(249, 101);
            this.groupBox3.Margin = new System.Windows.Forms.Padding(4);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Padding = new System.Windows.Forms.Padding(4);
            this.groupBox3.Size = new System.Drawing.Size(242, 108);
            this.groupBox3.TabIndex = 2;
            this.groupBox3.TabStop = false;
            // 
            // rdbBlackTea
            // 
            this.rdbBlackTea.AutoSize = true;
            this.rdbBlackTea.Location = new System.Drawing.Point(30, 80);
            this.rdbBlackTea.Margin = new System.Windows.Forms.Padding(4);
            this.rdbBlackTea.Name = "rdbBlackTea";
            this.rdbBlackTea.Size = new System.Drawing.Size(86, 20);
            this.rdbBlackTea.TabIndex = 3;
            this.rdbBlackTea.Text = "紅茶 $20";
            this.rdbBlackTea.UseVisualStyleBackColor = true;
            // 
            // rdbCoffee
            // 
            this.rdbCoffee.AutoSize = true;
            this.rdbCoffee.Location = new System.Drawing.Point(30, 53);
            this.rdbCoffee.Margin = new System.Windows.Forms.Padding(4);
            this.rdbCoffee.Name = "rdbCoffee";
            this.rdbCoffee.Size = new System.Drawing.Size(90, 20);
            this.rdbCoffee.TabIndex = 2;
            this.rdbCoffee.Text = "咖啡  $30";
            this.rdbCoffee.UseVisualStyleBackColor = true;
            // 
            // rdbCoke
            // 
            this.rdbCoke.AutoSize = true;
            this.rdbCoke.Checked = true;
            this.rdbCoke.Location = new System.Drawing.Point(30, 25);
            this.rdbCoke.Margin = new System.Windows.Forms.Padding(4);
            this.rdbCoke.Name = "rdbCoke";
            this.rdbCoke.Size = new System.Drawing.Size(86, 20);
            this.rdbCoke.TabIndex = 1;
            this.rdbCoke.TabStop = true;
            this.rdbCoke.Text = "可樂 $25";
            this.rdbCoke.UseVisualStyleBackColor = true;
            // 
            // chkDrink
            // 
            this.chkDrink.AutoSize = true;
            this.chkDrink.Location = new System.Drawing.Point(30, 0);
            this.chkDrink.Margin = new System.Windows.Forms.Padding(4);
            this.chkDrink.Name = "chkDrink";
            this.chkDrink.Size = new System.Drawing.Size(59, 20);
            this.chkDrink.TabIndex = 0;
            this.chkDrink.Text = "飲料";
            this.chkDrink.UseVisualStyleBackColor = true;
            // 
            // btnOrder
            // 
            this.btnOrder.Location = new System.Drawing.Point(22, 224);
            this.btnOrder.Margin = new System.Windows.Forms.Padding(4);
            this.btnOrder.Name = "btnOrder";
            this.btnOrder.Size = new System.Drawing.Size(129, 47);
            this.btnOrder.TabIndex = 3;
            this.btnOrder.Text = "點餐";
            this.btnOrder.UseVisualStyleBackColor = true;
            this.btnOrder.Click += new System.EventHandler(this.btnOrder_Click);
            // 
            // lblOutput
            // 
            this.lblOutput.BackColor = System.Drawing.SystemColors.Control;
            this.lblOutput.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblOutput.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblOutput.ForeColor = System.Drawing.SystemColors.ControlText;
            this.lblOutput.Location = new System.Drawing.Point(249, 224);
            this.lblOutput.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblOutput.Name = "lblOutput";
            this.lblOutput.Size = new System.Drawing.Size(241, 47);
            this.lblOutput.TabIndex = 4;
            this.lblOutput.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(167, 224);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(55, 47);
            this.label1.TabIndex = 5;
            this.label1.Text = "金額 :";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // order
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(513, 288);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblOutput);
            this.Controls.Add(this.btnOrder);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "order";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "點餐系統";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox chkBPizza;
        private System.Windows.Forms.CheckBox chkSPizza;
        private System.Windows.Forms.CheckBox chkChicken;
        private System.Windows.Forms.CheckBox chkFish;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rdbBig;
        private System.Windows.Forms.RadioButton rdbSmall;
        private System.Windows.Forms.CheckBox chkFries;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton rdbBlackTea;
        private System.Windows.Forms.RadioButton rdbCoffee;
        private System.Windows.Forms.RadioButton rdbCoke;
        private System.Windows.Forms.CheckBox chkDrink;
        private System.Windows.Forms.Button btnOrder;
        private System.Windows.Forms.Label lblOutput;
        private System.Windows.Forms.Label label1;
    }
}

