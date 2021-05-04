using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BothChainTable
{
    public class Objects
    {
        private int number;          /**//* 貨物編號 */
        private string name;      /**//* 貨物名稱 */
        private int counter;        /**//* 貨物數量 */

        //構造函數
        public Objects(int num, string Name, int count)
        {
            number = num;
            name = Name;
            counter = count;
        }
        public int Number
        {
            get
            {
                return number;
            }
            set
            {
                number = value;
            }
        }
        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }
        public int Counter
        {
            get
            {
                return counter;
            }
            set
            {
                counter = value;
            }
        }
    }

    // 結點類
    public class ListNode
    {
        public ListNode(Objects bugs)
        {
            goods = bugs;
        }
        /**/
        /// <summary>
        /// 前一個
        /// </summary>     
        public ListNode Previous;

        /**/
        /// <summary>
        /// 後一個
        /// </summary>
        public ListNode Next;
        public ListNode next
        {
            get
            {
                return Next;
            }
            set
            {
                Next = value;
            }
        }
        /**/
        /// <summary>
        /// 值
        /// </summary>
        public Objects goods;
        public Objects Goods
        {
            get
            {
                return goods;
            }
            set
            {
                goods = value;
            }
        }
    }

    public class Clists
    {
        public Clists()
        {
            //構造函數
            //初始化
            ListCountValue = 0;
            Head = null;
            Tail = null;
        }
        /**/
        /// <summary>
        /// 表名
        /// </summary>
        private string clistname = "";
        public string ClistName
        {
            get
            {
                return clistname;
            }
            set
            {
                clistname = value;
            }
        }
        /**/
        /// <summary>
        /// 頭指針
        /// </summary>
        private ListNode Head;

        /**/
        /// <summary>
        /// 尾指針
        /// </summary>
        private ListNode Tail;

        /**/
        /// <summary>
        /// 目前指針
        /// </summary>  
        private ListNode Current;
        public ListNode current
        {
            get
            {
                return Current;
            }
            set
            {
                Current = value;
            }
        }

        /**/
        /// <summary>
        /// 鏈表數據的個數
        /// </summary> 
        private int ListCountValue;

        /**/
        /// <summary>
        /// 尾部新增數據
        /// </summary>

        public void Append(Objects DataValue)
        {
            ListNode NewNode = new ListNode(DataValue);

            if (IsNull())

            //如果頭指針為空
            {
                Head = NewNode;

                Tail = NewNode;
            }
            else
            {
                Tail.Next = NewNode;

                NewNode.Previous = Tail;

                Tail = NewNode;
            }

            Current = NewNode;

            //鏈表數據個數加一

            ListCountValue += 1;

        }

        /**/
        /// <summary>
        /// 刪除目前的數據
        /// </summary>
        public void Delete()
        {
            //若為空鏈表

            if (!IsNull())
            {
                //若刪除頭

                if (IsBof())
                {
                    Head = Current.Next;
                    Current = Head;
                    ListCountValue -= 1;
                    return;
                }

                //若刪除尾

                if (IsEof())
                {
                    Tail = Current.Previous;

                    Tail.next = null;

                    Current = Tail;

                    ListCountValue -= 1;

                    return;
                }

                //若刪除中間數據

                Current.Previous.Next = Current.Next;

                Current = Current.Previous;

                ListCountValue -= 1;

                return;
            }
        }
        /**/
        /// <summary>
        /// 向後移動一個數據
        /// </summary>
        public void MoveNext()
        {
            if (!IsEof()) Current = Current.Next;
        }
        /**/
        /// <summary>
        /// 向前移動一個數據
        /// </summary>
        public void MovePrevious()
        {
            if (!IsBof()) Current = Current.Previous;
        }
        /**/
        /// <summary>
        /// 移動到第一個數據
        /// </summary>
        public void MoveFrist()
        {
            Current = Head;
        }

        /**/
        /// <summary>
        /// 移動到最後一個數據
        /// </summary>
        public void MoveLast()
        {
            Current = Tail;
        }
        /**/
        /// <summary>
        /// 判斷是否為空鏈表
        /// </summary>
        public bool IsNull()
        {
            if (ListCountValue == 0)
                return true;
            else
                return false;
        }

        /**/
        /// <summary>
        /// 判斷是否為到達尾部
        /// </summary>
        public bool IsEof()
        {
            if (Current == Tail)
                return true;
            else
                return false;
        }
        /**/
        /// <summary>
        /// 判斷是否為到達頭部
        /// </summary>
        public bool IsBof()
        {
            if (Current == Head)
                return true;
            else
                return false;

        }

        public Objects GetCurrentValue()
        {
            return Current.goods;
        }

        /**/
        /// <summary>
        /// 取得鏈表的數據個數
        /// </summary>

        public int ListCount
        {
            get
            {
                return ListCountValue;
            }
        }

        /**/
        /// <summary>
        /// 清空鏈表
        /// </summary>

        public void Clear()
        {
            MoveFrist();
            while (!IsNull())
            {
                //若不為空鏈表,從尾部刪除
                Delete();
            }
        }

        /**/
        /// <summary>
        /// 在目前位置前插入數據
        /// </summary>

        public void Insert(Objects DataValue)
        {
            ListNode NewNode = new ListNode(DataValue);
            if (IsNull())
            {
                //為空表，則新增
                Append(DataValue);
                return;
            }

            if (IsBof())
            {
                //為頭部插入
                NewNode.Next = Head;
                Head.Previous = NewNode;
                Head = NewNode;
                Current = Head;
                ListCountValue += 1;
                return;
            }
            //中間插入
            NewNode.Next = Current;
            NewNode.Previous = Current.Previous;
            Current.Previous.Next = NewNode;
            Current.Previous = NewNode;
            Current = NewNode;
            ListCountValue += 1;
        }

        /**/
        /// <summary>
        /// 進行升序插入
        /// </summary>

        public void InsertAscending(Objects InsertValue)
        {
            //參數：InsertValue 插入的數據
            //為空鏈表
            if (IsNull())
            {
                //新增
                Append(InsertValue);
                return;
            }
            //移動到頭
            MoveFrist();
            if ((InsertValue.Number < GetCurrentValue().Number))
            {
                //滿足條件，則插入，退出
                Insert(InsertValue);
                return;
            }
            while (true)
            {
                if (InsertValue.Number < GetCurrentValue().Number)
                {
                    //滿族條件，則插入，退出
                    Insert(InsertValue);
                    break;
                }

                if (IsEof())
                {
                    //尾部新增
                    Append(InsertValue);
                    break;
                }
                //移動到下一個指針
                MoveNext();
            }
        }
        /**/
        /// <summary>
        /// 進行降序插入
        /// </summary>

        /**/
        /*貨物入庫*/
        public void InsertUnAscending(Objects InsertValue)
        {
            //參數：InsertValue 插入的數據
            //為空鏈表
            if (IsNull())
            {
                //新增
                Append(InsertValue);
                return;
            }
            //移動到頭
            MoveFrist();
            if (InsertValue.Number > GetCurrentValue().Number)
            {
                //滿足條件，則插入，退出
                Insert(InsertValue);
                return;
            }
            while (true)
            {
                if (InsertValue.Number > GetCurrentValue().Number)
                {
                    //滿足條件，則插入，退出
                    Insert(InsertValue);
                    break;
                }

                if (IsEof())
                {
                    //尾部新增
                    Append(InsertValue);
                    break;
                }
                //移動到下一個指針
                MoveNext();
            }
        }
        //根據名字查詢貨物
        public Objects FindObjects(string name)
        {
            ListNode lnode = Head;
            if (IsNull())
            {
                return null;
            }
            else if (IsEof())
            {
                return null;
            }
            else
                while (lnode.goods.Name != name)
                {
                    if (lnode.Next == null)
                    {
                        Current = lnode;
                        return null;
                    }
                    lnode = lnode.Next;
                }
            Current = lnode;
            return lnode.goods;
        }
        //根據編號查詢貨物
        public Objects FindObjects(int number)
        {
            ListNode lnode = Head;
            if (IsNull())
            {
                return null;
            }
            else if (IsEof())
            {
                return null;
            }
            else
                while (lnode.goods.Number != number)
                {
                    if (lnode.Next == null)
                    {
                        Current = lnode;
                        return null;
                    }
                    lnode = lnode.Next;
                }
            Current = lnode;
            return lnode.goods;
        }
        /**/
        /*貨物出庫*/
        //根據名字刪除貨物
        public Objects DeleteObjects(string name)
        {
            Objects bugs;
            bugs = FindObjects(name);
            Delete();
            return bugs;
        }
        //根據編號刪除貨物
        public Objects DeleteObjects(int number)
        {
            Objects bugs;
            bugs = FindObjects(number);
            Delete();
            return bugs;
        }
    }
}
