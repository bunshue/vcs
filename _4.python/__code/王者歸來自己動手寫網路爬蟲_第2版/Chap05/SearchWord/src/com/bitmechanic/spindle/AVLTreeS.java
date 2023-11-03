/*
 * Created on 2005-2-9
 *
 */
package com.bitmechanic.spindle;

/**
 * @author Administrator
 */
public class AVLTreeS {

    // Each AVLtree object is (a header of) an AVL-tree.
    // This AVL-tree is represented simply by a reference to its root node (root).
    private Node root;
    
    public AVLTreeS () {
    // Construct an empty AVL-tree.
        this.root = null;
    }
    
    public Node search (String target) {
    // Find which if any node of this AVL-tree contains an element equal to target. 
    // Return a link to that node (or null if there is none).
        int direction = 0;  // ... 0 for here, < 0 for left, > 0 for right
        Node curr = this.root;
        for (;;) {
            if (curr == null)
                return null;
            direction = target.compareTo(curr.element);
            if (direction == 0)
                return curr;
            if (direction < 0)
                curr = curr.left;
            else  // direction > 0
                curr = curr.right;
        }
    }
    
    public int size() {
    	return Node.sizeOfSubtree(this.root);
    }
    
    public boolean find (String target) {
    // Find which if any node of this AVL-tree contains an element equal to target. 
    // Return a link to that node (or null if there is none).
        int direction = 0;  // ... 0 for here, < 0 for left, > 0 for right
        Node curr = this.root;
        for (;;) {
            if (curr == null)
                return false;
            direction = target.compareTo(curr.element);
            if (direction == 0)
                return true;
            if (direction < 0)
                curr = curr.left;
            else  // direction > 0
                curr = curr.right;
        }
    }
    
    public void add (String elem) {
    // Insert the element elem in this AVL-tree.
        Node ins = insertBST(elem);
        if (ins != null)
            rebalance(ins);
    }

    private Node insertBST (String elem) {
    // Insert the element elem in this AVL-tree, treating it as an ordinary
    // binary search tree. Return a link to the newly-inserted leaf node, or null
    // if no node was inserted.
        int direction = 0;  // ... 0 for here, < 0 for left, > 0 for right
        Node parent = null, curr = root;
        for (;;) {
            if (curr == null) {
                Node ins = new Node(elem, parent);
                if (root == null)
                    root = ins;
                else {
                    if (direction < 0)
                        parent.left = ins;
                    else  // direction > 0
                        parent.right = ins;
                }
                return ins;
            }
            direction = elem.compareTo(curr.element);
            if (direction == 0)
                return null;
            parent = curr;
            if (direction < 0)
                curr = curr.left;
            else  // direction > 0
                curr = curr.right;
        }
    }
    
    private Node deletee = null;  // link to node just deleted
                                  // (accessed only by delete and auxiliary methods)

    public void delete (String elem) {
    // Delete the element elem from this AVL-tree.
        deleteBST(elem);
        if (deletee != null) {
            rebalance(deletee);
            deletee = null;
        }
    }

    private void deleteBST (String elem) {
    // Delete the element elem in this AVL-tree, treating it as an ordinary
    // binary search tree.
        int direction = 0;  // ... 0 for here, < 0 for left, > 0 for right
        Node curr = this.root;
        for (;;) {
            if (curr == null)
                return;
            direction = elem.compareTo(curr.element);
            if (direction == 0) {
                Node modified = deleteTopmost(curr);
                Node parent = curr.parent;
                if (curr == this.root)
                    this.root = modified;
                else if (curr == parent.left)
                    parent.left = modified;
                else  // curr == parent.right
                    parent.right = modified;
                if (modified != null)  modified.parent = parent;
                return;
            }
            if (direction < 0)
                curr = curr.left;
            else  // direction > 0
                curr = curr.right;
        }
    }

    private Node deleteTopmost (Node top) {
    // Delete the topmost element in the subtree whose topmost node is top.
    // Return a link to the modified subtree.
        if (top.left == null) {
            deletee = top;
            return top.right;
        } else if (top.right == null) {
            deletee = top;
            return top.left;
        } else {  // top has both a left child and a right child
            top.element = top.right.getLeftmost();
            top.right = deleteLeftmost(top.right);
            return top;
        }
    }

    private Node deleteLeftmost (Node top) {
    // Delete the leftmost node of the (nonempty) subtree
    // whose topmost node is top.
    // Return a link to the modified subtree.
        Node curr = top;
        while (curr.left != null)
            curr = curr.left;
        deletee = curr;
        if (curr == top)
            return top.right;
        else {
            curr.parent.left = curr.right;
            return top;
        }
    }

    private void rebalance (Node node) {
    // Rebalance this AVL-tree, following insertion or deletion of node.
        Node ancestor = node;
        while (ancestor != root) {
            ancestor = ancestor.parent;
            ancestor.setHeight();
            if (! ancestor.isHeightBalanced()) {
                Node greatAncestor = ancestor.parent;
                Node rotated = rotate(ancestor);
                if (ancestor == root)
                    setRoot(rotated);
                else if (ancestor == greatAncestor.left)
                    greatAncestor.setLeft(rotated); 
                else  // ancestor == greatgrandparent.right
                    greatAncestor.setRight(rotated);
                ancestor = rotated;
            }
        }
    }

    private Node rotate (Node grandparent) {
    // Rotate the node grandparent, the node parent (grandparent's higher child),
    // and the node child (parent's higher child).
    // After an insertion, all three nodes are ancestors of the inserted node.
    // After a deletion, only grandparent is an ancestor of the deleted node.
        Node parent = grandparent.higherChild();
        Node child = parent.higherChild();
        Node a, b, c;
        Node t1, t2, t3, t4;
        if (child == parent.left && parent == grandparent.left) {
            a = child;  b = parent;  c = grandparent;
            t1 = child.left;  t2 = child.right;
            t3 = parent.right;  t4 = grandparent.right;
        } else if (child == parent.right && parent == grandparent.left) {
            a = parent;  b = child;  c = grandparent;
            t1 = parent.left;  t2 = child.left;
            t3 = child.right;  t4 = grandparent.right;
        } else if (child == parent.right && parent == grandparent.right) {
            a = grandparent;  b = parent;  c = child;
            t1 = grandparent.left;  t2 = parent.left;
            t3 = child.left;  t4 = child.right;
        } else {  // child == parent.left && parent == grandparent.right
            a = grandparent;  b = child;  c = parent;
            t1 = grandparent.left;  t2 = child.left;
            t3 = child.right;  t4 = parent.right;
        }
        //print();
        //System.out.println("... now rebalancing"
        //        + " a = " + a.element
        //        + " b = " + b.element
        //        + " b = " + c.element);
        a.setLeft(t1);  a.setRight(t2);  a.setHeight();
        c.setLeft(t3);  c.setRight(t4);  c.setHeight();
        b.setLeft(a);   b.setRight(c);   b.setHeight();
        return b;
    }

    private void setRoot (Node newRoot) {
    // Make newRoot this AVL-tree's root node.
        this.root = newRoot;
        newRoot.parent = null;
    }

    //////////// Driver ////////////

    public void print () {
    // Print a textual representation of this AVL-tree.
        printSubtree(root, "");
    }

    private static void printSubtree (Node top, String indent) {
    // Print a textual representation of the subtree of this AVL-tree whose
    // topmost node is top, indented by the string of spaces indent.
        if (top == null)
            System.out.println(indent + "o");
        else {
            System.out.println(indent + "o-->");
            String childIndent = indent + "    ";
            printSubtree(top.right, childIndent);
            System.out.println(childIndent + top.element + " (" + top.height + ")"
                    + (top.parent == null ? "" : " parent " + top.parent.element));
            printSubtree(top.left, childIndent);
        }
    }

    public static void main (String[] args) {
        AVLTreeS t = new AVLTreeS();
    
        t.add("aa");
        t.add("bb");

        System.out.println(t.find("aa"));
        System.out.println(t.size());
    }

    //////////// Inner class ////////////

    public static class Node {
    
        // Each Node object is an AVL-tree node.
        // This node is represented by its element (element) together with
        // references to its left child (left), its right child (right), and
        // its parent (parent), and its height (height).
        // For every element x stored in the subtree at left:
        //    x.compareTo(element) < 0
        // For every element y stored in the subtree at right:
        //    y.compareTo(element) > 0
        private String element;
        private Node left, right, parent;
        private int height;

        public Node (String elem, Node parent) {
        // Construct an AVL-tree node with element elem and no children.
            this.element = elem;
            this.left = null;
            this.right = null;
            this.parent = parent;
            this.height = 0;
        }

        private String getLeftmost () {
        // Return the element in the leftmost node of the (nonempty) subtree
        // whose topmost node is this.
            Node curr = this;
            while (curr.left != null)
                curr = curr.left;
            return curr.element;
        }
    
        private static int sizeOfSubtree (Node top) {
        // Return the size of the subtree whose topmost node is top.
            if (top == null)
                return 0;
            else
                return 1 + sizeOfSubtree(top.left) + sizeOfSubtree(top.right);
        }

        private void setLeft (Node child) {
        // Make child the left child of this node.
            left = child;
            if (child != null)  child.parent = this;
        }

        private void setRight (Node child) {
        // Make child the right child of this node.
            right = child;
            if (child != null)  child.parent = this;
        }

        private void setHeight () {
        // Recompute the height of this node (assuming that the heights of its
        // children are accurate).
            height = Math.max(getHeight(left), getHeight(right)) + 1;
        }

        private static int getHeight (Node node) {
        // Return the height of node.
            return (node == null ? -1 : node.height);
        }
    
        private Node higherChild () {
        // Return the child of this node with the greater height.
        // If the heights are equal, return either child.
            return (getHeight(left) >= getHeight(right) ? left : right);
        }

        private boolean isHeightBalanced () {
        // Return true if and only if this node is height-balanced, i.e.,
        // the heights of its children differ by at most one.
            int balance = getHeight(left) - getHeight(right);
            return (balance >= -1 && balance <= +1);
        }

    }

}


