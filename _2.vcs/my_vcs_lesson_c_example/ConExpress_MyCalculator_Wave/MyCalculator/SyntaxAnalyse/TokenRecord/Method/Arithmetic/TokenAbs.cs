using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 绝对值记号类，对应关键字abs，不区分大小写。
    /// </summary>
    /// <example>用法abs(-12)，必须带括号。</example>
    public class TokenAbs : TokenArithmeticMethod
    {
        public TokenAbs(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        public override void Execute()
        {
            this.CheckChildCount("Abs方法的运算元素数量不合法");

            TokenRecord Token = this.ChildList[0];
            Token.Execute();

            this.TokenValue = Math.Abs(Token.ChangeTokenToDouble("Abs方法的操作数不是数字"));
        }
    }
}