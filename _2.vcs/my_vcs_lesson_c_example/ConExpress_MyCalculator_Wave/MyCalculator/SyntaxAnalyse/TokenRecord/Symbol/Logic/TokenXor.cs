using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenXor : TokenLogic
    {
        public TokenXor(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "Xor运算的元素数量不合法";
        }

        public override void Execute()
        {
            base.Execute();
            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];

            this.TokenValue = TokenFirst.ChangeTokenToBoolean() ^ TokenSecond.ChangeTokenToBoolean();
        }
    }
}