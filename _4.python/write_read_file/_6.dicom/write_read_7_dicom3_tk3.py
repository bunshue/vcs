import tkinter.tix as tkinter_tix

print(__doc__)

usage = "Usage: python dicomtree.py dicom_filename"


def RunTree(w, filename):
    top = tkinter_tix.Frame(w, relief=tkinter_tix.RAISED, bd=1)
    tree = tkinter_tix.Tree(top, options="hlist.columns 2")
    tree.pack(expand=1, fill=tkinter_tix.BOTH, padx=10, pady=10, side=tkinter_tix.LEFT)
    # print(tree.hlist.keys())   # use to see the available configure() options
    tree.hlist.configure(bg="white", font="Courier 10", indent=30)
    tree.hlist.configure(selectbackground="light yellow", gap=150)

    box = tkinter_tix.ButtonBox(w, orientation=tkinter_tix.HORIZONTAL)
    # box.add('ok', text='Ok', underline=0, command=w.destroy, width=6)
    box.add("exit", text="Exit", underline=0, command=w.destroy, width=6)
    box.pack(side=tkinter_tix.BOTTOM, fill=tkinter_tix.X)
    top.pack(side=tkinter_tix.TOP, fill=tkinter_tix.BOTH, expand=1)
    # https://stackoverflow.com/questions/17355902/python-tkinter-binding-mousewheel-to-scrollbar
    tree.bind_all(
        "<MouseWheel>",
        lambda event: tree.hlist.yview_scroll(int(-1 * event.delta / 120.0), "units"),
    )  # Wheel in Windows
    tree.bind_all(
        "<Button-4>", lambda event: tree.hlist.yview_scroll(int(-1), "units")
    )  # Wheel up in Linux
    tree.bind_all(
        "<Button-5>", lambda event: tree.hlist.yview_scroll(int(+1), "units")
    )  # Wheel down in Linux

    show_file(filename, tree)


def show_file(filename, tree):
    tree.hlist.add("root", text=filename)
    ds = pydicom.dcmread(filename)
    ds.decode()  # change strings to unicode
    recurse_tree(tree, ds, "root", False)
    tree.autosetmode()


def recurse_tree(tree, dataset, parent, hide=False):
    # order the dicom tags
    for data_element in dataset:
        node_id = parent + "." + hex(id(data_element))
        tree.hlist.add(node_id, text=str(data_element))

        if hide:
            tree.hlist.hide_entry(node_id)
        if data_element.VR == "SQ":  # a sequence
            for i, dataset in enumerate(data_element.value):
                item_id = node_id + "." + str(i + 1)
                sq_item_description = data_element.name.replace(
                    " Sequence", ""
                )  # XXX not i18n
                item_text = "{0:s} {1:d}".format(sq_item_description, i + 1)
                tree.hlist.add(item_id, text=item_text)
                tree.hlist.hide_entry(item_id)
                recurse_tree(tree, dataset, item_id, hide=True)


if __name__ == "__main__":
    import pydicom

    filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/CT_small.dcm"

    root = tkinter_tix.Tk()
    root.title("DICOM tree viewer - " + filename)
    root.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(1200, 900, 0, 0))
    # print("{0:d}x{1:d}+{2:d}+{3:d}".format(1200, 900, 0, 0))

    RunTree(root, filename)

    root.mainloop()
