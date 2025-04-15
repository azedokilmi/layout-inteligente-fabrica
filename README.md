# 🏭 Otimizador de Layout Fabril com Simulated Annealing

Este projeto em Python realiza a otimização do posicionamento de máquinas dentro de um ambiente fabril, com o objetivo de **minimizar o tempo total de produção**. A solução considera **tempo de processamento** e **tempo de deslocamento** entre máquinas, além de restrições físicas do layout e distância mínima entre os equipamentos. A visualização gráfica do antes e depois permite fácil comparação dos resultados.

---

## ⚙️ Como Funciona?

1. 📀 **Definição Inicial do Layout**

   - O usuário define:
     - Dimensões da fábrica (largura x comprimento)
     - Posições e tamanhos das máquinas
     - Tempo de processamento por máquina
     - Tempo de deslocamento por metro
   - O layout inicial é visualizado com setas indicando os fluxos e distâncias.

2. 🧊 **Algoritmo de Otimização**

   - É utilizado o algoritmo **Simulated Annealing**, que busca o melhor posicionamento possível das máquinas, respeitando:
     - Limites físicos da fábrica
     - Restrições de sobreposição entre máquinas
     - Distância mínima entre máquinas
   - A função objetivo considera o tempo total do processo: soma do tempo de processamento + tempo de deslocamento entre máquinas.

3. 📊 **Visualização Gráfica**

   - Dois gráficos são gerados:
     - Layout inicial, com tempo total antes da otimização
     - Layout otimizado, com novo tempo total
   - Os tempos são exibidos no canto superior esquerdo do gráfico.

---

## 🚀 Passo a Passo para Execução

1. **Instale o Python (3.8+)**

2. **Instale as bibliotecas necessárias:**

   ```bash
   pip install numpy matplotlib scipy
   ```

3. **Execute o programa**:

   No terminal (ou prompt de comando), navegue até a área de trabalho onde o arquivo `.py` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/layout-inteligente-fabrica/blob/main/layout-inteligente.py)) deve estar localizado e execute o comando abaixo:
   
   Após a execução do script, os arquivos de saída serão gerados na mesma pasta onde o programa foi executado.
   
   ```bash
   python layout-inteligente.py
   ```
   
   Após a execução, serão exibidos e salvos os gráficos com os tempos comparativos.
   Layout inicial (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/layout-inteligente-fabrica/blob/main/layout-inicial.png))
   Layout otimizado (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/layout-inteligente-fabrica/blob/main/layout-otimizado.png))

   ![Prévia do Programa em Execução](https://github.com/azedokilmi/layout-inteligente-fabrica/blob/main/preview-layouts.png)
---

## 🧠 Sobre o Algoritmo Simulated Annealing

O **Simulated Annealing** (ou "Recozimento Simulado") é um algoritmo inspirado no processo físico de recozimento térmico. Ele busca soluções otimizadas ao longo do tempo permitindo, ocasionalmente, aceitar piores soluções para escapar de mínimos locais, aumentando a chance de encontrar uma **solução globalmente ótima**.

Etapas principais:

- Começa com uma solução aleatória.
- Realiza pequenas alterações nela.
- Se a nova solução for melhor, é aceita.
- Se for pior, pode ser aceita com uma certa probabilidade, que diminui com o tempo (temperatura vai “esfriando”).

---

## 📂 O que é Gerado

- Gráfico do layout inicial com o tempo total antes da otimização.
- Gráfico do layout otimizado com o novo tempo total.
- Impressão no terminal dos tempos e do progresso da otimização.

---

## 💡 Ideias Futuras

- Exportar os resultados em PDF.
- Interface gráfica para entrada de dados.
- Inclusão de restrições específicas (setores obrigatórios, agrupamentos, etc.).
- Otimização considerando rotas de empilhadeiras e áreas de segurança.

---

## ✍️ Autor

Feito com dedicação por Pedro Cicilini de Nadai 💪\
GitHub: [@azedokilmi](https://github.com/azedokilmi)
