# Anotações Regex

## Sumario

## O que é REGEX?

Regex é uma tecnologia integrada em simplesmente todas as linguagens para encontrar padrões em texto.

## Para que serve

A utiliza é diversa, sendo ampla em validações. cpf, cnpj, numero de telefone & etc.

## Como/Onde utilizar

Em geral cada linguagem tem um suporte unico para o regex & tambem editores de texto, porém o codigo regex em si não muda.

## Anotações

### Caracteres Iniciais Regex

```regex
^ - Inicio linha
$ - Fim linha
. - Qualquer Caracter que não seja fim linha
\n - Quebra Linha
```

### Basico

```regex
[a] - Encontra único caracter
[0] - Encontra único caracter

[ab] - Encontra um ou outro caracter, em ordem que achar primeiro
[a-b] - Procura entre a & b
[a-zA-Z] - Procura todos as letras do alfabeto, minusculo ou maiusculo
[0-9] - Procura todos os numeros
```

### Multiplicando Padrões

```regex
{2} - Multiplica a sequencia regex aplicada anteriormente.
Exemplo 
```

### Meta-Caracteres

```regex
\d - qualquer Caracter numerico
\D - Qualquer caracter não numerico (sem contar fim linha)

\s - Qualquer caracter espaco em braco
\S - Qualquer caracter Não espaco em braco
```