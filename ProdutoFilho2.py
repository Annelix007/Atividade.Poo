from Produto import Produto

class Arroz(Produto):
    def __init__(self, nome: str, preco: float, Kg_na_nota):
        super().__init__(nome, preco)

        try:
            kg_valido = float(Kg_na_nota)

            if kg_valido > 0:
                self._Kg_na_nota = kg_valido
            else:
                raise ValueError(f"Kg na nota inválido: '{Kg_na_nota}'. Coloca um peso real, rapaz.")
        except (ValueError, TypeError):
            raise ValueError(f"Coloca um peso válido, faz favor: '{Kg_na_nota}'. Coloca uma coisa mais real, tipo um 5 kilos.")

    def get_kg_na_nota(self):
        return self._Kg_na_nota

    def nota_fiscal(self) -> str:
        nota_p = super().nota_fiscal()
        nota_arroz = nota_p.replace(
            "=====================", f"Kg na Nota: {self._Kg_na_nota} Kg\n====================="
        )
        return nota_arroz
               
      print("--- Detalhes do Produto (Arroz Válido - Inteiro) ---")
print(f"Nome: {arroz_valido_int.get_nome()}")
print(f"Preço: R$ {arroz_valido_int.get_preco():.2f}")
print(f"Kg na Nota: {arroz_valido_int.get_kg_na_nota()} Kg")
print("\n--- Nota Fiscal Completa (Arroz Válido - Inteiro) ---")
print(arroz_valido_int.nota_fiscal())
