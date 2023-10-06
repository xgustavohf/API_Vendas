# API_Vendas

Este código é uma bela implementação de uma API que se conecta a um banco de dados MySQL, busca informações de vendas de colaboradores e, com base em critérios específicos, gera mensagens personalizadas usando a plataforma GPT-3 da OpenAI.

A API foi desenvolvida usando o framework Flask, que é conhecido pela sua simplicidade e eficiência na criação de aplicativos web. Ela oferece dois endpoints principais:

1. Homepage (/): A página inicial da API exibe uma mensagem informando que a API está funcionando e um botão que redireciona para a página de vendas.

2. Página de Vendas (/vendas): Esta página é responsável por buscar dados de vendas de um banco de dados MySQL. Ela conecta-se ao banco de dados, executa uma consulta SQL e transforma os resultados em um DataFrame do Pandas para posterior processamento. Além disso, calcula o total de vendas para cada colaborador com base nos meses e, com base em metas pré-definidas, determina se o colaborador atingiu ou não sua meta de vendas. Isso é feito por meio de mensagens geradas pela API da OpenAI GPT-3, que fornece respostas personalizadas com base no status da meta de vendas.

Este código é uma excelente demonstração de como usar diversas bibliotecas e tecnologias, como Flask, Pandas, MySQL Connector e a API da OpenAI, para criar uma aplicação web que processa dados de vendas e gera mensagens dinâmicas com base em critérios específicos. É uma implementação elegante que pode ser útil para empresas que desejam acompanhar o desempenho de vendas de seus colaboradores e fornecer feedback personalizado.
