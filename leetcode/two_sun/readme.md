# Problema Two sun

```
https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
```

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Soluçao 1

Usaremos o dict do python para fazer em O(n), pois não será necessário testar todos os pares/fazer
dois for, como fariamos na lista

ideia:

Para cada número num, precisamos descobrir se já vimos o número que completa o target:

complemento=target−num

nums = [2, 7, 11, 15]
target = 9

num = 2
complemento = 9 - 2 = 7
7 ainda não apareceu

num = 7
complemento = 9 - 7 = 2
2 já apareceu → encontramos!

o dict vai armazenar o seguinte:

valor -> indice

assim, no exemplo acima, quando chegarmos no 7, conseguimos descobrir que o 2 está no indice 0

```python
{
    2:0
}
```

Código da solução:

```python
def two_sun(nums:list[int],target:int)->list[int]:
    seen:dict[int,int]={}

    for i,num in enumerate(nums):
        complement=target-num

        if complement in seen:
            return[seen[complement],i]

        seen[num]=i

```

explicando o código

utilizaremos o enumerate, que é uma função do python que nos permite manipular o indice e o elemento
de forma mais elegante, seria como imaginar que temos o seguinte pelo enumerate: (índice, valor) e o
python automaticamente desempacota cada par

```
(0, 2)   → i = 0, num = 2
(1, 7)   → i = 1, num = 7
(2, 11)  → i = 2, num = 11
(3, 15)  → i = 3, num = 15
```

após isso, iremos verificar o complemento, caso ele já estiver sido visto, o algoritmo para,
senão ele continua.

## Solução 2

Usaremos a lista, onde iremos usar dois for, o primeiro irá começar do começo da lista e o outro
irá começar em i+1, assim, a cada iteração iremos testar caso a caso, dando uma complexidade de 0(n^2)

código da solução

```python
def two_sum_list(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []
```
