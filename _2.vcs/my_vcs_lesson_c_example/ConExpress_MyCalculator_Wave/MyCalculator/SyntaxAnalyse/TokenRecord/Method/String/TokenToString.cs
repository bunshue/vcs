using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenToString : TokenStringMethod
    {
        public TokenToString(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        public override void Execute()
        {
            this.CheckChildCount("string语句的运算元素数量不合法");

            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            this.TokenValueType = typeof(string);
            this.TokenValue = TokenSource.ChangeTokenToString();
        }
    }
}
