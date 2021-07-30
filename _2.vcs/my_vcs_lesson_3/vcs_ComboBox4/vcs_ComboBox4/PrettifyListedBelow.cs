using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ComboBox4
{
    public partial class PrettifyListedBelow : Form
    {
        public PrettifyListedBelow()
        {
            InitializeComponent();
        }

        private void PrettifyListedBelow_Load(object sender,EventArgs e)
        {
            beautyComboBox.Items.Add("白菜");//向ComboBox中添加「白菜」字段
            beautyComboBox.Items.Add("蘿蔔");//向ComboBox中添加「蘿蔔」字段
            beautyComboBox.Items.Add("土豆");//向ComboBox中添加「土豆」字段
            beautyComboBox.Items.Add("洋蔥");//向ComboBox中添加「洋蔥」字段
            beautyComboBox.Items.Add("南瓜");//向ComboBox中添加「南瓜」字段
            beautyComboBox.SelectedIndex = 0;//設置ComboBox控件默認選中第一項
        }

        private void beautyComboBox_DrawItem(object sender,DrawItemEventArgs e)
        {
            Graphics gComboBox = e.Graphics;//聲明一個GDI+繪圖圖面類的對象
            Rectangle rComboBox = e.Bounds;//聲明一個表示矩形的位置和大小類的對象
            Size imageSize = imageList1.ImageSize;//聲明一個有序整數對的對象
            FontDialog typeFace = new FontDialog();//定義一個字體類對像
            Font Style = typeFace.Font;//定義一個定義特定的文本格式類對像
            if (e.Index >= 0)//當繪製的索引項存在時
            {
                string temp = (string)beautyComboBox.Items[e.Index];//獲取ComboBox控件索引項下的文本內容
                StringFormat stringFormat = new StringFormat();//定義一個封裝文本佈局信息類的對象
                stringFormat.Alignment = StringAlignment.Near;//設定文本的佈局方式
                if (e.State == (DrawItemState.NoAccelerator | DrawItemState.NoFocusRect))//當繪製項沒有鍵盤加速鍵和焦點可視化提示時
                {
                    e.Graphics.FillRectangle(new SolidBrush(Color.Red), rComboBox);//用指定的顏色填充自定義矩形的內部
                    imageList1.Draw(e.Graphics, rComboBox.Left, rComboBox.Top, e.Index);//在指定位置繪製指定索引的圖片
                    e.Graphics.DrawString(temp, Style, new SolidBrush(Color.Black), rComboBox.Left + imageSize.Width, rComboBox.Top);//在指定的位置並且用指定的Font對像繪製指定的文本字符串
                    e.DrawFocusRectangle();//在指定的邊界範圍內繪製聚焦框
                }
                else //當繪製項有鍵盤加速鍵或者焦點可視化提示時
                {
                    e.Graphics.FillRectangle(new SolidBrush(Color.LightBlue), rComboBox);//用指定的顏色填充自定義矩形的內部
                    imageList1.Draw(e.Graphics, rComboBox.Left, rComboBox.Top, e.Index);//在指定位置繪製指定索引的圖片
                    e.Graphics.DrawString(temp, Style, new SolidBrush(Color.Black), rComboBox.Left + imageSize.Width, rComboBox.Top);//在指定的位置並且用指定的Font對像繪製指定的文本字符串
                    e.DrawFocusRectangle();//在指定的邊界範圍內繪製聚焦框
                }
            }
        }
    }
}
