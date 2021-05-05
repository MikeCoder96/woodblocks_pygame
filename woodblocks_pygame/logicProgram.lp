% % Matrix cells are provided as facts.
% matrixCell(0,0).
% matrixCell(0,1).

% % Shapes are provided as elementary cells to translate
shape(1,0,0).
shape(1,0,1).
shape(1,1,0).

% Model.
cell(1..3, 0..9, 0..9).

index(1..3).

% Translation point used to check for shape consistency.
tX(1..10).
tY(1..10).

blockCount(I,C) :- #count { X,Y: shape(I,X,Y) } = C, index(I).

% Guess.
inCell(I,X,Y) | outCell(I,X,Y) :- cell(I,X,Y).

% Check.

% The number of inCell() has to match exactly the number of blocks that make up a shape.
:- #count{ X,Y: inCell(I,X,Y) } = C1, blockCount(I,C2), C1 != C2, index(I).

% Placing shapes on non-empty cells is not possible.
:- inCell(_,X,Y), matrixCell(X,Y).

% Respect the original shapes shape (the individual matrix cells filled have to compose the same shape of the provided one)
% The chose approach is: find two numbers, tX and tY, such that *all* the generated cells to fill are distant from the original shape provided by tX and tY.
possibleXTransl(I,A) :- tX(A), #count{ X,Y: inCell(I,X,Y), shape(I,X-A,_) } = C1, blockCount(I,C1), index(I).
possibleYTransl(I,B) :- tY(B), #count{ X,Y: inCell(I,X,Y), shape(I,_,Y-B) } = C1, blockCount(I,C1), index(I).
%testTransl(I,A,B) :- tX(A), tY(B), #count{ X,Y: inCell(I,X,Y), shape(I,X-A,Y-B) } = C1, blockCount(I,C1), index(I).
:- #count{ A: possibleXTransl(I,A) } == 0, index(I). 
:- #count{ B: possibleYTransl(I,B) } == 0, index(I).

test(I,X,Y) :- possibleXTransl(I,X), possibleYTransl(I,Y), shape(I,C,D), inCell(I,E,F), index(I), E=C+X, F=D+Y.
:- #count{ I,X,Y: test(I,X,Y) } != 1.