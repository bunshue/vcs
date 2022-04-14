using System;
using System.Collections.Generic;
using System.Text;

//Author: Alex Leo
//Email: alexleo321@hotmail.com
//Blog: http://www.cnblogs.com/conexpress/

namespace ConExpress.Calculator
{
    /// <summary>
    /// 记号值类型枚举
    /// </summary>
    /// <remarks>Author:Alex Leo;</remarks>
    public enum TokenValueTypeEnum
    {
        /// <summary>
        /// 字符串值类型
        /// </summary>
        String,
        /// <summary>
        /// 数字值类型
        /// </summary>
        Number,
    }

    /// <summary>
    /// 操作记号类型枚举
    /// </summary>
    /// <remarks>Author:Alex Leo;</remarks>
    public enum OperateTokenTypeEnum
    {
        /// <summary>
        /// 关键字
        /// </summary>
        TokenKeyword,
        /// <summary>
        /// 符号
        /// </summary>
        TokenSymbol,
    }

    /// <summary>
    /// 记号记录
    /// </summary>
    /// <remarks>Author:Alex Leo;</remarks>
    public abstract class TokenRecord
    {
        #region 属性和字段

        //下级个数
        protected int m_ChildCount;

        private int m_Index;
        /// <summary>
        /// 列序号
        /// </summary>
        public int Index
        {
            get { return m_Index; }
        }

        /// <summary>
        /// 优先级，必须赋值
        /// </summary>
        protected int m_Priority;
        /// <summary>
        /// 优先级
        /// </summary>
        /// <returns></returns>
        public int Priority
        {
            get { return m_Priority; }
        }

        private int m_Length;
        /// <summary>
        /// 操作符长度
        /// </summary>
        public int Length
        {
            get { return m_Length; }
        }

        private Type m_TokenValueType;
        /// <summary>
        /// 记号值类型
        /// </summary>
        public Type TokenValueType
        {
            get { return m_TokenValueType; }
            set { m_TokenValueType = value; }
        }

        private object m_TokenValue;
        /// <summary>
        /// 记号值
        /// </summary>
        public object TokenValue
        {
            get { return m_TokenValue; }
            set { m_TokenValue = value; }
        }


        private List<TokenRecord> m_ChildList = new List<TokenRecord>();
        /// <summary>
        /// 下级列表
        /// </summary>
        public List<TokenRecord> ChildList
        {
            get { return m_ChildList; }
        }

        #endregion

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="Index">序号</param>
        /// <param name="Length">自身长度</param>
        public TokenRecord(int Index, int Length)
        {
            this.m_Index = Index;
            this.m_Length = Length;
            this.SetPriority();
            this.SetChildCount();
        }


        #region 方法

        /// <summary>
        /// 重写ToString方法
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            //可以根据需要修改以显示不同的信息
            return this.GetType().Name + "_" + GetValueString() + "_" + GetTypeName();
        }

        /// <summary>
        /// 获取值的字符串表示
        /// </summary>
        /// <returns></returns>
        public string GetValueString()
        {
            if (this.TokenValue == null)
                return "";
            else
                return this.TokenValue.ToString();
        }

        /// <summary>
        /// 获取类型名称
        /// </summary>
        /// <returns></returns>
        public string GetTypeName()
        {
            if (this.TokenValueType == null)
                return "未初始化类型";
            else
                return this.TokenValueType.ToString();
        }

        /// <summary>
        /// 检查下级数量，必要时可以重写，因为有些Token的下级数量可以是一个区间
        /// </summary>
        /// <param name="ErrorInformation">下级数量不符时显示的错误信息</param>
        internal void CheckChildCount(string ErrorInformation)
        {
            if (this.m_ChildList.Count != this.m_ChildCount)
                throw new SyntaxException(this.m_Index, this.m_Length, ErrorInformation);
        }

        #region 必须重写的方法

        /// <summary>
        /// 执行代码
        /// </summary>
        public abstract void Execute();

        /// <summary>
        /// 设置下级数量
        /// </summary>
        protected abstract void SetChildCount();

        /// <summary>
        /// 设置优先级
        /// </summary>
        protected abstract void SetPriority();

        #endregion


        #endregion


        #region 转换记号值类型

        /// <summary>
        /// 将记号值转换为字符串类型
        /// </summary>
        internal string ChangeTokenToString()
        {
            string strValue;
            strValue = (string)(this.TokenValue = (this.TokenValue != null ? this.TokenValue.ToString() : ""));
            this.TokenValueType = typeof(string);
            return strValue;
        }

        /// <summary>
        /// 将记号值转换为数字类型
        /// </summary>
        /// <param name="ErrorInformation">无法转换成数字时显示的错误信息</param>
        internal double ChangeTokenToDouble(string ErrorInformation)
        {
            double dblValue;
            if (this.TokenValueType == typeof(string))
            {
                if (double.TryParse(this.TokenValue.ToString(), out dblValue))
                {
                    this.TokenValue = dblValue;
                    this.TokenValueType = typeof(double);
                }
                else
                    throw new SyntaxException(this.m_Index, this.m_Length, ErrorInformation);
            }
            else if (this.TokenValueType == typeof(bool))
            {
                try
                {
                    dblValue = Convert.ToDouble(this.TokenValue);
                    this.TokenValue = dblValue;
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    throw new SyntaxException(this.m_Index, this.m_Length, ErrorInformation);
                }
            }
            else
            {
                dblValue = Convert.ToDouble(this.TokenValue != null ? this.TokenValue : 0D);
                this.TokenValue = dblValue;
            }
            return dblValue;
        }

        /// <summary>
        /// 将记号值转换为逻辑值
        /// </summary>
        internal bool ChangeTokenToBoolean()
        {
            this.TokenValueType = typeof(bool);
            bool blnValue = false;
            if (this.TokenValueType == typeof(string))
            {
                switch (this.TokenValue.ToString().Trim().ToLower())
                {
                    case "true":
                        blnValue = (bool)(this.TokenValue = true);
                        break;
                    case "false":
                    case "":
                    default:
                        blnValue = (bool)(this.TokenValue = false);
                        break;
                }
            }
            else if (this.TokenValueType == typeof(double))
            {
                blnValue = (bool)((Convert.ToInt32(this.TokenValue) != 0) ? (this.TokenValue = true) : (this.TokenValue = false));
                //检查上一行代码是否错误
            }
            else
            {
                blnValue = Convert.ToBoolean(this.TokenValue != null ? this.TokenValue : false);
                this.TokenValue = blnValue;
            }

            return blnValue;
        }

        #endregion

    }//class TokenRecord
}//namespace