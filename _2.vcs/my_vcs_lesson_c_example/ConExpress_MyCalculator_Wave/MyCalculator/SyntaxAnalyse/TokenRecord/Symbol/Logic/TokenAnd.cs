using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAnd : TokenLogic
    {
        public TokenAnd(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "AND运算的元素数量不合法";
        }

        public override void Execute()
        {
            base.Execute();
            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.ChangeTokenToBoolean();
            TokenSecond.ChangeTokenToBoolean();

            this.TokenValue = TokenFirst.ChangeTokenToBoolean() & TokenSecond.ChangeTokenToBoolean();           
        }
    }
}