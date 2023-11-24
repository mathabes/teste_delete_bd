import cx_Oracle

def delete_bd(tp_conta: str, dado: str):
        if tp_conta == 'usuario':
            consulta_id_conta = f'''SELECT fk_id_conta FROM t_hn_email WHERE ds_email = '{dado}' '''

            inst_consulta.execute(consulta_id_conta)
            id_conta = inst_consulta.fetchone()[0]

            deletar_usuario = f'''DELETE FROM t_hn_usuario WHERE fk_id_conta = {id_conta}'''
            inst_exclusao.execute(deletar_usuario)
            conn.commit

# Conectando com o banco de dados
try:
    # Conecta o servidor
    dsnStr = cx_Oracle.makedsn("oracle.fiap.com.br", "1521",
                               "ORCL")
    # Efetua a conexão com o Usuário
    conn = cx_Oracle.connect(user='RM98502', password="090405",
                             dsn=dsnStr)
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    # Informa o erro
    print(f"\033[031mErro: {e}\033[m\n")
    # Flag para não executar a Aplicação
    conexao = False
else:
    print('Conexão funcionando.')

delete_bd('usuario', 'daqui@')