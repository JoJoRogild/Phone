# Challenge
We need to create a formula for a given name

# Do RE with IDA Pro
The password is generated as follow:
- Calc `Sum` from username `S`:
    ```
    int Sum = 0, t;
    for (long i = 0; i < S.length(); ++i)
    {
        t = S[i];
        for (int j = 0; j < S[i] + 74; ++j)
            t = (137 * t + 187) % 2048;
        Sum += 666 * t * 666 * t;
    }
    ```
- Note that this `Sum` must be positive in 32bit and have at least 9 digits. Otherwise, there is no fomular for this name :(
- Create a map with 10 rows and 19 columns (0-base index): even index column is filled with `0s` and odd index column is filled with `1s`
- For each `1s` column from left to right, corresponding to each digit in `Sum` from left to right, set one cell in this column to `0s`
- There is the map generated from username `LongChampion`, `Sum = 2072973760`
    ```
    0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 2 0 
    0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 
    0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
    0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0
    ```
    Row 2 of first `1s` column and row 0 of the second `1s` column are set to `0s`, the same rule apply for any other `1s` column ...
    Except for the last `1s` column, the target cell is set to `2s` instead of `0s`

# Generate a formula
You need to use 4 character `{U, D, L, R}`, which corresponding to `{Up, Down, Left, Right}` to move from `[0, 0]` to the position of `2s`.

This is quite easy, just do it yourself. The following is the fomular for username `LongChampion` (for the map above, too):
```
0   0 0 0                          
0   0   0                          
0 0 0   0   0 0 0                  
        0   0   0       0 0 0      
        0   0   0       0   0      
        0   0   0       0   0      
        0   0   0       0   0   0 2
        0 0 0   0   0 0 0   0 0 0  
                0   0              
                0 0 0              
```
`DDRRUURRDDDDDDDRRUUUUURRDDDDDDDRRUURRUUUURRDDDDRRUR`

# Author
If you have any question, feel free to contact me at `ThePalazin@Gmail.com`

Sorry for my bad English anh thank you for your attention,

LongChampion