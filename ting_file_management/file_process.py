from ting_file_management.file_management import txt_importer
import sys

def verify_file(instance, path_file):
    for i in instance:
        if i["nome_do_arquivo"] == path_file:
            return True
    return False

def process(path_file, instance):
    if verify_file(instance, path_file):
        return None
    
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    instance.enqueue(data)
    return sys.stdout.write(str(data))


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    path_file = instance.dequeue()
    print(f'Arquivo {path_file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        print(f'{path_file}')
    except IndexError:
        sys.stderr.write('Posição inválida')
