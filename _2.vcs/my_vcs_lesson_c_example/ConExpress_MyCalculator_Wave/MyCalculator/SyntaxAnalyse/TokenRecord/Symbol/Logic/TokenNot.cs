using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenNot : TokenLogic
    {
        public TokenNot(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 2;
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "NOT�����Ԫ���������Ϸ�";
        }

        public override void Execute()
        {
            base.Execute();

            TokenRecord TokenFirst = this.ChildList[0];
            //TokenFirst.Execute();
            //TODO:��������ƺ�������

            this.TokenValue = !TokenFirst.ChangeTokenToBoolean();

        }
    }
}