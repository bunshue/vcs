using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMod : TokenArithmeticSymbol
    {
        public TokenMod(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("模运算的操作数数量不合法");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = TokenFirst.ChangeTokenToDouble("模运算的运算元素不是数值") % TokenSecond.ChangeTokenToDouble("模运算的运算元素不是数值");
        }
    }
}
