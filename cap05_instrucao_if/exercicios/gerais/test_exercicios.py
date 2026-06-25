import unittest
import sys
import os

# Tenta carregar 'exercicios.py'. Se houver falha ou se as funções retornarem None (ainda não implementadas),
# podemos alternar dinamicamente ou apenas deixar falhar para que o aluno veja o teste falhando.
try:
    import exercicios as ex
    # Se o arquivo estiver todo vazio ou não implementado, algumas verificações básicas podem ser feitas
except ImportError:
    print("Erro: Não foi possível importar o arquivo 'exercicios.py'.")
    sys.exit(1)

class TestExercicios(unittest.TestCase):
    def test_exercicio_01_maioridade(self):
        self.assertEqual(ex.exercicio_01_maioridade(18), "Maior de idade")
        self.assertEqual(ex.exercicio_01_maioridade(25), "Maior de idade")
        self.assertEqual(ex.exercicio_01_maioridade(17), "Menor de idade")
        self.assertEqual(ex.exercicio_01_maioridade(0), "Menor de idade")

    def test_exercicio_02_par_ou_impar(self):
        self.assertEqual(ex.exercicio_02_par_ou_impar(4), "Par")
        self.assertEqual(ex.exercicio_02_par_ou_impar(7), "Ímpar")
        self.assertEqual(ex.exercicio_02_par_ou_impar(0), "Par")
        self.assertEqual(ex.exercicio_02_par_ou_impar(-1), "Ímpar")

    def test_exercicio_03_triangulos(self):
        self.assertEqual(ex.exercicio_03_triangulos(3, 4, 5), "Escaleno")
        self.assertEqual(ex.exercicio_03_triangulos(5, 5, 5), "Equilátero")
        self.assertEqual(ex.exercicio_03_triangulos(5, 5, 8), "Isósceles")
        self.assertEqual(ex.exercicio_03_triangulos(10, 2, 2), "Não é um triângulo")
        self.assertEqual(ex.exercicio_03_triangulos(1, 2, 3), "Não é um triângulo")

    def test_exercicio_04_calculadora(self):
        self.assertEqual(ex.exercicio_04_calculadora(10, 5, "+"), 15.0)
        self.assertEqual(ex.exercicio_04_calculadora(10, 5, "-"), 5.0)
        self.assertEqual(ex.exercicio_04_calculadora(10, 5, "*"), 50.0)
        self.assertEqual(ex.exercicio_04_calculadora(10, 2, "/"), 5.0)
        self.assertEqual(ex.exercicio_04_calculadora(10, 0, "/"), "Erro: Divisão por Zero")
        self.assertEqual(ex.exercicio_04_calculadora(10, 5, "%"), "Operador Inválido")

    def test_exercicio_05_ano_bissexto(self):
        self.assertTrue(ex.exercicio_05_ano_bissexto(2020))
        self.assertFalse(ex.exercicio_05_ano_bissexto(2021))
        self.assertFalse(ex.exercicio_05_ano_bissexto(1900))
        self.assertTrue(ex.exercicio_05_ano_bissexto(2000))

    def test_exercicio_06_imc(self):
        self.assertEqual(ex.exercicio_06_imc(50, 1.70), "Abaixo do peso")
        self.assertEqual(ex.exercicio_06_imc(70, 1.75), "Peso normal")
        self.assertEqual(ex.exercicio_06_imc(85, 1.75), "Sobrepeso")
        self.assertEqual(ex.exercicio_06_imc(100, 1.70), "Obesidade")

    def test_exercicio_07_aprovacao_escolar(self):
        self.assertEqual(ex.exercicio_07_aprovacao_escolar(8, 7, 9), "Aprovado")
        self.assertEqual(ex.exercicio_07_aprovacao_escolar(6, 6, 6), "Recuperação")
        self.assertEqual(ex.exercicio_07_aprovacao_escolar(4, 3, 5), "Reprovado")

    def test_exercicio_08_desconto_compra(self):
        self.assertEqual(ex.exercicio_08_desconto_compra(600), (90.0, 510.0))
        self.assertEqual(ex.exercicio_08_desconto_compra(300), (30.0, 270.0))
        self.assertEqual(ex.exercicio_08_desconto_compra(150), (0.0, 150.0))
        self.assertEqual(ex.exercicio_08_desconto_compra(500), (50.0, 450.0))

    def test_exercicio_09_aprovacao_emprestimo(self):
        self.assertEqual(ex.exercicio_09_aprovacao_emprestimo(3000, 120000, 10), "Negado")
        self.assertEqual(ex.exercicio_09_aprovacao_emprestimo(3000, 120000, 20), "Aprovado")

    def test_exercicio_10_classificacao_clima(self):
        self.assertEqual(ex.exercicio_10_classificacao_clima(10), "Frio")
        self.assertEqual(ex.exercicio_10_classificacao_clima(20), "Agradável")
        self.assertEqual(ex.exercicio_10_classificacao_clima(30), "Quente")
        self.assertEqual(ex.exercicio_10_classificacao_clima(40), "Muito Quente")

if __name__ == '__main__':
    unittest.main()
