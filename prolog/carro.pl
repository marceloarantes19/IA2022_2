carro:-not(car).

car:-dynamic(conheco/2),
       not(oProblemaE(vela)),
       not(oProblemaE(bateria)),
       not(oProblemaE(motorDePartida)),
       write("Nao achei o problema."), fim.

oProblemaE(vela):-motorRecebeCombustivel,
                  pergunta("O motor tenta pegar"),
                  write("O problema e vela!"), fim.

oProblemaE(bateria):-not(pergunta("O motor tenta pegar")),
                     not(pergunta("As luzes acendem")),
                     write("O problema e bateria ou cabo!"),
                     fim.

oProblemaE(motorDePartida):-
                  not(pergunta("O motor tenta pegar")),
                  pergunta("As luzes acendem"),
                  write("O problema e o motor de partida"),
                  fim.

motorRecebeCombustivel:-
                pergunta("Ha combistivel no tanque"),
                pergunta("Ha combustivel no carburador").

pergunta(X):-conheco(X, sim).
pergunta(X):-conheco(X, _), !, false.
pergunta(X):-write(X), write("? "), read(Resp),
             assertz(conheco(X, Resp)),
             Resp == sim.

fim:-retractall(conheco(_, _)).