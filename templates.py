import os


def get_template_path(path):
    file_path=os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path")
    return file_path

def get_template(path):
    file_path=get_template_path(path)
    return open(file_path).read()

def render_context(template_string, context):
    return template_string.format(**context)

file_="F:\python programs\templates\email_mssg"
template=get_template(file_)
context={
    "name":"Justin",
    "date":None,
    "total":None
    }

print(render_context(template, context))





    








