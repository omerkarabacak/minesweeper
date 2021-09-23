# Command line Minesweeper Game

This is a small command line Minesweeper Game.
Actually it started with a matrix generation challenge and now, became a simple game. :)

It is generating a minefield, putting mines randomly, putting the numbers around the mines regarding to mine counts around it.
I know it could be more fancier but it was a 30 minutes challenge.

If you think that you can do it better or improve it, PRs are welcome!

## How to run it

### With Python

USAGE:
```
python3 minesweeper.py <size> <mine_count>
```

EXAMPLE:
```
python3 minesweeper.py 4 4
```

### With Docker

USAGE:
```
docker run -it ghcr.io/omerkarabacak/minesweeper:1.0 <size> <mine_count>
```

EXAMPLE:
```
docker run -it ghcr.io/omerkarabacak/minesweeper:1.0 4 4
```

## Which Python version
Tested with 3.x