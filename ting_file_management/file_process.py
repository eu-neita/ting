from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        item = instance.search(i)
        if item['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)
    if lines is not None:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(data)
        print(data)


def remove(instance):
    removed_item = instance.dequeue()
    if removed_item is not None:
        print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso"
            )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result)
        return result
    except IndexError:
        import sys
        print("Posição inválida", file=sys.stderr)
