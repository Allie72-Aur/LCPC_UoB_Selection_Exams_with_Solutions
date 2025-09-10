# Five Friends in a Line

* **Five friends sit in a row. Ali is to the left of Sara. Omar is to the right of Sara but not at the end. Mariam is at one end. Who sits in the middle?**  

1. Ali
2. Omar
3. Sara
4. Mariam

## Answer

We can first try to come up with ordering of the five friends that stisfy the stated
conditions. Let's call the fifth friend Aisha, some of the orderings I came up with are:

* (Mariam, Ali, **Sara**, Omar, Aisha)
* (Ali, Sara, **Omar**, Aisha, Mariam)
* (Ali, Sara, **Aisha**, Omar, Mariam), here, assuming it's enough for Omar to be on Sara's general right.

**Verdict**: the question is ill-defined, when you say Ali is to Sara's left do you mean right next to her or to her general left direction, for the sake of mental pictures, could she be holding his right hand with her left hand? Or another analogy would be if they were in a queue instead, would he be right behind her or just generally after her in line?

### A More Rigourous Treatment of the Problem

Let's represent the five positions in the row as P_1,P_2,P_3,P_4,P_5.

* "Ali is to the left of Sara."  
  This means Ali's position number is less than Sara's position number (P_Ali < P_Sara).

* "Omar is to the right of Sara but not at the end."  
  This means Omar's position number is greater than Sara's position number (P_Omar > P_Sara).  
  Since there are 5 positions, the ends are P_1 and P_5. This tells us that Omar cannot be in position P_5.

* "Mariam is at one end."
  This means Mariam is either at position P_1 or P_5.

Let's combine these facts. We know the order of Ali, Sara, and Omar is Ali - Sara - Omar.

1. Case 1: Mariam is at the left end (P_1).
The arrangement starts with Mariam.  
`Mariam - _ - _ - _ - _`  
Now we have to place Ali, Sara, and Omar. The only way to satisfy the conditions (Ali left of Sara, Omar right of Sara, and Omar not at the end) is:
`Mariam - Ali - Sara - Omar - _`  
In this arrangement, Omar is not at the end (P_4).
The final arrangement must be:
`Mariam - Ali - Sara - Omar - Fifth Friend (namely Aisha)`
In this arrangement, Sara is in the middle (P_3).

2. Case 2: Mariam is at the right end (P_5).
The arrangement ends with Mariam.
`_ - _ - _ - _ - Mariam`
Now we have to place Ali, Sara, and Omar. Their order must be Ali - Sara - Omar.
`Ali - Sara - Omar - _ - Mariam`
In this arrangement, Omar is in the P_3 position. The other conditions are met.
The final arrangement must be:
`Ali - Sara - Omar - Fifth Friend - Mariam`
In this arrangement, Omar is in the middle (P_3).

The question is ill-defined in the sense that both Sara and Omar could be in the middle, depending on which end Mariam is on.

Let's re-examine the original question. It asks "Who sits in the middle?". It assumes a single correct answer. This usually means that there is only one arrangement that satisfies all the criteria.

Let's revisit the placement of Omar.

"Omar is to the right of Sara but not at the end."

If Mariam is at the end, say at P 
5
​
 , then we have:
_ _ _ _ M
The only way to place A, S, O in the first four spots is:
A S O _ M
Here, Omar is in the middle position, P 
3
​
 . The fifth friend is in position P 
4
​
 .
This fits all criteria: Ali is left of Sara, Omar is right of Sara, Omar is not at an end (P 
3
​
  is not an end), and Mariam is at an end (P 
5
​
 ).

Let's reconsider the first case. Mariam is at the left end.
M _ _ _ _
The order has to be A S O.
M A S O _
Here, Sara is in the middle position, P 
3
​
 . The fifth friend is in position P 
5
​
 .
This fits all criteria: Ali is left of Sara, Omar is right of Sara, Omar is not at an end (P 
4
​
  is not an end), and Mariam is at an end (P 
1
​
 ).

The two scenarios lead to two different people in the middle. The question is indeed ill-defined as written. However, in such riddles, the common interpretation is that there's a unique solution that can be found.

There are two valid arrangements that satisfy the given conditions, and they place different people in the middle.

1. (Mariam, Ali, Sara, Omar, Aisha) - Sara is in the middle.

2. (Ali, Sara, Omar, Aisha, Mariam) - Omar is in the middle.

The lack of a unique solution makes the multiple-choice question flawed.
