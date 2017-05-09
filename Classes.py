import casa_rick_morty as casa


class Cenario:
	def __init__(self):
		self.imagem = casa
	
	def gravidade (self,direcao,sentido,intensidade):
		self.direcao=direcao
		self.sentido=sentido
		self.intensidade=intensidade


class caixa:
	def __init__(self,massa,tamanho,imagem):
		self.massa = massa
		self.tamanho = tamanho
		self.imagem = caixa

	def forca(self,direcao,sentido,intensidade):
		self.direcao=direcao
		self.sentido=sentido
		self.intensidade=intensidade


class rick:
	def __init__(self):
		self.massa = massa
		self.tamanho = tamanho
		self.imagem = rick 


class vetor:
	def __init__(self,direco,sentido,intensidade):
		self.intensidade = intensidade
		self.sentido = sentido
		self.direcao = direcao