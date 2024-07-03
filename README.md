# Como configurar/instalar/usar o `pdfunite` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `pdfunite` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install the `pdfunite` on `Linux Ubuntu`._


## Descrição [2]

### `pdfunite`

O `pdfunite` é uma ferramenta de linha de comando utilizada para mesclar múltiplos arquivos PDF em um único documento. Com essa ferramenta, os usuários podem combinar várias páginas ou documentos PDF de forma rápida e eficiente, facilitando a organização e compartilhamento de informações em um único arquivo PDF consolidado.


## 1. Como configurar/instalar/usar o `pdfunite` no `Linux Ubuntu` [1]

Para configurar/instalar/usar o `pdfunite` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    

### 1.1 Configurar/Instalar/usar o `pdfunite`

Para juntar dois arquivos PDF em um único no Linux, você pode usar várias ferramentas disponíveis na linha de comando. É possível usar o `pdfunite`, parte do pacote `poppler-utils`.

1. **Para instalar o `poppler-utils` (que inclui o `pdfunite`), use o seguinte comando:** Para sistemas baseados em Debian (como Ubuntu): `sudo apt install poppler-utils -y`


## 1.2 Juntar os arquivos `.pdf` com o `pdfunite`

1. **Para juntar os arquivos `.pdf`, use o comando:** `pdfunite arquivo1.pdf arquivo2.pdf arquivo_unido.pdf`

    Novamente, substitua `arquivo1.pdf` e `arquivo2.pdf` pelos nomes dos seus arquivos `.pdf` que deseja juntar, e `arquivo_unido.pdf` pelo nome que deseja dar ao arquivo PDF resultante.

## 1.2.1 Juntar muitos arquivos `.pdf` com o `pdfunite`

1. **Para juntar muitos arquivos `.pdf`, use o comando:** `pdfunite arquivo1.pdf arquivo2.pdf arquivo3.pdf arquivo_unido.pdf`

    Novamente, substitua `arquivo1.pdf`, `arquivo2.pdf` e `arquivo3.pdf` pelos nomes dos seus arquivos `.pdf` que deseja juntar, e `arquivo_unido.pdf` pelo nome que deseja dar ao arquivo `.pdf` resultante.

    1.1 Se você tiver uma lista grande de arquivos `.pdf` e eles estiverem nomeados de forma sequencial ou possuírem um padrão nos nomes, você pode até utilizar wildcards (coringas) ou outras técnicas de shell para especificar os arquivos de entrada. Por exemplo: `pdfunite arquivo*.pdf arquivo_unido.pdf`

    Esses comandos unirão todos os arquivos `.pdf` no diretório atual que correspondem ao padrão especificado (neste caso, todos os arquivos que começam com `"arquivo"` e terminam com `".pdf"`) em um único arquivo `.pdf`.


## 2. Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `pdfunite` no `Linux Ubuntu`sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt-get install poppler-utils -y
    ```


## Referências

[3] OPENAI. ***Unir arquivos pdf: pdftk vs. pdfunite:***. Disponível em: <https://chat.openai.com/c/592706f3-7b05-4cff-859e-c5b1727e4735> (texto adaptado). Acessado em: 19/02/2024 13:47.

[2] OPENAI. ***Vs code: editor popular***. Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 19/02/2024 13:48.


