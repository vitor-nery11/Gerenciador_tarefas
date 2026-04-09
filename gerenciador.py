def adicionar_tarefas(lista_tarefas,nome_tarefa):

#tarefa: vai armazenar o nome da tarefa
#completa: vai indicar se tarefa foi completada
  tarefa = {"nome": nome_tarefa, "completada":False}
  lista_tarefas.append(tarefa)
  print(f"tarefa {nome_tarefa} foi adicionada com sucesso!")
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
  elif escolha == "6":
    break

print("Programa finalizado")