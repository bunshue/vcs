using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using hisonic.WinForm.HisonicControl;
using hisonic.WinForm.HisonicControl.CourseGrid;

namespace testcontrol
{
    /// <summary>
    /// Form1 的摘要說明。
    /// </summary>
    public class Form1 : System.Windows.Forms.Form
    {
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.ImageList imageList2;
        private System.ComponentModel.IContainer components;
        private System.Windows.Forms.DataGrid dataGrid1;
        private CourseTable courseTable;
        public string[] curr = new string[4];

        public Form1()
        {
            //
            // Windows 窗體設計器支持所必需的
            //
            InitializeComponent();

            //
            // TODO: 在 InitializeComponent 調用後添加任何構造函數代碼
            this.courseTable = new CourseTable(this.dataGrid1, 5, 1, 4, 3, 2);
            // 設置表頭
            this.courseTable.SetCaptionText("測試用課程表");
            // 設置列寬
            this.courseTable.SetColumnWidth(80);
            // 設置課程
            this.courseTable.SetCellData(3, 1, new object(), "語文");
            this.courseTable.SetCellData(3, 0, new object(), "化學");
            this.courseTable.SetCellData(5, 6, new object(), "物理");
            this.courseTable.SetCellData(2, 5, new object(), "數學");
        }

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }

        #region Windows 窗體設計器生成的代碼
        /// <summary>
        /// 設計器支持所需的方法 - 不要使用代碼編輯器修改
        /// 此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.imageList2 = new System.Windows.Forms.ImageList(this.components);
            this.dataGrid1 = new System.Windows.Forms.DataGrid();
            ((System.ComponentModel.ISupportInitialize)(this.dataGrid1)).BeginInit();
            this.SuspendLayout();
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Black;
            this.imageList1.Images.SetKeyName(0, "");
            this.imageList1.Images.SetKeyName(1, "");
            this.imageList1.Images.SetKeyName(2, "");
            // 
            // imageList2
            // 
            this.imageList2.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList2.ImageStream")));
            this.imageList2.TransparentColor = System.Drawing.Color.Black;
            this.imageList2.Images.SetKeyName(0, "");
            this.imageList2.Images.SetKeyName(1, "");
            this.imageList2.Images.SetKeyName(2, "");
            // 
            // dataGrid1
            // 
            this.dataGrid1.DataMember = "";
            this.dataGrid1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGrid1.HeaderForeColor = System.Drawing.SystemColors.ControlText;
            this.dataGrid1.Location = new System.Drawing.Point(0, 0);
            this.dataGrid1.Name = "dataGrid1";
            this.dataGrid1.Size = new System.Drawing.Size(637, 384);
            this.dataGrid1.TabIndex = 15;
            // 
            // Form1
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.ClientSize = new System.Drawing.Size(637, 384);
            this.Controls.Add(this.dataGrid1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGrid1)).EndInit();
            this.ResumeLayout(false);

        }
        #endregion

        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.Run(new Form1());
        }

        private void Form1_Load(object sender, System.EventArgs e)
        {
            curr[0] = "語文";
            curr[1] = "數學";
            curr[2] = "化學";
            curr[3] = "物理";
        }

    }
}
