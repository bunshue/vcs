import textwrap

def help():
    help_msg = """
        This script behaves mostly the same as the `nosetests` command.

        The main difference is that it loads automatically the

        Local options:

            --help, -h: Displays this help.

            --batch[=n]:
                If specified without option '--time-profile', do not run all
                the tests in one run, but split the execution in batches of
                `n` tests each. Default n is 100.

            --time-profile:
                Each test will be run and timed separately and the results will
                be deposited in the files 'timeprof_sort', 'timeprof_nosort'
            --without-knownfailure: Do not load the KnownFailure plugin.

            --theano: This parameter is replaced with the path to the theano
                      library. As theano-nose is a wrapper to nosetests, it

            --debug-batch:
                Use this parameter to run nosetests with options '--verbose',
                '--nocapture' and '--detailed-errors' and show the output of

        The other options will be passed to nosetests, see ``nosetests -h``.
        """

    print(textwrap.dedent(help_msg))

help()

print("------------------------------------------------------------")  # 60個


"""
Topic: 格式化字符串为指定宽度
"""
import textwrap
import os

def reformat_width():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    print(textwrap.fill(s, 70))
    print('*' * 40)
    print(textwrap.fill(s, 40))
    print('*' * 40)
    print(textwrap.fill(s, 40, initial_indent='    '))
    print('*' * 40)
    print(textwrap.fill(s, 40, subsequent_indent='    '))

    # 获取终端屏幕尺寸
    #print(os.get_terminal_size().columns)


reformat_width()

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



