% Python input facts:
% matrixCell(X,Y), represents an occupied matrix cell
% shape(ID,T), represents a shape to place. ID: identifies the shape, T: identifies the shape type (0..19).

% Model
cell(0..9,0..9).
shapeType(0..18).

% Guess + initial culling on already occupied matrix cells
inCell(ID,T,X,Y) | outCell(T,X,Y) :- shape(ID,T), cell(X,Y), not matrixCell(X,Y).

% X/Y Adjacency
adjX(ID,X1,Y1,X2,Y2) :- inCell(ID,_,X1,Y1), inCell(ID,_,X2,Y2), X2 = X1 + 1, Y1 = Y2.
adjY(ID,X1,Y1,X2,Y2) :- inCell(ID,_,X1,Y1), inCell(ID,_,X2,Y2), Y2 = Y1 + 1, X1 = X2.
% Right X-adjacency. (A cell is considered right-adjacent if it's immediately to the x-right of the target (X2,Y2) cell)
adjXR(ID,X1,Y1,X2,Y2) :- inCell(ID,_,X1,Y1), inCell(ID,_,X2,Y2), X1 = X2 + 1, Y1 = Y2.

% ----------------------------------
% Shape type 0: O
:- shape(ID,0), #count{ X,Y: inCell(ID,0,X,Y) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 1: OO
:- shape(ID,1), #count{ X,Y: inCell(ID,1,X,Y) } != 2.
s1(X1,X2) :- shape(ID,1), inCell(ID,1,X1,Y1), inCell(ID,1,X2,Y2), adjX(ID,X1,Y1,X2,Y2).
:- shape(ID,1), #count{ X1,X2: s1(X1,X2) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 2: O
%				O
:- shape(ID,2), #count{ X,Y: inCell(ID,2,X,Y) } != 2.
s2(X1,X2) :- shape(ID,2), inCell(ID,2,X1,Y1), inCell(ID,2,X2,Y2), adjY(ID,X1,Y1,X2,Y2).
:- shape(ID,2), #count{ X1,X2: s2(X1,X2) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 3: OOO
:- shape(ID,3), #count{ X,Y: inCell(ID,3,X,Y) } != 3.
s3(X1,X2,X3) :- shape(ID,3), inCell(ID,3,X1,Y1), inCell(ID,3,X2,Y2), inCell(ID,3,X3,Y3), adjX(ID,X1,Y1,X2,Y2), adjX(ID,X2,Y2,X3,Y3).
:- shape(ID,3), #count{ X1,X2,X3: s3(X1,X2,X3) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 4: O
%				O
%				O
% ----------------------------------
:- shape(ID,4), #count{ X,Y: inCell(ID,4,X,Y) } != 3.
s4(X1,X2,X3) :- shape(ID,4), inCell(ID,4,X1,Y1), inCell(ID,4,X2,Y2), inCell(ID,4,X3,Y3), adjY(ID,X1,Y1,X2,Y2), adjY(ID,X2,Y2,X3,Y3).
:- shape(ID,4), #count{ X1,X2,X3: s4(X1,X2,X3) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 5: OO
%				 O
:- shape(ID,5), #count{ X,Y: inCell(ID,5,X,Y) } != 3.
s5(X1,X2,X3) :- shape(ID,5), inCell(ID,5,X1,Y1), inCell(ID,5,X2,Y2), inCell(ID,5,X3,Y3), adjX(ID,X1,Y1,X2,Y2), adjY(ID,X2,Y2,X3,Y3).
:- shape(ID,5), #count{ X1,X2,X3: s5(X1,X2,X3) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 6: OO
%				O
:- shape(ID,6), #count{ X,Y: inCell(ID,6,X,Y) } != 3.

% To ask. Negative constraint does not work. Building facts and constraining their count works. Why.
%:- shape(ID,3), inCell(ID,3,X1,Y1), inCell(ID,3,X2,Y2), inCell(ID,3,X3,Y3), ID != 0, not adjX(ID,X1,Y1,X2,Y2), not adjY(ID,X1,Y1,X3,Y3).
s6(X1,X2,X3) :- shape(ID,6), inCell(ID,6,X1,Y1), inCell(ID,6,X2,Y2), inCell(ID,6,X3,Y3), adjX(ID,X1,Y1,X2,Y2), adjY(ID,X1,Y1,X3,Y3).
:- shape(ID,6), #count{ A,B,C: s6(A,B,C) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 7: O
%				OO
:- shape(ID,7), #count{ X,Y: inCell(ID,7,X,Y) } != 3.
s7(X1,X2,X3) :- shape(ID,7), inCell(ID,7,X1,Y1), inCell(ID,7,X2,Y2), inCell(ID,7,X3,Y3), adjY(ID,X1,Y1,X2,Y2), adjX(ID,X2,Y2,X3,Y3).
:- shape(ID,7), #count{ X1,X2,X3: s7(X1,X2,X3) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 8:  O
%				OO
:- shape(ID,8), #count{ X,Y: inCell(ID,8,X,Y) } != 3.
s8(X1,X2,X3) :- shape(ID,8), inCell(ID,8,X1,Y1), inCell(ID,8,X2,Y2), inCell(ID,8,X3,Y3), adjY(ID,X1,Y1,X2,Y2), adjXR(ID,X2,Y2,X3,Y3).
:- shape(ID,8), #count{ X1,X2,X3: s8(X1,X2,X3) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 9:  OOOO
:- shape(ID,9), #count{ X,Y: inCell(ID,9,X,Y) } != 4.
s9(X1,X2,X3,X4) :- 	shape(ID,9), 
					inCell(ID,9,X1,Y1), 
					inCell(ID,9,X2,Y2), 
					inCell(ID,9,X3,Y3), 
					inCell(ID,9,X4,Y4), 
					adjX(ID,X1,Y1,X2,Y2), 
					adjX(ID,X2,Y2,X3,Y3), 
					adjX(ID,X3,Y3,X4,Y4).
:- shape(ID,9), #count{ X1,X2,X3,X4: s9(X1,X2,X3,X4) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 10:  	O
%					O
%					O
%					O
:- shape(ID,10), #count{ X,Y: inCell(ID,10,X,Y) } != 4.
s10(X1,X2,X3,X4) :- shape(ID,10), 
					inCell(ID,10,X1,Y1), 
					inCell(ID,10,X2,Y2), 
					inCell(ID,10,X3,Y3), 
					inCell(ID,10,X4,Y4), 
					adjY(ID,X1,Y1,X2,Y2), 
					adjY(ID,X2,Y2,X3,Y3), 
					adjY(ID,X3,Y3,X4,Y4).
:- shape(ID,10), #count{ X1,X2,X3,X4: s10(X1,X2,X3,X4) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 11:	OO
%					OO
:- shape(ID,11), #count{ X,Y: inCell(ID,11,X,Y) } != 4.
s11(X1,X2,X3,X4) :- shape(ID,11), 
					inCell(ID,11,X1,Y1), 
					inCell(ID,11,X2,Y2), 
					inCell(ID,11,X3,Y3), 
					inCell(ID,11,X4,Y4), 
					adjX(ID,X1,Y1,X2,Y2), 
					adjX(ID,X3,Y3,X4,Y4), 
					adjY(ID,X1,Y1,X3,Y3), 
					adjY(ID,X2,Y2,X4,Y4).
:- shape(ID,11), #count{ X1,X2,X3,X4: s11(X1,X2,X3,X4) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 12: OOOOO
:- shape(ID,12), #count{ X,Y: inCell(ID,12,X,Y) } != 5.
s12(X1,X2,X3,X4,X5) :- 	shape(ID,12),
						inCell(ID,12,X1,Y1),
						inCell(ID,12,X2,Y2),
						inCell(ID,12,X3,Y3),
						inCell(ID,12,X4,Y4),
						inCell(ID,12,X5,Y5),
						adjX(ID,X1,Y1,X2,Y2),
						adjX(ID,X2,Y2,X3,Y3),
						adjX(ID,X3,Y3,X4,Y4),
						adjX(ID,X4,Y4,X5,Y5).
:- shape(ID,12), #count{ X1,X2,X3,X4,X5: s12(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 13: vertical x5
:- shape(ID,13), #count{ X,Y: inCell(ID,13,X,Y) } != 5.
s13(X1,X2,X3,X4,X5) :- 	shape(ID,13),
						inCell(ID,13,X1,Y1),
						inCell(ID,13,X2,X2),
						inCell(ID,13,X3,Y3),
						inCell(ID,13,X4,Y5),
						inCell(ID,13,X5,Y5),
						adjY(ID,X1,Y1,X2,Y2),
						adjY(ID,X2,Y2,X3,Y3),
						adjY(ID,X3,Y3,X4,Y4),
						adjY(ID,X4,Y4,X5,Y5).
:- shape(ID,13), #count{ X1,X2,X3,X4,X5: s13(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 14: 	O
%					O
%					O O O
:- shape(ID,14), #count{ X,Y: inCell(ID,14,X,Y) } != 5.
s14(X1,X2,X3,X4,X5) :- 	shape(ID,14),
						inCell(ID,14,X1,Y1),
						inCell(ID,14,X2,Y2),
						inCell(ID,14,X3,Y3),
						inCell(ID,14,X4,Y4),
						inCell(ID,14,X5,Y5),
						adjY(ID,X1,Y1,X2,Y2),
						adjY(ID,X2,Y2,X3,Y3),
						adjX(ID,X3,Y3,X4,Y4),
						adjX(ID,X4,Y4,X5,Y5).
:- shape(ID,14), #count{ X1,X2,X3,X4,X5: s14(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 15:	O O O
%					O
%					O
:- shape(ID,15), #count{ X,Y: inCell(ID,15,X,Y) } != 5.
s15(X1,X2,X3,X4,X5) :- 	shape(ID,15),
						inCell(ID,15,X1,Y1),
						inCell(ID,15,X2,Y2),
						inCell(ID,15,X3,Y3),
						inCell(ID,15,X4,Y4),
						inCell(ID,15,X5,Y5),
						adjX(ID,X1,Y1,X2,Y2),
						adjX(ID,X2,Y2,X3,Y3),
						adjY(ID,X1,Y1,X4,Y4),
						adjY(ID,X4,Y4,X5,Y5).
:- shape(ID,15), #count{ X1,X2,X3,X4,X5: s15(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 16: 	    O
%					    O
%					O O O
:- shape(ID,16), #count{ X,Y: inCell(ID,16,X,Y) } != 5.
s16(X1,X2,X3,X4,X5) :- 	shape(ID,16),
						inCell(ID,16,X1,Y1),
						inCell(ID,16,X2,Y2),
						inCell(ID,16,X3,Y3),
						inCell(ID,16,X4,Y4),
						inCell(ID,16,X5,Y5),
						adjY(ID,X1,Y1,X2,Y2),
						adjY(ID,X2,Y2,X3,Y3),
						adjXR(ID,X3,Y3,X4,Y4),
						adjXR(ID,X4,Y4,X5,Y5).
:- shape(ID,16), #count{ X1,X2,X3,X4,X5: s16(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 17: 	O O O
%					    O
%						O
:- shape(ID,17), #count{ X,Y: inCell(ID,17,X,Y) } != 5.
s17(X1,X2,X3,X4,X5) :- 	shape(ID,17),
						inCell(ID,17,X1,Y1),
						inCell(ID,17,X2,Y2),
						inCell(ID,17,X3,Y3),
						inCell(ID,17,X4,Y4),
						inCell(ID,17,X5,Y5),
						adjX(ID,X1,Y1,X2,Y2),
						adjX(ID,X2,Y2,X3,Y3),
						adjY(ID,X3,Y3,X4,Y4),
						adjY(ID,X4,Y4,X5,Y5).
:- shape(ID,17), #count{ X1,X2,X3,X4,X5: s17(X1,X2,X3,X4,X5) } != 1.
% ----------------------------------

% ----------------------------------
% Shape type 18: 	O O O
%					O O O
%					O O O
:- shape(ID,18), #count{ X,Y: inCell(ID,18,X,Y) } != 9.
s18(X1,X2,X3,X4,X5,X6,X7,X8,X9) :- 	shape(ID,18),
									inCell(ID,18,X1,Y1),
									inCell(ID,18,X2,Y2),
									inCell(ID,18,X3,Y3),
									inCell(ID,18,X4,Y4),
									inCell(ID,18,X5,X5),
									inCell(ID,18,X6,Y6),
									inCell(ID,18,X7,Y7),
									inCell(ID,18,X8,Y8),
									inCell(ID,18,X9,Y9),
									adjX(ID,X1,Y1,X2,Y2),
									adjX(ID,X2,Y2,X3,Y3),
									adjX(ID,X4,Y4,X5,Y5),
									adjX(ID,X5,Y5,X6,Y6),
									adjX(ID,X7,Y7,X8,Y8),
									adjX(ID,X8,Y8,X9,Y9),
									adjY(ID,X1,Y1,X4,Y4),
									adjY(ID,X4,Y4,X7,Y7),
									adjY(ID,X2,Y2,X5,Y5),
									adjY(ID,X5,Y5,X8,Y8),
									adjY(ID,X3,Y3,X6,Y6),
									adjY(ID,X6,Y6,X9,Y9).
:- shape(ID,18), #count{ X1,X2,X3,X4,X5,X6,X7,X8,X9: s18(X1,X2,X3,X4,X5,X6,X7,X8,X9) } != 1.
% ----------------------------------

% Test facts
shape(0,5).
shape(1,10).
shape(2,18).