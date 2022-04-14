using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenGreatOrEqual : TokenCompare
    {
        public TokenGreatOrEqual(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "大于等于运算的元素数量不合法";
        }

        public override void Execute()
        {
            base.Execute();
            this.TokenValue = (base.Compare() >= 0);
        }

    }
}
