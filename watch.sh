watch -t -d "python main.py > result.txt 2> error.txt; cat ./result.txt | tail -n 30; cat error.txt"
