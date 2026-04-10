# Adicionar tarefas 
def adicionar_tarefas(lista_tarefas,nome_tarefa):

  tarefa = {"nome": nome_tarefa, "completada":False}
  lista_tarefas.append(tarefa)
  print(f"tarefa {nome_tarefa} foi adicionada com sucesso!")
  return 

#ver lista de tarefas 

def ver_tarefas(lista_tarefas):
  print("\nLista de tarefas:\n")
  
  for indice, tarefa in enumerate(lista_tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    print(f"{indice}. [{status}] {tarefa['nome']}")
    return

#  Atualizar lista de tarefas 
def atualizar_nome_tarefa(lista_tarefas,indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1 
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(lista_tarefas):
    lista_tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa 
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
  else:
    print("indice de tarefa invalido.")
  return 

lista_tarefas = []

while True:
  print("\n Menu do gerenciador lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. ver tarefas")
  print("3. Atualizar tarefas")
  print("4. Completar tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha:")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:")
    adicionar_tarefas(lista_tarefas,nome_tarefa)
  elif escolha == "2":
     ver_tarefas(lista_tarefas)
  elif escolha == "3":
    ver_tarefas(lista_tarefas)
    indice_tarefa = input("Digite o numero da tarefa que vocÊ deseja atualizar:")
    novo_nome_tarefa = input("Digite o novo nome da tarefa:")
    atualizar_nome_tarefa(lista_tarefas,indice_tarefa, novo_nome_tarefa)
  elif escolha == "6":
    break

print("Programa finalizado")
