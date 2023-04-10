print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)
metros_uma_lata = 3
litros_de_uma_lata = 18
preço_uma_lata = 80
litros = metros_quadrados/metros_uma_lata
latas_inteiras = (litros/litros_de_uma_lata)
if litros%litros_de_uma_lata !=0:
    latas_inteiras +=1
# Coloque o código para resolver o problema nessa parte do programa

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = int(latas_inteiras)
valor_total = qtd_de_latas*preço_uma_lata

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")