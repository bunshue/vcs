//原文連結：http://www.gamedev.net/reference/articles/article2003.asp
//原作者文章連結：http://www.policyalmanac.org/games/aStarTutorial.htm
//http://swf.com.tw/?p=67

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;  // Thread.Sleep(100);

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        short D = 10; // 方塊的半徑
        short w = 4, h = 4; // 方塊的個數 (寬 高)
        List<G2D_Cell> cList = new List<G2D_Cell>(); // 全部小方塊 的清單
        short Start = -1; // 開始點 的編號
        short Target = -1; // 目標點 的編號
        List<short> wallList = new List<short>(); // 牆壁點 的清單
        List<short> openList = new List<short>(); // 開放點的清單 (候選清單)
        List<short> closedList = new List<short>(); // 關閉點的清單 (評估完的清單)

        List<short> pathList = new List<short>(); // 路徑解答 
        short NeighborStep = 2; // 預設是 不允許斜行，( = 1 允許斜行)

        bool displayOpenList = false; // 要不要 顯示 openList 和 closedList
        Graphics graphic; // 這是 用來在 慢慢搜尋 時逐步 顯示 openList 和 closedList

        G2D_DraggingRect startRect, targetRect; // 拖曳用的 開始點和目標點 
        bool startRectDragging = false;  // 是否正在 拖曳 開始點  
        bool targetRectDragging = false; // 是否正在 拖曳 目標點 
        int dx, dy; // 拖曳中 開始點或目標點 的游標偏移值

        public Form1()
        {
            InitializeComponent();

            int Cx = 2 * D, Cy = 2 * D; // 起始的座標

            //Size screenSize = SystemInformation.PrimaryMonitorMaximizedWindowSize; // 取得主顯示器上最大化視窗的預設大小
            //Size screenSize = SystemInformation.PrimaryMonitorSize; // 取得主顯示器上目前的視訊模式大小
            
            Rectangle screenRect = SystemInformation.WorkingArea;  // 取得螢幕的工作區域大小
            Size screenSize = new Size(screenRect.Width, screenRect.Height);

            screenSize.Width = screenSize.Width - panel1.Width; // 可顯示方塊的作業寬高
            screenSize.Height = screenSize.Height - SystemInformation.CaptionHeight; // 取得視窗標準標題列區域的高度
            w = (short)(screenSize.Width / (2*D) - 1);   // 寬有幾個方塊
            h = (short)(screenSize.Height / (2*D) - 1);  // 高有幾個方塊

            G2D_Cell c;
            short no = 0;  // 方塊編號
            for (short j = 0; j < h; j++)  // 由上往下
                for (short i = 0; i < w; i++) // 由左往右
                {
                    c = new G2D_Cell(new Point(Cx + i * 2*D, Cy + j * 2*D), D, no);

                    // 鄰居方塊 的編號 (位於邊邊的方塊 可能會沒有 鄰居方塊)
                    if (j == 0) c.Neighbor[0] = -1; 
                    else c.Neighbor[0] = (short)(no - w); // 上

                    if (j == 0 || i == w-1) c.Neighbor[1] = -1;
                    else c.Neighbor[1] = (short)(no - w + 1); // 上 右

                    if (i == w - 1) c.Neighbor[2] = -1;
                    else c.Neighbor[2] = (short)(no + 1); // 右

                    if (i == w - 1 || j == h-1) c.Neighbor[3] = -1;
                    else c.Neighbor[3] = (short)(no + w + 1); // 右 下

                    if (j == h - 1) c.Neighbor[4] = -1;
                    else c.Neighbor[4] = (short)(no + w); // 下

                    if (j == h - 1 || i == 0) c.Neighbor[5] = -1;
                    else c.Neighbor[5] = (short)(no + w - 1); // 下 左

                    if (i == 0) c.Neighbor[6] = -1;
                    else c.Neighbor[6] = (short)(no - 1); // 右

                    if (i == 0 || j == 0) c.Neighbor[7] = -1;
                    else c.Neighbor[7] = (short)(no - w - 1); // 右 上

                    // 本方塊在大地圖的行列位置 (這是用來計算 本方塊到 目標點 的 成本)
                    c.row = i;    // 行
                    c.column = j; // 列

                    c.no = no; // 本方塊 在 cList 清單 的編號
                    cList.Add(c); // 加入到清單中
                    no++;
                }

            label1.Text = w + " x " + h + " 個小方塊，編號 ( 0 ~ " + (w * h - 1) + " )";

            graphic = this.CreateGraphics();  //  for display openList and closedList

            startRect = new G2D_DraggingRect(cList[0].pos, Color.Blue, D);
            targetRect = new G2D_DraggingRect(cList[w * 4 + 4].pos, Color.Red, D);
            Start = 0;
            Target = (short)(w * 4 + 4); // 隨便定一個 Target
            cList[Start].start = true;
            cList[Target].target = true;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            listBox1.Items.Clear();

            for (int i = 0; i < cList.Count; i++)
            {
                cList[i].Draw(e.Graphics);
            }

            if (displayOpenList) // for 慢慢搜尋
            {
                for (int i = 0; i < openList.Count; i++)
                {
                    cList[openList[i]].DrawEllipse(e.Graphics, Brushes.Violet); // openList
                }
                listBox1.Items.Add("openList 的個數： " + openList.Count);

                for (int i = 0; i < closedList.Count; i++)
                {
                    cList[closedList[i]].DrawEllipse(e.Graphics, Brushes.Teal); // closedList
                }
                listBox1.Items.Add("closedList 的個數： " + closedList.Count);
            }

            startRect.Draw(e.Graphics);
            targetRect.Draw(e.Graphics);

            listBox1.Items.Add("開始點的編號: " + Start);
            listBox1.Items.Add("目標點的編號: " + Target);

            // 路徑解答
            for (int i = 0; i < pathList.Count; i++)
            {
                cList[pathList[i]].DrawEllipse(e.Graphics, Brushes.Lime);  // .Green
            }

            listBox1.Items.Add("pathList 的個數： " + pathList.Count);
        }

        // 開始 移動 開始點  或是
        // 開始 移動 目標點
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (startRect.GetRect().Contains(e.Location)) // 選到 開始點
            {
                startRectDragging = true;
                dx = e.X - startRect.pos.X;
                dy = e.Y - startRect.pos.Y;
            }
            else if (targetRect.GetRect().Contains(e.Location)) // 選到 目標點
            {
                targetRectDragging = true;
                dx = e.X - targetRect.pos.X;
                dy = e.Y - targetRect.pos.Y;
            }
            else  // 連續 加入 或 移除 牆壁點
            {
                WallAddRemove(e.Button, e.Location);
            }
        }

        // 移動 開始點  或是 移動 目標點
        // 滑鼠左鍵 連續加入牆壁點
        // 滑鼠右鍵 連續移除牆壁點
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (startRectDragging)
            {
                startRect.pos.X = e.X - dx;
                startRect.pos.Y = e.Y - dy;
                this.Invalidate();
            }
            else if (targetRectDragging)
            {
                targetRect.pos.X = e.X - dx;
                targetRect.pos.Y = e.Y - dy;
                this.Invalidate();
            }
            else  // 連續 加入 或 移除 牆壁點
            {
                WallAddRemove(e.Button, e.Location);
            }
        }

         // 連續 加入 或 移除 牆壁點
        void WallAddRemove(MouseButtons eButton, Point eLocation)
        {
            if (eButton == MouseButtons.Left) // 加入
            {
                for (short i = 0; i < cList.Count; i++)
                {
                    if (cList[i].isInRectangle(eLocation))
                    {
                        
                        if (cList[i].start == true) // 牆壁 不能在 開始點
                            break;
                        if (cList[i].target == true) // 牆壁 不能在 目標點
                            break;

                        int old = wallList.IndexOf(i);
                        if (old != -1) // 原來就已經是牆壁了
                            break;
                        else // 原來不是牆壁
                        {
                            cList[i].wall = true; // 就加入
                            wallList.Add(i);
                            this.Invalidate();
                            break;
                        }
                    }
                }
            }
            else if (eButton == MouseButtons.Right) // 移除
            {
                for (short i = 0; i < cList.Count; i++)
                {
                    if (cList[i].isInRectangle(eLocation))
                    {
                        int old = wallList.IndexOf(i);
                        if (old != -1) // 已經是牆壁了
                        {
                            cList[i].wall = false; // 就移除
                            wallList.RemoveAt(old);
                            this.Invalidate();
                            break;
                        }
                        else break; // 原來就不是牆壁
                    }
                }
            }
        }

        // 在 openList 找尋 有著最小成本 (F) 的 node
        private short Find_The_Smallest_F_in_OpenList()
        {
            if (openList.Count == 0) return -1; // openList 是空的

            int F = Int32.MaxValue;
            int n = -1; // 有最小 F 的 node 是在 openList 的第幾個
            for (int i = 0; i < openList.Count; i++)
            {
                if (cList[openList[i]].F() < F)
                {
                    F = cList[openList[i]].F();
                    n = i;
                }
            }

            short K = openList[n];
            openList.RemoveAt(n); // 將選到的 node 移出 openList
            closedList.Add(K);    // 將選到的 node 加入 closedList
            return K; 
        }

        // 立即搜尋
        private void button2_Click(object sender, EventArgs e)
        {
            displayOpenList = false;
            //Go();
            Thread t = new Thread(new ThreadStart(Go));  // 包一個 Thread 來執行 會穩一些
            t.Start();
        }

        // 允許斜行
        private void checkBox1_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked) NeighborStep = 1;  // 允許斜行
            else NeighborStep = 2; // 不允許斜行
        }

        // 清除路徑
        private void button1_Click(object sender, EventArgs e)
        {
            //listBox1.Items.Clear();

            pathList.Clear();
            openList.Clear();
            closedList.Clear();

            displayOpenList = false;
            this.Invalidate();
        }

        // 慢慢搜尋 列出 openList 和 closedList
        private void button3_Click(object sender, EventArgs e)
        {
            displayOpenList = true;
            //Go();

            Thread t = new Thread(new ThreadStart(Go));  // 包一個 Thread 來執行 會穩一些
            t.Start();
        }

        void Go()
        {
            if (Start == -1 || Target == -1) return;

            //listBox1.Items.Clear();
            pathList.Clear();
            openList.Clear();
            closedList.Clear();

            for (int i = 0; i < cList.Count; i++)
                cList[i].Parent = -1;

            cList[Start].G = 0;
            cList[Start].H = 0;
            openList.Add(Start);

            if (displayOpenList)  // 如果要呈現細節
                cList[Start].DrawEllipse(graphic, Brushes.Violet); //DrawOpen(graphic);   // ****************************

            bool keepSearching = true;
            bool reachTarget = false;
            short k; // the current node
            int G;
            while (keepSearching)
            {
                k = Find_The_Smallest_F_in_OpenList();
                //listBox1.Items.Add(k);

                if (k == -1) // no node in openList
                {
                    keepSearching = false;
                    break;
                }

                if (displayOpenList) // 如果要呈現細節
                    cList[k].DrawEllipse(graphic, Brushes.Teal); //.DrawClosed(graphic); // ****************************

                if (k == Target) // reach the Target
                {
                    reachTarget = true;
                    keepSearching = false;
                    break;
                }

                for (int i = 0; i < 8; i = i + NeighborStep)  // i = i + 2 不允許斜行， i = i + 1 允許斜行
                {
                    if (cList[k].Neighbor[i] == -1) continue;  // no this Neighbor
                    else if (wallList.IndexOf(cList[k].Neighbor[i]) != -1) continue; // this Neighbor is a wall
                    else if (closedList.IndexOf(cList[k].Neighbor[i]) != -1) continue; // this Neighbor is in closedList
                    else if (openList.IndexOf(cList[k].Neighbor[i]) == -1)  // this Neighbor is not in openList
                    {
                        openList.Add(cList[k].Neighbor[i]); // add it to openList
                        
                        if (displayOpenList)
                            cList[cList[k].Neighbor[i]].DrawEllipse(graphic, Brushes.Violet); //.DrawOpen(graphic);   // ****************************

                        cList[cList[k].Neighbor[i]].Parent = k; // set parent
                        if (i == 0 || i == 2 || i == 4 || i == 6)
                            cList[cList[k].Neighbor[i]].G = cList[k].G + 10; // 臨邊 加 10
                        else
                            cList[cList[k].Neighbor[i]].G = cList[k].G + 14; // 斜邊 加 14
                        cList[cList[k].Neighbor[i]].H = 10 * (Math.Abs(cList[Target].row - cList[cList[k].Neighbor[i]].row) +
                            Math.Abs(cList[Target].column - cList[cList[k].Neighbor[i]].column));
                    }
                    else // this Neighbor is already in openList
                    {
                        if (i == 0 || i == 2 || i == 4 || i == 6)
                            G = cList[k].G + 10; // 臨邊 加 10
                        else
                            G = cList[k].G + 14; // 斜邊 加 14

                        if (G < cList[cList[k].Neighbor[i]].G)  // 看看是否要 更新 這個鄰居點的路徑
                        {
                            cList[cList[k].Neighbor[i]].Parent = k; // 重設 parent
                            cList[cList[k].Neighbor[i]].G = G;
                        }
                    }
                }

                if (displayOpenList)
                    Thread.Sleep(100);  // 休息一下 // ****************************
            }

            if (reachTarget) // 如果有找到路徑
            {
                pathList.Clear();
                pathList.Add(Target); // 就從 目標點 回頭一一組回路徑

                short b = cList[Target].Parent;
                while (b != -1)
                {
                    pathList.Add(b);
                    b = cList[b].Parent;
                }
            }

            this.Invalidate();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            graphic = this.CreateGraphics();
        }

        // 清除圍牆
        private void button4_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < wallList.Count; i++)
                cList[wallList[i]].wall = false;
            wallList.Clear();

            this.Invalidate();
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (startRectDragging)
            {
                startRectDragging = false;
                for (short i = 0; i < cList.Count; i++)
                {
                    if (cList[i].rect0.Contains(startRect.pos))
                    {
                        if (Target == i) // 開始點 不能在 目標點
                        {
                            startRect.pos = cList[Start].pos; // startRect 移回到 原先的開始點 
                            this.Invalidate();
                            return;
                        }
                        else 
                        {
                            int old = wallList.IndexOf(i);
                            if (old != -1)
                            {
                                cList[i].wall = false;
                                wallList.RemoveAt(old); // 如果疊在牆上 將牆移除
                            }
                            startRect.pos = cList[i].pos;
                            cList[Start].start = false; // 開始點 更換
                            Start = i;
                            cList[Start].start = true;
                            this.Invalidate();
                            return;
                        }
                    }
                }

                startRect.pos = cList[Start].pos; // 都沒有到定位 startRect 移回到 原先的開始點 
                this.Invalidate();
            }
            else if (targetRectDragging)
            {
                targetRectDragging = false;
                for (short i = 0; i < cList.Count; i++)
                {
                    if (cList[i].rect0.Contains(targetRect.pos))
                    {
                        if (Start == i) // 目標點 不能在 開始點 
                        {
                            targetRect.pos = cList[Target].pos; // targetRect 移回到 原先的目標點 
                            this.Invalidate(); 
                            return;
                        }
                        else
                        {
                            int old = wallList.IndexOf(i);
                            if (old != -1)
                            {
                                cList[i].wall = false;
                                wallList.RemoveAt(old); // 如果疊在牆上 就將牆移除
                            }
                            targetRect.pos = cList[i].pos;
                            cList[Target].target = false; // 開始點 更換
                            Target = i;
                            cList[Target].target = true;
                            this.Invalidate();
                            return;
                        }
                    }
                }

                targetRect.pos = cList[Target].pos; // 都沒有到定位 targetRect 移回到 原先的目標點 
                this.Invalidate();
            }
        }
    }
}