def init_plotly_online_mode():
    from IPython.display import display_javascript
    from plotly import offline
    offline.offline.__PLOTLY_OFFLINE_INITIALIZED = True
    jscode = """
    require.config({
      paths: {
        d3: 'http://cdnjs.cloudflare.com/ajax/libs/d3/3.5.16/d3.min',
        plotly: 'http://cdn.plot.ly/plotly-1.10.0.min',
        jquery: 'https://code.jquery.com/jquery-migrate-1.4.1.min'
      },

      shim: {
        plotly: {
          deps: ['d3', 'jquery'],
          exports: 'plotly'
        }
      }
    });

    require(['d3', 'plotly'], function(d3, plotly) {
        window.Plotly = plotly;
    });
    """
    display_javascript(jscode, raw=True)


def sudoku_to_table(sudoku, highlights):
    import io
    f = io.StringIO()
    f.write("""
    <style>
    table.sudoku span{
    color:#aaaaaa;
    }

    table.sudoku td{
    width: 30px;
    height: 30px;
    text-align: center;
    font-size: 20px;
    }

    table.sudoku tr.row0 td,
    table.sudoku tr.row3 td,
    table.sudoku tr.row6 td
    {
    border-top:2px solid;
    }

    table.sudoku tr.row8 td{
    border-bottom:2px solid;
    }

    table.sudoku td.col0,
    table.sudoku td.col3,
    table.sudoku td.col6{
    border-left:2px solid;
    }

    table.sudoku td.col8{
    border-right:2px solid;
    }

    table.sudoku .highlight{
    color: black;
    }
    </style>
    """)
    f.write('<table class="sudoku">')
    for i in range(sudoku.shape[0]):
        f.write('<tr class="row{}">'.format(i))
        for j in range(sudoku.shape[1]):
            v = sudoku[i, j]
            t = " " if v == 0 else str(v)
            highlight = "" if (i, j) in highlights else "highlight"
            f.write('<td class="col{j}"><span class="{highlight}">{t}</span></td>'.format(
                j=j, t=t, highlight=highlight))
        f.write("</tr>")
    f.write("</table>")
    return f.getvalue()


def display_sudoku(sudoku, highlights=[]):
    from IPython.display import display_html
    html = sudoku_to_table(sudoku, highlights)
    display_html(html, raw=True)


def mine_to_table(mines):
    import io
    f = io.StringIO()
    f.write("""
    <style>
    table.mine td{
    width: 20px;
    height:20px;
    text-align: center;
    padding: 1px;
    }
    </style>
    """)
    f.write('<table class="mine">')
    for i in range(mines.shape[0]):
        f.write('<tr class="row{}">'.format(i))
        for j in range(mines.shape[1]):
            v = mines[i, j]
            f.write('<td class="col{j}">{v}</td>'.format(
                j=j, v=v))
        f.write("</tr>")
    f.write("</table>")
    return f.getvalue()


def display_mine(mine):
    from IPython.display import display_html
    html = mine_to_table(mine)
    display_html(html, raw=True)
