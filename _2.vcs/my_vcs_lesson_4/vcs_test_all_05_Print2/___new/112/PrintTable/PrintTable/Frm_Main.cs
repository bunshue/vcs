using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PrintTable
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void txtGMoney_TextChanged(object sender, EventArgs e)
        {
        }

        private void txtGNum_TextChanged(object sender, EventArgs e)
        {
        }

        private void dgvInfo_CellClick(object sender, DataGridViewCellEventArgs e)
        {
        }

        //打印
        private void btnPrint_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.ShowDialog();
        }

        //设置打印的商品入库单据
        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            string strID = "A123456";  // 單據號
            string strInPeople = "david";  // 入庫人
            string strInProvider = "IMS";  // 供應商
            string strPlace = "Hsinchu";  // 產地
            string strGID = "P0123";  // 商品編號
            string strGName = "IMS EGD";  // 名稱
            string strGSpec = "XL";  // 規格
            string strGUnit = "PCS";  // 單位
            string strGMoney = "1234";  // 單價
            string strGNum = "12";  // 數量
            string strSMoney = "23456";  // 金額
            string strInDate = "2026/05/01";  // 入庫日期
            string strRemark = "請盡速安排出貨";  // 備註


            int printWidth = e.PageBounds.Width;//页面宽度
            int printHeight = e.PageBounds.Height;//页面高度
            int left = printWidth / 2 - 305;
            int right = printWidth / 2 + 305;
            int top = printHeight / 2 - 200;
            Brush myBrush = new SolidBrush(Color.Black);//创建Brush对象
            Pen mypen = new Pen(Color.Black);//创建Pen对象
            Font myFont = new Font("宋体", 12);//创建Font对象
            //绘制标题
            e.Graphics.DrawString("商品入库单", new Font("宋体", 20, FontStyle.Bold), myBrush, new Point(printWidth / 2 - 100, top));
            e.Graphics.DrawLine(new Pen(Color.Black, 2), 300, top + 30, 480, top + 30);//绘制线条
            e.Graphics.DrawLine(new Pen(Color.Black, 2), 300, top + 34, 480, top + 34);//绘制线条
            e.Graphics.DrawString("吉林省明日科技有限公司", new Font("宋体", 9), myBrush, new Point(left + 2, top + 25));
            e.Graphics.DrawString("日期：" + DateTime.Now.ToLongDateString(), new Font("宋体", 12), myBrush, new Point(right - 190, top + 25));
            e.Graphics.DrawRectangle(mypen, left, top + 42, 610, 230);//绘制矩形框
            e.Graphics.DrawLine(mypen, left, top + 72, left + 610, top + 72);//绘制第一行网格线
            e.Graphics.DrawLine(mypen, left, top + 102, left + 610, top + 102);//绘制第二行网格线
            e.Graphics.DrawLine(mypen, left, top + 132, left + 610, top + 132);//绘制第三行网格线
            e.Graphics.DrawLine(mypen, left, top + 162, left + 610, top + 162);//绘制第四行网格线
            e.Graphics.DrawLine(mypen, left + 80, top + 42, left + 80, top + 272);//绘制第一列网格线
            e.Graphics.DrawLine(mypen, left + 220, top + 42, left + 220, top + 72);//绘制第二列网格线
            e.Graphics.DrawLine(mypen, left + 280, top + 42, left + 280, top + 72);//绘制第三列网格线
            e.Graphics.DrawLine(mypen, left + 410, top + 42, left + 410, top + 132);//绘制第四列网格线
            e.Graphics.DrawLine(mypen, left + 470, top + 42, left + 470, top + 162);//绘制第五列网格线
            e.Graphics.DrawLine(mypen, left + 170, top + 102, left + 170, top + 162);//绘制第三行第二列网格线
            e.Graphics.DrawLine(mypen, left + 220, top + 102, left + 220, top + 162);//绘制第三行第三列网格线
            e.Graphics.DrawLine(mypen, left + 300, top + 132, left + 300, top + 162);//绘制第四行第四列网格线
            e.Graphics.DrawLine(mypen, left + 360, top + 132, left + 360, top + 162);//绘制第四行第五列网格线
            e.Graphics.DrawLine(mypen, left + 520, top + 132, left + 520, top + 162);//绘制第四行第七列网格线
            //绘制第一行数据
            e.Graphics.DrawString("入库日期", myFont, myBrush, new Point(left + 2, top + 50));
            e.Graphics.DrawString(strInDate, myFont, myBrush, new Point(left + 82, top + 50));
            e.Graphics.DrawString("单据号", myFont, myBrush, new Point(left + 222, top + 50));
            e.Graphics.DrawString(strID, myFont, myBrush, new Point(left + 282, top + 50));
            e.Graphics.DrawString("入库人", myFont, myBrush, new Point(left + 412, top + 50));
            e.Graphics.DrawString(strInPeople, myFont, myBrush, new Point(left + 472, top + 50));
            //绘制绘制第二行数据
            e.Graphics.DrawString("供货商", myFont, myBrush, new Point(left + 2, top + 80));
            e.Graphics.DrawString(strInProvider, myFont, myBrush, new Point(left + 82, top + 80));
            e.Graphics.DrawString("产地", myFont, myBrush, new Point(left + 412, top + 80));
            e.Graphics.DrawString(strPlace, myFont, myBrush, new Point(left + 472, top + 80));
            //第三行数据
            e.Graphics.DrawString("商品编号", myFont, myBrush, new Point(left + 2, top + 110));
            e.Graphics.DrawString(strGID, myFont, myBrush, new Point(left + 82, top + 110));
            e.Graphics.DrawString("名称", myFont, myBrush, new Point(left + 172, top + 110));
            e.Graphics.DrawString(strGName, myFont, myBrush, new Point(left + 222, top + 110));
            e.Graphics.DrawString("规格", myFont, myBrush, new Point(left + 412, top + 110));
            e.Graphics.DrawString(strGSpec, myFont, myBrush, new Point(left + 472, top + 110));
            //绘制第四行数据
            e.Graphics.DrawString("单位", myFont, myBrush, new Point(left + 2, top + 140));
            e.Graphics.DrawString(strGUnit, myFont, myBrush, new Point(left + 82, top + 140));
            e.Graphics.DrawString("单价", myFont, myBrush, new Point(left + 172, top + 140));
            e.Graphics.DrawString(strGMoney, myFont, myBrush, new Point(left + 222, top + 140));
            e.Graphics.DrawString("数量", myFont, myBrush, new Point(left + 302, top + 140));
            e.Graphics.DrawString(strGNum, myFont, myBrush, new Point(left + 362, top + 140));
            e.Graphics.DrawString("金额", myFont, myBrush, new Point(left + 472, top + 140));
            e.Graphics.DrawString(strSMoney, myFont, myBrush, new Point(left + 522, top + 140));
            //绘制第五行数据
            e.Graphics.DrawString("备注", myFont, myBrush, new Point(left + 2, top + 170));
            e.Graphics.DrawString(strRemark, myFont, myBrush, new Point(left + 82, top + 170));
        }
    }
}
