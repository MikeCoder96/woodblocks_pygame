% % Matrix cells are provided as facts.
% matrixCell(0,0).
% matrixCell(0,1).

% % Shapes are provided as elementary cells to translate
%shape(1,0,0).
%shape(1,0,1).
%shape(1,1,0).
%shape1
%shape2

% Sample input
% shape(ID, T). ID = shape's ID, T is the shape type.
shape(0,1).

% Model.
cell(0..9, 0..9).
shape(0..3).
shapeType(0..19).

% Cull guess search space
freeCell(X,Y) :- cell(X,Y), not matrixCell(X,Y).

% Guess.S
inCell(T,X,Y) | outCell(T,X,Y) :- freeCell(X,Y), shapeType(T).

% Calcolo delle celle adiacenti nella matrice - adjacentCell

% :- inCell(a, A, B), inCell(a, C,D), not adjacent(A,B,C,D).
% :- inCell(b, A, B), inCell(a,C,D), inCell(a,E,F), adjacent(A,B,C,D).

% Shape constraints

% O - O block
:- shape(_,1), inCell(1,X1,Y1), inCell(1,X2,Y2), X2 != X1 + 1, Y1 != Y2.
:- shape(_,1), #count{ T,X,Y: inCell(T,X,Y) } != 2.

%test
:- inCell(T,_,_), T != 1.
:- #count{ T,X,Y: inCell(T,X,Y) } < 1.

% % Check.

% % The number of inCell() has to match exactly the number of blocks that make up a shape.
% :- #count{ X,Y: inCell(I,X,Y) } = A, #count{ X,Y: shape(I,X,Y) } = B, A != B, index(I).

% % Placing shapes on non-empty cells is not possible.
% :- inCell(I,X,Y), matrixCell(X,Y).

% % Respect the original shapes shape (the individual matrix cells filled have to compose the same shape of the provided one)
% % The chose approach is: find two numbers, tX and tY, such that *all* the generated cells to fill are distant from the original shape provided by tX and tY.
% possibleXTransl(I,A) :- tX(A), #count{ X,Y: inCell(I,X,Y), shape(I,X-A,_) } = N1, #count{ X,Y: shape(I,X,Y) } = N2, N1 = N2, index(I).
% possibleYTransl(I,B) :- tY(B), #count{ X,Y: inCell(I,X,Y), shape(I,_,Y-B) } = N1, #count{ X,Y: shape(I,X,Y) } = N2, N1 = N2, index(I).

% :- #count{ A: possibleXTransl(I,A) } < 1, index(I). 
% :- #count{ B: possibleYTransl(I,B) } < 1, index(I).
