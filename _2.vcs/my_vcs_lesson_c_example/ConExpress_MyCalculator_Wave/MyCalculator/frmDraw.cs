﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Drawing.Design;

namespace ConExpress.Calculator
{
    public partial class frmDraw : Form
    {
        private SyntaxAnalyse m_Analyse = new SyntaxAnalyse();
        private List<DrawInfo> m_DrawInfoList = new List<DrawInfo>();

        public frmDraw()
        {
            InitializeComponent();
        }

        private void frmDraw_Load(object sender, EventArgs e)
        {
            this.bdsDrawInfo.DataSource = m_DrawInfoList;
        }

        private void Draw(Bitmap myImage)
        {
            try
            {
                Graphics g = Graphics.FromImage(myImage);

                SyntaxAnalyse.DicVariable.Clear();
                int intMin = this.numMin.Value < this.numMax.Value ? (int)this.numMin.Value : (int)this.numMax.Value;
                int intMax = this.numMin.Value < this.numMax.Value ? (int)this.numMax.Value : (int)this.numMin.Value;

                TokenRecord TokenN = m_Analyse.Analyse("n");
                TokenN.TokenValueType = typeof(double);
                TokenN.TokenValue = intMin;

                //初始化
                foreach (DrawInfo item in this.m_DrawInfoList)
                {
                    item.InitialToken(m_Analyse);
                }


                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                //繪制X軸和Y軸
                g.DrawLine(Pens.Black, 0, this.picImage.Height / 2, this.picImage.Width, this.picImage.Height / 2);
                g.DrawLine(Pens.Black, this.picImage.Width / 2, 0, this.picImage.Width / 2, this.picImage.Height);
                g.TranslateTransform(Convert.ToSingle(myImage.Width / 2), Convert.ToSingle(myImage.Height / 2));


                //計算表達式
                for (int intIndex = intMin; intIndex <= intMax; intIndex++)
                {
                    TokenN.TokenValue = (double)intIndex;
                    foreach (DrawInfo item in this.m_DrawInfoList)
                    {
                        item.Execute();
                    }
                }

                //繪制圖像
                foreach (DrawInfo item in this.m_DrawInfoList)
                {
                    g.DrawLines(new Pen(item.LineColor, item.LineWidth), item.PointList.ToArray());
                }
                myImage.RotateFlip(RotateFlipType.Rotate180FlipX);

                //繪制刻度
                SolidBrush myBrush = new SolidBrush(Color.Black);
                for (int intX = 0; intX < myImage.Width / 2; intX += (int)(this.numScale.Value))
                {
                    g.DrawLine(Pens.Black, intX, 0, intX, -3);
                    g.DrawString(intX.ToString(), this.Font, myBrush, intX + 1, 1);
                    if (intX == 0)
                        continue;
                    g.DrawLine(Pens.Black, -intX, 0, -intX, -3);
                    g.DrawString("-" + intX.ToString(), this.Font, myBrush, -intX + 1, 1);
                }

                for (int intY = 0; intY < myImage.Height / 2; intY += (int)this.numScale.Value)
                {
                    g.DrawLine(Pens.Black, 0, -intY, 3, -intY);
                    g.DrawString(intY.ToString(), this.Font, myBrush, 1, -intY + 1);
                    if (intY == 0)
                        continue;
                    g.DrawLine(Pens.Black, 0, intY, 3, intY);
                    g.DrawString("-" + intY.ToString(), this.Font, myBrush, 1, intY + 1);
                }
                //TODO:繪制網格

                //繪制圖示Legend
                g.TranslateTransform(Convert.ToSingle(myImage.Width / 2 * -1), Convert.ToSingle(myImage.Height / 2 * -1));
                int intOffsetX = 10;
                int intOffsetY = 10;
                int intLegendHeight = (int)g.MeasureString("123", this.Font).Height;
                foreach (DrawInfo item in m_DrawInfoList)
                {
                    using (SolidBrush LegendBrush = new SolidBrush(item.LineColor))
                    {
                        g.FillRectangle(LegendBrush, intOffsetX, intOffsetY, 30, intLegendHeight);
                        g.DrawString(item.Name, this.Font, LegendBrush, intOffsetX + 30 + 5, intOffsetY);
                        intOffsetY += intLegendHeight + 5;
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("錯誤信息為：" + ex.Message, "運算發生錯誤", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        #region 工具欄操作

        private void btnDraw_Click(object sender, EventArgs e)
        {
            Bitmap myImage = new Bitmap(this.picImage.Width, this.picImage.Height);
            this.Draw(myImage);
            this.picImage.Image = myImage;

            this.btnSave.Enabled = (this.picImage.Image != null);
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            if (this.dlgSaveImage.ShowDialog() == DialogResult.OK)
            {
                string strFileName = this.dlgSaveImage.FileName;
                string strExtension = Path.GetExtension(strFileName).ToLower();
                Bitmap myImage = (Bitmap)this.picImage.Image;

                switch (strExtension)
                {
                    case ".png":
                        myImage.Save(strFileName, System.Drawing.Imaging.ImageFormat.Png);
                        break;
                    case ".jpg":
                        myImage.Save(strFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
                        break;
                    case ".gif":
                        myImage.Save(strFileName, System.Drawing.Imaging.ImageFormat.Gif);
                        break;
                    case ".bmp":
                        myImage.Save(strFileName, System.Drawing.Imaging.ImageFormat.Bmp);
                        break;
                    default:
                        break;
                }
            }
        }

        private void btnShowProperty_Click(object sender, EventArgs e)
        {
            this.splitContainer1.Panel2Collapsed = !this.btnShowProperty.Checked;
        }

        #endregion 工具欄操作


        private void btnAdd_Click(object sender, EventArgs e)
        {
            object NewItem = this.bdsDrawInfo.AddNew();
            this.lstDrawInfo.SelectedIndex = this.bdsDrawInfo.Count - 1;
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            for (int index = this.lstDrawInfo.SelectedItems.Count - 1; index >= 0; index--)
            {
                this.bdsDrawInfo.Remove(this.lstDrawInfo.SelectedItems[index]);
            }
        }

        private void lstDrawInfo_SelectedIndexChanged(object sender, EventArgs e)
        {
            List<object> myList = new List<object>();
            foreach (object item in this.lstDrawInfo.SelectedItems)
                myList.Add(item);
            this.propertyGrid1.SelectedObjects = myList.ToArray();
        }

    }//class frmDraw


    /// <summary>
    /// 繪圖信息
    /// </summary>
    public class DrawInfo
    {
        #region 字段和屬性聲明

        private const string CategoryName = "繪圖信息";

        private string m_Name = "未命名項";
        [Category(CategoryName), DisplayName("名稱"), DefaultValue("未命名項"), MergableProperty(false), Description("繪圖信息的名稱。")]
        public string Name
        {
            get { return m_Name; }
            set
            {
                if (m_Name != value && value.Trim().Length > 0)
                    m_Name = value;
            }
        }

        private Color m_LineColor = Color.Black;
        [Category(CategoryName), DisplayName("線條顏色"), DefaultValue(typeof(Color), "Black"), Description("繪制線條的顏色。")]
        public Color LineColor
        {
            get { return m_LineColor; }
            set { m_LineColor = value; }
        }

        private float m_LineWidth = 1.0f;
        [Category(CategoryName), DisplayName("線條寬度"), DefaultValue(1.0f), Description("繪制線條的寬度(以像素為單位)。")]
        public float LineWidth
        {
            get { return m_LineWidth; }
            set { m_LineWidth = value; }
        }

        private string m_ExpressionX = "n";
        [Category(CategoryName), DisplayName("表達式X"), DefaultValue("n"), Description("對應坐標軸X的表達式。")]
        [Editor("System.ComponentModel.Design.MultilineStringEditor, System.Design, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a", typeof(UITypeEditor))]
        public string ExpressionX
        {
            get { return m_ExpressionX; }
            set
            {
                if (m_ExpressionX != value && value.Trim().Length > 0)
                    m_ExpressionX = value.Trim();
            }
        }

        private string m_ExpressionY = "n";
        [Category(CategoryName), DisplayName("表達式Y"), DefaultValue("n"), Description("對應坐標軸Y的表達式。")]
        [Editor("System.ComponentModel.Design.MultilineStringEditor, System.Design, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a", typeof(UITypeEditor))]
        public string ExpressionY
        {
            get { return m_ExpressionY; }
            set
            {
                if (m_ExpressionY != value && value.Trim().Length > 0)
                    m_ExpressionY = value.Trim();
            }
        }

        private List<PointF> m_PointList = new List<PointF>();
        /// <summary>
        /// 坐標列表
        /// </summary>
        [Browsable(false)]
        public List<PointF> PointList
        {
            get { return m_PointList; }
        }

        #endregion 字段和屬性聲明

        /// <summary>
        /// 構造函數
        /// </summary>
        public DrawInfo()
        { }


        private TokenRecord m_TokenX;
        private TokenRecord m_TokenY;
        /// <summary>
        /// 初始化記號對象
        /// </summary>
        /// <param name="Analyser">表達式分析計算類的實例</param>
        public void InitialToken(SyntaxAnalyse Analyser)
        {
            if (Analyser != null)
            {
                m_TokenX = Analyser.Analyse(m_ExpressionX.ToLower());
                m_TokenY = Analyser.Analyse(m_ExpressionY.ToLower());
                this.m_PointList.Clear();
            }
        }

        /// <summary>
        /// 執行計算
        /// </summary>
        public void Execute()
        {
            m_TokenX.Execute();
            m_TokenY.Execute();
            m_PointList.Add(new PointF(Convert.ToSingle(m_TokenX.TokenValue), Convert.ToSingle(m_TokenY.TokenValue)));
        }

        public override string ToString()
        {
            return m_Name;
        }

    }//class DrawInfo



}//namespace