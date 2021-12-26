# Python - Flask - SqlAlchemy

> Backend implementado em Python para a disciplina de Desenvolvimento de Sistemas em Python_ do IFC Campus Blumenau.

## Diagrama de classes
As classes modeladas foram: 

**Pessoa**(nome, cpf, email),

**Disciplina**(nome, carga horária, ementa),

**EstudanteDaDisciplina**(semestre, pessoa, disciplina, mediaFinal, frequencia);

![diagrama-classes-ped](https://user-images.githubusercontent.com/50798315/147422186-46b93007-db8c-461b-b24f-f17e2dae90c3.png)

## Para testar

### Instalar as dependências
```python -m pip install -r requirements.txt```

### Iniciar o servidor
Rodar o arquivo _servidor.py_ utilizando a sua IDE de preferência, ou através do comando:

```python server.py```

Após isso, o backend irá rodar na porta 5000.
