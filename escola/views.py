from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerial, CursoSerial, MatriculaSerial, ListaMatriculasAlunoSerial, ListaAlunosMatriculadosSerial


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatricula(generics.ListAPIView):
    '''Listando os alunos e as alunas matriculados em um curso'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    