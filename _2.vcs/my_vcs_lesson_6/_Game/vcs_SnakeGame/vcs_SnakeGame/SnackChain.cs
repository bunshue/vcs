using System;
using System.Collections.Generic;
using System.Linq;

namespace vcs_SnakeGame
{


    /// <summary>
    /// 記錄蛇的位置物件
    /// </summary>
    public class node
    {
        /// <summary>
        /// 位置
        /// </summary>
        public System.Drawing.Point Loccation { get; set; }
        /// <summary>
        /// 某個位置的圖
        /// </summary>
        public System.Drawing.Bitmap mImage { get; set; }

        /// <summary>
        /// 這個節點的方向
        /// </summary>
        public SnackChain.Direction Direction { get; set; }


        public node()
        {
        }

        public node(node copy)
        {
            this.Direction = copy.Direction;
            this.Loccation = copy.Loccation;
            this.mImage = new System.Drawing.Bitmap(copy.mImage);
        }
    }


    /// <summary>
    /// 蛇的物件
    /// </summary>
    public class SnackChain : IDisposable
    {
        /// <summary>
        /// 移動之後會有什麼結果
        /// </summary>
        public enum moveResult : sbyte { MoveSuccess = 0, MoveToBlock, MoveToBoundary, BiteMyself, Eat }

        /// <summary>
        /// 在視覺上蛇的方向(4-way)
        /// </summary>
        public enum Direction : byte { right = 0, down, left, up }


        public map Map { get { return this._map; } }

        /// <summary>
        /// 記錄蛇的頭位置
        /// </summary>
        node _head;

        /// <summary>
        /// 記錄蛇的尾巴位置
        /// </summary>
        node _tail;

        /// <summary>
        /// 蛇所在的地圖
        /// </summary>
        map _map;

        List<node> _chain;
        /// <summary>
        /// 記錄整條蛇的chain
        /// </summary>
        public List<node> chain { get { return this._chain; } }

        /// <summary>
        /// 當修改過方向之後,不能再修改方向,只能等待蛇移動之後才能再進行改變
        /// </summary>
        public bool CanChangeDirection { get; set; }

        public delegate void GraphicChanged(List<System.Drawing.Point> DisposePoints, List<node> CreatePoints);
        /// <summary>
        /// 當圖形必須修改的時候會引發的事件
        /// </summary>
        public event GraphicChanged OnGraphicChanged;



        /// <summary>
        /// 初始化這個類別
        /// </summary>
        /// <param name="m_map">蛇所在的地圖位置</param>
        public SnackChain(map m_map)
        {
            this.CanChangeDirection = true;

            this._map = m_map;

            this._chain = new List<node>(20);

            /*
             * 建立長度為5的一條蛇
             */
            this._head = new node();
            this._head.mImage = new System.Drawing.Bitmap(this._map.ImgLst.Images["snake-head"]);
            this._head.Loccation = new System.Drawing.Point(10,0);
            this._head.Direction = Direction.right;
            this._chain.Add(new node(this._head) );


            for (int i = 9; i >= 1; i--)
            {
                node tmp = new node();
                tmp.Loccation = new System.Drawing.Point(i, 0);
                tmp.mImage = new System.Drawing.Bitmap(this._map.ImgLst.Images["snake-body"]);
                tmp.Direction = Direction.right;
                this._chain.Add(tmp);
            }


            this._tail = new node();
            this._tail.Loccation = new System.Drawing.Point(0, 0);
            this._tail.mImage = new System.Drawing.Bitmap(this._map.ImgLst.Images["snake-tail"]);
            this._tail.Direction = Direction.right;

            this._chain.Add(this._tail);
            //---------------------------

        }

        /// <summary>
        /// 根據目前的方向移動這條蛇
        /// </summary>
        /// <returns></returns>
        public moveResult Move()
        {
            //根據目前蛇的方向,改變蛇頭的方向
            switch (this._head.Direction)
            {
                case Direction.right:
                    this._head.Loccation = new System.Drawing.Point(this._head.Loccation.X + 1, this._head.Loccation.Y);
                    break;
                case Direction.down:
                    this._head.Loccation = new System.Drawing.Point(this._head.Loccation.X , this._head.Loccation.Y + 1);
                    break;
                case Direction.left:
                    this._head.Loccation = new System.Drawing.Point(this._head.Loccation.X - 1, this._head.Loccation.Y );
                    break;
                case Direction.up:
                    this._head.Loccation = new System.Drawing.Point(this._head.Loccation.X , this._head.Loccation.Y - 1);
                    break;
                default:
                    break;
            }

            moveResult result = moveResult.MoveSuccess;

            //如果移動後蛇的位置有在這張地圖上
            if (this._map.WithinBoundary(this._head.Loccation))
            {
                node crashNode;

                BiteMyself(this._head.Loccation , out crashNode) ;
                //判斷有沒有咬到自己
                if (crashNode != null && crashNode.Loccation != this._tail.Loccation)
                {
                    result = moveResult.BiteMyself;
                }
                else
                {
                    //取得移動後蛇頭的位置的地圖資訊
                    switch (this._map.GetBlock(this._head.Loccation))
                    {
                        //如果可以移動
                        case map.blocktype.Road:
                            //蛇的chain全部移動
                            MoveChain(false);
                            result = moveResult.MoveSuccess;
                            break;
                        //如果是障礙物
                        case map.blocktype.Obstacle:
                            MoveChain(false);
                            result = moveResult.MoveToBlock;
                            break;
                        case map.blocktype.Food:
                            this._map.eat();
                            MoveChain(true);
                            result = moveResult.Eat;
                            break;
                        default:
                            break;
                    }
                }
                //return moveResult.MoveToBlock;
            }
            else
                result = moveResult.MoveToBoundary;
            return result;
        }

        /// <summary>
        /// 檢查有沒有咬到自己
        /// </summary>
        /// <param name="_pt">要搜尋的位置</param>
        /// <param name="crashNode">如果發生吃到自己就回傳發生此事件的那個節點</param>
        /// <returns></returns>
        void BiteMyself(System.Drawing.Point _pt , out node crashNode)
        {
            crashNode = null;
            //逐一檢查每個節點的位置
            foreach (node n in this._chain)
                if (n.Loccation == _pt)
                    crashNode = n;
        }




        /// <summary>
        /// 改變蛇頭的方向
        /// </summary>
        /// <param name="_d"></param>
        public void ChangeDirection(Direction _d)
        {
            if (!this.CanChangeDirection)
                return;
            //防止使用者的錯誤動作,如果目前往右走就不能往左
            byte b = this._head.Direction - _d;
            b = (byte)Math.Abs(b);

            if (b % 2 == 0)
                return;
            //----------------------------------------------
            this._head.Direction = _d;
            this.CanChangeDirection = false;
        }


        /// <summary>
        /// 移動這個chain
        /// </summary>
        void MoveChain(bool _eat)
        {
            //需要清除的point
            List<System.Drawing.Point> clearPTs = new List<System.Drawing.Point>(this.chain.Count);
            //需要重新產生的node
            List<node> CreatePTs = new List<node>(this.chain.Count);

            //產生一個新的頭
            node newHead = new node(this._head);
            //加入到重新產生的node的list裡面
            CreatePTs.Add(newHead);

            //把新的node插入到list最前面那個元素
            this._chain.Insert(0, newHead);
            /*把舊的頭變成身體*/
            //舊的頭加入清除行列
            clearPTs.Add(this._chain[1].Loccation);
            //把舊的頭改成身體
            this._chain[1].mImage.Dispose();
            this._chain[1].mImage = new System.Drawing.Bitmap(this._map.ImgLst.Images["snake-body"]);
            //把改成身體的頭加入產生的行列
            CreatePTs.Add(this._chain[1]);
            //----------------------------

            if (!_eat)
            {
                /*清除尾巴,假設目前蛇的長度為5,加入新的頭之後長度＝6,要砍掉最後一個尾巴,這樣數量才會變回5*/
                clearPTs.Add(this._chain.Last<node>().Loccation);
                this._chain.RemoveAt(this._chain.Count - 1);

                //把本來為身體的變成尾巴
                clearPTs.Add(this._chain.Last<node>().Loccation);
                this._chain.Last<node>().mImage.Dispose();
                this._chain.Last<node>().mImage = new System.Drawing.Bitmap(this._map.ImgLst.Images["snake-tail"]);
                CreatePTs.Add(this._chain.Last<node>());
            }

            this._tail = this._chain[this._chain.Count - 1];
            this.OnGraphicChanged(clearPTs, CreatePTs);
        }

        public void Dispose()
        {
            this._map.Dispose();
            //this._map.ImgLst.Dispose();
            this._chain.Clear();
            GC.SuppressFinalize(this);
        }

        public bool HasNode(System.Drawing.Point _pt)
        {
            node crashNode;
            this.BiteMyself(_pt, out crashNode);
            if (crashNode == null)
                return false;
            else
            {
                //Console.WriteLine("has node!!");
                return true;
            }
        }
    }

    /// <summary>
    /// 地圖物件
    /// </summary>
    public class map
    {
        /// <summary>
        /// 地圖資訊的每一個block的狀態列舉
        /// </summary>
        public enum blocktype : sbyte { Road = 0, Obstacle, Food }


        /// <summary>
        /// 記錄這個地圖的資訊陣列（1維）
        /// </summary>
        private blocktype[] _map;
        /// <summary>
        /// 這個地圖資訊有多大
        /// </summary>
        private System.Drawing.Size Mapsize;

        private System.Windows.Forms.ImageList _imgLst;
        /// <summary>
        /// 圖形資料（地圖.蛇）
        /// </summary>
        public System.Windows.Forms.ImageList ImgLst { get { return this._imgLst; } }


        /// <summary>
        /// 初始化這個類別
        /// </summary>
        /// <param name="_s"></param>
        public map(System.Drawing.Size _s)
        {
            this._map = new blocktype[_s.Width * _s.Height];

            for (int i = 0; i < _s.Height; i++)
                for (int j = 0; j < _s.Width; j++)
                    this._map[i * _s.Height + j] = blocktype.Road;

            this.Mapsize = _s;
            this._imgLst = new System.Windows.Forms.ImageList();

            this._imgLst.ImageSize = new System.Drawing.Size(20, 20);
            //測試用,產生一個20*20綠色的bitmap物件
            System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(20, 20, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(bmp);
            g.Clear(System.Drawing.Color.Green);
           
            this._imgLst.Images.Add("snake-body", new System.Drawing.Bitmap(bmp));
            g.Clear(System.Drawing.Color.Blue);
            this._imgLst.Images.Add("snake-head", new System.Drawing.Bitmap(bmp));
            g.Clear(System.Drawing.Color.Red);
            this._imgLst.Images.Add("snake-tail", new System.Drawing.Bitmap(bmp));
            g.Clear(System.Drawing.Color.White);
            this._imgLst.Images.Add("road", new System.Drawing.Bitmap(bmp));
            g.Clear(System.Drawing.Color.Pink);
            this._imgLst.Images.Add("food", new System.Drawing.Bitmap(bmp));
            bmp.Dispose();
            g.Dispose();
        }



        /// <summary>
        /// 取得某個位置的狀態資訊
        /// </summary>
        /// <param name="_p"></param>
        /// <returns></returns>
        public blocktype GetBlock(System.Drawing.Point _p)
        {
            return this._map[_p.Y * this.Mapsize.Width + _p.X];
        }
        /// <summary>
        /// 判斷這個位置有沒有超出這張地圖的範圍
        /// </summary>
        /// <param name="_p"></param>
        /// <returns></returns>
        public bool WithinBoundary(System.Drawing.Point _p)
        {
            if (_p.X >= this.Mapsize.Width || _p.X < 0 || _p.Y >= this.Mapsize.Height || _p.Y < 0)
                return false;
            return true;
        }

        /// <summary>
        /// 設定某一點變成食物
        /// </summary>
        /// <param name="_pt"></param>
        public void SetFood(System.Drawing.Point _pt)
        {
            this.FoodPoint = _pt;
            this._map[_pt.Y * this.Mapsize.Width + _pt.X] = blocktype.Food;
        }


        public System.Drawing.Point FoodPoint;

        public void eat()
        {
            //var t = this.GetBlock(_pt);
            //t = blocktype.Road;

            this._map[FoodPoint.Y * this.Mapsize.Width + FoodPoint.X] = blocktype.Road;
        }

        public void Dispose()
        {
            this._map = null;
            this.ImgLst.Dispose();
            GC.ReRegisterForFinalize(this);
        }
    }
}
