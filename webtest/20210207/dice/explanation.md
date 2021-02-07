# Strategy

I used BFS for the calculation.
Usually, checking if already visited a cordinate, all you need is check cordinates.
But in this situation, state of dice is matter, like what number is on the top or which direction it is facing.
So I prepared all state of dice that dice could take.
Contatenation of dice state and dice cordinate is fully descriibed situation.

# Detail

## Using Hash Table

I needed to get index of states.
Although, I could write like this,

```python
STATES.get_index(state)
```

this could take much calculation cost.
So instead of doing that, I prepared mapping table from state to index using dictionary which is hash table.
As writing this explanation, I realized that I could refactor how to decline `STATE_TO_IDX`.

```python
STATE_TO_IDX = {value: idx for idx, value in enumerate(STATES)}
```

But I could not rewrite because I've already answered, so I show it here.
