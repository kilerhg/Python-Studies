def criar_emails_acadamicos(alunos):
    lista_email_alunos = []
    alunos_clean = list(map(str.strip, alunos.lower().split(',')))
    for aluno in alunos_clean:
        nome_aluno_separado = aluno.split()
        lista_nome_limpo = []
        for nome in nome_aluno_separado:
            if not nome in ['de', 'da', 'das', 'do', 'dos']:
                lista_nome_limpo.append(nome)
        email = f"{'.'.join(lista_nome_limpo)}@academico.ufgd.edu.br"
        tupla_nome_email = (nome_aluno_separado[0], email)
        lista_email_alunos.append(tupla_nome_email)
    return lista_email_alunos
