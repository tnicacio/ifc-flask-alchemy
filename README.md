# Python - Flask - SqlAlchemy

> Backend implementado em Python para a disciplina de Desenvolvimento de Sistemas em Python_ do IFC Campus Blumenau.

## Diagrama de classes
As classes modeladas foram: **Pessoa**(nome, cpf, email), **Disciplina**(nome, carga horária, ementa) e **EstudanteDaDisciplina**(semestre, pessoa, disciplina, mediaFinal, frequencia).

O nome da entidade EstudanteDaDisciplina foi modificado para _Student_, e ela possui relacionamentos Many-To-One tanto com a entidade Pessoa (_Person_), quanto com a entidade Disciplina (_Subject_). Ambos são relacionamentos de composição em que o _Student_ não existe sem uma pessoa ou disciplina. Dessa forma, os campos **person** e **subject** da entidade *Student* são obrigatórios; i.e., não podem ser nulos.

![diagrama-classes-ped](https://user-images.githubusercontent.com/50798315/147425974-51eeab06-8b44-42a0-8023-b2edf22572d9.png)

## Para testar

### Instalar as dependências
```python -m pip install -r requirements.txt```

### Iniciar o servidor
Rodar o arquivo _servidor.py_ utilizando a sua IDE de preferência, ou através do comando:

```python server.py```

Após isso, o backend irá rodar na porta 5000.
