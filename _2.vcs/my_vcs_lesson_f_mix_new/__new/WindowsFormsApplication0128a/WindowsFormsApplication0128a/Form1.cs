using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//進度條的創建與使用

namespace WindowsFormsApplication0128a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ShowLoading("正在搜索..."); 

        }

        private void button2_Click(object sender, EventArgs e)
        {
            RemoveLoading();

        }

        #region 數據加載進度條
        /// <summary>  
        /// 顯示頁面正在加載中效果  
        /// </summary>  
        public void ShowLoading(string msg)
        {
            StringBuilder s = new StringBuilder();
            s.Append(" <script language=JavaScript type=text/javascript>\n");
            s.Append(" var t_id = setInterval(animate,20);\n");
            s.Append(" var pos=0;var dir=2;var len=0;\n");
            s.Append(" function animate(){\n");
            s.Append(" var elem = document.getElementById('progress');\n");
            s.Append(" if(elem != null) {\n");
            s.Append(" if (pos==0) len += dir;\n");
            s.Append(" if (len>32 || pos>79) pos += dir;\n");
            s.Append(" if (pos>79) len -= dir;\n");
            s.Append(" if (pos>79 && len==0) pos=0;\n");
            s.Append(" elem.style.left = pos;\n");
            s.Append(" elem.style.width = len;\n");
            s.Append(" }}\n");
            s.Append(" function removeLoadMsg() {\n");
            s.Append(" this.clearInterval(t_id);\n");
            s.Append(" var targelem = document.getElementById('loader_container');\n");
            s.Append(" targelem.style.display='none';\n");
            s.Append(" targelem.style.visibility='hidden';\n");
            s.Append(" }\n ");
            s.Append("</script>\n");
            s.Append("<style>");
            s.Append("#loader_container {text-align:center; position:absolute; top:40%; width:100%; left: 0;}\n");
            s.Append("#loader {font-family:Tahoma, Helvetica, sans; font-size:11.5px; color:#000000; background-color:#FFFFFF; padding:10px 0 16px 0; margin:0 auto; display:block; width:130px; border:1px solid #5a667b; text-align:left; z-index:9999;}\n");
            s.Append("#progress {height:5px; font-size:1px; width:1px; position:relative; top:1px; left:0px; background-color:#8894a8;}\n");
            s.Append("#loader_bg {background-color:#e4e7eb; position:relative; top:8px; left:8px; height:7px; width:113px; font-size:1px;}\n");
            s.Append("</style>\n");
            s.Append("<div id=loader_container>\n");
            s.Append("<div id=loader>\n");
            s.Append("<div align=center>" + msg + "</div>\n");
            s.Append("<div id=loader_bg><div id=progress> </div></div>\n");
            s.Append("</div></div>\n ");
            //HttpContext.Current.Response.Write(s.ToString()); 
            //HttpContext.Current.Response.Flush(); 

            richTextBox1.Text += s.ToString();
        }


        public void RemoveLoading()
        {
            //ClientScript.RegisterClientScriptBlock(typeof(string), "", "<script>removeLoadMsg();</script>");
        }
        #endregion

    }
}

