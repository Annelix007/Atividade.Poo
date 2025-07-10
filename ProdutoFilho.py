from Produto import Produto

       class Cigarro(Produto):
		
		def __init__(self, nome: str, preco: float, cpf_na_nota: str):
        super().__init__(nome, preco)
        cpf_valido = ' ' . join(filter(str.isdigit, cpf_na_nota))
        
        if len(cpf_valido) == 11:
        	self.cpf_na_nota = cpf_valido
        	
        else:
        	raise VelueErro (f"CPF invalido: '{cpf_na_nota}. Você não me engana! coloque o cpf com apenas números, 11 digitos viu -_-")
        
        def getcpf (self)-> str
             return self.cpf_na_nota 
             
         def nota_fiscal(self)-> str:
         	nota_p = super ( ).nota_fiscal
         	
         	nota_cigarro = nota_p.replace ("==================== , f"CPF na Nota:{self._cpf_na_nota}\n===============")
        return nota_cigarro 
        
        print("--- Detalhes do Produto ---")
print(f"Nome: {produto_exemplo.get_nome()}")
print(f"Preço: R$ {produto_exemplo.get_preco():.2f}")
print(f"CPF na Nota: {produto_exemplo.getcpf()}")
         	
