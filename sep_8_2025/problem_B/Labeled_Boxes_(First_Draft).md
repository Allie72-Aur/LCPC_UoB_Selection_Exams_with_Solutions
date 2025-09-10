# Problem B: Labeled Boxes (Logic Puzzle)

## Problem Statement

Three boxes are labeled: Apples, Oranges, Mix (Apples & Oranges). All labels
are wrong. You may pick one fruit from one box.

* Which box do you choose from?
* How do you relabel correctly?

## Analisys

This is a derrangement of the set {apples, oranges, mix}, the box labeled
"Mix" contains either apples OR oranges. If this box contains one fruit then
the box labeled with the other fruit nessesaraly contains a mix of both;
because it can't contain the fruit on its label.

## Answer to Puzzle

The solution is to choose the box labeled "Mix" to pick from, and whichever
fruit it contains; you swap its label with the box labeled with the other fruit.  
Now, the box labeled "Mix" actually contains a mix of both fruits, and the
other two boxes' labels are swapped, therefore correct them by swapping
them, and you now relabeled the boxes correctly.
