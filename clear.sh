find . -name '*.aux'  -print0 | xargs -0 rm 
find . -name '*.bbl'  -print0 | xargs -0 rm
find . -name '*.blg'  -print0 | xargs -0 rm
find . -name '*.log' -print0  | xargs -0 rm
find . -name '*.gz'  -print0 | xargs -0 rm
find . -name '*.toc' -print0  | xargs -0 rm
find . -name '*.fls'  -print0 | xargs -0 rm
