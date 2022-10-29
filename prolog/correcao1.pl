tipoTri:-write("Digite o valor do lado A: "), read(A),
         write("Digite o valor do lado B: "), read(B),
         write("Digite o valor do lado C: "), read(C),
         eTriangulo(A, B, C),
         tipoTriangulo(A, B, C).

eTriangulo(A, B, C):-A < B + C, B < C + A, C < A + B.
eTriangulo(_, _, _):-write("Nao e triangulo!"), !, fail.

tipoTriangulo(A, A, A):-write("Equilatero.").
tipoTriangulo(A, A, _):-write("Isosceles.").
tipoTriangulo(A, _, A):-write("Isosceles.").
tipoTriangulo(_, A, A):-write("Isosceles.").
tipoTriangulo(_, _, _):-write("Escaleno.").

eq2g:-write("Digite o valor do lado A: "), read(A),
      write("Digite o valor do lado B: "), read(B),
      write("Digite o valor do lado C: "), read(C),
      verificarEq2g(A),
      delta(A, B, C, D),
      write("Delta: "), write(D),
      x1(A, B, D).


verificarEq2g(0):-write("Nao e Eq do segundo grau"), fail.
verificarEq2g(_).

delta(A, B, C, D):-write("xxxx"), D is B ^ 2 - 4 * A * C, write(D).
x1(_, _, D):-D < 0, write("Nao tem raiz.").
x1(A, B, D):-R is (- B + sqrt(D)) / 2 * A,
             write("X1 = "), write(R),
             x2(A, B, D).
x2(_, _, 0).
x2(A, B, D):-R is (- B - sqrt(D)) / 2 * A,
             write("X2 = "), write(R).

pot(X, 0, 1).
pot(X, Y, Z):-Y1 is Y - 1, pot(X, Y1, Z1), Z is X * Z1.

fib(1, 1).
fib(2, 1).
fib(N, W):-N1 is N - 1, N2 is N - 2,
           fib(N1, R1), fib(N2, R2),
           W is R1 + R2.