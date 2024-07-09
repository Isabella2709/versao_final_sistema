import json

def salvar_dados_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print(f'Dados salvos em {nome_arquivo}')


def recuperar_dados_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    print(f'Dados recuperados de {nome_arquivo}')
    return dados



estudantes_lista = [
    {"codigo": 4572,"nome": "luana", "cpf": "966541531"},
    {"codigo": 4578,"nome": "joão", "cpf": "458925318"},
    {"codigo": 4574,"nome": "lucas", "cpf": "21441531"},

                        ]

estudantes_lista = json.loads(estudantes_lista)

salvar_dados_json(estudantes_lista, 'estudantes.json')
recuperar_dados_json(estudantes_lista)

disciplinas_lista = [
    {"nome": "comunicacao aplicada", "professor": "maria", "codigo": 8965214},
    {"nome": "pensamente computacional", "professor": "carlos", "codigo": 5698742},
    {"nome": "emprendedorismo e inovacao", "professor": "catia", "codigo": 865231}

                         ]

disciplinas_lista = json.loads(disciplinas_lista)

salvar_dados_json(disciplinas_lista, 'disciplinas.json')
recuperar_dados_json(disciplinas_lista)


professores_lista = [
   {"nome": "luiz", "materia": "comunicacao aplicada", "codigo": 963214},
   {"nome": "joana dark", "materia": "ed fisica", "codigo": 569874},
   {"nome": "luana", "materia": "matematica", "codigo": 695412}
                        ]

professores_lista = json.loads(professores_lista)

salvar_dados_json(professores_lista, 'professores.json')
recuperar_dados_json(professores_lista)


turmas_lista = [
   {"nome": "primeira", "curso": "big data", "codigo": 632142},
   {"nome": "segunda", "curso": "desenvolvimento de sistemas", "codigo": 632578 },
   {"nome": "terceira", "curso": "inteligencia aritificial", "codigo": 698741}
]

turmas_lista = json.loads(turmas_lista)

salvar_dados_json(turmas_lista, 'turmas.json')
recuperar_dados_json(estudantes_lista)


matriculas_lista = [
   {"estudante": "luan", "curso": "desenvolvimento de sistemas", "codigo": 624157},
   {"estudante": "lucas", "curso": "desenvolvimento de sistemas", "codigo": 624158},
   {"estudante": "carla", "curso": "desenvolvimento de sistemas", "codigo": 624523}
   
                        ]

matriculas_lista = json.loads(matriculas_lista)
salvar_dados_json(matriculas_lista, 'matriculas.json')
recuperar_dados_json(matriculas_lista)

print("Bem vindo ao sistema academico:")
print("================================")

operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
operacao = operacao.upper()



if(operacao != "N" and operacao != "S"):
  print("Opção invalida")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
  operacao = operacao.upper()

operacao = operacao.upper()


while(operacao == "S"):

  escolha_menu = int(input("Bem vindo ao menu principal, por favor escolha a opção desejada: \n 1. Estudantes \n 2. Disciplinas \n 3. Professores \n 4. Turmas \n 5. Matriculas \n 6. Sair \n"))

  if(escolha_menu == 1):
   escolha_pergunta = int(input("====== [ESTUDANTES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   if(escolha_pergunta == 1):

     codigo_estudante = str(input("Digite o codigo de 4 digitos do estudante: "))
     nome_estudante = str(input("Digite o nome do estudante que voce deseja inserir: "))
     cpf_estudante = str(input("Digite o cpf de 9 digitos do estudante "))
     estudantes_lista.append({"codigo": codigo_estudante, "nome": nome_estudante, "cpf": cpf_estudante})

     print("Estudante adicionado com sucesso")
   elif(escolha_pergunta == 2):

    for estudante in estudantes_lista:
                print(estudante)

   elif(escolha_pergunta == 3):
    atualizar_estudante = str(input("Digite qual o nome do estudante que você quer alterar: "))
    for estudante in estudantes_lista:
        if(estudante["nome"] == atualizar_estudante):
            nome_estudante = str(input("Digite o nome do estudante que você deseja inserir: "))
            cpf_estudante = str(input("Digite o CPF de 9 dígitos do estudante: "))
            estudante.update({"nome": nome_estudante, "cpf": cpf_estudante})
            print("Estudante atualizado com sucesso")
            break
    else:
        print("Estudante não encontrado.")

   elif(escolha_pergunta == 4):
    remover_estudante = int(input("Digite o código do estudante que você quer remover: "))
    nova_lista = [estudante for estudante in estudantes_lista if estudante["codigo"] != remover_estudante]
    if len(nova_lista) != len(estudantes_lista):
        estudantes_lista[:] = nova_lista
        print("Estudante removido com sucesso")
    else:
        print("Estudante não encontrado.")


   elif(escolha_pergunta == 5):
    print("Voltando ao menu inicial")



  elif(escolha_menu == 2):
   escolha_menu_disciplina = int(input("====== [DISCIPLINAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))

   if escolha_menu_disciplina == 1:
    nome_disciplina = str(input("Digite o nome da disciplina que você quer adicionar: "))
    professor_disciplina = str(input("Digite o nome do professor dessa disciplina: "))
    codigo_disciplina = int(input("Digite o numero da disciplina: "))
    disciplinas_lista.append({"nome": nome_disciplina, "professor": professor_disciplina, "codigo_disciplina": codigo_disciplina})

   elif escolha_menu_disciplina == 2:
      for disc in disciplinas_lista:
        print(disc)

   elif(escolha_menu_disciplina == 3):
      atualizar_disciplina = input("Digite o nome da disciplina que você quer alterar: ")
      for disc in disciplinas_lista:
         if disc["nome"] == atualizar_disciplina:
             nome_disc_atualizacao = input("Digite o novo nome da disciplina: ")
             prof_disci_atualizacao = input("Digite o nome do professor atualizado: ")
             disc.update({"nome": nome_disc_atualizacao, "professor": prof_disci_atualizacao})
             print("Disciplina atualizada com sucesso")
             break

   elif escolha_menu_disciplina == 4:
    remover_disciplina = int(input("Digite o código da disciplina que você quer remover: "))
    disciplina_encontrada = False


    for disciplina in disciplinas_lista:
        if disciplina["codigo"] == remover_disciplina:
            disciplinas_lista.remove(disciplina)
            disciplina_encontrada = True
            print("Disciplina removida com sucesso")
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada")

  elif escolha_menu_disciplina == 5:
     print("Retornando ao menu inicial")






  elif(escolha_menu == 3):
   escolha_menu_professores = int(input("====== [PROFESSORES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   
   if escolha_menu_professores == 1:
    nome_professor = str(input("Digite o nome da disciplina que você quer adicionar: "))
    professor_materia = str(input("Digite o nome do professor dessa disciplina: "))
    codigo_disciplina = int(input("Digite o numero da disciplina: "))
    professores_lista.append({"nome": nome_professor, "materia": professor_materia, "codigo": codigo_disciplina})

   elif escolha_menu_professores== 2:
      for disc in professores_lista:
        print(disc)

   elif(escolha_menu_professores == 3):
      atualizar_professor = input("Digite o nome do professor que você quer alterar: ")
      for disc in professores_lista:
         if disc["nome"] == professores_lista:
             nome_disc_atualizacao = input("Digite o novo nome do professor: ")
             prof_disci_atualizacao = input("Digite o nome da materia atualizada: ")
             disc.update({"nome": nome_disc_atualizacao, "materia": prof_disci_atualizacao})
             print("professor atualizado com sucesso")
             break

   elif escolha_menu_professores == 4:
    remover_professor = int(input("Digite o código do professor que você quer remover: "))
    prof_encontrado = False


    for prof in professores_lista:
        if prof["codigo"] == remover_professor:
            professores_lista.remove(prof)
            prof_encontrado = True
            print("professor removido com sucesso")
            break

    if not prof_encontrado:
        print("Disciplina não encontrada")

  elif escolha_menu_professores == 5:
     print("Retornando ao menu inicial")

 

  elif(escolha_menu == 4):
   
   escolha_menu_turmas = int(input("====== [TURMAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   
   if escolha_menu_turmas == 1:
    nome_turma = str(input("Digite o nome da turma que você quer adicionar: "))
    curso_turma = str(input("Digite o nome do curso dessa disciplina: "))
    codigo_turma = int(input("Digite o numero da disciplina: "))
    turmas_lista.append({"nome": nome_turma, "materia": curso_turma, "codigo": codigo_turma})

   elif escolha_menu_turmas == 2:
      for disc in turmas_lista:
        print(disc)

   elif(escolha_menu_turmas == 3):
      atualizar_turma = input("Digite o nome da turma que você quer alterar: ")
      for disc in turmas_lista:
         if disc["nome"] == turmas_lista:
             nome_turma_atualizacao = input("Digite o novo nome da turma: ")
             curso_turma_atualizacao = input("Digite o nome do curso atualizada: ")
             disc.update({"nome": nome_turma_atualizacao, "materia": curso_turma_atualizacao})
             print("professor atualizado com sucesso")
             break

   elif escolha_menu_turmas == 4:
    remover_turma = int(input("Digite o código do professor que você quer remover: "))
    turma_encontrada = False


    for turma in turmas_lista:
        if turma["codigo"] == remover_turma:
            turmas_lista.remove(prof)
            turma_encontrada = True
            print("turma removida com sucesso")
            break

    if not turma_encontrada:
        print("Turma não encontrada")

  elif escolha_menu_turmas == 5:
     print("Retornando ao menu inicial")



  elif(escolha_menu == 5):
   escolha_menu_matriculas = int(input("====== [MATRICULAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
  
   if escolha_menu_matriculas == 1:
    nome_estudante = str(input("Digite o nome do estudante que você quer adicionar: "))
    curso_matricula = str(input("Digite o nome do curso dessa disciplina: "))
    codigo_matricula = int(input("Digite o numero da disciplina: "))
    matriculas_lista.append({"nome": nome_estudante, "curso": curso_turma, "codigo": codigo_matricula})

   elif escolha_menu_matriculas == 2:
      for disc in matriculas_lista:
        print(disc)

   elif(escolha_menu_matriculas == 3):
      atualizar_matricula = input("Digite o nome da turma que você quer alterar: ")
      for disc in matriculas_lista:
         if disc["estudante"] == turmas_lista:
             nome_estudante_atualizacao = input("Digite o novo nome do estudante: ")
             curso_atualizacao = input("Digite o nome do curso atualizada: ")
             disc.update({"nome": nome_estudante_atualizacao, "materia": curso_atualizacao})
             print("Matricula atualizada com sucesso")
             break

   elif escolha_menu_matriculas == 4:
    remover_mat = int(input("Digite o código da matricula que você quer remover: "))
    matricula_encontrada = False


    for mat in matriculas_lista:
        if mat["codigo"] == remover_mat:
            matriculas_lista.remove(mat)
            matricula_encontrada = True
            print("Matricula removida com sucesso")
            break

    if not matricula_encontrada:
        print("Turma não encontrada")

  elif escolha_menu_matriculas == 5:
     print("Retornando ao menu inicial")

  
  
  
  elif(escolha_menu == 6):
   print("Obrigada por ultilizar nosso sistema, esperamos te ver em breve.")
  else:
   print("Opção invalida, por favor informe um numero valido, você sera direcionado para o menu inicial.")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações e N para sair): "))
  operacao = operacao.upper()

  if(operacao == "N"):
   print("Bem vindo de volta ao menu do sistema academico")
   operacao = str(input("Deseja começar a fazer operações novamente? (S - Fazer operações e N para sair): "))
   operacao = operacao.upper()