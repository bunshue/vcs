using System;
using System.Collections.Generic;
using System.Text;

//Author: Alex Leo
//Email: alexleo321@hotmail.com
//Blog: http://www.cnblogs.com/conexpress/
namespace ConExpress.Calculator
{
    /// <summary>
    /// 语法树分析
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    internal class SyntaxTreeAnalyse
    {
        /// <summary>
        /// 记号段提取，提取顶级操作记号
        /// </summary>
        /// <param name="TokenList">记号列表</param>
        /// <param name="VariableDic">变量字典</param>
        /// <param name="IndexStart">起始序号</param>
        /// <param name="IndexEnd">结束序号</param>
        /// <returns>传入记号段的顶级操作记号记录对象</returns>
        /// <remarks>Author:Alex Leo</remarks>
        internal static TokenRecord SyntaxTreeGetTopTokenAnalyse(List<TokenRecord> TokenList, int IndexStart, int IndexEnd)
        {
            int intIndexCurrent = IndexStart;//当前处理序号
            int intIndexSubStart = IndexStart;//子记号段的起始序号
            TokenRecord Token;//获取当前Token
            Stack<TokenRecord> StackCompart = new Stack<TokenRecord>();//括号堆栈
            Stack<TokenRecord> StackOperate = new Stack<TokenRecord>();//操作记号堆栈

            for (int intIndex = IndexStart; intIndex <= IndexEnd; intIndex++)
            {
                Token = TokenList[intIndex];
                intIndexCurrent = intIndex;
                if (Token is TokenLeftBracket)
                {
                    StackCompart.Push(TokenList[intIndexCurrent]);//把左括号压栈
                    //获取该括号对中包含的记号段
                    intIndexSubStart = intIndexCurrent + 1;//设置子记号段的起始序号
                    //提取记号段
                    //如果语法错误，比如在记号段的末尾没有配对的右括号记号，则会出错，这里假设为语法正确
                    while (StackCompart.Count > 0)
                    {
                        intIndexCurrent += 1;
                        if (intIndexCurrent >= TokenList.Count)
                        {
                            //Error or auto add lossed bracket
                            throw new SyntaxException(Token.Index, Token.Length, "缺少配对的括号");
                        }

                        if (TokenList[intIndexCurrent] is TokenLeftBracket)
                        {
                            StackCompart.Push(TokenList[intIndexCurrent]);
                        }
                        else if (TokenList[intIndexCurrent] is TokenRightBracket)
                        {
                            StackCompart.Pop();
                        }
                    }

                    TokenRecord TokenInnerTop = SyntaxTreeGetTopTokenAnalyse(TokenList, intIndexSubStart, intIndexCurrent - 1);
                    if (TokenInnerTop != null)//只有在取得括号中的顶级节点才添加
                    {
                        Token.ChildList.Add(TokenInnerTop);
                    }
                    else
                    {
                        //无法获取括号内的顶级节点
                        throw new SyntaxException(Token.Index, Token.Length, "括号内不包含计算表达式");
                    }

                    intIndex = intIndexCurrent;//移动序号到当前序号
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }//if token is TokenLeftBracket
                else if (Token is TokenMethod)//方法处理
                {
                    //检查方法后是否接着左括号
                    if (intIndexCurrent >= IndexEnd || !(TokenList[intIndexCurrent + 1] is TokenLeftBracket))
                    {
                        throw new SyntaxException(Token.Index, Token.Length, "方法后缺少括号");
                    }

                    intIndexSubStart = intIndexCurrent;//设置子记号段的起始序号
                    intIndexCurrent += 1;//指针后移
                    StackCompart.Push(TokenList[intIndexCurrent]);//把左括号压栈
                    //提取记号段
                    //如果语法错误，比如在记号段的末尾没有配对的右括号记号，则会出错，这里假设为语法正确
                    while (StackCompart.Count > 0)
                    {
                        intIndexCurrent += 1;
                        if (intIndexCurrent >= TokenList.Count)
                        {
                            //Error or auto add lossed bracket
                            throw new SyntaxException(Token.Index, Token.Length, "缺少配对的括号");
                        }
                        if (TokenList[intIndexCurrent] is TokenLeftBracket)
                        {
                            StackCompart.Push(TokenList[intIndexCurrent]);
                        }
                        else if (TokenList[intIndexCurrent] is TokenRightBracket)
                        {
                            StackCompart.Pop();
                        }
                    }

                    if ((intIndexCurrent - intIndexSubStart) == 2)//如果右括号的序号和方法的序号之差是2，说明中间只有一个左括号
                    {
                        throw new SyntaxException(TokenList[intIndexCurrent - 1].Index, 1, "括号内不包含计算表达式");
                    }

                    //分析方法记号段，因为方法括号段中可能有多个运算结果，比如if，max等，不能用获取顶级节点的方法SyntaxTreeGetTopTokenAnalyse
                    SyntaxTreeMethodAnalyse(TokenList, intIndexSubStart, intIndexCurrent);

                    intIndex = intIndexCurrent;//移动序号到当前序号
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }//if token is TokenKeyword
                else if (Token is TokenSymbol || Token is TokenValue)
                {
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }
                else
                {
                    //不做处理
                    throw new SyntaxException(Token.Index, Token.Length, "运算符位置错误");
                }
            }
            return SyntaxTreeStackGetTopToken(StackOperate);//返回顶级记号
        }


        /// <summary>
        /// 方法记号段分析（处于括号中间的代码段）
        /// </summary>
        /// <param name="ListToken">记号列表</param>
        /// <param name="IndexStart">括号开始的序号</param>
        /// <param name="IndexEnd">括号结束的序号</param>
        /// <remarks>只处理完整的方法段，比如if(...), round(...)</remarks>
        /// <remarks>Author:Alex Leo</remarks>
        private static void SyntaxTreeMethodAnalyse(List<TokenRecord> ListToken, int IndexStart, int IndexEnd)
        {
            int intIndexSubStart = IndexStart;//子记号段的起始序号
            intIndexSubStart = IndexStart + 2;//移动子记号段的开始序号到括号后面
            int intIndexSubEnd = IndexEnd;//子记号段的结束序号
            TokenRecord TokenMethod = ListToken[IndexStart];//方法记号对象
            TokenRecord TokenCurrent;//获取当前Token
            Stack<TokenRecord> StackCompart = new Stack<TokenRecord>();//分隔符堆栈

            for (int intIndex = IndexStart; intIndex <= IndexEnd; intIndex++)
            {
                TokenCurrent = ListToken[intIndex];
                if (TokenCurrent is TokenLeftBracket)
                {
                    StackCompart.Push(TokenCurrent);
                }
                else if (TokenCurrent is TokenRightBracket)
                {
                    StackCompart.Pop();
                    if (StackCompart.Count == 0)//如果是最后一个右括号
                    {
                        intIndexSubEnd = intIndex - 1;//设置段结束序号
                        TokenMethod.ChildList.Add(SyntaxTreeGetTopTokenAnalyse(ListToken, intIndexSubStart, intIndexSubEnd));//递归
                    }
                }
                else if (TokenCurrent is TokenComma)
                {
                    if (StackCompart.Count == 1)//如果是方法的子段
                    {
                        intIndexSubEnd = intIndex - 1;//设置段结束序号
                        TokenMethod.ChildList.Add(SyntaxTreeGetTopTokenAnalyse(ListToken, intIndexSubStart, intIndexSubEnd));//递归
                        intIndexSubStart = intIndex + 1;//把子记号段序号后移
                    }
                }
                else
                {
                    //不作处理
                }
            }

            //TokenMethod.GetType().GetMethod("CheckChildCount").Invoke(TokenMethod, new object[] { "运算元素数量不合法" });
        }


        /// <summary>
        /// 语法树堆栈分析，基于记号的优先级
        /// </summary>
        /// <param name="SyntaxTreeStack">语法树堆栈</param>
        /// <param name="NewToken">新记号</param>
        /// <remarks>Author:Alex Leo</remarks>
        private static void SyntaxTreeStackAnalyse(Stack<TokenRecord> SyntaxTreeStack, TokenRecord NewToken)
        {
            if (SyntaxTreeStack.Count == 0)//如果语法树堆栈中不存在记号，则直接压栈
            {
                SyntaxTreeStack.Push(NewToken);
            }
            else//否则，比较优先级进行栈操作
            {
                //比较优先级，如果新Token优先级高，则压栈；
                //如果新Token优先级低，则弹栈，把弹出的Token设置为新Token的下级，并把新Token压栈；
                //相同优先级也弹栈，并将新Token压栈
                //if (this.m_DicTokenTypePriority[SyntaxTreeStack.Peek().TokenType] < this.m_DicTokenTypePriority[NewToken.TokenType])//低进
                if (SyntaxTreeStack.Peek().Priority < NewToken.Priority)//低进
                {
                    SyntaxTreeStack.Push(NewToken);//低进
                }
                else
                {
                    TokenRecord TempToken = null;
                    //如果堆栈中有记号，并且栈顶的记号优先级大于等于新记号的优先级，则继续弹栈
                    while (SyntaxTreeStack.Count > 0 && (SyntaxTreeStack.Peek().Priority >= NewToken.Priority))
                    {
                        TempToken = SyntaxTreeStack.Pop();
                        if (SyntaxTreeStack.Count > 0)//检测栈顶是否可能为空，如果为空则退出
                        {
                            if (SyntaxTreeStack.Peek().Priority >= NewToken.Priority)
                            {
                                SyntaxTreeStack.Peek().ChildList.Add(TempToken);
                            }
                            else
                            {
                                NewToken.ChildList.Add(TempToken);
                            }
                        }
                        else
                        {
                            NewToken.ChildList.Add(TempToken);
                        }
                    }
                    SyntaxTreeStack.Push(NewToken);//压栈
                }
            }
        }


        /// <summary>
        /// 获取语法树堆栈的顶级记号
        /// </summary>
        /// <param name="SyntaxTreeStack">语法树堆栈</param>
        /// <returns>顶级记号</returns>
        /// <remarks>Author:Alex Leo</remarks>
        private static TokenRecord SyntaxTreeStackGetTopToken(Stack<TokenRecord> SyntaxTreeStack)
        {
            TokenRecord TempToken = null;
            if (SyntaxTreeStack.Count > 0)
            { 
                TempToken = SyntaxTreeStack.Pop();
                while (SyntaxTreeStack.Count > 0)
                {
                    SyntaxTreeStack.Peek().ChildList.Add(TempToken);
                    TempToken = SyntaxTreeStack.Pop();
                }
            }
            return TempToken;
        }
    }//class SyntaxTreeAnalyse
}//namespace