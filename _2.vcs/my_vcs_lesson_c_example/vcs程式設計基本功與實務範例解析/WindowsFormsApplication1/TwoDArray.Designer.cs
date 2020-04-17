namespace WindowsFormsApplication1
{
    partial class TwoDArray
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnSearch = new System.Windows.Forms.Button();
            this.txtName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnCompute = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.chkCourseAvg = new System.Windows.Forms.CheckBox();
            this.chkRank = new System.Windows.Forms.CheckBox();
            this.chkFailNum = new System.Windows.Forms.CheckBox();
            this.chkAvg = new System.Windows.Forms.CheckBox();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnSearch
            // 
            this.btnSearch.Location = new System.Drawing.Point(280, 203);
            this.btnSearch.Name = "btnSearch";
            this.btnSearch.Size = new System.Drawing.Size(149, 33);
            this.btnSearch.TabIndex = 11;
            this.btnSearch.Text = "搜尋成績";
            this.btnSearch.UseVisualStyleBackColor = true;
            this.btnSearch.Click += new System.EventHandler(this.btnSearch_Click);
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(62, 208);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(201, 27);
            this.txtName.TabIndex = 10;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 211);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 16);
            this.label1.TabIndex = 9;
            this.label1.Text = "名字:";
            // 
            // btnCompute
            // 
            this.btnCompute.Location = new System.Drawing.Point(432, 155);
            this.btnCompute.Name = "btnCompute";
            this.btnCompute.Size = new System.Drawing.Size(160, 33);
            this.btnCompute.TabIndex = 8;
            this.btnCompute.Text = "計算";
            this.btnCompute.UseVisualStyleBackColor = true;
            this.btnCompute.Click += new System.EventHandler(this.btnCompute_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.chkCourseAvg);
            this.groupBox1.Controls.Add(this.chkRank);
            this.groupBox1.Controls.Add(this.chkFailNum);
            this.groupBox1.Controls.Add(this.chkAvg);
            this.groupBox1.Location = new System.Drawing.Point(432, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(160, 137);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "成績統計";
            // 
            // chkCourseAvg
            // 
            this.chkCourseAvg.AutoSize = true;
            this.chkCourseAvg.Location = new System.Drawing.Point(15, 104);
            this.chkCourseAvg.Name = "chkCourseAvg";
            this.chkCourseAvg.Size = new System.Drawing.Size(91, 20);
            this.chkCourseAvg.TabIndex = 3;
            this.chkCourseAvg.Text = "各科平均";
            this.chkCourseAvg.UseVisualStyleBackColor = true;
            // 
            // chkRank
            // 
            this.chkRank.AutoSize = true;
            this.chkRank.Location = new System.Drawing.Point(15, 78);
            this.chkRank.Name = "chkRank";
            this.chkRank.Size = new System.Drawing.Size(91, 20);
            this.chkRank.TabIndex = 2;
            this.chkRank.Text = "每人名次";
            this.chkRank.UseVisualStyleBackColor = true;
            // 
            // chkFailNum
            // 
            this.chkFailNum.AutoSize = true;
            this.chkFailNum.Location = new System.Drawing.Point(15, 52);
            this.chkFailNum.Name = "chkFailNum";
            this.chkFailNum.Size = new System.Drawing.Size(139, 20);
            this.chkFailNum.TabIndex = 1;
            this.chkFailNum.Text = "每人不及格科數";
            this.chkFailNum.UseVisualStyleBackColor = true;
            // 
            // chkAvg
            // 
            this.chkAvg.AutoSize = true;
            this.chkAvg.Location = new System.Drawing.Point(15, 26);
            this.chkAvg.Name = "chkAvg";
            this.chkAvg.Size = new System.Drawing.Size(91, 20);
            this.chkAvg.TabIndex = 0;
            this.chkAvg.Text = "每人平均";
            this.chkAvg.UseVisualStyleBackColor = true;
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(12, 12);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(414, 176);
            this.txtOutput.TabIndex = 6;
            this.txtOutput.WordWrap = false;
            // 
            // TwoDArray
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(607, 252);
            this.Controls.Add(this.btnSearch);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnCompute);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.txtOutput);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "TwoDArray";
            this.Text = "成績處理-二維陣列";
            this.Load += new System.EventHandler(this.TwoDArray_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnSearch;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnCompute;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox chkCourseAvg;
        private System.Windows.Forms.CheckBox chkRank;
        private System.Windows.Forms.CheckBox chkFailNum;
        private System.Windows.Forms.CheckBox chkAvg;
        private System.Windows.Forms.TextBox txtOutput;
    }
}