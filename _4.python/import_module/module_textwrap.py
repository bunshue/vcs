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

