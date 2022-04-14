using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// ���ҼǺ��࣬��Ӧ�ؼ���cos�������ִ�Сд�����ýǶ�ֵ����ȡС�����10λ��
    /// </summary>
    /// <example>�÷�cos(45)����������š�</example>
    public class TokenCos : TokenTrigonometricFunction
    {
        public TokenCos(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("cos����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Cos(TokenChild.ChangeTokenToDouble("cos�����Ĳ�������������") / 180 * Math.PI), 10);
        }
    }
}