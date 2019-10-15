

```python
def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          smaller = [i for i in x[1:] if i <= pivot]
          bigger = [i for i in x[1:] if i > pivot]
          return quicksort(smaller) + [pivot] + quicksort(bigger)
```


```python
alist=[3,10,6,9,2,5,3,7,1]
```


```python
quicksort(alist)
```




    [1, 2, 3, 3, 5, 6, 7, 9, 10]




```python

```
