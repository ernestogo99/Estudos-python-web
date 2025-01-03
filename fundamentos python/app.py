import os
# pylint: disable=all

restaurantes=[{'nome':'praça', 'categoria':'japonesa', 'ativo':False},{'nome':'pizza suprema', 'categoria':'italiana', 'ativo':True}]  

def exibir_nome_programa():
            
    print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

        



def voltar_ao_menu():
    input('digite uma tecla para voltar ao menu: ')
    main()


def finalizar_app():
    exibir_subtitulo('finalizado')

def exibir_opcoes():
    print("\n1. cadastrar restaurante")
    print("\n2. Listar restaurante")
    print("\n3. Ativar restaurante")
    print("\n4. Sair ")

def opcao_invalida():
    print('opção inválida\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
  
 
def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            estado = "ativado" if restaurante['ativo'] else "desativado"
            print(f"O restaurante {nome_restaurante} foi {estado} com sucesso.")
            break

    if not restaurante_encontrado:
        print("Restaurante não foi encontrado")
    voltar_ao_menu()  
        
        
def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de rastaurantes: ")
    nome=input("Digite o nome do restaurante: ")
    categoria=input(f"Digite a categoria do restaurante: {nome}: ")
    dados_restaurante={'nome':nome, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)  
    print(f'o restaurante {nome} foi cadastrado\n')
    voltar_ao_menu()
    
def listar_restaurante():
    exibir_subtitulo("-----RESTAURANTES-----")
    for restaurante in restaurantes:
        print(f"-{restaurante['nome']} | {restaurante['categoria']} | {restaurante['ativo']}")
    voltar_ao_menu()
        
def escolher_opcao():
    try:
        option=int(input("Digite uma opção: "))
        match option:
                case 1:
                    cadastrar_novo_restaurante()
                    
                case 2:
                    listar_restaurante()
                case 3:
                    alternar_estado_restaurante()
                case 4:
                    finalizar_app()
             
    except:
        opcao_invalida()
    
            
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
   


        

if __name__=='__main__':
    main()
    
    