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
    /// Form1 ���K�n�����C
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
            // Windows ����]�p������ҥ��ݪ�
            //
            InitializeComponent();

            //
            // TODO: �b InitializeComponent �եΫ�K�[����c�y��ƥN�X
            this.courseTable = new CourseTable(this.dataGrid1, 5, 1, 4, 3, 2);
            // �]�m���Y
            this.courseTable.SetCaptionText("���եνҵ{��");
            // �]�m�C�e
            this.courseTable.SetColumnWidth(80);
            // �]�m�ҵ{
            this.courseTable.SetCellData(3, 1, new object(), "�y��");
            this.courseTable.SetCellData(3, 0, new object(), "�ƾ�");
            this.courseTable.SetCellData(5, 6, new object(), "���z");
            this.courseTable.SetCellData(2, 5, new object(), "�ƾ�");
        }

        /// <summary>
        /// �M�z�Ҧ����b�ϥΪ��귽�C
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

        #region Windows ����]�p���ͦ����N�X
        /// <summary>
        /// �]�p������һݪ���k - ���n�ϥΥN�X�s�边�ק�
        /// ����k�����e�C
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
        /// ���ε{�����D�n�i�J�I�C
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.Run(new Form1());
        }

        private void Form1_Load(object sender, System.EventArgs e)
        {
            curr[0] = "�y��";
            curr[1] = "�ƾ�";
            curr[2] = "�ƾ�";
            curr[3] = "���z";
        }

    }
}
