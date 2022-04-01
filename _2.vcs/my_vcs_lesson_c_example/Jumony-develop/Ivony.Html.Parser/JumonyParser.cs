﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Ivony.Fluent;
using Ivony.Html.Parser.ContentModels;

namespace Ivony.Html.Parser
{

  /// <summary>
  /// 一个标准 HTML 解析器的实现（基于HTML 4.01规范）
  /// </summary>
  public class JumonyParser : HtmlParserBase, IDomFragmentParserProvider, IDomFragmentParser
  {

    /// <summary>
    /// 获取 HTML DOM 提供程序
    /// </summary>
    public override IHtmlDomProvider DomProvider
    {
      get { return new DomProvider( this ); }
    }

    /// <summary>
    /// 创建一个 HTML 读取器
    /// </summary>
    /// <param name="html">要读取的 HTML</param>
    /// <returns>HTML 读取器</returns>
    protected override IHtmlReader CreateReader( string html )
    {
      return new JumonyReader( html );
    }


    /// <summary>
    /// 处理丢失了开始标签的结束标签
    /// </summary>
    /// <param name="endTag">结束标签信息</param>
    protected override void ProcessEndTagMissingBeginTag( HtmlEndTag endTag )
    {
      //忽略多出的结束标签
    }


    /// <summary>
    /// 处理文本节点
    /// </summary>
    /// <param name="textContent">文本内容</param>
    /// <returns></returns>
    protected override IHtmlTextNode ProcessText( HtmlTextContent textContent )
    {
      var textNode = base.ProcessText( textContent ).CastTo<DomTextNode>();
      textNode.ContentFragment = textContent;
      return textNode;
    }


    /// <summary>
    /// 处理注释
    /// </summary>
    /// <param name="commentContent">注释内容</param>
    /// <returns></returns>
    protected override IHtmlComment ProcessComment( HtmlCommentContent commentContent )
    {
      var commentObject = base.ProcessComment( commentContent ).CastTo<DomComment>();
      commentObject.ContentFragment = commentContent;
      return commentObject;
    }


    /// <summary>
    /// 处理特殊标签
    /// </summary>
    /// <param name="specialTag">特殊标签</param>
    /// <returns></returns>
    protected override IHtmlSpecial ProcessSpecial( HtmlSpecialTag specialTag )
    {
      var specialObject = base.ProcessSpecial( specialTag ).CastTo<DomSpecial>();
      specialObject.ContentFragment = specialTag;
      return specialObject;
    }



    /// <summary>
    /// 获取文档片段解析器
    /// </summary>
    /// <param name="document">要解析文档片段的文档</param>
    /// <returns></returns>
    public virtual IDomFragmentParser GetFragmentParser( DomDocument document )
    {
      return this;
    }




    /// <summary>
    /// 解析 HTML 文本到指定的文档碎片对象
    /// </summary>
    /// <param name="html">要解析的 HTML 文本</param>
    /// <param name="fragment">要处理的文本碎片</param>
    public virtual void ParseToFragment( string html, DomFragment fragment )
    {

      if ( string.IsNullOrEmpty( html ) )
        return;

      lock ( SyncRoot )
      {

        Initialize();

        SetHtmlSpecification( fragment.Document.HtmlSpecification );

        ContainerStack.Push( fragment );

        ParseInternal( html );

        fragment.ContentFragment = new HtmlContentFragment( Reader, 0, Reader.HtmlText.Length );
      }
    }


  }
}
