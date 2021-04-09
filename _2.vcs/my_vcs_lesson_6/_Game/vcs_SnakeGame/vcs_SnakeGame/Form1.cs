using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SnakeGame
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const int WM_KEYDOWN = 0x0100;
        const int WM_CHAR = 0x0102;
        
        //接收來自作業系統的訊息
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_KEYDOWN:
                    //當keyborad被按下的時候
                    char keys = (char)m.WParam;

                    if ((Keys)keys == Keys.Escape)
                        this.Close();

                    if ((Keys)keys == Keys.Enter)
                        NewGame();

                    if (this.sc == null)
                        break;

                    Keys key = (Keys)keys;

                    Console.WriteLine("key-> " + key.ToString());
                    switch (key)
                    {
                        case Keys.Down:
                            this.sc.ChangeDirection(SnackChain.Direction.down);
                            break;
                        case Keys.Left:
                            this.sc.ChangeDirection(SnackChain.Direction.left);
                            break;
                        case Keys.Right:
                            this.sc.ChangeDirection(SnackChain.Direction.right);
                            break;
                        case Keys.Up:
                            this.sc.ChangeDirection(SnackChain.Direction.up);
                            break;
                        case Keys.Add:
                            Console.WriteLine("speed up!");
                            this.delay = (this.delay > 10) ? (UInt16)(this.delay - 10) : this.delay;
                            this.Text = "當前延遲時間: " + this.delay ;
                            break;
                        default:
                            break;
                    }
                    
                    break;
                case WM_CHAR:
                    char keys1 = (char)m.WParam;
                    Console.WriteLine(keys1);
                    break;
                default:
                    break;
            }
            base.WndProc(ref m);
        }

        #region 變數宣告

        UInt32 eatCounts = 0;

        SnackChain sc;

        UInt16 delay;

        System.Threading.Thread _t;

        SnackChain.moveResult moveresult;

        #endregion


        #region 遊戲邏輯相關

        void sc_OnGraphicChanged(List<Point> DisposePoints, List<node> CreatePoints)
        {
            this.RefreshPictureBoxAsyn(DisposePoints, (byte)UpdateImageEvents.Dispose);
            this.RefreshPictureBoxAsyn(CreatePoints, (byte)UpdateImageEvents.Create);
        }

        

        

        /// <summary>
        /// 開啟一個新的遊戲
        /// </summary>
        void NewGame()
        {
            //還原變數成初始狀態
            this.eatCounts = 0;
            this.delay = 200;
            this.label1.ForeColor = Color.Black;
            this.label1.Text = "目前吃了 " + (this.eatCounts) + " 個";

            this.pictureBox1.Size = new Size(600, 400);

            //建立一個空的map,大小為 20 * 30 （高 * 寬）
            map _map = new map(new Size(30, 20));

            //先清除picturebox上面的東西
            this.pictureBox1.Refresh();

            //如果蛇不是空的,代表是重新開始遊戲
            if (this.sc != null)
                this.sc.Dispose(); //關閉蛇的資源

            if (this._t != null)
                this._t.Abort();

            //建立蛇的chain
            this.sc = new SnackChain(_map);
            //當遊戲必須更新當前畫面的時候,要去sc_OnGraphicChanged處理事件
            this.sc.OnGraphicChanged += new SnackChain.GraphicChanged(sc_OnGraphicChanged);

            //如果沒有背景圖,就產生一個背景圖
            if (this.pictureBox1.BackgroundImage == null)
            {
                Bitmap bmp = new Bitmap(this.pictureBox1.Size.Width, this.pictureBox1.Size.Height, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

                Graphics g = Graphics.FromImage(bmp);
                //清空城白色的
                g.Clear(Color.White);

                g.Dispose();
                //把背景圖塗上去
                this.pictureBox1.BackgroundImage = bmp;
            }
            //更新目前的picturebox
            this.pictureBox1.Refresh();
            //開啟一個背景執行續,來移動蛇的chain
            this._t = new System.Threading.Thread(GameMove);
            this._t.Start();
        }

        void GameMove()
        {
            this.GenerateFood();
            this.CreateNodesToForeImage(this.sc.chain.ToList<node>());

            while (true)
            {
                System.Threading.Thread.Sleep((int)delay);
                this.moveresult = this.sc.Move();
                switch (moveresult)
                {
                    case SnackChain.moveResult.MoveSuccess:
                        break;
                    case SnackChain.moveResult.MoveToBlock:
                        SetLabelAsyn(this.label1, (byte)UpdateLabelEvents.Crash);
                        return;
                    case SnackChain.moveResult.MoveToBoundary:
                        SetLabelAsyn(this.label1, (byte)UpdateLabelEvents.Crash);
                        return;
                    case SnackChain.moveResult.BiteMyself:
                        SetLabelAsyn(this.label1, (byte)UpdateLabelEvents.Crash);
                        return;
                    case SnackChain.moveResult.Eat:
                        
                        this.SetLabelAsyn(this.label1, (byte)UpdateLabelEvents.EatFood);

                        this.delay = ((this.eatCounts % 10 == 0) && (this.delay > 10)) ? (UInt16)(this.delay - 10) : this.delay;

                        
                        this.RefreshPictureBoxAsyn(null, (byte)UpdateImageEvents.GenerateFood);

                        break;
                    default:
                        return;
                }
                this.sc.CanChangeDirection = true;
                
            }
        }


        /// <summary>
        /// 產生一個食物讓貪食蛇吃
        /// </summary>
        void GenerateFood()
        {
            Console.WriteLine("generate Food!");


            Console.WriteLine("current eat " + this.eatCounts);
            Random r = new Random();

            Point dstPt = new Point();

            do
            {
                int x = r.Next(0, 29);
                int y = r.Next(0, 19);

                dstPt = new Point(x, y);

                if (!this.sc.HasNode(dstPt) && (this.sc.Map.GetBlock(dstPt) == map.blocktype.Road))
                    break;
            } while (true);

            this.sc.Map.SetFood(dstPt);


            this.DrawFoodToFore(dstPt);
            //Graphics g = Graphics.FromImage(this.pictureBox1.Image);

            Console.WriteLine(dstPt.ToString());

            Console.WriteLine("---------------------------");
        }

        #endregion

        #region 繪圖相關

        /// <summary>
        /// 列舉目前要以什麼方式來非同步呼叫更新label
        /// </summary>
        enum UpdateLabelEvents : byte { EatFood , Crash ,   }

        /// <summary>
        /// 列舉出有什麼事件來更新當前的picturebox
        /// </summary>
        enum UpdateImageEvents : byte { Dispose, Create, GenerateFood }

        /// <summary>
        /// 非同步呼叫使用的指派函式
        /// </summary>
        /// <param name="obj"></param>
        /// <param name="_e"></param>
        private delegate void RefreshPictureboxAsynDelegate(object obj, byte _e);

        /// <summary>
        /// 非同步呼叫的方式更新label
        /// </summary>
        /// <param name="obj"></param>
        /// <param name="_e">引發了什麼事件</param>
        private void SetLabelAsyn(object obj, byte _e)
        {
            Label _obj = (Label)obj;
            if (_obj.InvokeRequired)
                _obj.Invoke(new RefreshPictureboxAsynDelegate(SetLabelAsyn), obj, _e);
            else
            {
                //根據傳入的事件來更新label
                switch ((UpdateLabelEvents)_e)
                {
                    case UpdateLabelEvents.Crash:
                        _obj.ForeColor = Color.Red;
                        _obj.Text = "遊戲結束!\n此次總共吃了" + this.eatCounts + "個\n結束原因: " + this.moveresult.ToString() + "\n請按enter重新開始!";
                        break;
                    case UpdateLabelEvents.EatFood:
                        Console.WriteLine("eat the food!");
                        _obj.Text = "目前吃了 " + (++this.eatCounts) + " 個\n延遲速度: " + this.delay;
                        break;
                    default:
                        break;
                }
            }
        }


       
        /// <summary>
        /// 非同步呼叫的方式更新picturebox
        /// </summary>
        /// <param name="obj"></param>
        /// <param name="_e"></param>
        private void RefreshPictureBoxAsyn(object obj,byte _e)
        {
            if (this.pictureBox1.InvokeRequired)
                this.pictureBox1.Invoke(new RefreshPictureboxAsynDelegate(RefreshPictureBoxAsyn), obj, _e);
            else
            {
                //根據傳入的事件來更新picturebox
                switch ((UpdateImageEvents)_e)
                {
                    case UpdateImageEvents.Dispose:
                        this.ClearNodeToForeImage((List<Point>)obj);
                        break;
                    case UpdateImageEvents.Create:
                        this.CreateNodesToForeImage((List<node>)obj);
                        break;
                    case UpdateImageEvents.GenerateFood:
                        this.GenerateFood();
                        break;
                    default:
                        break;
                }
            }
        }

        /// <summary>
        /// 把指定的食物位置畫上去picturebox上面
        /// </summary>
        /// <param name="dstPt"></param>
        void DrawFoodToFore(Point dstPt)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawImage(this.sc.Map.ImgLst.Images["food"], dstPt.X * 20 , dstPt.Y * 20 );
            g.Dispose();
        }


        /// <summary>
        /// 指定某幾些node要畫去picturebox的前景
        /// </summary>
        /// <param name="CreatePoints"></param>
        void CreateNodesToForeImage(List<node> CreatePoints)
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            foreach (node n in CreatePoints)
                g.DrawImage(n.mImage, n.Loccation.X * 20, n.Loccation.Y * 20 );

            g.Dispose();
        }

        /// <summary>
        /// 指定某些位置的資料貼回road
        /// </summary>
        /// <param name="pts"></param>
        void ClearNodeToForeImage(List<Point> pts)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            foreach (Point pt in pts)
                g.DrawImage(this.sc.Map.ImgLst.Images["road"], pt.X * 20 , pt.Y * 20 );
            g.Dispose();

        }

        #endregion

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //當程式被關閉的時候關閉程式所使用的資源
            if (this.sc != null)
                this.sc.Dispose();

            if (this._t != null)
                this._t.Abort();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (this.sc != null)
            {
                this.CreateNodesToForeImage(this.sc.chain.ToList<node>());
                this.DrawFoodToFore(this.sc.Map.FoodPoint);
            }
        }
    }
}
