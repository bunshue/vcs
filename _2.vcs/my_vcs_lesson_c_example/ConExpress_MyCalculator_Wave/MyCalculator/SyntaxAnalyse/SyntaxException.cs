using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 语法错误类，用于发生错误时提示用户并选中错误的操作符
    /// </summary>
    /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
    public class SyntaxException : Exception
    {
        private int m_Index;
        /// <summary>
        /// 错误列号
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
        public int Index
        {
            get { return m_Index; }
        }

        private int m_Length;
        /// <summary>
        /// 错误操作符长度
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
        public int Length
        {
            get { return m_Length; }
        }

        private string m_Message;
        /// <summary>
        /// 错误信息
        /// </summary>
        public override string Message
        {
            get { return m_Message; }
        }

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="Index">错误处的列号（用于错误时确定错误操作符起始位置）</param>
        /// <param name="Length">错误操作符长度（用于错误时选择错误操作符的长度）</param>
        /// <param name="ErrorInformation">错误信息</param>
        public SyntaxException(int Index, int Length, string ErrorInformation)
        {
            this.m_Index = Index;
            this.m_Length = Length;
            this.m_Message = ErrorInformation;
        }

    }
}
