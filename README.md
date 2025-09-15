Esse programa em Python implementa um Sistema de Controle de Estoque para uma distribuidora de papelaria: 
- Ele começa com um dicionário (estoque_atual) contendo pelo menos 8 produtos e suas quantidades iniciais;
- Em seguida processa uma lista de movimentações (movimentacoes_dia) com pelo menos 15 registros de entrada ou saída de itens;
- Para cada movimentação, se for entrada, soma a quantidade ao estoque, se for saída, subtrai, e se for um produto novo, adiciona automaticamente ao dicionário;
- Ao final, o sistema identifica todos os produtos que estão com quantidade menor ou igual a 50 unidades, considerados em “nível baixo”;
- Gera um relatório no console mostrando o estoque atualizado e, em uma seção separada, a lista dos produtos que precisam de reposição, garantindo uma visão clara da situação após as movimentações.
