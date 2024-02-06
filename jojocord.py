import random

class Ataque:
    """Classe que representa o ataque de um Stand"""
    def __init__(self, dano, nome, stars):
        self.dano = dano   # % do AP usado pelo ataque
        self.nome = nome   # Nome do ataque
        self.stars = stars # Nível de raridade do ataque (1-6)

    def to_string(self, ap):
        return f"""* {self.nome} ({"★" * self.stars})
        Dano: {ap * self.dano / 100}"""

class Stand:
    """Classe que representa a instância de um stand"""
    def __init__(self, ap, ataques, cp, desc, dp, hp, lvl, nome, stars, sp, xp):
        self.ap = ap           # Attack points
        self.ataques = ataques # Lista de ataques
        self.cp = cp           # Critical points (0-100%)
        self.desc = desc       # Descrição do Stand
        self.dp = dp           # Defense points
        self.hp = hp           # Health points
        self.lvl = lvl         # Level do Stand
        self.nome = nome       # Nome do Stand
        self.stars = stars     # Nível de raridade do Stand (1-6)
        self.sp = sp           # Speed points
        self.xp = xp           # Experience points

    def to_string(self):
        ataques = ""
        for a in self.ataques:
            ataques += a.to_string(self.ap) + "\n\n"

        return f"""
**Stand:** {self.nome} ({"★" * self.stars})

    *"{self.desc}"*

Ataque: {self.ap}
Ataque crítico: {self.cp}%
Defesa: {self.dp}
Hp: {self.hp}
Lvl: {self.lvl}
Velocidade: {self.sp}

**Ataques:**\n""" + ataques

class User:
    """Classe que representa um usuário"""
    def __init__(self, stands, username):
        self.stands = stands     # Lista de Stands do usuário
        self.username = username
    
    # Permite que o usuário consiga seu 1º Stand
    def get_1st_stand(self):
        self.stands.append(random.choice(stands_iniciais))


# Lista com todos os stands iniciais
stands_iniciais = [
    Stand(
        random.randrange(57, 60, 1),
        [
            Ataque(100, "Ora Ora!", 3)
        ],
        2,
        """Star Platinum é um Stand de curto alcance com força e velocidade
        excepcionais, além de ganhar a habilidade de parar o tempo durante a luta
        contra DIO. Seu poder avassalador, aliado às proezas de luta de Jotaro,
        fazem dele um dos Stands mais fortes e icônicos da série.""",
        random.randrange(37, 40, 1),
        random.randrange(38, 42),
        5,
        "Star Platinum",
        5,
        random.randrange(47, 50),
        0
    )
]

