block(1,0,0).
block(1,0,1).
block(1,1,0).

cell(1..3, 0..9, 0..9).
index(1..3).
translation(0..9, 0..9).

% Count number of input blocks per shape.
blockCount(I,C) :- index(I), #count{ X,Y: block(I,X,Y) } = C.

% Guess.
inCell(I,X,Y) | outCell(I,X,Y) :- cell(I,X,Y).

% Check.
% ------

% Number of inCell has to coincide with input shape's blocks.
:- index(I), blockCount(I,C), #count{ X,Y: inCell(I,X,Y) } = C1, C != C1.

test(C,I) :- index(I), A=0, B=1, #count{ X,Y: inCell(I,X,Y), block(I,X-A,Y-B) } = C.
%test(C,I) :- index(I), A=1, B=1, #count{ X,Y: inCell(I,X,Y), block(I,X-A,Y-B) } = C.

:- test(X,1), X < 3.

myTest([[0,0],[0,1],[1,0]]).
myTest1(Y) :- myTest(L), &head(L;Y).