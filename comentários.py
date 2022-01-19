'''

                        Resumo NEW_SAM
• Dados de entrada:
    o Cliente;
    o Data a ser analisada (Não precisa, mas é bom pra controlar erros);
    o Query SQL que retorna t_fatura_base (Tabela com informação das faturas não-saneadas);
    o Query SQL que retorna id_ged (Usado para buscar o PDF no Raven).

• SQL: Coleta tabela de informações das faturas não-saneadas do TWM usando conta 
aglutinada e data de vencimento (Usar o Identificar é inviável pois a Identificador no 
Raven geralmente está errado, isso é um problema de Parser);

• Loop SQL: Itera sobre as linhas da tabela do  SQL cada fatura por vez do período 
escolhido, se a fatura não existir no Raven informa o erro e não realiza os procedimentos;

• NOSQL: Executa query pela conta aglutinada e data de vencimento que é gerada no SQL;

• Compara o Valor_total da fatura com a soma dos valores de auditoria (Pra isso são
tratadas as Strings na função def_str_to_float);

x Se o valor estiver errado é preciso criar um modo de verificação (tela estilo cara-crachá);

x É preciso criar a mesma validação para o consumo, mas ainda está difícil de encontrar 
um padrão pois o Parser erra muito;

• Se estiver correto é coletado o Json do Raven;

• Depois o arquivo PDF do GED é coletado usando a chave da fatura que é fornecida pelo 
SQL;

x Caso a fatura não esteja Parseada no Raven é preciso enviar o arquivo para o Doc Parser 
usando o import DocParser e retornar o Json parseado, este deve entrar no fluxo da mesma 
forma que o Json saindo do Raven (o código está preparado para fazer isso mas ainda não 
consegue-se coletar o PDF do GED, apenas é retornado um Objeto que precisa ser 
“binárizado” para PDF;

• Extra*Uma função def_linkado_excel foi usada para organizar os arquivos “consolidado”
e “linkado” em formato de lista e dicionário. python (os arquivos foram disponibilizados 
pela equipe de consultoria de BH e são padrões utilizados no Dashboard); *Não impacta 
diretamente no funcionamento do código, mas está lá para ser usado caso haja 
modificações bruscas ou entrada de um novo cliente, pois como não estão padronizadas 
é necessário criar uma relação para cada cliente;

• A função def_linkado_excel gera no terminal os índices das colunas e das comparações 
a serem feitas, no início da def_parser_to_col_consolidado são fixadas (Copia e cola) no 
código em formato de listas;

• As listas contêm como está a escrita do nome da coluna no Doc Parser, como está a escrita 
no Dashboard e qual a conexão entre ambas (Ex: no Doc Parser ‘Dc_identificador_conta’
significa ‘Nº da conta’ no Dashboard);

• As listas são conectadas através de dicionários no Python (igual Json) que informam as 
Keys = Palavra no Doc Parser e os Values = Palavra no Dashboard;

• De acordo com qual cliente está sendo analisado, o dicionário criado é comparado com 
os dados Parseados no Raven da fatura, e cria-se o consolidado com as informações;

• Cada campo que não for encontrado na relação entre o dicionário e o arquivo do Doc 
Parser é procurado no banco SQL (isso acontece, pois, alguns campos precisam ser 
coletados no TWM, como localidade, AVB, nota fiscal, etc.);

• Então é gerado um Json (dicionário Python) completo contendo os campos usados no 
Dashboard e as informações referentes ao Parseamento (são as informações prontas pra 
serem usadas no Sheets do Dashboard);

x Esse Json precisa ser armazenado no banco do Raven para segurança das informações;

• A def_parser_to_json transforma o Json do arquivo consolidado em formato de 
DataFrame no Pandas e salva um arquivo em Excel dentro da pasta do código (Esse é o 
arquivo usado para copiar e colar os dados no Sheets do Dashboard);

• Encerramento do código. 

x Após ser testado e tiver com a estrutura de falhas funcionando é preciso enviar o Excel 
diretamente para o Sheets (Sugestão: Usar um Sheets separado dentro do Drive de 
saneamento e copiar e colar para o Sheets do Dashboard, isso pois são feitas diversas 
alterações no Sheets que podem impactar o funcionamento do código, depois de um 
tempo sendo validado pode ser enviado diretamente);

• *Extra: Existe uma def_string_to_float que deve ser usada sempre que forem calculados 
valores inteiros ou de ponto flutuante, pois geralmente são encontrados valores usando 
ponto como separador decimal, mas o padrão do python é usar vírgula, então essa função 
normaliza os números para evitar erro








'''