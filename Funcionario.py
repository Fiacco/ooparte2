class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self,horas):
        print("Horas registradas")

    def mostrar_taferas(self):
        print('fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_taferas(self):
        print('fez muita coisa Caleumer')

    def buscar_cursos_do_mes(self, mes= None):
        print(f'Mostrando cursos - {mes}' if mes else 'mostrando cursos desse mes')

class Alura(Funcionario):
     def mostrar_tarefas(self):
       print('Fez muita coisa, Alurete!')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

    def buscar_perguntas_sem_respostas(self):
        print('mostrando perguntas não respondidas do forum')

class Junior(Alura):
    pass

class Senior(Alura, Caelum):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass


Jose = Junior ()
Jose.buscar_perguntas_sem_respostas()

Luan = Pleno ()
Luan.buscar_perguntas_sem_respostas()
Luan.buscar_cursos_do_mes()

Luan.mostrar_taferas()

print(Luan)