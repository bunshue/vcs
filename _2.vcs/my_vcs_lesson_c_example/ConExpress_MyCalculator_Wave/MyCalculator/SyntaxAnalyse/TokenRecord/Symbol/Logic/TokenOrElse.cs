using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenOrElse : TokenLogic
    {
        public TokenOrElse(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "OrElse运算的元素数量不合法";
        }

        public override void Execute()
        {
            this.CheckChildCount(m_ChildCountErrorInformation);
            
            TokenRecord TokenFirst = this.ChildList[0];
            TokenFirst.Execute();
            if (TokenFirst.ChangeTokenToBoolean())
            {
                this.TokenValue = true;
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
