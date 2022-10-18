from dataclasses import fields
from rest_framework import serializers

from teacher.models import Professor, Aula

class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Professor
    fields = '__all__'
    # fields = ('id', 'nome', 'valor_hora', 'descricao', 'foto')

# POST /professores/1/aulas
# {
#   "email":"cleyson@gmail.com",
#   "nome": "Cleyson Lima"
# }

class CadastrarAulaSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  nome = serializers.CharField(max_length=100)


  class AulaSerializer(serializers.ModelSerializer):
    class Meta:
      model = Aula
      fields = '__all__'