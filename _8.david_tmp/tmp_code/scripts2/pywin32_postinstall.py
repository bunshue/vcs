
    # Create the win32com\gen_py directory.
    make_dir = os.path.join(lib_dir, "win32com", "gen_py")
    if not os.path.isdir(make_dir):
        if verbose:
            print("Creating directory", make_dir)
        directory_created(make_dir)
        os.mkdir(make_dir)

    try:
        # create shortcuts
        # CSIDL_COMMON_PROGRAMS only available works on NT/2000/XP, and
        # will fail there if the user has no admin rights.
        fldr = get_shortcuts_folder()
        # If the group doesn't exist, then we don't make shortcuts - its
        # possible that this isn't a "normal" install.
        if os.path.isdir(fldr):
            dst = os.path.join(fldr, "PythonWin.lnk")
            create_shortcut(os.path.join(lib_dir, "Pythonwin\\Pythonwin.exe"),
                            "The Pythonwin IDE", dst, "", sys.prefix)
            file_created(dst)
            if verbose:
                print("Shortcut for Pythonwin created")
            # And the docs.
            dst = os.path.join(fldr, "Python for Windows Documentation.lnk")
            doc = "Documentation for the PyWin32 extensions"
            create_shortcut(chm_file, doc, dst)
            file_created(dst)
            if verbose:
                print("Shortcut to documentation created")
        else:
            if verbose:
                print("Can't install shortcuts - %r is not a folder" % (fldr,))
    except Exception as details:
        print(details)

    # importing win32com.client ensures the gen_py dir created - not strictly
    # necessary to do now, but this makes the installation "complete"
    try:
        import win32com.client
    except ImportError:
        # Don't let this error sound fatal
        pass
    print("The pywin32 extensions were successfully installed.")

def uninstall():
    import distutils.sysconfig
    lib_dir = distutils.sysconfig.get_python_lib(plat_specific=1)
    # First ensure our system modules are loaded from pywin32_system, so
    # we can remove the ones we copied...
    LoadSystemModule(lib_dir, "pywintypes")
    LoadSystemModule(lib_dir, "pythoncom")

    try:
        RegisterCOMObjects(False)
    except Exception as why:
        print("Failed to unregister COM objects:", why)

    try:
        RegisterPythonwin(False)
    except Exception as why:
        print("Failed to unregister Pythonwin:", why)
    else:
        if verbose:
            print('Unregistered Pythonwin')

    try:
        # remove gen_py directory.
        gen_dir = os.path.join(lib_dir, "win32com", "gen_py")
        if os.path.isdir(gen_dir):
            shutil.rmtree(gen_dir)
            if verbose:
                print("Removed directory", gen_dir)

        # Remove pythonwin compiled "config" files.
        pywin_dir = os.path.join(lib_dir, "Pythonwin", "pywin")
        for fname in glob.glob(os.path.join(pywin_dir, "*.cfc")):
            os.remove(fname)

        # The dbi.pyd.old files we may have created.
        try:
            os.remove(os.path.join(lib_dir, "win32", "dbi.pyd.old"))
        except os.error:
            pass
        try:
            os.remove(os.path.join(lib_dir, "win32", "dbi_d.pyd.old"))
        except os.error:
            pass
        
    except Exception as why:
        print("Failed to remove misc files:", why)

    try:
        fldr = get_shortcuts_folder()
        for link in ("PythonWin.lnk", "Python for Windows Documentation.lnk"):
            fqlink = os.path.join(fldr, link)
            if os.path.isfile(fqlink):
                os.remove(fqlink)
                if verbose:
                    print("Removed", link)
    except Exception as why:
        print("Failed to remove shortcuts:", why)
    # Now remove the system32 files.
    files = glob.glob(os.path.join(lib_dir, "pywin32_system32\\*.*"))
    # Try the system32 directory first - if that fails due to "access denied",
    # it implies a non-admin user, and we use sys.prefix
    try:
        for dest_dir in [get_system_dir(), sys.prefix]:
            # and copy some files over there
            worked = 0
            for fname in files:
                base = os.path.basename(fname)
                dst = os.path.join(dest_dir, base)
                if os.path.isfile(dst):
                    try:
                        os.remove(dst)
                        worked = 1
                        if verbose:
                            print("Removed file %s" % (dst))
                    except Exception:
                        print("FAILED to remove", dst)
            if worked:
                break
    except Exception as why:
        print("FAILED to remove system files:", why)

def usage():
    msg = \
"""%s: A post-install script for the pywin32 extensions.
    
This should be run automatically after installation, but if it fails you
can run it again with a '-install' parameter, to ensure the environment
is setup correctly.

Additional Options:
  -wait pid : Wait for the specified process to terminate before starting.
  -silent   : Don't display the "Abort/Retry/Ignore" dialog for files in use.
  -quiet    : Don't display progress messages.
"""
    print(msg.strip() % os.path.basename(sys.argv[0]))

# NOTE: If this script is run from inside the bdist_wininst created
# binary installer or uninstaller, the command line args are either
# '-install' or '-remove'.

# Important: From inside the binary installer this script MUST NOT
# call sys.exit() or raise SystemExit, otherwise not only this script
# but also the installer will terminate! (Is there a way to prevent
# this from the bdist_wininst C code?)

if __name__=='__main__':
    if len(sys.argv)==1:
        usage()
        sys.exit(1)

    arg_index = 1
    while arg_index < len(sys.argv):
        arg = sys.argv[arg_index]
        # Hack for installing while we are in use.  Just a simple wait so the
        # parent process can terminate.
        if arg == "-wait":
            arg_index += 1
            pid = int(sys.argv[arg_index])
            try:
                os.waitpid(pid, 0)
            except AttributeError:
                # Python 2.2 - no waitpid - just sleep.
                time.sleep(3)
            except os.error:
                # child already dead
                pass
        elif arg == "-install":
            install()
        elif arg == "-silent":
            silent = 1
        elif arg == "-quiet":
            verbose = 0
        elif arg == "-remove":
            # bdist_msi calls us before uninstall, so we can undo what we
            # previously did.  Sadly, bdist_wininst calls us *after*, so
            # we can't do much at all.
            if not is_bdist_wininst:
                uninstall()
        else:
            print("Unknown option:", arg)
            usage()
            sys.exit(0)
        arg_index += 1
