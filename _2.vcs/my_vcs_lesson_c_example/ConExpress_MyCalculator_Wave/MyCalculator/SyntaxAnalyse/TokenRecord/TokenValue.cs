using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    class TokenValue : TokenRecord
    {
        public TokenValue(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetPriority()
        {
            this.m_Priority = 6;//值的优先级仅低于括号
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 0;
        }

        public override void Execute()
        {
            //throw new Exception("The method or operation is not implemented.");
        }
    }
}