using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 分隔符记号类
    /// </summary>
    public abstract class TokenCompart : TokenSymbol
    {
        public TokenCompart(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        protected override void SetPriority()
        {
            this.m_Priority = 5;//这里并无实际意义
        }

        public override void Execute()
        {
            throw new SyntaxException(this.Index, this.Length, "分隔符无法执行运算");
        }
    }
}
