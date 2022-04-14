using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 右括号记号类，对应字符)，只在词法分析和语法分析中使用，实际计算时无意义，不需要实现任何功能
    /// </summary>
    public class TokenRightBracket : TokenCompart
    {
        public TokenRightBracket(int Index, int Length)
            : base(Index, Length)
        {
        }
    }
}
