using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using dotnetCHARTING;

//需要 改成 .Net Framework 4
//需要 參考/加入參考/.NET/System.Web


namespace vcs_DotNetCharting
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //调用说明及范例#region 调用说明及范例  
            //在要显示统计图的页面代码直接调用，方法类似如下：  


            DataTable dt = new DataTable();
            dt.Columns.Add("月份");
            dt.Columns.Add("金額");

            dt.Rows.Add("1", "123");
            dt.Rows.Add("2", "456");
            dt.Rows.Add("3", "333");

            ShowData show = new ShowData();
            show.Title = "2008年各月消费情况统计";
            show.XTitle = "月份";
            show.YTitle = "金額(万元)";
            show.PicHight = 300;
            show.PicWidth = 600;
            show.SeriesName = "具体详情";
            show.PhaysicalImagePath = "ChartImages";
            show.DataSource = dt;
            //show.CreateColumn(this.Chart1);


        }
    }

    /// <summary>      
    /// 彭建军  
    /// 根据数据动态生成图形（柱形图、饼图、曲线图）  
    /// 2008-06-19  
    /// </summary>  
    public class ShowData
    {
        #region 属性
        private string _phaysicalimagepath;//图片存放路径  
        private string _title; //图片标题  
        private string _xtitle;//图片x座标名称  
        private string _ytitle;//图片y座标名称  
        private string _seriesname;//图例名称  
        private int _picwidth;//图片宽度  
        private int _pichight;//图片高度  
        private DataTable _dt;//图片数据源  

        /// <summary>  
        /// 图片存放路径  
        /// </summary>  
        public string PhaysicalImagePath
        {
            set { _phaysicalimagepath = value; }
            get { return _phaysicalimagepath; }
        }
        /// <summary>  
        /// 图片标题  
        /// </summary>  
        public string Title
        {
            set { _title = value; }
            get { return _title; }
        }
        /// <summary>  
        /// 图片标题  
        /// </summary>  
        public string XTitle
        {
            set { _xtitle = value; }
            get { return _xtitle; }
        }
        /// <summary>  
        /// 图片标题  
        /// </summary>  
        public string YTitle
        {
            set { _ytitle = value; }
            get { return _ytitle; }
        }

        /// <summary>  
        /// 图例名称  
        /// </summary>  
        public string SeriesName
        {
            set { _seriesname = value; }
            get { return _seriesname; }
        }
        /// <summary>  
        /// 图片宽度  
        /// </summary>  
        public int PicWidth
        {
            set { _picwidth = value; }
            get { return _picwidth; }
        }
        /// <summary>  
        /// 图片高度  
        /// </summary>  
        public int PicHight
        {
            set { _pichight = value; }
            get { return _pichight; }
        }
        /// <summary>  
        /// 图片数据源  
        /// </summary>  
        public DataTable DataSource
        {
            set { _dt = value; }
            get { return _dt; }
        }
        #endregion

        #region 构造函数
        public ShowData()
        {
            //  
            // TODO: 在此处添加构造函数逻辑  
            //  
        }

        public ShowData(string PhaysicalImagePath, string Title, string XTitle, string YTitle, string SeriesName)
        {
            _phaysicalimagepath = PhaysicalImagePath;
            _title = Title;
            _xtitle = XTitle;
            _ytitle = YTitle;
            _seriesname = SeriesName;
        }
        #endregion

        #region 输出柱形图
        /// <summary>  
        /// 柱形图  
        /// </summary>  
        /// <returns></returns>  
        public void CreateColumn(dotnetCHARTING.Chart chart)
        {
            chart.Title = this._title;
            chart.XAxis.Label.Text = this._xtitle;
            chart.YAxis.Label.Text = this._ytitle;
            chart.TempDirectory = this._phaysicalimagepath;
            chart.Width = this._picwidth;
            chart.Height = this._pichight;
            chart.Type = ChartType.Combo;
            chart.Series.Type = SeriesType.Cylinder;
            chart.Series.Name = this._seriesname;
            chart.Series.Data = this._dt;
            chart.SeriesCollection.Add();
            chart.DefaultSeries.DefaultElement.ShowValue = true;
            chart.ShadingEffect = true;
            chart.Use3D = false;
            chart.Series.DefaultElement.ShowValue = true;
        }
        #endregion

        #region 输出饼图
        /// <summary>  
        /// 饼图  
        /// </summary>  
        /// <returns></returns>  
        public void CreatePie(dotnetCHARTING.Chart chart)
        {
            chart.Title = this._title;
            chart.TempDirectory = this._phaysicalimagepath;
            chart.Width = this._picwidth;
            chart.Height = this._pichight;
            chart.Type = ChartType.Pie;
            chart.Series.Type = SeriesType.Cylinder;
            chart.Series.Name = this._seriesname;

            chart.ShadingEffect = true;
            chart.Use3D = false;
            chart.DefaultSeries.DefaultElement.Transparency = 20;
            chart.DefaultSeries.DefaultElement.ShowValue = true;
            chart.PieLabelMode = PieLabelMode.Outside;
            chart.SeriesCollection.Add(getArrayData());
            chart.Series.DefaultElement.ShowValue = true;
        }

        private SeriesCollection getArrayData()
        {
            SeriesCollection SC = new SeriesCollection();
            DataTable dt = this._dt;

            for (int i = 0; i < dt.Rows.Count; i++)
            {
                Series s = new Series();
                s.Name = dt.Rows[i][0].ToString();

                Element e = new Element();

                // 每元素的名称  
                e.Name = dt.Rows[i][0].ToString();

                // 每元素的大小数值  
                e.YValue = Convert.ToInt32(dt.Rows[i][1].ToString());

                s.Elements.Add(e);
                SC.Add(s);
            }
            return SC;
        }
        #endregion

        #region 输出曲线图
        /// <summary>  
        /// 曲线图  
        /// </summary>  
        /// <returns></returns>  
        public void CreateLine(dotnetCHARTING.Chart chart)
        {
            chart.Title = this._title;
            chart.XAxis.Label.Text = this._xtitle;
            chart.YAxis.Label.Text = this._ytitle;
            chart.TempDirectory = this._phaysicalimagepath;
            chart.Width = this._picwidth;
            chart.Height = this._pichight;
            chart.Type = ChartType.Combo;
            chart.Series.Type = SeriesType.Line;
            chart.Series.Name = this._seriesname;
            chart.Series.Data = this._dt;
            chart.SeriesCollection.Add();
            chart.DefaultSeries.DefaultElement.ShowValue = true;
            chart.ShadingEffect = true;
            chart.Use3D = false;
            chart.Series.DefaultElement.ShowValue = true;
        }
        #endregion

    }
}

