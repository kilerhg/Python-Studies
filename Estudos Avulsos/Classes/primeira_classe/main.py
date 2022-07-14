from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('111.222.333-44', nome='teste', idade=10)

print(a.getCPF())
print(a.getNome())
print(a.getIdade())

b = PessoaJuridica('11.222.3333/0001-99', nome='teste', idade=10)

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())