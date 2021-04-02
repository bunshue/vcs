using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace Arbor
{
    /// <summary>
    /// LEFT左子樹，RIGHT右子樹
    /// </summary>
    enum Position { LEFT, RIGHT };
    /// <summary>
    /// LINK指向孩子，THREAD指向後繼
    /// </summary>
    enum Tag { LINK, THREAD };
    /// <summary>
    /// 二叉樹節點的抽像定義
    /// </summary>
    interface IBinNode
    {
        bool isLeaf();
        object Element { get; set; }
        IBinNode Left { get; set; }
        IBinNode Right { get; set; }
    }

    /// <summary>
    /// 搜尋，線索化等操作的接口
    /// </summary>
    interface ITravelBinTree
    {
        void PreOrderTravel();
        void InOrderTravel();
        void RevOrderTravel();
        void Print(IBinNode t);
    }
    interface IInsertBinTree
    {
        void Insert(IBinNode node, Position pos);
    }
    /// <summary>
    /// Normal actualize of bintree
    /// </summary>
    class BinNodePtr : IBinNode
    {
        protected object element;
        protected IBinNode lchild;
        protected IBinNode rchild;
        public BinNodePtr(object e, IBinNode left, IBinNode right)
        {
            element = e;
            lchild = left;
            rchild = right;
        }
        public BinNodePtr(object e)
        {
            element = e;
            lchild = rchild = null;
        }
        public BinNodePtr()
        {
            element = null;
            lchild = rchild = null;
        }
        public bool isLeaf()
        {
            if (lchild == null && rchild == null)
                return true;
            return false;
        }
        public object Element
        {
            get { return element; }
            set { element = value; }
        }
        public IBinNode Left
        {
            get
            {
                return lchild;
            }
            set
            {
                lchild = value;
            }
        }
        public IBinNode Right
        {
            get
            {
                return rchild;
            }
            set
            {
                rchild = value;
            }
        }
    }
    class BinNodeLine : BinNodePtr, IBinNode
    {
        private Tag ltag, rtag;
        public BinNodeLine(object e, IBinNode left, IBinNode right)
            : base(e, left, right)
        { ltag = rtag = Tag.LINK; }
        public BinNodeLine(object e)
            : base(e)
        { ltag = rtag = Tag.LINK; }
        public Tag LTag
        {
            get { return ltag; }
            set { ltag = value; }
        }
        public Tag RTag
        {
            get { return rtag; }
            set { rtag = value; }
        }
    }
    class TravelBinTree : ITravelBinTree, IInsertBinTree
    {
        const int INIT_TREE_SIZE = 20;
        private IBinNode tree;
        private BinNodeLine head; //線索化後的頭指針
        private IBinNode prenode; //指向最近存取過的前驅節點
        public TravelBinTree()
        {
            tree = new BinNodePtr();
        }
        public TravelBinTree(IBinNode INode)
        {
            tree = INode;
        }
        /// <summary>
        /// 先序搜尋樹,用非遞歸算法完成
        /// </summary>
        /// <remarks>非遞歸完成</remarks>
        public void PreOrderTravel()
        {
            IBinNode temptree;
            Stack stk = new Stack(INIT_TREE_SIZE);
            if (tree == null)
                throw (new InvalidOperationException("存取的樹為空"));
            temptree = tree;
            stk.Push(tree);
            while (stk.Count != 0)
            {
                while (temptree != null)
                {
                    Print(temptree);
                    stk.Push(temptree.Left);
                    temptree = temptree.Left;
                }
                stk.Pop(); // 空指針退棧
                if (stk.Count != 0)
                {
                    temptree = (IBinNode)stk.Pop();
                    stk.Push(temptree.Right);
                    temptree = temptree.Right;
                }
            }
        }
        public void InOrderTravel()
        {
            InOrderTravel(tree);
        }
        private void InOrderTravel(IBinNode t)
        {
            if (t == null) return;
            InOrderTravel(t.Left);
            Print(t);
            InOrderTravel(t.Right);
        }
        public void RevOrderTravel()
        {
            RevOrderTravel(tree);
        }
        private void RevOrderTravel(IBinNode t)
        {
            if (t == null) return;
            RevOrderTravel(t.Left);
            RevOrderTravel(t.Right);
            Print(t);
        }
        public void Print(IBinNode t)
        {
            Console.Write(t.Element + ",");
        }
        public void Insert(IBinNode node, Position pos)
        {
            if (node == null)
                throw (new InvalidOperationException("不能將空節點插入樹"));
            switch (pos)
            {
                case Position.LEFT: tree.Left = node; break;
                case Position.RIGHT: tree.Right = node; break;
            }
        }
        /// <summary>
        /// 按照先序搜尋順序搜尋樹
        /// </summary>
        public void TreeBuilder()
        {
            Stack stk = new Stack(INIT_TREE_SIZE);
            stk.Push(tree);
            Position pos;
            string para;
            pos = Position.LEFT;
            IBinNode baby, temp;
            while (true)
            {
                para = Console.ReadLine();
                if (para == "")
                {
                    if (pos == Position.RIGHT)
                    {
                        stk.Pop();
                        while (stk.Count != 0 && ((IBinNode)stk.Peek()).Right != null)
                            stk.Pop();
                        if (stk.Count == 0) break;
                    }
                    else
                        pos = Position.RIGHT;
                }
                else
                {
                    // if (tree.GetType().Equals(baby) == true)
                    baby = new BinNodePtr(para);
                    temp = (IBinNode)stk.Peek();
                    if (pos == Position.LEFT)
                        temp.Left = baby;
                    else
                        temp.Right = baby;
                    pos = Position.LEFT;
                    stk.Push(baby);
                }
            }

        }
        /// <summary>
        /// 中序線索化
        /// </summary>
        public void InOrderThreading()
        {
            head = new BinNodeLine("");
            head.RTag = Tag.THREAD;
            head.Right = head;
            if (tree == null) head.Left = head;
            else
            {
                head.Left = tree; prenode = head;

            }
        }
        /// <summary>
        /// 中序線索化的遞歸完成
        /// </summary>
        /// <param name="t"></param>
        private void InThreading(IBinNode t)
        {
            if (t == null)
                return;
            else
            {
                InThreading(t.Left);
            }
        }
    }
}
