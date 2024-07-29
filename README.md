# Restaurante

## Conceitos e ferramentas utilizados

BaseModel
FastAPI


Endpoints

Restaurante:
- POST /cardapio
- PUT /cardapio 
- DELETE /itemcardapio [OK]
- GET /pedidos: Retorna os pedidos solicitados
- PUT /pedido/status: seta o status do pedido
- GET /clientes: pega informações dos clientes [OK]
- GET /relatorio: pega informações de vendas
- DELETE user [OK] (verificar)
Clientes:
- GET /pedido
- POST /pedido
- POST /cliente [OK]
- PUT /cliente 
Em comum:
- GET /cardapio [OK]
- POST /login
- POST-GET /chat