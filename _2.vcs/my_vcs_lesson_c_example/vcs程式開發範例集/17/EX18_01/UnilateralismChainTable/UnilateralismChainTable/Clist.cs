using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace UnilateralismChainTable
{
    //  結點類
    public class ListNode
    {
        public ListNode(int NewValue)
        {
            Value = NewValue;
        }

        //前一個
        public ListNode Previous;

        // 後一個
        public ListNode Next;

        // 值
        public int Value;
    }
    // 定義結點之後，開始類線性表的操作編程了.在LIST 類中,採用了，Head ,Tail,  Current，三個指針，使用Append ，
    //MoveFrist,MovePrevious，MoveNext,MoveLast ,Delete,InsertAscending,InsertUnAscending ,Clear 完成移動，新增，
    //刪除,升序插入，降序插入，清空鏈表操作，GetCurrentValue（） 方法取得目前的值。
    public class Clist
    {
        public Clist()
        {
            //構造函數
            //初始化
            ListCountValue = 0;
            Head = null;
            Tail = null;
        }


        // 頭指針
        private ListNode Head;

        // 尾指針  
        private ListNode Tail;

        // 目前指針
        private ListNode Current;

        //鏈表數據的個數
        private int ListCountValue;

        //尾部新增數據 
        public void Append(int DataValue)
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
        //刪除目前的數據
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

        // 向後移動一個數據
        public void MoveNext()
        {
            if (!IsEof()) Current = Current.Next;
        }

        // 向前移動一個數據
        public void MovePrevious()
        {
            if (!IsBof()) Current = Current.Previous;
        }

        // 移動到第一個數據  
        public void MoveFrist()
        {
            Current = Head;
        }


        // 移動到最後一個數據
        public void MoveLast()
        {
            Current = Tail;
        }

        // 判斷是否為空鏈表
        public bool IsNull()
        {
            if (ListCountValue == 0)
                return true;

            return false;
        }

        // 判斷是否為到達尾  
        public bool IsEof()
        {
            if (Current == Tail)
                return true;
            return false;
        }

        // 判斷是否為到達頭部
        public bool IsBof()
        {
            if (Current == Head)
                return true;
            return false;

        }

        public int GetCurrentValue()
        {
            return Current.Value;
        }

        // 取得鏈表的數據個數
        public int ListCount
        {
            get
            {
                return ListCountValue;
            }
        }


        // 清空鏈表
        public void Clear()
        {
            MoveFrist();
            while (!IsNull())
            {
                //若不為空鏈表,從尾部刪除  
                Delete();
            }
        }


        // 在目前位置前插入數據
        public void Insert(int DataValue)
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

        // 進行升序插入  
        public void InsertAscending(int InsertValue)
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
            if ((InsertValue < GetCurrentValue()))
            {
                //滿足條件，則插入，退出
                Insert(InsertValue);
                return;
            }
            while (true)
            {
                if (InsertValue < GetCurrentValue())
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
        //進行降序插入
        public void InsertUnAscending(int InsertValue)
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
            if (InsertValue > GetCurrentValue())
            {
                //滿足條件，則插入，退出
                Insert(InsertValue);
                return;
            }
            while (true)
            {
                if (InsertValue > GetCurrentValue())
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
    }

}
