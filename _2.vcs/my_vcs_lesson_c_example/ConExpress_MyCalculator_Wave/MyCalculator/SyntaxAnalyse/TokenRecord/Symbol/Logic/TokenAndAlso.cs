using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAndAlso : TokenLogic
    {
        public TokenAndAlso(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "AndAlso运算的元素数量不合法";
        }

        public override void Execute()
        {
            this.CheckChildCount(m_ChildCountErrorInformation);
            
            TokenRecord TokenFirst = this.ChildList[0];
            TokenFirst.Execute();
            if (!TokenFirst.ChangeTokenToBoolean())
            {
                this.TokenValue = false;
            }
            else
            {
                TokenRecord TokenSecond = this.ChildList[1];
                TokenSecond.Execute();
                this.TokenValue = TokenSecond.ChangeTokenToBoolean();
            }
        }
    }
}