using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenOr : TokenLogic
    {
        public TokenOr(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "OR�����Ԫ���������Ϸ�";
        }

        public override void Execute()
        {
            base.Execute();
            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];

            this.TokenValue = TokenFirst.ChangeTokenToBoolean() | TokenSecond.ChangeTokenToBoolean();
        }
    }
}
