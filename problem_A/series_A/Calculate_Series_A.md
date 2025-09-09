# Calculating series A

A = (X + 1)/(2)! + (X + 2)/(4)! + (X + 3)/(8)! + ... + (X + 7)/(128)!
A = Summation from i = 1 through 7, of `(x + i) / (2^i)!`  
replace the above lines with LaTeX  

## Pseudocode

|Procedure Calc_A is
|    input: `X` a pre-defined constant  
|
|    let `Sum` <- 0  
|    *{ Start iterating }*
|    for `j` from 1 through 7
|
|        *{ Calculate 2 raised to the power j }*  
|        let `pow2` <- 1
|        for `k` from 1 through `j`
|            `pow2` <- `pow2` \* 2  
|        *{ `pow2` now contains the desired value, 2^j }*  
|
|        *{ Calculate factorial of `pow2` }*  
|        let `product` <- 1  
|        for `k` from `pow2` downto 1
|            `product` <- `product` \* `k`
|        *{ `product` now contains the factorial of 2^j }*  
|
|        *{ Calculate current term of summation }*
|        let `CurrentTerm` <- (`X` + `j`) / `product`
|
|        *{ Add current term to running sum }*
|        `Sum` <- `Sum` + `CurrentTerm`
|
|    let A <- `Sum`
