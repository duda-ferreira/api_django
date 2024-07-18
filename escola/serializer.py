from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerial(serializers.ModelSerializer):
    class Meta:
        #tabela:
        model = Aluno
        #campos:
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento'] 

class CursoSerial(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__'

class MatriculaSerial(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasAlunoSerial(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerial(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='aluno.nome')
    
    class Meta:
        model = Matricula
        fields = ['nome']
