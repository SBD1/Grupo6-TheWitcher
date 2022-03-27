INSERT INTO Habilidade (nome, tipo) VALUES 
('Ataque Rápido', 'Combate'),
('Ataque Forte', 'Combate'), 
('Sinal Igni', 'Sinais'), 
('Sinal Axii', 'Sinais'),
('Preparação', 'Alquimia'), 
('Criação de Bomba', 'Alquimia'), 
('Instinto de Sobrevivência', 'Combat'); 

INSERT INTO Personagem (nome, gold, vida, ataque, defesa) VALUES 
('Geralt of Rivia', 0, 100, 20, 10),
('Lambert', 0, 100, 15, 15),
('Triss Merigold', 0, 100, 25, 5),
('Eskel', 0, 100, 15, 15),
('Vesemir', 0, 100, 18, 12);

INSERT INTO item (nome, tipo, descricao, preco, efeito, peso, alcance, ataque, defesa, vida) VALUES
('Cerveja', 'consumivel', NULL, 10.0, 'Cura a vida perdida em 7 pontos', 0.1, NULL, NULL, NULL, 7.0),
('Pão', 'consumivel', NULL, 6.0, 'Cura a vida perdida em 10 pontos', 0.1, NULL, NULL, NULL, 10.0),
('Arco', 'arma', NULL, 100.0, NULL, 0.4, 5.0, 23, 0, 0.0),
('Peixe', 'consumivel', NULL, 5.0, 'Cura a vida perdida em 20 pontos', 0.2, NULL, NULL, NULL, 20.0),
('Queijo', 'consumivel', NULL, 3.0, 'Cura a vida perdida em 18 pontos', 0.3, NULL, NULL, NULL, 18.0),
('Frango', 'consumivel', NULL, 4.0, 'Cura a vida perdida em 25 pontos', 0.6, NULL, NULL, NULL, 25.0),
('Uvas', 'consumivel', NULL, 3.0, 'Cura a vida perdida em 7 pontos', 0.1, NULL, NULL, NULL, 7.0),
('Carne', 'consumivel', NULL, 6.0, 'Cura a vida perdida em 30 pontos', 0.6, NULL, NULL, NULL, 30.0),
('Armadura Legendária Ursina', 'equipamento', NULL, 3348.0, NULL, 11.36, NULL, 20, 120, 100.0),
('Armadura Nilfgaardiana', 'equipamento', NULL, 1097.0, NULL, 24.3, NULL, 0, 30, 50.0),
('Armadura Thyssen', 'equipamento', NULL, 1297.0, NULL, 24.0, NULL, 10, 32, 55.0),
('Luvas de Cavaleiro', 'equipamento', NULL, 405.0, NULL, 5.48, NULL, 12, 15, 10.0),
('Luvas Nilfgaardianas', 'equipamento', NULL, 955.0, NULL, 4.88, NULL, 15, 20, 14.0),
('Luvas Griffin', 'equipamento', NULL, 214.0, NULL, 1.63, NULL, 8, 11, 7.0),
('Calças Hen Gaidth', 'equipamento', NULL, 1428.0, NULL, 17.38, NULL, 0, 20, 14.0),
('Calças Ursinas', 'equipamento', NULL, 657.0, NULL, 1.73, NULL, 0, 12, 12.0),
('Botas do Guardião', 'equipamento', NULL, 188.0, NULL, 3.22, NULL, 0, 8, 8.0),
('Botas de Capitão', 'equipamento', NULL, 192.0, NULL, 3.72, NULL, 2, 8, 10.0),
('Botas do Executor', 'equipamento', NULL, 158.0, NULL, 3.37, NULL, 0, 6, 8.0),
('Espada Iris', 'arma', 'Uma espada comum, forjada com ferro de baixa qualidade', 16.0, NULL, 2.04, 1.5, 16, 0, 13.0),
('Espada assina de bruxas', 'arma', NULL, 130.0, NULL, 2.06, 1.6, 34, 8, 20.0),
('Espada de guerreiro Wild Hunt', 'arma', NULL, 366.0, NULL, 4.25, 1.6, 58, 12, 15.0),
('Espada da ordem da rosa em chamas', 'arma', NULL, 106.0, NULL, 2.04, NULL, 30, 20, 20.0),
('Espada do caçador de bruxos', 'arma', NULL, 755.0, NULL, 2.31, NULL, 42, 27, 18.0),
('Espada Tor Lara', 'arma', NULL, 1211.0, NULL, 2.73, NULL, 70, 34, 26.0),
('Flecha com ponta de ferro', 'flecha', NULL, 10.0, NULL, 0.2, NULL, NULL, NULL, NULL),
('Flecha com ponta de prata', 'flecha', NULL, 12.0, NULL, 0.4, NULL, NULL, NULL, NULL);