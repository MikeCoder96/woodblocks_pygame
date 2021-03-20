% % Matrix cells are provided as facts.
% matrixCell(0,0).
% matrixCell(0,1).

% % Shapes are provided as elementary cells to translate
% shape1(0,0).
% shape1(0,1).
% shape1(0,2).

% Model.
cell(1..3, 0..4, 0..4).

index(1..3).

% Translation point used to check for shape consistency.
tX(0..4).
tY(0..4).

% Guess.
inCell(I,X,Y) | outCell(I,X,Y) :- cell(I,X,Y).

% Check.

% The number of inCell() has to match exactly the number of blocks that make up a shape.
:- #count{ X,Y: inCell(I,X,Y) } = A, #count{ X,Y: shape(I,X,Y) } = B, A != B, index(I).

% Placing shapes on non-empty cells is not possible.
:- inCell(I,X,Y), matrixCell(X,Y).

% Respect the original shape's shape (the individual matrix cells filled have to compose the same shape of the provided one)
% The chose approach is: find two numbers, tX and tY, such that *all* the generated cells to fill are distant from the original shape provided by tX and tY.
possibleXTransl(I,A) :- tX(A), #count{ X,Y: inCell(I,X,Y), shape(I,X-A,_) } = N1, #count{ X,Y: shape(I,X,Y) } = N2, N1 = N2, index(I).
possibleYTransl(I,B) :- tY(B), #count{ X,Y: inCell(I,X,Y), shape(I,_,Y-B) } = N1, #count{ X,Y: shape(I,X,Y) } = N2, N1 = N2, index(I).

:- #count{ A: possibleXTransl(I,A) } < 1, index(I). 
:- #count{ B: possibleYTransl(I,B) } < 1, index(I).