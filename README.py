#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `img2pdf` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `img2pdf` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `img2pdf` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `img2pdf`
# 
# O `img2pdf` é uma ferramenta de linha de comando para converter imagens em arquivos PDF no sistema Linux. Ele permite a criação de documentos PDF a partir de imagens em diversos formatos, como JPEG, PNG e TIFF. O `img2pdf` é eficiente e flexível, oferecendo opções para ajustar a qualidade, o tamanho e a disposição das imagens no PDF resultante. É uma ferramenta leve, ideal para usuários que precisam converter rapidamente imagens para PDF sem perder qualidade, e é particularmente útil para a criação de documentos digitais ou arquivos de apresentação a partir de imagens.
# 

# ## 1. Como configurar/instalar/usar o `img2pdf` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `img2pdf` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# ### 1.1 Configurar/Instalar/usar o `img2pdf`
# 
# Para juntar dois arquivos PDF em um único no `Linux Ubuntu`, você pode usar várias ferramentas disponíveis na linha de comando. É possível usar o `img2pdf`, parte do pacote `poppler-utils`.
# 
# 1. **Instale o `img2pdf`**: Agora, você pode instalar o pacote com o comando: `sudo apt install img2pdf`
# 
# 2. **Verifique a instalação**: Após a instalação, você pode verificar se o `img2pdf` foi instalado corretamente rodando o comando: `img2pdf --version`
# 
# Isso deve mostrar a versão do `img2pdf`, confirmando que ele foi instalado corretamente.
# 

# ## 1.2 Juntar os arquivos `.pdf` com o `img2pdf`
# 
# 1. **Para juntar os arquivos `.pdf`, use o comando:** `img2pdf arquivo1.jpg arquivo2.png -o output.pdf`
# 
#     Novamente, substitua `arquivo1.pdf` e `arquivo2.pdf` pelos nomes dos seus arquivos `.pdf` que deseja juntar, e `arquivo_unido.pdf` pelo nome que deseja dar ao arquivo PDF resultante.
# 
# ## 1.2.1 Juntar muitos arquivos `.pdf` com o `img2pdf`
# 
# 1. **Para juntar muitos arquivos `.pdf`, use o comando:** `img2pdf arquivo1.jpg arquivo2.png arquivo3.png -o output.pdf`
# 
#     Novamente, substitua `arquivo1.pdf`, `arquivo2.pdf` e `arquivo3.pdf` pelos nomes dos seus arquivos `.pdf` que deseja juntar, e `arquivo_unido.pdf` pelo nome que deseja dar ao arquivo `.pdf` resultante.
# 
#     1.1 Se você tiver uma lista grande de arquivos `.pdf` e eles estiverem nomeados de forma sequencial ou possuírem um padrão nos nomes, você pode até utilizar wildcards (coringas) ou outras técnicas de shell para especificar os arquivos de entrada. Por exemplo: `img2pdf arquivo*.pdf arquivo_unido.pdf`
# 
#     Esses comandos unirão todos os arquivos `.pdf` no diretório atual que correspondem ao padrão especificado (neste caso, todos os arquivos que começam com `"arquivo"` e terminam com `".pdf"`) em um único arquivo `.pdf`.
# 

# ## 2. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `img2pdf` no `Linux Ubuntu`sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt-get img2pdf -y
#     img2pdf --version
#     ```
# 

# ## Referências
# 
# [3] OPENAI. ***Unir arquivos pdf: pdftk vs. img2pdf:***. Disponível em: <https://chat.openai.com/c/592706f3-7b05-4cff-859e-c5b1727e4735> (texto adaptado). Acessado em: 19/02/2024 13:47.
# 
# [2] OPENAI. ***Vs code: editor popular***. Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 19/02/2024 13:48.
# 
# 
